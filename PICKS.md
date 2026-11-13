# ⭐ 精选速查（自动生成）

> 全库 2528 条里的 204 个同类首选，一页看完。没有特殊要求时直接从这里选；要更多候选，点分类标题进完整目录，或运行 `python3 scripts/find.py <关键词>`。
> 本文件由 `scripts/build.py` 生成，请勿手改。

## ui/

### [聚合站与目录（先从这里找）](ui/catalog/01-aggregators.md#ui-aggregators)

- [21st.dev](https://21st.dev) — 最大的社区组件目录：12000+ React/Tailwind 组件、库、模板；含 424 个 shadcn registry 的目录和 AI 生成 `npx @21st-dev/cli@latest init --client claude`
- [awesome-shadcn-ui](https://github.com/birobirobiro/awesome-shadcn-ui) — shadcn 生态主力 awesome 列表（20.8k★，每日更新）
- [registry.directory](https://registry.directory) — 公开 shadcn registry 浏览器，可预览代码、复制安装命令；对 Agent 极友好（items.json、/api/markdown、OpenAPI、llms.txt）
- [shadcn 官方 Registry Directory](https://ui.shadcn.com/docs/directory) — 官方社区 registry 清单（JSON 索引 548 个），CLI 和 MCP 原生支持 `npx shadcn@latest search @<ns>`

### [基础 / 无头组件库](ui/catalog/02-component-libraries.md#ui-core)

- [Base UI](https://base-ui.com) — MUI 团队的无头组件，shadcn 新底座选项之一
- [shadcn/ui](https://ui.shadcn.com) — 复制进项目的组件（代码归你），AI 生态事实标准；registry + MCP + Skill 齐全 `npx shadcn@latest init`

### [动画与稀有特效组件](ui/catalog/03-animated-components.md#ui-animated)

- [Aceternity UI](https://ui.aceternity.com) — 200+ 酷炫暗色 Hero/落地页特效（Spotlight、Beams、3D Card）+ 区块模板 `npx shadcn@latest add @aceternity/<item>`
- [Animate UI](https://animate-ui.com) — 给 Radix/Base UI/React Aria 加动画的原语：换个 import，shadcn 组件就会动 `npx shadcn@latest add @animate-ui/<item>`
- [Magic UI](https://magicui.design) — 150+ 落地页动画组件与特效（Marquee、Globe、Bento…） `npx shadcn@latest add @magicui/<item>`
- [React Bits](https://reactbits.dev) — 超大创意库：动画文字、背景、组件（1274 条目，51.6k★） `npx shadcn@latest add @react-bits/<Component>-TS-TW`

### [风格化主题（手绘 / 复古 / 像素 / 新粗野 / 玻璃）](ui/catalog/04-stylized-themes.md#ui-stylized)

- [Looseleaf](https://kevintngo.github.io/looseleaf/) — 「手绘版 shadcn/ui」：123 个可访问组件，纸张纹理 + 钢笔墨线 + 胶带贴纸印章；保留 shadcn 的 props 和 data-slot，直接替换不改 JSX `npx shadcn@latest add https://kevintngo.github.io/looseleaf/r/button.json`
- [Neobrutalism components](https://www.neobrutalism.dev) — 新粗野主义 shadcn 组件 `npx shadcn@latest add https://neobrutalism.dev/r/<item>.json`
- [Sketchbook UI](https://sarthakrawat-1.github.io/sketchbook-ui/) — 手绘笔记本风：20 个带抖动 SVG 边框和纸张纹理的组件，零运行时依赖，<70KB `npm i sketchbook-ui`

### [移动端 / React Native](ui/catalog/05-mobile.md#ui-mobile)

- [beUI](https://beui.dev) — 同时覆盖 Web 和 React Native 的动画组件（Motion/Tailwind/Reanimated），带 MCP 和 Skill `npx shadcn@latest add @beui/<item>`
- [expo-glass-effect](https://docs.expo.dev/versions/latest/sdk/glass-effect/) — Expo 官方液态玻璃视图（iOS 26 Liquid Glass 原生效果）。React Native 里要真·液态玻璃用它 `npx expo install expo-glass-effect`
- [ExpoKit](https://expokit.in) — Expo 复制粘贴组件库：73 组件（340+ 变体）、12 屏、44 图表、液态玻璃与 3D 效果；iOS/Android/Web/Expo Go `npx @expokit/cli@latest init`
- [React Native Reusables](https://reactnativereusables.com) — shadcn/ui 的标准 RN 移植（NativeWind / Uniwind） `npx @react-native-reusables/cli@latest init`

### [原生与跨端（Flutter / SwiftUI / Compose / 桌面）以及 RN 基础库](ui/catalog/05-mobile.md#ui-native)

- **React Native 基础库**：[React Native Reanimated](https://docs.swmansion.com/react-native-reanimated/) — React Native 动画的事实标准：动画跑在 UI 线程，支持布局动画和 CSS 式动画；几乎所有 RN 动效库的依赖，必装 `npm install react-native-reanimated`
- **Flutter**：[Forui](https://forui.dev) — 极简风的 Flutter UI 库，自带 CLI 可把样式源码生成进项目；不想要 Material 观感的 Flutter 应用首选
- **Compose / Android**：[Compose Multiplatform](https://kotlinlang.org/compose-multiplatform/) — JetBrains 的声明式 UI 框架，一套 Kotlin 代码覆盖 Android / iOS / 桌面 / Web；Kotlin 团队做跨端时首选

### [物理、液体、3D 与 Shader](ui/catalog/06-effects-3d-shaders.md#ui-effects)

- [goopUI](https://goop.timmcmasters.work/docs/components) — 「会滴落的组件」：带小型物理引擎的黏液版 shadcn 目录（滴落、拉伸、融合），subtle/playful/wild 预设。⚠ 仅 Vue 3/Nuxt，pre-alpha，未发布 npm
- [Paper Shaders](https://shaders.paper.design) — 零依赖高性能 canvas shader（网格渐变、颗粒…）

### [AI 产品 UI（聊天 / Agent / 可观测性）](ui/catalog/07-ai-product-ui.md#ui-ai-product)

- [affectUI](https://www.affectui.com) — 「给 AI 产品的 Agent-ready React UI」：173 个条目，Agent 可观测性做得很深（检查点、审批闸门、Agent 图、上下文窗口地图、成本与 trace 瀑布、权限页）；每个是零依赖单文件 .tsx `npx shadcn@latest add @affectui/<item>`
- [AI Elements（Vercel）](https://elements.ai-sdk.dev) — 基于 shadcn 的 AI 原生组件（消息、工具调用、推理过程…） `npx shadcn@latest add @ai-elements/<item>`
- [assistant-ui](https://www.assistant-ui.com) — AI 聊天 React 组件 + runtime：流式、工具、持久化；兼容 AI SDK/LangGraph/Mastra `npx assistant-ui@latest create`

### [动画引擎 / 滚动 / 3D 底层库](ui/catalog/08-animation-engines.md#ui-animation-engines)

- [GSAP](https://gsap.com) — 时间轴与滚动动画（ScrollTrigger）。2025-04-30 起完全免费（含 SplitText、MorphSVG） `npx skills add https://github.com/greensock/gsap-skills`
- [Lenis](https://lenis.dev) — 平滑滚动，高级感网站标配
- [Motion（原 Framer Motion）](https://motion.dev) — React/JS/Vue 动画首选。布局动画、手势、滚动 `npx motion-ai`
- [Three.js](https://threejs.org) — WebGL/WebGPU 3D `npx skills add cloudai-x/threejs-skills`

### [动效 / 特效词汇与可复制 Prompt](ui/catalog/09-design-vocabulary.md#ui-vocabulary)

- [animations.dev Vocabulary](https://animations.dev/vocabulary) — Emil Kowalski 动画课程公开的动效术语表，按入场退场、编排时序、缓动、手势、布局过渡等分组解释常见动画模式的叫法，明确写着「用这些名字向 AI 描述你要的效果」，不知道某个动效该怎么称呼时先查这页；免费
- [Emil Kowalski skills](https://github.com/emilkowalski/skills) — 含 animation-vocabulary（教 AI 用正确的动效术语）、animate、choreograph、apple-design、review-animations；作者是 Sonner/Vaul 作者 `npx skills add emilkowalski/skills`
- [motion-prompt](https://github.com/showheyohtaki/motion-prompt) — 192 个带专业名称的效果（8 包×24：动态图形、镜头运动与转场、UI 组件名、落地页/网页特效、摄影风格灯光），每个都有实时演示 + Copy Prompt；可按编号引用（#012）。画廊：showheyohtaki.github.io/motion-prompt `npx skills add showheyohtaki/motion-prompt`

### [设计风格 / 审美类 Skill 与 DESIGN.md](ui/catalog/09-design-vocabulary.md#ui-design-skills)

- [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) — Anthropic 官方「去 AI 味」前端审美 Skill，避免千篇一律的紫色渐变 + Inter 字体 `npx skills add anthropics/skills --skill frontend-design`
- [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — 从 Claude、Stripe、Linear、Vercel 等名站提取的 DESIGN.md，丢进项目根目录即可让 AI 照着这个风格做（126k★）
- [Impeccable](https://impeccable.style) — 「给编码 Agent 的设计词汇」：polish/bolder/critique/audit 等命令 + AI-slop 检测器（107k★） `npx impeccable install`
- [Taste Skill](https://github.com/Leonxlnx/taste-skill) — 艺术指导、参考图、浏览器自检，避免通用 AI 外观（112k★） `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`
- [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) — 可检索的设计数据库：80 种 UI 风格、192 种产品类型、192 套配色、74 组字体搭配 + UX 规则，自动生成设计系统（147k★） `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill → /plugin install ui-ux-pro-max@ui-ux-pro-max-skill`

### [官方 Prompt 指南（v0 / Lovable / Bolt / Stitch / Claude）](ui/catalog/09-design-vocabulary.md#ui-prompt-guides)

- [Claude Cookbook: Prompting for frontend aesthetics](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb) — 排版、主题、动效的 Prompt 模块，可直接拼进系统提示

### [镜头 / 摄影 / 灯光词汇（图像与视频生成）](ui/catalog/09-design-vocabulary.md#ui-camera-photo)

- [Google Veo 视频提示指南](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide) — 官方镜头运动、景别、镜头焦段、风格术语

### [灵感画廊（带 MCP 的优先）](ui/catalog/10-inspiration.md#ui-inspiration)

- [Codrops](https://tympanus.net/codrops/) — 创意前端的标杆站点，持续发布带完整源码的实验性效果（WebGL 转场、滚动动画、文字特效、图片悬停）和案例拆解，想做获奖网站级别的交互时先来这里找可改的 Demo；免费，Demo 代码可自由用于个人和商业项目
- [Dribbble](https://dribbble.com) — 最大的设计师作品社区，按关键词能搜到海量界面概念稿、图标和插画，找视觉风格与配色方向时用；浏览免费，⚠ 多为概念稿而非上线产品，交互合理性要自己判断，作品版权归作者
- [Mobbin](https://mobbin.com) — 60 万+ 真实 App/Web 截图、流程、页面区块 `claude mcp add --transport http mobbin https://api.mobbin.com/mcp`
- [Refero](https://refero.design) — 12.5 万+ Web/iOS 截图、8000+ 流程；配套 refero_skill 做「先调研再设计」 `claude mcp add --transport http refero https://api.refero.design/mcp`

### [图标、字体、配色、主题生成](ui/catalog/11-assets.md#ui-assets)

- [Fontshare](https://www.fontshare.com) — 免费高质量字体（Clash、General Sans、Satoshi…），比 Inter 更有个性
- [Iconify](https://iconify.design) — 200+ 图标集、20 万+ 图标；公开免 key API `claude mcp add iconify -- npx -y iconify-mcp-server@latest`
- [Lucide](https://lucide.dev) — shadcn 和多数 AI 工具的默认图标集
- [Realtime Colors](https://www.realtimecolors.com) — 在真实页面上预览配色和字体，导出 CSS/Tailwind
- [tweakcn](https://tweakcn.com) — shadcn/Tailwind 可视化主题编辑器，有预设和 AI 主题生成，导出后一行命令装入 `npx shadcn@latest add https://tweakcn.com/r/themes/<preset>.json`

### [插画、3D、图片视频、样机、背景生成器、音效](ui/catalog/11-assets.md#ui-media-assets)

- **插画**：[unDraw](https://undraw.co) — 可在线改主色的扁平风 SVG 插画库，空状态、引导页、落地页配图的默认选择；可商用免署名，⚠ 不得打包再分发、做同类站或用于机器学习训练
- **3D 素材**：[Poly Haven](https://polyhaven.com) — 高质量 HDRI 环境贴图、PBR 材质和 3D 模型库，做 three.js/R3F 场景打光和材质时首选；全部 CC0，可商用免署名，并有免 key 公开 API
- **背景与图案生成**：[Haikei](https://haikei.app) — 一站式 SVG 背景素材生成器：波浪、Blob、叠层波、渐变光斑、低多边形、分隔线等十几种，调参后导出 SVG/PNG，落地页需要装饰背景时首选；基础生成器免费、免注册，产物可商用
- **头像与占位**：[DiceBear](https://www.dicebear.com) — 开源头像生成库与免 key HTTP API，60 多种风格（像素、首字母、卡通人物、几何图形…），同一 seed 永远得到同一张 SVG，给用户列表和评论区生成默认头像的首选；代码 MIT，⚠ 各风格美术许可不同（CC0、CC BY 等），商用前看风格页

### [UI 相关 MCP 服务器](ui/catalog/12-mcp-registries-llms.md#ui-mcp)

- [21st MCP（原 Magic MCP）](https://21st.dev/mcp) — 搜索并获取 21st.dev 上万个组件；AI 生成需付费。旧 Magic API key 已重置 `npx @21st-dev/cli@latest init --client claude`
- [Context7](https://context7.com) — 几乎任何库的最新文档（Tailwind、Radix 这类没有 llms.txt/MCP 的库靠它兜底） `claude mcp add context7 -- npx -y @upstash/context7-mcp`
- [Figma MCP（官方）](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation) — 读取设计稿上下文、变量、截图、Code Connect，也能写回 Figma `claude mcp add --transport http figma https://mcp.figma.com/mcp`
- [Motion AI Kit](https://motion.dev/docs/ai-kit) — Motion 官方 /motion Skill + 文档 MCP（免费）；Motion+ 版加示例和性能诊断 `npx motion-ai`
- [shadcn MCP（官方）](https://ui.shadcn.com/docs/mcp) — 在任何已配置的 registry（含 @命名空间）里浏览、搜索、安装组件。装这一个就能接入几百个组件库 `npx shadcn@latest mcp init --client claude`

### [其他框架组件库（Vue / Svelte / Angular / Solid / Web Components）](ui/catalog/13-other-frameworks.md#ui-frameworks-other)

- **Vue / Nuxt**：[PrimeVue](https://primevue.org) — Vue 生态组件最全的套件之一（90+ 组件，Styled / Unstyled 双模式 + 主题预设），做后台、数据密集型应用时首选；官方提供 MCP `npm install primevue @primeuix/themes`
- **Svelte**：[Bits UI](https://bits-ui.com) — Svelte 5 无样式无障碍原语库，shadcn-svelte 的底座；自建 Svelte 设计系统时首选 `npm install bits-ui`
- **Angular**：[Angular Material + CDK](https://material.angular.dev) — Angular 官方 Material Design 组件库及底层 CDK，与框架同步发版；Angular 项目的默认选择

### [CSS 框架与纯 HTML / Tailwind 组件](ui/catalog/13-other-frameworks.md#ui-css-kits)

- **CSS 框架与引擎**：[Bootstrap](https://getbootstrap.com) — 最老牌的 CSS 组件框架，类名即组件、资料最多；服务端渲染模板或不想配构建工具时选 ⚠ 官网首页已展示 v6 alpha，生产用 5.3 `npm install bootstrap@5.3.8`

### [国内生态（Ant Design / Element / TDesign / 小程序 / AntV…）](ui/catalog/14-china-ecosystem.md#ui-china)

- **React 组件库**：[Ant Design](https://ant.design) — 蚂蚁出品的企业级 React 组件库（100k★，当前 v6），中后台项目默认首选；官方提供 llms.txt、CLI 和 MCP，国内镜像 ant-design.antgroup.com `npm install antd`
- **Vue 组件库**：[Element Plus](https://element-plus.org) — 国内使用最广的 Vue 3 桌面端组件库（饿了么 Element 的继任者），Vue 中后台项目默认首选，官方提供 llms.txt `npm install element-plus --save`
- **移动端 H5**：[Vant](https://vant-ui.github.io/vant/) — 有赞开源的 Vue 3 移动端组件库（24k★），国内 H5 电商 / 营销页事实标准，国内镜像 vant.pro `npm i vant`
- **小程序与跨端**：[Taro](https://taro-docs.jd.com/docs/) — 京东开源的多端统一开发框架（37k★），用 React / Vue 写一套代码编译到微信等各家小程序、H5、RN 和鸿蒙，React 团队做小程序首选；⚠ 文档域名 docs.taro.zone 证书异常，用 taro-docs.jd.com `npm install -g @tarojs/cli`
- **小程序与跨端**：[uni-app](https://uniapp.dcloud.net.cn) — DCloud 出品的 Vue 跨端框架（41k★），一套代码发 iOS / Android / 鸿蒙 / 各家小程序 / H5，国内 Vue 团队做小程序和 App 的最常见选择，官方提供 llms.txt `npx degit dcloudio/uni-preset-vue#vite-ts my-vue3-project`
- **图表与可视化**：[Apache ECharts](https://echarts.apache.org) — 百度发起、Apache 孵化毕业的图表库（67k★，当前 v6），图表类型最全、中文文档和示例最多，国内项目做图表默认首选 `npm install echarts --save`

### [大厂设计系统与官方实现](ui/catalog/15-design-systems.md#ui-design-systems)

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) — 苹果全平台（iOS / iPadOS / macOS / watchOS / visionOS）官方界面设计规范，做苹果生态应用或想让 Web 界面有 iOS 质感时必读
- [Carbon Design System](https://carbondesignsystem.com) — IBM 的开源设计系统，规范文档极完整、数据密集型企业界面范例多，React / Web Components 双实现，并提供 llms.txt 和官方 Carbon MCP `npm install @carbon/react`
- [Material Design 3](https://m3.material.io) — Google 的开源设计系统规范（动态配色、形状、动效、组件指南），做 Android 应用或需要一套完整可引用的设计 token 体系时的权威参考
- [React Aria](https://react-aria.adobe.com) — Adobe 的无样式 React 组件与 hooks，键盘、读屏、触屏交互和国际化处理业界标杆，自建设计系统需要最强无障碍底座时首选；提供 llms.txt、MCP 和 Agent Skills `claude mcp add react-aria npx @react-aria/mcp@latest`

### [功能型组件](ui/catalog/16-functional-components.md#ui-functional)

- **图表与可视化**：[Recharts](https://recharts.github.io) — React + D3 的声明式 SVG 图表库（v3），生态最大、shadcn Chart 的底层；React 项目做常规折线/柱状/饼图的默认选择 `npm install recharts react-is`
- **编辑器（富文本 / 代码 / Markdown）**：[Tiptap](https://tiptap.dev) — 基于 ProseMirror 的无头富文本编辑器框架（v3，扩展丰富，React/Vue 皆可）；做 Notion 式或评论框式编辑器的默认选择（⚠ 核心 MIT，协同、AI、评论等为付费云服务） `npm install @tiptap/react @tiptap/pm @tiptap/starter-kit`
- **日期与日历**：[React DayPicker](https://daypicker.dev) — 可访问、可定制的日期选择日历（v10 起包名为 @daypicker/react），shadcn Calendar 的底层；React 日期选择器的默认选择 `npm install @daypicker/react`
- **拖拽与排序**：[dnd kit](https://dndkit.com) — 现代的拖拽工具包（可访问、支持触摸与键盘、可排序/看板/网格），新版为框架无关核心 + @dnd-kit/react；React 拖拽排序的默认选择 `npm install @dnd-kit/react`
- **流程图 / 白板 / 节点编辑**：[React Flow（xyflow）](https://reactflow.dev) — 节点式流程图/工作流编辑器的事实标准（同仓库含 Svelte Flow），另有 shadcn 版 React Flow UI 组件；做工作流、Agent 编排、思维导图界面的默认选择（Pro 示例付费） `npm install @xyflow/react`
- **地图**：[MapLibre GL JS](https://maplibre.org) — 开源的 WebGL 矢量瓦片地图引擎（Mapbox GL v1 的社区分支，无需 token）；自托管或想避开 Mapbox 计费时的默认选择，瓦片可配 OpenFreeMap `npm install maplibre-gl`
- **轮播**：[Embla Carousel](https://www.embla-carousel.com) — 轻量无依赖的轮播引擎（拖拽手感好、插件化），shadcn Carousel 的底层；React 轮播的默认选择 `npm install embla-carousel-react --save`
- **弹层 / 通知 / 命令面板**：[Sonner](https://sonner.emilkowal.ski) — Emil Kowalski 的堆叠式 Toast 组件（动效细腻、Promise 状态、API 极简），shadcn 默认 Toast；React 通知提示的默认选择 `npm install sonner`
- **文件上传**：[react-dropzone](https://react-dropzone.js.org) — 拖拽选文件的无头 React hook（只管文件选择与校验，不管上传）；自己写上传逻辑时做拖拽区的默认选择 `npm install react-dropzone`
- **媒体（视频 / 音频 / PDF）**：[Video.js 10](https://videojs.org) — Video.js、Vidstack、Plyr、Media Chrome 四个团队合并后的新一代播放器（可组合控件、React/HTML 两套、HLS/DASH）；现在做网页视频播放器的默认选择 `npm install @videojs/react`
- **认证界面**：[Clerk Components](https://clerk.com/docs/reference/components/overview) — Clerk 的现成认证组件（SignIn、SignUp、UserButton、组织切换，另有 shadcn registry）；想最快得到完整登录注册与用户管理界面时选（⚠ 托管服务，超出免费用户数收费） `npm install @clerk/nextjs`
- **其他**：[Driver.js](https://driverjs.com) — 轻量零依赖的产品导览与元素高亮库（框架无关）；做新手引导、功能聚光灯的默认选择 `npm install driver.js`
- **其他**：[qrcode.react](https://github.com/zpao/qrcode.react) — 把字符串渲染成二维码的 React 组件（SVG/Canvas，可嵌 logo）；React 里生成二维码的默认选择 `npm install qrcode.react`
- **其他**：[react-resizable-panels](https://react-resizable-panels.vercel.app) — 可拖拽调整大小的分栏面板（可折叠、布局持久化、键盘可用），shadcn Resizable 的底层；做 IDE 式分栏布局的默认选择 `npm install react-resizable-panels`
- **其他**：[xterm.js](https://xtermjs.org) — 浏览器里的终端模拟器（VS Code 终端同款，WebGL 渲染、插件体系）；做 Web 终端、云 IDE、SSH 面板的默认选择 `npm install --save @xterm/xterm`

### [模板、区块、UI Kit](ui/catalog/17-templates-blocks.md#ui-templates)

- **Tailwind / shadcn 模板与区块**：[Tailwind Plus（原 Tailwind UI）](https://tailwindcss.com/plus) — Tailwind 官方的付费模板与 UI 区块合集（500+ 区块、十余套 Next.js 站点模板、Catalyst 应用 UI Kit）；想要官方品质的现成页面时买它（⚠ 一次性买断，代码不可再分发，完整内容需登录）
- **仪表盘模板**：[shadcn-admin](https://github.com/satnaing/shadcn-admin) — 最受欢迎的开源 shadcn 后台模板（Vite + TanStack Router，10+ 页面、命令面板、RTL、明暗主题）；做管理后台的默认起点 `git clone https://github.com/satnaing/shadcn-admin.git`
- **落地页与营销模板**：[Launch UI](https://www.launchuicomponents.com) — 开源的 shadcn 落地页组件与模板（Hero、特性、定价、插画，多套配色）；SaaS 产品做深色质感落地页的首选起点（基础版免费开源，Pro 一次买断） `npx shadcn@latest add @launchui/<item>`
- **Figma UI Kit**：[Untitled UI Figma](https://www.untitledui.com/figma) — 规模最大的 Figma UI Kit 与设计系统之一（上万组件变体，与 Untitled UI React 对应）；从零搭设计系统或要设计与代码一一对应时选（免费精简版 + 付费完整版）

## skills/

### [Skill 目录站与 Awesome 列表](skills/catalog.md#skills-directories)

- [skills.sh](https://skills.sh) — Agent Skills 事实标准目录与排行榜；搜索 API：skills.sh/api/search?q=关键词 `npx skills add <owner/repo>`

### [全球累计安装量 Top（skills.sh All Time，2026-11-09 实时数据）](skills/catalog.md#skills-top)

- [find-skills](https://github.com/vercel-labs/skills) — #1（约 430 万次安装）让 AI 自己去找需要的 Skill。建议第一个装 `npx skills add vercel-labs/skills --skill find-skills`
- [grill-me](https://github.com/mattpocock/skills) — #2（约 150 万）不停追问，把需求彻底问清楚 `npx skills add mattpocock/skills --skill grill-me`
- [agent-browser](https://github.com/vercel-labs/agent-browser) — #5（约 140 万）让 AI 自己打开、点击、操作网页 `npx skills add vercel-labs/agent-browser`
- [setup-matt-pocock-skills](https://github.com/mattpocock/skills) — #13（约 110 万）一键配好 Matt Pocock 整套 Skills 工作流（grill/tdd/handoff/triage/prototype…）。装完后在 Agent 里运行 /setup-matt-pocock-skills `npx skills add mattpocock/skills --skill setup-matt-pocock-skills`

### [工程 / 工作流类 Skill](skills/catalog.md#skills-engineering)

- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — Addy Osmani 的工程实践 Skill 集（code-review-and-quality 约 8.4 万安装），覆盖规格、评审、安全加固和性能，想要资深工程师流程时用 `npx skills add addyosmani/agent-skills`
- [Supabase agent-skills（官方）](https://github.com/supabase/agent-skills) — Supabase 官方 Skill（supabase-postgres-best-practices 约 48 万安装），写 Postgres 表结构、RLS 和查询优化时用 `npx skills add supabase/agent-skills`
- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) — react-best-practices、web-design-guidelines、composition-patterns、react-view-transitions `npx skills add vercel-labs/agent-skills`

### [其他领域 Skill（写作 / 调研 / 数据 / 文档 / 运维 / 安全 / 产品）](skills/catalog.md#skills-more)

- **官方厂商 Skill**：[飞书 / Lark CLI skills（官方）](https://github.com/larksuite/cli) — 飞书官方 CLI 自带的 Skill 集（lark-doc 约 49 万安装），让 Agent 操作文档、多维表格、消息、日历和审批时用（⚠ 需飞书应用授权） `npx skills add larksuite/cli`
- **写作与内容**：[baoyu-skills（宝玉）](https://github.com/JimLiu/baoyu-skills) — 宝玉的内容创作 Skill 集（baoyu-post-to-wechat 约 3.5 万安装），做公众号排版发布、小红书配图、翻译和发 X 时用 `npx skills add jimliu/baoyu-skills`
- **产品与增长**：[marketingskills（Corey Haines）](https://github.com/coreyhaines31/marketingskills) — 最流行的营销 Skill 集（seo-audit 约 25 万安装），做 SEO 审计、文案、定价、转化优化和内容策略时用 `npx skills add coreyhaines31/marketingskills`
- **插件市场**：[claude-plugins-official](https://github.com/anthropics/claude-plugins-official) — Anthropic 官方的 Claude Code 插件市场（默认已内置），找厂商认证的插件（Stripe、Sentry、Exa 等）时首选 `/plugin install {plugin-name}@claude-plugins-official`

### [规则 / Prompt / 子 Agent / 规格驱动工作流](skills/02-rules-prompts.md#rules-prompts)

- **规则与 AGENTS.md / CLAUDE.md**：[cursor.directory](https://cursor.directory) — 最大的 Cursor 规则社区站，按框架和语言找现成 rules 直接复制进项目时用
- **子 Agent、命令与工作流框架**：[Superpowers（obra）](https://github.com/obra/superpowers) — Star 最多的 Agent 技能与工作流框架（头脑风暴→计划→TDD→评审），想让 Agent 按严格工程流程干活时用 `/plugin install superpowers@claude-plugins-official`
- **规格驱动开发**：[GitHub Spec Kit](https://github.com/github/spec-kit) — GitHub 官方的规格驱动开发工具包（constitution→specify→plan→tasks→implement），新功能想先写规格再让 Agent 实现时用 `uv tool install specify-cli`
- **官方 Prompt 指南**：[Claude Prompt 工程指南（官方）](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) — Anthropic 官方 Prompt 工程文档（清晰指令、示例、XML 标签、思考、长上下文），给 Claude 写提示词前读
- **中文 Prompt 资源**：[LangGPT](https://github.com/langgptai/LangGPT) — 国内最知名的结构化提示词方法论（Role / Rules / Workflow 模板），想用模板化方式写中文提示词时用

## tools/

### [数据采集 / 爬虫](tools/catalog.md#tools-crawl)

- [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) — 小红书/抖音/快手/B站/微博/贴吧/知乎 的帖子、视频、评论（含二级评论）采集；Playwright 复用登录态免逆向；存 CSV/JSON/Excel/SQLite/MySQL；带 WebUI（约 70k★）。⚠ 仅供学习，禁止商用 `git clone https://github.com/NanmiCoder/MediaCrawler && cd MediaCrawler && uv sync`

### [MCP 目录站](tools/02-mcp.md#mcp-directories)

- [Claude Connectors 目录](https://claude.com/connectors) — Anthropic 官方审核的 Claude 连接器（远程 MCP）目录，给 Claude / Claude Code 找官方认可的集成时用
- [Docker MCP Catalog](https://hub.docker.com/mcp) — Docker 官方审核、容器化运行的 MCP 服务器目录，想隔离运行第三方服务器时用（⚠ 需 Docker Desktop）
- [PulseMCP](https://www.pulsemcp.com/servers) — 每日更新的 MCP 服务器与客户端目录，附下载量估算和周报，追踪生态动态时用
- [官方 MCP Registry](https://registry.modelcontextprotocol.io) — MCP 官方维护的服务器注册表（带 API），想确认某个 MCP 服务器是否由厂商正式发布时先查这里

### [常用 MCP 服务器](tools/02-mcp.md#mcp-servers)

- **开发与代码托管**：[GitHub MCP（官方）](https://github.com/github/github-mcp-server) — GitHub 官方 MCP，让 Agent 读写仓库、Issue、PR 和 Actions 时用（⚠ 需 PAT 或 OAuth） `claude mcp add-json github '{"type":"http","url":"https://api.githubcopilot.com/mcp","headers":{"Authorization":"Bearer YOUR_GITHUB_PAT"}}'`
- **开发与代码托管**：[Serena](https://github.com/oraios/serena) — 基于语言服务器的语义检索与符号级编辑 MCP，在大型代码库里省 token 地精确改代码时用 `uv tool install -p 3.13 serena-agent`
- **数据库与后端服务**：[Supabase MCP（官方）](https://github.com/supabase/mcp) — Supabase 官方远程 MCP，让 Agent 建表、跑迁移、查日志和生成类型时用（⚠ 生产库建议加 read_only） `claude mcp add --scope project --transport http supabase "https://mcp.supabase.com/mcp"`
- **搜索与网页抓取**：[Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server) — Firecrawl 官方 MCP，把网页抓成干净 Markdown、整站爬取和结构化提取时用（⚠ 需 API key）
- **国内服务**：[高德地图 MCP（官方）](https://lbs.amap.com/api/mcp-server/summary) — 高德开放平台官方 MCP，做地理编码、路径规划、周边搜索和天气查询时用（⚠ 需申请高德 key） `npx -y @amap/amap-maps-mcp-server`

### [AI 编码 Agent、IDE 与应用生成器](tools/03-ai-builders.md#tools-ai-builders)

- **终端编码 Agent**：[Claude Code](https://claude.com/product/claude-code) — Anthropic 官方的终端编码 Agent（也有 IDE、桌面和网页版），支持子 Agent、Hook、Skill、MCP 和插件，做复杂多文件工程任务时首选（⚠ 需 Claude 订阅或 API） `curl -fsSL https://claude.ai/install.sh | bash`
- **终端编码 Agent**：[Codex CLI](https://github.com/openai/codex) — OpenAI 开源的终端编码 Agent（Rust 实现，带沙箱），已有 ChatGPT 订阅或想用 GPT-5 系列写代码时用 `npm install -g @openai/codex`
- **AI IDE 与编辑器插件**：[Cursor](https://cursor.com) — 最流行的 AI 原生 IDE（VS Code 分支），带 Tab 补全、Agent 和云端 Agent，日常主力 AI 编辑器首选（⚠ 高阶模型需订阅）
- **应用 / 网站生成器**：[v0（Vercel）](https://v0.app) — Vercel 的 AI 应用生成器，产出 Next.js + shadcn/ui 代码并一键部署，做 React 界面和全栈原型首选
- **国内工具**：[Trae（字节跳动）](https://www.trae.ai) — 字节出品的 AI IDE（国内版 trae.cn），提供 Builder / SOLO 模式和免费模型额度，国内网络环境下想要 Cursor 式体验时用

## scaffolds/

### [全栈 Web Starter](scaffolds/01-starters.md#scaffold-web)

- [create-next-app](https://nextjs.org/docs/app/getting-started/installation) — 官方 Next.js 脚手架（v16），React 全栈默认选择 `npx create-next-app@latest`
- [create-vite](https://vite.dev/guide/) — 轻量 SPA/库脚手架（React/Vue/Svelte/Solid…），不需要 SSR 时选 `npm create vite@latest`
- [next-forge（Vercel）](https://www.next-forge.com) — 生产级 Turborepo SaaS 单仓：认证、支付、数据库、邮件、可观测性。认真做多应用 SaaS 时选 `npx next-forge@latest init`
- [Open SaaS](https://opensaas.sh) — 免费全功能 SaaS 模板：Stripe/Polar/Lemon Squeezy 支付、后台、文档、AI demo `npm i -g @wasp.sh/wasp-cli && wasp new -t saas`
- [shadcn/ui init + Blocks](https://ui.shadcn.com/blocks) — 初始化项目时直接带上 shadcn（next/vite/start/react-router/astro）；/create 是可视化构建器；Blocks 是可复制的整页区块 `npx shadcn@latest init -t next`

### [移动端 / 桌面端 Starter](scaffolds/01-starters.md#scaffold-mobile)

- [create-expo-app](https://docs.expo.dev/more/create-expo/) — 官方 React Native + Expo（Expo Router），RN 默认选择 `npx create-expo-app@latest`
- [create-tauri-app](https://v2.tauri.app/start/create-project/) — Tauri 2：Rust 后端的轻量桌面/移动应用，前端任意 `npm create tauri-app@latest`

### [后端 / API Starter](scaffolds/01-starters.md#scaffold-backend)

- [Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template) — FastAPI + SQLModel + Postgres + React/Vite + Docker Compose + JWT，Python 全栈 `git clone https://github.com/fastapi/full-stack-fastapi-template`
- [Hono](https://hono.dev/docs/getting-started/basic) — 超轻量 Web 标准 API 框架（Cloudflare Workers/Bun/Deno/Node/Vercel） `npm create hono@latest`

### [AI 应用 Starter 与 Agent 框架](scaffolds/02-ai-agents.md#scaffold-ai)

- [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) — 驱动 Claude Code 的 Agent 循环：工具、子 Agent、hooks、MCP `npm i @anthropic-ai/claude-agent-sdk / pip install claude-agent-sdk`
- [Dify](https://github.com/langgenius/dify) — 可自托管的可视化 LLM 应用 / Agent 工作流 / RAG 构建平台（161k★） `git clone https://github.com/langgenius/dify && cd dify/docker && cp .env.example .env`
- [LangGraph](https://langchain-ai.github.io/langgraph/) — 持久化、有状态的图式 Agent，支持人在环中。Python 多 Agent / 复杂控制流首选 `pip install -U langgraph`
- [Mastra](https://mastra.ai/docs) — TS Agent 框架：Agent、workflow、RAG、记忆、评测、本地 playground `npm create mastra@latest`
- [n8n](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm) — 工作流自动化，内置 AI Agent 节点（210k★） `npx n8n`
- [OpenAI Customer Service Agents Demo](https://github.com/openai/openai-cs-agents-demo) — 多 Agent 客服系统完整示例：Python（Agents SDK）后端做分流与 handoff，Next.js 前端实时显示每步 Agent、工具调用和 guardrail。做客服/分流类多 Agent 直接照它改 `git clone https://github.com/openai/openai-cs-agents-demo`
- [Pydantic AI](https://pydantic.dev/docs/ai/overview/) — Pydantic 团队出品的类型安全 Python Agent 框架。Python 单 Agent / 结构化输出首选 `pip install pydantic-ai`
- [Vercel AI SDK](https://ai-sdk.dev) — TS 工具包：流式输出、工具调用、Agent、生成式 UI，跨模型厂商（v7） `npm i ai`
- [Vercel Chatbot](https://github.com/vercel/chatbot) — 完整 Next.js 聊天应用：AI SDK + AI Gateway + Neon + Blob + 认证（原 ai-chatbot） `git clone https://github.com/vercel/chatbot`

### [MCP Server 开发模板](scaffolds/02-ai-agents.md#scaffold-mcp)

- [FastMCP](https://gofastmcp.com) — 最快的 Python MCP 服务端/客户端写法（v4，已迁到 PrefectHQ） `pip install fastmcp`
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) — 官方 MCP SDK（v2）：服务端装 server 包，客户端装 client 包。旧的 @modelcontextprotocol/sdk 是 v1，只做维护 `npm install @modelcontextprotocol/server`

### [架构 / 系统设计参考](scaffolds/03-architecture.md#scaffold-arch)

- [Martin Fowler 架构指南](https://martinfowler.com/architecture/) — 微服务、模式、重构的权威文章
- [Mermaid](https://mermaid.js.org) — 用文本画流程图、时序图、架构图；GitHub README 原生渲染，AI 最容易生成
- [patterns.dev](https://www.patterns.dev) — 现代 JS/React 设计模式、渲染模式、性能模式
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — 大规模系统设计经典指南（377k★）

### [服务与基础设施（认证 / 数据库 / 支付 / 邮件 / 部署…）](scaffolds/05-services.md#stack-services)

- **认证**：[Better Auth](https://better-auth.com) — TypeScript 开源认证框架，用户数据存自己的数据库，插件覆盖 2FA、组织、passkey、SSO；想免费自托管、不被厂商锁定时首选 `npm i better-auth`
- **数据库与 ORM**：[Drizzle ORM](https://orm.drizzle.team) — 轻量、无运行时代码生成的 TypeScript ORM，写法贴近 SQL，在 Serverless/Edge 上冷启动快；新 TS 项目的默认 ORM，配 drizzle-kit 做迁移 `npm i drizzle-orm`
- **数据库与 ORM**：[Supabase](https://supabase.com) — 开源 Firebase 替代品：托管 Postgres + 认证 + 存储 + 实时 + Edge Functions + 向量检索，一个平台包完后端；想用 SQL 且让 Agent 通过 MCP 直接管库时首选，⚠ 国内直连不稳定 `npm i @supabase/supabase-js`
- **支付与订阅**：[Stripe](https://stripe.com) — 支付基础设施的事实标准：Checkout、订阅、按量计费、发票、Connect 分账，文档和 Agent 工具最全；主体在海外或香港的项目默认选，⚠ 不支持中国大陆主体开户，税务需自己处理或另开 Stripe Tax `npm i stripe`
- **邮件与通知**：[Resend](https://resend.com) — 开发者优先的事务邮件 API，与 React Email 同团队，支持收信、广播和 webhook；新项目发验证码、通知邮件的默认选择 `npm i resend`
- **文件存储与媒体**：[Cloudflare R2](https://developers.cloudflare.com/r2/) — 兼容 S3 API 的对象存储，出口流量免费；存用户上传、图片、视频、AI 生成文件的默认选择，⚠ 国内访问需绑自定义域名且速度一般
- **部署与托管**：[Vercel](https://vercel.com) — Next.js 母公司的前端云：Git 推送即部署、预览环境、Fluid Compute、AI Gateway 等一体化；Next.js/React 项目的默认部署平台，⚠ 国内访问需绑自定义域名且仍不稳定 `npm i -g vercel`
- **后台任务与队列**：[Inngest](https://www.inngest.com) — 事件驱动的持久化工作流平台：把函数拆成可重试的步骤，自带并发、限流、定时和 Agent 编排，无需自建队列；Serverless 应用里跑后台任务和 AI 工作流的默认选择 `npm i inngest`
- **实时与协作**：[Liveblocks](https://liveblocks.io) — 协作功能的托管平台：在线状态、多人光标、评论、通知、协同文本编辑和 AI Copilot 组件；要给产品加 Figma/Notion 式多人协作时首选 `npm i @liveblocks/client @liveblocks/react`
- **搜索**：[Meilisearch](https://www.meilisearch.com) — Rust 写的开源搜索引擎，开箱即有容错、分面和混合（关键词+向量）搜索，中文分词可用；站内搜索想自托管且几分钟跑起来时首选 `npm i meilisearch`
- **分析 / 监控 / 特性开关**：[PostHog](https://posthog.com) — 开源的一体化产品平台：事件分析、会话回放、特性开关、A/B 实验、错误追踪、问卷和 LLM 可观测性，免费额度大；想用一个 SDK 覆盖产品数据全链路时首选 `npx -y @posthog/wizard@latest`
- **分析 / 监控 / 特性开关**：[Sentry](https://sentry.io) — 错误监控与性能追踪的事实标准，带会话回放、日志和 AI 根因分析（Seer），各语言 SDK 齐全；任何要上线的项目都该接一个，默认选它 `npx @sentry/wizard@latest -i nextjs`
- **国际化**：[next-intl](https://next-intl.dev) — Next.js App Router 的国际化库：ICU 消息、类型安全的 key、本地化路由，原生支持服务端组件；Next.js 项目的默认 i18n 方案 `npm i next-intl`
- **安全与限流**：[Upstash Ratelimit](https://upstash.com/docs/redis/sdks/ratelimit-ts/overview) — 基于 Upstash Redis 的无连接限流库（固定窗口、滑动窗口、令牌桶），可在 Edge/Serverless 运行；给 API 路由和 AI 接口加限流的默认做法 `npm i @upstash/ratelimit`
- **国内可用替代**：[腾讯云开发 CloudBase](https://tcb.cloud.tencent.com) — 腾讯云的一体化 Serverless 后端：云函数、云数据库（文档型 + MySQL）、云存储、静态托管、身份认证，原生支持微信小程序；做小程序或面向国内用户的全栈应用时首选，官方提供 MCP 让 Agent 直接部署 `npm i @cloudbase/js-sdk`

### [文档站 / 博客 / CMS](scaffolds/05-services.md#stack-content)

- **文档站**：[Fumadocs](https://fumadocs.dev) — 基于 Next.js App Router 的文档框架，UI 精致、内置搜索、OpenAPI 页面和 llms.txt 生成，也支持 TanStack Start/React Router；文档要和 Next.js 应用放同一仓库并深度定制时首选 `npm create fumadocs-app`
- **API 文档**：[Scalar](https://scalar.com) — 开源的 OpenAPI 文档与 API 客户端，界面现代、可直接发请求，Hono/FastAPI/NestJS/.NET 等都有官方集成；给后端自动生成交互式 API 文档时首选 `npm i @scalar/api-reference`
- **内容层与 MDX**：[Content Collections](https://www.content-collections.dev) — 把 Markdown/MDX 等本地内容转成带校验的类型安全数据集合，适配 Next.js、Vite、Remix 等；Contentlayer 停更后的首选替代 `npm i @content-collections/core @content-collections/next -D`
- **Headless CMS**：[Sanity](https://www.sanity.io) — 结构化内容平台：schema 即代码、可定制的 Studio、实时协作、GROQ 查询和可视化编辑；内容模型复杂、需要编辑体验和开发灵活性兼得时首选 `npm create sanity@latest`

### [AI 基础设施（模型网关 / 向量库 / 评测 / 沙箱 / 语音 / 生成 API）](scaffolds/06-ai-infra.md#stack-ai)

- **模型网关与路由**：[OpenRouter](https://openrouter.ai) — 一个 API Key 调用数百个模型的聚合网关，OpenAI 兼容接口、自动故障转移、按量透传计费；想快速对比和切换各家模型时首选，⚠ 国内访问受限，需国际信用卡或加密货币充值 `npm i @openrouter/ai-sdk-provider`
- **官方 SDK**：[Anthropic SDK（Claude API）](https://platform.claude.com/docs) — Claude 官方 TypeScript/Python SDK：Messages API、工具调用、提示词缓存、扩展思考、批处理和文件；直接调用 Claude 模型时用，⚠ 国内无法直接访问 `npm install @anthropic-ai/sdk`
- **本地模型**：[Ollama](https://ollama.com) — 最易用的本地模型运行器：一条命令拉取并运行开源模型，提供 OpenAI 兼容接口；本地开发、离线或隐私场景跑 LLM 的默认选择 `curl -fsSL https://ollama.com/install.sh | sh`
- **向量库与检索**：[pgvector](https://github.com/pgvector/pgvector) — Postgres 的向量相似度检索扩展（HNSW/IVFFlat），Supabase、Neon 等均内置；已经在用 Postgres 时的默认向量方案，不必再加一个数据库 `npm i pgvector`
- **文档解析与抓取**：[Docling](https://docling-project.github.io/docling/) — IBM 开源（现属 LF AI）的文档解析库，把 PDF、DOCX、PPTX、图片等转成保留版面、表格和阅读顺序的 Markdown/JSON，可完全本地运行；RAG 入库前解析文档的开源首选 `pip install docling`
- **文档解析与抓取**：[Firecrawl](https://www.firecrawl.dev) — 把任意网站抓取、爬取、搜索并转成干净 Markdown 或结构化数据的 API，处理 JS 渲染和反爬，核心开源；给 LLM 喂网页内容时首选 `npm i @mendable/firecrawl-js`
- **记忆**：[Mem0](https://mem0.ai) — 给 AI 应用加长期记忆的开源层：自动从对话中抽取、更新和检索用户事实，有托管平台和自托管版；想让助手跨会话记住用户偏好时首选 `pip install mem0ai`
- **评测与可观测性**：[promptfoo](https://www.promptfoo.dev) — 开源的提示词与模型评测 CLI：用 YAML 声明测试用例和断言，横向对比多模型并支持红队安全测试；想把提示词改动纳入 CI 回归测试时首选 `npx promptfoo@latest init`
- **结构化输出与护栏**：[Instructor](https://python.useinstructor.com) — 最流行的结构化输出库：用 Pydantic 模型定义期望结果，自动校验并重试，支持十多家模型；Python 里从 LLM 拿可靠 JSON 的默认做法 `pip install instructor`
- **Agent 沙箱与浏览器**：[E2B](https://e2b.dev) — 给 AI Agent 用的云端安全沙箱（Firecracker 微虚拟机），毫秒级启动，可运行代码、终端和桌面环境，SDK 开源；要执行模型生成的代码时首选 `npm i e2b`
- **语音**：[LiveKit Agents](https://docs.livekit.io/agents/) — 开源的实时语音/视频 Agent 框架，基于 WebRTC，把语音识别、LLM、语音合成和打断处理串成低延迟管线，可接电话；做生产级实时语音助手时首选 `pip install livekit-agents`
- **图像 / 视频 / 音乐生成**：[fal](https://fal.ai) — 生成式媒体推理平台，一个 API 调用数百个图像、视频、语音、3D 模型（FLUX、Kling、Veo、Seedance 等），速度快、按量计费；应用里要接图像或视频生成时首选 `npm install --save @fal-ai/client`
- **推理与微调平台**：[Hugging Face](https://huggingface.co) — 开源模型、数据集和 Demo 的中心仓库，Inference Providers 用一个接口路由到多家推理服务，官方提供 MCP；找模型、下权重、托管 Demo 都从这里开始，⚠ 国内需镜像（hf-mirror.com） `pip install -U huggingface_hub`
- **国内模型平台**：[DeepSeek 开放平台](https://platform.deepseek.com) — DeepSeek 官方 API，OpenAI 与 Anthropic 接口双兼容，价格低且有缓存命中折扣；国内项目的默认大模型接口，把 base_url 换成 https://api.deepseek.com 即可

### [常用库（状态 / 请求 / 校验 / 测试 / 工具链 / Python）](scaffolds/07-common-libs.md#stack-libs)

- **状态管理**：[Zustand](https://zustand.docs.pmnd.rs) — 极简的 React 全局状态库，一个 hook 即一个 store，无 Provider、无样板代码；客户端状态的默认选择 `npm i zustand`
- **数据请求与 API 层**：[TanStack Query](https://tanstack.com/query/latest) — 异步服务端状态管理库：缓存、去重、后台刷新、乐观更新、无限滚动；React（及 Vue/Svelte/Solid）里请求数据的默认选择 `npm i @tanstack/react-query`
- **校验与类型**：[React Hook Form](https://react-hook-form.com) — 基于非受控组件的高性能表单库，配 @hookform/resolvers 接 Zod 等校验，shadcn/ui 表单默认搭配；React 表单的默认选择 `npm install react-hook-form @hookform/resolvers`
- **校验与类型**：[Zod](https://zod.dev) — TypeScript 优先的 schema 校验库，从 schema 推导静态类型，AI SDK、tRPC、表单库等几乎都以它为通用语言；校验的默认选择，对包体敏感可用 zod/mini `npm i zod`
- **路由**：[TanStack Router](https://tanstack.com/router/latest) — 完全类型安全的 React 路由，路径参数、search params 和 loader 都有类型推导，支持文件路由与内置缓存；Vite 单页应用的默认路由 `npm i @tanstack/react-router`
- **日期与工具函数**：[date-fns](https://date-fns.org) — 函数式、可 tree-shake 的日期工具库，操作原生 Date，带时区支持和大量本地化；处理日期的默认选择 `npm i date-fns`
- **日期与工具函数**：[es-toolkit](https://es-toolkit.dev) — 现代的 Lodash 替代品，体积更小、速度更快、类型完善，并提供 es-toolkit/compat 平滑迁移；通用工具函数的默认选择 `npm i es-toolkit`
- **样式工具**：[Class Variance Authority（cva）](https://cva.style/docs) — 用声明式配置定义组件样式变体（variant、size 等）并得到类型安全的 props，shadcn/ui 组件的变体方案；给组件写多种外观时的默认选择 `npm i class-variance-authority`
- **测试**：[Playwright](https://playwright.dev) — 微软的端到端测试框架，一套 API 驱动 Chromium/Firefox/WebKit，自动等待、Trace 回放、并行和代码生成；E2E 测试的默认选择，也是多数浏览器 Agent 的底座 `npm init playwright@latest`
- **测试**：[Vitest](https://vitest.dev) — 基于 Vite 的测试框架，Jest 兼容 API、原生 ESM/TypeScript、极快的监听模式，并支持真实浏览器模式；JS/TS 单元与组件测试的默认选择 `npm install -D vitest`
- **构建与工具链**：[Biome](https://biomejs.dev) — Rust 写的一体化格式化器 + Linter，一个配置文件替代 ESLint 和 Prettier，速度快一个数量级；新项目想要最省心、最快的代码规范工具时首选 `npm i -D -E @biomejs/biome`
- **构建与工具链**：[pnpm](https://pnpm.io) — 基于内容寻址存储和硬链接的包管理器，安装快、省磁盘、依赖严格，原生支持 workspace 与 catalog；Node 项目和 monorepo 的默认包管理器 `npm install -g pnpm@latest`
- **环境与配置**：[T3 Env](https://env.t3.gg) — 用 Zod 等 schema 在构建期和运行时校验环境变量，并区分服务端与客户端变量防止泄露；Next.js/Nuxt 等全栈项目管理 env 的默认做法 `npm install @t3-oss/env-nextjs zod`
- **命令行工具**：[Commander.js](https://github.com/tj/commander.js) — Node.js 最普及的命令行参数解析库，子命令、选项和帮助信息齐全；写 Node CLI 的默认选择 `npm i commander`
- **Python 基础**：[Pydantic](https://docs.pydantic.dev) — 基于类型注解的数据校验与序列化库（Rust 内核），FastAPI、各家 LLM SDK 和结构化输出的共同基础；Python 里定义数据模型的默认选择 `pip install pydantic`
- **Python 基础**：[pytest](https://docs.pytest.org) — Python 测试的事实标准：普通 assert、fixture 依赖注入、参数化和庞大的插件生态；Python 测试的默认选择 `pip install pytest`
- **Python 基础**：[Ruff](https://docs.astral.sh/ruff/) — Rust 写的 Python Linter + 格式化器，一个工具替代 Flake8、isort、Black 等，速度极快；Python 代码规范的默认选择 `uv add --dev ruff`
- **Python 基础**：[uv](https://docs.astral.sh/uv/) — Astral 用 Rust 写的 Python 包与项目管理器，一个工具替代 pip、venv、pipx、pyenv 和 poetry，速度快 10–100 倍；Python 项目的默认工具链入口，uvx 可直接运行 MCP 等命令行工具 `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Python 数据与界面**：[Polars](https://pola.rs) — Rust 写的多线程 DataFrame 库，惰性执行与查询优化，处理大数据比 pandas 快且省内存；新写的数据处理代码默认选它 `pip install polars`
- **Python 数据与界面**：[Streamlit](https://streamlit.io) — 用纯 Python 脚本几分钟做出数据应用和 AI Demo 的框架，脚本自上而下重跑；内部工具、数据看板和模型演示的最快路径 `pip install streamlit`

### [Awesome 元列表 / Prompt 合集](scaffolds/04-awesome-lists.md#meta-lists)

- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — Claude Code 命令、hooks、工作流、CLAUDE.md 示例
- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — 100+ 可运行的 Agent / RAG 应用示例，直接 fork
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — 最大的 MCP 服务器目录
- [prompts.chat（原 awesome-chatgpt-prompts）](https://prompts.chat) — 最大的开源 Prompt 库
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) — 所有 awesome 列表的根索引
