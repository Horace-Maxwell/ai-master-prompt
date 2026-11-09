# 新增 / 修改条目

所有数据在 `data/resources/*.json`（按模块分文件，随便放哪个文件都行，脚本会合并）。分类定义在 `data/categories.json`。

## 条目格式

每个条目是一个 JSON 对象（下面是合法 JSON，可以直接复制改）：

```json
{
  "id": "sketchbook-ui",
  "name": "Sketchbook UI",
  "url": "https://sarthakrawat-1.github.io/sketchbook-ui/",
  "category": "ui-stylized",
  "star": true,
  "desc": "手绘笔记本风：20 个带抖动 SVG 边框和纸张纹理的组件，零运行时依赖",
  "stack": ["React", "TS"],
  "ai": "npm i sketchbook-ui",
  "price": "free",
  "tags": ["hand-drawn", "手绘", "notebook"]
}
```

| 字段 | 必填 | 说明 |
|---|:-:|---|
| `id` | ✅ | 全局唯一，kebab-case（小写字母、数字、连字符） |
| `name` | ✅ | 显示名称 |
| `url` | ✅ | `http(s)` 链接；仓库内文件写 `./路径` |
| `category` | ✅ | 分类 id，运行 `python3 scripts/find.py --list` 查看 |
| `desc` | ✅ | 一句话：是什么 + 什么时候用；有坑用 ⚠ 标出 |
| `star` | | `true` = 同类首选。每个分类别超过 3–5 个 |
| `stack` | | 技术栈数组 |
| `ai` | | 安装命令 / MCP / Skill / llms.txt，写法见下文 |
| `price` | | `free` \| `freemium` \| `paid` \| `oss` |
| `tags` | | 搜索关键词，中英文都加 |
| `order` | | 数字，分类内按它排序（排行榜用）；不写则 ⭐ 优先再按字母 |
| `alias_of` | | 另一个条目的 id。表示这是同一资源在第二个分类里的重复展示，不计入总数、不出现在搜索结果 |

## 流程

```bash
python3 scripts/build.py --check   # 校验（必填字段、重复 id、未知分类）
python3 scripts/build.py --fmt     # 整理 JSON（每条一行、固定字段顺序）
python3 scripts/build.py           # 重新生成目录、INDEX.md、llms.txt、llms-full.txt、README 徽章统计、头图
python3 scripts/check_links.py     # 可选：检查链接
```

推送后 GitHub Actions 会自动跑同样的校验（`.github/workflows/validate.yml`）：数据不合法、或生成文件没更新，CI 会失败并提示该跑哪条命令。

## 其他可调的数据

| 文件 | 作用 |
|---|---|
| `data/aliases.json` | 搜索同义词组（中英文互通）。搜不到某个词时，把它加进对应的组，或新增一组 |
| `data/meta.json` | 仓库地址（llms.txt 里的原始链接用）和「最后核实日期」（徽章和头图用） |
| `data/categories.json` | 分类定义 |

`ai` 字段的写法：能直接运行的命令照原样写；多条用 `；` 分隔；补充说明放在末尾的中文括号里，例如 `npx -y flowbite-mcp（需 FIGMA_ACCESS_TOKEN）`。生成目录时命令会变成可复制的代码块，说明保持普通文字。

## 新增分类

在 `data/categories.json` 加一项：`id`、`module`（ui/skills/tools/scaffolds）、`file`（输出到哪个 md）、`title`、`intro`；如果是新文件，再加 `file_title`。新模块记得在 `AGENTS.md` 路由表里加一行。

## 让 AI 帮你加

> 帮我把 https://xxx 加进这个库。先核实链接和安装命令，再按 CONTRIBUTING.md 的格式写进合适的 data/resources/*.json，然后运行 build.py。
