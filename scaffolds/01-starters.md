# 脚手架 / Starter 模板

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

## 全栈 Web Starter

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [create-next-app](https://nextjs.org/docs/app/getting-started/installation) | 官方 Next.js 脚手架（v16），React 全栈默认选择 | Next.js, React | `npx create-next-app@latest` | 开源 |
| ⭐ [create-vite](https://vite.dev/guide/) | 轻量 SPA/库脚手架（React/Vue/Svelte/Solid…），不需要 SSR 时选 | Vite | `npm create vite@latest` | 开源 |
| ⭐ [next-forge（Vercel）](https://www.next-forge.com) | 生产级 Turborepo SaaS 单仓：认证、支付、数据库、邮件、可观测性。认真做多应用 SaaS 时选 | Next.js, Turborepo | `npx next-forge@latest init` | 开源 |
| ⭐ [Open SaaS](https://opensaas.sh) | 免费全功能 SaaS 模板：Stripe/Polar/Lemon Squeezy 支付、后台、文档、AI demo | Wasp | `wasp new（选 SaaS 模板）` | 开源 |
| ⭐ [shadcn/ui init + Blocks](https://ui.shadcn.com/blocks) | 初始化项目时直接带上 shadcn（next/vite/start/react-router/astro）；/create 是可视化构建器；Blocks 是可复制的整页区块 | React, Tailwind | `npx shadcn@latest init -t next` | 开源 |
| [Astro](https://astro.build/themes/) | 内容优先站点（营销、文档、博客），Islands 架构；Starlight 是文档站 starter | Astro | `npm create astro@latest` | 开源 |
| [BoxyHQ SaaS Starter Kit](https://github.com/boxyhq/saas-starter-kit) | 企业 SaaS 功能：SSO/SAML、审计日志、团队 | Next.js |  | 开源 |
| [create-t3-app](https://create.t3.gg) | Next.js + tRPC + Prisma/Drizzle + NextAuth + Tailwind 全类型安全（注意：2025-12 后更新放缓） | Next.js, tRPC | `npm create t3-app@latest` | 开源 |
| [ixartz Next.js Boilerplate](https://github.com/ixartz/Next-js-Boilerplate) | 开箱即用 Next.js（Clerk、Drizzle、测试、i18n）；SaaS 版加多租户 | Next.js | `git clone --depth=1 https://github.com/ixartz/Next-js-Boilerplate` | 开源 |
| [Next.js SaaS Starter](https://github.com/nextjs/saas-starter) | 官方极简 SaaS：Next.js + Postgres + Stripe + shadcn/ui | Next.js, Stripe | `git clone https://github.com/nextjs/saas-starter` | 开源 |
| [Nuxt](https://nuxt.com/templates) | Vue 全栈 + 模板画廊 | Vue | `npm create nuxt@latest` | 开源 |
| [Nx](https://nx.dev/getting-started/intro) | 企业级单仓工具，带各框架生成器 |  | `npx create-nx-workspace@latest` | 开源 |
| [Payload CMS](https://payloadcms.com/docs/getting-started/installation) | 装在 Next.js 里的 Headless CMS / 应用框架，内容型应用和后台 | Next.js | `npx create-payload-app@latest` | 开源 |
| [React Router v7（原 Remix）](https://reactrouter.com/start/framework/installation) | Remix 的继任者：SSR、loaders、actions，基于 Vite | React | `npx create-react-router@latest` | 开源 |
| [Refine](https://refine.dev) | CRUD / 后台管理 / 内部工具专用 React 框架 | React | `npm create refine-app@latest` | 开源 |
| [Supabase Next.js Starter](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs) | Postgres + 认证 + 存储后端，cookie SSR 认证 | Next.js, Supabase | `npx create-next-app -e with-supabase` | 免费+付费 |
| [SvelteKit（sv）](https://svelte.dev/docs/cli/sv-create) | Svelte 全栈；sv CLI 可一键加 Tailwind/Drizzle/auth | Svelte | `npx sv create my-app` | 开源 |
| [TanStack Start](https://tanstack.com/start/latest) | 基于 TanStack Router 的全栈 React：类型安全路由 + server functions + Vite。Next.js 替代品 | React, Vite | `npx @tanstack/cli@latest create` | 开源 |
| [Turborepo](https://turborepo.com/docs/getting-started/installation) | JS/TS 单仓构建系统 |  | `npx create-turbo@latest` | 开源 |
| [Vercel Templates](https://vercel.com/templates) | 可一键部署的模板画廊（AI、电商、SaaS、博客），跨框架 |  | `npx create-next-app -e <example>` | 免费 |
| [Wasp](https://wasp.sh) | 声明式全栈（React + Node + Prisma），内置认证、任务、邮件 | React, Node | `npm i -g @wasp.sh/wasp-cli@latest && wasp new` | 开源 |

## 移动端 / 桌面端 Starter

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [create-expo-app](https://docs.expo.dev/more/create-expo/) | 官方 React Native + Expo（Expo Router），RN 默认选择 | React Native, Expo | `npx create-expo-app@latest` | 开源 |
| ⭐ [create-tauri-app](https://v2.tauri.app/start/create-project/) | Tauri 2：Rust 后端的轻量桌面/移动应用，前端任意 | Rust, Web | `npm create tauri-app@latest` | 开源 |
| [Electron Forge](https://www.electronforge.io) | Electron 官方打包、发布与模板 | Electron | `npx create-electron-app@latest my-app --template=vite-typescript` | 开源 |
| [electron-vite](https://electron-vite.org) | 基于 Vite 的 Electron 构建工具，带 React/Vue/Svelte 模板 | Electron, Vite | `npm create @quick-start/electron@latest` | 开源 |
| [Ignite（Infinite Red）](https://docs.infinite.red/ignite-cli/) | 久经考验的 RN/Expo 模板 + 代码生成器 | React Native | `npx ignite-cli@latest new MyApp` | 开源 |
| [Obytes RN Template](https://starter.obytes.com) | Expo + TS + Tailwind（Nativewind）+ React Query + Zustand，面向生产 | React Native | `npx create-obytes-app@latest MyApp` | 开源 |

## 后端 / API Starter

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template) | FastAPI + SQLModel + Postgres + React/Vite + Docker Compose + JWT，Python 全栈 | Python, FastAPI | `git clone https://github.com/fastapi/full-stack-fastapi-template` | 开源 |
| ⭐ [Hono](https://hono.dev/docs/getting-started/basic) | 超轻量 Web 标准 API 框架（Cloudflare Workers/Bun/Deno/Node/Vercel） | TS | `npm create hono@latest` | 开源 |
| [Encore](https://encore.dev) | Go/TS 后端框架，在代码里声明基础设施（DB、pub/sub、cron） | Go, TS | `brew install encoredev/tap/encore && encore app create` | 开源 |
| [Go Blueprint](https://go-blueprint.dev) | Go 项目脚手架：选框架（Gin/Fiber/Echo/chi）、DB、Docker、HTMX/React | Go | `go install github.com/melkeydev/go-blueprint@latest && go-blueprint create` | 开源 |
| [golang-standards/project-layout](https://github.com/golang-standards/project-layout) | 广泛使用的 Go 目录结构参考（非官方标准） | Go |  | 开源 |
| [NestJS](https://docs.nestjs.com/first-steps) | 结构化 Node/TS 后端（依赖注入、模块），企业级 API | TS, Node | `npx @nestjs/cli new my-api` | 开源 |
