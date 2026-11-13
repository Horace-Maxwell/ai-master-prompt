#!/usr/bin/env python3
"""Merge a JSON array of new entries into data/resources/, safely.

For bulk additions (for example a list an AI researched). It:
  - skips entries whose URL or name is already in the catalog (or repeated in the batch)
  - rejects entries with missing fields, unknown category, bad price or unknown group
  - renames colliding ids (adds -2, -3 ...)
  - normalises `npx shadcn add` to `npx shadcn@latest add`
  - caps ⭐ per category/group with --max-stars (extra stars are dropped, entry is kept)
  - appends each accepted entry to the data file that already holds its category
    (or data/resources/<module>-extra.json for a brand-new category)

Usage:
  python3 scripts/import_batch.py batch.json [more.json ...] [--dry-run] [--max-stars 4]
Then: python3 scripts/build.py --fmt && python3 scripts/build.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

from _data import DATA, load_categories, load_resources

PRICES = {"free", "freemium", "paid", "oss"}
ALLOWED = {"id", "name", "url", "category", "star", "desc", "stack", "ai", "price", "tags", "group", "order", "alias_of"}
# Where a category's entries live when no existing entry tells us.
DEFAULT_FILE = {
    "ui-frameworks-other": "ui-frameworks.json", "ui-css-kits": "ui-frameworks.json", "ui-native": "ui-frameworks.json",
    "ui-china": "ui-china-design-systems.json", "ui-design-systems": "ui-china-design-systems.json",
    "ui-functional": "ui-functional-templates.json", "ui-templates": "ui-functional-templates.json",
    "ui-media-assets": "ui-media-assets.json",
    "stack-services": "stack-services.json", "stack-content": "stack-services.json",
    "stack-ai": "stack-ai.json", "stack-libs": "stack-libs.json",
    "mcp-directories": "mcp.json", "mcp-servers": "mcp.json",
    "rules-prompts": "rules-ai-tools.json", "tools-ai-builders": "rules-ai-tools.json", "skills-more": "skills-more.json",
}


def url_key(url: str) -> str:
    """Same site + path => same resource, ignoring scheme, www, trailing slash, query and case."""
    sp = urlsplit(url.strip())
    host = sp.netloc.lower().removeprefix("www.")
    return host + sp.path.rstrip("/").lower()


def name_key(name: str) -> str:
    return re.sub(r"[\W_]+", "", name.lower())


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    max_stars = int(sys.argv[sys.argv.index("--max-stars") + 1]) if "--max-stars" in sys.argv else 4
    if "--max-stars" in sys.argv:
        args.remove(str(max_stars))
    if not args:
        print(__doc__)
        return 1

    cats = {c["id"]: c for c in load_categories()}
    existing = load_resources()
    ids = {r["id"] for r in existing}
    urls = {url_key(r["url"]) for r in existing if r["url"].startswith("http")}
    names = {name_key(r["name"]) for r in existing}
    file_of: dict[str, str] = {}
    for r in existing:
        file_of.setdefault(r["category"], r["_file"])
    stars = Counter((r["category"], r.get("group", "")) for r in existing if r.get("star"))

    accepted: dict[str, list[dict]] = defaultdict(list)
    stats: Counter = Counter()
    problems: list[str] = []
    for path in args:
        try:
            batch = json.loads(Path(path).read_text("utf-8"))
        except Exception as e:  # noqa: BLE001
            problems.append(f"{path}: cannot read ({e})")
            continue
        for i, e in enumerate(batch):
            label = f"{Path(path).name}#{i} {e.get('id', '?')}"
            miss = [k for k in ("id", "name", "url", "category", "desc") if not e.get(k)]
            if miss:
                problems.append(f"{label}: missing {miss}")
                stats["rejected"] += 1
                continue
            cat = cats.get(e["category"])
            if not cat:
                problems.append(f"{label}: unknown category {e['category']}")
                stats["rejected"] += 1
                continue
            if not str(e["url"]).startswith("http"):
                problems.append(f"{label}: url must be http(s)")
                stats["rejected"] += 1
                continue
            # several skills can live in one repo, so skills are matched by name only
            same_url = url_key(e["url"]) in urls and not e["category"].startswith("skills-")
            if same_url or name_key(e["name"]) in names:
                stats["duplicate"] += 1
                continue
            e = {k: v for k, v in e.items() if k in ALLOWED}
            if e.get("price") not in PRICES:
                e.pop("price", None)
            groups = cat.get("groups")
            if groups and e.get("group") not in groups:
                if e.get("group"):
                    problems.append(f"{label}: unknown group '{e['group']}' (kept, shown under 其他)")
                e.pop("group", None)
            if not groups:
                e.pop("group", None)
            e["id"] = re.sub(r"[^a-z0-9]+", "-", str(e["id"]).lower()).strip("-")
            base, n = e["id"], 2
            while e["id"] in ids:
                e["id"] = f"{base}-{n}"
                n += 1
            if e.get("ai"):
                e["ai"] = re.sub(r"npx shadcn add ", "npx shadcn@latest add ", e["ai"]).strip()
            if e.get("star"):
                key = (e["category"], e.get("group", ""))
                if stars[key] >= max_stars:
                    e.pop("star")
                    stats["star dropped"] += 1
                else:
                    stars[key] += 1
            else:
                e.pop("star", None)
            ids.add(e["id"])
            urls.add(url_key(e["url"]))
            names.add(name_key(e["name"]))
            target = file_of.get(e["category"]) or DEFAULT_FILE.get(e["category"]) or f"{cat['module']}-extra.json"
            accepted[target].append(e)
            stats["added"] += 1
            stats[f"  {e['category']}"] += 1

    for p in problems[:40]:
        print("!", p)
    for k, v in sorted(stats.items(), key=lambda kv: (kv[0].startswith("  "), kv[0])):
        print(f"{k}: {v}")
    if dry:
        print("(dry run, nothing written)")
        return 0
    for fname, items in accepted.items():
        f = DATA / "resources" / fname
        cur = json.loads(f.read_text("utf-8")) if f.exists() else []
        f.write_text(json.dumps(cur + items, ensure_ascii=False), "utf-8")
    print("written. Now run: python3 scripts/build.py --fmt && python3 scripts/build.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
