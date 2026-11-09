# 新增 / 修改条目

所有数据在 `data/resources/*.json`（按模块分文件，随便放哪个文件都行，脚本会合并）。分类定义在 `data/categories.json`。

## 条目格式

```json
{
  "id": "looseleaf",                         // 必填，全局唯一，kebab-case
  "name": "Looseleaf",                       // 必填
  "url": "https://kevintngo.github.io/looseleaf/",  // 必填，http(s) 链接；本地文件用 ./路径
  "category": "ui-stylized",                 // 必填，见 data/categories.json
  "desc": "手绘版 shadcn/ui ……",              // 必填，一句话：是什么 + 什么时候用；有坑用 ⚠ 标出
  "star": true,                              // 可选，同类首选
  "stack": ["React", "Tailwind v4"],         // 可选
  "ai": "npx shadcn add @looseleaf/button",  // 可选：安装命令 / MCP / Skill / llms.txt
  "price": "free",                           // 可选：free | freemium | paid | oss
  "tags": ["hand-drawn", "手绘"]              // 可选：搜索关键词，中英文都加
}
```

## 流程

```bash
python3 scripts/build.py --check   # 校验（必填字段、重复 id、未知分类）
python3 scripts/build.py           # 重新生成 catalog/*.md 和 INDEX.md
python3 scripts/check_links.py     # 可选：检查链接
```

## 新增分类

在 `data/categories.json` 加一项：`id`、`module`（ui/skills/tools/scaffolds）、`file`（输出到哪个 md）、`title`、`intro`；如果是新文件，再加 `file_title`。新模块记得在 `AGENTS.md` 路由表里加一行。

## 让 AI 帮你加

> 帮我把 https://xxx 加进这个库。先核实链接和安装命令，再按 CONTRIBUTING.md 的格式写进合适的 data/resources/*.json，然后运行 build.py。
