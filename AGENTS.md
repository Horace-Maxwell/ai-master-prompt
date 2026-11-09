# AI Master Prompt: Agent 入口

> 给 AI 看的入口文件。Codex、Cursor 等会自动读取 `AGENTS.md`；Claude Code 通过 `CLAUDE.md`、Gemini CLI 通过 `GEMINI.md` 转到这里。
> 如果你是被用户「丢进这个文件夹」的 AI：先读完本页（约 2 分钟），再按下面的路由表只打开需要的文件，不要整库通读。
> 不能读本地文件但能联网：抓取 `llms.txt`（索引）或 `llms-full.txt`（全部内容合成的单个文件）。

## 这个文件夹是什么

用户的个人「万能参考库」。里面收录了经过核实的（2026-11-09）：

- **UI 组件库、特效、动效词汇、设计风格 Skill、灵感站、图标字体配色**：`ui/`
- **Agent Skills**（skills.sh 排行榜 + 分类精选 + 自带 Skill）：`skills/`
- **开源工具**（爬虫、浏览器自动化）：`tools/`
- **脚手架 / Starter、Agent 框架、MCP 模板、架构参考、Awesome 元列表**：`scaffolds/`

所有条目都存在 `data/resources/*.json`（唯一数据源）。`*/catalog*.md`、`INDEX.md`、`llms*.txt` 是由脚本生成的。

## 最快的找法

```bash
python3 scripts/find.py <关键词...>          # 多个关键词取交集；中英文同义词互通（玻璃 = glass）
python3 scripts/find.py 手绘                  # 例：找手绘风组件库
python3 scripts/find.py 玻璃 react native     # 没有同时命中时，会给出部分匹配
python3 scripts/find.py mcp --module ui       # 只在某个模块里找：ui | skills | tools | scaffolds
python3 scripts/find.py 磁吸                  # 动效名称也能搜（来自词汇表）
python3 scripts/find.py shadcn --json         # 输出 JSON
python3 scripts/find.py --list                # 列出全部分类 id 和对应文件
```

- 默认显示前 20 条，按相关度排序，⭐ 优先；`--limit N` 调整。
- 脚本在任何目录下都能运行。从别的项目引用本库时用绝对路径，**路径里有空格要加引号**：`python3 "/path/to/AI Master Prompt/scripts/find.py" 手绘`。
- Windows 把 `python3` 换成 `python` 或 `py -3`。只需要 Python 3.9+，没有第三方依赖。
- 不想跑脚本：打开 [INDEX.md](INDEX.md) 按分类浏览，或直接 grep `ui/catalog/*.md`。

## 路由表：用户想要 X → 打开 Y

**多行同时命中时**：凡是涉及界面，先读 [ui/SKILL.md](ui/SKILL.md)；用户指定了风格，「风格」行优先于「落地页」行（别给手绘风需求推荐暗色炫技组件）。

| 用户的需求 | 先读 | 然后 |
|---|---|---|
| 做/改网页或 App 的 UI、「做好看点」 | [ui/SKILL.md](ui/SKILL.md) | 按其中流程挑库、挑风格 |
| 指定视觉风格（手绘、复古、玻璃、粗野、终端…） | [ui/prompts/style-recipes.md](ui/prompts/style-recipes.md) | [ui/catalog/04-stylized-themes.md](ui/catalog/04-stylized-themes.md) |
| 想要某个动效/特效，但说不出名字 | [ui/prompts/effect-vocabulary.md](ui/prompts/effect-vocabulary.md) | [ui/catalog/09-design-vocabulary.md](ui/catalog/09-design-vocabulary.md)（motion-prompt 等画廊） |
| 落地页 / Hero / 炫酷动画组件（未指定风格） | [ui/catalog/03-animated-components.md](ui/catalog/03-animated-components.md) | [ui/catalog/06-effects-3d-shaders.md](ui/catalog/06-effects-3d-shaders.md) |
| 移动端 / React Native / Expo | [ui/catalog/05-mobile.md](ui/catalog/05-mobile.md) | [scaffolds/01-starters.md](scaffolds/01-starters.md) |
| AI 产品界面（聊天、Agent 面板、trace、成本） | [ui/catalog/07-ai-product-ui.md](ui/catalog/07-ai-product-ui.md) | [scaffolds/02-ai-agents.md](scaffolds/02-ai-agents.md) |
| 给 Agent 装 UI 相关 MCP / 查最新文档 | [ui/catalog/12-mcp-registries-llms.md](ui/catalog/12-mcp-registries-llms.md) | |
| 图标、字体、配色、主题 / 找参考截图 | [ui/catalog/11-assets.md](ui/catalog/11-assets.md) | [ui/catalog/10-inspiration.md](ui/catalog/10-inspiration.md) |
| 新建项目、选技术栈、要脚手架 | [scaffolds/README.md](scaffolds/README.md) | [scaffolds/01-starters.md](scaffolds/01-starters.md) |
| 做 Agent / 多 Agent / RAG / Chatbot / MCP Server | [scaffolds/README.md](scaffolds/README.md) | [scaffolds/02-ai-agents.md](scaffolds/02-ai-agents.md) |
| 系统设计、架构决策、画架构图 | [scaffolds/03-architecture.md](scaffolds/03-architecture.md) | |
| 想装 Skill / 问「有没有能做 X 的 Skill」 | [skills/README.md](skills/README.md) | [skills/catalog.md](skills/catalog.md) |
| 采集小红书/抖音/B站等公开数据、浏览器自动化 | [tools/README.md](tools/README.md) | [tools/catalog.md](tools/catalog.md) |
| 中文文章去 AI 味 | [lieflat-less-ai-tone/SKILL.md](lieflat-less-ai-tone/SKILL.md) | 按该 Skill 的流程执行（目录为空就先运行 `./setup.sh`） |
| 本库没有的东西 | [scaffolds/04-awesome-lists.md](scaffolds/04-awesome-lists.md) | 巨型 awesome 列表、skills.sh 搜索 |
| 用户要一段能贴进任何 AI 聊天框的总提示词 | [MASTER_PROMPT.md](MASTER_PROMPT.md) | |

## 使用规则

1. **先用库里的，再上网搜。** 本库条目已核实可用；只有找不到或需要更新时才搜索网络。
2. **⭐ 表示同类首选。** 没有特殊要求时优先推荐 ⭐ 条目；模块 README 里的「快速选型」表和 ⭐ 一致。
3. **不是每条都有安装命令。** 目录里「AI 接入」一列是代码块的可以直接运行；是普通文字的（如 `llms.txt: <链接>`、「copy prompt」）是接入方式说明。带 `<item>`、`<component>` 的是占位符，先用 `npx shadcn@latest search @命名空间 --query 关键词` 查到真实条目名再装。
4. **安装前告诉用户。** 运行 `npx skills add`、`claude mcp add`、`npx shadcn@latest add` 这类会改动用户项目或配置的命令之前，先说明要装什么。价格是「付费」或「免费+付费」的要提醒。
5. **注意许可证与合规。** 条目描述里带 ⚠ 的要转告用户（如 Rare UI 需署名、goopUI 仅 Vue 且未发布、MediaCrawler 禁止商用）。
6. **数据会过时。** 星数、安装量、价格是 2026-11-09 的快照。用户关心时用 `python3 scripts/check_links.py` 检查链接，或上网核实。
7. **想给库加东西：** 改 `data/resources/*.json` → 运行 `python3 scripts/build.py`。不要手改生成的文件。格式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 不是 Claude Code？命令这样换

目录里的 MCP 命令以 Claude Code 为例（`claude mcp add <名字> -- <命令>`）。`--` 后面那段 `npx …` 对所有 Agent 都一样，只是登记的位置不同：

| Agent | MCP 写在哪 | Skill 怎么装 |
|---|---|---|
| Claude Code | `claude mcp add <名字> -- npx …`，或项目根目录 `.mcp.json` | `npx skills add <owner/repo>`，或 `/plugin marketplace add` |
| Codex | `codex mcp add <名字> -- npx …`，或 `~/.codex/config.toml` 的 `[mcp_servers.<名字>]` | `npx skills add <owner/repo>` |
| Cursor | `.cursor/mcp.json` 的 `mcpServers` | `npx skills add <owner/repo>` |
| Gemini CLI | `~/.gemini/settings.json` 的 `mcpServers` | `npx skills add <owner/repo>` |

- 远程（HTTP）MCP：Claude Code 用 `claude mcp add --transport http <名字> <URL>`；其他 Agent 在各自配置里填同一个 URL。
- `npx skills add` 会自动识别本机装了哪些 Agent。`/plugin …` 开头的命令只有 Claude Code 能用，条目里一般同时给了通用写法。
- 带 `--client claude` 的初始化命令（shadcn、21st、ExpoKit 等）通常也支持 `--client cursor` / `vscode` 等，以各自文档为准。

## 目录结构

```
AGENTS.md            ← 你在这里（AI 入口）
CLAUDE.md / GEMINI.md← 指向本文件
README.md            ← 给人看的说明
MASTER_PROMPT.md     ← 可直接粘贴进任何 AI 的总提示词
INDEX.md             ← 全部分类索引（自动生成）
llms.txt             ← 给联网 AI 的索引（原始链接）；llms-full.txt 是全部内容的单文件版
setup.sh             ← 一键检查环境 / 拉子模块 / 安装 Skill（--link-skills）；可选，不跑也能用
ui/                  ← SKILL.md + README.md + prompts/（3 份手写指南）+ catalog/（12 个文件）
skills/              ← README.md + catalog.md
tools/               ← README.md + catalog.md
scaffolds/           ← README.md + 4 个分类文件
lieflat-less-ai-tone/← 子模块 Skill：中文去 AI 味（若为空，运行 ./setup.sh）
data/                ← resources/*.json（唯一数据源）+ categories.json + aliases.json + meta.json
scripts/             ← find.py 搜索 / build.py 校验与生成 / check_links.py 查死链
assets/              ← README 头图（自动生成）
```
