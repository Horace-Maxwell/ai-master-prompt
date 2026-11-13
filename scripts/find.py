#!/usr/bin/env python3
"""Search the resource index by keyword(s). Works from any directory.

- All keywords must match (AND). If nothing matches all of them, partial
  matches are shown instead, best first. A quoted phrase is split on spaces.
- Chinese and English synonyms are expanded from data/aliases.json
  (玻璃 = glass, 脚手架 = starter, 爬虫 = crawler ...).
- Results are ranked: tags > name > stack > install command > description,
  with ⭐ picks first among equals. A match on the category title alone is
  only shown when there are few direct matches.
- The hand-written effect vocabulary and style recipes (ui/prompts/*.md) are
  searched too, so effect names like 磁吸 / parallax are found.
- The full official shadcn registry index (data/registries.json, 500+ namespaces)
  is searched as well and shown after the curated results.

Usage:
  python3 scripts/find.py 手绘
  python3 scripts/find.py motion react
  python3 scripts/find.py mcp --module ui
  python3 scripts/find.py --category ui-animated
  python3 scripts/find.py shadcn --json
  python3 scripts/find.py --category stack-services --group 认证
  python3 scripts/find.py 数据库 --stars     # only ⭐ picks
  python3 scripts/find.py --list            # list modules and categories
(Windows: use `python` or `py -3` instead of `python3`.)
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
from pathlib import Path

from _data import DATA, is_command, load_categories, load_resources

ROOT = Path(__file__).resolve().parent.parent
FIELD_WEIGHT = (("tags", 6), ("name", 5), ("stack", 3), ("ai", 2), ("desc", 2))
CAT_WEIGHT = 1
MIN_DIRECT = 3  # show category-title-only matches when fewer direct matches than this


def load_aliases() -> dict[str, set[str]]:
    path = DATA / "aliases.json"
    table: dict[str, set[str]] = {}
    if path.exists():
        for group in json.loads(path.read_text("utf-8")):
            low = {a.lower() for a in group}
            for a in low:
                table.setdefault(a, set()).update(low - {a})
    return table


def word_hit(word: str, text: str) -> bool:
    """ASCII terms match at a word start (icon -> icons, not 'silicon'); CJK by substring."""
    if word.isascii():
        return re.search(r"(?<![a-z0-9])" + re.escape(word), text) is not None
    return word in text


def kw_hit(kw: str, text: str) -> bool:
    """What the user typed: substring, except very short ASCII (rn, ai, 3d) needs a word start."""
    if kw.isascii() and len(kw) <= 3:
        return word_hit(kw, text)
    return kw in text


def matches(kw: str, alts, text: str) -> bool:
    return kw_hit(kw, text) or any(word_hit(a, text) for a in alts)


def score_keyword(kw: str, alts: set[str], fields: dict[str, str]) -> tuple[int, bool]:
    """Returns (score, direct). direct=False means only the category title matched."""
    best = 0
    for name, weight in FIELD_WEIGHT:
        text = fields[name]
        if kw_hit(kw, text):
            best = max(best, weight + 1)
        elif any(word_hit(a, text) for a in alts):
            best = max(best, weight)
    if best:
        return best, True
    return (CAT_WEIGHT, False) if matches(kw, alts, fields["cat"]) else (0, False)


def fields_of(r: dict, cat: dict) -> dict[str, str]:
    return {
        "name": r.get("name", "").lower(),
        "tags": " ".join(r.get("tags", []) + [r.get("price", ""), r.get("group", "")]).lower(),
        "cat": f"{r.get('category', '')} {cat.get('title', '')}".lower(),
        "stack": " ".join(r.get("stack", [])).lower(),
        "ai": r.get("ai", "").lower(),
        "desc": r.get("desc", "").lower(),
    }


def search_resources(kws, aliases, res, cats, module, category, group=None, stars=False):
    scored = []
    for r in res:
        if r.get("alias_of"):
            continue  # cross-listed copy of another entry
        if stars and not r.get("star"):
            continue
        if group and group.lower() not in r.get("group", "").lower():
            continue
        cat = cats.get(r["category"], {})
        if module and cat.get("module") != module:
            continue
        if category and r["category"] != category:
            continue
        f = fields_of(r, cat)
        per = [score_keyword(k, aliases.get(k, set()), f) for k in kws]
        matched = sum(1 for s, _ in per if s)
        direct = all(d for s, d in per if s)
        scored.append((matched, sum(s for s, _ in per) + (2 if r.get("star") else 0), direct, r, cat))
    rank = lambda s: (-s[0], -s[1], s[3]["name"].lower())  # noqa: E731
    full = sorted((s for s in scored if s[0] == len(kws)), key=rank)
    if kws:
        strong = [s for s in full if s[2]]
        full = strong if len(strong) >= MIN_DIRECT else strong + [s for s in full if not s[2]]
    partial = sorted((s for s in scored if 0 < s[0] < len(kws)), key=rank) if not full else []
    return full, partial


def search_prompts(kws: list[str], aliases: dict[str, set[str]], need: int | None = None) -> list[tuple[str, str]]:
    """Named effects (table rows) and style recipes (headings) from ui/prompts/."""
    need = len(kws) if need is None else need
    out = []
    for name, keep in (("effect-vocabulary.md", "| "), ("style-recipes.md", "## ")):
        f = ROOT / "ui" / "prompts" / name
        if not f.exists():
            continue
        for i, line in enumerate(f.read_text("utf-8").splitlines(), 1):
            if not line.startswith(keep) or line.startswith(("|---", "| 名称")):
                continue
            low = line.lower()
            n = sum(1 for k in kws if matches(k, aliases.get(k, ()), low))
            if n >= need and n:
                text = line.strip().strip("|#").replace(" | ", " · ").strip()
                out.append((n, f"{f.relative_to(ROOT)}:{i}", text[:150]))
    out.sort(key=lambda t: -t[0])
    return [(loc, text) for _, loc, text in out]


def search_registries(kws: list[str], aliases: dict[str, set[str]], res: list[dict]) -> list[dict]:
    """Namespaces in the official shadcn index that the curated catalog does not already cover."""
    path = DATA / "registries.json"
    if not path.exists() or not kws:
        return []
    covered = set()
    for r in res:
        covered.update(re.findall(r"(@[a-z0-9][a-z0-9-]*)/", r.get("ai", "")))
    hits = []
    for x in json.loads(path.read_text("utf-8"))["registries"]:
        if x["name"] in covered or x.get("hidden"):
            continue
        text = f"{x['name']} {x.get('desc', '')}".lower()
        if all(matches(k, aliases.get(k, ()), text) for k in kws):
            hits.append(x)
    return hits  # already sorted by official ranking


def bigrams(kws: list[str]) -> list[str]:
    """字母乱跳 -> 字母, 母乱, 乱跳. Fallback for natural Chinese phrasing."""
    out = []
    for k in kws:
        if not k.isascii() and len(k) > 2:
            out += [k[i : i + 2] for i in range(len(k) - 1)]
        else:
            out.append(k)
    return list(dict.fromkeys(out))


def print_entry(r: dict, cat: dict) -> None:
    star = "⭐" if r.get("star") else "  "
    print(f"{star} {r['name']}  —  {r['url']}")
    where = cat.get("title", r["category"]) + (f" › {r['group']}" if r.get("group") else "")
    print(f"     [{where}] {r['desc']}")
    if r.get("ai"):
        label = "$" if is_command(r["ai"]) else "AI:"
        print(f"     {label} {r['ai']}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Search AI Master Prompt resources.")
    ap.add_argument("keywords", nargs="*")
    ap.add_argument("--module", help="ui | skills | tools | scaffolds")
    ap.add_argument("--category", help="category id (see --list)")
    ap.add_argument("--group", help="sub-group inside a category (substring match, e.g. 认证)")
    ap.add_argument("--stars", action="store_true", help="only ⭐ picks")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--list", action="store_true", help="list modules and categories, then exit")
    a = ap.parse_args()

    cats = {c["id"]: c for c in load_categories()}
    res = load_resources()

    if a.list:
        count: dict[str, int] = {}
        for r in res:
            count[r["category"]] = count.get(r["category"], 0) + 1
        module = None
        for c in cats.values():
            if c["module"] != module:
                module = c["module"]
                print(f"\n{module}/")
            print(f"  {c['id']:<22} {count.get(c['id'], 0):>3}  {c['title']}  →  {c['file']}")
        return

    kws = [w for k in a.keywords for w in k.lower().split()]  # "glass mobile" == glass mobile
    if not kws and not (a.module or a.category or a.group or a.stars):
        ap.print_help()
        return

    aliases = load_aliases()
    full, partial = search_resources(kws, aliases, res, cats, a.module, a.category, a.group, a.stars)
    vocab = [] if (a.module or a.category or a.group or a.stars or not kws) else search_prompts(kws, aliases)

    note = ""
    if not full and partial:
        note = f"没有同时匹配 {' + '.join(kws)} 的条目，以下是部分匹配（按相关度）：\n"
    if not full and not partial and not vocab:
        loose = bigrams(kws)
        if loose != kws:  # natural Chinese phrasing: retry on two-character pieces
            f2, p2 = search_resources(loose, aliases, res, cats, a.module, a.category, a.group, a.stars)
            partial = f2 or p2
            vocab = search_prompts(loose, aliases, need=max(1, len(loose) // 2))
            if partial or vocab:
                note = f"没有精确匹配，按「{' / '.join(loose)}」放宽搜索：\n"
                partial = partial[:5]

    shown = (full or partial)[: a.limit]
    if a.json:
        clean = [{k: v for k, v in s[3].items() if not k.startswith("_")} for s in shown]
        print(json.dumps(clean, ensure_ascii=False, indent=2))
        return

    regs = [] if (a.category or a.group or a.stars or a.module not in (None, "ui") or a.json) else search_registries(kws, aliases, res)
    if not shown and not vocab and not regs:
        words = set()
        for r in res:
            words.update(w for w in re.split(r"[^a-z0-9.+-]+", r["name"].lower()) if len(w) > 3)
            words.update(t.lower() for t in r.get("tags", []) if len(t) > 3)
        hints = []
        for k in kws:
            hints += difflib.get_close_matches(k, words, n=3, cutoff=0.75)
        print("没有找到。" + (f"你是不是想找：{', '.join(dict.fromkeys(hints))}？" if hints else ""))
        print("试试更少或更宽泛的关键词，或运行 `python3 scripts/find.py --list` 看全部分类。")
        return

    if note:
        print(note)
    for _, _, _, r, cat in shown:
        print_entry(r, cat)
    if vocab:
        print("\n📖 词汇表 / 风格配方命中：")
        for loc, line in vocab[:8]:
            print(f"   {loc}  {line}")

    if regs:
        print(f"\n📦 shadcn 官方索引里还有 {len(regs)} 个相关 registry（未精选，说明为作者原文）：")
        for x in regs[:6]:
            print(f"   {x['name']:<22} {x.get('items') or '?':>5} 项  {x.get('desc', '')[:90]}")
        print("   安装：npx shadcn@latest list <命名空间>  →  npx shadcn@latest add <命名空间>/<条目>"
              + ("；全部见 ui/catalog/18-shadcn-registries.md" if len(regs) > 6 else ""))

    total = len(full or partial)
    more = f"（共 {total} 条，只显示前 {len(shown)} 条，加 --limit {total} 看全部）" if total > len(shown) else ""
    print(f"\n{len(shown)} 条资源，{len(vocab)} 条词汇。{more}")


if __name__ == "__main__":
    main()
