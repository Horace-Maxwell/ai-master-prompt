# 效果词汇表与 Prompt 库（教你怎么跟 AI 描述）

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-vocabulary"></a>

## 动效 / 特效词汇与可复制 Prompt

不知道一个效果叫什么？在这些画廊里点开演示，复制它的专业名称和 Prompt。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [animations.dev Vocabulary](https://animations.dev/vocabulary) | Emil Kowalski 动画课程公开的动效术语表，按入场退场、编排时序、缓动、手势、布局过渡等分组解释常见动画模式的叫法，明确写着「用这些名字向 AI 描述你要的效果」，不知道某个动效该怎么称呼时先查这页；免费 |  |  | 免费 |
| ⭐ [Emil Kowalski skills](https://github.com/emilkowalski/skills) | 含 animation-vocabulary（教 AI 用正确的动效术语）、animate、choreograph、apple-design、review-animations；作者是 Sonner/Vaul 作者 |  | `npx skills add emilkowalski/skills` | 免费 |
| ⭐ [motion-prompt](https://github.com/showheyohtaki/motion-prompt) | 192 个带专业名称的效果（8 包×24：动态图形、镜头运动与转场、UI 组件名、落地页/网页特效、摄影风格灯光），每个都有实时演示 + Copy Prompt；可按编号引用（#012）。画廊：showheyohtaki.github.io/motion-prompt |  | `npx skills add showheyohtaki/motion-prompt` | 免费 |
| [Aesthetics Wiki](https://aesthetics.fandom.com/wiki/Aesthetics_Wiki) | 社区维护的美学风格百科，收录上千种风格词条（Vaporwave、Cottagecore、Dark Academia、赛博朋克等）及其视觉元素、配色和相关风格，给 Agent 写风格关键词或做情绪板时用来查名字；免费，⚠ 社区内容质量参差 |  |  | 免费 |
| [aimotions.art](https://aimotions.art) | 195 种命名文字动画风格（故障、材质 3D、光效 shader…），可复制 Prompt |  | copy prompt | 免费 |
| [Animate.css](https://animate.style) | CSS 入场/出场动画的「标准命名」来源 |  |  | 免费 |
| [animation-principles](https://github.com/dylantarre/animation-principles) | 把迪士尼 12 条动画原则（挤压拉伸、预备动作、跟随重叠、缓入缓出…）拆成 144 个 Claude Code Skill，按应用领域、情绪、时长、工具等 12 个维度组织，想让 Agent 用专业动画语言设计微交互和加载动效时装上；MIT（个人项目，星数不多） |  | `git clone https://github.com/dylantarre/animation-principles.git ~/.claude/plugins/animation-principles` | 开源 |
| [Animista](https://animista.net) | CSS 动画预设及其标准名称（slide-in-blurred、flip-scale…），可在线调参 |  |  | 免费 |
| [AnimXYZ](https://animxyz.com) | 可组合的 CSS 动画工具包，用 fade、up、rotate-right、stagger 等属性词像搭积木一样拼出入场退场动画，文档带实时调参面板，适合用声明式词汇描述组合动效；MIT 开源 | CSS, Vue, React | `npm install @animxyz/core` | 开源 |
| [AOS (Animate On Scroll)](https://michalsnik.github.io/aos/) | 经典的滚动入场动画库，fade-up、zoom-in、flip-left、slide-right 等命名已成为「滚动揭示」效果的通用叫法，用 data 属性即可启用；MIT，⚠ 多年未更新，新项目可用 CSS 滚动驱动动画或 Motion 的 whileInView 替代 |  | `npm i aos` | 开源 |
| [ARIA Authoring Practices Guide (APG) Patterns](https://www.w3.org/WAI/ARIA/apg/patterns/) | W3C 官方的组件模式指南，给出 Combobox、Disclosure、Listbox、Menu Button、Tabs、Treegrid 等约 30 种交互组件的规范名称、键盘交互和 ARIA 用法及可运行示例，是组件「标准叫法」和无障碍行为的最终依据；免费 |  |  | 免费 |
| [CARI（消费美学研究所）](https://cari.institute) | Consumer Aesthetics Research Institute 整理的 1970 年代至今的消费视觉美学词典，给 Frutiger Aero、Y2K、Global Village Coffeehouse、Corporate Memphis 等风格定名并配大量图例，想准确说出某种年代感视觉风格的名字时查；免费 |  |  | 免费 |
| [CSSFX](https://cssfx.netlify.app) | 命名 CSS 效果，点击复制代码 |  |  | 免费 |
| [cubic-bezier.com](https://cubic-bezier.com) | 贝塞尔缓动曲线编辑器 |  |  | 免费 |
| [design-motion-principles](https://github.com/kylezantos/design-motion-principles) | 设计或审查「有目的」的动效 |  | `npx skills add kylezantos/design-motion-principles` | 免费 |
| [Easing Wizard](https://easingwizard.com) | CSS 缓动函数生成器，除贝塞尔曲线外还能用 linear() 生成弹簧、回弹、摆动等物理感曲线，并可预览在移动、缩放、透明度上的效果，需要「带回弹的缓动」而不想引入 JS 动画库时用；免费 |  |  | 免费 |
| [Easings.net](https://easings.net) | 缓动曲线标准名称（easeOutExpo…）对照图 |  |  | 免费 |
| [Eyecannndy](https://eyecannndy.com) | 视觉技法图书馆，把影像和动态设计里的手法逐个命名并配 GIF 示例（如 Dolly Zoom、Match Cut、Slit Scan、Datamosh、Double Exposure），不知道某种镜头或后期效果叫什么时来这里对照；免费 |  |  | 免费 |
| [Flim](https://flim.ai) | 影视画面的 AI 搜索引擎，可按情绪、颜色、年代或自然语言描述检索 200 多万帧电影、剧集、广告和 MV 画面并建立参考板，作为 ShotDeck 的替代；有免费额度，完整功能订阅 |  |  | 免费+付费 |
| [Hover.css](https://ianlunn.github.io/Hover/) | 命名 hover 效果（grow、sweep、underline-from-center…） |  |  | 免费 |
| [Linear Easing Generator](https://linear-easing-generator.netlify.app) | Jake Archibald 与 Adam Argyle 做的 linear() 缓动生成器，把任意 JS 缓动函数或 SVG 路径转换成 CSS linear() 取样点，用来把弹簧、弹跳等复杂曲线带进纯 CSS；免费 |  |  | 免费 |
| [LottieFiles motion-design-skill](https://github.com/LottieFiles/motion-design-skill) | 时长、缓动、编排、迪士尼动画原则 |  | `npx skills add LottieFiles/motion-design-skill` | 免费 |
| [Motion Effects 325](https://sueun-dev.github.io/motion-effects/) | 325 个 Canvas/WebGL/three.js 效果，5 秒视频演示 + 英/韩 Prompt（新项目） |  | copy prompt | 免费 |
| [Motion Library（510 效果）](https://chengwq95.github.io/motion-library/) | 510 个网页效果（文字/按钮/卡片/导航…），可搜索筛选，有 React/Vue 版本，每个可复制 Prompt（新项目，星数少） |  | copy prompt | 免费 |
| [motion-prompt 动态画廊](https://showheyohtaki.github.io/motion-prompt/) | motion-prompt 的在线画廊，所有效果可实时播放，点 Copy Prompt 直接复制给 AI |  | copy prompt | 免费 |
| [NN/g UI Elements Glossary](https://www.nngroup.com/articles/ui-elements-glossary/) | 权威 UI 元素术语表 |  |  | 免费 |
| [Open UI](https://open-ui.org) | W3C 社区组的组件研究项目，横向对比各大设计系统对同一组件的命名与结构（组件名称矩阵），并孵化 popover、可定制 select 等新 HTML 能力，想知道某个控件在业界有哪些叫法时查；免费 |  |  | 免费 |
| [Scroll-driven Animations](https://scroll-driven-animations.style) | Chrome 团队 Bramus 维护的滚动驱动动画演示与工具站，涵盖阅读进度条、视差、进入视口揭示、吸顶头部收缩、横向滚动画廊等，并有 view-timeline 范围可视化工具，用纯 CSS 做滚动联动效果时参考；免费 |  |  | 免费 |
| [SheCodes: Animations for AI Coders](https://books.shecodes.io/animations) | 入门级 hover/入场/循环动效术语表（Wiggle、Shimmer、Typing Dots），带 Prompt |  | copy prompt | 免费 |
| [ShotDeck](https://shotdeck.com) | 专业级电影剧照参考库，上百万张高清影视截图逐张标注了景别、机位角度、镜头焦段、布光方式、色彩和年代，可按这些维度精确检索，写图像/视频生成 Prompt 需要准确的镜头与灯光术语时用；⚠ 付费订阅 |  |  | 付费 |
| [Superdesign Prompt Library](https://superdesign.dev/library) | 社区设计 Prompt，按风格和页面区块分类（如 GSAP 横向画廊） |  | Use this prompt / llms.txt: https://superdesign.dev/llms.txt | 免费 |
| [tailwindcss-animated](https://www.tailwindcss-animated.com) | Tailwind 的扩展动画工具类插件，提供 animate-fade-up、animate-jump-in、animate-wiggle、animate-shake 等大量命名动画，并可用类名调时长、延迟、缓动和次数，文档页可在线配置后复制；MIT | Tailwind | `npm i tailwindcss-animated` | 开源 |
| [tailwindcss-motion (Rombo)](https://rombo.co/tailwind/) | Rombo 出品的 Tailwind 动画插件，用 motion-preset-fade、motion-preset-slide-up、motion-scale-in-0 等语义化类名组合出入场、循环和弹性动画，纯 CSS 无运行时，适合让 Agent 直接写类名而不是手写 keyframes；MIT | Tailwind | `npm i -D tailwindcss-motion` | 开源 |
| [The Component Gallery](https://component.gallery) | 90+ 设计系统里同一组件的标准叫法（Accordion/Disclosure/Collapse…），用来查组件到底叫什么 |  |  | 免费 |
| [Theme Toggle (View Transitions)](https://theme-toggle.rdsx.dev) | 一组用 View Transitions API 做的主题切换转场（以圆形遮罩扩散为基础，演示加模糊、改圆心、换形状等变体），每种都能预览并复制 CSS，做亮暗模式切换动效时直接取用；免费 |  |  | 免费 |
| [Transition.css](https://www.transition.style) | 一组用 clip-path 实现的即插即用 CSS 过渡，按形状和方向命名（circle、square、polygon、wipe 的 in/out 各方向），点击即可预览并复制，想给页面或图片加「圆形展开」「擦除揭示」这类转场时用它的叫法；免费开源 | CSS |  | 开源 |
| [Transitions.dev](https://transitions.dev) | 专门为 AI Agent 准备的 UI 过渡库：40 多个命名清楚的过渡（弹窗开合、Toast、下拉、标签切换、数字滚动等）可逐个预览并复制，配套 Skill 让 Agent 直接按名称套用，另有命令行给现有项目的动效打分；基础库和 Skill 免费，Pro 内容付费 |  | `npx skills add Jakubantalik/transitions.dev`<br>`npx transitions-agent` | 免费+付费 |
| [TypeUI UI Animations](https://typeui.sh/ui-animations) | 约 281 个命名 UI 微交互（Spring slide、Dot ripple…） |  | copy prompt / TypeUI MCP | 免费+付费 |
| [UI Guideline](https://www.uiguideline.com) | 拆解全球主流设计系统后归纳出的组件百科，逐个组件汇总各家的命名、解剖结构、属性和文档写法，给自己的组件定名、定结构时用来取最大公约数；组件百科免费浏览，配套 Figma 套件付费 |  |  | 免费+付费 |
| [UI-Patterns](https://ui-patterns.com) | 命名 UX 模式库 |  |  | 免费 |
| [UI-Prompt（UI 风格提示词模板库）](https://github.com/TonnyWong1052/UI-Prompt) | 中英双语的 UI 风格 Prompt 模板库，用「风格卡片 + 一键复制 + 即时预览」的方式提供扁平、极简等风格以及导航、弹窗、骨架屏等组件的提示词，用来压低 AI 生成界面的同质化；⚠ 仓库未声明许可证，在线演示站已无法访问，需克隆后本地运行，组件与布局部分作者标注为未完成 |  |  | 免费 |
| [uiprompt](https://uiprompt.io) | 落地页设计 Prompt 蓝图库，每条以某个知名网站的视觉风格为蓝本（如暗绿颗粒渐变、色块新粗野、AI 开发工具暗色风），给出可直接喂给 Claude、Codex、v0、Lovable、Bolt 的完整设计提示词，想复刻某种成熟风格时找对应条目复制 |  |  | 免费 |
| [userinterface.wiki](https://userinterface.wiki) | 「更好界面的活手册」，带演示，站内提供 Skill |  |  | 免费 |
| [UX Patterns for Developers](https://uxpatterns.dev) | 写给开发者的 UX 模式文档站，逐个讲清自动完成、无限滚动、模态框、分页、通知等模式的标准名称、适用场景、无障碍要求和实现要点，并有「该用弹窗还是表单」这类决策指南，让 Agent 选对并叫对交互模式时用；免费 |  | llms.txt: https://uxpatterns.dev/llms.txt | 免费 |
| [View Transitions Demos](https://view-transitions.chrome.dev) | Chrome DevRel 的 Bramus 做的 View Transitions API 演示合集，展示共享元素过渡、列表重排、图片展开、跨页面转场、圆形揭示等典型模式并附源码，想让 Agent 用浏览器原生能力做页面级过渡时指给它看；免费 |  |  | 免费 |

<a id="ui-design-skills"></a>

## 设计风格 / 审美类 Skill 与 DESIGN.md

让 Agent 有审美、去 AI 味；或直接套用知名网站的设计系统（DESIGN.md）。

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Anthropic 官方「去 AI 味」前端审美 Skill，避免千篇一律的紫色渐变 + Inter 字体 | `npx skills add anthropics/skills --skill frontend-design` | 免费 |
| ⭐ [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 从 Claude、Stripe、Linear、Vercel 等名站提取的 DESIGN.md，丢进项目根目录即可让 AI 照着这个风格做（126k★） | drop-in DESIGN.md | 免费 |
| ⭐ [Impeccable](https://impeccable.style) | 「给编码 Agent 的设计词汇」：polish/bolder/critique/audit 等命令 + AI-slop 检测器（107k★） | `npx impeccable install` | 免费 |
| ⭐ [Taste Skill](https://github.com/Leonxlnx/taste-skill) | 艺术指导、参考图、浏览器自检，避免通用 AI 外观（112k★） | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` | 免费 |
| ⭐ [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 可检索的设计数据库：80 种 UI 风格、192 种产品类型、192 套配色、74 组字体搭配 + UX 规则，自动生成设计系统（147k★） | `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill`<br>`/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`<br>或 `npm i -g ui-ux-pro-max-cli && uipro init --ai claude` | 免费 |
| [Aura](https://www.aura.build) | Meng To 做的设计优先型 AI 建站工具，可用模板、组件、素材和 DESIGN.md 设计系统作参考生成落地页，并导出 HTML + Tailwind 或 Figma，站内的组件、Skills 和设计系统页面可当作高质量 Prompt 与风格参考库；按 Prompt 额度计费，有免费额度 | llms.txt: https://www.aura.build/llms.txt | 免费+付费 |
| [awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design) | 68 个为 Claude Design 调过的 DESIGN.md 灵感 |  | 免费 |
| [awesome-claude-design (rohitg00)](https://github.com/rohitg00/awesome-claude-design) | 围绕 Claude Design 的资源清单，按美学流派整理 DESIGN.md 提示词，并收录混搭配方、相关 Skill、视频拆解和社区评价，想找某种风格的现成 DESIGN.md 或了解大家怎么用时翻；MIT（与 VoltAgent 的同名仓库是两个项目） |  | 开源 |
| [awesome-design-skills](https://github.com/bergside/awesome-design-skills) | 67 个 DESIGN.md / SKILL.md 风格文件，带 pull CLI |  | 免费 |
| [bencium-marketplace](https://github.com/bencium/bencium-marketplace) | 一组基于 Anthropic Skill 指南扩展的设计与开发 Skill，含受控型 UX 设计师、排版、设计审查等，可用 --list 查看后按需单装，想要比官方 frontend-design 更克制、可控的设计输出时试；MIT | `npx skills add bencium/bencium-marketplace --list` | 开源 |
| [claudedesignskills](https://github.com/freshtechbro/claudedesignskills) | 面向 3D 与动效 Web 开发的 Claude Code 插件市场，按主题打包 Three.js、GSAP ScrollTrigger、React Three Fiber、Motion、Babylon.js、PixiJS、Lottie、Rive、Spline、Blender 等二十多个 Skill，做沉浸式落地页前按需安装对应包；MIT | `/plugin marketplace add freshtechbro/claudedesignskills` | 开源 |
| [daisyUI UI design prompts](https://trends.daisyui.com/ui-design-prompts/) | 命名风格 Prompt，做出有辨识度的界面 | copy prompt | 免费 |
| [Dembrandt](https://github.com/dembrandt/dembrandt) | 一条命令把任意网站的设计系统提取成令牌（Logo、配色、字体、间距、圆角、阴影等），可输出 DESIGN.md 并提供 MCP 与 Skill，想让 Agent「照着某个网站的风格做」时先用它抓取；MIT | `npx dembrandt <url>`<br>`claude mcp add --transport stdio dembrandt -- npx -y dembrandt mcp`<br>`npx skills add dembrandt/dembrandt-skills` | 开源 |
| [DESIGN.md 规范（Google Labs）](https://github.com/google-labs-code/design.md) | 向 Agent 描述视觉识别的官方格式规范，附 lint 工具 | `npx @google/design.md lint DESIGN.md` | 免费 |
| [Designer Skills (Owl-Listener)](https://github.com/Owl-Listener/designer-skills) | 覆盖设计全流程的 Skill 与命令合集，分设计研究、UX 策略、UI 设计、交互设计、设计系统、交付等插件，适合把 Agent 当设计搭档做用户研究综合、信息架构和设计评审而不仅是写界面；MIT | `/plugin marketplace add Owl-Listener/designer-skills` | 开源 |
| [designer-skills (julianoczkowski)](https://github.com/julianoczkowski/designer-skills) | 写给用 AI 编码工具做原型的设计师的一组 Skill，把设计流程编码成固定步骤，让 Agent 按结构化路径推进而不是直接跳去写代码；Apache-2.0 | `npx skills add julianoczkowski/designer-skills` | 开源 |
| [DesignPrompts](https://designprompts.dev) | 落地页风格构建器，选好风格后复制 Prompt 给 Agent；含词汇表 + JSON Schema | copy prompt / llms.txt: https://designprompts.dev/llms.txt | 免费+付费 |
| [Devouring Details](https://devouringdetails.com) | Rauno Freiberg 的交互设计互动参考手册，用可操作的原型逐章讲解手势、运动、反馈和隐喻背后的原则并附组件源码，想系统提升交互质感的设计工程师可读；⚠ 付费内容 |  | 付费 |
| [getdesign.md](https://getdesign.md) | awesome-design-md 的网站版，550+ DESIGN.md 目录 | copy DESIGN.md | 免费+付费 |
| [interface-design](https://github.com/Dammyjay93/interface-design) | 跨会话保持 UI 决策一致性 | `npx skills add https://github.com/dammyjay93/interface-design --skill interface-design` | 免费 |
| [jakubkrehel/skills（Interfaces）](https://github.com/jakubkrehel/skills) | 设计工程师 Jakub Krehel 的界面 Skill 合集，含 better-ui、better-typography、better-colors、better-layout、better-accessibility、better-writing 以及 interface-review、explain-interface、variant 等，给出圆角、光学对齐、阴影、字距这类具体数值，与同作者的 make-interfaces-feel-better 一脉相承且范围更广；MIT | `npx skills add jakubkrehel/skills` | 开源 |
| [make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) | 界面打磨与微交互 Skill | `npx skills add jakubkrehel/make-interfaces-feel-better` | 免费 |
| [MengTo Skills](https://github.com/MengTo/Skills) | 视频→超级 Prompt、HTML→交互 Prompt、14 种 SVG 插画风格、3D Skill |  | 免费 |
| [nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) | 让 Claude Code 按 Nothing 的设计语言生成 UI 的 Skill：单色 OLED 黑、瑞士式排版、Space Grotesk/Space Mono/Doto 字体、分段进度条和点阵元素，可输出 HTML/CSS、SwiftUI 或 React/Tailwind，想要一眼可辨的 Nothing 风格界面时用；MIT | `git clone https://github.com/dominikmartn/nothing-design-skill.git` | 开源 |
| [OpenAI Plugins（Figma / Product Design）](https://github.com/openai/plugins) | OpenAI 官方的 Codex 插件仓库，其中 figma 插件含 figma-use、figma-design-to-code、figma-generate-design、figma-generate-library、figma-implement-motion 等 Skill，product-design 插件含 audit、design-qa、ideate、image-to-code、url-to-code；⚠ 原 openai/skills 仓库已标记弃用并指向这里 |  | 开源 |
| [OpenDesign](https://github.com/nexu-io/open-design) | 开源、本地优先的 AI 设计 Agent 工作台，从一段需求出发让编码 Agent 按你的设计系统生成原型、网站、仪表盘、演示和动效，并内置可查看和改写的 Skill、设计模板与设计系统库，想要 Claude Design 的开源替代时用；Apache-2.0，云端服务另行收费 |  | 开源 |
| [platform-design-skills](https://github.com/ehmo/platform-design-skills) | 把 Apple HIG、Material Design 3 和 WCAG 2.2 提炼成 300 多条规则的平台设计 Skill 包，覆盖 iOS、iPadOS、macOS、watchOS、visionOS、tvOS、Android 和 Web，做原生应用时让 Agent 遵守对应平台规范；MIT | `npx skills add ehmo/platform-design-skills` | 开源 |
| [PostHog: Engineer's guide to vibe design](https://newsletter.posthog.com/p/an-engineers-guide-to-vibe-design) | 工程师视角的 vibe design 提示指南，带示例 Prompt |  | 免费 |
| [Rams](https://www.rams.ai) | 给 Agent 写的 UI 做设计质量审查的引擎，按 365 条规则（无障碍、配色、排版、间距、状态、动效等 9 类）给代码打 0–100 分并返回可应用的修复补丁，可作为 MCP 或 GitHub App 接入，适合在提交前自动拦住「AI 味」和设计系统漂移；有免费试用额度，之后付费 | MCP: https://worker.rams.ai/mcp（OAuth 登录，接入方式见 https://www.rams.ai/setup）<br>llms.txt: https://www.rams.ai/llms.txt | 免费+付费 |
| [Refero Styles](https://styles.refero.design) | 2000+ 真实产品的 AI 可读设计系统，每个带 DESIGN.md | Refero MCP | 免费+付费 |
| [Refero：给 AI Agent 的设计资源](https://styles.refero.design/ai-agents/design-resources) | Refero Styles 的 Agent 专题入口，把真实网站的设计风格按仪表盘、落地页、定价、引导、表单、设置等场景整理成可复制的设计 Prompt 与 DESIGN.md 示例，并附 DESIGN.md 模板、规范说明和 AI 生成 UI 质量检查清单；免费浏览 |  | 免费 |
| [TypeUI](https://typeui.sh) | 设计 Skill 注册表、UI Prompt、布局指导 | TypeUI MCP<br>`npx typeui.sh pull <slug>` | 免费+付费 |
| [UI Skills](https://www.ui-skills.com) | 设计工程师 Skill 注册表（含 motion 分类） | `npx ui-skills get baseline-ui`<br>MCP https://www.ui-skills.com/mcp | 免费 |
| [ui-craft](https://github.com/educlopez/ui-craft) | SmoothUI 作者做的「设计工程系统」Skill，为 Agent 提供从发现、设计到打磨、审查的整套流程和命令，并附带一个做确定性检查的 MCP，想让 Agent 产出达到手工打磨水准的 UI 时装；MIT | `npx skills add educlopez/ui-craft` | 开源 |
| [ui-ux-pro-mcp](https://github.com/redf0x1/ui-ux-pro-mcp) | 把 UI/UX 设计知识库做成 MCP 服务器的社区项目，内置 1500+ 条风格、配色、字体搭配、图表类型和各技术栈的 UX 准则供 Agent 检索，不想装 Skill 而想用 MCP 查设计建议时用；MIT（社区小项目，星数少） | `npx ui-ux-pro-mcp` | 开源 |
| [ui.sh](https://ui.sh) | 面向界面构建者的任务型 Agent Skill 集：Design（以资深设计师水准做新界面）、Ideas（并排生成多个设计方向）、Brand Kit、Componentize、Add Dark Mode、Make Responsive、Markup From Image 等，每个 Skill 对应一个明确任务；⚠ 需登录后使用，定价以官网为准 |  | 付费 |
| [Uncodixfy](https://github.com/cyxzdev/Uncodixfy) | 一份专治「GPT 味」界面的规则集，不教模型怎么设计，而是逐条禁止它惯用的套路（悬浮卡片、过大圆角、满屏渐变、装饰性小标签、玻璃面板等），把输出推回更正常的界面，可作为 Skill 安装或直接贴进系统提示；MIT | `npx skills add cyxzdev/Uncodixfy` | 开源 |
| [Vercel Web Interface Guidelines](https://vercel.com/design/guidelines) | 界面质量规则；也作为 web-design-guidelines Skill 发布 | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` | 免费 |
| [Web Interface Guidelines (Rauno)](https://interfaces.rauno.me) | Rauno Freiberg 整理的 Web 界面细节清单，按交互、排版、动效、触控、性能、无障碍分条列出「好界面该有的细节」（如输入框不缩放、Toast 不遮挡、动画可被打断），Vercel 的同名规范即由此发展而来，适合整段贴进 AGENTS.md 当约束；免费 |  | 免费 |
| [wondelai/skills（UX Design 包）](https://github.com/wondelai/skills) | 把畅销书方法论做成 Skill 的合集，其中 ux-design 插件包含 Refactoring UI、iOS HIG、UX 启发式评估、Hooked、微交互、Web 排版、日常物品的设计等，想让 Agent 按经典设计书的框架评审界面时装；MIT | `/plugin marketplace add wondelai/skills`<br>`/plugin install ux-design@wondelai-skills` | 开源 |
| [乔木 Design（qiaomu-design）](https://github.com/joeseesun/qiaomu-design) | 「偏执型设计顾问」Skill：反 AI 味的设计规则、可先试穿再定的风格试衣间，以及 58 个真实网站的设计系统库，中文说明完整，想让 Agent 先比较几种风格再动手时用；MIT | `npx skills add joeseesun/qiaomu-design` | 开源 |
| [花叔 Design（huashu-design）](https://github.com/alchaincyf/huashu-design) | 中文社区最热门的设计 Skill 之一：一句话需求，先出多个候选方向再深化，可交付网页、App 原型、可编辑 PPTX、动画和信息图，内置 84 种带样张的风格库和设计体检，中文场景下想要开箱即用的设计能力时装；MIT | `npx skills add alchaincyf/huashu-design` | 开源 |

<a id="ui-prompt-guides"></a>

## 官方 Prompt 指南（v0 / Lovable / Bolt / Stitch / Claude）

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Claude Cookbook: Prompting for frontend aesthetics](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb) | 排版、主题、动效的 Prompt 模块，可直接拼进系统提示 |  | 免费 |
| [Anthropic: Improving frontend design through Skills](https://claude.com/resources/articles/improving-frontend-design-through-skills) | frontend-design Skill 背后的思路与提示方法 |  | 免费 |
| [Bolt: Prompting effectively](https://support.bolt.new/prompting/prompting-effectively) | Bolt 官方提示最佳实践 |  | 免费 |
| [Google Stitch Prompt Guide](https://stitch.withgoogle.com/docs/learn/prompting/) | Stitch 官方 UI 生成提示指南 |  | 免费 |
| [Lovable Prompting Handbook](https://docs.lovable.dev/prompting/prompting-one) | Lovable 官方提示手册 |  | 免费 |
| [Stitch Skills（Google Labs）](https://github.com/google-labs-code/stitch-skills) | Stitch MCP 配套的 design-md、shadcn-ui 等 Skill | `npx skills add google-labs-code/stitch-skills` | 免费 |
| [v0 text-prompting docs](https://v0.app/docs/text-prompting) | v0 官方提示指南 |  | 免费 |

<a id="ui-camera-photo"></a>

## 镜头 / 摄影 / 灯光词汇（图像与视频生成）

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Google Veo 视频提示指南](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide) | 官方镜头运动、景别、镜头焦段、风格术语 |  | 免费 |
| [Atlabs: 27 种电影级布光](https://www.atlabs.ai/blog/27-cinematic-lighting-looks-ai-prompts-guide) | 命名布光风格 + 可复制修饰词 | copy prompt | 免费 |
| [FilmGrab](https://film-grab.com) | 电影截图参考库（找画面风格） |  | 免费 |
| [Midlibrary](https://midlibrary.io) | Midjourney 风格库：艺术家、流派、技法、胶片质感 |  | 免费+付费 |
| [Promptomania](https://promptomania.com) | 可视化图像 Prompt 构建器，含风格与镜头术语 |  | 免费 |
| [Runway AI camera prompts](https://runway.com/resources/ai-camera-prompts) | 镜头术语（pan vs truck、pedestal…） |  | 免费 |
| [StudioBinder 镜头运动大全](https://www.studiobinder.com/blog/different-types-of-camera-movements-in-film/) | 电影镜头运动/景别标准词汇，带示例 |  | 免费 |
