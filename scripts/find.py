#!/usr/bin/env python3
"""Search the resource index by keyword(s). All keywords must match (AND).

Matches against name, description, category, stack, tags and AI-install text.

Usage:
  python3 scripts/find.py motion react
  python3 scripts/find.py 手绘
  python3 scripts/find.py mcp --module ui
  python3 scripts/find.py --category ui-animated
  python3 scripts/find.py shadcn --json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _data import load_categories, load_resources

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("keywords", nargs="*")
    ap.add_argument("--module", help="ui | skills | tools | scaffolds")
    ap.add_argument("--category", help="category id, see data/categories.json")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--limit", type=int, default=40)
    a = ap.parse_args()

    cats = {c["id"]: c for c in load_categories()}
    res = load_resources()

    kws = [k.lower() for k in a.keywords]
    hits = []
    for r in res:
        cat = cats.get(r["category"], {})
        if a.module and cat.get("module") != a.module:
            continue
        if a.category and r["category"] != a.category:
            continue
        hay = " ".join(
            [
                r.get("name", ""),
                r.get("desc", ""),
                r.get("category", ""),
                cat.get("title", ""),
                r.get("ai", ""),
                " ".join(r.get("stack", [])),
                " ".join(r.get("tags", [])),
            ]
        ).lower()
        if all(k in hay for k in kws):
            hits.append((not r.get("star"), r, cat))

    hits.sort(key=lambda t: (t[0], t[1]["name"].lower()))
    hits = hits[: a.limit]

    if a.json:
        print(json.dumps([h[1] for h in hits], ensure_ascii=False, indent=2))
        return
    for _, r, cat in hits:
        star = "⭐" if r.get("star") else "  "
        print(f"{star} {r['name']}  —  {r['url']}")
        print(f"     [{cat.get('title', r['category'])}] {r['desc']}")
        if r.get("ai"):
            print(f"     AI: {r['ai']}")

    # Also search the hand-written vocabulary / recipes (effect names, styles)
    vocab = [] if (a.module or a.category or not kws) else search_prompts(kws)
    if vocab:
        print("\n📖 词汇表 / 风格配方命中：")
        for loc, line in vocab[:10]:
            print(f"   {loc}  {line}")

    if not hits and not vocab:
        print("No match. Try fewer / broader keywords, or browse INDEX.md.")
        return
    print(f"\n{len(hits)} resource(s), {len(vocab)} vocabulary line(s).")


def search_prompts(kws: list[str]) -> list[tuple[str, str]]:
    out = []
    for f in sorted((ROOT / "ui" / "prompts").glob("*.md")):
        for i, line in enumerate(f.read_text("utf-8").splitlines(), 1):
            if line.startswith(("|---", "> ")) or not line.strip():
                continue
            if all(k in line.lower() for k in kws):
                text = line.strip().strip("|").replace(" | ", " · ").strip()
                out.append((f"{f.relative_to(ROOT)}:{i}", text[:140]))
    return out


if __name__ == "__main__":
    main()
