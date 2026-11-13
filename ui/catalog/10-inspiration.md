# 设计灵感画廊

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-inspiration"></a>

## 灵感画廊（带 MCP 的优先）

找参考图、截图给 AI 看。Mobbin / Refero / Lazyweb 有 MCP，Agent 可直接检索（都需要账号，Mobbin 和 Refero 要付费套餐）。

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Codrops](https://tympanus.net/codrops/) | 创意前端的标杆站点，持续发布带完整源码的实验性效果（WebGL 转场、滚动动画、文字特效、图片悬停）和案例拆解，想做获奖网站级别的交互时先来这里找可改的 Demo；免费，Demo 代码可自由用于个人和商业项目 |  | 免费 |
| ⭐ [Dribbble](https://dribbble.com) | 最大的设计师作品社区，按关键词能搜到海量界面概念稿、图标和插画，找视觉风格与配色方向时用；浏览免费，⚠ 多为概念稿而非上线产品，交互合理性要自己判断，作品版权归作者 |  | 免费+付费 |
| ⭐ [Mobbin](https://mobbin.com) | 60 万+ 真实 App/Web 截图、流程、页面区块 | `claude mcp add --transport http mobbin https://api.mobbin.com/mcp` | 付费 |
| ⭐ [Refero](https://refero.design) | 12.5 万+ Web/iOS 截图、8000+ 流程；配套 refero_skill 做「先调研再设计」 | `claude mcp add --transport http refero https://api.refero.design/mcp` | 付费 |
| [404s](https://www.404s.design) | 创意 404 错误页的精选合集，看别人如何把死胡同做成品牌露出和引导回流的机会；免费 | llms.txt: https://www.404s.design/llms.txt | 免费 |
| [60fps](https://60fps.design) | 界面动效与交互细节的灵感库，收录顶级 iOS 和 Web 应用里的真实动画片段，按交互类型（下拉刷新、转场、加载、手势）归类，写动效 Prompt 前先来看实际效果；免费 | llms.txt: https://60fps.design/llms.txt | 免费 |
| [A1 Gallery](https://www.a1.gallery) | 几乎每日更新的手选网站合集，面向设计师和开发者，画风统一、噪音少，适合当作日常的网站灵感订阅源；免费 | llms.txt: https://www.a1.gallery/llms.txt | 免费 |
| [Admire The Web](https://admiretheweb.com) | 专注简洁、干净、响应式网站的每日灵感站，可按行业和风格分类浏览，适合找中规中矩但执行精良的商业网站参考；免费 |  | 免费 |
| [Appshots](https://appshots.design) | 移动应用界面灵感库，按 App 和页面类型浏览真实应用的截图，作为 Mobbin 之外的轻量补充；基础浏览免费，高级功能付费 |  | 免费+付费 |
| [Are.na](https://www.are.na) | 以「频道」组织链接、图片和文字的知识与灵感收集平台，设计师常用来做长期研究型情绪板，可顺着别人的频道深挖某个主题；免费版有内容上限，并有公开 API | OpenAPI: https://api.are.na/v3/openapi.json<br>llms.txt: https://www.are.na/llms.txt | 免费+付费 |
| [Awwwards](https://www.awwwards.com) | 获奖网站；有 llms.txt 和只读 OpenAPI | llms.txt: https://www.awwwards.com/llms.txt | 免费 |
| [Baymard Institute](https://baymard.com) | 电商 UX 研究权威，基于大规模可用性测试给出结账、商品页、搜索、移动端等环节的具体准则和各大站点评分，做电商或表单密集型流程时参考；文章和部分基准免费，完整研究库需订阅 | llms.txt: https://baymard.com/llms.txt | 免费+付费 |
| [Behance](https://www.behance.net) | Adobe 旗下的作品集平台，以完整项目案例为主（品牌、界面、插画、动效的全流程展示），想看一个设计从概念到落地的整套呈现时用；免费浏览，作品版权归作者 |  | 免费 |
| [Bento Grids](https://bentogrids.com) | 便当盒（Bento）网格布局的精选合集，收录产品发布页、功能概览和作品集里的各种卡片拼接方式，做 Apple 风功能总览区时用；免费 |  | 免费 |
| [Best Website Gallery](https://bestwebsite.gallery) | 一位设计师自 2008 年起手工精选的网站画廊，可按颜色、字体、所用技术和 CMS 筛选，想查「用某款字体/某种配色的好网站」时用；免费 |  | 免费 |
| [Brutalist Websites](https://brutalistwebsites.com) | 粗野主义网站合集，收录刻意粗糙、反精致的网页设计并附站长访谈，做 Brutalist 或新粗野风时用来校准「度」；免费 |  | 免费 |
| [Built for Mars](https://builtformars.com) | 深度 UX 案例研究与示例库，90 多篇拆解讲清真实产品的做法及其心理学依据，并整理了 1500+ 个 UX 示例，做开户、结账等关键流程前值得对照；部分免费，完整内容订阅 | llms.txt: https://builtformars.com/llms.txt | 免费+付费 |
| [CallToInspiration](https://calltoinspiration.com) | 数千个手选的真实网站与应用 UI 示例，按登录、弹窗、定价、仪表盘、表单等模式归类，适合逐个模式找参考；免费 |  | 免费 |
| [Checklist Design](https://www.checklist.design) | 按页面、组件、流程整理的设计检查清单（登录页、表单、弹窗、定价页、暗色模式等），逐项列出该有的元素和状态，让 Agent 或自己在交付前自查有没有漏掉；免费 | llms.txt: https://www.checklist.design/llms.txt | 免费 |
| [CodePen](https://codepen.io) | 前端代码片段社区，任何效果名（如 glitch text、magnetic button）几乎都能搜到可运行、可改的 Demo，把灵感直接落到 HTML/CSS/JS 时用；免费浏览，⚠ 公开 Pen 默认 MIT 许可，但部分 Pen 引用了付费库或素材 |  | 免费+付费 |
| [Collect UI](https://collectui.com) | 按界面类型归档的每日 UI 灵感，把 Dribbble 上的作品整理成登录、结算、日历、设置等上百个类别，想快速看某一种页面的多种视觉做法时用；免费，⚠ 多为概念稿 |  | 免费 |
| [Cosmos](https://www.cosmos.so) | 视觉情绪板与灵感发现 |  | 免费 |
| [Craftwork Inspiration](https://craftwork.design/inspiration/websites) | Craftwork 整理的 2900+ 个精选网站，每个都配实时滚动录屏，可按代理商、Web App、作品集、AI、电商等类别筛选；免费浏览 | llms.txt: https://craftwork.design/llms.txt | 免费 |
| [CSS Design Awards](https://www.cssdesignawards.com) | 与 Awwwards 并列的网页设计奖项，按 UI、UX、创新三项打分，每日评选获奖站点，适合作为 Awwwards 之外的第二信息源；免费浏览 |  | 免费 |
| [CTA Gallery](https://www.cta.gallery) | 行动号召（CTA）区块的灵感合集，集中看各家如何写按钮文案、排布主次按钮和收尾区块；免费 |  | 免费 |
| [Curated Design](https://www.curated.design) | 精选网页设计 |  | 免费 |
| [Dark Design](https://dark.design) | 暗色模式网站合集 |  | 免费 |
| [Dark Mode Design](https://www.darkmodedesign.com) | 精选暗色模式网站的展示站，做暗色主题时用来参考层级、对比度和强调色的处理；免费 |  | 免费 |
| [Dashboard Design Patterns](https://dashboarddesignpatterns.github.io) | 爱丁堡大学研究团队总结的仪表盘设计模式，把数据信息、元信息、视觉表达、页面布局、交互和配色归纳成可组合的模式并讨论取舍，设计数据看板前用来理清结构；免费 |  | 免费 |
| [Data Viz Project](https://datavizproject.com) | Ferdio 整理的 160 多种数据可视化形式，可按家族、输入数据结构、功能和形状筛选，并附真实案例，找不落俗套的图表形式时用；免费 |  | 免费 |
| [Dead Simple Sites](https://deadsimplesites.com) | 只收极简网站的画廊：没有动画、没有滚动劫持，纯靠排版和留白，想做内容优先、加载飞快的简洁站点时参考；免费 |  | 免费 |
| [Deceptive Patterns](https://www.deceptive.design) | 「黑暗模式」的权威索引，分类列出诱导订阅、隐藏费用、确认羞辱等欺骗性设计手法，并附相关法律和执法案例，用来让 Agent 和团队明确什么不能做；免费 | llms.txt: https://deceptive.design/llms.txt | 免费 |
| [Design Spells](https://www.designspells.com) | 专门收集「有魔法感」的设计细节：微交互、彩蛋和让人会心一笑的小巧思，想给产品加几处令人记住的细节时来找点子；免费 |  | 免费 |
| [Design Systems Repo](https://designsystemsrepo.com) | 持续更新的设计系统资源合集，汇总公开的设计系统范例、文章、工具、演讲和书籍，从零搭设计系统时用来找范本；免费 |  | 免费 |
| [Design Systems Surf](https://designsystems.surf) | 可横向检索的设计系统资料库，收录大量公司的真实设计系统并能按组件、基础规范逐项对比，想看「各家的 Button/Toast 是怎么定义的」时用；部分免费，完整内容订阅 |  | 免费+付费 |
| [Detail](https://detail.design) | 记录那些塑造好界面的小设计决策的精选参考库，每条聚焦一个具体细节（对齐、状态、过渡、文案）并说明为什么好，面向在意细节的设计师和工程师；免费 |  | 免费 |
| [Empty States](https://emptystat.es) | 空状态设计的专题画廊，收录各产品在「暂无数据」「搜索无结果」「首次使用」时的界面，写空状态的插画、文案和引导按钮时参考；免费 |  | 免费 |
| [Fonts In Use](https://fontsinuse.com) | 可按字体、行业和媒介检索的字体应用档案库，每个案例都标明用了哪些字体，想看某款字体在真实设计中的效果或查某个设计用的是什么字时用；免费 |  | 免费 |
| [Footer Design](https://www.footer.design) | 页脚模式 |  | 免费 |
| [Framer Gallery](https://www.framer.com/community/gallery/) | Framer 官方的优秀站点画廊，全部为真实上线的 Framer 网站，动效和版式代表了当前无代码建站的流行审美，其中不少可 Remix；免费浏览 | llms.txt: https://www.framer.com/llms.txt | 免费 |
| [Game UI Database](https://www.gameuidatabase.com) | 最全的游戏界面参考库，收录上千款游戏的数万张截图，可按界面类型（HUD、背包、技能树、设置、对话）、风格、配色和控件筛选，做游戏 UI 或游戏化产品时必查；免费 |  | 免费 |
| [GoodUI](https://goodui.org) | 基于真实 A/B 测试结果的 UI 模式库，每个模式标注在多次实验中的胜负和提升幅度，并追踪大厂泄露的实验，做转化优化时用数据而不是直觉做决定；部分模式免费，完整数据付费 |  | 免费+付费 |
| [Growth.Design Case Studies](https://growth.design/case-studies) | 以漫画式幻灯片呈现的 UX 案例研究，逐步拆解 Airbnb、Duolingo、Tinder 等产品的流程并标注背后的心理学原理，想理解「为什么这样设计能转化」时读；免费 | llms.txt: https://growth.design/llms.txt | 免费 |
| [Hoverstat.es](https://www.hoverstat.es) | 「另类网页设计之家」，收录实验性强、打破常规的网站，带录屏展示交互，想找非模板化、有态度的排版与交互点子时用；免费 |  | 免费 |
| [Httpster](https://httpster.net) | 网页设计画廊 |  | 免费 |
| [HUDS+GUIS](https://www.hudsandguis.com) | 影视与游戏里的未来感界面（FUI）灵感站，收集电影中的全息屏、驾驶舱 HUD 和科幻操作台设计，做赛博朋克、科幻或数据大屏风格时用；免费 |  | 免费 |
| [Humane by Design](https://humanebydesign.com) | 以数字福祉为核心的人性化产品设计准则，围绕赋能、有限、包容、透明等原则给出可执行的建议，作为 Deceptive Patterns 的正面对照；免费 |  | 免费 |
| [Inclusive Components](https://inclusive-components.design) | Heydon Pickering 的无障碍组件模式博客，逐篇讲透开关、标签页、折叠面板、通知、数据表格等组件如何做到键盘与读屏友好，自己手写交互组件时对照；免费阅读 |  | 免费 |
| [Interface In Game](https://interfaceingame.com) | 电子游戏界面的截图与视频合集，按游戏和界面类型组织，带视频所以能看到菜单转场和动效，与 Game UI Database 互补；免费 |  | 免费 |
| [iOS Icon Gallery](https://www.iosicongallery.com) | App Store 优秀应用图标的展示站，可按颜色和类别浏览，设计 iOS 应用图标时看构图、材质和配色趋势；免费 |  | 免费 |
| [Land-book](https://land-book.com) | 每日精选落地页，可按区块/颜色浏览 | llms.txt: https://land-book.com/llms.txt | 免费+付费 |
| [Landingfolio](https://www.landingfolio.com) | 落地页与组件 |  | 免费+付费 |
| [Lapa Ninja](https://www.lapa.ninja) | 落地页画廊 |  | 免费 |
| [Laws of UX](https://lawsofux.com) | 把菲茨定律、希克定律、雅各布定律、米勒定律等 30 条 UX 心理学法则做成卡片式速查，每条有定义、要点和来源，给 Agent 写设计约束或评审界面时可直接引用法则名；免费 | llms.txt: https://lawsofux.com/llms.txt | 免费 |
| [Layers](https://layers.to) | 新一代设计师社区，氛围更贴近当下的产品设计圈，界面、图标和动效作品质量整齐，想看一线产品设计师最近在做什么风格时逛；免费 |  | 免费 |
| [Lazyweb](https://design.lazyweb.com) | 28 万+ 真实 App/营销页截图与流程，2 万+ 移动端 A/B 测试；MCP 需注册账号（OAuth 登录），免费账号只能拿到部分结果 | `claude mcp add --transport http lazyweb https://www.lazyweb.com/mcp`（首次连接要 OAuth 登录） | 免费+付费 |
| [Logosystem](https://logosystem.co) | 1600+ 个 Logo 的免费灵感库，含字标、图形标和动态 Logo，可按颜色、风格、形状和行业筛选，设计或让 AI 生成 Logo 前用来定方向；免费 | llms.txt: https://logosystem.co/llms.txt | 免费 |
| [macOS Icon Gallery](https://www.macosicongallery.com) | Mac App Store 优秀应用图标的展示站，与 iOS Icon Gallery 同系列，做桌面应用图标时参考其立体感和圆角矩形内的构图；免费 |  | 免费 |
| [Made in Webflow](https://webflow.com/made-in-webflow) | Webflow 社区作品库，可按热门、交互类型和标签浏览，许多项目可一键克隆后查看交互是如何搭的，想拆解某个滚动或悬停效果的实现时用；免费浏览 | llms.txt: https://webflow.com/llms.txt | 免费 |
| [Minimal Gallery](https://minimal.gallery) | 极简风网站 |  | 免费 |
| [Muzli](https://muz.li) | 设计灵感聚合器，把 Dribbble、Behance、Awwwards 和各设计媒体的新内容汇成一个信息流，另有浏览器新标签页扩展，想每天被动刷到新设计时用；免费 | llms.txt: https://muz.li/llms.txt | 免费 |
| [Navbar Gallery](https://www.navbar.gallery) | 导航栏模式 |  | 免费 |
| [Nicelydone](https://nicelydone.club) | 20 多万张真实 SaaS 界面截图的搜索库，覆盖 500+ 产品，可像搜索引擎一样检索具体页面和组件并拖进 Figma，找某类功能页（账单、权限、通知设置）的行业做法时用；部分免费，完整库需订阅 | llms.txt: https://nicelydone.club/llms.txt | 免费+付费 |
| [One Page Love](https://onepagelove.com) | 单页网站与模板 |  | 免费 |
| [Page Flows](https://pageflows.com) | 真实用户流程录屏（注册、引导、支付…） |  | 付费 |
| [Pinterest](https://www.pinterest.com) | 通用的图片收藏与发现引擎，搜任意风格词都能顺着相关推荐无限延展，适合项目初期建情绪板和找跨领域视觉参考；免费，⚠ 图片来源混杂、出处常缺失，只宜做参考 |  | 免费 |
| [Pricing Pages](https://pricingpages.design) | 定价页专题画廊，手选 SaaS、电商和代理商的定价页设计，对比套餐卡片、月付年付切换和功能对照表的做法时用；免费 | llms.txt: https://pricingpages.design/llms.txt | 免费 |
| [Rauno Freiberg — Craft](https://rauno.me/craft) | Vercel 设计工程师 Rauno 的交互原型集，展示各种精细的界面实验（手势、物理感动画、命令面板等），是「交互质感」的高水位参考；免费 |  | 免费 |
| [Really Good Emails](https://reallygoodemails.com) | 最大的邮件设计灵感库，1.9 万+ 封真实营销与事务邮件，按欢迎、促销、订单、召回等类型归类，并可查看每封的 HTML 源码，做邮件模板时用；免费 | llms.txt: https://reallygoodemails.com/llms.txt | 免费 |
| [Rebrand Gallery](https://www.rebrand.gallery) | 品牌重塑案例库，收录各公司换标的发布视频，并拆解其 Logo、配色和字体，可按风格、字体、行业和设计工作室检索，做品牌升级或了解品牌趋势时用；免费 | llms.txt: https://www.rebrand.gallery/llms.txt | 免费 |
| [Recent（原 Godly）](https://recent.design) | 原 Godly 改版而来的网站灵感库，卡片为自动播放的滚动录屏，能直接看到动效和交互节奏，收录偏前卫的品牌站和产品站；免费 |  | 免费 |
| [Refactoring UI](https://www.refactoringui.com) | Tailwind 作者 Adam Wathan 与 Steve Schoger 写给开发者的界面设计书，用大量前后对比讲层级、间距、配色和阴影的具体手法，是「不会设计的工程师」提升审美最高效的材料；⚠ 付费电子书（含视频与素材的完整包约 149 美元） |  | 付费 |
| [SaaS Interface](https://saasinterface.com) | SaaS 应用界面与交互示例库，按页面类型和 UI 元素（表格、筛选、空状态、弹窗）分类，适合逐个组件看成熟产品怎么做；免费浏览 |  | 免费 |
| [SaaS Landing Page](https://saaslandingpage.com) | SaaS 落地页，按区块分类 |  | 免费 |
| [SaaSFrame](https://www.saasframe.io) | SaaS UI 与邮件示例 |  | 免费+付费 |
| [SaaSUI](https://www.saasui.design) | 3500+ 张真实 SaaS 产品界面截图，来自 Notion、Linear、Stripe 等 160 多款产品，按仪表盘、引导、定价、设置等页面类型组织，做 B 端产品内页时比落地页画廊更对口；免费浏览 | llms.txt: https://www.saasui.design/llms.txt | 免费 |
| [Savee](https://savee.com) | 设计师策展的无广告视觉灵感平台，内容偏平面、品牌、排版和艺术指导，做情绪板和找高级感视觉语言时用；基础免费，高级功能订阅 | llms.txt: https://savee.com/llms.txt | 免费+付费 |
| [ScreensDesign](https://screensdesign.com) | 移动 App 设计库，收录真实 iOS 应用的界面、引导流程、付费墙录屏及营收数据，并能据此生成屏幕，做订阅制 App 的引导和付费墙时很对口；部分免费，完整库需订阅 | llms.txt: https://screensdesign.com/llms.txt | 免费+付费 |
| [Seesaw](https://www.seesaw.website) | 每日更新的网站灵感精选，偏设计工作室、品牌和产品站，支持按类型与风格标签筛选；免费 |  | 免费 |
| [Siteinspire](https://www.siteinspire.com) | 老牌精选网站画廊，偏好克制、排版讲究的作品，可按风格、类型和行业组合筛选，找高品位的企业站、作品集和编辑类网站参考时用；免费 |  | 免费 |
| [SiteSee](https://sitesee.co) | 手工挑选的现代网站画廊，可按类别、配色和风格浏览，界面清爽、更新勤，快速扫一遍当下主流的落地页风格时用；免费 |  | 免费 |
| [Spotted in Prod](https://www.spottedinprod.com) | 精选 iOS 应用里出彩交互细节的短视频合集，全部来自已上线的产品，找转场、手势和微交互的真实范例时用；免费 |  | 免费 |
| [Supahero](https://supahero.io) | 只收 Hero 首屏的灵感库，按风格、布局和行业筛选，专门解决「首屏怎么排」的问题；免费 |  | 免费 |
| [The Data Visualisation Catalogue](https://datavizcatalogue.com) | 图表类型百科，可按「想表达什么」（比较、占比、分布、关系、流程）反查合适的图表，每种都有结构图解和适用说明，让 Agent 选对图表类型并叫对名字时用；免费 |  | 免费 |
| [The FWA](https://thefwa.com) | 始于 2000 年的数字设计奖项，侧重沉浸式体验、WebGL、装置和创新交互，每天评出当日最佳，想了解创意技术的上限时看；免费浏览 |  | 免费 |
| [typo/graphic posters](https://www.typographicposters.com) | 始于 2008 年的字体与平面海报参考平台，收录全球设计师的海报作品，做大字排版、海报感 Hero 或编辑风页面时找构图与字体搭配；免费 |  | 免费 |
| [UI Garage](https://www.uigarage.net) | 按模式分类的 UI 灵感库，覆盖 Web、移动端和平板的具体界面类型（引导、搜索、图表、表单等）；免费 |  | 免费 |
| [UIland](https://uiland.design) | 移动端 UI 截图 |  | 免费+付费 |
| [Unsection](https://www.unsection.com) | 以「区块」为单位的网站灵感库，直接浏览 Hero、功能介绍、定价、FAQ、页脚等单个 Section 的截图，拼落地页时逐块找参考比看整页更高效；免费 |  | 免费 |
| [UserOnboard](https://www.useronboard.com) | Samuel Hulick 的新手引导拆解合集，把知名产品的注册与首次使用流程逐屏截图并配评注，做 Onboarding 时用来学习好坏判断的理由；免费 |  | 免费 |
| [Viewport UI](https://viewportui.com) | 从 X（Twitter）上设计师发布的作品里精选的 UI、交互和动效研究合集，可按种类、风格和行业浏览，能看到最新的设计工程师圈子在玩什么；免费 | llms.txt: https://viewportui.com/llms.txt | 免费 |
| [waitlist.design](https://www.waitlist.design) | 候补名单（Waitlist）页面专题库，以动态录屏收录线上最好的预发布页，产品上线前做一个邮件收集页时参考；免费 |  | 免费 |
| [Wall of Portfolios](https://www.wallofportfolios.in) | 全球 UX/UI 与产品设计师作品集的集合，可按风格和角色筛选，做个人作品集网站或看案例研究怎么写时参考；免费 | llms.txt: https://www.wallofportfolios.in/llms.txt | 免费 |
