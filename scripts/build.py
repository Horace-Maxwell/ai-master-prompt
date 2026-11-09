#!/usr/bin/env python3
"""Generate catalog Markdown from data/*.json.

Single source of truth:
  data/categories.json  -> category id, module, title, output file, intro
  data/resources/*.json -> every resource (one object per entry, merged)

Usage:
  python3 scripts/build.py          # regenerate catalogs, INDEX.md, llms.txt, llms-full.txt,
                                    # README badges/stats and assets/banner.svg
  python3 scripts/build.py --check  # validate data only, write nothing
  python3 scripts/build.py --fmt    # tidy data/resources/*.json (one entry per line)
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

from _data import countable, is_command, load_categories, load_meta, load_resources

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

REQUIRED = ("id", "name", "url", "category", "desc")
PRICE_LABEL = {"free": "免费", "freemium": "免费+付费", "paid": "付费", "oss": "开源"}


def load() -> tuple[list[dict], list[dict]]:
    return load_categories(), load_resources()


PRICES = {"free", "freemium", "paid", "oss"}


def validate(cats: list[dict], res: list[dict]) -> list[str]:
    errs: list[str] = []
    cat_ids = {c["id"] for c in cats}
    ids = {r.get("id") for r in res}
    seen: set[str] = set()
    for i, r in enumerate(res):
        rid = r.get("id", "?")
        for k in REQUIRED:
            if not r.get(k):
                errs.append(f"#{i} {rid}: missing '{k}'")
        if rid in seen:
            errs.append(f"duplicate id: {rid}")
        seen.add(rid)
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", str(rid)):
            errs.append(f"{rid}: id must be kebab-case (a-z, 0-9, -)")
        if r.get("category") not in cat_ids:
            errs.append(f"{rid}: unknown category '{r.get('category')}'")
        url = str(r.get("url", ""))
        if url.startswith("./"):
            top = url[2:].split("/")[0]
            gitmodules = ROOT / ".gitmodules"
            unfetched = gitmodules.exists() and f"path = {top}" in gitmodules.read_text("utf-8") \
                and not any((ROOT / top).glob("*"))
            if not (ROOT / url).exists() and not unfetched:  # an unfetched submodule is not a data error
                errs.append(f"{rid}: local path does not exist: {url}")
        elif not url.startswith("http"):
            errs.append(f"{rid}: url must start with http or ./ (local path)")
        if r.get("price") and r["price"] not in PRICES:
            errs.append(f"{rid}: price must be one of {sorted(PRICES)}")
        if r.get("alias_of") and r["alias_of"] not in ids:
            errs.append(f"{rid}: alias_of points to unknown id '{r['alias_of']}'")
        if re.search(r"<[^<>]*(host|your-|TODO)[^<>]*>", r.get("ai", "") + url, re.I):
            errs.append(f"{rid}: unresolved placeholder in ai/url")
    alias_file = DATA / "aliases.json"
    if alias_file.exists():
        owner: dict[str, str] = {}
        for group in json.loads(alias_file.read_text("utf-8")):
            for a in group:
                if a.lower() in owner and owner[a.lower()] != group[0]:
                    errs.append(f"aliases.json: '{a}' is in two groups ({owner[a.lower()]}, {group[0]})")
                owner[a.lower()] = group[0]
    return errs


def cell(text: str | None) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def render_ai(ai: str | None) -> str:
    """Commands go in code spans (copyable); notes stay plain text. One per line."""
    if not ai:
        return ""
    if "`" in ai:
        return cell(ai)
    out = []
    for seg in re.split(r"\s*[；;]\s*|\s+→\s+|\s+/\s+(?=(?:npx|npm|pip|claude|uvx|git) )", ai):
        seg = seg.strip()
        if not seg:
            continue
        lead = ""
        if seg.startswith("或 "):
            lead, seg = "或 ", seg[2:].strip()
        m = re.match(r"^(.*?)\s*(（[^（）]*）)$", seg)  # trailing Chinese note stays outside the code span
        body, note = (m.group(1), m.group(2)) if m else (seg, "")
        if is_command(body):
            out.append(f"{lead}`{cell(body)}`{note}")
        else:
            out.append(cell(lead + seg).replace("<", "&lt;").replace(">", "&gt;"))
    return "<br>".join(out)


def render_category(cat: dict, items: list[dict]) -> str:
    # explicit `order` (e.g. leaderboard rank) wins; otherwise ⭐ first, then A-Z
    items = sorted(items, key=lambda r: (r.get("order", 10**6), not r.get("star"), r["name"].lower()))
    here = (ROOT / cat["file"]).parent
    has_stack = any(r.get("stack") for r in items)
    has_ai = any(r.get("ai") for r in items)
    head = ["名称", "是什么 / 什么时候用"]
    if has_stack:
        head.append("技术栈")
    if has_ai:
        head.append("AI 接入（安装命令 / MCP / Skill）")
    head.append("价格")
    out = [f'<a id="{cat["id"]}"></a>', "", f"## {cat['title']}", ""]
    if cat.get("intro"):
        out += [cat["intro"], ""]
    out += ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in items:
        url = r["url"]
        if url.startswith("./"):  # repo-local file: make the link relative to this catalog
            url = os.path.relpath(ROOT / url, here).replace(os.sep, "/")
        name = f"[{cell(r['name'])}]({url})"
        if r.get("star"):
            name = "⭐ " + name
        row = [name, cell(r["desc"])]
        if has_stack:
            row.append(cell(", ".join(r.get("stack", []))))
        if has_ai:
            row.append(render_ai(r.get("ai")))
        row.append(PRICE_LABEL.get(r.get("price", ""), cell(r.get("price"))))
        out.append("| " + " | ".join(row) + " |")
    out.append("")
    return "\n".join(out)


HAND_WRITTEN = [
    ("AGENTS.md", "AI 入口：需求 → 文件 路由表与使用规则（先读这个）"),
    ("MASTER_PROMPT.md", "可直接粘贴进任何 AI 的总提示词"),
    ("ui/SKILL.md", "UI 工作流程：选型决策表、MCP、shadcn 命名空间用法、自检清单"),
    ("ui/prompts/effect-vocabulary.md", "100+ 个动效/特效/镜头/摄影专业名称速查表"),
    ("ui/prompts/style-recipes.md", "11 种视觉风格配方：特征、推荐库、安装命令、避坑"),
    ("ui/prompts/request-template.md", "UI 需求描述模板"),
    ("skills/README.md", "Agent Skills 安装方式与起步包"),
    ("tools/README.md", "MediaCrawler 等开源工具用法"),
    ("scaffolds/README.md", "脚手架快速选型表与已失效项目"),
]


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

    # Global index: hand-written guides first, then one line per category
    idx = [
        "# 资源总索引（自动生成）",
        "",
        f"共 {len(countable(res))} 条资源，{len(cats)} 个分类。点击进入对应分类。",
        "也可以用 `python3 scripts/find.py <关键词>` 搜索，或 `python3 scripts/find.py --list` 列出分类 id。",
        "",
        "## 入口与手写指南",
        "",
    ]
    idx += [f"- [{p}]({p}) — {d}" for p, d in HAND_WRITTEN]
    module = None
    for c in cats:
        if c["module"] != module:
            module = c["module"]
            idx += ["", f"## {module}/", ""]
        n = len(by_cat.get(c["id"], []))
        idx.append(f"- [{c['title']}]({c['file']}#{c['id']}) — {n} 条")
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
    res = countable(res)
    cat_mod = {c["id"]: c["module"] for c in cats}
    n_star = sum(1 for r in res if r.get("star"))
    n_ai = sum(1 for r in res if r.get("ai") and re.search(r"(?:^|[；;→/] ?|或 )(?:npx|npm|pip|claude|uvx|uv|git|go|brew|wasp|/plugin) ", r["ai"]))
    badges = " ".join(
        [
            badge("resources", str(len(res))),
            badge("categories", str(len(cats))),
            badge("⭐ picks", str(n_star)),
            badge("install commands", str(n_ai)),
            badge("verified", load_meta()["verified"], "9BC27D"),
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


KEY_ORDER = ("id", "name", "url", "category", "star", "desc", "stack", "ai", "price", "tags")


def format_data() -> None:
    """Rewrite data/resources/*.json as one entry per line with a stable key order."""
    for f in sorted((DATA / "resources").glob("*.json")):
        items = json.loads(f.read_text("utf-8"))
        lines = []
        for it in items:
            ordered = {k: it[k] for k in KEY_ORDER if k in it}
            ordered.update({k: v for k, v in it.items() if k not in ordered and not k.startswith("_")})
            lines.append("  " + json.dumps(ordered, ensure_ascii=False))
        f.write_text("[\n" + ",\n".join(lines) + "\n]\n", "utf-8")
        print("formatted", f.relative_to(ROOT))


def build_llms(cats: list[dict], res: list[dict]) -> list[Path]:
    """llms.txt (index with raw URLs) and llms-full.txt (everything in one file)."""
    raw = f"https://raw.githubusercontent.com/{load_meta()['repo']}/main/"
    n_total = len(countable(res))
    by_cat: dict[str, int] = defaultdict(int)
    for r in res:
        by_cat[r["category"]] += 1
    files: dict[str, list[dict]] = defaultdict(list)
    for c in cats:
        files[c["file"]].append(c)

    out = [
        "# AI Master Prompt",
        "",
        f"> 给 AI Agent 用的参考库：{n_total} 条经核实的 UI 组件库、动效词汇、设计 Skill、MCP、"
        "Agent Skills、脚手架、Agent 框架与架构参考。每条有一句话说明，多数带可直接运行的安装命令。",
        "",
        "用法：先读 AGENTS.md 的路由表，再按需求只打开 1–3 个文件。⭐ = 同类首选。"
        "不能读文件但能联网的 AI，直接抓取下面的原始链接；想一次读完，用 llms-full.txt。",
        "",
        "## 入口与手写指南",
        "",
    ]
    out += [f"- [{p}]({raw}{p}): {d}" for p, d in HAND_WRITTEN]
    module = None
    for file, fcats in files.items():
        if fcats[0]["module"] != module:
            module = fcats[0]["module"]
            out += ["", f"## 目录：{module}", ""]
        n = sum(by_cat[c["id"]] for c in fcats)
        titles = "；".join(c["title"] for c in fcats)
        out.append(f"- [{file}]({raw}{file}): {titles}（{n} 条）")
    out += [
        "",
        "## Optional",
        "",
        f"- [llms-full.txt]({raw}llms-full.txt): 以上全部内容合并成的单个文件",
        f"- [INDEX.md]({raw}INDEX.md): 全部分类与条目数",
        f"- [CONTRIBUTING.md]({raw}CONTRIBUTING.md): 条目格式与新增流程",
        "",
    ]
    p1 = ROOT / "llms.txt"
    p1.write_text("\n".join(out), "utf-8")

    full = [
        "# AI Master Prompt（完整版，单文件）",
        "",
        f"> {n_total} 条资源，{len(cats)} 个分类。本文件由 scripts/build.py 自动合并生成，"
        "把它整个交给任何 AI 即可。文件之间用 `===== FILE: 路径 =====` 分隔。",
        "",
    ]
    for p in [h[0] for h in HAND_WRITTEN] + list(files):
        f = ROOT / p
        if f.exists():
            body = re.sub(r"^---\n.*?\n---\n", "", f.read_text("utf-8"), flags=re.S)
            full += [f"===== FILE: {p} =====", "", body.strip(), ""]
    p2 = ROOT / "llms-full.txt"
    p2.write_text("\n".join(full) + "\n", "utf-8")
    return [p1, p2]


def main() -> int:
    cats, res = load()
    errs = validate(cats, res)
    if errs:
        print("Data errors:\n  " + "\n  ".join(errs), file=sys.stderr)
        return 1
    if "--fmt" in sys.argv:
        format_data()
        return 0
    if "--check" in sys.argv:
        print(f"OK: {len(countable(res))} resources, {len(cats)} categories")
        return 0
    for p in build(cats, res):
        print("wrote", p.relative_to(ROOT))
    for p in build_llms(cats, res):
        print("wrote", p.relative_to(ROOT), f"({p.stat().st_size // 1024} KB)")
    update_readme(cats, res)
    print("updated README.md (badges + stats)")
    import make_banner

    make_banner.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
