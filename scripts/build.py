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
    cat_groups = {c["id"]: c.get("groups") for c in cats}
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
        groups = cat_groups.get(r.get("category"))
        if r.get("group") and (not groups or r["group"] not in groups):
            errs.append(f"{rid}: group '{r['group']}' is not defined for category {r.get('category')}")
        if r.get("alias_of") and r["alias_of"] not in ids:
            errs.append(f"{rid}: alias_of points to unknown id '{r['alias_of']}'")
        if re.search(r"<[^<>]*(-host|TODO)[^<>]*>", r.get("ai", "") + url):  # <your-api-key> style is fine
            errs.append(f"{rid}: unresolved placeholder in ai/url")
    regs = load_registries()["registries"]
    if regs:  # every @namespace used in a shadcn command must be resolvable
        known = {x["name"] for x in regs} | set(load_meta().get("extra_namespaces", []))
        for r in res:
            for ns in re.findall(r"shadcn@latest add (@[a-z0-9][a-z0-9-]*)/", r.get("ai", "")):
                if ns not in known:
                    errs.append(f"{r.get('id')}: shadcn namespace {ns} is not in data/registries.json "
                                "(run scripts/sync_registries.py, or add it to meta.json extra_namespaces)")
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


def render_table(items: list[dict], here: Path) -> list[str]:
    has_stack = any(r.get("stack") for r in items)
    has_ai = any(r.get("ai") for r in items)
    head = ["名称", "是什么 / 什么时候用"]
    if has_stack:
        head.append("技术栈")
    if has_ai:
        head.append("AI 接入（安装命令 / MCP / Skill）")
    head.append("价格")
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
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
    return out


def render_category(cat: dict, items: list[dict]) -> str:
    # explicit `order` (e.g. leaderboard rank) wins; otherwise ⭐ first, then A-Z
    items = sorted(items, key=lambda r: (r.get("order", 10**6), not r.get("star"), r["name"].lower()))
    here = (ROOT / cat["file"]).parent
    out = [f'<a id="{cat["id"]}"></a>', "", f"## {cat['title']}", ""]
    if cat.get("intro"):
        out += [cat["intro"], ""]
    groups = [g for g in cat.get("groups", []) if any(r.get("group") == g for r in items)]
    if not groups:
        return "\n".join(out + render_table(items, here))
    rest = [r for r in items if r.get("group") not in groups]
    out += ["本类分组：" + " · ".join(groups + (["其他"] if rest else [])), ""]
    for g in groups:
        out += [f"### {g}", ""] + render_table([r for r in items if r.get("group") == g], here)
    if rest:
        out += ["### 其他", ""] + render_table(rest, here)
    return "\n".join(out)


REGISTRY_FILE = "ui/catalog/18-shadcn-registries.md"
STATUS_LABEL = {"healthy": "正常", "degraded": "不稳定", "unavailable": "暂不可用", "observing": "观察中"}


def load_registries() -> dict:
    path = DATA / "registries.json"
    return json.loads(path.read_text("utf-8")) if path.exists() else {"registries": [], "fetched": "", "source": ""}


def build_registry_index(res: list[dict]) -> Path | None:
    """Full snapshot of the official shadcn registry index (one row per namespace)."""
    data = load_registries()
    regs = data["registries"]
    if not regs:
        return None
    curated: dict[str, str] = {}
    for r in res:
        for ns in re.findall(r"(@[a-z0-9][a-z0-9-]*)/", r.get("ai", "")):
            curated.setdefault(ns, r["name"])

    def rows(items):
        out = ["| 命名空间 | 说明（官方索引原文） | 条目数 | 状态 | 本库精选 |", "|---|---|---:|---|---|"]
        for x in items:
            name = f"[`{x['name']}`]({x['homepage']})" if x.get("homepage") else f"`{x['name']}`"
            desc = cell(x.get("desc", "")).replace("<", "&lt;").replace(">", "&gt;")
            pick = "⭐ " + cell(curated[x["name"]]) if x["name"] in curated else ""
            out.append(f"| {name} | {desc} | {x.get('items') or ''} | {STATUS_LABEL.get(x.get('status'), x.get('status', ''))} | {pick} |")
        return out

    live = [x for x in regs if not x.get("hidden")]
    hidden = [x for x in regs if x.get("hidden")]
    out = [
        "# shadcn 官方 Registry 索引（全量）",
        "",
        f"> 本文件由 `scripts/build.py` 从 `data/registries.json` 自动生成（快照日期 {data.get('fetched', '')}，"
        f"来源 {data.get('source', '')}）。刷新：`python3 scripts/sync_registries.py && python3 scripts/build.py`。",
        "",
        f"官方索引里的全部 {len(regs)} 个命名空间，合计约 {sum(x.get('items') or 0 for x in regs):,} 个可安装条目。"
        "这里的任何一个都**无需配置**即可安装：",
        "",
        "```bash",
        "npx shadcn@latest list @命名空间                    # 看它有哪些条目",
        "npx shadcn@latest search @命名空间 --query 关键词    # 按关键词找",
        "npx shadcn@latest add @命名空间/条目名               # 安装",
        "```",
        "",
        "按官方排名分排序。「本库精选」一列有内容的，在前面的分类目录里有中文说明和注意事项，优先看那些。"
        "说明一列是各 registry 作者自己写的英文简介，未经本库核实。",
        "",
        f"## 正常收录（{len(live)} 个）",
        "",
        *rows(live),
        "",
    ]
    if hidden:
        out += [
            f"## 已从官方目录页下架（{len(hidden)} 个）",
            "",
            "官方健康检查未通过而被隐藏，CLI 仍能解析这些命名空间。安装前先用 `npx shadcn@latest list` 确认它还能用。",
            "",
            *rows(hidden),
            "",
        ]
    path = ROOT / REGISTRY_FILE
    path.write_text("\n".join(out), "utf-8")
    return path


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
    idx.append("- [PICKS.md](PICKS.md) — 全部 ⭐ 精选，一页看完（自动生成）")
    module = None
    for c in cats:
        if c["module"] != module:
            module = c["module"]
            idx += ["", f"## {module}/", ""]
        n = len(by_cat.get(c["id"], []))
        idx.append(f"- [{c['title']}]({c['file']}#{c['id']}) — {n} 条")
        if c["id"] == "ui-registries" and load_registries()["registries"]:
            idx.append(f"- [shadcn 官方 Registry 索引（全量）]({REGISTRY_FILE}) — {len(load_registries()['registries'])} 个命名空间")
    (ROOT / "INDEX.md").write_text("\n".join(idx) + "\n", "utf-8")
    written.append(ROOT / "INDEX.md")
    return written


MODULE_LABEL = {
    "ui": ("ui/", "组件库（React / Vue / Svelte / 原生 / 国内生态）· 功能型组件 · 特效 · 动效词汇 · 设计系统 · 模板 · 灵感 · 素材 · MCP", "ui/SKILL.md"),
    "skills": ("skills/", "Agent Skills 排行与分领域精选 · 规则 / Prompt / 子 Agent 库", "skills/README.md"),
    "tools": ("tools/", "MCP 目录与常用 MCP 服务器 · AI 编码工具 · 采集与浏览器自动化", "tools/README.md"),
    "scaffolds": ("scaffolds/", "脚手架 · Agent 框架 · 服务与基础设施 · AI 基础设施 · 常用库 · 架构 · 元列表", "scaffolds/README.md"),
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
            badge("shadcn registries", str(len(load_registries()["registries"]))),
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


KEY_ORDER = ("id", "name", "url", "category", "group", "star", "desc", "stack", "ai", "price", "tags")


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


def build_picks(cats: list[dict], res: list[dict]) -> Path:
    """PICKS.md: every ⭐ entry on one page, the fast path for choosing defaults."""
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for r in countable(res):
        if r.get("star"):
            by_cat[r["category"]].append(r)
    n = sum(len(v) for v in by_cat.values())
    out = [
        "# ⭐ 精选速查（自动生成）",
        "",
        f"> 全库 {len(countable(res))} 条里的 {n} 个同类首选，一页看完。没有特殊要求时直接从这里选；"
        "要更多候选，点分类标题进完整目录，或运行 `python3 scripts/find.py <关键词>`。",
        "> 本文件由 `scripts/build.py` 生成，请勿手改。",
        "",
    ]
    module = None
    for c in cats:
        items = by_cat.get(c["id"])
        if not items:
            continue
        if c["module"] != module:
            module = c["module"]
            out += [f"## {module}/", ""]
        out += [f"### [{c['title']}]({c['file']}#{c['id']})", ""]
        order = {g: i for i, g in enumerate(c.get("groups", []))}
        items.sort(key=lambda r: (order.get(r.get("group"), 999), r.get("order", 10**6), r["name"].lower()))
        for r in items:
            url = r["url"]
            grp = f"**{r['group']}**：" if r.get("group") else ""
            line = f"- {grp}[{cell(r['name'])}]({url}) — {r['desc']}"
            ai = r.get("ai", "")
            first = re.split(r"[；;]", ai)[0].strip() if ai else ""
            m = re.match(r"^(.*?)\s*（[^（）]*）$", first)
            first = m.group(1) if m else first
            if first and is_command(first) and "`" not in first:
                line += f" `{first}`"
            out.append(line)
        out.append("")
    path = ROOT / "PICKS.md"
    path.write_text("\n".join(out), "utf-8")
    return path


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
        if file.endswith("12-mcp-registries-llms.md") and load_registries()["registries"]:
            out.append(
                f"- [{REGISTRY_FILE}]({raw}{REGISTRY_FILE}): shadcn 官方索引全部 "
                f"{len(load_registries()['registries'])} 个命名空间（未并入 llms-full.txt）"
            )
    out += [
        "",
        "## Optional",
        "",
        f"- [llms-full.txt]({raw}llms-full.txt): 手写指南 + 全部 ⭐ 精选合并成的单个文件",
        f"- [PICKS.md]({raw}PICKS.md): 全部 ⭐ 精选，一页看完",
        f"- [INDEX.md]({raw}INDEX.md): 全部分类与条目数",
        f"- [CONTRIBUTING.md]({raw}CONTRIBUTING.md): 条目格式与新增流程",
        "",
    ]
    p1 = ROOT / "llms.txt"
    p1.write_text("\n".join(out), "utf-8")

    full = [
        "# AI Master Prompt（单文件版）",
        "",
        f"> 全部手写指南 + {sum(1 for r in countable(res) if r.get('star'))} 个 ⭐ 精选（全库共 {n_total} 条）。"
        "本文件由 scripts/build.py 自动合并生成，把它整个交给任何 AI 即可。",
        f"> 完整目录太大，没有并入：需要更多候选时抓取 {raw}llms.txt 里列出的分类文件。"
        "文件之间用 `===== FILE: 路径 =====` 分隔。",
        "",
    ]
    for p in [h[0] for h in HAND_WRITTEN] + ["PICKS.md"]:
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
    print("wrote", build_picks(cats, res).relative_to(ROOT))
    p = build_registry_index(res)
    if p:
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
