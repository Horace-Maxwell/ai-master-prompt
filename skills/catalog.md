# Agent Skills 目录

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="skills-directories"></a>

## Skill 目录站与 Awesome 列表

安装格式统一为 `npx skills add <owner/repo>`（可加 `--skill <名称>` 只装其中一个）。

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [skills.sh](https://skills.sh) | Agent Skills 事实标准目录与排行榜；搜索 API：skills.sh/api/search?q=关键词 | `npx skills add <owner/repo>` | 免费 |
| [awesome-frontend-skills](https://github.com/finfin/awesome-frontend-skills) | 按框架/UI 库/动画/视频分类的前端 Skill |  | 免费 |
| [ComposioHQ awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Claude Skill 精选列表（79k★） |  | 免费 |
| [travisvn awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Claude Skill 精选列表（15.8k★） |  | 免费 |
| [vercel-labs/skills（skills CLI）](https://github.com/vercel-labs/skills) | npx skills 命令本体，支持 Claude Code / Codex / Cursor 等多种 Agent | `npx skills add <owner/repo> [--skill <name>]` | 免费 |
| [VoltAgent awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 1000+ 精选 Skill（37k★） |  | 免费 |

<a id="skills-top"></a>

## 全球累计安装量 Top（skills.sh All Time，2026-11-09 实时数据）

数据来源 skills.sh All Time 排行榜（2026-11-09 抓取），按名次排列。安装量不等于独立用户数。

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [find-skills](https://github.com/vercel-labs/skills) | #1（约 430 万次安装）让 AI 自己去找需要的 Skill。建议第一个装 | `npx skills add vercel-labs/skills --skill find-skills` | 免费 |
| ⭐ [grill-me](https://github.com/mattpocock/skills) | #2（约 150 万）不停追问，把需求彻底问清楚 | `npx skills add mattpocock/skills --skill grill-me` | 免费 |
| [hyperframes 系列](https://github.com/heygen-com/hyperframes) | #3/#4（各约 150 万）HeyGen 出品，HTML→视频，含 cli、media-use、animation、registry 等子 Skill | `npx skills add heygen-com/hyperframes` | 免费 |
| ⭐ [agent-browser](https://github.com/vercel-labs/agent-browser) | #5（约 140 万）让 AI 自己打开、点击、操作网页 | `npx skills add vercel-labs/agent-browser` | 免费 |
| [design-mobile-apps](https://www.skills.sh/designed-by-ai/skills/design-mobile-apps) | #7（约 130 万）移动 App 设计 Skill（designed-by-ai/skills） | `npx skills add designed-by-ai/skills --skill design-mobile-apps` | 免费 |
| [grill-with-docs](https://github.com/mattpocock/skills) | #9（约 130 万）拿着文档追问，专门找方案漏洞 | `npx skills add mattpocock/skills --skill grill-with-docs` | 免费 |
| [improve-codebase-architecture](https://github.com/mattpocock/skills) | #10（约 120 万）帮 AI 检查并重构代码架构 | `npx skills add mattpocock/skills --skill improve-codebase-architecture` | 免费 |
| [tdd](https://github.com/mattpocock/skills) | #12（约 120 万）让 AI 按测试驱动流程写代码 | `npx skills add mattpocock/skills --skill tdd` | 免费 |
| ⭐ [setup-matt-pocock-skills](https://github.com/mattpocock/skills) | #13（约 110 万）一键配好 Matt Pocock 整套 Skills 工作流（grill/tdd/handoff/triage/prototype…）。装完后在 Agent 里运行 /setup-matt-pocock-skills | `npx skills add mattpocock/skills --skill setup-matt-pocock-skills` | 免费 |
| [handoff](https://github.com/mattpocock/skills) | #14（约 110 万）换一个 AI / 新会话也能从当前进度接着干 | `npx skills add mattpocock/skills --skill handoff` | 免费 |
| ⭐ [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | #15（约 110 万）Anthropic 官方「去 AI 味」前端 Skill | `npx skills add anthropics/skills --skill frontend-design` | 免费 |
| [ui-taste](https://www.skills.sh/site/uizze.sh/ui-taste) | #16（约 110 万）UI 审美 Skill，来自 uizze.sh（不是 GitHub 仓库） | `npx skills add https://uizze.sh/` | 免费 |
| [prototype](https://github.com/mattpocock/skills) | #18（约 110 万）快速原型 | `npx skills add mattpocock/skills --skill prototype` | 免费 |
| [triage](https://github.com/mattpocock/skills) | #19（约 110 万）自动整理 Issue，判断下一步怎么处理 | `npx skills add mattpocock/skills --skill triage` | 免费 |
| [diagnosing-bugs](https://github.com/mattpocock/skills) | #30（约 91 万）系统化定位 Bug | `npx skills add mattpocock/skills --skill diagnosing-bugs` | 免费 |

<a id="skills-engineering"></a>

## 工程 / 工作流类 Skill

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Addy Osmani 的工程实践 Skill 集（code-review-and-quality 约 8.4 万安装），覆盖规格、评审、安全加固和性能，想要资深工程师流程时用 | `npx skills add addyosmani/agent-skills` | 免费 |
| ⭐ [Supabase agent-skills（官方）](https://github.com/supabase/agent-skills) | Supabase 官方 Skill（supabase-postgres-best-practices 约 48 万安装），写 Postgres 表结构、RLS 和查询优化时用 | `npx skills add supabase/agent-skills` | 免费 |
| ⭐ [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | react-best-practices、web-design-guidelines、composition-patterns、react-view-transitions | `npx skills add vercel-labs/agent-skills` | 免费 |
| [AI SDK skill（Vercel 官方）](https://github.com/vercel/ai) | Vercel AI SDK 官方 Skill（约 7.2 万安装），用 AI SDK 写流式聊天、工具调用和 Agent 时用 | `npx skills add vercel/ai` | 免费 |
| [antfu/skills](https://github.com/antfu/skills) | Anthony Fu 的 Skill 集（vitest 约 4.7 万安装），覆盖 Vite、Vitest、pnpm、Pinia 等 Vue / Vite 生态工具 | `npx skills add antfu/skills` | 免费 |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 官方 Skill 仓库（docx/pdf/pptx/xlsx/frontend-design/skill-creator…） | `npx skills add anthropics/skills` | 免费 |
| [Azure Skills（微软官方）](https://github.com/microsoft/azure-skills) | 微软官方 Azure Skill 集（microsoft-foundry 约 67 万安装），在 Azure 上准备、部署、诊断应用和用 Foundry 时用 | `npx skills add microsoft/azure-skills` | 免费 |
| [Better Auth skills（官方）](https://github.com/better-auth/skills) | Better Auth 官方 Skill（约 13 万安装），在 TypeScript 项目里接入登录鉴权时用 | `npx skills add better-auth/skills` | 免费 |
| [browser-use skill](https://skills.sh/browser-use/browser-use/browser-use) | browser-use 官方 Skill（约 9.9 万安装），让 Agent 用 browser-use CLI 自主完成网页操作时用 | `npx skills add browser-use/browser-use` | 免费 |
| [caveman](https://github.com/JuliusBrussee/caveman) | 让 Agent 用极简「穴居人」语体输出以大幅省 token 的 Skill（约 62 万安装），长会话想压缩输出成本时用 | `npx skills add juliusbrussee/caveman` | 免费 |
| [cc-skills-golang（samber）](https://github.com/samber/cc-skills-golang) | lo 作者 samber 的 Go Skill 集（golang-lint 约 4.2 万安装），写地道 Go 代码、测试和 CI 时用 | `npx skills add samber/cc-skills-golang` | 免费 |
| [Clerk skills（官方）](https://github.com/clerk/skills) | Clerk 官方 Skill 集（约 1.5 万安装），在 Next.js、Expo、Nuxt 等框架里接入 Clerk 鉴权时用 | `npx skills add clerk/skills` | 免费 |
| [ClickHouse agent-skills（官方）](https://github.com/ClickHouse/agent-skills) | ClickHouse 官方 Skill（约 2.3 万安装），设计表引擎、排序键和查询优化时用 | `npx skills add clickhouse/agent-skills` | 免费 |
| [Cloudflare skills（官方）](https://github.com/cloudflare/skills) | Cloudflare 官方 Skill 集（cloudflare 约 15 万安装），写 Workers、Durable Objects、Agents SDK 和用 wrangler 时用 | `npx skills add cloudflare/skills` | 免费 |
| [code-review（CodeRabbit）](https://github.com/coderabbitai/skills) | CodeRabbit 官方 Skill（约 1.6 万安装），让 Agent 在本地调用 CodeRabbit 做 AI 代码评审时用（⚠ 需 CodeRabbit 账号） | `npx skills add coderabbitai/skills` | 免费+付费 |
| [Convex agent-skills（官方）](https://github.com/convex/agent-skills) | Convex 官方 Skill 集（convex-quickstart 约 14 万安装），搭 Convex 后端、配鉴权和做迁移时用 | `npx skills add convex/agent-skills` | 免费 |
| [design-doc-mermaid](https://github.com/SpillwaveSolutions/design-doc-mermaid) | 生成带 Mermaid 图的设计文档的 Skill（约 9.4 万安装），写架构说明、时序图和流程图时用 | `npx skills add spillwavesolutions/design-doc-mermaid` | 免费 |
| [Expo skills（官方）](https://github.com/expo/skills) | Expo 官方 Skill 集（expo-dev-client 约 7.5 万安装），做 React Native / Expo 原生界面、模块和发布时用 | `npx skills add expo/skills` | 免费 |
| [fastapi skill（官方仓库）](https://github.com/fastapi/fastapi) | FastAPI 官方仓库自带的 Skill（约 1.5 万安装），按最新官方惯例写 FastAPI 接口时用 | `npx skills add fastapi/fastapi` | 免费 |
| [fastify-best-practices（mcollina）](https://github.com/mcollina/skills) | Fastify 联合作者 Matteo Collina 的 Skill（约 9.4 万安装），写 Fastify / Node.js 服务时用 | `npx skills add mcollina/skills` | 免费 |
| [Firebase agent-skills（官方）](https://github.com/firebase/agent-skills) | Firebase 官方 Skill 集（firebase-basics 约 18 万安装），配置 Auth、Hosting、Data Connect 和安全规则时用 | `npx skills add firebase/agent-skills` | 免费 |
| [Flutter agent-plugins（官方）](https://github.com/flutter/agent-plugins) | Flutter 官方 Skill 集（约 4.5 万安装），按官方架构建议写 Flutter、修布局和加测试时用 | `npx skills add flutter/agent-plugins` | 免费 |
| [gemini-api-dev（Google 官方）](https://github.com/google-gemini/gemini-skills) | Google 官方 Gemini API 开发 Skill（约 2.7 万安装），用最新 SDK 和模型名写 Gemini 应用时用 | `npx skills add google-gemini/gemini-skills` | 免费 |
| [Google agents-cli skills](https://github.com/google/agents-cli) | Google 官方 Skill（约 56 万安装），用 ADK 编写、评测并部署 Agent 时用 | `npx skills add google/agents-cli` | 免费 |
| [LangChain skills（官方）](https://github.com/langchain-ai/langchain-skills) | LangChain 官方 Skill 集（约 2.0 万安装），写 LangChain、LangGraph 和 Deep Agents 时用 | `npx skills add langchain-ai/langchain-skills` | 免费 |
| [Mastra skill（官方）](https://github.com/mastra-ai/skills) | Mastra 官方 Skill（约 9.7 万安装），用 Mastra 框架写 Agent 和工作流时用 | `npx skills add mastra-ai/skills` | 免费 |
| [mcp-builder（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | Anthropic 官方 Skill（约 14 万安装），按最佳实践设计和实现高质量 MCP 服务器时用 | `npx skills add anthropics/skills --skill mcp-builder` | 免费 |
| [Neon agent-skills（官方）](https://github.com/neondatabase/agent-skills) | Neon 官方 Skill（neon-postgres 约 31 万安装），用 Neon Serverless Postgres 及其分支功能时用 | `npx skills add neondatabase/agent-skills` | 免费 |
| [Nx skills（官方）](https://github.com/nrwl/nx-ai-agents-config) | Nx 官方 Skill（nx-workspace 约 8.9 万安装），让 Agent 理解 Nx 工作区结构并运行任务时用 | `npx skills add nrwl/nx-ai-agents-config` | 免费 |
| [openai/skills（官方）](https://github.com/openai/skills) | OpenAI 官方 Skill 目录（pdf 约 1.4 万安装），给 Codex 等装文档处理、安全实践、修 CI 等技能时用 | `npx skills add openai/skills` | 免费 |
| [playwright-best-practices（Currents）](https://github.com/currents-dev/playwright-best-practices-skill) | Currents 出品的 Playwright 测试最佳实践 Skill（约 10 万安装），写稳定的 E2E 测试、排查 flaky 时用 | `npx skills add currents-dev/playwright-best-practices-skill` | 免费 |
| [playwright-cli（微软官方）](https://github.com/microsoft/playwright-cli) | 微软官方 Playwright CLI Skill（约 21 万安装），让 Agent 用命令行驱动浏览器做测试和调试，比 MCP 更省 token | `npx skills add microsoft/playwright-cli` | 免费 |
| [Prisma skills（官方）](https://github.com/prisma/skills) | Prisma 官方 Skill 集（prisma-client-api 约 42 万安装），写 Prisma Client 查询、配置数据库和升级版本时用 | `npx skills add prisma/skills` | 免费 |
| [react-doctor](https://github.com/millionco/react-doctor) | Million 团队的 React 体检 Skill（约 2.1 万安装），扫描并修复 React 代码里的性能和正确性问题时用 | `npx skills add millionco/react-doctor` | 免费 |
| [react-native-best-practices（Callstack）](https://github.com/callstackincubator/agent-skills) | Callstack 出品的 React Native 性能与最佳实践 Skill（约 3.2 万安装），优化 RN 应用性能时用 | `npx skills add callstackincubator/agent-skills` | 免费 |
| [Resend skills（官方）](https://github.com/resend/resend-skills) | Resend 官方 Skill（约 2.4 万安装），在应用里发事务邮件和处理收件时用 | `npx skills add resend/resend-skills` | 免费 |
| [rust-best-practices（Apollo）](https://github.com/apollographql/skills) | Apollo GraphQL 团队的 Rust 最佳实践 Skill（约 2.3 万安装），写生产级 Rust 时用 | `npx skills add apollographql/skills` | 免费 |
| [Sanity agent-toolkit（官方）](https://github.com/sanity-io/agent-toolkit) | Sanity 官方 Skill 集（约 3.4 万安装），做内容建模、GROQ 查询和迁移时用 | `npx skills add sanity-io/agent-toolkit` | 免费 |
| [Sentry CLI skill（官方）](https://github.com/getsentry/cli) | Sentry 官方 Skill（约 19 万安装），教 Agent 用 sentry CLI 查 Issue、事件和发布，排查线上报错时用 | `npx skills add getsentry/cli --skill sentry-cli` | 免费 |
| [sentry-for-ai（官方）](https://github.com/getsentry/sentry-for-ai) | Sentry 官方 Skill 集（sentry-fix-issues 约 1.0 万安装），给各框架接入 Sentry SDK 并按 Issue 修 bug 时用 | `npx skills add getsentry/sentry-for-ai` | 免费 |
| [shadcn skill（官方）](https://ui.shadcn.com/docs/skills) | 通过 shadcn info --json 读取项目并强制 shadcn 写法；含 migrate-radix-to-base | `npx skills add shadcn/ui` | 免费 |
| [Shopify AI Toolkit（官方）](https://github.com/Shopify/Shopify-AI-Toolkit) | Shopify 官方 Skill 集（shopify-admin 约 1.8 万安装），写 Admin / Storefront GraphQL 和 Liquid 主题时用 | `npx skills add shopify/shopify-ai-toolkit` | 免费 |
| [skill-creator（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Anthropic 官方的 Skill 制作与评测 Skill（约 43 万安装），自己写或优化 Skill 时用 | `npx skills add anthropics/skills --skill skill-creator` | 免费 |
| [solana-dev（Solana 基金会）](https://github.com/solana-foundation/solana-dev-skill) | Solana 基金会官方 Skill（约 11 万安装），写 Solana 程序和前端集成时用 | `npx skills add solana-foundation/solana-dev-skill` | 免费 |
| [Stripe skills（官方）](https://github.com/stripe/ai) | Stripe 官方 Skill（stripe-best-practices 约 10 万安装），接入支付、订阅和升级 API 版本时用 | `npx skills add stripe/ai` | 免费 |
| [swiftui-expert-skill（Antoine van der Lee）](https://github.com/AvdLee/SwiftUI-Agent-Skill) | SwiftLee 作者的 SwiftUI 专家 Skill（约 3.6 万安装），评审和改进 SwiftUI 状态管理与性能时用 | `npx skills add avdlee/swiftui-agent-skill` | 免费 |
| [swiftui-pro（Paul Hudson）](https://github.com/twostraws/SwiftUI-Agent-Skill) | Hacking with Swift 作者的 SwiftUI Skill（约 3.7 万安装），让 Agent 写出符合现代 API 的 SwiftUI 代码时用 | `npx skills add twostraws/swiftui-agent-skill` | 免费 |
| [Turborepo skill（官方）](https://github.com/vercel/turborepo) | Turborepo 官方 Skill（约 8.9 万安装），配置 monorepo 任务管线和缓存时用 | `npx skills add vercel/turborepo` | 免费 |
| [typescript-advanced-types（wshobson）](https://skills.sh/wshobson/agents/typescript-advanced-types) | wshobson 合集里安装量最高的 Skill（约 9.9 万安装），写泛型、条件类型和类型体操时用 | `npx skills add wshobson/agents --skill typescript-advanced-types` | 免费 |
| [Upstash skills（官方）](https://github.com/upstash/skills) | Upstash 官方 Skill 集（约 2.4 万安装），用 Upstash Redis、限流和 QStash 时用 | `npx skills add upstash/skills` | 免费 |
| [vue-best-practices](https://github.com/vuejs-ai/skills) | Vue 社区的最佳实践 Skill（约 4.5 万安装），写 Vue 3 组合式 API 和组件时用 | `npx skills add vuejs-ai/skills` | 免费 |
| [Warp common-skills](https://github.com/warpdotdev/common-skills) | Warp 团队公开的通用 Skill（review-pr 约 2.9 万安装），评审 PR 和诊断 CI 失败时用 | `npx skills add warpdotdev/common-skills` | 免费 |
| [web-quality-skills](https://github.com/addyosmani/web-quality-skills) | Addy Osmani 的 Web 质量 Skill 集（accessibility 约 6.9 万安装），按 Lighthouse 思路审查可访问性、性能和 SEO 时用 | `npx skills add addyosmani/web-quality-skills` | 免费 |
| [webapp-testing（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | Anthropic 官方 Skill（约 20 万安装），用 Playwright 脚本测试本地 Web 应用并截图取日志时用 | `npx skills add anthropics/skills --skill webapp-testing` | 免费 |

<a id="skills-ui"></a>

## 前端 / 设计 / 动效类 Skill

完整清单另见 ui/catalog/09-design-vocabulary.md。

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [ai-elements skill（Vercel）](https://github.com/vercel/ai-elements) | Vercel AI Elements 官方 Skill（约 2.1 万安装），用 AI Elements 组件搭聊天和 Agent 界面时用 | `npx skills add vercel/ai-elements` | 免费 |
| [algorithmic-art（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) | Anthropic 官方 Skill（约 9.4 万安装），用 p5.js 做可调参数的生成艺术时用 | `npx skills add anthropics/skills --skill algorithmic-art` | 免费 |
| [brand-guidelines（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) | Anthropic 官方 Skill（约 12 万安装），示范如何把品牌色和字体规范固化成 Skill，照此改成自己品牌时用 | `npx skills add anthropics/skills --skill brand-guidelines` | 免费 |
| [building-components（components.build）](https://github.com/vercel/components.build) | Vercel components.build 规范的 Skill（约 1.5 万安装），按可组合、可访问的标准写组件库时用 | `npx skills add vercel/components.build` | 免费 |
| [canvas-design（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | Anthropic 官方 Skill（约 13 万安装），生成海报、封面等静态视觉稿（PNG / PDF）时用 | `npx skills add anthropics/skills --skill canvas-design` | 免费 |
| [extract-design-system](https://github.com/arvindrk/extract-design-system) | 从现有网站提取颜色、字体、间距等设计 token 的 Skill（约 13 万安装），想复刻某站视觉体系时用 | `npx skills add arvindrk/extract-design-system` | 免费 |
| [GSAP skills（官方）](https://github.com/greensock/gsap-skills) | gsap-core、scrolltrigger、timeline、react、performance… | `npx skills add https://github.com/greensock/gsap-skills` | 免费 |
| [Mobbin skills](https://github.com/mobbin/skills) | 配合 Mobbin MCP 的设计调研 Skill |  | 免费 |
| [Refero design skill](https://github.com/referodesign/refero_skill) | 先用 Refero MCP 调研真实产品再设计 | `npx skills add https://github.com/referodesign/refero_skill --skill refero-design` | 免费 |
| [tailwind-4-docs](https://github.com/Lombiq/Tailwind-Agent-Skills) | 内置 Tailwind CSS v4 文档的 Skill（约 1.9 万安装），避免 Agent 写出 v3 旧语法时用 | `npx skills add lombiq/tailwind-agent-skills` | 免费 |
| [tailwind-design-system（wshobson）](https://skills.sh/wshobson/agents/tailwind-design-system) | 用 Tailwind 搭设计系统的 Skill（约 7.3 万安装），定义 token、主题和组件变体时用 | `npx skills add wshobson/agents --skill tailwind-design-system` | 免费 |
| [theme-factory（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | Anthropic 官方 Skill（约 10 万安装），给幻灯片、文档和网页套用成套配色字体主题时用 | `npx skills add anthropics/skills --skill theme-factory` | 免费 |
| [Three.js skills](https://github.com/CloudAI-X/threejs-skills) | 基础、动画、shader、材质、几何、交互 | `npx skills add cloudai-x/threejs-skills` | 免费 |
| [web-artifacts-builder（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) | Anthropic 官方 Skill（约 12 万安装），用 React + Tailwind + shadcn/ui 打包复杂单文件 HTML 作品时用 | `npx skills add anthropics/skills --skill web-artifacts-builder` | 免费 |

<a id="skills-media"></a>

## 视频 / 多媒体类 Skill

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [101-skills/superpowers](https://www.skills.sh/101-skills/superpowers) | ai-video-generation 等（Top 30 中占 4 席） |  | 免费 |
| [baoyu-image-gen（宝玉）](https://skills.sh/jimliu/baoyu-skills/baoyu-image-gen) | 宝玉的 AI 生图 Skill（约 3.4 万安装），在 Agent 里调用多家图像模型生成配图时用（⚠ 需相应 API key） | `npx skills add jimliu/baoyu-skills --skill baoyu-image-gen` | 免费 |
| [ElevenLabs skills（官方）](https://github.com/elevenlabs/skills) | ElevenLabs 官方 Skill 集（text-to-speech 约 2.0 万安装），做配音、音效、转写和音乐生成时用（⚠ 需 API key） | `npx skills add elevenlabs/skills` | 免费+付费 |
| [ffmpeg（claude-code-video-toolkit）](https://github.com/digitalsamba/claude-code-video-toolkit) | 视频工具包里的 ffmpeg Skill（约 1.4 万安装），让 Agent 剪辑、转码、加字幕时写对 ffmpeg 命令 | `npx skills add digitalsamba/claude-code-video-toolkit --skill ffmpeg` | 免费 |
| [Higgsfield skills（官方）](https://github.com/higgsfield-ai/skills) | Higgsfield 官方 Skill 集（higgsfield-generate 约 24 万安装），生成图片、视频、产品摄影和讲解视频时用（⚠ 需 Higgsfield 账号，按量付费） | `npx skills add higgsfield-ai/skills` | 付费 |
| [Remotion skills（官方）](https://github.com/remotion-dev/skills) | remotion-best-practices（78 万安装）、render、captions | `npx skills add remotion-dev/skills` | 免费 |
| [Replicate skills（官方）](https://github.com/replicate/skills) | Replicate 官方 Skill 集（约 2.9 千安装），查找并运行图像、视频模型及写生成提示词时用（⚠ 需 API token，按量付费） | `npx skills add replicate/skills` | 付费 |
| [slack-gif-creator（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator) | Anthropic 官方 Skill（约 7.9 万安装），制作符合 Slack 尺寸限制的动画 GIF 时用 | `npx skills add anthropics/skills --skill slack-gif-creator` | 免费 |

<a id="skills-more"></a>

## 其他领域 Skill（写作 / 调研 / 数据 / 文档 / 运维 / 安全 / 产品）

本类分组：官方厂商 Skill · 写作与内容 · 调研与数据 · 文档与办公 · 运维与安全 · 产品与增长 · 插件市场

### 官方厂商 Skill

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [飞书 / Lark CLI skills（官方）](https://github.com/larksuite/cli) | 飞书官方 CLI 自带的 Skill 集（lark-doc 约 49 万安装），让 Agent 操作文档、多维表格、消息、日历和审批时用（⚠ 需飞书应用授权） | `npx skills add larksuite/cli` | 免费 |
| [Firecrawl CLI skills（官方）](https://github.com/firecrawl/cli) | Firecrawl 官方 CLI Skill（firecrawl 约 10 万安装），抓取、搜索、爬站并存成本地 Markdown 时用（⚠ 需 API key） | `npx skills add firecrawl/cli` | 免费+付费 |
| [Google Workspace CLI skills](https://github.com/googleworkspace/cli) | Google Workspace CLI 自带的 Skill 集（gws-gmail 约 8.4 万安装），让 Agent 收发 Gmail、管理 Drive 和日历时用（⚠ 需 Google OAuth 授权） | `npx skills add googleworkspace/cli` | 免费 |
| [notion-api（intellectronica）](https://github.com/intellectronica/agent-skills) | 直接调用 Notion API 的 Skill（约 10 万安装），不装 MCP 也想读写 Notion 页面和数据库时用（⚠ 需 Notion 集成令牌） | `npx skills add intellectronica/agent-skills --skill notion-api` | 免费 |
| [Tavily skills（官方）](https://github.com/tavily-ai/skills) | Tavily 官方 Skill 集（tavily-search 约 3.8 万安装），让 Agent 联网搜索、提取网页和做研究时用（⚠ 需 API key） | `npx skills add tavily-ai/skills` | 免费+付费 |
| [企业微信 CLI skills（官方）](https://github.com/WecomTeam/wecom-cli) | 企业微信官方 CLI 的 Skill 集（wecomcli-doc 约 2.6 万安装），操作企微文档、表格和待办时用（⚠ 需企业微信授权） | `npx skills add wecomteam/wecom-cli` | 免费 |

### 写作与内容

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [baoyu-skills（宝玉）](https://github.com/JimLiu/baoyu-skills) | 宝玉的内容创作 Skill 集（baoyu-post-to-wechat 约 3.5 万安装），做公众号排版发布、小红书配图、翻译和发 X 时用 | `npx skills add jimliu/baoyu-skills` | 免费 |
| [dbskill（dontbesilent）](https://github.com/dontbesilent2025/dbskill) | 中文自媒体向 Skill 集（dbs-ai-check 约 2.8 万安装），检测 AI 味、起小红书标题和排公众号版式时用 | `npx skills add dontbesilent2025/dbskill` | 免费 |
| [humanizer](https://github.com/blader/humanizer) | 基于维基百科「AI 写作特征」的英文去 AI 味 Skill（约 1.3 万安装），润色英文稿时用 | `npx skills add blader/humanizer` | 免费 |
| [humanizer-zh](https://github.com/op7418/Humanizer-zh) | 中文去 AI 味 Skill（约 5.7 万安装），按常见 AI 写作特征检查并改写中文稿时用 | `npx skills add op7418/humanizer-zh` | 免费 |
| [ljg-skills（李继刚）](https://github.com/lijigang/ljg-skills) | 李继刚的思考与表达 Skill 集（ljg-card 约 7.1 千安装），做概念卡片、读论文、圆桌讨论和深度写作时用 | `npx skills add lijigang/ljg-skills` | 免费 |
| [resumeskills](https://github.com/Paramchoudhary/ResumeSkills) | 简历优化 Skill 集（resume-ats-optimizer 约 1.5 万安装），按 ATS 规则改简历和针对岗位定制时用 | `npx skills add paramchoudhary/resumeskills` | 免费 |

### 调研与数据

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [firecrawl-deep-research](https://github.com/firecrawl/firecrawl-workflows) | Firecrawl 官方的深度研究工作流 Skill（约 3.6 万安装），多轮搜索抓取并产出带引用的报告时用（⚠ 需 API key） | `npx skills add firecrawl/firecrawl-workflows --skill firecrawl-deep-research` | 免费+付费 |
| [just-scrape（ScrapeGraphAI）](https://github.com/ScrapeGraphAI/just-scrape) | ScrapeGraphAI 官方 Skill（约 25 万安装），用自然语言描述要抓的字段并返回结构化数据时用（⚠ 需 API key） | `npx skills add scrapegraphai/just-scrape` | 免费+付费 |
| [last30days](https://github.com/mvanhorn/last30days-skill) | 汇总某话题近 30 天在 Reddit、X、YouTube 等平台讨论的调研 Skill（约 6.0 万安装），想快速了解最新舆论和趋势时用 | `npx skills add mvanhorn/last30days-skill` | 免费 |
| [nature-skills](https://github.com/Yuan1z0825/nature-skills) | 面向科研写作的中文 Skill 集（nature-polishing 约 1.9 万安装），按顶刊风格润色论文、精读文献和把论文做成 PPT 时用 | `npx skills add yuan1z0825/nature-skills` | 免费 |
| [notebooklm（notebooklm-py）](https://github.com/teng-lin/notebooklm-py) | 让 Agent 操作 Google NotebookLM 的 Skill（约 1.0 万安装），批量导入资料并生成播客、摘要时用（⚠ 非官方接口） | `npx skills add teng-lin/notebooklm-py` | 免费 |
| [scientific-agent-skills（K-Dense）](https://github.com/K-Dense-AI/scientific-agent-skills) | K-Dense 的科研 Skill 大合集（scientific-writing 约 2.6 千安装），做生信、化学、数据分析和科学写作时用 | `npx skills add k-dense-ai/scientific-agent-skills` | 免费 |

### 文档与办公

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [docx（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/docx) | Anthropic 官方 Skill（约 22 万安装），创建和编辑带修订、批注的 Word 文档时用 | `npx skills add anthropics/skills --skill docx` | 免费 |
| [html-ppt](https://github.com/lewislulu/html-ppt-skill) | 用 HTML 生成演示文稿的中文 Skill（约 2.1 万安装），想快速做出可在浏览器放映的幻灯片时用 | `npx skills add lewislulu/html-ppt-skill` | 免费 |
| [obsidian-skills（kepano）](https://github.com/kepano/obsidian-skills) | Obsidian CEO 写的 Skill 集（obsidian-markdown 约 9.6 万安装），让 Agent 正确读写 Obsidian Markdown、Bases 和 Canvas 时用 | `npx skills add kepano/obsidian-skills` | 免费 |
| [pdf（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/pdf) | Anthropic 官方 Skill（约 23 万安装），提取、合并、拆分 PDF 及填写表单时用 | `npx skills add anthropics/skills --skill pdf` | 免费 |
| [pptx（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/pptx) | Anthropic 官方 Skill（约 25 万安装），创建、编辑和分析 PowerPoint 文件时用 | `npx skills add anthropics/skills --skill pptx` | 免费 |
| [xlsx（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/xlsx) | Anthropic 官方 Skill（约 20 万安装），创建带公式的表格、清洗和分析数据时用 | `npx skills add anthropics/skills --skill xlsx` | 免费 |

### 运维与安全

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [HashiCorp agent-skills（官方）](https://github.com/hashicorp/agent-skills) | HashiCorp 官方 Skill 集（terraform-style-guide 约 1.3 万安装），按官方风格写 Terraform、测试和 Stacks 时用 | `npx skills add hashicorp/agent-skills` | 免费 |
| [security-audit（Cloudflare）](https://github.com/cloudflare/security-audit-skill) | Cloudflare 出品的安全审计 Skill（约 9.5 万安装），系统性排查代码库里的漏洞和配置风险时用 | `npx skills add cloudflare/security-audit-skill` | 免费 |
| [security-review（Sentry）](https://github.com/getsentry/skills) | Sentry 工程团队的安全评审 Skill（约 2.3 万安装），按低误报原则审查代码改动里的安全问题时用 | `npx skills add getsentry/skills --skill security-review` | 免费 |
| [Trail of Bits skills](https://github.com/trailofbits/skills) | 安全公司 Trail of Bits 的 Skill 集（semgrep 约 1.0 万安装），做静态分析、变体分析和审计智能合约时用 | `npx skills add trailofbits/skills` | 免费 |

### 产品与增长

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [marketingskills（Corey Haines）](https://github.com/coreyhaines31/marketingskills) | 最流行的营销 Skill 集（seo-audit 约 25 万安装），做 SEO 审计、文案、定价、转化优化和内容策略时用 | `npx skills add coreyhaines31/marketingskills` | 免费 |
| [audit-website（SquirrelScan）](https://github.com/squirrelscan/skills) | SquirrelScan 的网站体检 Skill（约 7.5 万安装），上线前按 SEO、性能、安全等上百条规则审查站点时用 | `npx skills add squirrelscan/skills` | 免费 |
| [autonnel-skills](https://github.com/autonnel/autonnel-skills) | 销售漏斗与转化 Skill 集（landing-page-conversion-audit 约 12 万安装），审查落地页转化和设计漏斗时用（⚠ 厂商营销向内容，按需取用） | `npx skills add autonnel/autonnel-skills` | 免费 |
| [pm-skills（Paweł Huryn）](https://github.com/phuryn/pm-skills) | 产品经理向 Skill 集（create-prd 约 1.1 万安装），写 PRD、做产品发现和制定策略时用 | `npx skills add phuryn/pm-skills` | 免费 |

### 插件市场

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Anthropic 官方的 Claude Code 插件市场（默认已内置），找厂商认证的插件（Stripe、Sentry、Exa 等）时首选 | `/plugin install {plugin-name}@claude-plugins-official` | 免费 |
| [awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins) | Claude Code 插件、命令、子 Agent 和 Hook 的精选列表，找社区插件市场入口时用 |  | 免费 |
| [Build with Claude](https://github.com/davepoon/buildwithclaude) | 社区的 Claude Code 插件与 Skill 聚合市场（buildwithclaude.com），想在一个地方搜社区插件时用 | `/plugin marketplace add davepoon/buildwithclaude` | 开源 |
| [Claude Code 插件市场文档](https://code.claude.com/docs/en/discover-plugins) | 官方讲如何添加市场、安装和管理插件的文档，第一次用 /plugin 时读 |  | 免费 |
| [Claude 插件目录](https://claude.com/plugins) | Anthropic 官方插件目录网页版，浏览 Claude Code / Cowork 可装插件及其说明时用 |  | 免费 |
| [knowledge-work-plugins（Anthropic）](https://github.com/anthropics/knowledge-work-plugins) | Anthropic 开源的知识工作插件（销售、法务、财务、数据、产品等岗位），想给非工程岗位配成套 Skill 和连接器时用 | `claude plugin marketplace add anthropics/knowledge-work-plugins` | 开源 |
| [superpowers-marketplace](https://github.com/obra/superpowers-marketplace) | obra 维护的插件市场，除 Superpowers 外还有 Chrome 控制、写作等配套插件 | `/plugin marketplace add obra/superpowers-marketplace` | 开源 |
| [tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace) | 收录数百个插件和上千个 Skill 的社区市场（原 claude-code-plugins-plus-skills），想批量挑选社区技能时用（⚠ 质量参差，装前先看内容） | `/plugin marketplace add jeremylongshore/claude-code-plugins` | 开源 |

<a id="skills-local"></a>

## 本文件夹自带的 Skill

已经在本文件夹里，无需安装。

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [lieflat-less-ai-tone（本地）](../lieflat-less-ai-tone/SKILL.md) | 中文去 AI 味：脚本检测 + 语义判读 + 改写 + 前后对比报告。路径：./lieflat-less-ai-tone/SKILL.md。⚠ CC BY-NC 4.0，禁止商用 | 直接读 lieflat-less-ai-tone/SKILL.md | 免费 |
| [ui-master（本地）](../ui/SKILL.md) | 本文件夹的 UI 路由 Skill：按需求选组件库、风格、动效词汇和 MCP。路径：./ui/SKILL.md | 直接读 ui/SKILL.md | 免费 |
