# AI 编码工具与建站工具

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="tools-ai-builders"></a>

## AI 编码 Agent、IDE 与应用生成器

这些工具本身。用户问「有什么工具能做 X」时从这里答。

本类分组：终端编码 Agent · AI IDE 与编辑器插件 · 应用 / 网站生成器 · 云端自主 Agent · 多 Agent 编排与辅助 · 国内工具

### 终端编码 Agent

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Claude Code](https://claude.com/product/claude-code) | Anthropic 官方的终端编码 Agent（也有 IDE、桌面和网页版），支持子 Agent、Hook、Skill、MCP 和插件，做复杂多文件工程任务时首选（⚠ 需 Claude 订阅或 API） | `curl -fsSL https://claude.ai/install.sh \| bash` | 付费 |
| ⭐ [Codex CLI](https://github.com/openai/codex) | OpenAI 开源的终端编码 Agent（Rust 实现，带沙箱），已有 ChatGPT 订阅或想用 GPT-5 系列写代码时用 | `npm install -g @openai/codex` | 开源 |
| [Aider](https://aider.chat) | 老牌开源结对编程 CLI，每次改动自动 git commit，想要可控、按 diff 精确改代码时用 | python -m pip install aider-install<br>aider-install | 开源 |
| [Amp](https://ampcode.com) | Sourcegraph 团队出品的编码 Agent（CLI 与编辑器扩展），主打免调参的强模型组合和团队共享线程（⚠ 按用量付费） |  | 付费 |
| [Auggie CLI（Augment Code）](https://www.augmentcode.com) | Augment 的编码 Agent（IDE 扩展与 Auggie CLI），以大型代码库上下文引擎见长，仓库很大时用（⚠ 付费订阅） | `npm install -g @augmentcode/auggie@latest` | 付费 |
| [Crush](https://github.com/charmbracelet/crush) | Charm 出品的高颜值终端编码 Agent，支持多模型、LSP 和 MCP，喜欢 TUI 体验时用 | `npm install -g @charmland/crush` | 开源 |
| [Cursor CLI](https://cursor.com/cli) | Cursor 的终端 Agent，可在任意终端或 CI 里用 Cursor 的模型和规则，需要无头运行时用 | `curl https://cursor.com/install -fsS \| bash` | 付费 |
| [Droid（Factory）](https://factory.com) | Factory 的企业级编码 Agent（CLI 与云端），强调与工单、CI 和代码评审流程打通（⚠ 付费为主） |  | 付费 |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google 开源的终端 Agent，个人账号有较大免费额度和超长上下文，想免费体验或处理超大代码库时用 | `npm install -g @google/gemini-cli` | 开源 |
| [GitHub Copilot CLI](https://github.com/github/copilot-cli) | GitHub 官方的终端 Agent，与仓库、Issue、PR 深度集成，已有 Copilot 订阅时在终端里用 | `npm install -g @github/copilot` | 付费 |
| [Goose](https://github.com/aaif-goose/goose) | Block 发起、现归属 Agentic AI Foundation 的开源本地 Agent（CLI 与桌面端），以 MCP 扩展为核心，想要可自由扩展的通用 Agent 时用 | `curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh \| bash` | 开源 |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Nous Research 开源的自我改进型个人 Agent，可长期运行并自己沉淀技能，想要常驻助手时用 | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` | 开源 |
| [OpenClaw](https://github.com/openclaw/openclaw) | 现象级开源个人 AI 助手，常驻本机并通过聊天软件接收指令、调用技能，想要 7×24 私人 Agent 时用（⚠ 权限很大，注意隔离环境） | `npm install -g openclaw@latest --allow-scripts=openclaw` | 开源 |
| [OpenCode](https://opencode.ai) | Star 最多的开源终端编码 Agent，可接任意模型供应商，不想被单一厂商锁定时用 | `curl -fsSL https://opencode.ai/v2/install \| bash` | 开源 |
| [OpenHands](https://github.com/OpenHands/OpenHands) | 开源的自主软件工程 Agent 平台（CLI、本地 GUI 和云端），想自托管类 Devin 体验时用 |  | 开源 |
| [Pi](https://github.com/earendil-works/pi) | 极简、可高度定制的开源终端编码 Agent 工具包（OpenClaw 的底层），想自己拼装 Agent 或研究最小实现时用 |  | 开源 |

### AI IDE 与编辑器插件

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Cursor](https://cursor.com) | 最流行的 AI 原生 IDE（VS Code 分支），带 Tab 补全、Agent 和云端 Agent，日常主力 AI 编辑器首选（⚠ 高阶模型需订阅） |  | 免费+付费 |
| [Cline](https://cline.bot) | 开源的 VS Code / JetBrains 自主编码 Agent（也有 CLI），Plan / Act 双模式且自带模型密钥，想透明控制每一步时用 | `npm i -g cline` | 开源 |
| [Continue](https://continue.dev) | 开源的 IDE 助手与 CLI，可自定义模型、规则和后台 Agent，想自建团队统一的 AI 编码配置时用 |  | 开源 |
| [Devin Desktop（原 Windsurf）](https://devin.ai/desktop) | 原 Windsurf，被 Cognition 收购后更名为 Devin Desktop 的 AI IDE，带 Cascade Agent 和自动上下文感知，想要 Cursor 之外的选择时用 |  | 免费+付费 |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub 的 AI 编程助手（补全、聊天、Agent 模式、云端编码 Agent），在 VS Code / JetBrains 里使用或团队已采购时用 |  | 免费+付费 |
| [Google Antigravity](https://antigravity.google) | Google 的 Agent 优先 IDE，可并行管理多个 Agent 并用浏览器自测，想体验 Gemini 3 系列的完整 Agent 工作台时用 |  | 免费+付费 |
| [JetBrains Junie](https://junie.jetbrains.com) | JetBrains 官方编码 Agent，深度利用 IDE 的索引与检查，JetBrains 用户不想换编辑器时用（⚠ 需 JetBrains AI 订阅） |  | 付费 |
| [Kilo Code](https://kilo.ai) | 开源编码 Agent（VS Code、JetBrains 与 CLI），融合 Cline / Roo 的特性并提供多模型网关，想要开源且功能全的插件时用 | `npm install -g @kilocode/cli` | 开源 |
| [Kiro](https://kiro.dev) | AWS 出品的规格驱动 AI IDE 与 CLI（需求→设计→任务），想让 Agent 先写规格再编码时用 |  | 免费+付费 |
| [Tabby](https://github.com/TabbyML/tabby) | 可自托管的开源 AI 编码助手服务，代码不能出内网、需要私有化补全与问答时用 |  | 开源 |
| [Warp](https://www.warp.dev) | 内置 Agent 的现代终端 / Agent 开发环境，可同时管理多个 Agent 会话，重度终端用户用 |  | 免费+付费 |
| [Zed](https://zed.dev) | Rust 写的高性能开源编辑器，内置 Agent 面板并可通过 ACP 接 Claude Code、Codex、Gemini CLI，追求速度时用 |  | 免费+付费 |

### 应用 / 网站生成器

| 名称 | 是什么 / 什么时候用 | 技术栈 | 价格 |
|---|---|---|---|
| ⭐ [v0（Vercel）](https://v0.app) | Vercel 的 AI 应用生成器，产出 Next.js + shadcn/ui 代码并一键部署，做 React 界面和全栈原型首选 | Next.js, shadcn/ui | 免费+付费 |
| [Base44](https://base44.com) | Wix 旗下的一体化 AI 应用生成器，内置数据库、鉴权和托管，做内部工具时用 |  | 免费+付费 |
| [bolt.diy](https://github.com/stackblitz-labs/bolt.diy) | Bolt.new 的官方开源版，可自选任意模型并本地运行，想自托管应用生成器时用 |  | 开源 |
| [Bolt.new](https://bolt.new) | StackBlitz 的浏览器内全栈生成器，基于 WebContainers 即时运行，想在浏览器里边聊边跑代码时用 |  | 免费+付费 |
| [Dyad](https://www.dyad.sh) | 本地运行的开源应用生成器，代码留在自己电脑并可自带 API key，想要免订阅的 Lovable 替代时用 |  | 开源 |
| [Emergent](https://emergent.sh) | 多 Agent 协作的全栈应用生成平台，可产出 Web 与移动端并部署，想要更高自动化程度时用 |  | 免费+付费 |
| [Figma Make](https://www.figma.com/make/) | Figma 内置的 prompt-to-app 工具，可把现有设计稿变成可交互原型，设计师验证交互时用（⚠ 需 Figma 付费席位才有完整额度） |  | 免费+付费 |
| [Firebase Studio](https://firebase.studio) | Google 的云端 AI 开发环境（原 Project IDX），用 Gemini 原型化并直连 Firebase 后端，做 Google 生态全栈应用时用 |  | 免费+付费 |
| [Framer AI](https://www.framer.com/ai/) | Framer 的 AI 建站功能，生成并可视化编辑响应式营销站，做落地页且要直接托管时用 |  | 免费+付费 |
| [Google Stitch](https://stitch.withgoogle.com) | Google Labs 的 AI 界面设计工具，从文字或草图生成多屏 UI 并导出代码或 Figma，做界面探索时用 |  | 免费 |
| [Lovable](https://lovable.dev) | 对话式全栈应用生成器（React + Supabase），非技术用户想从想法直接做出可上线产品时用 | React, Supabase | 免费+付费 |
| [Magic Patterns](https://www.magicpatterns.com) | 面向产品团队的 AI 原型工具，可导入自家设计系统生成界面并导出 React / Figma，做产品原型评审时用 |  | 免费+付费 |
| [Onlook](https://onlook.com) | 开源的「设计师版 Cursor」，可视化编辑真实 Next.js + Tailwind 代码，想像在 Figma 里一样直接改 React 界面时用 | Next.js, Tailwind | 开源 |
| [Readdy](https://readdy.ai) | 从文字生成网站设计稿并导出代码 / Figma 的 AI 工具，快速出官网和落地页视觉时用 |  | 免费+付费 |
| [Replit Agent](https://replit.com) | Replit 的云端应用构建 Agent，自带数据库、鉴权和部署，零本地环境做出可托管应用时用 |  | 免费+付费 |
| [Rork](https://rork.com) | 专做移动端的 AI 应用生成器，输出 React Native / Expo 应用并协助上架，做原生 App 原型时用 | React Native, Expo | 免费+付费 |
| [Same](https://same.new) | 擅长按 URL 像素级复刻网站的全栈生成器，想快速克隆某个参考站再改造时用 |  | 免费+付费 |
| [Webflow AI](https://webflow.com/ai) | Webflow 的 AI 站点与应用生成能力，基于自家设计系统和 CMS，团队已在用 Webflow 时用 |  | 免费+付费 |

### 云端自主 Agent

| 名称 | 是什么 / 什么时候用 | 价格 |
|---|---|---|
| [Claude Code 网页版](https://claude.ai/code) | 在 Anthropic 云端沙箱里运行的 Claude Code，连接 GitHub 后可在浏览器或手机上并行派任务，离开电脑也想推进工作时用 | 付费 |
| [Codex（云端）](https://chatgpt.com/codex) | OpenAI 的云端编码 Agent，在 ChatGPT 里并行委派任务并生成 PR，已有 ChatGPT 付费订阅时用 | 付费 |
| [Devin](https://devin.ai) | Cognition 的云端自主软件工程师，可在自己的沙箱里接工单、写代码并提 PR，把明确的任务整块外包时用（⚠ 付费） | 付费 |
| [Genspark](https://www.genspark.ai) | 集搜索、幻灯片、表格和建站于一体的通用 Agent 工作台，做调研汇报类交付物时用 | 免费+付费 |
| [GitHub Copilot 编码 Agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) | 把 Issue 指派给 Copilot 后在 GitHub Actions 环境里自主实现并提 PR 的云端 Agent，团队流程都在 GitHub 上时用 | 付费 |
| [Jules](https://jules.google) | Google 的异步云端编码 Agent，连接 GitHub 仓库后在云端 VM 里执行任务并提 PR，有免费额度 | 免费+付费 |
| [Manus](https://manus.im) | 通用型云端自主 Agent，可完成调研、数据分析、建站等长流程任务，需要端到端交付结果而非只写代码时用 | 免费+付费 |

### 多 Agent 编排与辅助

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [Beads](https://github.com/gastownhall/beads) | 给编码 Agent 用的 git 原生 Issue 追踪与长期记忆工具，任务跨多次会话时用来保存计划和依赖 |  | `brew install beads` | 开源 |
| [ccusage](https://github.com/ccusage/ccusage) | 读取本地日志统计 Claude Code / Codex 等的 token 用量和费用的 CLI，想知道每天花了多少时用 |  | `npx ccusage@latest` | 开源 |
| [Claude Code Action](https://github.com/anthropics/claude-code-action) | Anthropic 官方 GitHub Action，在 PR / Issue 里 @claude 触发评审或实现，把 Claude Code 接进 CI 时用 |  |  | 开源 |
| [Claude Code Router](https://github.com/musistudio/claude-code-router) | 把 Claude Code 的请求路由到其他模型供应商的代理，想在 Claude Code 里用 DeepSeek、Gemini 或本地模型时用（⚠ 非官方，第三方模型效果不保证） |  | `npm install -g @musistudio/claude-code-router` | 开源 |
| [Claude Code UI（CloudCLI）](https://github.com/siteboon/claudecodeui) | 开源的 Web / 移动端界面，远程管理 Claude Code、Cursor CLI、Codex 会话，想在浏览器里操作本机 Agent 时用 |  | `npx @cloudcli-ai/cloudcli` | 开源 |
| [Claude Squad](https://github.com/smtg-ai/claude-squad) | 用 tmux 和 git worktree 管理多个终端 Agent 会话的 TUI，纯终端环境下并行多任务时用 |  | `brew install claude-squad` | 开源 |
| [cmux](https://github.com/manaflow-ai/cmux) | 为并行编码 Agent 设计的 macOS 终端（竖排标签、通知、内置浏览器），同时盯多个 Agent 会话时用（⚠ 仅 macOS） | macOS |  | 开源 |
| [Conductor](https://conductor.build) | 在 Mac 上用独立 git worktree 并行跑多个 Claude Code / Codex 的桌面应用，同时推进多个任务并逐个评审时用（⚠ 仅 macOS） | macOS |  | 免费 |
| [Container Use（Dagger）](https://github.com/dagger/container-use) | 给每个编码 Agent 独立容器和 git 分支的 MCP 工具，想让多个 Agent 安全并行且互不污染环境时用 |  | `brew install dagger/tap/container-use`<br>`claude mcp add container-use -- container-use stdio` | 开源 |
| [Gas Town](https://github.com/gastownhall/gastown) | Steve Yegge 的多 Agent 工作区管理器，在 Beads 之上编排几十个并行 Agent，想尝试大规模 Agent 车间时用（⚠ 实验性强） |  |  | 开源 |
| [Happy](https://github.com/slopus/happy) | Claude Code / Codex 的开源手机与网页客户端，端到端加密，想在手机上远程查看和操控本机会话时用 |  | `npm install -g happy` | 开源 |
| [opcode](https://github.com/winfunc/opcode) | Claude Code 的开源桌面 GUI（原 Claudia），可视化管理会话、自定义 Agent 和用量，不想只用终端时用 |  |  | 开源 |
| [Task Master](https://github.com/eyaltoledano/claude-task-master) | 把 PRD 拆成带依赖的任务清单并逐条喂给 Agent 的任务管理工具（CLI + MCP），项目较大需要 Agent 按计划推进时用 |  | `npm install -g task-master-ai`<br>`claude mcp add taskmaster-ai -- npx -y task-master-ai` | 开源 |
| [Vibe Kanban](https://github.com/BloopAI/vibe-kanban) | 用看板编排多个编码 Agent 的开源工具，每张卡片在独立 worktree 里执行并可逐个评审合并 |  | `npx vibe-kanban` | 开源 |

### 国内工具

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Trae（字节跳动）](https://www.trae.ai) | 字节出品的 AI IDE（国内版 trae.cn），提供 Builder / SOLO 模式和免费模型额度，国内网络环境下想要 Cursor 式体验时用 |  | 免费+付费 |
| [CC Switch](https://github.com/farion1231/cc-switch) | 一键切换 Claude Code / Codex / Gemini CLI 供应商配置的桌面工具，同时使用多家中转或国产模型 API 时用 | `brew install --cask cc-switch` | 开源 |
| [CodeBuddy（腾讯）](https://www.codebuddy.cn) | 腾讯的 AI 编程助手（IDE、插件与 CLI），集成微信小程序和腾讯云部署链路，做小程序或用腾讯云时用 |  | 免费+付费 |
| [Coze Studio（开源版）](https://github.com/coze-dev/coze-studio) | 扣子的开源版 Agent 开发平台，可私有化部署可视化工作流和知识库，需要自托管 Coze 能力时用 |  | 开源 |
| [DeerFlow（字节）](https://github.com/bytedance/deer-flow) | 字节开源的深度研究 / 超级 Agent 框架，带沙箱、记忆和子 Agent，想自托管类 Manus 的长任务 Agent 时用 |  | 开源 |
| [iFlow CLI（心流）](https://github.com/iflow-ai/iflow-cli) | 阿里心流团队的终端 Agent，免费提供多款国产模型，国内想零成本体验终端编码 Agent 时用 | `npm i -g @iflow-ai/iflow-cli` | 免费 |
| [MiniMax Agent](https://agent.minimax.io) | MiniMax 的通用自主 Agent，可生成全栈应用、幻灯片和多媒体内容，想用国产模型做端到端交付时用 |  | 免费+付费 |
| [Qoder（阿里）](https://qoder.com) | 阿里推出的 Agentic 编码平台（IDE 与 CLI），带 Quest 任务委派和 Repo Wiki，需要长任务委派和代码库知识沉淀时用 |  | 免费+付费 |
| [Qwen Code](https://github.com/QwenLM/qwen-code) | 阿里通义团队开源的终端编码 Agent（源自 Gemini CLI），适配 Qwen Coder 模型并有免费额度，国内想用开源 CLI 时用 | `npm install -g @qwen-code/qwen-code@latest` | 开源 |
| [YouWare](https://www.youware.com) | 面向非程序员的 vibe coding 社区与生成平台，生成网页作品并一键分享时用 |  | 免费+付费 |
| [ZCF（Zero-Config Code Flow）](https://github.com/UfoMiao/zcf) | 中文友好的 Claude Code / Codex 一键配置工具，自动装好工作流、MCP 和 API 设置，国内新手初始化环境时用 | `npx zcf` | 开源 |
| [扣子 Coze](https://www.coze.cn) | 字节的零代码 Agent / 工作流搭建平台（国际版 coze.com），做聊天机器人和业务自动化并发布到飞书、微信等渠道时用 |  | 免费+付费 |
| [文心快码 Comate（百度）](https://comate.baidu.com) | 百度的 AI 编码助手（插件与独立 IDE），支持 Zulu Agent 和私有化部署，百度系或国企合规场景用 |  | 免费+付费 |
| [秒哒（百度）](https://www.miaoda.cn) | 百度的对话式无代码应用生成平台，中文用户零基础做小工具和活动页并直接上线时用 |  | 免费+付费 |
| [通义灵码](https://lingma.aliyun.com) | 阿里云的 AI 编码助手（IDE 插件与 Lingma IDE），个人版免费，企业内网或国内合规场景用 |  | 免费+付费 |
