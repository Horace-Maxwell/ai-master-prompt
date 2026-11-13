# AI Master Prompt: Agent 入口

> 给 AI 看的入口文件。Codex、Cursor 等会自动读取 `AGENTS.md`；Claude Code 通过 `CLAUDE.md`、Gemini CLI 通过 `GEMINI.md` 转到这里。
> 如果你是被用户「丢进这个文件夹」的 AI：先读完本页（约 2 分钟），再按下面的路由表只打开需要的文件，不要整库通读。
> 不能读本地文件但能联网：抓取 `llms.txt`（索引）或 `llms-full.txt`（手写指南 + 全部 ⭐ 精选合成的单个文件，约 100 KB）。

## 这个文件夹是什么

用户的个人「万能参考库」（数据核实于 2026-11-09）：

- **UI**：各框架组件库（React / Vue / Svelte / 原生 / 国内生态）、功能型组件、特效、动效词汇、设计系统、模板、灵感站、图标字体配色素材：`ui/`
- **Agent Skills、规则与 Prompt 库**：`skills/`
- **工具**：MCP 目录与常用 MCP 服务器、AI 编码工具、爬虫与浏览器自动化：`tools/`
- **搭项目用的**：脚手架、Agent 框架、服务与基础设施、AI 基础设施、常用库、架构参考、Awesome 元列表：`scaffolds/`

规模：约 2500 条资源，另含 shadcn 官方索引的全部 548 个 registry。**不要通读**，按下面的方法找。

所有条目都存在 `data/resources/*.json`（唯一数据源）。`*/catalog*.md`、`INDEX.md`、`llms*.txt` 是由脚本生成的。

## 最快的找法

**想要默认选择**：直接读 [PICKS.md](PICKS.md)，全库 200 多个 ⭐ 首选都在这一页。

**想找具体的东西**：搜索。

```bash
python3 scripts/find.py <关键词...>          # 多个关键词取交集；中英文同义词互通（玻璃 = glass）
python3 scripts/find.py 手绘                  # 例：找手绘风组件库
python3 scripts/find.py 玻璃 react native     # 没有同时命中时，会给出部分匹配
python3 scripts/find.py mcp --module ui       # 只在某个模块里找：ui | skills | tools | scaffolds
python3 scripts/find.py 磁吸                  # 动效名称也能搜（来自词汇表）
python3 scripts/find.py shadcn --json         # 输出 JSON
python3 scripts/find.py 数据库 --stars        # 只看 ⭐ 首选
python3 scripts/find.py --category stack-services --group 认证   # 看某分类下某一组的全部条目
python3 scripts/find.py --list                # 列出全部分类 id 和对应文件
```

- 默认显示前 20 条，按相关度排序，⭐ 优先；`--limit N` 调整。
- 脚本在任何目录下都能运行。从别的项目引用本库时用绝对路径，**路径里有空格要加引号**：`python3 "/path/to/AI Master Prompt/scripts/find.py" 手绘`。
- Windows 把 `python3` 换成 `python` 或 `py -3`。只需要 Python 3.9+，没有第三方依赖。
- 搜索结果末尾的「📦 shadcn 官方索引」是未精选的 registry，说明是作者原文，装之前自己看一眼。
- 不想跑脚本：打开 [INDEX.md](INDEX.md) 按分类浏览。**目录文件有的很大**（服务、素材、功能型组件各有上百条），不要整个读：先 grep 文件里的 `### 小标题`，只读需要的那一组。

## 路由表：用户想要 X → 打开 Y

**多行同时命中时**：凡是涉及界面，先读 [ui/SKILL.md](ui/SKILL.md)；用户指定了风格，「风格」行优先于「落地页」行（别给手绘风需求推荐暗色炫技组件）。

| 用户的需求 | 先读 | 然后 |
|---|---|---|
| 做/改网页或 App 的 UI、「做好看点」 | [ui/SKILL.md](ui/SKILL.md) | 按其中流程挑库、挑风格 |
| 指定视觉风格（手绘、复古、玻璃、粗野、终端…） | [ui/prompts/style-recipes.md](ui/prompts/style-recipes.md) | [ui/catalog/04-stylized-themes.md](ui/catalog/04-stylized-themes.md) |
| 想要某个动效/特效，但说不出名字 | [ui/prompts/effect-vocabulary.md](ui/prompts/effect-vocabulary.md) | [ui/catalog/09-design-vocabulary.md](ui/catalog/09-design-vocabulary.md)（motion-prompt 等画廊） |
| 落地页 / Hero / 炫酷动画组件（未指定风格） | [ui/catalog/03-animated-components.md](ui/catalog/03-animated-components.md) | [ui/catalog/06-effects-3d-shaders.md](ui/catalog/06-effects-3d-shaders.md) |
| 移动端 / React Native / Expo / Flutter / SwiftUI / Compose | [ui/catalog/05-mobile.md](ui/catalog/05-mobile.md) | [scaffolds/01-starters.md](scaffolds/01-starters.md) |
| Vue / Svelte / Angular / 纯 HTML+CSS 项目的组件库 | [ui/catalog/13-other-frameworks.md](ui/catalog/13-other-frameworks.md) | |
| 国内项目：Ant Design / Element Plus / 中后台 / 小程序 / uni-app / 中文字体 | [ui/catalog/14-china-ecosystem.md](ui/catalog/14-china-ecosystem.md) | |
| 要一个具体功能的组件（图表、表格、富文本编辑器、日历、拖拽、流程图、地图、上传…） | [ui/catalog/16-functional-components.md](ui/catalog/16-functional-components.md) | `find.py <功能名>` |
| 对齐某个平台规范（Material、Apple HIG、Fluent…） | [ui/catalog/15-design-systems.md](ui/catalog/15-design-systems.md) | |
| 要现成模板 / 整页区块 / Figma UI Kit | [ui/catalog/17-templates-blocks.md](ui/catalog/17-templates-blocks.md) | |
| 某个 shadcn registry 有没有、怎么装 | [ui/catalog/18-shadcn-registries.md](ui/catalog/18-shadcn-registries.md)（548 个，先 grep） | |
| AI 产品界面（聊天、Agent 面板、trace、成本） | [ui/catalog/07-ai-product-ui.md](ui/catalog/07-ai-product-ui.md) | [scaffolds/02-ai-agents.md](scaffolds/02-ai-agents.md) |
| 给 Agent 装 UI 相关 MCP / 查最新文档 | [ui/catalog/12-mcp-registries-llms.md](ui/catalog/12-mcp-registries-llms.md) | |
| 图标、字体、配色、主题、插画、3D、样机、背景、音效 / 找参考截图 | [ui/catalog/11-assets.md](ui/catalog/11-assets.md) | [ui/catalog/10-inspiration.md](ui/catalog/10-inspiration.md) |
| 新建项目、选技术栈、要脚手架 | [scaffolds/README.md](scaffolds/README.md) | [scaffolds/01-starters.md](scaffolds/01-starters.md) |
| 做 Agent / 多 Agent / RAG / Chatbot / MCP Server | [scaffolds/README.md](scaffolds/README.md) | [scaffolds/02-ai-agents.md](scaffolds/02-ai-agents.md) |
| 选认证 / 数据库 / 支付 / 邮件 / 部署 / 文档站 / CMS | [PICKS.md](PICKS.md) | [scaffolds/05-services.md](scaffolds/05-services.md) |
| AI 应用的模型网关 / 向量库 / 评测 / 沙箱 / 语音 / 国内模型平台 | [PICKS.md](PICKS.md) | [scaffolds/06-ai-infra.md](scaffolds/06-ai-infra.md) |
| 状态管理 / 请求 / 校验 / 测试 / 工具链 / Python 常用库选哪个 | [scaffolds/07-common-libs.md](scaffolds/07-common-libs.md) | |
| 系统设计、架构决策、画架构图 | [scaffolds/03-architecture.md](scaffolds/03-architecture.md) | |
| 想装 Skill / 问「有没有能做 X 的 Skill」 | [skills/README.md](skills/README.md) | [skills/catalog.md](skills/catalog.md) |
| 要规则文件、CLAUDE.md / AGENTS.md 范例、子 Agent、规格驱动流程、Prompt 写法 | [skills/02-rules-prompts.md](skills/02-rules-prompts.md) | |
| 某个服务有没有 MCP、怎么装（GitHub、Supabase、Notion、Sentry、高德…） | [tools/02-mcp.md](tools/02-mcp.md) | `find.py mcp <服务名>` |
| 「有什么 AI 工具能做 X」（编码 Agent、AI IDE、建站生成器） | [tools/03-ai-builders.md](tools/03-ai-builders.md) | |
| 采集小红书/抖音/B站等公开数据、浏览器自动化 | [tools/README.md](tools/README.md) | [tools/catalog.md](tools/catalog.md) |
| 中文文章去 AI 味 | [lieflat-less-ai-tone/SKILL.md](lieflat-less-ai-tone/SKILL.md) | 按该 Skill 的流程执行（目录为空就先运行 `./setup.sh`） |
| 本库没有的东西 | [scaffolds/04-awesome-lists.md](scaffolds/04-awesome-lists.md) | 巨型 awesome 列表、skills.sh 搜索 |
| 用户要一段能贴进任何 AI 聊天框的总提示词 | [MASTER_PROMPT.md](MASTER_PROMPT.md) | |

## 使用规则

1. **先用库里的，再上网搜。** 库里条目的链接和安装包都自动检查过；只有找不到或需要更新时才搜索网络。
2. **⭐ 表示同类首选。** 没有特殊要求时优先推荐 ⭐ 条目；模块 README 里的「快速选型」表和 ⭐ 一致。
3. **不是每条都有安装命令。** 目录里「AI 接入」一列是代码块的可以直接运行；是普通文字的（如 `llms.txt: <链接>`、「copy prompt」）是接入方式说明。带 `<item>`、`<component>` 的是占位符，先用 `npx shadcn@latest search @命名空间 --query 关键词` 查到真实条目名再装。
4. **安装前告诉用户。** 运行 `npx skills add`、`claude mcp add`、`npx shadcn@latest add` 这类会改动用户项目或配置的命令之前，先说明要装什么。价格是「付费」或「免费+付费」的要提醒。
5. **注意许可证与合规。** 条目描述里带 ⚠ 的要转告用户（如 Rare UI 需署名、goopUI 仅 Vue 且未发布、MediaCrawler 禁止商用）。
6. **数据会过时，核实程度也不一样。** 星数、安装量、价格是 2026-11-09 的快照。⭐ 条目和最早的 380 条逐条对照过官方文档；批量收录的条目由调研时核对，并经脚本检查链接存在、命令里的包和仓库存在，但没有人逐条试装。装之前看一眼官方文档；用户关心时运行 `python3 scripts/check_links.py` 和 `python3 scripts/check_commands.py`。
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
PICKS.md             ← 全部 ⭐ 首选，一页看完（自动生成）
INDEX.md             ← 全部分类索引（自动生成）
llms.txt             ← 给联网 AI 的索引（原始链接）；llms-full.txt 是手写指南 + ⭐ 精选的单文件版
setup.sh             ← 一键检查环境 / 拉子模块 / 安装 Skill（--link-skills）；可选，不跑也能用
ui/                  ← SKILL.md + README.md + prompts/（3 份手写指南）+ catalog/（18 个文件）
skills/              ← README.md + catalog.md + 02-rules-prompts.md
tools/               ← README.md + catalog.md + 02-mcp.md + 03-ai-builders.md
scaffolds/           ← README.md + 7 个分类文件
lieflat-less-ai-tone/← 子模块 Skill：中文去 AI 味（若为空，运行 ./setup.sh）
data/                ← resources/*.json（唯一数据源）+ registries.json（shadcn 索引快照）+ categories / aliases / meta
scripts/             ← find.py 搜索 / build.py 校验与生成 / check_links.py 查死链 / check_commands.py 查安装命令 / import_batch.py 批量导入 / sync_registries.py 刷新 shadcn 索引
assets/              ← README 头图（自动生成）
```
