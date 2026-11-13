# 常用库速查

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="stack-libs"></a>

## 常用库（状态 / 请求 / 校验 / 测试 / 工具链 / Python）

每个关注点的默认选择，避免每次重新调研。

本类分组：状态管理 · 数据请求与 API 层 · 校验与类型 · 路由 · 日期与工具函数 · 样式工具 · 测试 · 构建与工具链 · 环境与配置 · 命令行工具 · Python 基础 · Python 数据与界面

### 状态管理

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Zustand](https://zustand.docs.pmnd.rs) | 极简的 React 全局状态库，一个 hook 即一个 store，无 Provider、无样板代码；客户端状态的默认选择 | React, TS | `npm i zustand`<br>llms.txt: https://zustand.docs.pmnd.rs/llms.txt | 开源 |
| [Immer](https://immerjs.github.io/immer/) | 用可变写法生成不可变数据的工具库；在 reducer 或 Zustand 里更新深层嵌套状态时用 | TS | `npm i immer` | 开源 |
| [Jotai](https://github.com/pmndrs/jotai) | 原子化的 React 状态库，状态由小原子自底向上组合、按需订阅；状态之间派生关系多、想要细粒度重渲染控制时选 | React, TS | `npm i jotai` | 开源 |
| [Legend State](https://legendapp.com/open-source/state/) | 基于信号的高性能状态库，内置本地持久化和远端同步插件；React Native 应用要细粒度更新和离线同步时选 | React, React Native | `npm i @legendapp/state` | 开源 |
| [MobX](https://mobx.js.org) | 基于可观察对象的响应式状态管理，自动追踪依赖；面向对象风格的领域模型或存量 MobX 项目选 | React, TS | `npm install mobx mobx-react-lite` | 开源 |
| [nuqs](https://nuqs.dev) | 类型安全的 URL 查询参数状态管理，用法像 useState；筛选、分页、标签页等需要可分享、可刷新的状态时选 | Next.js, React | `npm i nuqs`<br>llms.txt: https://nuqs.dev/llms.txt | 开源 |
| [Pinia](https://pinia.vuejs.org) | Vue 官方状态管理库，类型推导好、支持组合式写法和 DevTools；Vue/Nuxt 项目的默认选择 | Vue, Nuxt | `npm i pinia`<br>llms.txt: https://pinia.vuejs.org/llms.txt | 开源 |
| [Redux Toolkit](https://redux-toolkit.js.org) | Redux 官方推荐写法，内置 Immer、createSlice 和 RTK Query；大型团队需要严格的单向数据流、时间旅行调试或维护存量 Redux 项目时选 | React, TS | `npm install @reduxjs/toolkit react-redux` | 开源 |
| [TanStack Store](https://tanstack.com/store/latest) | 框架无关的不可变响应式 store，TanStack 系列库的内部状态底座；写跨框架的库或想要信号式派生状态时选 | TS, React, Vue, Solid | `npm i @tanstack/react-store`<br>llms.txt: https://tanstack.com/store/latest/llms.txt | 开源 |
| [Valtio](https://valtio.dev) | 基于 Proxy 的状态库，直接修改对象即可触发更新；喜欢可变写法、想把状态当普通对象用时选 | React, TS | `npm i valtio` | 开源 |
| [XState](https://stately.ai/docs/xstate) | 状态机与 Actor 模型的状态编排库，可视化建模复杂流程；多步骤表单、支付流程、播放器这类状态转换多且不能出错的逻辑选 | TS, React | `npm install xstate @xstate/react`<br>llms.txt: https://stately.ai/llms.txt | 开源 |

### 数据请求与 API 层

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [TanStack Query](https://tanstack.com/query/latest) | 异步服务端状态管理库：缓存、去重、后台刷新、乐观更新、无限滚动；React（及 Vue/Svelte/Solid）里请求数据的默认选择 | React, Vue, Svelte, Solid | `npm i @tanstack/react-query`<br>llms.txt: https://tanstack.com/query/latest/llms.txt | 开源 |
| [Axios](https://axios-http.com) | 最普及的 HTTP 客户端，拦截器、取消、进度和 Node/浏览器通用；存量项目或需要成熟拦截器生态时用，新项目可考虑 ky/ofetch | JS, TS | `npm i axios` | 开源 |
| [GraphQL Yoga](https://the-guild.dev/graphql/yoga-server) | The Guild 出的全功能 GraphQL 服务端，基于 Web 标准、可跑在任意运行时；需要 GraphQL API 时的服务端默认选择 | TS, Node, Workers | `npm i graphql-yoga graphql`<br>llms.txt: https://the-guild.dev/graphql/yoga-server/llms.txt | 开源 |
| [Hey API（openapi-ts）](https://heyapi.dev) | 把 OpenAPI 规范生成完整 SDK、类型、Zod schema 和 TanStack Query hooks 的代码生成器；希望一条命令产出可直接调用的客户端时选 | TS, OpenAPI | `npx @hey-api/openapi-ts -i openapi.json -o src/client`<br>llms.txt: https://heyapi.dev/llms.txt | 开源 |
| [ky](https://github.com/sindresorhus/ky) | 基于 fetch 的小巧 HTTP 客户端，带重试、超时、钩子和 JSON 快捷方法；想要比原生 fetch 顺手但不引入 Axios 时选 | TS | `npm i ky` | 开源 |
| [ofetch](https://github.com/unjs/ofetch) | UnJS 的增强版 fetch，自动解析 JSON、重试和拦截器，Node/浏览器/Workers 通用，Nuxt 的 $fetch 即是它；Nuxt 或跨运行时代码选 | TS | `npm i ofetch` | 开源 |
| [openapi-typescript / openapi-fetch](https://openapi-ts.dev) | 从 OpenAPI 规范生成零运行时的 TypeScript 类型，配套 openapi-fetch 提供类型安全的 fetch 客户端；调用已有 OpenAPI 后端（如 FastAPI）时选 | TS, OpenAPI | `npm i -D openapi-typescript`<br>`npm i openapi-fetch` | 开源 |
| [oRPC](https://orpc.dev) | 端到端类型安全的 RPC，同时原生输出 OpenAPI 规范，支持 Standard Schema、契约优先和 Server Actions；既要 tRPC 的体验又要对外提供 REST/OpenAPI 时选 | TS | `npm install @orpc/server@latest @orpc/client@latest`<br>llms.txt: https://orpc.dev/llms.txt | 开源 |
| [Orval](https://orval.dev) | 从 OpenAPI 生成类型安全客户端、TanStack Query/SWR hooks 和 MSW mock 的工具；前端要同时生成请求 hooks 和 mock 数据时选 | TS, OpenAPI | `npm i orval`<br>llms.txt: https://orval.dev/llms.txt | 开源 |
| [SWR](https://swr.vercel.app) | Vercel 出的轻量数据请求 hook，stale-while-revalidate 策略；只要简单的获取 + 缓存、不需要 TanStack Query 全套功能时选 | React, Next.js | `npm i swr`<br>llms.txt: https://swr.vercel.app/llms.txt | 开源 |
| [TanStack DB](https://tanstack.com/db/latest) | TanStack Query 之上的客户端响应式数据层，集合 + 实时查询 + 乐观写入，可接 ElectricSQL 等同步引擎；前端要做跨集合联表和即时交互时选，⚠ 仍在 beta | React, TS | `npm i @tanstack/react-db`<br>llms.txt: https://tanstack.com/db/latest/llms.txt | 开源 |
| [TanStack Table](https://tanstack.com/table/latest) | 无头表格引擎：排序、筛选、分组、分页、列固定逻辑全包，UI 自己写（shadcn 的 Data Table 即基于它）；要做功能复杂的数据表格时选 | React, Vue, Svelte, Solid | `npm i @tanstack/react-table`<br>llms.txt: https://tanstack.com/table/latest/llms.txt | 开源 |
| [tRPC](https://trpc.io) | 无需代码生成的端到端类型安全 RPC，前端直接调用后端函数并获得完整类型；前后端同在一个 TypeScript 仓库时选 | TS, React, Next.js | `npm install @trpc/server @trpc/client`<br>llms.txt: https://trpc.io/llms.txt | 开源 |
| [ts-rest](https://ts-rest.com) | 以契约为中心的类型安全 REST：先定义契约，再在前后端共享实现；想保留标准 REST 接口又要端到端类型时选 | TS | `npm i @ts-rest/core` | 开源 |
| [urql](https://urql.dev) | 轻量、可扩展的 GraphQL 客户端，缓存策略通过 exchange 组合；前端消费 GraphQL 且嫌 Apollo 太重时选 | React, TS | `npm i urql` | 开源 |

### 校验与类型

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [React Hook Form](https://react-hook-form.com) | 基于非受控组件的高性能表单库，配 @hookform/resolvers 接 Zod 等校验，shadcn/ui 表单默认搭配；React 表单的默认选择 | React, TS | `npm install react-hook-form @hookform/resolvers`<br>llms.txt: https://react-hook-form.com/llms.txt | 开源 |
| ⭐ [Zod](https://zod.dev) | TypeScript 优先的 schema 校验库，从 schema 推导静态类型，AI SDK、tRPC、表单库等几乎都以它为通用语言；校验的默认选择，对包体敏感可用 zod/mini | TS | `npm i zod`<br>llms.txt: https://zod.dev/llms.txt | 开源 |
| [ArkType](https://arktype.io) | 用接近 TypeScript 语法的字符串定义类型并做运行时校验，性能极高；校验在热路径上或想要最贴近 TS 的定义写法时选 | TS | `npm i arktype`<br>llms.txt: https://arktype.io/llms.txt | 开源 |
| [Conform](https://conform.guide) | 面向渐进增强的表单校验库，围绕原生 FormData 与 Server Actions 设计；React Router/Remix 或 Next.js 服务端表单选 | React, Remix, Next.js | `npm install @conform-to/react @conform-to/zod` | 开源 |
| [Effect](https://effect.website) | TypeScript 的函数式标准库：类型化错误、依赖注入、并发、重试、Schema 和可观测性一体；后端逻辑复杂、想在类型层面追踪错误和依赖时选，⚠ 学习曲线陡 | TS | `npm i effect` | 开源 |
| [neverthrow](https://github.com/supermacro/neverthrow) | 轻量的 Result 类型库，把可能失败的操作显式编码进返回类型；只想要类型安全的错误处理、不想上 Effect 时选 | TS | `npm i neverthrow` | 开源 |
| [Standard Schema](https://standardschema.dev) | Zod、Valibot、ArkType 共同制定的校验库通用接口规范；写接受「任意校验库」的工具或库时面向它编程 | TS | `npm i @standard-schema/spec` | 开源 |
| [TanStack Form](https://tanstack.com/form/latest) | 无头、类型安全的表单状态库，字段级校验与异步校验内置，跨 React/Vue/Solid 等框架；表单很复杂或想要最强类型推导时选 | React, Vue, Solid | `npm i @tanstack/react-form`<br>llms.txt: https://tanstack.com/form/latest/llms.txt | 开源 |
| [ts-pattern](https://github.com/gvergnaud/ts-pattern) | 带穷尽性检查的 TypeScript 模式匹配库；处理可辨识联合和复杂分支、想让编译器保证不漏情况时用 | TS | `npm i ts-pattern` | 开源 |
| [ts-reset](https://www.totaltypescript.com/ts-reset) | Matt Pocock 出的 TypeScript 内置类型「重置」，修正 JSON.parse 返回 any、filter(Boolean) 等常见坑；应用项目里装一次即可 | TS | `npm i @total-typescript/ts-reset` | 开源 |
| [type-fest](https://github.com/sindresorhus/type-fest) | 常用 TypeScript 工具类型合集（PartialDeep、SetRequired、JsonValue 等）；不想自己手写类型体操时装 | TS | `npm i type-fest` | 开源 |
| [TypeBox](https://github.com/sinclairzx81/typebox) | 直接构建 JSON Schema 并推导 TypeScript 类型的库，与 Fastify、Elysia 和 OpenAPI 天然契合；schema 需要原样作为 JSON Schema 对外时选 | TS | `npm i @sinclair/typebox` | 开源 |
| [Valibot](https://valibot.dev) | 模块化、可 tree-shake 的 schema 校验库，打包后体积可比 Zod 小一个数量级；客户端包体或 Edge 冷启动敏感时选 | TS | `npm i valibot`<br>llms.txt: https://valibot.dev/llms.txt | 开源 |

### 路由

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [TanStack Router](https://tanstack.com/router/latest) | 完全类型安全的 React 路由，路径参数、search params 和 loader 都有类型推导，支持文件路由与内置缓存；Vite 单页应用的默认路由 | React, Vite | `npm i @tanstack/react-router`<br>llms.txt: https://tanstack.com/router/latest/llms.txt | 开源 |
| [Expo Router](https://docs.expo.dev/router/introduction/) | Expo 的文件式路由，同一套路由覆盖 iOS、Android 和 Web，支持深链和类型化路由；React Native 新项目的默认导航方案 | Expo, React Native | `npx expo install expo-router`<br>llms.txt: https://docs.expo.dev/llms.txt | 开源 |
| [React Navigation](https://reactnavigation.org) | React Native 生态的基础导航库（栈、标签、抽屉），Expo Router 的底层；需要完全手写导航结构或不用 Expo 时选 | React Native | `npm i @react-navigation/native`<br>llms.txt: https://reactnavigation.org/llms.txt | 开源 |
| [Vue Router](https://router.vuejs.org) | Vue 官方路由，支持嵌套路由、导航守卫和类型化路由；Vue 单页应用的标准选择 | Vue | `npm i vue-router`<br>llms.txt: https://router.vuejs.org/llms.txt | 开源 |
| [wouter](https://github.com/molefrog/wouter) | 约 2KB 的极简 React/Preact 路由，hook 风格 API；小型应用或嵌入式部件只需要基本路由时选 | React, Preact | `npm i wouter` | 开源 |

### 日期与工具函数

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [date-fns](https://date-fns.org) | 函数式、可 tree-shake 的日期工具库，操作原生 Date，带时区支持和大量本地化；处理日期的默认选择 | TS | `npm i date-fns` | 开源 |
| ⭐ [es-toolkit](https://es-toolkit.dev) | 现代的 Lodash 替代品，体积更小、速度更快、类型完善，并提供 es-toolkit/compat 平滑迁移；通用工具函数的默认选择 | TS | `npm i es-toolkit`<br>llms.txt: https://es-toolkit.dev/llms.txt | 开源 |
| [Day.js](https://day.js.org) | 2KB 的 Moment.js 兼容替代，链式 API、插件化，中文社区使用广；从 Moment 迁移或偏好链式写法时选 | JS | `npm i dayjs` | 开源 |
| [Lodash](https://lodash.com) | 最经典的 JavaScript 工具函数库；维护存量代码时用，新项目优先 es-toolkit，⚠ 整包引入体积大 | JS | `npm i lodash` | 开源 |
| [Luxon](https://moment.github.io/luxon/) | Moment 团队出的不可变日期库，基于 Intl，时区与国际化处理完善；需要强时区运算且偏好面向对象 API 时选 | JS | `npm i luxon` | 开源 |
| [Nano ID](https://github.com/ai/nanoid) | 极小、URL 安全的唯一 ID 生成器；需要比 UUID 更短的随机 ID 时用 | JS | `npm i nanoid` | 开源 |
| [p-limit](https://github.com/sindresorhus/p-limit) | 限制 Promise 并发数的小工具；批量调用 API 或 LLM 时避免打爆限流用 | JS | `npm i p-limit` | 开源 |
| [Pino](https://getpino.io) | 极快的 Node.js 结构化 JSON 日志库，开销低、生态完善；Node 后端日志的默认选择 | Node | `npm i pino` | 开源 |
| [Remeda](https://remedajs.com) | 为 TypeScript 设计的函数式工具库，同时支持数据优先和 pipe 管道写法，类型推导精确；喜欢管道式数据变换时选 | TS | `npm i remeda` | 开源 |
| [SuperJSON](https://github.com/ravionhq/superjson) | 能序列化 Date、Map、Set、BigInt 等类型的 JSON 超集；在服务端与客户端之间传递富类型数据（tRPC 常配）时用 | TS | `npm i superjson` | 开源 |
| [TanStack Virtual](https://tanstack.com/virtual/latest) | 无头虚拟滚动库，只渲染可视区域的行/列/网格；长列表或大表格卡顿时用 | React, Vue, Svelte, Solid | `npm i @tanstack/react-virtual`<br>llms.txt: https://tanstack.com/virtual/latest/llms.txt | 开源 |
| [Temporal（polyfill）](https://github.com/fullcalendar/temporal-polyfill) | JavaScript 新一代日期时间标准 Temporal 的轻量 polyfill，原生支持时区、日历和不可变值；新项目想直接面向未来标准、彻底摆脱 Date 的坑时选 | TS | `npm i temporal-polyfill` | 开源 |
| [usehooks-ts](https://usehooks-ts.com) | 类型完善的常用 React hooks 合集（useLocalStorage、useDebounce、useMediaQuery 等）；不想重复手写通用 hook 时装 | React, TS | `npm i usehooks-ts` | 开源 |
| [VueUse](https://vueuse.org) | Vue 组合式函数工具集，200+ 个覆盖浏览器 API、传感器、动画和状态；Vue/Nuxt 项目几乎必装 | Vue, Nuxt | `npm i @vueuse/core` | 开源 |

### 样式工具

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Class Variance Authority（cva）](https://cva.style/docs) | 用声明式配置定义组件样式变体（variant、size 等）并得到类型安全的 props，shadcn/ui 组件的变体方案；给组件写多种外观时的默认选择 | Tailwind, TS | `npm i class-variance-authority`<br>llms.txt: https://cva.style/llms.txt | 开源 |
| [clsx](https://github.com/lukeed/clsx) | 239 字节的条件 className 拼接工具；与 tailwind-merge 组合成 shadcn/ui 里的 cn() 函数 | JS | `npm i clsx` | 开源 |
| [Open Props](https://open-props.style) | 一套即用的 CSS 自定义属性设计令牌（间距、颜色、缓动、阴影等）；不用框架、手写 CSS 时想有一致的设计基线选 | CSS | `npm i open-props` | 开源 |
| [Panda CSS](https://panda-css.com) | 构建期生成原子 CSS 的类型安全 CSS-in-JS，支持 recipes 和设计令牌，兼容服务端组件；想要 CSS-in-JS 的写法又要零运行时时选 | React, TS | `npm install -D @pandacss/dev`<br>`npx -y @pandacss/mcp`<br>llms.txt: https://panda-css.com/llms.txt | 开源 |
| [Tailwind CSS](https://tailwindcss.com) | 原子化 CSS 框架，v4 起用 CSS 配置、Rust 引擎；shadcn/ui 及绝大多数 AI 生成前端代码的默认样式方案 | CSS | `npm install tailwindcss @tailwindcss/vite` | 开源 |
| [Tailwind Variants](https://www.tailwind-variants.org) | 功能更全的变体 API：插槽（slots）、响应式变体、组合继承并内置冲突合并；组件由多个部位组成、cva 不够用时选 | Tailwind, TS | `npm i tailwind-variants`<br>llms.txt: https://www.tailwind-variants.org/llms.txt | 开源 |
| [tailwind-merge](https://github.com/dcastil/tailwind-merge) | 合并 Tailwind 类名并自动解决冲突（后者覆盖前者）；封装可被外部 className 覆盖的组件时必备 | Tailwind, TS | `npm i tailwind-merge` | 开源 |
| [tw-animate-css](https://github.com/Wombosvideo/tw-animate-css) | Tailwind v4 下替代 tailwindcss-animate 的纯 CSS 动画工具类，shadcn/ui 新项目默认引入；需要进出场动画类名时装 | Tailwind | `npm i tw-animate-css` | 开源 |
| [UnoCSS](https://unocss.dev) | 按需生成的原子化 CSS 引擎，预设可兼容 Tailwind 语法，支持属性化模式和纯 CSS 图标；Vue/Vite 生态或想高度自定义规则时选 | Vite, Vue | `npm install -D unocss`<br>llms.txt: https://unocss.dev/llms.txt | 开源 |
| [vanilla-extract](https://vanilla-extract.style) | 用 TypeScript 写样式、构建期产出静态 CSS 的零运行时方案，带类型安全的主题与 Sprinkles 原子类；设计系统想要强类型约束时选 | TS | `npm i @vanilla-extract/css` | 开源 |

### 测试

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Playwright](https://playwright.dev) | 微软的端到端测试框架，一套 API 驱动 Chromium/Firefox/WebKit，自动等待、Trace 回放、并行和代码生成；E2E 测试的默认选择，也是多数浏览器 Agent 的底座 | TS, Python | `npm init playwright@latest` | 开源 |
| ⭐ [Vitest](https://vitest.dev) | 基于 Vite 的测试框架，Jest 兼容 API、原生 ESM/TypeScript、极快的监听模式，并支持真实浏览器模式；JS/TS 单元与组件测试的默认选择 | TS, Vite | `npm install -D vitest`<br>llms.txt: https://vitest.dev/llms.txt | 开源 |
| [Chromatic](https://www.chromatic.com) | Storybook 团队的视觉回归测试与 UI 评审云服务，逐像素比对每个 story；组件库需要防止样式意外变化时选 | Storybook, Playwright | `npm i chromatic`<br>llms.txt: https://www.chromatic.com/docs/llms.txt | 免费+付费 |
| [Cypress](https://www.cypress.io) | 运行在浏览器内的 E2E 与组件测试工具，可视化调试体验好；团队已有 Cypress 用例或偏好其交互式运行器时选 | JS, TS | `npm install cypress --save-dev`<br>llms.txt: https://www.cypress.io/llms.txt | 开源 |
| [Faker](https://fakerjs.dev) | 生成姓名、地址、邮箱、商品等逼真假数据的库，支持中文等多语言区域；写种子数据、测试夹具和演示数据时用 | TS | `npm install @faker-js/faker --save-dev` | 开源 |
| [fast-check](https://fast-check.dev) | TypeScript 的属性测试库，自动生成大量随机输入并缩小反例；测试解析器、算法、序列化等有不变式的纯函数时选 | TS | `npm i fast-check`<br>llms.txt: https://fast-check.dev/llms.txt | 开源 |
| [Grafana k6](https://k6.io) | 用 JavaScript/TypeScript 写脚本的开源负载测试工具；上线前压测 API 和验证性能阈值时选 | JS, Go |  | 开源 |
| [happy-dom](https://github.com/capricorn86/happy-dom) | 比 jsdom 更快的无头 DOM 实现；Vitest 里跑组件测试想提速时把 environment 设为它 | TS | `npm i happy-dom` | 开源 |
| [Jest](https://jestjs.io) | 老牌 JavaScript 测试框架，React Native 官方模板默认使用；维护存量项目或 React Native 时用，其他新项目优先 Vitest | JS, React Native | `npm install --save-dev jest` | 开源 |
| [Maestro](https://maestro.dev) | 用 YAML 编写的移动端与 Web UI 自动化测试框架，内置容错等待，支持 iOS/Android/React Native/Flutter；移动端 E2E 测试的首选 | iOS, Android, YAML | `claude mcp add maestro -- maestro mcp`<br>llms.txt: https://docs.maestro.dev/llms.txt | 开源 |
| [MSW（Mock Service Worker）](https://mswjs.io) | 在网络层拦截请求的 API mock 库，同一份 handler 可用于浏览器、Node 测试和 Storybook；测试或前端先行开发需要模拟后端时选 | TS | `npm i msw --save-dev` | 开源 |
| [Storybook](https://storybook.js.org) | 隔离开发、文档化和测试 UI 组件的工作台，支持交互测试、可访问性检查和视觉回归；做组件库或设计系统时选（其 MCP 插件见 storybook-mcp 条目） | React, Vue, Svelte | `npm create storybook@latest`<br>llms.txt: https://storybook.js.org/llms.txt | 开源 |
| [Stryker Mutator](https://stryker-mutator.io) | 变异测试框架：故意改坏代码看测试能否发现；想衡量测试是否真的有效（而不只是覆盖率数字）时选 | JS, TS | `npm init stryker@latest` | 开源 |
| [Testing Library](https://testing-library.com) | 以用户视角（按角色、文本查询）测试组件的工具族，覆盖 React/Vue/Svelte 等；写不依赖实现细节的组件测试时配 Vitest 使用 | React, Vue, Svelte | `npm install --save-dev @testing-library/react @testing-library/dom @testing-library/user-event` | 开源 |

### 构建与工具链

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Biome](https://biomejs.dev) | Rust 写的一体化格式化器 + Linter，一个配置文件替代 ESLint 和 Prettier，速度快一个数量级；新项目想要最省心、最快的代码规范工具时首选 | TS, JS, CSS | `npm i -D -E @biomejs/biome`<br>`npx @biomejs/biome init` | 开源 |
| ⭐ [pnpm](https://pnpm.io) | 基于内容寻址存储和硬链接的包管理器，安装快、省磁盘、依赖严格，原生支持 workspace 与 catalog；Node 项目和 monorepo 的默认包管理器 | Node | `npm install -g pnpm@latest` | 开源 |
| [Bun](https://bun.sh) | 一体化 JavaScript 运行时 + 包管理器 + 打包器 + 测试运行器，启动和安装极快，内置 SQLite/Postgres/S3 客户端；写脚本、CLI 或追求极致速度的新服务时选 | TS, JS | `curl -fsSL https://bun.sh/install \| bash`<br>llms.txt: https://bun.sh/llms.txt | 开源 |
| [Deno](https://deno.com) | 安全优先的 TypeScript 运行时，默认权限沙箱、内置格式化/测试/打包，兼容 npm；需要沙箱执行脚本或喜欢零配置 TS 时选 | TS | `curl -fsSL https://deno.land/install.sh \| sh`<br>llms.txt: https://docs.deno.com/llms.txt | 开源 |
| [esbuild](https://esbuild.github.io) | Go 写的极速打包与转译器；写构建脚本、打包 Lambda/CLI 或只需要快速转译 TS 时直接用 | Go, JS | `npm install --save-exact --save-dev esbuild` | 开源 |
| [ESLint](https://eslint.org) | 生态最大的 JavaScript/TypeScript Linter，规则和插件最全（React、a11y、框架专用规则）；需要 Biome 尚未覆盖的插件规则时选 | JS, TS | `npm init @eslint/config@latest` | 开源 |
| [Husky + lint-staged](https://typicode.github.io/husky/) | 最普及的 Git hooks 方案，配合 lint-staged 只检查暂存文件；JS 项目里约定俗成的提交前检查组合 | Node | `npm install --save-dev husky lint-staged` | 开源 |
| [Knip](https://knip.dev) | 找出未使用的文件、导出和依赖的工具，支持上百种框架插件；Agent 反复改代码后清理死代码和多余依赖时用 | TS | `npm init @knip/config` | 开源 |
| [Lefthook](https://lefthook.dev) | Go 写的快速 Git hooks 管理器，可并行执行、单个 YAML 配置；想在提交前自动跑 lint/格式化/类型检查时选 | Go, YAML | `npm install lefthook --save-dev`<br>llms.txt: https://lefthook.dev/llms.txt | 开源 |
| [mise](https://mise.jdx.dev) | 多语言运行时版本管理器（Node、Python、Go 等）兼环境变量和任务运行器，asdf 的更快替代；团队要统一各语言工具版本时选 | CLI | `curl https://mise.run \| sh`<br>llms.txt: https://mise.jdx.dev/llms.txt | 开源 |
| [npmmirror 镜像](https://npmmirror.com) | 阿里维护的国内 npm 镜像站，同时镜像 Node、Electron、Playwright 等二进制；国内安装依赖慢或失败时把 registry 指向它 | npm | `npm config set registry https://registry.npmmirror.com` | 免费 |
| [Oxlint / Oxfmt（Oxc）](https://oxc.rs) | VoidZero 的 Rust 工具链：Oxlint 比 ESLint 快数十倍并兼容其常用规则与 JS 插件，Oxfmt 为 Prettier 兼容格式化器；大仓库 lint 太慢或想保留 ESLint 规则习惯时选 | TS, JS | `npm add -D oxlint`<br>llms.txt: https://oxc.rs/llms.txt | 开源 |
| [Prettier](https://prettier.io) | 固执己见的代码格式化器，支持语言最广，配 prettier-plugin-tailwindcss 可排序类名；项目用 ESLint 或需要格式化 Markdown/YAML 等时选 | JS, TS, CSS, Markdown | `npm install --save-dev --save-exact prettier`<br>llms.txt: https://prettier.io/llms.txt | 开源 |
| [publint](https://publint.dev) | 检查 npm 包的 package.json 导出配置是否能被各种环境正确解析；发布库之前跑一遍 | Node | `npx publint` | 开源 |
| [Renovate](https://docs.renovatebot.com) | 自动提交依赖升级 PR 的机器人，分组、自动合并和调度规则灵活；想让依赖保持最新且不被 PR 淹没时选 | GitHub App |  | 开源 |
| [Rolldown](https://rolldown.rs) | Rust 写的 Rollup 兼容打包器，Vite 新一代底层引擎；直接用它的场景不多，了解它有助于排查 Vite 构建问题或写高性能构建脚本 | Rust, JS | `npm install -D rolldown`<br>llms.txt: https://rolldown.rs/llms.txt | 开源 |
| [Rspack / Rsbuild](https://rspack.rs) | 字节跳动开源的 Rust 打包器，兼容 webpack 的配置与插件生态，Rsbuild 是其开箱即用的构建工具；从 webpack 迁移的大型项目想提速时选 | Rust, JS | `npm create rsbuild@latest`<br>llms.txt: https://rspack.rs/llms.txt | 开源 |
| [tsdown](https://tsdown.dev) | 基于 Rolldown 和 Oxc 的库打包器，tsup 的继任者，输出 ESM/CJS 和类型声明；发布 TypeScript 库时的默认打包工具 | TS | `npm install -D tsdown`<br>llms.txt: https://tsdown.dev/llms.txt | 开源 |
| [tsup](https://tsup.egoist.dev) | 基于 esbuild 的零配置 TypeScript 库打包器；存量项目继续可用，⚠ 已不再积极维护，新项目建议用 tsdown | TS | `npm i tsup -D` | 开源 |
| [tsx](https://tsx.is) | 直接运行 TypeScript 文件的 Node.js 增强器，带监听模式；跑脚本、种子数据和开发服务器时替代 ts-node | Node, TS | `npm install -D tsx` | 开源 |
| [TypeScript](https://www.typescriptlang.org) | JavaScript 的类型超集与编译器，本目录里几乎所有前端与 Node 技术栈的基础；新的原生（Go）编译器 tsgo 让类型检查大幅提速，新项目开启 strict 即可 | TS | `npm install -D typescript` | 开源 |
| [typescript-eslint](https://typescript-eslint.io) | 让 ESLint 理解 TypeScript 并提供类型感知规则（如未处理的 Promise）；用 ESLint 检查 TS 项目时必装 | TS | `npm install --save-dev eslint @eslint/js typescript typescript-eslint` | 开源 |

### 环境与配置

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [T3 Env](https://env.t3.gg) | 用 Zod 等 schema 在构建期和运行时校验环境变量，并区分服务端与客户端变量防止泄露；Next.js/Nuxt 等全栈项目管理 env 的默认做法 | TS, Next.js | `npm install @t3-oss/env-nextjs zod` | 开源 |
| [c12](https://github.com/unjs/c12) | UnJS 的智能配置加载器，支持 TS/JSON/YAML/RC 文件、环境覆盖和继承；给自己的 CLI 或框架实现 xxx.config.ts 时用 | TS | `npm i c12` | 开源 |
| [cosmiconfig](https://github.com/cosmiconfig/cosmiconfig) | 按约定搜索并加载工具配置文件（package.json 字段、rc 文件、config.js 等）；写需要用户配置的 Node 工具时用 | Node | `npm i cosmiconfig` | 开源 |
| [direnv](https://direnv.net) | 进入目录时自动加载、离开时卸载环境变量的 shell 扩展；想让每个项目目录自带环境而不污染全局时选 | Shell | llms.txt: https://direnv.net/llms.txt | 开源 |
| [dotenvx](https://dotenvx.com) | dotenv 作者的新一代工具：跨语言加载 .env、多环境文件，并可把 .env 加密后提交进仓库；想安全地随代码分发环境变量时选 | CLI, 多语言 | `npm install @dotenvx/dotenvx --save`<br>llms.txt: https://dotenvx.com/llms.txt | 开源 |
| [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | 用 Pydantic 模型从环境变量、.env 和密钥文件加载并校验配置；Python 服务管理配置的默认做法 | Python | `pip install pydantic-settings`<br>llms.txt: https://docs.pydantic.dev/llms.txt | 开源 |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | 把 .env 文件读进环境变量的最简工具；Python 小脚本只需要加载 .env 时用 | Python | `pip install python-dotenv` | 开源 |
| [Varlock](https://varlock.dev) | 用带注解的 .env.schema 声明环境变量的类型、是否敏感和来源，自动校验、脱敏日志并从密钥管理器取值；想让 Agent 能读配置结构却看不到密钥值时选 | CLI, TS | `npx varlock init`<br>llms.txt: https://varlock.dev/llms.txt | 开源 |

### 命令行工具

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Commander.js](https://github.com/tj/commander.js) | Node.js 最普及的命令行参数解析库，子命令、选项和帮助信息齐全；写 Node CLI 的默认选择 | Node, TS | `npm i commander` | 开源 |
| [citty](https://github.com/unjs/citty) | UnJS 的轻量 CLI 构建器，类型安全的参数定义、子命令懒加载（Nuxt CLI 同款）；想要零依赖、ESM 优先的小型 CLI 时选 | TS | `npm i citty` | 开源 |
| [Clack](https://bomb.sh/docs/clack/basics/getting-started/) | 外观精致的交互式命令行提示组件（输入、选择、多选、加载动画）；做 create-xxx 式脚手架向导时选 | Node, TS | `npm i @clack/prompts` | 开源 |
| [Click](https://click.palletsprojects.com) | 装饰器风格的 Python CLI 库，Typer 的底层；需要更细的控制或维护存量工具时用 | Python | `pip install click` | 开源 |
| [execa](https://github.com/sindresorhus/execa) | 更好用的子进程执行库，Promise 接口、模板字符串语法和流式输出；Node 脚本里调用外部命令时用 | Node | `npm i execa` | 开源 |
| [Ink](https://github.com/vadimdemedes/ink) | 用 React 组件和 Flexbox 布局写终端界面的渲染器（Claude Code、Gemini CLI 等都在用）；做带实时刷新、复杂布局的终端应用时选 | React, Node | `npm install ink react` | 开源 |
| [Inquirer](https://github.com/SBoudrias/Inquirer.js) | 经典的交互式命令行提问库，新版拆分为 @inquirer/prompts；需要丰富的提问类型和成熟生态时选 | Node | `npm i @inquirer/prompts` | 开源 |
| [oclif](https://oclif.io) | Salesforce 开源的 CLI 框架（Heroku、Shopify CLI 同款），插件体系、自动更新和文档生成；做大型、可扩展的产品级 CLI 时选 | Node, TS | `npx oclif generate mynewcli` | 开源 |
| [OpenTUI](https://opentui.com) | SST 团队用 Zig 内核写的 TypeScript 终端 UI 库（OpenCode 同款），支持 React/Solid 绑定；想做高性能、动画流畅的 TUI 时选，⚠ 仍较新 | TS, Bun | `npm i @opentui/core` | 开源 |
| [picocolors](https://github.com/alexeyraspopov/picocolors) | 最小最快的终端着色库；CLI 只需要给输出上色时用它替代 chalk | Node | `npm i picocolors` | 开源 |
| [Rich](https://rich.readthedocs.io) | 在终端输出彩色文本、表格、进度条、Markdown 和语法高亮的 Python 库；让脚本和 CLI 的输出更可读 | Python | `pip install rich` | 开源 |
| [Textual](https://textual.textualize.io) | 用 Python 写全功能终端应用的 TUI 框架，CSS 式布局、组件丰富，还能发布成 Web；做交互式终端面板时选 | Python | `pip install textual` | 开源 |
| [Typer](https://typer.tiangolo.com) | 基于类型注解的 Python CLI 框架（FastAPI 作者出品），自动生成帮助与补全；写 Python 命令行工具的默认选择 | Python | `pip install typer` | 开源 |
| [yargs](https://yargs.js.org) | 功能丰富的参数解析库，自动生成帮助、补全和校验；参数规则复杂或存量项目用 | Node | `npm i yargs` | 开源 |
| [zx](https://google.github.io/zx/) | Google 出的用 JavaScript 写 shell 脚本的工具，$`cmd` 语法自动转义；想用 JS/TS 替代复杂 bash 脚本时选 | Node, TS | `npm i zx` | 开源 |

### Python 基础

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Pydantic](https://docs.pydantic.dev) | 基于类型注解的数据校验与序列化库（Rust 内核），FastAPI、各家 LLM SDK 和结构化输出的共同基础；Python 里定义数据模型的默认选择 | Python | `pip install pydantic`<br>llms.txt: https://docs.pydantic.dev/latest/llms.txt | 开源 |
| ⭐ [pytest](https://docs.pytest.org) | Python 测试的事实标准：普通 assert、fixture 依赖注入、参数化和庞大的插件生态；Python 测试的默认选择 | Python | `pip install pytest` | 开源 |
| ⭐ [Ruff](https://docs.astral.sh/ruff/) | Rust 写的 Python Linter + 格式化器，一个工具替代 Flake8、isort、Black 等，速度极快；Python 代码规范的默认选择 | Python | `uv add --dev ruff`<br>llms.txt: https://docs.astral.sh/ruff/llms.txt | 开源 |
| ⭐ [uv](https://docs.astral.sh/uv/) | Astral 用 Rust 写的 Python 包与项目管理器，一个工具替代 pip、venv、pipx、pyenv 和 poetry，速度快 10–100 倍；Python 项目的默认工具链入口，uvx 可直接运行 MCP 等命令行工具 | Python | `curl -LsSf https://astral.sh/uv/install.sh \| sh`<br>llms.txt: https://docs.astral.sh/uv/llms.txt | 开源 |
| [Alembic](https://alembic.sqlalchemy.org) | SQLAlchemy 官方数据库迁移工具，可根据模型自动生成迁移脚本；用 SQLAlchemy/SQLModel 时管理表结构变更 | Python | `pip install alembic` | 开源 |
| [Celery](https://docs.celeryq.dev) | Python 最成熟的分布式任务队列，支持 Redis/RabbitMQ、定时任务和工作流编排；Django/Flask 项目跑后台任务的传统选择 | Python, Redis | `pip install celery` | 开源 |
| [Django](https://www.djangoproject.com) | 「自带电池」的 Python Web 框架：ORM、迁移、后台管理、认证和表单一应俱全；内容型或后台管理型应用想最快交付时选 | Python | `pip install Django` | 开源 |
| [FastAPI](https://fastapi.tiangolo.com) | 基于类型注解和 Pydantic 的高性能异步 Web 框架，自动生成 OpenAPI 文档；Python 写 API 和 AI 后端的默认框架（完整模板见 fastapi-template 条目） | Python | `pip install "fastapi[standard]"` | 开源 |
| [Flask](https://flask.palletsprojects.com) | 经典的轻量 WSGI 微框架；小型服务、教学示例或维护存量项目时用 | Python | `pip install Flask` | 开源 |
| [HTTPX](https://www.python-httpx.org) | 同时支持同步和异步的现代 HTTP 客户端，API 接近 requests 并支持 HTTP/2；Python 里发请求的默认选择 | Python | `pip install httpx` | 开源 |
| [Hypothesis](https://hypothesis.readthedocs.io) | Python 的属性测试库，自动生成边界输入并缩小失败用例；测试有不变式的函数、解析器和数据处理代码时配 pytest 使用 | Python | `pip install hypothesis` | 开源 |
| [Litestar](https://litestar.dev) | 高性能 ASGI 框架，内置依赖注入、DTO、OpenAPI 和多种 ORM 集成；想要比 FastAPI 更强约定和内置功能的 API 框架时选 | Python | `pip install litestar`<br>llms.txt: https://litestar.dev/llms.txt | 开源 |
| [Loguru](https://loguru.readthedocs.io) | 开箱即用的 Python 日志库，一个 logger 搞定格式、轮转和异常回溯；脚本和小服务不想配置 logging 模块时选 | Python | `pip install loguru` | 开源 |
| [mypy](https://mypy-lang.org) | Python 类型检查的参考实现，插件生态成熟（Django、SQLAlchemy、Pydantic）；存量项目或依赖其插件时用 | Python | `pip install mypy` | 开源 |
| [orjson](https://github.com/ijl/orjson) | Rust 写的最快 Python JSON 库，原生支持 dataclass、datetime 和 numpy；JSON 序列化成为性能瓶颈时替换标准库 | Python | `pip install orjson` | 开源 |
| [Poetry](https://python-poetry.org) | 老牌的 Python 依赖管理与打包工具；维护存量 Poetry 项目时用，新项目优先 uv | Python | pipx install poetry | 开源 |
| [pre-commit](https://pre-commit.com) | 多语言 Git 提交钩子管理框架，用 YAML 声明要跑的检查；Python 项目在提交前自动跑 Ruff、类型检查时用 | Python, YAML | `pip install pre-commit` | 开源 |
| [Pyright / basedpyright](https://github.com/microsoft/pyright) | 微软的 Python 静态类型检查器（VS Code Pylance 内核），社区分支 basedpyright 规则更严并可直接 pip 安装；需要最完整的类型规范支持时选 | Python | `pip install pyright`<br>`pip install basedpyright` | 开源 |
| [SQLAlchemy](https://www.sqlalchemy.org) | Python 最成熟的 SQL 工具包与 ORM，2.0 起有完整类型和异步支持；需要复杂查询、多数据库或精细控制时选 | Python | `pip install SQLAlchemy` | 开源 |
| [SQLModel](https://sqlmodel.tiangolo.com) | 把 SQLAlchemy 与 Pydantic 合成一个模型定义的 ORM（FastAPI 作者出品）；FastAPI 项目想让表模型和接口模型共用一套定义时选 | Python | `pip install sqlmodel` | 开源 |
| [structlog](https://www.structlog.org) | 结构化日志库，输出带上下文的 JSON 日志；生产服务要把日志送进日志平台检索时选 | Python | `pip install structlog` | 开源 |
| [Taskiq](https://taskiq-python.github.io) | 原生 asyncio 的分布式任务队列，类型友好并与 FastAPI 依赖注入集成；异步 Python 服务想要比 Celery 更现代的任务队列时选 | Python | `pip install taskiq` | 开源 |
| [Tenacity](https://tenacity.readthedocs.io) | 通用的重试装饰器库，支持指数退避、抖动和条件重试；调用不稳定的外部 API 或 LLM 接口时用 | Python | `pip install tenacity` | 开源 |
| [ty](https://docs.astral.sh/ty/) | Astral 用 Rust 写的 Python 类型检查器和语言服务器，比 mypy/Pyright 快一到两个数量级；已用 uv + Ruff、想统一工具链并加速类型检查时选 | Python | `uv tool install ty@latest`<br>llms.txt: https://docs.astral.sh/ty/llms.txt | 开源 |
| [Uvicorn](https://uvicorn.dev) | 基于 uvloop 的 ASGI 服务器；运行 FastAPI/Starlette/Litestar 应用的标准方式 | Python | `pip install uvicorn` | 开源 |
| [清华 PyPI 镜像（TUNA）](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/) | 清华大学开源软件镜像站的 PyPI 镜像；国内 pip/uv 安装慢时把 index-url 指向它 | Python | `pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple` | 免费 |

### Python 数据与界面

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Polars](https://pola.rs) | Rust 写的多线程 DataFrame 库，惰性执行与查询优化，处理大数据比 pandas 快且省内存；新写的数据处理代码默认选它 | Python, Rust | `pip install polars` | 开源 |
| ⭐ [Streamlit](https://streamlit.io) | 用纯 Python 脚本几分钟做出数据应用和 AI Demo 的框架，脚本自上而下重跑；内部工具、数据看板和模型演示的最快路径 | Python | `pip install streamlit`<br>llms.txt: https://docs.streamlit.io/llms.txt | 开源 |
| [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) | 容错性强的 HTML/XML 解析库；从静态网页里提取数据的入门首选，配 httpx 使用 | Python | `pip install beautifulsoup4` | 开源 |
| [Chainlit](https://docs.chainlit.io) | 专为对话式 AI 设计的 Python 界面框架，内置消息流、步骤可视化、文件上传和认证；用 Python 快速给 Agent 或 RAG 套一个聊天界面时选 | Python | `pip install chainlit`<br>llms.txt: https://docs.chainlit.io/llms.txt | 开源 |
| [Flet](https://flet.dev) | 用 Python 调用 Flutter 控件构建 Web、桌面和移动应用的框架；Python 开发者想打包出原生桌面或手机应用时选 | Python, Flutter | `pip install flet` | 开源 |
| [Gradio](https://www.gradio.app) | 为机器学习模型快速生成 Web 界面的库，输入输出组件丰富，一行分享并可直接发布到 Hugging Face Spaces，还能把函数暴露成 MCP 服务器；做模型 Demo 时选 | Python | `pip install gradio` | 开源 |
| [Ibis](https://ibis-project.org) | 可移植的 Python DataFrame API，同一份代码可在 DuckDB、Polars、BigQuery、Snowflake 等二十多种后端执行；想让分析代码不绑定具体引擎时选 | Python | `pip install ibis-framework` | 开源 |
| [JupyterLab](https://jupyter.org) | 交互式笔记本的标准环境，科研、教学和探索性分析的通用语言；需要与现有 .ipynb 生态和云端 Notebook 兼容时用 | Python | `pip install jupyterlab` | 开源 |
| [marimo](https://marimo.io) | 响应式 Python 笔记本，以纯 .py 文件存储、单元格自动按依赖重算，可当脚本运行或发布成应用；想要可复现、可用 Git 管理的 Jupyter 替代时选 | Python | `pip install marimo`<br>llms.txt: https://marimo.io/llms.txt | 开源 |
| [Matplotlib](https://matplotlib.org) | Python 绘图的基础库，能画几乎任何静态图；出论文图、需要像素级控制或被其他库依赖时用 | Python | `pip install matplotlib` | 开源 |
| [NiceGUI](https://nicegui.io) | 基于 FastAPI 和 Vue/Quasar 的 Python UI 框架，事件驱动、状态保留在服务端；需要比 Streamlit 更可控的交互（按钮回调、实时更新、硬件控制面板）时选 | Python | `pip install nicegui`<br>llms.txt: https://nicegui.io/llms.txt | 开源 |
| [NumPy](https://numpy.org) | Python 数值计算的基础数组库，科学计算与机器学习生态的共同底座；做向量和矩阵运算时用 | Python | `pip install numpy` | 开源 |
| [pandas](https://pandas.pydata.org) | Python 数据分析的经典 DataFrame 库，生态与教程最多；与现有科学计算库对接或数据量不大时用 | Python | `pip install pandas` | 开源 |
| [Pandera](https://pandera.readthedocs.io) | DataFrame 的 schema 校验库，支持 pandas、Polars 等；数据管线里需要在运行时断言列类型和取值范围时用 | Python | `pip install pandera` | 开源 |
| [Plotly / Dash](https://plotly.com/python/) | 交互式图表库 Plotly 及其之上的数据应用框架 Dash；要做可缩放、可悬停的图表或企业级分析看板时选 | Python | `pip install plotly dash`<br>llms.txt: https://plotly.com/llms.txt | 开源 |
| [Reflex](https://reflex.dev) | 用纯 Python 写全栈 Web 应用的框架，前端编译为 React、后端为 FastAPI；Python 开发者想做正式的多页面应用而不学 JavaScript 时选 | Python | `pip install reflex`<br>llms.txt: https://reflex.dev/llms.txt | 开源 |
| [scikit-learn](https://scikit-learn.org) | 经典机器学习算法库（分类、回归、聚类、降维、模型评估）；表格数据建模和传统 ML 基线的默认选择 | Python | `pip install scikit-learn` | 开源 |
| [Vega-Altair](https://altair-viz.github.io) | 基于 Vega-Lite 的声明式统计可视化库，语法简洁、默认美观；在笔记本里做探索性图表时选 | Python | `pip install altair` | 开源 |
