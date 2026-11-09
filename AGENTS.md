# AI Master Prompt: Agent 入口

> 给 AI 看的入口文件。Claude Code、Codex、Cursor、Gemini CLI 等会自动读取 `AGENTS.md`。
> 如果你是被用户「丢进这个文件夹」的 AI：先读完本页（约 2 分钟），再按下面的路由表只打开需要的文件，不要整库通读。

## 这个文件夹是什么

用户的个人「万能参考库」。里面收录了经过核实的（2026-11-09）：

- **UI 组件库、特效、动效词汇、设计风格 Skill、灵感站、图标字体配色**：`ui/`
- **Agent Skills**（skills.sh 排行榜 + 分类精选 + 本地自带 Skill）：`skills/`
- **开源工具**（爬虫、浏览器自动化）：`tools/`
- **脚手架 / Starter、Agent 框架、MCP 模板、架构参考、Awesome 元列表**：`scaffolds/`

所有条目都存在 `data/resources/*.json`（唯一数据源）。`*/catalog*.md` 和 `INDEX.md` 是由脚本生成的可读表格。

## 最快的找法

```bash
python3 scripts/find.py <关键词...>          # 多个关键词取交集，中英文都行
python3 scripts/find.py 手绘                  # 例：找手绘风组件库
python3 scripts/find.py mcp --module ui       # 只在 ui 模块里找
python3 scripts/find.py agent --module scaffolds
python3 scripts/find.py shadcn --json         # 输出 JSON 方便程序处理
```

找不到时打开 [INDEX.md](INDEX.md)，按分类浏览。

## 路由表：用户想要 X → 打开 Y

| 用户的需求 | 先读 | 然后 |
|---|---|---|
| 做/改网页或 App 的 UI、「做好看点」 | [ui/SKILL.md](ui/SKILL.md) | 按其中流程挑库、挑风格 |
| 想要某个动效/特效，但说不出名字 | [ui/prompts/effect-vocabulary.md](ui/prompts/effect-vocabulary.md) | [ui/catalog/09-design-vocabulary.md](ui/catalog/09-design-vocabulary.md)（motion-prompt 等画廊） |
| 指定视觉风格（手绘、复古、玻璃、粗野、终端…） | [ui/prompts/style-recipes.md](ui/prompts/style-recipes.md) | [ui/catalog/04-stylized-themes.md](ui/catalog/04-stylized-themes.md) |
| 落地页 / Hero / 炫酷动画组件 | [ui/catalog/03-animated-components.md](ui/catalog/03-animated-components.md) | [ui/catalog/06-effects-3d-shaders.md](ui/catalog/06-effects-3d-shaders.md) |
| 移动端 / React Native / Expo | [ui/catalog/05-mobile.md](ui/catalog/05-mobile.md) | [scaffolds/01-starters.md](scaffolds/01-starters.md) |
| AI 产品界面（聊天、Agent 面板、trace） | [ui/catalog/07-ai-product-ui.md](ui/catalog/07-ai-product-ui.md) | [scaffolds/02-ai-agents.md](scaffolds/02-ai-agents.md) |
| 给 Agent 装 UI 相关 MCP / 查最新文档 | [ui/catalog/12-mcp-registries-llms.md](ui/catalog/12-mcp-registries-llms.md) | |
| 新建项目、选技术栈、要脚手架 | [scaffolds/README.md](scaffolds/README.md) | [scaffolds/01-starters.md](scaffolds/01-starters.md) |
| 做 Agent / RAG / Chatbot / MCP Server | [scaffolds/02-ai-agents.md](scaffolds/02-ai-agents.md) | |
| 系统设计、架构决策、画架构图 | [scaffolds/03-architecture.md](scaffolds/03-architecture.md) | |
| 想装 Skill / 问「有没有能做 X 的 Skill」 | [skills/README.md](skills/README.md) | [skills/catalog.md](skills/catalog.md) |
| 采集小红书/抖音/B站等公开数据、浏览器自动化 | [tools/README.md](tools/README.md) | [tools/catalog.md](tools/catalog.md) |
| 中文文章去 AI 味 | [lieflat-less-ai-tone/SKILL.md](lieflat-less-ai-tone/SKILL.md) | 按该 Skill 的流程执行 |
| 本库没有的东西 | [scaffolds/04-awesome-lists.md](scaffolds/04-awesome-lists.md) | 巨型 awesome 列表、skills.sh 搜索 |
| 用户要一段能贴进任何 AI 聊天框的总提示词 | [MASTER_PROMPT.md](MASTER_PROMPT.md) | |

## 使用规则

1. **先用库里的，再上网搜。** 本库条目已核实可用；只有找不到或需要更新时才搜索网络。
2. **⭐ 表示同类首选。** 没有特殊要求时优先推荐 ⭐ 条目。
3. **安装前告诉用户。** 运行 `npx skills add`、`claude mcp add`、`npx shadcn add` 这类会改动用户项目或配置的命令之前，先说明要装什么。付费项（price=付费/免费+付费）要提醒。
4. **注意许可证与合规。** 条目描述里带 ⚠ 的要转告用户（如 Rare UI 需署名、goopUI 仅 Vue 且未发布、MediaCrawler 禁止商用）。
5. **数据会过时。** 星数、安装量、价格是 2026-11-09 的快照。用户关心时用 `python3 scripts/check_links.py` 检查链接，或上网核实。
6. **想给库加东西：** 改 `data/resources/*.json` → 运行 `python3 scripts/build.py`。不要手改生成的 catalog 文件。格式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 目录结构

```
AGENTS.md            ← 你在这里（AI 入口）
CLAUDE.md            ← 指向本文件
README.md            ← 给人看的说明
MASTER_PROMPT.md     ← 可直接粘贴进任何 AI 的总提示词
setup.sh             ← 一键检查环境 / 拉子模块 / 安装 Skill（--link-skills）
INDEX.md             ← 全部分类索引（自动生成）
ui/                  ← SKILL.md + prompts/ + catalog/（12 个分类）
skills/              ← README.md + catalog.md
tools/               ← README.md + catalog.md
scaffolds/           ← README.md + 4 个分类文件
lieflat-less-ai-tone/← 子模块 Skill：中文去 AI 味（若为空，运行 ./setup.sh）
assets/              ← README 头图（自动生成）
data/                ← categories.json + resources/*.json（唯一数据源）
scripts/             ← find.py 搜索 / build.py 生成（含 README 统计与头图）/ check_links.py 查死链
```
