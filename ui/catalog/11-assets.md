# 图标 / 字体 / 配色 / 主题

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-assets"></a>

## 图标、字体、配色、主题生成

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Fontshare](https://www.fontshare.com) | 免费高质量字体（Clash、General Sans、Satoshi…），比 Inter 更有个性 |  |  | 免费 |
| ⭐ [Iconify](https://iconify.design) | 200+ 图标集、20 万+ 图标；公开免 key API |  | `claude mcp add iconify -- npx -y iconify-mcp-server@latest`（社区） | 免费 |
| ⭐ [Lucide](https://lucide.dev) | shadcn 和多数 AI 工具的默认图标集 |  | llms.txt: https://lucide.dev/llms.txt<br>`npx lucide-mcp`（社区） | 免费 |
| ⭐ [Realtime Colors](https://www.realtimecolors.com) | 在真实页面上预览配色和字体，导出 CSS/Tailwind |  |  | 免费 |
| ⭐ [tweakcn](https://tweakcn.com) | shadcn/Tailwind 可视化主题编辑器，有预设和 AI 主题生成，导出后一行命令装入 |  | `npx shadcn@latest add https://tweakcn.com/r/themes/<preset>.json`（预设主题，例如 amber-minimal） | 免费 |
| [Accessible Palette](https://accessiblepalette.com) | 用 CIELAB/LCh 模型生成亮度一致的色彩系统，保证任意色相的同一级与背景的对比度相同，从而只需记住「相差几级就达标」，做设计系统色板时用；免费 |  |  | 免费 |
| [Adobe Color](https://color.adobe.com) | 经典的色轮配色工具，按互补、三角、类比等和谐规则取色，可从图片提取主题色和渐变，并内置对比度与色盲友好检查；免费，登录后可保存到 Creative Cloud 库 |  |  | 免费 |
| [Adobe Fonts](https://fonts.adobe.com) | Creative Cloud 订阅附带的商业字体库，3 万+ 款字体含大量知名铸字厂作品和中日韩字体，可同步到桌面和以 Web Project 嵌入网站；⚠ 需有效订阅，只能经 Adobe 托管加载、不可自托管字体文件 |  |  | 付费 |
| [Akar Icons](https://akaricons.com) | 400 多个圆角描边图标，线条饱满、识别度高，可在线调线宽和尺寸后复制，适合小而精的产品界面；MIT |  | `npm i akar-icons` | 开源 |
| [APCA Contrast Calculator](https://apcacontrast.com) | APCA（拟用于 WCAG 3 的感知对比度算法）的官方计算器，按字号和字重给出所需的 Lc 值，暗色模式和细字体下比 WCAG 2 的比值更贴近真实可读性；免费，⚠ APCA 尚非正式合规标准 |  |  | 免费 |
| [Atkinson Hyperlegible](https://www.brailleinstitute.org/freefont/) | Braille Institute 为低视力读者设计的字体，刻意放大易混字符（I/l/1、O/0）的差异，面向老年用户或无障碍要求高的产品时用；OFL，可商用 |  |  | 开源 |
| [Atmos](https://atmos.style) | 面向 UI 设计师的调色板工具，在 LCH/OKLCH 空间里生成亮度均匀的色阶、检查对比度并导出 CSS 变量与 Figma，适合从零搭一套产品色板；基础功能免费，高级功能付费 |  |  | 免费+付费 |
| [Bootstrap Icons](https://icons.getbootstrap.com) | Bootstrap 官方的 2000+ 个开源图标，提供 SVG、Sprite 和图标字体，不依赖 Bootstrap 也能单独用，传统后台和文档站常用；MIT |  | `npm i bootstrap-icons` | 开源 |
| [BrandColors](https://brandcolors.net) | 收录 600 多个知名品牌官方色值的速查表，可搜索并导出 CSS/SCSS/ASE，做第三方登录按钮、分享按钮或竞品色彩分析时查用；免费，⚠ 品牌色的使用受各品牌规范约束 |  |  | 免费 |
| [Brandfetch](https://brandfetch.com) | 品牌数据平台，按域名取一家公司的 Logo、品牌色、字体和简介，Logo CDN 免费、完整品牌 API 按额度计费，并提供 MCP，想让界面自动套用客户品牌色或批量拿 Logo 时用 |  | llms.txt: https://brandfetch.com/llms.txt | 免费+付费 |
| [Bunny Fonts](https://fonts.bunny.net) | 与 Google Fonts CSS API 兼容的零追踪字体 CDN，把域名换成 fonts.bunny.net 即可，不记录访客 IP、符合 GDPR，不想自托管又要合规时用；免费，字体均为开源许可 |  | https://fonts.bunny.net/css?family=inter:400,700 | 免费 |
| [Capsize](https://seek-oss.github.io/capsize/) | 根据字体度量裁掉行框上下多余空白的工具，让文字按大写高度与基线精确对齐，并可生成与 Web 字体度量匹配的回退字体以消除加载时的布局偏移；MIT |  | `npm i @capsizecss/core` | 开源 |
| [Carbon Icons](https://www.carbondesignsystem.com/building-blocks/foundations/icons/library) | IBM Carbon 设计系统的 2000+ 个图标，偏工程与企业场景（云、数据、AI、网络设备），做 B 端控制台和技术架构类界面时用；Apache-2.0 | React | `npm i @carbon/icons-react`<br>llms.txt: https://www.carbondesignsystem.com/llms.txt | 开源 |
| [Catppuccin](https://catppuccin.com) | 社区驱动的柔和粉彩配色方案，Latte（亮）到 Mocha（暗）四种风味，各 26 个命名色，已移植到数百种编辑器和应用，给开发者工具或终端风界面套一个受欢迎的主题时用；MIT |  | `npm i @catppuccin/tailwindcss` | 开源 |
| [chroma.js](https://gka.github.io/chroma.js/) | 老牌的颜色处理库，颜色转换、混合、明暗调整、感知均匀的色阶和对比度计算一应俱全，数据可视化里生成连续/分级色带的常用选择；BSD 许可 |  | `npm i chroma-js` | 开源 |
| [circle-flags](https://hatscripts.github.io/circle-flags/) | 400+ 个极简的圆形 SVG 旗帜，涵盖国家、地区和语言，可直接通过 CDN 按代码引用，头像旁的小国旗和语言选择器用圆形更协调时选它；MIT |  | https://hatscripts.github.io/circle-flags/flags/&lt;国家代码&gt;.svg | 开源 |
| [Collletttivo](https://www.collletttivo.it) | 意大利的开源字体铸造集体，出品 Mazius、Ribes、Sneaky、Apfel Grotezk 等风格鲜明的展示与正文字体，做编辑感、时尚感页面时用；OFL，可商用 |  |  | 开源 |
| [Color Hunt](https://colorhunt.co) | 社区投票的四色配色合集，可按流行度、色系和风格（复古、霓虹、柔和、暗色等）筛选，想快速拿一组现成的小配色时用；免费 |  |  | 免费 |
| [Color Names (meodai)](https://github.com/meodai/color-names) | 3 万多个人工整理的颜色名称库和免 key API，传入任意 hex 返回最接近的命名（如 #0f1012 → Ruined Smores），给设计令牌、色板或生成式主题起名字时用；MIT |  | https://api.color.pizza/v1/?values=0d0d0f,f39d91<br>`npm install color-name-list` | 开源 |
| [Color Thief](https://lokeshdhakar.com/projects/color-thief/) | 从图片中提取主色和调色板的 JavaScript 库，浏览器和 Node 都能用，做「卡片背景跟随封面图变色」这类自适应配色时用；MIT |  | `npm i colorthief` | 开源 |
| [ColorBox](https://colorbox.io) | Lyft 设计团队的色阶生成器，用可编辑的曲线分别控制色相、饱和度和亮度的走向，适合系统性地生成一整套多色相、步进均匀的色板；免费 |  | llms.txt: https://colorbox.io/llms.txt | 免费 |
| [Colormind](https://colormind.io) | 用深度学习从照片、电影和流行设计中学习配色的调色板生成器，可锁定部分颜色让它补全，并提供网站模板预览和免 key 的 HTTP API；免费，⚠ API 仅限个人和非商业使用 |  | `curl 'https://colormind.io/api/' --data-binary '{"model":"default"}'` | 免费 |
| [ColorSpace](https://mycolor.space) | 输入一个颜色，一次性给出几十组不同逻辑的配色方案（通用渐变、匹配渐变、点缀色、经典色等）和双色/三色渐变代码，已有主色想扩展成整套时用；免费 |  |  | 免费 |
| [Colour Contrast Checker](https://colourcontrast.cc) | 界面简洁的对比度检查工具，用滑块实时调整前景和背景色并即时显示 WCAG 各等级结果，可分享链接，日常快速试色时用；免费 |  |  | 免费 |
| [Coolors](https://coolors.co) | 配色生成器 |  |  | 免费+付费 |
| [css.gg](https://css.gg) | 700+ 个纯 CSS 绘制的极简图标，同时提供 SVG、React 组件等格式，适合想用一个 class 画图标、不引入图片资源的场景；开源免费 |  | `npm i css.gg` | 开源 |
| [Culori](https://culorijs.org) | 功能全面的 JavaScript 色彩库，支持 OKLCH、OKLab、P3 等现代色彩空间的解析、转换、插值、色差计算和色域映射，写主题生成器或需要在 OKLCH 里做运算时用；MIT |  | `npm i culori` | 开源 |
| [Devicon](https://devicon.dev) | 编程语言、框架和开发工具的图标集，提供彩色、单色、带文字等版本的 SVG 与图标字体，做技术栈展示、文档和作品集时用；MIT，⚠ 商标归各项目所有 |  | `npm i devicon` | 开源 |
| [Eva Colors](https://colors.eva.design) | 输入一个主色，用深度学习算法生成成功、信息、警告、危险四种语义色及各自 9 级色阶，快速得到一套语义完整的产品色板；免费 |  |  | 免费 |
| [Feather](https://feathericons.com) | 280 多个极简的 24px 开源描边图标，是 Lucide 的前身，老项目和教程里很常见；MIT，⚠ 已基本停止更新，新项目直接用 Lucide |  | `npm install feather-icons` | 开源 |
| [flag-icons](https://flagicons.lipis.dev) | 全部国家和地区旗帜的 SVG 集合，提供 4:3 和 1:1 两种比例及配套 CSS 类，语言切换器、国家选择器和电话区号下拉里用；MIT |  | `npm i flag-icons` | 开源 |
| [Fluent UI System Icons](https://github.com/microsoft/fluentui-system-icons) | 微软 Fluent 设计语言的系统图标，数千个图标均有 Regular 和 Filled 两版及多种尺寸，Windows/Office 风格或 Teams 应用里保持原生观感时用；MIT |  | `npm i @fluentui/react-icons` | 开源 |
| [Fluid Type Scale Calculator](https://www.fluid-type-scale.com) | 专门生成流式字号阶梯的小工具，设好最小和最大屏宽下的基准与比例，直接输出一组 clamp() 自定义属性，比 Utopia 更轻、拿来即用；免费 |  |  | 免费 |
| [Font Awesome](https://fontawesome.com) | 最老牌的图标库，Free 版 2000+ 个图标含大量品牌 Logo，Pro 版有更多风格与图标；Free 版图标为 CC BY 4.0、字体 OFL、代码 MIT（使用官方文件时署名信息已内嵌），Pro 需订阅 |  | `npm i @fortawesome/fontawesome-free`<br>llms.txt: https://fontawesome.com/llms.txt | 免费+付费 |
| [Font Squirrel](https://www.fontsquirrel.com) | 人工筛选「可免费商用」字体的老牌站点，并提供 Webfont Generator（把字体转成 WOFF2 并子集化）和字体识别工具；免费，⚠ 仍需逐款核对许可细则 |  |  | 免费 |
| [FontDrop!](https://fontdrop.info) | 拖入字体文件即可查看全部字形、OpenType 特性、可变轴、语言支持和授权信息的在线检视器，核对一款字体的许可字段和字符覆盖时用；免费，文件不上传 |  |  | 免费 |
| [Fontjoy](https://fontjoy.com) | AI 生成字体搭配 |  |  | 免费 |
| [Fontpair](https://www.fontpair.co) | Google Fonts 搭配 |  |  | 免费 |
| [Fontsource](https://fontsource.org) | 把 Google Fonts 等 1500+ 开源字体做成 npm 包自托管的方案，字体随构建打包、可只引入需要的字重和子集并支持可变字体，替代在线引用 Google Fonts 以提升性能和隐私合规；包本身开源，字体多为 OFL |  | `npm install @fontsource-variable/inter`<br>https://api.fontsource.org/v1/fonts（公开 API）<br>llms.txt: https://fontsource.org/llms.txt | 开源 |
| [Free Faces](https://www.freefaces.gallery) | 按无衬线、衬线、等宽、展示等分类整理的免费字体画廊，样张直观，适合快速扫一遍当下流行的免费字体；⚠ 各字体许可不同，有的仅限个人使用，点进原站确认 |  |  | 免费 |
| [Game-icons.net](https://game-icons.net) | 4000+ 个游戏题材的单色图标（武器、技能、怪物、道具、状态），可在线改前景背景色和加描边阴影后导出，做游戏 UI、卡牌和技能树时用；⚠ CC BY 3.0，需署名作者 |  |  | 免费 |
| [Google Fonts](https://fonts.google.com) | 字体目录 + Developer API |  | `uvx google-fonts-mcp`（社区） | 免费 |
| [Google Fonts Knowledge](https://fonts.google.com/knowledge) | Google Fonts 的排版知识库，系统讲解字体选择、搭配、可变字体、行高字距和多语言排版，并附完整术语表，想让 Agent 或自己用对排版术语时查阅；免费 |  |  | 免费 |
| [Happy Hues](https://www.happyhues.co) | 在真实页面语境里展示的配色 |  |  | 免费 |
| [Harmonizer](https://harmonizer.evilmartians.com) | 基于 OKLCH 与 APCA 对比度生成整套 UI 色板的工具，保证不同色相在同一级上的感知亮度和对比一致，并可导出为代码，想要「换主题色也不会破对比度」的色阶时用；免费 |  |  | 免费 |
| [Health Icons](https://healthicons.org) | 面向医疗健康项目的开源图标集，覆盖人体、疾病、器械、药物、诊疗流程等上千个专业图形，做医疗、健身、公共卫生类产品时用；CC0，可商用免署名 |  |  | 开源 |
| [Heroicons](https://heroicons.com) | Tailwind 官方图标 |  |  | 免费 |
| [Huemint](https://huemint.com) | AI 生成配色 |  |  | 免费 |
| [Huetone](https://huetone.ardov.me) | 在 LCH 色彩空间里编辑整张色板矩阵的工具，实时显示每个色块对白/黑底的 WCAG 与 APCA 对比度，手工精修多色相色阶并保证可访问性时用；免费开源 |  |  | 开源 |
| [Hugeicons](https://hugeicons.com) | 号称最全的图标库，6 万+ 图标、10 种风格，免费包提供数千个 Stroke Rounded 风格图标并有官方 MCP 供 Agent 搜索，需要冷门行业图标或多风格统一时用；免费包 MIT，其余风格需 Pro |  | `npm install @hugeicons/react @hugeicons/core-free-icons`<br>`claude mcp add --transport http hugeicons https://mcp.hugeicons.com/mcp` | 免费+付费 |
| [IBM Plex](https://www.ibm.com/plex/) | IBM 的开源字体超家族，含 Sans、Serif、Mono 和中日韩等多文种版本，气质工程化、略带人文感，适合需要一套字体覆盖正文、代码和多语言的技术产品；OFL，可商用 |  | `npm i @ibm/plex` | 开源 |
| [Iconoir](https://iconoir.com) | 1600+ 个风格克制的开源描边图标（含实心变体），无需注册和署名，支持 React、Vue、Flutter、React Native 和纯 CSS，想要比 Lucide 更圆润轻盈的线条时用；MIT |  | `npm i iconoir-react`<br>llms.txt: https://iconoir.com/llms.txt | 开源 |
| [Icônes](https://icones.js.org) | Anthony Fu 做的 Iconify 图标浏览器，搜索极快，可跨 200 多套图标集检索并一键复制 SVG、组件代码或 Iconify 名称，挑图标时比各家官网都顺手；免费开源 |  |  | 开源 |
| [InclusiveColors](https://www.inclusivecolors.com) | 同时编辑多条色阶的无障碍色板工具，可分别调色相/饱和度/亮度曲线，实时核对 WCAG 与 APCA 对比度，并导出 Tailwind、CSS、Figma 和 Adobe 格式；免费 |  |  | 免费 |
| [Inter](https://rsms.me/inter/) | 为屏幕界面设计的可变无衬线字体，小字号清晰、OpenType 特性丰富（等宽数字、替代字形、光学尺寸），是事实上的 UI 默认字体；OFL，可商用，⚠ 太常见，想要辨识度时换 Fontshare 等来源的字体 |  | https://rsms.me/inter/inter.css（官方 CSS，直接 link 引入） | 开源 |
| [Ionicons](https://ionic.io/ionicons) | Ionic 团队的 1300+ 个图标，每个都有 Outline、Filled、Sharp 三种风格，以 Web Component 形式分发，移动端 Web 和 Ionic/Capacitor 应用里常用；MIT |  | `npm i ionicons` | 开源 |
| [JetBrains Mono](https://www.jetbrains.com/lp/mono/) | JetBrains 为写代码设计的等宽字体，x 高度大、字符区分清楚并带编程连字，代码块、终端风界面和数据表格的可靠选择；OFL，可商用 |  |  | 开源 |
| [Khroma](https://www.khroma.co) | 先让你挑 50 个喜欢的颜色训练个人偏好模型，再无限生成符合你口味的双色组合，并以文字、海报、渐变、图片等方式预览，没有配色灵感时用；免费 |  |  | 免费 |
| [Leonardo](https://leonardocolor.io) | Adobe 开源的对比度驱动色彩系统工具：先定目标对比度再反推各级色值，可生成自适应主题（亮暗、对比度可调）并导出设计令牌，做无障碍达标的设计系统色板时用；Apache-2.0 |  | `npm i @adobe/leonardo-contrast-colors` | 开源 |
| [Lineicons](https://lineicons.com) | 数量庞大的线性图标库，提供多种变体、CDN 和在线图标编辑器；⚠ 免费版仅 600 多个基础图标（MIT 附带限制，不得转售或再分发成图标包），完整库需 Pro 授权 |  |  | 免费+付费 |
| [Logo.dev](https://www.logo.dev) | 按域名、股票代码或加密货币符号返回公司 Logo 的图片 API（Clearbit Logo 的接班人），做客户列表、交易记录、CRM 里自动显示企业 Logo 时用；有免费档，⚠ 免费使用需按要求署名链接，token 为可公开的 publishable key |  | https://img.logo.dev/&lt;domain&gt;?token=&lt;publishable_key&gt;<br>llms.txt: https://www.logo.dev/llms.txt | 免费+付费 |
| [lucide-animated](https://lucide-animated.com) | 468 个带动画的 Lucide 图标 | React, Tailwind | `npx shadcn@latest add @lucide-animated/<icon>` | 免费 |
| [Material Design Icons (Pictogrammers)](https://pictogrammers.com/library/mdi/) | 社区维护的 Material 风格图标库，7000+ 个图标，比 Google 官方集多出大量品类（智能家居、设备、品牌相关），Vuetify 和 Home Assistant 生态的默认图标；Apache-2.0，⚠ 已不再收录新的品牌图标 |  | `npm i @mdi/js` | 开源 |
| [Material Symbols](https://fonts.google.com/icons) | Google 的可变图标字体，数千个图标有 Outlined/Rounded/Sharp 三种风格，并可连续调节填充、字重、粗细等级和光学尺寸，Android/Material 风产品或需要图标随状态变粗变实时用；Apache-2.0，可商用 |  | `npm i material-symbols`（社区维护，Google 官方仓库 README 列出但不负责审核） | 开源 |
| [Material Theme Builder](https://material-foundation.github.io/material-theme-builder/) | Material 3 官方主题生成器，从一个种子色或一张图片推导出完整的亮暗色角色体系（HCT 色彩空间），并导出 CSS、Compose、Flutter 和 Figma 令牌，做 Material You 动态配色时用；免费开源 |  | `npm i @material/material-color-utilities` | 开源 |
| [MingCute](https://www.mingcute.com) | 国内设计师出品的 3000+ 图标，线性与填充成对、圆角饱满，中文语境的类目（支付、出行、社交）覆盖好，做国内风格 App 时很合适；Apache-2.0，可商用 | React, Vue | `npm install @mingcute/react` | 开源 |
| [Modern Font Stacks](https://modernfontstacks.com) | 按字体分类（人文无衬线、几何、旧式衬线、等宽、手写等）整理的系统字体栈 CSS，不下载任何字体文件即可得到有风格差异的排版，追求零加载、零布局偏移时用；CC0 |  |  | 开源 |
| [Monaspace](https://monaspace.githubnext.com) | GitHub Next 的等宽字体超家族，五种风格（Neon、Argon、Xenon、Radon、Krypton）可在同一行混排，并有 texture healing 改善等宽字距，想在代码界面里用字体区分人写与 AI 生成内容时很合适；OFL |  |  | 开源 |
| [MynaUI Icons](https://mynaui.com/icons) | 一套线条优美的开源图标，提供描边和实心两版，风格介于 Lucide 与 Heroicons 之间，想给 shadcn 项目换一套不那么常见的图标时用；MIT |  | `npm i @mynaui/icons-react`<br>llms.txt: https://mynaui.com/llms.txt | 开源 |
| [Nerd Fonts](https://www.nerdfonts.com) | 给 70 多款等宽字体打补丁加入上万个图标字形（Devicon、Octicons、Font Awesome 等），终端提示符和 TUI 里显示图标的前提，做终端风格界面或 CLI 工具时用；补丁脚本 MIT，各字体沿用原许可 |  |  | 开源 |
| [NIPPON COLORS](https://nipponcolors.com) | 日本传统色网站，250 种带和名的颜色，点击即全屏切换并显示 CMYK/RGB/HEX，做和风、侘寂风配色或找低饱和的雅致颜色时用；免费 |  |  | 免费 |
| [Noun Project](https://thenounproject.com) | 全球最大的图标库，800 万+ 个风格各异的图标，几乎任何概念都能搜到对应图形，并有图标 API；⚠ 免费下载须署名作者，免署名和改色下载需订阅或单买 |  | llms.txt: https://thenounproject.com/llms.txt | 免费+付费 |
| [Nucleo](https://nucleoapp.com) | 4 万+ 个高度一致的商业图标，分 UI、Core、Micro 等尺寸体系，配套桌面应用管理和导出，愿意为图标质量与一致性付费的团队首选；付费授权 |  |  | 付费 |
| [Octicons](https://primer.style/octicons) | GitHub Primer 设计系统的图标集，专为代码托管、协作和开发者工具场景设计（PR、Issue、分支、提交等），做开发者产品时语义最贴切；MIT |  | `npm i @primer/octicons-react` | 开源 |
| [OKLCH Color Picker](https://oklch.com) | Evil Martians 做的 OKLCH 取色与转换器，直观展示亮度、色度、色相三个轴和 sRGB/P3 色域边界，Tailwind v4 与 shadcn 的主题变量都已改用 OKLCH，调这类变量时必备；免费开源 |  |  | 开源 |
| [Open Color](https://yeun.github.io/open-color/) | 为 UI 优化的开源配色方案，13 个色相各 10 级，Mantine 的默认色板即源于它，需要一套现成、均衡的基础色阶时用；MIT |  | `npm i open-color` | 开源 |
| [Open Foundry](https://open-foundry.com) | 精选开源字体的展示平台，每款都配有高质量的排版样张和设计师信息，适合在 Google Fonts 之外找更有设计感的免费字体；收录字体均为开源许可（多为 OFL） |  |  | 免费 |
| [Pangram Pangram](https://pangrampangram.com) | 当代知名铸字厂，Neue Montreal、Editorial New、Mori 等字体在设计圈和获奖网站里极常见，全部字体可免费下载试用；⚠ 免费版仅限个人和非商业使用，商用（含商业网站）必须购买授权 |  |  | 免费+付费 |
| [Phosphor Icons](https://phosphoricons.com) | 6 种字重的图标家族 |  |  | 免费 |
| [Picular](https://picular.co) | 「颜色版 Google」：输入任意词语（如 sunset、牛油果、信任），根据图片搜索结果返回与之关联的颜色，给抽象概念或品牌关键词找对应色时用；免费 |  |  | 免费 |
| [Pixelarticons](https://pixelarticons.com) | 24×24 网格上的像素风图标，共 5600+ 个、四种风格，做复古、游戏化或 8-bit 主题界面时用；其中 1000 多个免费（MIT），完整集需 Pro 授权 |  | `npm install pixelarticons`<br>llms.txt: https://pixelarticons.com/llms.txt | 免费+付费 |
| [Poline](https://meodai.github.io/poline/) | 在极坐标 HSL 空间的锚点之间「画线」取色的小型调色库，能程序化生成过渡自然、带点意外感的色板，适合生成式主题、数据可视化配色和创意编程；MIT |  | `npm i poline` | 开源 |
| [Practical Typography](https://practicaltypography.com) | Matthew Butterick 的在线排版书，「十分钟排版速成」和行长、行距、字号等规则被大量设计规范引用，给 Agent 写排版约束时可直接引用其结论；在线免费阅读（作者请求读者付费支持） |  |  | 免费 |
| [Programming Fonts](https://www.programmingfonts.org) | 上百款编程等宽字体的在线试用台，粘贴自己的代码、切换主题即可横向对比，给产品的代码块或终端组件挑字体时用；免费，⚠ 收录字体各有许可，下载前看清 |  |  | 免费 |
| [Radix Colors](https://www.radix-ui.com/colors) | 可访问性友好的色阶系统 |  |  | 免费 |
| [Radix Icons](https://www.radix-ui.com/icons) | Radix 团队的 15×15 小尺寸图标集，笔画干脆、像素对齐，专为按钮、菜单、表单等紧凑界面设计，搭配 Radix/shadcn 的密集型 UI 时用；MIT | React | `npm install @radix-ui/react-icons` | 开源 |
| [RandomA11y](https://randoma11y.com) | 不断随机生成满足对比度要求的双色组合，可按 WCAG 或 APCA 设阈值并投票收藏，想找既大胆又达标的文字/背景配色时用；免费 |  |  | 免费 |
| [React Icons](https://react-icons.github.io/react-icons/) | 把 Font Awesome、Material、Tabler、Remix、Simple Icons 等 30 多套流行图标集打包成统一的 React 组件，一个依赖按需引入任意图标，快速原型时最省事；⚠ 各图标集沿用自己的许可，用到品牌图标时注意商标 | React | `npm i react-icons` | 开源 |
| [Reasonable Colors](https://www.reasonable.work/colors/) | 一套开源的无障碍色彩系统，24 个色相各 6 级，色号差值直接对应对比度等级（差 2 级达 AA 大字、差 3 级达 AA、差 4 级达 AAA），不想自己算对比度时直接采用；MIT |  |  | 开源 |
| [SF Symbols](https://developer.apple.com/sf-symbols/) | Apple 官方的 6000+ 个系统符号，与 San Francisco 字体对齐并支持多色、分层和符号动画，做 iOS/macOS 原生应用时的标准图标；⚠ 许可只允许用于 Apple 平台上运行的应用，不能用在 Web、Android 或应用图标与 Logo 里 | SwiftUI, UIKit |  | 免费 |
| [ShadCN Themer](https://shadcnthemer.com) | shadcn/ui 主题的创建与分享社区，可浏览数千个社区主题，用 OKLCH 取色器调色、选 Google Fonts 和圆角后一键导出，想先看别人做的主题再改时用；免费 | shadcn/ui, Tailwind |  | 免费 |
| [Simple Icons](https://simpleicons.org) | 品牌图标 |  |  | 免费 |
| [Skill Icons](https://skillicons.dev) | 通过一条图片 URL 生成成排技术栈图标的服务，常用于 GitHub README 和个人主页，参数里列出技术名即可；免费开源（MIT） |  | https://skillicons.dev/icons?i=js,html,css,react&theme=light | 开源 |
| [Solar Icon Set](https://github.com/480-Design/Solar-Icon-Set) | 480 Design 的 7000+ 图标，同一图标有 Linear、Bold、Duotone、Broken、Outline 等六种风格，圆润现代，适合想要双色调或「断线」风格的产品；⚠ CC BY 4.0，需署名，也收录在 Iconify 的 solar 图标集 |  | `npm i @solar-icons/react`（社区） | 免费 |
| [Streamline](https://www.streamlinehq.com) | 规模最大的商业图标与插画库之一，几十套风格统一的系列（Core、Flex、Plump、像素、手绘等），大型产品需要上万个同风格图标时用；⚠ 免费图标须署名并链接 Streamline，免署名和完整套装需付费 |  |  | 免费+付费 |
| [Style Dictionary](https://styledictionary.com) | 设计令牌的构建系统，把一份 JSON 令牌转换成 CSS 变量、iOS、Android、JS 等各平台产物，兼容 DTCG 规范，多端共用一套设计系统时的标准工具；Apache-2.0 |  | `npm i style-dictionary` | 开源 |
| [StyleGlide](https://www.styleglide.ai) | 按项目描述用 AI 生成配色和字体风格的工具，结果以 shadcn 主题形式分发并可继续手调，不知道从哪种风格起步时用来出几个方向；可免费起步 | shadcn/ui, Tailwind |  | 免费+付费 |
| [SVG Credit Card & Payment Icons](https://github.com/aaronfagan/svg-credit-card-payment-icons) | 一套开源的银行卡与支付方式图标（Visa、Mastercard、Amex、PayPal、银联、支付宝、JCB 等），有扁平、圆角、Logo、单色、描边多种风格，结账页和页脚的「支持的支付方式」直接用；Apache-2.0，⚠ 商标归各品牌所有 |  |  | 开源 |
| [SVGL](https://svgl.app) | 品牌 Logo SVG，有公开 API | React, Tailwind | `npx shadcn@latest add @svgl/<logo>` | 免费 |
| [Tabler Icons](https://tabler.io/icons) | 6200+ 个 24px 描边图标（另有填充版），线宽可调、覆盖面比 Lucide 更广，后台和数据密集型产品找不到图标时首先换它；MIT，可商用免署名 | React, Vue, Svelte | `npm install @tabler/icons-react`<br>llms.txt: https://tabler.io/llms.txt | 开源 |
| [Tailwind CSS Colors](https://tailwindcss.com/docs/colors) | Tailwind 官方默认色板文档，20 多个色相各 11 级（v4 起以 OKLCH 定义），说明了命名、透明度修饰和自定义主题变量的写法，是 Agent 写 Tailwind 颜色类名的事实参照；免费 |  |  | 免费 |
| [The League of Moveable Type](https://www.theleagueofmoveabletype.com) | 最早的开源字体铸造厂，出品 League Gothic、League Spartan、Raleway、Ostrich Sans 等经典标题字体，想要有性格的开源展示字体时来挑；全部 OFL，可商用 |  |  | 开源 |
| [themux](https://themux.vercel.app) | 可完全自定义的 shadcn/ui 主题生成器，支持 Tailwind v4 与 v3、OKLCH 色值、字体和阴影等令牌的调整并实时预览，需要比官方主题页更细的控制时用；免费 | shadcn/ui, Tailwind |  | 免费 |
| [theSVG](https://thesvg.org) | 7600+ 个品牌 SVG 图标（另含 AWS、Azure、GCP、Kubernetes 架构图标），每个有彩色、单色、深浅色和文字标变体，并提供 npm 包、CLI、CDN 和 MCP，比 SVGL 更适合程序化批量取用；MIT，⚠ 商标归各品牌所有 |  | `npm i thesvg`<br>`npx -y @thesvg/mcp-server`<br>llms.txt: https://thesvg.org/llms.txt | 开源 |
| [tints.dev](https://www.tints.dev) | 输入一个品牌色生成 Tailwind 50–950 十一级色阶，可微调色相偏移、饱和度和亮度分布，并直接输出 Tailwind v3/v4 配置，给 Tailwind 项目加自定义主色时用；免费开源 |  | https://www.tints.dev/api/&lt;名称&gt;/&lt;hex&gt;（返回色阶 JSON） | 开源 |
| [Typescale](https://typescale.com) | 字号比例尺计算器，选基准字号和比例（大三度、纯四度、黄金比例等）即时预览标题到正文的层级，并导出 CSS，定字号阶梯时用；基础功能免费，另有 Pro |  |  | 免费+付费 |
| [Typewolf](https://www.typewolf.com) | 字体搭配与真实用例 |  |  | 免费 |
| [UI Colors](https://uicolors.app) | 生成 Tailwind 50–950 色阶 |  |  | 免费+付费 |
| [Uncut](https://uncut.wtf) | 当代风格的免费字体目录，偏实验性和编辑感的无衬线、衬线与展示字体，适合想避开「烂大街」字体的品牌和落地页；⚠ 收录的字体各有许可（多为 OFL 或可免费商用），下载页逐款标注 |  |  | 免费 |
| [unplugin-icons](https://github.com/unplugin/unplugin-icons) | 基于 Iconify 的按需图标方案，在 Vite、Next.js、Nuxt、Astro 等里用 import 路径把 20 万+ 图标中的任意一个编译成组件，只打包用到的图标，想自由混用多套图标集又不想装一堆依赖时用；MIT | Vite, Vue, React, Svelte | `npm i -D unplugin-icons` | 开源 |
| [Use & Modify](https://usemodify.com) | 一位设计师个人精选的自由字体合集，专挑「美、有格调、朋克、专业、不完整、怪异」的开源字体，找有个性的标题字时逛；全部为开源许可，可使用也可修改 |  |  | 免费 |
| [Utopia](https://utopia.fyi) | 流式响应设计的方法与计算器，按最小和最大视口各定一套比例，生成基于 clamp() 的流式字号与间距变量，不用断点就让排版随屏幕平滑缩放；免费 |  |  | 免费 |
| [Variable Fonts (v-fonts)](https://v-fonts.com) | 可变字体的检索与试玩站，每款字体都能直接拖动字重、字宽、倾斜等轴滑块，并标明来源和许可，找可变字体或理解某个轴的效果时用；免费 |  |  | 免费 |
| [Wakamai Fondue](https://wakamaifondue.com) | 把字体文件拖进浏览器就能看到它的全部能力：可变轴、OpenType 特性、支持的字符与语言，并生成对应的 CSS，拿到一款字体想知道「它能做什么」时用；免费，文件不上传 |  |  | 免费 |
| [Web3 Icons](https://web3icons.io) | 2500+ 个加密货币、公链、钱包和交易所的 SVG 与 React 图标，分品牌色、单色和背景版，做钱包、行情和 DeFi 界面时用；MIT，⚠ 商标归各项目所有 | React | `npm i @web3icons/react` | 开源 |
| [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) | 最常被引用的 WCAG 对比度检查器，输入前景和背景色即给出比值及 AA/AAA 各项是否通过，并有免 key 的 JSON API，适合让 Agent 自动核对配色；免费 |  | https://webaim.org/resources/contrastchecker/?fcolor=0000FF&bcolor=FFFFFF&api | 免费 |
| [Who Can Use](https://www.whocanuse.com) | 输入一组前景/背景色，展示它在各类色觉障碍和低视力情况下的实际观感与 WCAG 评级，并标注受影响人群比例，用来向团队直观说明对比度为什么重要；免费 |  |  | 免费 |
| [ZippyStarter Shadcn Theme Generator](https://zippystarter.com/tools/shadcn-ui-theme-generator) | 从一个主色或预设出发的 shadcn/ui 主题生成器，可细调各语义色、圆角和亮暗模式并实时预览组件，然后导出 CSS 变量，快速给 shadcn 项目换肤时用；免费 | shadcn/ui, Tailwind |  | 免费 |
| [配色辞典（和田三造）](https://sanzo-wada.dmbk.io) | 和田三造《配色辞典》的交互式网页版，收录 348 组经典的二色、三色、四色搭配，每个颜色可点开查看它参与的所有组合，想要有年代感、耐看的小配色时参考；免费 |  | llms.txt: https://sanzo-wada.dmbk.io/llms.txt | 免费 |

<a id="ui-media-assets"></a>

## 插画、3D、图片视频、样机、背景生成器、音效

素材用之前看描述里的授权说明（可商用 / 需署名 / 仅个人）。

本类分组：插画 · 3D 素材 · 图片与视频 · 样机与截图美化 · 背景与图案生成 · SVG 与动画素材 · 头像与占位 · 表情符号 · 音效 · 其他工具

### 插画

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [unDraw](https://undraw.co) | 可在线改主色的扁平风 SVG 插画库，空状态、引导页、落地页配图的默认选择；可商用免署名，⚠ 不得打包再分发、做同类站或用于机器学习训练 |  | 免费 |
| [Absurd Design](https://absurd.design) | 超现实手绘黑白插画，气质怪诞有辨识度，适合不想要「标准 SaaS 插画」的品牌；⚠ 免费素材须按其许可条款署名，会员素材另行授权 | llms.txt: https://absurd.design/llms.txt | 免费+付费 |
| [Blush](https://blush.design) | 汇集多位插画师作品的可定制插画平台，可逐个部件随机组合并有 Figma/Sketch 插件，适合要「每张都不一样」的成套插画；免费版可商用但只有 PNG，SVG 与高清导出需付费 |  | 免费+付费 |
| [DrawKit](https://www.drawkit.com) | 按主题打包的 2D/3D 插画与图标集，适合一次拿齐某个行业（电商、金融、教育）的整套配图；免费包可商用免署名，⚠ 不得转售或再分发素材本身，部分包需 Pro |  | 免费+付费 |
| [Humaaans](https://www.humaaans.com) | 可混搭发型、上衣、裤子和姿势的扁平人物插画库，适合做团队、用户场景类配图；CC0，可商用免署名 |  | 免费 |
| [illlustrations](https://illlustrations.co) | 设计师 vijay verma 的插画站，含早期「100 天插画」开源包和新的在线角色构建器；⚠ 只有明确标注 CC0 的旧包可随意商用，新素材与构建器资源适用其付费许可 | llms.txt: https://illlustrations.co/llms.txt | 免费+付费 |
| [IRA Design](https://iradesign.io) | Creative Tim 的渐变风插画组件，人物、物件、背景可自由拼装并选 5 种渐变配色，适合快速拼出 SaaS 风 Hero 图；MIT，可商用 |  | 免费 |
| [Lukasz Adam Illustrations](https://lukaszadam.com/illustrations) | 一位设计师持续更新的免费 SVG 插画集，风格统一、体积小，适合个人项目和博客配图；CC0，可商用免署名 |  | 免费 |
| [ManyPixels Illustration Gallery](https://www.manypixels.co/gallery) | 数千张可改主色的免费插画，分等距、扁平、线条等多种风格，适合 unDraw 用腻后的替代；可商用免署名，⚠ 不得打包再分发 |  | 免费 |
| [Open Doodles](https://www.opendoodles.com) | 一套松弛的手绘涂鸦人物，提供 SVG/PNG/GIF 并可在线换色，适合轻松随意的品牌调性；可商用免署名（CC0） |  | 免费 |
| [Open Peeps](https://www.openpeeps.com) | Pablo Stanley 的手绘黑白人物库，头、身体、表情像积木一样自由组合，适合需要「真人感」但不想用照片的页面；CC0，可商用免署名 |  | 免费 |
| [Ouch! (Icons8)](https://icons8.com/illustrations) | Icons8 的插画库，按风格成套（3D、手绘、线条…）且每套都覆盖 404、空状态、成功、报错等常见 UX 场景；⚠ 免费仅 PNG 且须加 Icons8 链接署名，SVG 和免署名需付费 |  | 免费+付费 |
| [Storyset](https://storyset.com) | Freepik 出品的可定制插画，能在线改色、换背景、隐藏图层并导出带动画的版本，适合要成套风格的营销页；⚠ 免费使用需署名 Storyset/Freepik，免署名要付费订阅 |  | 免费+付费 |
| [Transhumans](https://www.transhumans.xyz) | 朋克科幻风人物插画（机械义肢、赛博元素），适合科技、AI 或另类调性的页面配图；CC0，可商用免署名 |  | 免费 |

### 3D 素材

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Poly Haven](https://polyhaven.com) | 高质量 HDRI 环境贴图、PBR 材质和 3D 模型库，做 three.js/R3F 场景打光和材质时首选；全部 CC0，可商用免署名，并有免 key 公开 API |  | https://api.polyhaven.com/assets?t=hdris（免 key<br>t 可为 hdris/textures/models）<br>llms.txt: https://polyhaven.com/llms.txt | 免费 |
| [3dicons](https://3dicons.co) | 200 个统一风格的 3D 图标（1400+ 张多角度、多配色渲染图），提供 PNG、Blender 源文件和 Figma 文件，适合给落地页或功能卡片加立体点缀；CC0，可商用免署名 |  |  | 免费 |
| [ambientCG](https://ambientcg.com) | 数千套 PBR 材质、HDRI 和扫描模型，适合需要大量地面、墙面、金属等写实材质时批量下载；全部 CC0，可商用免署名 |  | https://ambientcg.com/api/v2/full_json?limit=10（公开 API，文档 https://docs.ambientcg.com/api/） | 免费 |
| [glTF Sample Assets](https://github.com/KhronosGroup/glTF-Sample-Assets) | Khronos 官方的 glTF 示例模型集（头盔、材质球、动画角色等），用来测试渲染器、材质扩展和加载流程；⚠ 每个模型许可不同（CC0/CC-BY 等），目录里逐个标注 |  |  | 开源 |
| [glTF Transform](https://gltf-transform.dev) | glTF/GLB 的命令行与 SDK 优化工具：Draco/Meshopt 压缩、贴图转 WebP/KTX2、去重、合并、检查，模型上线前减体积用；MIT 开源，在线检查版是 gltf.report |  | `npm install --global @gltf-transform/cli` | 开源 |
| [gltfjsx](https://github.com/pmndrs/gltfjsx) | 把 GLTF/GLB 模型转成可直接使用的 React Three Fiber JSX 组件，并可顺带压缩（--transform），在 R3F 项目里引入任何下载来的模型时用；MIT 开源，另有免安装在线版 gltf.pmnd.rs | React, three.js | `npx gltfjsx model.glb --transform` | 开源 |
| [Handz](https://www.handz.design) | 一套多肤色、多手势的 3D 手部渲染图和 Blender 源文件，适合做手持、点击、指向类的插图；免费版可个人和商用，⚠ 不得再分发素材本身 |  | llms.txt: https://www.handz.design/llms.txt | 免费+付费 |
| [Kenney](https://kenney.nl/assets) | 游戏素材宝库：低多边形 3D 模型、2D 精灵、UI 元素包以及界面音效包，适合游戏化界面、原型和小游戏；全部 CC0，可商用免署名 |  |  | 免费 |
| [Mixamo](https://www.mixamo.com) | Adobe 的免费角色自动绑骨与动作库，上传人形模型即可套用上千个动作并导出 FBX，适合给 3D 角色加走跑跳动画；登录 Adobe 账号后免费、可商用，⚠ 不得单独再分发动作/角色文件 |  |  | 免费 |
| [Poly Pizza](https://poly.pizza) | 上万个低多边形 3D 模型的搜索站（收录了 Google Poly、Quaternius、Kenney 等来源），可直接下载 GLB/FBX；⚠ 逐个模型标注 CC0 或 CC-BY，后者需署名，另有需申请 key 的 API |  |  | 免费 |
| [Quaternius](https://quaternius.com) | 成套的低多边形 3D 模型包（角色、自然、建筑、载具，多数带骨骼动画），风格统一，适合 three.js 小场景和游戏原型；CC0，可商用免署名 |  |  | 免费 |
| [Sketchfab](https://sketchfab.com) | 最大的在线 3D 模型平台，可筛选「可下载」模型并嵌入交互式查看器，适合找特定物件的写实模型；⚠ 许可逐个模型不同（多为 CC-BY 需署名，也有 NC 禁商用），下载前看清 |  | https://api.sketchfab.com/v3/search?type=models&q=chair&downloadable=true（搜索免 key，下载需 OAuth token） | 免费+付费 |
| [Spline Community](https://community.spline.design) | Spline 官方社区库，成千上万个可一键 Remix 的交互式 3D 场景和模板，适合找现成的 3D Hero 再改色改文案；浏览免费，商用和导出权限取决于各作品设置与自己的 Spline 套餐 |  | llms.txt: https://community.spline.design/llms.txt | 免费+付费 |
| [Thiings](https://www.thiings.co) | 1.3 万+ 个 AI 生成的 3D 风格物件图标（PNG），风格统一、可按物件名检索，适合做情绪板和个人项目点缀；⚠ 免费许可仅限个人非商用且须署名，商用要买授权 |  |  | 免费+付费 |
| [腾讯混元 3D](https://3d.hunyuan.tencent.com) | 腾讯的文生/图生 3D 创作平台，中文提示词友好，适合国内网络环境下快速出模型；网页版有免费额度，底层 Hunyuan3D 模型也已开源，⚠ 产物商用条款以平台协议为准 |  |  | 免费+付费 |

### 图片与视频

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [Burst (Shopify)](https://www.shopify.com/stock-photos) | Shopify 的免费商品与生活方式图库，电商、餐饮、时尚类题材多，做店铺和商品落地页 Demo 时用；可商用免署名 |  | 免费 |
| [Coverr](https://coverr.co) | 专做网页背景视频的免费素材库，片段短、循环自然，适合 Hero 区视频背景；库内素材可商用，并提供免费 API（需 key，50 次/小时）和 MCP 接入 | https://api.coverr.co/videos?query=city+sunset&page_size=3&api_key=YOUR_KEY（文档 https://api.coverr.co/docs） | 免费+付费 |
| [Lummi](https://www.lummi.ai) | Pablo Stanley 团队的 AI 生成免费图库（照片、插画、3D 风格），画面统一干净，适合找不到合适实拍时的抽象或概念配图；可个人和商用、免署名，⚠ 不得原样打包转售 | llms.txt: https://www.lummi.ai/llms.txt | 免费+付费 |
| [Mixkit](https://mixkit.co) | Envato 的免费素材站，主打视频片段、背景音乐、音效和视频模板，适合做落地页背景视频和产品演示配乐；按 Mixkit 免费许可可商用免署名，⚠ 无公开 API，个别条目标注为限制性许可 | llms.txt: https://mixkit.co/llms.txt | 免费 |
| [Nappy](https://nappy.co) | 以黑人和棕色人种为主角的高质量免费图库，需要更多元的人物形象时补充 Unsplash；CC0，可商用免署名 |  | 免费 |
| [Openverse](https://openverse.org) | WordPress 基金会维护的开放版权搜索引擎，聚合 8 亿+ CC 协议和公有领域的图片与音频，适合需要明确许可出处时检索；API 可匿名调用，⚠ 每条结果许可不同（CC0/BY/BY-SA/NC…），按返回的 license 字段处理署名 | https://api.openverse.org/v1/images/?q=mountain&license=cc0,by（匿名可用，有速率限制） | 免费 |
| [Pexels](https://www.pexels.com) | 同时提供免费照片和视频的图库，需要背景视频或人物生活类素材时用；可商用免署名，API 免费（需 key，默认 200 次/小时），⚠ 通过 API 展示时要标注来源 Pexels | https://api.pexels.com/v1/search?query=nature（Header 带 Authorization: YOUR_API_KEY<br>视频用 /videos/search） | 免费 |
| [Pixabay](https://pixabay.com) | 品类最全的免费素材站：照片、插画、矢量图、视频、音乐和音效都有，适合一站式找齐；可商用免署名（Pixabay Content License），有免费 API | https://pixabay.com/api/?key=YOUR_API_KEY&q=yellow+flowers&image_type=photo（视频用 /api/videos/<br>文档 https://pixabay.com/api/docs/） | 免费 |
| [Unsplash](https://unsplash.com) | 质量最高的免费摄影图库，Hero 图、背景和文章配图的默认来源；可商用免署名（不得原样售卖或做同类图库），API 免费申请，⚠ API 调用须热链接原图并署名摄影师，演示级限 50 次/小时 | https://api.unsplash.com/search/photos?query=office&client_id=YOUR_ACCESS_KEY（需免费 Access Key，文档 https://unsplash.com/developers） | 免费+付费 |

### 样机与截图美化

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [AppMockUp Studio](https://app-mockup.com) | 免费的应用商店截图设计器，内置各尺寸设备外框、多屏连排画布和文案排版，适合独立开发者直接出 App Store/Google Play 上架图 |  | llms.txt: https://app-mockup.com/llms.txt | 免费 |
| [BrowserFrame](https://browserframe.com) | 专门给截图套浏览器窗口外框的小工具，可选多种浏览器样式和深浅色，只想要一个「浏览器壳」时最快；免费 |  |  | 免费 |
| [Cap](https://cap.so) | 开源的 Loom 替代品，录屏后可加背景、圆角、光标效果并生成分享链接，支持自托管，适合不想付 Screen Studio 或需要跨平台时用；桌面端免费，云端功能付费 |  | llms.txt: https://cap.so/llms.txt | 免费+付费 |
| [Carbon](https://carbon.now.sh) | 老牌开源代码截图工具，主题和窗口样式可调，配合社区 CLI 可在终端直接把文件转成图片，适合脚本化批量出图；MIT 开源 |  | `npx carbon-now-cli <file>`（社区 CLI） | 开源 |
| [CodeImage](https://codeimage.dev) | 开源的代码截图编辑器，支持多标签窗口、终端样式、自定义字体与主题预设，比 Carbon 更可调；免费，MIT 开源 |  |  | 开源 |
| [Devices.css](https://devicescss.xyz) | 纯 CSS 画的现代设备外框（iPhone、iPad、MacBook、Apple Watch、Pixel 等），直接在页面里把真实组件或截图放进设备框，不用图片样机；MIT 开源 | CSS | `npm i devices.css` | 开源 |
| [MockUPhone](https://mockuphone.com) | 上传截图一键套进各代 iPhone、Android、iPad、电视等设备外框并打包下载，适合批量生成纯设备图；免费 |  |  | 免费 |
| [Mockuuups Studio](https://mockuuups.studio) | 5000+ 个真实场景设备样机（手持、桌面、户外）的生成器，有 Figma/Sketch 插件和桌面端，适合要「实拍感」的营销图；生成图可商用免署名，按次或订阅付费解锁完整库 |  |  | 免费+付费 |
| [Pika](https://pika.style) | 截图美化工具，给截图加背景、圆角、阴影、浏览器或设备外框，也能把代码、推文做成图片并生成 OG 图；免费版带小水印，去水印和 4K 导出需 Pro |  | llms.txt: https://pika.style/llms.txt | 免费+付费 |
| [PostSpark](https://postspark.app) | 截图与社媒图片美化工具，支持设备外框、背景、标注和把推文/代码转成图片，适合批量做风格统一的社媒配图；免费可用，高级功能付费 |  | llms.txt: https://postspark.app/llms.txt | 免费+付费 |
| [Previewed](https://previewed.app) | App 展示图生成器，有 2D/3D 设备模板和动画导出，适合做应用商店预览图和推广图；⚠ 免费版仅 720p 且须署名（CC 署名许可），商用和高清需一次性付费或订阅 |  |  | 免费+付费 |
| [ray.so](https://ray.so) | Raycast 出品的代码截图工具，选主题、语言和内边距后导出漂亮的代码图片，写文档、发推介绍代码片段时用；免费 |  |  | 免费 |
| [Rotato](https://rotato.app) | macOS 上的 3D 设备样机与动画工具，把截图或录屏贴到可旋转的 3D 手机/电脑上并导出 4K 视频，做产品宣传片时用；可免费上手，完整导出需付费授权 |  | llms.txt: https://rotato.app/llms.txt | 免费+付费 |
| [Screen Studio](https://screen.studio) | macOS 录屏工具，自动跟随光标缩放、平滑鼠标轨迹并加背景与设备外框，产品演示视频和功能 GIF 的事实标准；付费订阅 |  | llms.txt: https://screen.studio/llms.txt | 付费 |
| [Screenshot.Rocks](https://screenshot.rocks) | 免登录的在线截图套壳工具，贴图或输入网址即可套浏览器/手机外框并换背景，适合文档和博客里快速出一张干净截图；免费 |  | llms.txt: https://screenshot.rocks/llms.txt | 免费 |
| [Shots](https://shots.so) | 浏览器里的截图样机工具，拖入截图即可套 iPhone/MacBook/浏览器外框、加渐变背景和 3D 倾角，还能导出动画，做产品发布图和社媒配图时首选；基础功能免费，部分样机与高清导出需 Pro |  |  | 免费+付费 |
| [Xnapper](https://xnapper.com) | macOS 截图应用，截完自动居中、配背景、加圆角并可一键打码敏感信息，适合高频发截图的人；免费可用但带水印，一次性付费去除 |  |  | 免费+付费 |

### 背景与图案生成

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Haikei](https://haikei.app) | 一站式 SVG 背景素材生成器：波浪、Blob、叠层波、渐变光斑、低多边形、分隔线等十几种，调参后导出 SVG/PNG，落地页需要装饰背景时首选；基础生成器免费、免注册，产物可商用 |  |  | 免费+付费 |
| [bg.ibelick](https://bg.ibelick.com) | ibelick 整理的即用型背景片段（网格、点阵、聚光渐变），点一下复制 Tailwind 代码，适合暗色 SaaS 落地页的 Hero 背景；免费 | Tailwind |  | 免费 |
| [BGJar](https://bgjar.com) | 免费的 SVG 背景生成器，提供流星、电路板、等高线、波浪、低多边形等数十种风格，随机后下载 SVG/PNG，适合快速要一张科技感背景；免费 |  |  | 免费 |
| [Blobmaker](https://www.blobmaker.app) | 随机有机形状（Blob）SVG 生成器，调复杂度和对比度即可得到不规则色块，做头像底、装饰色斑时用；免费（现已并入 Haikei） |  |  | 免费 |
| [Clippy](https://bennettfeely.com/clippy/) | CSS clip-path 可视化编辑器，内置多边形、箭头、星形等预设并可拖点自定义，做斜切区块、异形图片裁剪时用；免费 |  |  | 免费 |
| [Color4Bg](https://www.color4bg.com) | 抽象彩色背景生成器，提供模糊渐变、环境光、流动曲线等多种 WebGL 风格，可导出静态图或作为 JS 库嵌入做动态背景；免费 |  | llms.txt: https://www.color4bg.com/llms.txt | 免费 |
| [CSS Gradient](https://cssgradient.io) | 可视化 CSS 渐变编辑器，支持线性/径向、多色标和透明度，并附渐变色卡与教程，手调渐变参数时用；免费 |  |  | 免费 |
| [CSS Pattern](https://css-pattern.com) | Temani Afif 用纯 CSS 渐变写出的 150+ 种背景图案（棋盘、之字、六边形、编织等），无图片无 SVG，可用 CSS 变量调尺寸颜色；免费 |  |  | 免费 |
| [css-doodle](https://css-doodle.com) | 用 CSS 规则在网格上生成图案和生成艺术的 Web Component，几行代码就能写出随机纹样和动画背景，想要代码生成、每次刷新都不同的背景时用；MIT 开源 |  | `npm i css-doodle`<br>llms.txt: https://css-doodle.com/llms.txt | 开源 |
| [Fancy Border Radius](https://9elements.github.io/fancy-border-radius/) | 八值 border-radius 可视化工具，拖手柄就能得到有机 Blob 形状的 CSS，不用 SVG 也能做不规则色块和头像框；免费 |  |  | 免费 |
| [fffuel](https://www.fffuel.co) | 几十个小而美的 SVG 生成器合集（噪点 nnnoise、流体渐变、网格、扭曲线条、光斑、有机形状等），做颗粒质感、极光背景这类流行效果时来这里找；免费，生成的图像可个人和商用 |  |  | 免费 |
| [Get Waves](https://getwaves.io) | SVG 波浪生成器，调波峰数量、曲线类型和颜色后导出，专门用来做区块之间的波浪形分隔；免费 |  |  | 免费 |
| [gradient.style](https://gradient.style) | Adam Argyle 做的现代 CSS 渐变编辑器，支持 OKLCH/Display-P3 等广色域色彩空间和插值方式，想要更鲜艳、中间不发灰的 HDR 渐变时用；免费 |  |  | 免费 |
| [Hero Patterns](https://heropatterns.com) | Steve Schoger 的可平铺 SVG 背景纹样集，选前景/背景色和透明度后直接复制 CSS 的 background-image，适合给大色块加细腻底纹；⚠ CC BY 4.0，需署名 |  |  | 免费 |
| [MagicPattern](https://www.magicpattern.design) | 30+ 个设计小工具合集（CSS 背景纹样、网格渐变、Blob、噪点、几何图形、涂鸦等），想在一个站里把装饰素材配齐时用；⚠ 免费可试用，无限导出和商用授权需订阅 |  |  | 免费+付费 |
| [Mesher (CSS Hero)](https://csshero.org/mesher/) | 纯 CSS 的弥散/网格渐变生成器，拖动色点即可得到多层 radial-gradient 代码，适合不想上 WebGL 的柔和渐变背景；免费 |  |  | 免费 |
| [NEAT](https://neat.rebase.pro) | 基于 WebGL 的 3D 流动渐变背景生成器，在线调色调形后导出配置，用很小的库在页面里渲染 60fps 动态渐变；⚠ MIT + Commons Clause，免费使用会带 NEAT 标记，去除需按域名一次性付费 |  | `npm install @firecms/neat`<br>llms.txt: https://neat.rebase.pro/llms.txt | 免费+付费 |
| [Pattern Monster](https://pattern.monster) | 数百个可调的 SVG 平铺纹样，可改颜色、描边、缩放、角度后导出 SVG/CSS，适合需要几何感底纹时挑选；免费 |  |  | 免费 |
| [pattern.css](https://bansal.io/pattern-css) | 只有 CSS 的背景图案库，用类名（pattern-dots-md、pattern-diagonal-lines-sm…）给元素或图片叠加纹样，适合给色块和图片加波普感装饰；MIT 开源 | CSS | `npm i pattern.css` | 开源 |
| [PatternCraft](https://patterncraft.fun) | 一组现代背景片段（点阵、网格、径向光晕、极光渐变等），每个都能复制 Tailwind/CSS 代码，给 shadcn 风页面加背景时直接粘贴；免费，MIT 开源 | Tailwind, CSS |  | 开源 |
| [PatternPad](https://patternpad.com) | 参数化的图案生成器，可无限随机出品牌感图案并导出 PNG/JPG/SVG，适合做演示文稿、社媒和品牌延展图形；免费，⚠ 商用须署名并链接 PatternPad，且不得转售图案本身 |  |  | 免费 |
| [Shape Divider App](https://www.shapedivider.app) | 区块分隔形状生成器（波浪、斜切、曲线、三角、箭头等），直接给出可粘贴的 HTML+CSS，做落地页上下区块的异形过渡时用；免费 |  |  | 免费 |
| [Subtle Patterns (Toptal)](https://www.toptal.com/designers/subtlepatterns/) | 老牌的低调平铺纹理库，全是不抢戏的浅色/深色细纹，适合正文区背景和卡片底纹；免费，可商用 |  |  | 免费 |
| [SVG Backgrounds](https://www.svgbackgrounds.com) | 可调色的 SVG 背景与纹样库，一键复制内联 CSS，体积极小，适合不想引入图片文件的全屏背景；⚠ 免费素材使用时须署名，订阅后免署名并解锁全部 |  |  | 免费+付费 |
| [Transparent Textures](https://www.transparenttextures.com) | 数百张半透明 PNG 纹理（纸纹、布纹、噪点、金属拉丝等），叠在任意背景色上使用，做纸张感、复古质感时用；免费 |  |  | 免费 |
| [Trianglify](https://trianglify.io) | 低多边形（三角网格）背景生成器，可在线调色和网格密度导出 SVG/PNG，也可作为库在代码里生成；在线生成免费，⚠ 库为 GPL-3.0，闭源项目内嵌需另购商业授权 |  | `npm i trianglify` | 免费+付费 |
| [uiGradients](https://uigradients.com) | 社区投稿的双色/多色线性渐变合集，每个渐变有名字，可复制 CSS 或下载图片，适合快速挑一个顺眼的渐变；MIT 开源，可商用 |  |  | 开源 |
| [WebGradients](https://webgradients.com) | 180 个精选线性渐变，全部带名称，可一键复制 CSS 或下载 PNG，适合当作渐变色板直接取用；免费，可商用 |  | llms.txt: https://webgradients.com/llms.txt | 免费 |

### SVG 与动画素材

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [Animated Icons](https://animatedicons.co) | 4000+ 个可改色的动画图标，提供 Lottie、SVG、PNG 等格式，数量多、覆盖业务场景广；免费图标可个人和商用且免署名，完整库需付费 |  |  | 免费+付费 |
| [Boxy SVG](https://boxy-svg.com) | 跑在浏览器里的 SVG 矢量编辑器，界面干净、直接读写标准 SVG 且可查看元素源码，适合不想开 Figma/Illustrator 时改图标和插画；付费订阅，有试用期 |  |  | 付费 |
| [CSS Loaders](https://css-loaders.com) | Temani Afif 的 600+ 个单元素纯 CSS 加载动画，按 spinner、点、进度条、形状等分类，点开即复制代码；免费 |  |  | 免费 |
| [dotLottie Web](https://github.com/LottieFiles/dotlottie-web) | LottieFiles 官方的新一代播放器（Rust + WASM 渲染），支持 .lottie 压缩格式、主题和状态机交互，并有 React/Vue/Svelte/Web Component 封装，在网页里播放 Lottie 的推荐方式；MIT 开源 | React, Vue, Svelte | `npm i @lottiefiles/dotlottie-react` | 开源 |
| [heroicons-animated](https://www.heroicons-animated.com) | 316 个带 Motion 动画的 Heroicons，做法同 lucide-animated，通过 shadcn CLI 把单个图标源码装进项目，用 Heroicons 的项目想加 hover 动效时选它；MIT 开源 | React, Motion | `npx shadcn@latest add @heroicons-animated/<icon>`<br>llms.txt: https://www.heroicons-animated.com/llms.txt | 开源 |
| [IconScout](https://iconscout.com) | 综合素材市场：图标、插画、3D 素材和 Lottie 动画都有，数量巨大且有 Figma 等插件，适合需要同一风格成套素材时检索；⚠ 免费素材数量有限且各条目许可不同，多数高质量资源需订阅 |  |  | 免费+付费 |
| [Its Hover](https://www.itshover.com) | 一组「动效优先」的开源动画图标，每个都是可编辑的 React + Motion 组件，含不少 AI 与品牌 Logo 的动效版，经 shadcn CLI 按需安装；免费开源 | React, Motion | `npx shadcn@latest add https://itshover.com/r/<icon-name>.json` | 开源 |
| [Lordicon](https://lordicon.com) | 近 5 万个动画图标，分线条、扁平、渐变等风格，可设 hover/click/loop 触发并导出 Lottie、GIF、SVG，适合给功能卡片和导航加动态图标；⚠ 免费图标为 CC BY-ND（须署名、不得改动），Pro 订阅免署名 |  | `npm i @lordicon/react` | 免费+付费 |
| [LottieFiles 免费动画库](https://lottiefiles.com/free-animations) | 最大的 Lottie 动画社区库，加载、成功、空状态、404、庆祝等场景应有尽有，可在线改色后导出 JSON/dotLottie；公开的免费动画按 Lottie Simple License 可商用、免署名，⚠ 标注 Premium 的需订阅 |  | `npm i @lottiefiles/dotlottie-react`<br>llms.txt: https://lottiefiles.com/llms.txt | 免费+付费 |
| [Lottielab](https://www.lottielab.com) | 浏览器里的 Lottie 动画编辑器，可导入 Figma/SVG 后加关键帧并直接导出 Lottie，不会 After Effects 也能自己做或修改动画；有免费档 |  |  | 免费+付费 |
| [Meteocons](https://meteocons.com) | 一整套带动画的天气图标（晴雨雪雷、月相、风力、紫外线等），提供 SVG 与 Lottie、彩色与单色版本，做天气卡片和仪表盘时用；MIT，可商用 |  | `npm install @meteocons/svg` | 开源 |
| [Recraft](https://www.recraft.ai) | 能直接生成可编辑 SVG 矢量图的 AI 设计工具，可锁定品牌风格批量出图标、插画和 Logo，并提供 API 与官方 MCP；⚠ 免费版生成的图归 Recraft 所有、公开展示且不可商用，商用需付费套餐 |  | `claude mcp add --transport http recraft https://mcp.recraft.ai/mcp`<br>llms.txt: https://www.recraft.ai/llms.txt | 免费+付费 |
| [Rive Marketplace](https://rive.app/marketplace/) | Rive 官方社区与市场，可预览并 Remix 带状态机的交互动画（按钮、开关、角色、加载器），想要能响应输入的动画而不是定时播放的 Lottie 时来这里找；社区文件多为 CC BY 许可（需署名），以各文件页标注为准 |  | `npm i @rive-app/react-canvas`<br>llms.txt: https://rive.app/llms.txt | 免费+付费 |
| [SVG Artista](https://svgartista.net) | 粘贴 SVG 即生成「描边绘制 + 填充渐显」的 CSS 动画代码，做 Logo 手写入场、线稿自绘效果时用；免费 |  |  | 免费 |
| [SVG Repo](https://www.svgrepo.com) | 50 万+ 免费 SVG 图标与矢量图的搜索库，可在线改色、调描边并导出 React 组件，找零散的单个图形时用；⚠ 每个素材许可不同（CC0、MIT、CC BY 等），详情页逐个标注 |  |  | 免费 |
| [SVG Spinners](https://github.com/n3r4zzurr0/svg-spinners) | 一组 24×24 的纯 SVG 加载动画（SMIL/CSS 实现，无需 JS），圆环、点阵、条形、脉冲等几十种，也收录在 Iconify 的 svg-spinners 图标集里；MIT 开源 |  |  | 开源 |
| [SVG Viewer](https://www.svgviewer.dev) | 在线 SVG 查看与转换工具：粘贴代码即预览，可一键优化并转成 React/React Native 组件、Data URI 或 PNG，调试 AI 生成的 SVG 时很顺手；免费 |  |  | 免费 |
| [SVGator](https://www.svgator.com) | 在线 SVG 动画制作工具，时间轴式编辑，可导出带 CSS/JS 的动画 SVG 或 Lottie，适合给插画和图标做路径变形、交互触发动画；免费版有导出数量和功能限制 |  |  | 免费+付费 |
| [SVGOMG / SVGO](https://svgomg.net) | SVGO 的可视化界面：粘贴或拖入 SVG，逐项开关优化选项并实时看体积与效果，设计稿导出的 SVG 上线前都该过一遍；免费开源，批量处理用 SVGO 命令行 |  | `npm i -D svgo` | 开源 |
| [SvgPathEditor](https://yqnn.github.io/svg-path-editor/) | 在线编辑 SVG path 的 d 属性：可视化拖点、缩放平移、相对/绝对坐标互转和精度取整，手改或排查某条路径时用；免费，Apache-2.0 开源 |  |  | 开源 |
| [SVGR](https://react-svgr.com) | 把 SVG 转成 React 组件的工具链，有在线 Playground、CLI 以及 Vite/webpack/Next.js 插件，项目里要把一批 SVG 图标变成可传 props 的组件时用；MIT 开源 | React | `npx @svgr/cli --out-dir dist -- icons` | 开源 |
| [URL-encoder for SVG](https://yoksel.github.io/url-encoder/) | 把 SVG 代码转成可直接写进 CSS background-image 的 data URI（比 base64 更小），需要把图标或纹样内联进样式表时用；免费 |  |  | 免费 |
| [useAnimations](https://useanimations.com) | 300 个手工制作的微动效图标（菜单变关闭、播放暂停、点赞、加载等），内置 hover/click/loop 交互，可当 React 组件用或经 shadcn CLI 安装；MIT，可商用 | React | `npm install react-useanimations`<br>`npx shadcn@latest add https://useanimations.com/r/checkmark.json`<br>llms.txt: https://useanimations.com/llms.txt | 免费 |
| [VTracer](https://www.visioncortex.org/vtracer/) | 开源的位图转矢量工具，能把彩色 PNG/JPG（含像素画、AI 生成的 Logo）描成多层 SVG，效果比 Potrace 更适合彩色图；免费，有在线版、命令行和 Python 包 |  | cargo install vtracer-cli | 开源 |

### 头像与占位

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [DiceBear](https://www.dicebear.com) | 开源头像生成库与免 key HTTP API，60 多种风格（像素、首字母、卡通人物、几何图形…），同一 seed 永远得到同一张 SVG，给用户列表和评论区生成默认头像的首选；代码 MIT，⚠ 各风格美术许可不同（CC0、CC BY 等），商用前看风格页 |  | https://api.dicebear.com/10.x/&lt;style&gt;/svg?seed=&lt;任意字符串&gt;<br>`npm install @dicebear/core @dicebear/styles`<br>llms.txt: https://www.dicebear.com/llms.txt | 开源 |
| [Avvvatars](https://avvvatars.com) | 轻量的 React 头像组件，按传入的邮箱或用户名生成唯一的首字母色块或几何形状头像，后台和 SaaS 用户列表里即插即用；MIT 开源 | React | `npm i avvvatars-react` | 开源 |
| [BlurHash](https://blurha.sh) | 把图片编码成二三十个字符的字符串，前端解码成模糊色块作为加载占位，图片多的瀑布流和卡片列表想避免空白闪烁时用；MIT 开源，各语言都有实现 |  | `npm i blurhash` | 开源 |
| [Boring Avatars](https://boringavatars.com) | 根据用户名和调色板生成抽象 SVG 头像的小型 React 组件（marble、beam、pixel、sunset、ring、bauhaus 六种），想要有设计感且与品牌色一致的默认头像时用；MIT 开源 | React | `npm install boring-avatars` | 开源 |
| [Doodle Ipsum](https://doodleipsum.com) | Blush 出品的「插画版 Lorem Ipsum」，用 URL 取随机手绘插画作占位，可选风格、尺寸和背景色，原型里需要插画位又还没定稿时用；免费，素材适用 Blush 许可 |  | https://doodleipsum.com/700/flat | 免费 |
| [Facehash](https://www.facehash.dev) | 把任意字符串变成一张带表情的极简小脸头像的 React 组件，确定性生成、无需网络请求，适合 Agent、机器人和匿名用户的默认头像；MIT 开源 | React | `npm install facehash` | 开源 |
| [Logoipsum](https://logoipsum.com) | 200 多个免费的占位 Logo（SVG），用来填「客户 Logo 墙」「合作伙伴」区块，避免在 Demo 里误用真实品牌商标；免费，可随意使用 |  |  | 免费 |
| [Lorem Picsum](https://picsum.photos) | 返回随机真实照片的占位图服务（图源为 Unsplash），支持固定 id/seed、灰度和模糊，需要「看起来像真图」的占位时用；免费、免 key，⚠ 只适合占位和 Demo |  | https://picsum.photos/200/300<br>https://picsum.photos/seed/&lt;seed&gt;/800/600 | 免费 |
| [Notion Avatar Maker](https://notion-avatar.app) | 在线拼装 Notion 风格的黑白手绘头像，可选脸型、发型、配饰后导出 PNG/SVG，适合团队介绍页和个人主页；CC0，可商用免署名 |  |  | 免费 |
| [Placehold](https://placehold.co) | 最简单的占位图服务，URL 里写尺寸即可，还能指定颜色、文字、字体和格式（SVG/PNG/WebP/AVIF），布局阶段替代未到位的图片；免费、免 key |  | https://placehold.co/600x400<br>https://placehold.co/600x400/000000/FFF?text=Hello | 免费 |
| [Pravatar](https://pravatar.cc) | 返回随机真人头像照片的占位服务，可指定尺寸、编号或按邮箱固定同一张，做原型和 Demo 数据时用；免费（CC0），⚠ 仅适合占位，不要用于正式产品的真实用户 |  | https://i.pravatar.cc/150?img=3 | 免费 |
| [Random User Generator](https://randomuser.me) | 生成随机用户资料（姓名、邮箱、地址、头像照片）的免费 JSON API，可指定数量、国籍和 seed，给列表、表格和个人页填充逼真的假数据时用；免费、免 key |  | https://randomuser.me/api/?results=10 | 免费 |
| [ThumbHash](https://evanw.github.io/thumbhash/) | esbuild 作者做的图片占位编码，和 BlurHash 同样大小但细节更多、保留宽高比并支持透明通道，新项目做模糊占位时优先考虑；MIT 开源 |  | `npm i thumbhash` | 开源 |
| [UI Avatars](https://ui-avatars.com) | 按姓名首字母生成头像图片的免费 API，URL 参数可控背景色、字色、尺寸和圆角，不想装任何依赖时当头像回退图用；免费、免 key |  | https://ui-avatars.com/api/?name=John+Doe&background=random | 免费 |
| [UI Faces](https://uifaces.co) | AI 生成的头像合集（真人风、卡通、外星人、抽象），用于设计稿和原型里的用户头像，有 Figma 插件；⚠ 免费头像仅限 Mockup 使用，用到上线产品需购买含商用授权的合集 |  |  | 免费+付费 |
| [unavatar](https://unavatar.io) | 按用户名、邮箱或域名从 GitHub、X、Gravatar、Google 等来源取真实头像/Logo 的统一 API，并带回退链，做「输入账号就显示头像」时用；有免费额度，⚠ 免费使用要求署名，去署名和更高配额需付费 |  | https://unavatar.io/github/&lt;username&gt;<br>llms.txt: https://unavatar.io/llms.txt | 免费+付费 |
| [Vercel Avatar](https://avatar.vercel.sh) | Vercel 提供的渐变色头像服务，任意字符串作路径即返回一张确定性的渐变圆图，做占位头像和团队图标最省事；免费、免 key |  | https://avatar.vercel.sh/&lt;任意字符串&gt; | 免费 |

### 表情符号

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [Fluent Emoji](https://github.com/microsoft/fluentui-emoji) | 微软的开源 Emoji 全集，每个表情都有 3D、彩色扁平、高对比线条三种风格的 SVG/PNG，3D 版很适合当功能图标或插画点缀；MIT，可商用 |  | 开源 |
| [Noto Animated Emoji](https://googlefonts.github.io/noto-emoji-animation/) | Google 官方的动画 Emoji 库，几百个常用表情提供 Lottie、GIF、WebP 格式并可直接复制嵌入代码，做反应、庆祝、空状态的小动效时用；⚠ CC BY 4.0，需署名 |  | 免费 |
| [Noto Emoji](https://github.com/googlefonts/noto-emoji) | Google 的开源 Emoji 字体与图形，Android 默认表情，有彩色字体和可变字重的单色版，需要可自托管的 Emoji 字体时用；字体为 OFL，工具和多数图片为 Apache 2.0，可商用 |  | 开源 |
| [OpenMoji](https://openmoji.org) | 德国 HfG 设计学院主导的开源 Emoji，统一的手绘描边风格，有彩色和黑白线稿两版并含额外的界面类图标，适合想要不同于各大厂风格的 Emoji 时用；⚠ CC BY-SA 4.0，需署名且衍生作品须同协议共享 | `npm install openmoji` | 开源 |
| [Twemoji](https://github.com/jdecked/twemoji) | 原 Twitter 的扁平 Emoji 图形集，现由原团队成员在 jdecked/twemoji 持续维护，需要跨平台一致的 Emoji 显示时用它替换系统字体；代码 MIT，⚠ 图形为 CC-BY 4.0，需署名 | `npm install @twemoji/api` | 开源 |

### 音效

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [BBC Sound Effects](https://sound-effects.bbcrewind.co.uk) | BBC 开放的 3 万+ 条档案级音效，自然、城市、机械、历史录音质量极高，可在线混音试听；⚠ RemArc 许可仅限个人、教育和研究用途，商用必须另行购买授权 |  |  | 免费 |
| [ElevenLabs Sound Effects](https://elevenlabs.io/sound-effects) | 用文字描述生成音效的 AI 工具，找不到现成素材时直接生成一段界面音、环境音或拟音，可通过 API 批量调用；⚠ 免费档不含商用授权，商用需付费套餐 |  | POST https://api.elevenlabs.io/v1/sound-generation（需 xi-api-key）<br>llms.txt: https://elevenlabs.io/llms.txt | 免费+付费 |
| [Freesound](https://freesound.org) | 最大的协作式音效数据库，数十万条用户上传的声音，环境音、拟音、界面音都能搜到，并有带 token 的 API；⚠ 每条声音许可不同（CC0、CC BY 需署名、CC BY-NC 禁商用），下载前务必确认 |  | https://freesound.org/apiv2/search/text/?query=click&token=YOUR_API_KEY（文档 https://freesound.org/docs/api/） | 免费 |
| [howler.js](https://howlerjs.com) | 最常用的 Web 音频库，封装 Web Audio 并自动回退 HTML5 Audio，支持 sprite、淡入淡出、空间音频和多格式兼容，非 React 项目或需要精细控制播放时用；MIT 开源 |  | `npm i howler` | 开源 |
| [jsfxr](https://sfxr.me) | 8-bit 复古音效生成器，点「拾取/跳跃/爆炸/提示」随机生成并可微调参数，导出 WAV 或在代码里直接合成播放，做游戏化界面和像素风产品的音效时用；免费开源，生成的音效可自由使用 |  | `npm i jsfxr` | 开源 |
| [Material Design Sound Resources](https://m2.material.io/design/sound/sound-resources.html) | Google Material Design 官方的界面音效包（提示、导航、成功失败、Hero 音效等）及配套的声音设计准则，想要克制、专业的系统级提示音时用；⚠ CC-BY 4.0，需署名 |  |  | 免费 |
| [SND](https://snd.dev) | 专为界面交互设计的 UI 音效套件（点击、切换、输入、通知、转场等成套音色）和配套播放库，想要一整套风格统一的界面声音时用；素材免费、可商用，⚠ 不得原样再分发或转售 |  | `npm install snd-lib` | 免费 |
| [soundcn](https://soundcn.xyz) | 给 Web 应用用的界面音效 Registry，点击、通知、成功、报错等音效经 shadcn CLI 一条命令装成可直接播放的模块，给按钮和提示加声音反馈的最快办法；多数音效源自 CC0 素材，⚠ 其中魔兽世界合集版权属暴雪，不可随意商用 | React | `npx shadcn@latest add @soundcn/click-soft` | 免费 |
| [Tone.js](https://tonejs.github.io) | 在浏览器里合成声音和编排音乐的框架，有合成器、效果器和精确的时间轴调度，想用代码实时生成提示音、音阶反馈而不加载音频文件时用；MIT 开源 |  | `npm i tone` | 开源 |
| [use-sound](https://github.com/joshwcomeau/use-sound) | Josh Comeau 写的 React 音效 Hook，一行代码播放音效并支持音量、变速、打断和 sprite，给按钮、开关、通知加声音反馈时用；MIT 开源（底层为 Howler） | React | `npm i use-sound` | 开源 |
| [ZapSplat](https://www.zapsplat.com) | 15 万+ 专业音效与免版税音乐库，分类细、音质稳定，找特定场景的拟音时用；⚠ 免费账号可商用但须署名且只能下 MP3，捐赠升级后免署名并可下 WAV |  |  | 免费+付费 |

### 其他工具

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [@imgly/background-removal](https://github.com/imgly/background-removal-js) | 完全在浏览器或 Node 本地运行的抠图库（ONNX 模型，无需服务端和 API 费用），适合对隐私敏感或想零成本批量去背景的场景；⚠ AGPL 许可，闭源商用需联系 IMG.LY 购买授权 |  | `npm i @imgly/background-removal` | 开源 |
| [Anthony's QR Toolkit](https://qrcode.antfu.me) | Anthony Fu 做的二维码精调工具，可细致控制码点样式、边距、定位点和扰动，并能把 AI 生成的艺术二维码与原码对比校正以保证可扫，做 AI 艺术二维码后处理时用；免费开源 |  |  | 开源 |
| [capture-website-cli](https://github.com/sindresorhus/capture-website-cli) | Sindre Sorhus 的网页截图命令行工具（基于 Puppeteer），支持整页、模拟设备、暗色模式、隐藏元素和延时，Node 生态里一条命令截网页时用；MIT 开源 |  | `npm install --global capture-website-cli` | 开源 |
| [favicon.io](https://favicon.io) | 最快的 Favicon 生成器，可从文字、Emoji 或图片生成 favicon.ico 和各尺寸 PNG 并打包下载，项目刚起步需要一个临时图标时用；免费 |  |  | 免费 |
| [goQR.me API](https://goqr.me/api/) | 免注册的二维码生成与识别 HTTP API，一条 URL 就返回 PNG/SVG 二维码图片，适合不想装库、直接用 img 标签嵌入的场景；免费、免 key，可商用 |  | https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=&lt;内容&gt; | 免费 |
| [Icon Horse](https://icon.horse) | 按域名取任意网站 Favicon 的 API，自动挑最高清的版本并在取不到时生成回退图标，做链接卡片、书签列表、集成列表时用；免费可用，另有付费档 |  | https://icon.horse/icon/&lt;domain&gt; | 免费+付费 |
| [IconKitchen](https://icon.kitchen) | 在线应用图标生成器，从图片、剪贴画或文字生成 Android（自适应图标）、iOS、macOS 和 Web 的全套尺寸，可调背景、形状和内边距，独立开发者出 App 图标时用；免费 |  |  | 免费 |
| [Meta Tags](https://metatags.io) | 在线编辑并预览标题、描述和分享图在 Google 搜索结果与各社交平台的呈现，同时生成整套 meta 标签代码，写 SEO/社交 meta 时对照用；免费 |  |  | 免费 |
| [Microlink](https://microlink.io) | 把任意网址变成结构化数据的 API：元信息、Logo、整页截图、PDF 都能取，做链接预览卡片和自动化截图时用；免费档免 key 可直接调用但有每日限额，更高配额付费 |  | https://api.microlink.io/?url=https://example.com&screenshot=true<br>llms.txt: https://microlink.io/llms.txt | 免费+付费 |
| [node-qrcode](https://github.com/soldair/node-qrcode) | Node 与浏览器通用的二维码生成库，可输出 PNG、SVG、终端字符和 Data URL，并自带命令行，服务端或脚本里批量生成二维码时用；MIT 开源 |  | `npm i qrcode` | 开源 |
| [Nuxt OG Image](https://nuxtseo.com/og-image) | Nuxt 的 OG 图模块，用 Vue 组件当模板，可选 Takumi、Satori 或浏览器截图渲染并带开发期预览面板，Nuxt 项目做动态分享图时用；MIT 开源 | Nuxt, Vue | `npx nuxt module add nuxt-og-image`<br>llms.txt: https://nuxtseo.com/llms.txt | 开源 |
| [OGimage.gallery](https://www.ogimage.gallery) | 精选优秀 OG 分享图的灵感库，按产品类型浏览知名网站的卡片设计，设计自己的分享图模板前先来看构图和文字层级；免费 |  |  | 免费 |
| [OpenGraph.xyz](https://www.opengraph.xyz) | 输入网址即预览它在 X、Facebook、LinkedIn、Discord 等平台的分享卡片效果，并可生成缺失的 meta 标签，上线前检查 OG 图和标题是否正确时用；免费 |  |  | 免费 |
| [PWA Assets Generator (Vite PWA)](https://vite-pwa-org.netlify.app/assets-generator/) | 从一张 SVG/PNG 源图生成 PWA 所需全套图标、Favicon、maskable 图标和 iOS 启动图的 CLI 与 Vite 集成，Vite 系项目配 PWA 图标时用；MIT 开源 | Vite | `npm i -D @vite-pwa/assets-generator`<br>llms.txt: https://vite-pwa-org.netlify.app/llms.txt | 开源 |
| [pwa-asset-generator](https://github.com/elegantapp/pwa-asset-generator) | 用无头浏览器按 Apple 规范批量渲染 PWA 图标和各机型启动图，并自动写入 manifest 与 HTML 的命令行工具，与框架无关；MIT 开源 |  | `npx pwa-asset-generator logo.svg ./assets` | 开源 |
| [QRBTF](https://qrbtf.com) | 国内团队做的艺术二维码生成器，提供多种参数化样式（圆点、波普、3D 等）和 AI 生成的风格化二维码，想让二维码本身成为视觉元素时用；样式生成免费，⚠ 主仓库为 GPL-3.0，AI 生成需登录并有额度 |  |  | 免费+付费 |
| [RealFaviconGenerator](https://realfavicongenerator.net) | 最全面的 Favicon 生成与检查工具，上传一张图即生成各平台所需的全套图标（含 SVG、Apple Touch、PWA manifest）和对应 HTML，并能检测线上站点的 Favicon 配置问题；免费 |  |  | 免费 |
| [remove.bg](https://www.remove.bg) | 一键去除图片背景的在线服务，人像、商品、汽车抠图质量稳定，并有 API；⚠ 免费仅能下载低分辨率预览图，高清结果按点数付费（API 每月有少量免费预览额度） |  | POST https://api.remove.bg/v1.0/removebg（Header 带 X-Api-Key） | 免费+付费 |
| [resvg-js](https://github.com/thx/resvg-js) | 高性能的 SVG 转 PNG 渲染器（Rust resvg 的 Node/WASM 绑定），常与 Satori 配对把生成的 SVG 光栅化，也可用于服务端批量导出图标；MPL-2.0 开源 |  | `npm i @resvg/resvg-js` | 开源 |
| [ScreenshotOne](https://screenshotone.com) | 面向开发者和 Agent 的网页截图 API，能屏蔽广告与 Cookie 弹窗、整页滚动截图、指定视口与暗色模式，需要稳定的线上截图服务时用；有免费额度，之后按量付费 |  | https://api.screenshotone.com/take?url=https://example.com&access_key=YOUR_KEY<br>llms.txt: https://screenshotone.com/llms.txt | 免费+付费 |
| [shot-scraper](https://shot-scraper.datasette.io) | Simon Willison 的命令行截图工具（基于 Playwright），可按 CSS 选择器截取页面局部、先执行 JS 再截，并用 YAML 批量定义，文档配图自动化和让 Agent 自查界面时用；Apache-2.0 开源 |  | `pip install shot-scraper && shot-scraper install` | 开源 |
| [Squoosh](https://squoosh.app) | Google Chrome 团队的在线图片压缩工具，左右对比画质并可选 AVIF、WebP、MozJPEG、OxiPNG 等编码器，全部在本地浏览器完成，手动压单张 Hero 图时用；免费开源 |  |  | 开源 |
| [Takumi](https://takumi.kane.tw) | Rust 写的 JSX/CSS 转图片引擎，不经 SVG 中转直接输出 PNG/WebP/动图/PDF，CSS 支持面比 Satori 更广且更快，OG 图需要复杂样式或大批量渲染时用；MIT/Apache-2.0 开源 |  | `npm install takumi-js`<br>llms.txt: https://takumi.kane.tw/llms.txt | 开源 |
| [TinyPNG](https://tinypng.com) | 老牌智能有损压缩服务，支持 PNG、JPEG、WebP、AVIF，拖入即压，另有开发者 API 可接入构建流程；网页版免费有张数和体积上限，API 每月有免费额度、超出按量付费 |  | `npm i tinify`（需 API key） | 免费+付费 |
| [Upscayl](https://upscayl.org) | 开源的 AI 图片放大桌面应用（Real-ESRGAN），把低清截图、老素材或 AI 生成图放大 2–4 倍并补细节，本地运行不上传；免费，AGPL-3.0 开源 |  |  | 开源 |
| [Vercel OG (@vercel/og)](https://vercel.com/docs/og-image-generation) | 用 JSX + CSS 子集在边缘函数里动态生成 Open Graph 社交分享图的官方库，Next.js App Router 已内置为 next/og 的 ImageResponse，给每篇文章/每个页面自动出分享卡片时首选；开源免费 | Next.js, React | `npm i @vercel/og`<br>llms.txt: https://vercel.com/llms.txt | 开源 |
| [WebHaptics](https://haptics.lochie.me) | 给移动端网页加触感反馈的小型库，封装震动 API 并内置成功、警告、轻触等预设节奏，支持 React/Vue/Svelte，与音效配合做「按下去有感觉」的交互时用；开源免费 | React, Vue, Svelte | `npm i web-haptics`<br>llms.txt: https://haptics.lochie.me/llms.txt | 开源 |
