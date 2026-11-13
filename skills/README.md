# Agent Skills

Skill 是一个带 `SKILL.md` 的文件夹，教 Agent 按特定流程做某件事。Claude Code、Codex、Cursor 等都支持。完整清单见 [catalog.md](catalog.md)（排行榜 + 工程 / 前端 / 视频 / 其他领域 + 厂商官方 Skill）。规则文件、CLAUDE.md / AGENTS.md 范例、子 Agent 集合、规格驱动工作流和 Prompt 指南在 [02-rules-prompts.md](02-rules-prompts.md)。

## 怎么装

```bash
npx skills add <owner/repo>                      # 装整个仓库里的所有 Skill
npx skills add <owner/repo> --skill <名称>        # 只装其中一个
npx skills add https://github.com/<owner>/<repo>  # 直接用 GitHub URL 也可以
```

- 不在 skills.sh 上列出的仓库也能装，只要仓库里有 `SKILL.md`（例如 `showheyohtaki/motion-prompt`）
- 搜索：网页 [skills.sh](https://skills.sh)，或 API `https://skills.sh/api/search?q=<关键词>`
- Claude Code 也支持插件市场：`/plugin marketplace add <owner/repo>`，然后 `/plugin install <name>@<marketplace>`

## 推荐起步包

| 用途 | 命令 |
|---|---|
| 让 AI 自己找 Skill（排行 #1） | `npx skills add vercel-labs/skills --skill find-skills` |
| 需求追问、TDD、交接、架构等整套工作流 | `npx skills add mattpocock/skills` |
| 前端审美基线 | `npx skills add anthropics/skills --skill frontend-design` |
| 动效词汇（192 个带演示的效果） | `npx skills add showheyohtaki/motion-prompt` |
| React/Next 最佳实践 + 界面规范审查 | `npx skills add vercel-labs/agent-skills` |
| 浏览器自动化 | `npx skills add vercel-labs/agent-browser` |

## 排行榜说明

`catalog.md` 里的「全球累计安装量 Top」来自 skills.sh All Time 排行（2026-11-09 抓取），按名次排列。排行榜变化很快：2026 年 9 月时前十几乎全是 find-skills 和 Matt Pocock 的工作流 Skill，之后 HeyGen 的 hyperframes 系列、design-mobile-apps、ui-taste 等冲进了前列。安装量不等于独立用户数，要最新数据直接看 [skills.sh](https://skills.sh)。

## 本文件夹自带的 Skill

| Skill | 路径 | 用途 |
|---|---|---|
| ui-master | [../ui/SKILL.md](../ui/SKILL.md) | UI 需求路由：挑组件库、风格、动效术语、MCP |
| lieflat-less-ai-tone | [../lieflat-less-ai-tone/SKILL.md](../lieflat-less-ai-tone/SKILL.md) | 中文文章去 AI 味 |

想在任何项目里都能用：

- Claude Code：在仓库根目录运行 `./setup.sh --link-skills`（软链接到 `~/.claude/skills/`，保留搜索脚本）。
- 任何 Agent：`npx skills add Horace-Maxwell/ai-master-prompt` 安装 ui-master（带目录和词汇表，不带搜索脚本）；`npx skills add larashero3-dotcom/lieflat-less-ai-tone` 安装去 AI 味。
