# Agent Skills 目录

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

## Skill 目录站与 Awesome 列表

安装格式统一为 `npx skills add <owner/repo>`（可加 `--skill <名称>` 只装其中一个）。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [skills.sh](https://skills.sh) | Agent Skills 事实标准目录与排行榜；搜索 API：skills.sh/api/search?q=关键词 |  | `npx skills add <owner/repo>` | 免费 |
| [awesome-frontend-skills](https://github.com/finfin/awesome-frontend-skills) | 按框架/UI 库/动画/视频分类的前端 Skill |  |  | 免费 |
| [ComposioHQ awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Claude Skill 精选列表（79k★） |  |  | 免费 |
| [travisvn awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Claude Skill 精选列表（15.8k★） |  |  | 免费 |
| [vercel-labs/skills（skills CLI）](https://github.com/vercel-labs/skills) | npx skills 命令本体，支持 Claude Code / Codex / Cursor 等多种 Agent |  | `npx skills add <owner/repo> [--skill <name>]` | 免费 |
| [VoltAgent awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 1000+ 精选 Skill（37k★） |  |  | 免费 |

## 全球累计安装量 Top（skills.sh All Time，2026-11-09 实时数据）

数据来源 skills.sh 排行榜。安装量不等于独立用户数。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [agent-browser](https://github.com/vercel-labs/agent-browser) | #5（约 140 万）让 AI 自己打开、点击、操作网页 |  | `npx skills add vercel-labs/agent-browser` | 免费 |
| ⭐ [find-skills](https://github.com/vercel-labs/skills) | #1（约 430 万次安装）让 AI 自己去找需要的 Skill。建议第一个装 |  | `npx skills add vercel-labs/skills --skill find-skills` | 免费 |
| ⭐ [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | #15（约 110 万）Anthropic 官方「去 AI 味」前端 Skill |  | `npx skills add anthropics/skills --skill frontend-design` | 免费 |
| ⭐ [grill-me](https://github.com/mattpocock/skills) | #2（约 150 万）不停追问，把需求彻底问清楚 |  | `npx skills add mattpocock/skills --skill grill-me` | 免费 |
| ⭐ [setup-matt-pocock-skills](https://github.com/mattpocock/skills) | #13（约 110 万）一键配好 Matt Pocock 整套 Skills 工作流（grill/tdd/handoff/triage/prototype…） |  | `npx skills add mattpocock/skills` | 免费 |
| [design-mobile-apps](https://www.skills.sh/designed-by-ai/skills/design-mobile-apps) | #7（约 130 万）移动 App 设计 Skill（designed-by-ai/skills） |  | `npx skills add designed-by-ai/skills --skill design-mobile-apps` | 免费 |
| [diagnosing-bugs](https://github.com/mattpocock/skills) | #30（约 91 万）系统化定位 Bug |  | `npx skills add mattpocock/skills --skill diagnosing-bugs` | 免费 |
| [grill-with-docs](https://github.com/mattpocock/skills) | #9（约 130 万）拿着文档追问，专门找方案漏洞 |  | `npx skills add mattpocock/skills --skill grill-with-docs` | 免费 |
| [handoff](https://github.com/mattpocock/skills) | #14（约 110 万）换一个 AI / 新会话也能从当前进度接着干 |  | `npx skills add mattpocock/skills --skill handoff` | 免费 |
| [hyperframes 系列](https://github.com/heygen-com/hyperframes) | #3/#4（各约 150 万）HeyGen 出品，HTML→视频，含 cli、media-use、animation、registry 等子 Skill |  | `npx skills add heygen-com/hyperframes` | 免费 |
| [improve-codebase-architecture](https://github.com/mattpocock/skills) | #10（约 120 万）帮 AI 检查并重构代码架构 |  | `npx skills add mattpocock/skills --skill improve-codebase-architecture` | 免费 |
| [prototype](https://github.com/mattpocock/skills) | #18（约 110 万）快速原型 |  | `npx skills add mattpocock/skills --skill prototype` | 免费 |
| [tdd](https://github.com/mattpocock/skills) | #12（约 120 万）让 AI 按测试驱动流程写代码 |  | `npx skills add mattpocock/skills --skill tdd` | 免费 |
| [triage](https://github.com/mattpocock/skills) | #19（约 110 万）自动整理 Issue，判断下一步怎么处理 |  | `npx skills add mattpocock/skills --skill triage` | 免费 |
| [ui-taste](https://www.skills.sh/?q=ui-taste) | #16（约 110 万）UI 审美 Skill（uizze.sh）；来源非 GitHub 仓库，在 skills.sh 搜索 ui-taste 查看 |  |  | 免费 |

## 工程 / 工作流类 Skill

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | react-best-practices、web-design-guidelines、composition-patterns、react-view-transitions |  | `npx skills add vercel-labs/agent-skills` | 免费 |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 官方 Skill 仓库（docx/pdf/pptx/xlsx/frontend-design/skill-creator…） |  | `npx skills add anthropics/skills` | 免费 |
| [shadcn skill（官方）](https://ui.shadcn.com/docs/skills) | 通过 shadcn info --json 读取项目并强制 shadcn 写法；含 migrate-radix-to-base |  | `npx skills add shadcn/ui` | 免费 |

## 前端 / 设计 / 动效类 Skill

完整清单另见 ui/catalog/09-design-vocabulary.md。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [GSAP skills（官方）](https://github.com/greensock/gsap-skills) | gsap-core、scrolltrigger、timeline、react、performance… |  | `npx skills add https://github.com/greensock/gsap-skills` | 免费 |
| [Mobbin skills](https://github.com/mobbin/skills) | 配合 Mobbin MCP 的设计调研 Skill |  |  | 免费 |
| [Refero design skill](https://github.com/referodesign/refero_skill) | 先用 Refero MCP 调研真实产品再设计 |  | `npx skills add https://github.com/referodesign/refero_skill --skill refero-design` | 免费 |
| [Three.js skills](https://github.com/CloudAI-X/threejs-skills) | 基础、动画、shader、材质、几何、交互 |  | `npx skills add cloudai-x/threejs-skills` | 免费 |

## 视频 / 多媒体类 Skill

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [101-skills/superpowers](https://www.skills.sh/101-skills/superpowers) | ai-video-generation 等（Top 30 中占 4 席） |  |  | 免费 |
| [Remotion skills（官方）](https://github.com/remotion-dev/skills) | remotion-best-practices（78 万安装）、render、captions |  | `npx skills add remotion-dev/skills` | 免费 |

## 本文件夹自带的 Skill

已经在本文件夹里，无需安装。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [lieflat-less-ai-tone（本地）](./lieflat-less-ai-tone/SKILL.md) | 中文去 AI 味：脚本检测 + 语义判读 + 改写 + 前后对比报告。路径：./lieflat-less-ai-tone/SKILL.md |  | `直接读 lieflat-less-ai-tone/SKILL.md` | 免费 |
| [ui-master（本地）](./ui/SKILL.md) | 本文件夹的 UI 路由 Skill：按需求选组件库、风格、动效词汇和 MCP。路径：./ui/SKILL.md |  | `直接读 ui/SKILL.md` | 免费 |
