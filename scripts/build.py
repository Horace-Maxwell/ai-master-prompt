#!/usr/bin/env python3
"""Generate catalog Markdown from data/*.json.

Single source of truth:
  data/categories.json  -> category id, module, title, output file, intro
  data/resources/*.json -> every resource (one object per entry, merged)

Usage:
  python3 scripts/build.py          # regenerate all catalog files + INDEX.md
  python3 scripts/build.py --check  # validate data only, write nothing
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

from _data import load_categories, load_resources

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

REQUIRED = ("id", "name", "url", "category", "desc")
PRICE_LABEL = {"free": "免费", "freemium": "免费+付费", "paid": "付费", "oss": "开源"}


def load() -> tuple[list[dict], list[dict]]:
    return load_categories(), load_resources()


def validate(cats: list[dict], res: list[dict]) -> list[str]:
    errs: list[str] = []
    cat_ids = {c["id"] for c in cats}
    seen: set[str] = set()
    for i, r in enumerate(res):
        for k in REQUIRED:
            if not r.get(k):
                errs.append(f"#{i} {r.get('id', '?')}: missing '{k}'")
        if r.get("id") in seen:
            errs.append(f"duplicate id: {r['id']}")
        seen.add(r.get("id"))
        if r.get("category") not in cat_ids:
            errs.append(f"{r.get('id')}: unknown category '{r.get('category')}'")
        if not str(r.get("url", "")).startswith(("http", "./")):
            errs.append(f"{r.get('id')}: url must start with http or ./ (local path)")
    return errs


def cell(text: str | None) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def render_entry_row(r: dict) -> str:
    name = f"[{cell(r['name'])}]({r['url']})"
    if r.get("star"):
        name = "⭐ " + name
    ai = cell(r.get("ai"))
    if ai:
        ai = f"`{ai}`" if "`" not in ai else ai
    stack = cell(", ".join(r.get("stack", [])))
    price = PRICE_LABEL.get(r.get("price", ""), cell(r.get("price")))
    return f"| {name} | {cell(r['desc'])} | {stack} | {ai} | {price} |"


def render_category(cat: dict, items: list[dict]) -> str:
    items = sorted(items, key=lambda r: (not r.get("star"), r["name"].lower()))
    out = [f"## {cat['title']}", ""]
    if cat.get("intro"):
        out += [cat["intro"], ""]
    out += [
        "| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |",
        "|---|---|---|---|---|",
    ]
    out += [render_entry_row(r) for r in items]
    out.append("")
    return "\n".join(out)


def build(cats: list[dict], res: list[dict]) -> list[Path]:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for r in res:
        by_cat[r["category"]].append(r)

    by_file: dict[str, list[dict]] = defaultdict(list)
    for c in cats:
        by_file[c["file"]].append(c)

    written: list[Path] = []
    for file, file_cats in by_file.items():
        path = ROOT / file
        path.parent.mkdir(parents=True, exist_ok=True)
        head = file_cats[0].get("file_title") or path.stem
        parts = [
            f"# {head}",
            "",
            "> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；"
            "要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。",
            "",
        ]
        for c in file_cats:
            parts.append(render_category(c, by_cat.get(c["id"], [])))
        path.write_text("\n".join(parts), "utf-8")
        written.append(path)

    # Global index: one line per category with counts
    idx = [
        "# 资源总索引（自动生成）",
        "",
        f"共 {len(res)} 条资源，{len(cats)} 个分类。按模块列出，点击进入分类文件。",
        "也可以用 `python3 scripts/find.py <关键词>` 直接搜索。",
        "",
    ]
    module = None
    for c in cats:
        if c["module"] != module:
            module = c["module"]
            idx += ["", f"## {module}/", ""]
        n = len(by_cat.get(c["id"], []))
        idx.append(f"- [{c['title']}]({c['file']}) — {n} 条")
    (ROOT / "INDEX.md").write_text("\n".join(idx) + "\n", "utf-8")
    written.append(ROOT / "INDEX.md")
    return written


MODULE_LABEL = {
    "ui": ("ui/", "UI 组件 · 特效 · 动效词汇 · 设计 Skill · 灵感 · 素材 · MCP", "ui/SKILL.md"),
    "skills": ("skills/", "Agent Skills 排行与精选", "skills/README.md"),
    "tools": ("tools/", "开源工具（采集 / 浏览器自动化）", "tools/README.md"),
    "scaffolds": ("scaffolds/", "脚手架 · Agent 框架 · MCP 模板 · 架构 · 元列表", "scaffolds/README.md"),
}


def badge(label: str, value: str, color: str = "F5A524") -> str:
    from urllib.parse import quote

    v = quote(value.replace("-", "--"))
    l = quote(label.replace("-", "--"))
    return (
        f'<img src="https://img.shields.io/badge/{l}-{v}-{color}?style=flat-square&labelColor=1C1916" '
        f'alt="{label}: {value}">'
    )


def replace_block(text: str, name: str, body: str) -> str:
    start, end = f"<!-- AUTO:{name} -->", f"<!-- /AUTO:{name} -->"
    if start not in text:
        return text
    a = text.index(start) + len(start)
    b = text.index(end)
    return text[:a] + "\n" + body + "\n" + text[b:]


def update_readme(cats: list[dict], res: list[dict]) -> None:
    path = ROOT / "README.md"
    if not path.exists():
        return
    t = path.read_text("utf-8")
    cat_mod = {c["id"]: c["module"] for c in cats}
    n_star = sum(1 for r in res if r.get("star"))
    n_ai = sum(1 for r in res if r.get("ai"))
    badges = " ".join(
        [
            badge("resources", str(len(res))),
            badge("categories", str(len(cats))),
            badge("⭐ picks", str(n_star)),
            badge("install commands", str(n_ai)),
            badge("verified", "2026-11-09", "9BC27D"),
            badge("deps", "python3 only", "8C857A"),
        ]
    )
    rows = ["| 模块 | 内容 | 条目 | 分类 | 入口 |", "|---|---|---:|---:|---|"]
    for mod, (folder, desc, entry) in MODULE_LABEL.items():
        n = sum(1 for r in res if cat_mod.get(r["category"]) == mod)
        k = sum(1 for c in cats if c["module"] == mod)
        rows.append(f"| **`{folder}`** | {desc} | {n} | {k} | [{entry}]({entry}) |")
    rows.append(f"| | **合计** | **{len(res)}** | **{len(cats)}** | [INDEX.md](INDEX.md) |")
    t = replace_block(t, "badges", f'<p align="center">{badges}</p>')
    t = replace_block(t, "stats", "\n".join(rows))
    path.write_text(t, "utf-8")


def main() -> int:
    cats, res = load()
    errs = validate(cats, res)
    if errs:
        print("Data errors:\n  " + "\n  ".join(errs), file=sys.stderr)
        return 1
    if "--check" in sys.argv:
        print(f"OK: {len(res)} resources, {len(cats)} categories")
        return 0
    for p in build(cats, res):
        print("wrote", p.relative_to(ROOT))
    update_readme(cats, res)
    print("updated README.md (badges + stats)")
    import make_banner

    make_banner.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
