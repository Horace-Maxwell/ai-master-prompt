# 其他框架与 CSS 组件库

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-frameworks-other"></a>

## 其他框架组件库（Vue / Svelte / Angular / Solid / Web Components）

项目不是 React 时从这里选。

本类分组：Vue / Nuxt · Svelte · Angular · Solid / Qwik · Web Components / 跨框架

### Vue / Nuxt

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [PrimeVue](https://primevue.org) | Vue 生态组件最全的套件之一（90+ 组件，Styled / Unstyled 双模式 + 主题预设），做后台、数据密集型应用时首选；官方提供 MCP | Vue, Nuxt | `npm install primevue @primeuix/themes`<br>`claude mcp add primevue -- npx -y @primevue/mcp` | 开源 |
| [Flowbite Vue](https://flowbite-vue.com) | Flowbite 设计体系的 Vue 3 组件封装，基于 Tailwind；项目已用 Flowbite 样式时选 | Vue, Tailwind | `npm i flowbite flowbite-vue` | 开源 |
| [Headless UI](https://headlessui.com) | Tailwind Labs 出的无样式组件（React + Vue），与 Tailwind 配合最顺；只需少量基础交互组件时选 ⚠ Vue 版停在 v1.7，组件数少于 React 版 | Vue, React, Tailwind | `npm install @headlessui/vue@latest` | 开源 |
| [Maz-UI](https://maz-ui.com) | Vue / Nuxt 组件库，自带主题、图标、i18n 和 Nuxt 模块；想要开箱即用又对 Agent 友好（MCP + llms.txt）时选 | Vue, Nuxt | `npm install maz-ui`<br>`npx @maz-ui/mcp init`<br>llms.txt: https://maz-ui.com/llms.txt | 开源 |
| [Oruga UI](https://oruga-ui.com) | 不绑定任何 CSS 框架的 Vue 组件库，class 全可配，可套 Bootstrap / Bulma / Tailwind 主题；已有样式体系只缺组件逻辑时选 | Vue | `npm install @oruga-ui/oruga-next` | 开源 |
| [Quasar](https://quasar.dev) | Vue 全家桶框架：一套代码出 SPA / SSR / PWA / 移动端（Capacitor）/ 桌面（Electron），自带 Material 组件；要一份代码多端发布时选 | Vue | `npm init quasar@latest`<br>llms.txt: https://quasar.dev/llms.txt | 开源 |
| [Reka UI（原 Radix Vue）](https://reka-ui.com) | Vue 的无样式无障碍原语库，shadcn-vue 和 Nuxt UI 的底座；自建 Vue 设计系统、需要完全掌控样式时选 | Vue, Nuxt | `npm install reka-ui`<br>llms.txt: https://reka-ui.com/llms.txt | 开源 |
| [Volt（PrimeVue）](https://volt.primevue.org) | PrimeVue 团队的 Tailwind 版：基于 Unstyled PrimeVue 的 copy-paste 组件，代码进仓库可随意改；想要 shadcn 式工作流又要 PrimeVue 功能时选 ⚠ CLI 包仍是 alpha | Vue, Tailwind | `npx volt-vue add Button` | 开源 |
| [Vuetify](https://vuetifyjs.com) | Vue 的 Material Design 组件框架，组件多、生态老牌；要 Material 风格或需要长期维护的企业项目时选；有官方 MCP 和 llms.txt | Vue, Nuxt | `npm create vuetify@latest`<br>`claude mcp add --transport http vuetify-mcp https://mcp.vuetifyjs.com/mcp`<br>llms.txt: https://vuetifyjs.com/llms.txt | 开源 |

### Svelte

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Bits UI](https://bits-ui.com) | Svelte 5 无样式无障碍原语库，shadcn-svelte 的底座；自建 Svelte 设计系统时首选 | Svelte | `npm install bits-ui`<br>llms.txt: https://bits-ui.com/llms.txt | 开源 |
| [Carbon Components Svelte](https://svelte.carbondesignsystem.com) | IBM Carbon 设计系统的 Svelte 实现，数据表格等企业组件齐全；做企业后台、要 IBM 风格时选 | Svelte | `npm i carbon-components-svelte`<br>llms.txt: https://svelte.carbondesignsystem.com/llms.txt | 开源 |
| [Flowbite Svelte](https://flowbite-svelte.com) | Flowbite 的 Svelte 实现，Tailwind 样式开箱即用；想在 Svelte 里快速搭常规页面时选 | Svelte, Tailwind | `pnpm i -D flowbite-svelte flowbite` | 开源 |
| [LayerChart](https://www.layerchart.com) | Svelte 的可组合图表库（基于 Layer Cake，shadcn-svelte 图表的底层）；在 Svelte 里画图表时选 | Svelte | llms.txt: https://www.layerchart.com/llms.txt | 开源 |
| [M3 Svelte](https://kendell.dev/m3-svelte/) | Material 3 的 Svelte 实现，体积小并支持动态配色；Svelte 项目要 Material You 风格时选 | Svelte | `pnpm install m3-svelte vite-plugin-functions-mixins @ktibow/iconset-material-symbols @fontsource-variable/google-sans-flex -D` | 开源 |
| [Melt UI](https://next.melt-ui.com) | Svelte 的 headless builders：把行为挂到任意元素上，比组件式原语更灵活；需要最底层控制时选 ⚠ 更新放缓（melt 包 2026-01 后无新版） | Svelte | `npm install melt` | 开源 |
| [Motion Core](https://motion-core.dev) | Svelte 原生动效组件库，GSAP + OGL 驱动（画廊、磁吸、WebGL 效果），CLI 复制源码；要更重的创意动效时选 | Svelte, GSAP | `npx @motion-core/cli init`<br>llms.txt: https://motion-core.dev/llms.txt | 开源 |
| [shadcn-svelte-extras](https://www.shadcn-svelte-extras.com) | shadcn-svelte 的补充组件（聊天、代码块、文件拖放、图片裁剪等），用 jsrepo 安装；官方库缺组件时来这里找 | Svelte, Tailwind | jsrepo init @ieedan/shadcn-svelte-extras<br>jsrepo add button<br>llms.txt: https://www.shadcn-svelte-extras.com/llms.txt | 开源 |
| [Skeleton](https://www.skeleton.dev) | 基于 Tailwind 的自适应设计系统 + Zag.js 驱动的组件（Svelte / React），主题生成器好用；SvelteKit 项目要整套带主题的 UI 时选 | Svelte, Tailwind | `npm i -D @skeletonlabs/skeleton @skeletonlabs/skeleton-svelte`<br>llms.txt: https://www.skeleton.dev/llms.txt | 开源 |
| [Svelte Animations](https://sv-animations.vercel.app) | Svelte 版 Magic UI 风格动效组件，基于 motion-sv，按 shadcn-svelte registry 分发；给 Svelte 落地页加动效时选 | Svelte, Tailwind | `pnpm dlx shadcn-svelte@latest add https://sv-animations.vercel.app/r/morphing-text.json` | 开源 |
| [Svelte Material UI（SMUI）](https://sveltematerialui.com) | 基于 Material Components Web 的 Svelte 组件库；Svelte 项目要严格 Material 风格时选 | Svelte | `npm install --save svelte-material-ui` | 开源 |
| [Svelte UX](https://svelte-ux.techniq.dev) | Tailwind 驱动的 Svelte 组件 + actions / stores 工具集，和 LayerChart 同作者；做数据应用界面时选 | Svelte, Tailwind |  | 开源 |

### Angular

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Angular Material + CDK](https://material.angular.dev) | Angular 官方 Material Design 组件库及底层 CDK，与框架同步发版；Angular 项目的默认选择 | Angular | ng add @angular/material<br>`npx -y @angular/cli mcp`（Angular CLI 自带的 MCP） | 开源 |
| [Angular Aria](https://angular.dev/guide/aria/overview) | Angular 官方的无样式无障碍指令集（headless）；想自己写样式但要正确的键盘与 ARIA 行为时选 | Angular | `npm install @angular/aria`<br>llms.txt: https://angular.dev/llms.txt | 开源 |
| [Angular Primitives](https://angularprimitives.com) | Angular 的 headless 原语库（类似 Radix），无样式、可访问；自建 Angular 设计系统时选 | Angular | `npm install ng-primitives` | 开源 |
| [ng-bootstrap](https://ng-bootstrap.github.io) | 用 Angular 原生重写的 Bootstrap 组件（不依赖 jQuery）；团队用 Bootstrap 样式的 Angular 项目选它 | Angular, Bootstrap | ng add @ng-bootstrap/ng-bootstrap | 开源 |
| [PrimeNG](https://primeng.org) | Angular 组件最全的套件（表格、图表、编辑器齐全），主题体系与 PrimeVue 共用；企业后台首选之一；官方提供 MCP | Angular | `npm install primeng @primeuix/themes`<br>`claude mcp add primeng -- npx -y @primeng/mcp` | 开源 |
| [spartan/ui](https://spartan.ng) | Angular 版 shadcn/ui：brain（无样式原语）+ helm（Tailwind 样式）复制进项目；Angular + Tailwind 项目选它；有官方 MCP | Angular, Tailwind | ng g @spartan-ng/cli:ui<br>`npx -y @spartan-ng/mcp`（MCP，写入客户端配置） | 开源 |
| [Taiga UI](https://taiga-ui.dev) | T-Bank 开源的 Angular 组件库，100+ 组件，模块化、可深度定制；要现代观感的 Angular 应用时选 | Angular | ng add taiga-ui<br>llms.txt: https://taiga-ui.dev/llms.txt | 开源 |
| [Zard UI](https://zardui.com) | 另一个 Angular 版 shadcn/ui：CLI 把 Tailwind 组件源码写进项目；与 spartan/ui 二选一 | Angular, Tailwind | `npx zard-cli init`<br>`npx zard-cli add button`<br>llms.txt: https://zardui.com/llms.txt | 开源 |

### Solid / Qwik

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [corvu](https://corvu.dev) | SolidJS 无样式原语，补齐 Kobalte 没有的 Drawer、Resizable、OTP 等；做复杂交互组件时配合 Kobalte 用 | Solid | `npm install corvu` | 开源 |
| [Kobalte](https://kobalte.dev) | SolidJS 的无样式无障碍组件库（相当于 Solid 版 Radix），solid-ui / shadcn-solid 的底座 | Solid | `npm install @kobalte/core`<br>llms.txt: https://kobalte.dev/llms.txt | 开源 |
| [Qwik UI](https://qwikui.com) | Qwik 官方社区组件库：headless 套件 + 带样式套件；Qwik 项目基本只有这一个选择 | Qwik | `npm install -D @qwik-ui/headless` | 开源 |
| [shadcn-solid](https://shadcn-solid.com) | 另一个 shadcn/ui 的 SolidJS 移植，跟进上游较快；与 solid-ui 二选一 | Solid, Tailwind | `npx shadcn-solid@latest init` | 开源 |
| [solid-ui](https://www.solid-ui.com) | shadcn/ui 的 SolidJS 移植（Kobalte + Corvu + Tailwind），CLI 复制源码；Solid 项目要 shadcn 风格时选 | Solid, Tailwind | `npx solidui-cli@latest init` | 开源 |

### Web Components / 跨框架

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [AgnosticUI](https://www.agnosticui.com) | 以 Lit 为核心、同时输出 React / Vue / Svelte 的组件库，CLI 把源码复制进项目 ⚠ v2 仍是 alpha | Lit, React, Vue, Svelte | `npx agnosticui-cli init --framework vue` | 开源 |
| [bejamas/ui](https://ui.bejamas.com) | Bejamas 出的 Astro 版 shadcn 组件，自带 CLI；把 React 站点迁到 Astro 时好用 | Astro, Tailwind | `npx bejamas@latest init`<br>`npx bejamas@latest add button` | 开源 |
| [Carbon Web Components](https://web-components.carbondesignsystem.com) | IBM Carbon 设计系统的 Web Components 版；非 React 技术栈想用 Carbon 时选 | Web Components | `npm install @carbon/web-components` | 开源 |
| [FAST](https://fast.design) | 微软的轻量 Web Components 基础库（Fluent Web Components 的底层）；需要比 Lit 更底层的性能控制时选 | Web Components | `npm install --save @microsoft/fast-element` | 开源 |
| [Framework7](https://framework7.io) | 老牌移动端 UI 框架，iOS / Material 双主题，支持原生 JS、Vue、React、Svelte；要高度拟原生的 H5 / 混合应用时选 | Vue, React, Svelte | `npm install framework7` | 开源 |
| [fulldev/ui](https://ui.full.dev) | Astro 组件与区块，按 shadcn 兼容 registry 分发，直接用 shadcn CLI 安装；做内容型网站时选 | Astro, Tailwind | 先在 components.json 的 registries 里加 `"@fulldev": "https://ui.full.dev/r/styles/{style}/{name}.json"`，再运行 `npx shadcn@latest add @fulldev/button`；llms.txt: https://ui.full.dev/llms.txt | 开源 |
| [Ionic Framework](https://ionicframework.com) | 基于 Web Components 的移动端 UI 套件，自动切换 iOS / Material 外观，配 Capacitor 打包成原生 App；用 Web 技术做 App 时首选 | Web Components, Angular, React, Vue | `npm install -g @ionic/cli`<br>ionic start | 开源 |
| [Konsta UI](https://konstaui.com) | 用 Tailwind 写的 iOS / Material 风移动端组件（React / Vue / Svelte），可搭配 Ionic 或 Framework7；Tailwind 项目要拟原生移动 UI 时选 | React, Vue, Svelte, Tailwind | `npm i konsta` | 开源 |
| [Lion](https://lion.js.org) | ING 银行开源的白标 Web Components：只给行为和无障碍，不带样式；作为自有设计系统的底层时选 | Web Components, Lit | `npm i @lion/ui` | 开源 |
| [Lit](https://lit.dev) | Google 的轻量 Web Components 基础库，写一次组件可在任何框架里用；要做跨框架设计系统时选 | Web Components, TS | `npm i lit` | 开源 |
| [Starwind UI](https://starwind.dev) | 面向 Astro 的 shadcn 式组件库（另有 Vue / Svelte 适配），CLI 复制源码，不需要 React；Astro 内容站首选；有 MCP 和 llms.txt | Astro, Tailwind | `npx starwind@latest init`<br>`npx -y @starwind-ui/mcp`（MCP，写入客户端配置）<br>llms.txt: https://starwind.dev/llms.txt | 开源 |
| [Stencil](https://stenciljs.com) | 把 TSX 编译成标准 Web Components 的编译器（Ionic 团队出品），可自动生成 React / Vue / Angular 封装；自建跨框架组件库时选 | Web Components, TS | `npm init stencil` | 开源 |
| [Web Awesome（Shoelace 继任）](https://webawesome.com) | Shoelace 的继任者（原仓库已归档），框架无关的 Web Components 组件库，CDN 一行即可用；不想绑框架时首选 ⚠ Pro 组件与主题付费 | Web Components | `npm install @awesome.me/webawesome`<br>llms.txt: https://webawesome.com/llms.txt | 免费+付费 |
| [Zag.js](https://zagjs.com) | 用状态机实现的框架无关组件逻辑（Ark UI 的底层），有 React / Vue / Solid / Svelte 适配器；要一套交互逻辑跨多个框架复用时选 | React, Vue, Solid, Svelte | `npm install @zag-js/toggle-group @zag-js/react`（按组件 + 框架适配器分包，示例）<br>llms.txt: https://zagjs.com/llms.txt | 开源 |

<a id="ui-css-kits"></a>

## CSS 框架与纯 HTML / Tailwind 组件

不依赖前端框架，复制 HTML 或加一个 CSS 文件就能用。

本类分组：CSS 框架与引擎 · Tailwind 组件与区块 · 轻量 / 免 class

### CSS 框架与引擎

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Bootstrap](https://getbootstrap.com) | 最老牌的 CSS 组件框架，类名即组件、资料最多；服务端渲染模板或不想配构建工具时选 ⚠ 官网首页已展示 v6 alpha，生产用 5.3 | CSS, JS | `npm install bootstrap@5.3.8`<br>llms.txt: https://getbootstrap.com/llms.txt | 开源 |
| [Beer CSS](https://www.beercss.com) | 基于 Material Design 3 的轻量 CSS 框架，不用构建；想零配置做 Material You 风页面时选 | CSS | `npm i beercss`<br>llms.txt: https://www.beercss.com/llms.txt | 开源 |
| [Bulma](https://bulma.io) | 纯 CSS（无 JS）的 Flexbox 组件框架，类名直观；不想引 JS、只要干净样式时选 | CSS, Sass | `npm install bulma` | 开源 |
| [Charts.css](https://chartscss.org) | 用纯 CSS 类把 HTML 表格渲染成图表（柱、线、面积、饼），零 JS；静态站或邮件式报表里要轻量图表时选 | CSS | `npm install charts.css` | 开源 |
| [cva（class-variance-authority）](https://cva.style) | 用类型安全的方式声明组件变体到类名的映射，shadcn/ui 的标配；自己写带 variant 的 Tailwind 组件时用 | Tailwind, TS | `npm i class-variance-authority`<br>llms.txt: https://cva.style/llms.txt | 开源 |
| [Master CSS](https://css.master.co) | 一种"CSS 语言"式的原子化框架，类名语法更接近原生 CSS；觉得 Tailwind 缩写难记时可试；有 MCP 和 llms.txt | CSS | `npx -y @master/css-mcp@latest`（MCP，需加 --root 项目路径）<br>llms.txt: https://css.master.co/llms.txt | 开源 |
| [Materialize](https://materializeweb.com) | 经典 Material Design CSS 框架的社区维护版（已支持 Material 3）；维护老 Materialize 项目或要纯 CSS Material 时选 | CSS, JS | `npm install @materializecss/materialize` | 开源 |
| [Pure.css](https://pure-css.github.io) | 极小的响应式 CSS 模块集（栅格、表单、按钮、表格、菜单），gzip 后仅几 KB；只需要基础样式骨架时选 | CSS |  | 开源 |
| [StyleX](https://stylexjs.com) | Meta 的编译期原子化 CSS-in-JS，样式合并结果可预测；大型 React 代码库要可扩展样式方案时选 | CSS-in-JS, React | `npm install --save @stylexjs/stylex` | 开源 |
| [UIkit](https://getuikit.com) | 模块化的 CSS + JS 前端框架，组件丰富、更新稳定；做传统多页站点时选 | CSS, JS | `npm install uikit` | 开源 |

### Tailwind 组件与区块

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [Basecoat](https://basecoatui.com) | 不依赖 React 的 shadcn/ui 风组件：一份 Tailwind CSS 加少量原生 JS，适配任何后端模板（Django、Rails、Laravel、HTMX） | Tailwind, HTML | `npm install basecoat-css`<br>llms.txt: https://basecoatui.com/llms.txt | 开源 |
| [Float UI](https://floatui.com) | 免费开源的 Tailwind 组件与落地页模板，提供 React / Vue / Svelte / HTML 版本 ⚠ 仓库 2025-03 后未更新 | Tailwind, HTML, React, Vue |  | 免费 |
| [FlyonUI](https://flyonui.com) | daisyUI 式语义类名 + Preline JS 插件的组合，纯 Tailwind 组件带交互；想要语义类名又要下拉、弹窗等交互时选 ⚠ Pro 区块与 MCP 高级功能付费 | Tailwind, HTML | `npm install flyonui`<br>llms.txt: https://flyonui.com/llms.txt（MCP 见 https://flyonui.com/mcp） | 免费+付费 |
| [Franken UI](https://franken-ui.dev) | 把 shadcn/ui 观感搬到纯 HTML（基于 UIkit + Tailwind），不需要 React；服务端模板项目想要 shadcn 风时选 ⚠ README 公告项目已转向 0build（0build.dev） | Tailwind, HTML, UIkit |  | 开源 |
| [Mamba UI](https://mambaui.com) | 150+ 免费 Tailwind 组件与模板，可复制 HTML 或 JSX（MIT）⚠ 仓库 2024 年后未更新 | Tailwind, HTML |  | 免费 |
| [Meraki UI](https://merakiui.com) | 免费 Tailwind 组件合集，支持 RTL 和暗色模式，复制 HTML 即用 ⚠ 仓库 2025-07 后未更新 | Tailwind, HTML |  | 免费 |
| [Oxbow UI](https://oxbowui.com) | MIT 许可的 Tailwind + Alpine.js 区块合集（营销页、定价、登录等），复制即用；做静态站或 Astro 站时选 | Tailwind, Alpine.js |  | 免费 |
| [Pagedone](https://pagedone.io) | 开源 Tailwind 组件与区块库，配套 Figma 设计系统；设计稿与代码需要对得上时选 ⚠ 部分模板付费 | Tailwind, HTML, Figma |  | 免费+付费 |
| [Penguin UI](https://www.penguinui.com) | 免费的 Tailwind + Alpine.js 组件合集，带主题切换；不想上 React 又要带交互的组件时选 | Alpine.js, Tailwind |  | 免费 |
| [Pines UI](https://devdojo.com/pines) | Alpine.js + Tailwind 的交互组件库（弹窗、轮播、提示等），复制粘贴、无需构建；Laravel / Livewire 或纯 HTML 项目选它 | Alpine.js, Tailwind |  | 免费 |
| [Preline UI](https://preline.co) | 开源 Tailwind 组件库，自带原生 JS 交互插件，不绑定框架；任何技术栈想用 Tailwind 组件时选 ⚠ Pro 区块和模板付费 | Tailwind, HTML | `npm i preline`<br>`npx skills add htmlstreamofficial/preline` | 免费+付费 |
| [Tailwind Components（Creative Tim）](https://www.creative-tim.com/twcomponents/) | 原 tailwindcomponents.com，现由 Creative Tim 托管的 600+ 免费社区 Tailwind 组件与模板 | Tailwind, HTML |  | 免费 |
| [Tailwind Flex](https://tailwindflex.com) | 社区投稿的 3000+ Tailwind 示例片段，带在线预览；找某个具体小组件的写法时来搜 ⚠ 质量参差，Pro 订阅付费 | Tailwind, HTML |  | 免费+付费 |

### 轻量 / 免 class

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [matcha.css](https://matcha.mizu.sh) | 免 class 的 CSS，覆盖面比同类更全（表单、菜单、代码块、对话框），可按模块裁剪；静态页或 Markdown 渲染页选它 | CSS | &lt;link rel="stylesheet" href="https://matcha.mizu.sh/matcha.css"&gt; | 开源 |
| [missing.css](https://missing.style) | htmx 团队（Big Sky Software）出的近乎免 class 的 CSS，另带少量工具类和 ARIA 驱动的组件；配 htmx 做超媒体应用时选 | CSS | &lt;link rel="stylesheet" href="https://unpkg.com/missing.css"&gt; | 开源 |
| [MVP.css](https://andybrewer.github.io/mvp/) | 免 class 的极简样式表，专为快速做 MVP 落地页设计；只写 HTML 就要一个能看的页面时选 | CSS | &lt;link rel="stylesheet" href="https://unpkg.com/mvp.css"&gt; | 开源 |
| [new.css](https://newcss.net) | 极小的免 class CSS，复古简洁的"早期互联网"观感；个人主页或纯文本站点选它 | CSS | `npm i @exampledev/new.css` | 开源 |
| [Oat](https://oat.ink) | 超轻量的语义化 HTML UI 库：很小的 CSS + JS、零依赖，直接给原生标签上样式并带少量组件；不要构建、不要框架时选 | CSS, JS | `npm install @knadh/oat` | 开源 |
| [Simple.css](https://simplecss.org) | 免 class 的 CSS：引一个文件，语义化 HTML 就自动好看并支持暗色；写文档页、原型、个人博客时选 | CSS | https://cdn.simplecss.org/simple.css（CDN 引入） | 开源 |
| [Water.css](https://watercss.kognise.dev) | 最知名的免 class 样式表之一，自动明暗主题；给 demo 页一行变好看 ⚠ 2022 年后未发新版（功能已稳定） | CSS | &lt;link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.min.css"&gt; | 开源 |
