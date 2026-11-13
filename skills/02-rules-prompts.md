# 规则、Prompt 与子 Agent 库

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="rules-prompts"></a>

## 规则 / Prompt / 子 Agent / 规格驱动工作流

给编码 Agent 用的规则文件、现成子 Agent 和命令、Prompt 写法指南。

本类分组：规则与 AGENTS.md / CLAUDE.md · 子 Agent、命令与工作流框架 · 规格驱动开发 · 官方 Prompt 指南 · Prompt 合集 · 中文 Prompt 资源

### 规则与 AGENTS.md / CLAUDE.md

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [cursor.directory](https://cursor.directory) | 最大的 Cursor 规则社区站，按框架和语言找现成 rules 直接复制进项目时用 |  | 免费 |
| [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 把 Karpathy 对 LLM 编码常见毛病的观察整理成一份 CLAUDE.md，想让 Agent 少过度设计、少擅自改动时直接套用 | `/plugin marketplace add forrestchang/andrej-karpathy-skills`<br>`/plugin install andrej-karpathy-skills@karpathy-skills` | 免费 |
| [awesome-claude-md](https://github.com/josix/awesome-claude-md) | 收集各知名开源项目真实 CLAUDE.md 并附点评的列表，写自己的 CLAUDE.md 找范例时用 |  | 免费 |
| [awesome-cursor-rules-mdc](https://github.com/sanjeed5/awesome-cursor-rules-mdc) | 按库名整理的 .mdc 格式 Cursor 规则合集（附生成脚本），需要新版 mdc 规则文件时用 |  | 免费 |
| [Claude Code 最佳实践（官方）](https://code.claude.com/docs/en/best-practices) | Anthropic 官方总结的 Claude Code 使用方法（上下文管理、验证手段、并行会话），刚上手或想提效时读 |  | 免费 |
| [Claude Code 记忆与 CLAUDE.md 文档](https://code.claude.com/docs/en/memory) | Anthropic 官方讲 CLAUDE.md 的层级、导入语法和自动记忆，写或精简 CLAUDE.md 时读 |  | 免费 |
| [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | 社区整理的 Claude Code 实践手册（命令、子 Agent、Hook、Skill 的组合用法与示例），想系统配置 .claude 目录时参考 |  | 免费 |
| [claude-code-guide](https://github.com/zebbern/claude-code-guide) | 社区写的 Claude Code 全功能速查手册，查某个命令、配置项或技巧时用 |  | 免费 |
| [claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | 演示 Hook、Skill、子 Agent、命令和 GitHub Actions 如何配合的完整示例项目，照着搭团队级配置时用 |  | 免费 |
| [Cline Memory Bank](https://docs.cline.bot/prompting/cline-memory-bank) | Cline 官方的 Memory Bank 自定义指令方案，用一组 Markdown 文件让 Agent 跨会话保留项目上下文时用 |  | 免费 |
| [cline/prompts](https://github.com/cline/prompts) | Cline 官方的 .clinerules 与工作流提示词库，给 Cline 找现成规则时用 |  | 免费 |
| [Codex AGENTS.md 指南](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | OpenAI 官方讲 Codex 如何分层发现和合并 AGENTS.md，给 Codex 写项目指令时读 |  | 免费 |
| [Cursor Rules 官方文档](https://cursor.com/docs/context/rules) | Cursor 官方说明 .cursor/rules 与 AGENTS.md 的写法和生效范围，自己写规则前先读 |  | 免费 |
| [GitHub Copilot 自定义指令文档](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) | GitHub 官方讲 copilot-instructions.md、路径级指令和 AGENTS.md 的写法，给 Copilot 配仓库规则时读 |  | 免费 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | GitHub 官方维护的 Copilot 指令、提示词、自定义 Agent 和 Skill 合集，找各语言现成指令文件时用 |  | 免费 |
| [my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | 一套可直接抄的 Claude Code 起步配置（CLAUDE.md 记忆库、命令、子 Agent），新项目初始化 .claude 时用 |  | 免费 |
| [Ruler](https://github.com/intellectronica/ruler) | 把一份规则同步分发给 Claude Code、Cursor、Copilot 等几十种 Agent 的 CLI，团队同时用多个 Agent 时用 | `npm install -g @intellectronica/ruler`<br>ruler init | 开源 |
| [rulesync](https://github.com/dyoshikawa/rulesync) | 从统一源文件生成各家 AI 编码工具的规则、命令、MCP 和子 Agent 配置的 CLI，多工具并用时用 | rulesync init | 开源 |

### 子 Agent、命令与工作流框架

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Superpowers（obra）](https://github.com/obra/superpowers) | Star 最多的 Agent 技能与工作流框架（头脑风暴→计划→TDD→评审），想让 Agent 按严格工程流程干活时用 | `/plugin install superpowers@claude-plugins-official` | 开源 |
| [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) | 构建可靠 LLM 应用的 12 条工程原则，自己设计 Agent 架构或提示词体系前读 |  | 免费 |
| [Advanced Context Engineering for Coding Agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents) | HumanLayer 的「研究→计划→实现」上下文工程方法论，在大型存量代码库里用 Agent 时参考 |  | 免费 |
| [Claude Code Hooks 指南](https://code.claude.com/docs/en/hooks-guide) | Anthropic 官方 Hook 入门（事件类型、匹配器、示例脚本），想在工具调用前后自动跑检查时读 |  | 免费 |
| [Claude Code Templates（aitmpl）](https://www.aitmpl.com) | 可交互浏览并一键安装子 Agent、命令、Hook、MCP 和设置的模板库，快速给项目配齐 .claude 组件时用 | `npx claude-code-templates@latest` | 开源 |
| [Claude Code 子 Agent 文档](https://code.claude.com/docs/en/sub-agents) | Anthropic 官方讲子 Agent 的文件格式、工具权限和调用方式，自己写子 Agent 前读 |  | 免费 |
| [Claude Command Suite](https://github.com/qdhenry/Claude-Command-Suite) | 上百个结构化斜杠命令和 Agent 的合集（代码审查、测试、部署、项目管理），补充常用命令时用 |  | 开源 |
| [claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | 覆盖全部 Hook 事件的可运行示例仓库，学习或照抄 Claude Code Hook 脚本时用 |  | 开源 |
| [claude-code-subagents（0xfurai）](https://github.com/0xfurai/claude-code-subagents) | 100+ 个按语言和框架划分的专家型子 Agent，缺某个技术栈的专用 Agent 时来这里拿 |  | 开源 |
| [claude-mem](https://github.com/thedotmack/claude-mem) | 自动压缩并回注历史会话的 Claude Code 记忆插件，想让 Agent 记住之前会话做过什么时用 | `/plugin marketplace add thedotmack/claude-mem` | 开源 |
| [Compound Engineering 插件（Every）](https://github.com/EveryInc/compound-engineering-plugin) | Every 团队的「复利工程」插件：计划→执行→评审→沉淀经验的循环，想让每次任务都改进下一次时用 | `/plugin marketplace add EveryInc/compound-engineering-plugin` | 开源 |
| [contains-studio/agents](https://github.com/contains-studio/agents) | 按部门（工程、设计、营销、产品）划分的一套 Claude Code 子 Agent，想快速拥有全职能团队时用（⚠ 2025 年后未更新） |  | 开源 |
| [ECC（原 everything-claude-code）](https://github.com/affaan-m/ECC) | Star 极高的 Claude Code 全套配置合集（Agent、Skill、Hook、规则、MCP），想一次装好成熟工作流时用 | `/plugin marketplace add https://github.com/affaan-m/ECC`<br>`/plugin install ecc@ecc` | 开源 |
| [gstack（Garry Tan）](https://github.com/garrytan/gstack) | YC 总裁 Garry Tan 公开的 Claude Code 技能栈（规划、评审、QA、发布等角色化命令），一个人模拟整支工程团队时用 | `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` | 开源 |
| [Ralph](https://github.com/snarktank/ralph) | 让 Agent 按 PRD 逐条循环执行直到全部完成的自治循环脚本，想无人值守跑完一批任务时用 |  | 开源 |
| [Ruflo（原 claude-flow）](https://github.com/ruvnet/ruflo) | 面向 Claude Code 的多 Agent 蜂群编排平台，带记忆和大量 MCP 工具，需要大规模并行 Agent 时用（⚠ 概念多、上手成本高） | `npx ruflo init` | 开源 |
| [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 给 Claude Code 加一套 /sc: 命令、人格和 MCP 集成的元框架，想要开箱即用的结构化命令集时用 | pipx install superclaude<br>superclaude install | 开源 |
| [wshobson/agents](https://github.com/wshobson/agents) | 最大的 Claude Code 插件市场之一，含上百个专业子 Agent、命令和 Skill，按领域（后端、安全、数据等）装插件时用 | `/plugin marketplace add wshobson/agents` | 开源 |

### 规格驱动开发

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [GitHub Spec Kit](https://github.com/github/spec-kit) | GitHub 官方的规格驱动开发工具包（constitution→specify→plan→tasks→implement），新功能想先写规格再让 Agent 实现时用 | `uv tool install specify-cli`<br>specify init my-project --integration copilot（--integration 换成你用的 Agent） | 开源 |
| [Agent OS](https://github.com/buildermethods/agent-os) | 用标准、产品和规格三层文档约束 Agent 的规格驱动系统，想把团队编码规范固化给 Agent 时用 |  | 开源 |
| [ai-dev-tasks](https://github.com/snarktank/ai-dev-tasks) | 三个 Markdown 提示文件（生成 PRD→拆任务→逐条执行），想要最简单的规格流程时用 |  | 开源 |
| [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 用分析师、PM、架构师、开发等角色 Agent 走完敏捷流程的方法论框架，做较大项目需要完整 PRD 和架构文档时用 | `npx bmad-method install` | 开源 |
| [cc-sdd](https://github.com/gotalab/cc-sdd) | 把 Kiro 式规格流程装进 Claude Code、Codex、Cursor 等的命令包，支持中文，想用 /kiro: 系列命令时用 | `npx cc-sdd@latest` | 开源 |
| [context-engineering-intro（PRP）](https://github.com/coleam00/context-engineering-intro) | 上下文工程与 PRP（Product Requirements Prompt）方法的入门模板，学习如何给 Agent 准备完整上下文时用 |  | 开源 |
| [Kiro Specs 文档](https://kiro.dev/docs/specs/) | Kiro 官方讲 requirements→design→tasks 三段式规格流程，想在其他 Agent 里复刻 Kiro 式工作流时参考 |  | 免费 |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | 轻量的规格驱动框架，用变更提案和增量规格管理需求，给存量项目加规格流程时用 | `npm install -g @fission-ai/openspec@latest`<br>openspec init | 开源 |
| [PRP（Wirasm）](https://github.com/Wirasm/prp) | 一套 PRP 提示词与 Claude Code 命令，把需求写成可一次实现的产品需求提示时用 |  | 开源 |

### 官方 Prompt 指南

| 名称 | 是什么 / 什么时候用 | 价格 |
|---|---|---|
| ⭐ [Claude Prompt 工程指南（官方）](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Anthropic 官方 Prompt 工程文档（清晰指令、示例、XML 标签、思考、长上下文），给 Claude 写提示词前读 | 免费 |
| [Anthropic Prompt Library](https://platform.claude.com/docs/en/resources/prompt-library/library) | Anthropic 官方的现成提示词库，按任务找可直接改用的范例时用 | 免费 |
| [Anthropic Prompt 工程互动教程](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic 官方 9 章 Jupyter 互动教程，想系统练习提示词技巧时用 | 开源 |
| [Azure OpenAI Prompt 工程技巧](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering) | 微软官方 Prompt 工程文档，在 Azure OpenAI / Foundry 上部署模型时参考 | 免费 |
| [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | Anthropic 讲工作流与 Agent 常见模式（链式、路由、并行、编排、评估优化）的经典文章，设计 Agent 架构前读 | 免费 |
| [Claude 系统提示词（官方公开）](https://platform.claude.com/docs/en/release-notes/system-prompts) | Anthropic 官方公布的 Claude 各版本系统提示词，学习官方如何写长系统提示时读 | 免费 |
| [Codex Prompting Guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) | OpenAI 官方 Codex 模型提示指南，强调「少即是多」，给 Codex 写系统提示或 AGENTS.md 时读 | 免费 |
| [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anthropic 讲上下文工程（系统提示、工具、压缩、子 Agent）的文章，Agent 长任务跑偏或上下文爆满时读 | 免费 |
| [Gemini Cookbook](https://github.com/google-gemini/cookbook) | Google 官方 Gemini API 示例与指南合集，找多模态、函数调用、Live API 的可运行范例时用 | 开源 |
| [Gemini for Workspace Prompt 指南](https://workspace.google.com/learning/content/gemini-prompt-guide) | Google 面向办公场景的提示词手册（角色、任务、上下文、格式四要素），教非技术同事写提示词时用 | 免费 |
| [Gemini Prompt 设计策略](https://ai.google.dev/gemini-api/docs/prompting-strategies) | Google 官方 Gemini 提示策略文档（指令、少样本、上下文、Gemini 3 注意事项），给 Gemini 写提示词前读 | 免费 |
| [GPT-5 Prompting Guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide) | OpenAI 官方 GPT-5 提示指南（Agent 主动性、工具前言、推理强度），给 GPT-5 系列写 Agent 提示时读 | 免费 |
| [OpenAI Cookbook](https://developers.openai.com/cookbook) | OpenAI 官方示例与指南合集（含各代模型的 Prompting Guide），找 OpenAI API 实战范例时用 | 免费 |
| [OpenAI Prompt 工程指南](https://developers.openai.com/api/docs/guides/prompt-engineering) | OpenAI 官方 Prompt 工程文档（消息角色、推理模型、结构化输出），给 GPT 系列写提示词前读 | 免费 |
| [Vertex AI Prompt 设计入门](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design) | Google Cloud 官方提示设计文档，按组件拆解提示词结构，在 Vertex AI 上做企业级提示时读 | 免费 |
| [Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Anthropic 讲如何给 Agent 设计和评估工具的文章，写 MCP 工具描述和返回值时读 | 免费 |

### Prompt 合集

| 名称 | 是什么 / 什么时候用 | 价格 |
|---|---|---|
| [awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) | ChatGPT、Claude、v0、Cursor、Manus 等产品系统提示词合集并附写法分析，学习 Agent 系统提示结构时用（⚠ 含非官方流出内容） | 免费 |
| [Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) | Prompt 工程论文、工具、课程和社区的精选列表，做调研或找工具时用 | 免费 |
| [awesome-prompts（ai-boost）](https://github.com/ai-boost/awesome-prompts) | GPT Store 高分 GPTs 的提示词和提示工程进阶资料合集，参考成熟产品级提示时用（⚠ 部分为非官方流出内容） | 免费 |
| [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt) | 大量 GPTs 的系统提示词及提示注入防护知识合集，研究 GPTs 写法和防泄露时用（⚠ 非官方流出内容） | 免费 |
| [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | 各大 AI 产品与 Agent 系统提示词的流出合集，研究厂商如何写系统提示时参考（⚠ 非官方泄露内容，真实性和时效无保证） | 免费 |
| [claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | 按版本从 Claude Code 中提取的系统提示、工具描述和子 Agent 提示，研究 Claude Code 内部提示设计时用（⚠ 非官方提取） | 免费 |
| [LangChain Hub](https://smith.langchain.com/hub) | LangSmith 上的公开提示词仓库，可版本化拉取，做 LangChain 应用找现成 prompt 时用 | 免费+付费 |
| [Learn Prompting](https://learnprompting.org) | 免费的 Prompt 工程课程站，从零入门到进阶和提示注入防护，带新人入门时用 | 免费+付费 |
| [Prompt Engineering Guide（DAIR.AI）](https://www.promptingguide.ai) | 最全面的开源 Prompt 工程指南（技术、论文、模型笔记，有中文版），系统学习或查某种提示技术时用 | 免费 |
| [TheBigPromptLibrary](https://github.com/0xeb/TheBigPromptLibrary) | 系统提示、自定义指令、越狱与防护提示的大型合集，做提示安全研究或找范例时用（⚠ 含非官方流出内容） | 免费 |

### 中文 Prompt 资源

| 名称 | 是什么 / 什么时候用 | 价格 |
|---|---|---|
| ⭐ [LangGPT](https://github.com/langgptai/LangGPT) | 国内最知名的结构化提示词方法论（Role / Rules / Workflow 模板），想用模板化方式写中文提示词时用 | 免费 |
| [awesome-chatgpt-zh](https://github.com/EmbraceAGI/awesome-chatgpt-zh) | ChatGPT 中文指南与提示词、工具、应用资源合集，找中文 AI 使用资料时用 | 免费 |
| [awesome-claude-prompts](https://github.com/langgptai/awesome-claude-prompts) | 面向 Claude 的提示词精选合集，找适配 Claude 的现成提示时用 | 免费 |
| [Claude 提示工程指南（中文）](https://platform.claude.com/docs/zh-CN/build-with-claude/prompt-engineering/overview) | Anthropic 官方 Prompt 工程文档的简体中文版，中文读者给 Claude 写提示词前读 | 免费 |
| [lijigang/prompts](https://github.com/lijigang/prompts) | 李继刚早期公开的结构化提示词合集，学习其「角色 + 约束 + 流程」写法时参考（⚠ 2023 年后未更新，新作见 ljg-skills） | 免费 |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 国人整理的热门 GPTs 提示词流出合集，参考成熟 GPTs 的提示结构时用（⚠ 非官方泄露内容，2024 年后未更新） | 免费 |
| [wonderful-prompts](https://github.com/langgptai/wonderful-prompts) | LangGPT 社区精选的中文提示词合集，找可直接使用的中文场景提示词时用 | 免费 |
| [提示工程指南（中文版）](https://www.promptingguide.ai/zh) | DAIR.AI Prompt Engineering Guide 的官方中文版，想用中文系统学习提示技术时读 | 免费 |
| [面向开发者的 LLM 入门教程（Datawhale）](https://github.com/datawhalechina/llm-cookbook) | 吴恩达大模型系列课程的中文版（含提示工程、LangChain、RAG），中文开发者系统入门时用 | 免费 |
