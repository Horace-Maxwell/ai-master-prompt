# 功能型组件（图表 / 表格 / 编辑器 / 拖拽 / 地图…）

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-functional"></a>

## 功能型组件

单一用途、别自己造的那类组件。每个子类的 ⭐ 是默认选择。

本类分组：图表与可视化 · 表格与数据网格 · 表单 · 编辑器（富文本 / 代码 / Markdown） · 日期与日历 · 拖拽与排序 · 流程图 / 白板 / 节点编辑 · 地图 · 轮播 · 弹层 / 通知 / 命令面板 · 虚拟列表 · 文件上传 · 媒体（视频 / 音频 / PDF） · Markdown 渲染与代码高亮 · 认证界面 · 其他

### 图表与可视化

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Recharts](https://recharts.github.io) | React + D3 的声明式 SVG 图表库（v3），生态最大、shadcn Chart 的底层；React 项目做常规折线/柱状/饼图的默认选择 | React | `npm install recharts react-is` | 开源 |
| [ApexCharts](https://apexcharts.com) | 交互式 SVG 图表库，默认样式好看、配置简单，有 React/Vue 封装（⚠ 年收入 200 万美元以上的组织需购买商业授权，部分高级图型需 license key） | JS | `npm install apexcharts` | 免费+付费 |
| [Bklit UI](https://bklit.com) | 基于 visx + Motion 的可组合图表组件（折线/面积/柱状/饼/雷达/地图），shadcn CLI 安装；需要带动画的定制图表时选 | React, shadcn, visx, Motion | `npx shadcn@latest add @bklit/line-chart` | 开源 |
| [Chart.js](https://www.chartjs.org) | 最普及的 Canvas 图表库，框架无关、上手最快；非 React 项目或只要几张简单图表时选 | JS | `npm install chart.js` | 开源 |
| [Cytoscape.js](https://js.cytoscape.org) | 图论/网络关系图的分析与可视化库，内置多种布局与图算法；做知识图谱、依赖关系图时选 | JS | `npm install cytoscape` | 开源 |
| [D3.js](https://d3js.org) | 数据可视化的底层标准库（比例尺、布局、形状、地理投影）；现成图表库做不出的定制可视化才直接用，学习成本高 | JS | `npm install d3` | 开源 |
| [EvilCharts](https://evilcharts.com) | shadcn 风格的手工动效图表集（Recharts 或 ECharts 双引擎，300+ registry 条目）；想要比官方 Chart 更花哨的仪表盘图表时用 | React, shadcn, Recharts, ECharts | `npx shadcn@latest add @evilcharts/recharts-{chart-name}` | 开源 |
| [Highcharts](https://www.highcharts.com) | 老牌商业图表套件（含 Stock、Maps、Gantt），无障碍和导出能力强（⚠ 商业项目必须购买授权，仅非商业免费） | JS | `npm install --save highcharts` | 付费 |
| [Lightweight Charts](https://tradingview.github.io/lightweight-charts/) | TradingView 的金融 K 线/时间序列 Canvas 图表，体积小性能高；做行情、交易类界面时选（⚠ 需保留 TradingView 署名） | JS | `npm install lightweight-charts`<br>`npx skills add https://github.com/tradingview/lightweight-charts` | 开源 |
| [Liveline](https://benji.org/liveline) | Benji Taylor 做的实时动画折线图组件（单一 canvas、零依赖、数值平滑过渡）；只需要一条精致的实时走势线时选，尚在 0.x | React | `pnpm add liveline` | 开源 |
| [Nivo](https://nivo.rocks) | 图表类型最全的 React 库之一（SVG/Canvas/HTML 三种渲染，含桑基、日历热力、和弦图）；要冷门图型或服务端渲染时选 | React | yarn add @nivo/core @nivo/bar | 开源 |
| [Observable Plot](https://observablehq.com/plot/) | D3 团队出的高层图形语法库，一行代码出探索性图表；做数据分析、笔记本式快速出图时选 | JS | `npm install @observablehq/plot` | 开源 |
| [Plotly.js](https://plotly.com/javascript/) | 科学计算向图表库（3D、统计图、等高线、地图），与 Python Plotly 同源；做科研或数据科学类可视化时选，体积较大 | JS | `npm i --save plotly.js-dist-min` | 开源 |
| [react-chartjs-2](https://react-chartjs-2.js.org) | Chart.js 的 React 封装；团队已熟悉 Chart.js 配置又要在 React 里用时选 | React | `npm i react-chartjs-2 chart.js` | 开源 |
| [react-force-graph](https://github.com/vasturiano/react-force-graph) | 力导向图的 React 组件（2D Canvas / 3D WebGL / VR / AR 四个版本）；要快速做炫酷的 3D 关系网络时选 | React |  | 开源 |
| [shadcn/ui Charts](https://ui.shadcn.com/charts) | shadcn 官方图表区块（基于 Recharts，复制即用、跟随主题色）；已用 shadcn 的项目直接选它 | React, shadcn, Recharts | `npx shadcn@latest add chart` | 免费 |
| [Sigma.js](https://www.sigmajs.org) | WebGL 渲染的大规模网络图库（配合 graphology），上万节点仍流畅；节点数量很大的关系图选它 | JS |  | 开源 |
| [Unovis](https://unovis.dev) | F5 开源的模块化可视化框架，同一套核心支持 React/Vue/Angular/Svelte，含地图与网络图；多框架团队统一图表方案时选 | React, Vue, Angular, Svelte | `npm install -P @unovis/ts` | 开源 |
| [uPlot](https://github.com/leeoniya/uPlot) | 约 50KB 的超快 Canvas 时间序列图表，百万点仍流畅；监控面板、实时流数据等对性能敏感的场景选 | JS |  | 开源 |
| [Vega-Lite](https://vega.github.io/vega-lite/) | 用 JSON 声明图表的图形语法（可交互、可组合）；需要让 LLM 或配置文件直接生成图表规格时很合适 | JS |  | 开源 |
| [Victory](https://nearform.com/open-source/victory/) | Nearform 维护的模块化 React 图表库，Web 与 React Native 共用同一套 API；要跨端复用图表代码时选 | React, React Native | `npm install victory --save` | 开源 |
| [visx](https://visx.airbnb.tech) | Airbnb 的低层 React 可视化原语（D3 计算 + React 渲染）；需要完全自定义图表而不想直接写 D3 时选 | React | `npm install --save @visx/visx` | 开源 |

### 表格与数据网格

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [AG Grid](https://www.ag-grid.com) | 功能最全的企业级数据网格（十万行、透视、分组、Excel 导出）；需要开箱即用的重型表格时选（⚠ Community 版 MIT，透视/主从表等 Enterprise 功能付费） | React, Angular, Vue, JS | `npm install --save ag-grid-react` | 免费+付费 |
| [FortuneSheet](https://github.com/ruilisi/fortune-sheet) | Luckysheet 的 TypeScript/React 重写版在线表格，开箱即用；只需要一个 MIT 的类 Excel 组件时选（近一年更新放缓） | React | `npm install --save @fortune-sheet/react` | 开源 |
| [Glide Data Grid](https://grid.glideapps.com) | Canvas 渲染的 React 数据网格，百万行滚动无压力、可编辑；超大数据量表格时选（稳定版 6.0 更新较慢） | React | `npm i @glideapps/glide-data-grid` | 开源 |
| [Handsontable](https://handsontable.com) | 类 Excel 的电子表格式数据网格（公式、合并单元格、复制粘贴）；需要用户像用 Excel 一样录入数据时选（⚠ 商业使用需购买授权，仅非商业免费） | JS, React, Angular, Vue | `npm install handsontable @handsontable/react-wrapper` | 付费 |
| [HyperFormula](https://handsontable.com/hyperformula/) | 无界面的电子表格公式计算引擎（约 400 个 Excel 函数）；自己画表格 UI 但需要公式能力时配合使用（⚠ GPLv3 或商业授权） | JS | `npm install hyperformula` | 免费+付费 |
| [Jspreadsheet CE](https://bossanova.uk/jspreadsheet) | 原生 JS 的轻量在线电子表格（社区版 MIT）；无框架页面要 Excel 式录入时选（Pro 版付费） | JS | `npm install jspreadsheet-ce` | 免费+付费 |
| [MUI X](https://mui.com/x/) | MUI 的高级组件套件（Data Grid、Date Pickers、Charts、Tree View）；Material UI 项目需要重型表格/日期/图表时选（⚠ Pro/Premium 功能付费） | React, MUI | `npm install @mui/x-data-grid @mui/material @emotion/react @emotion/styled` | 免费+付费 |
| [Niko Table](https://niko-table.com) | 基于 TanStack Table 的可组合 shadcn 数据表格与可编辑网格（高级筛选、行列拖拽、虚拟化）；想按需拼装表格功能时选，项目较新 | React, shadcn, TanStack Table | `npx shadcn@latest add @niko-table/data-table` | 免费 |
| [OpenStatus Data Table Filters](https://data-table.openstatus.dev) | OpenStatus 开源的 shadcn 数据表格（分面筛选、无限滚动、行详情抽屉、Drizzle 服务端过滤）；做日志/监控类列表页时选 | React, shadcn, TanStack Table | `npx shadcn@latest add @data-table-filters/data-table @data-table-filters/data-table-schema` | 开源 |
| [React Spreadsheet](https://iddan.github.io/react-spreadsheet/) | 极简的 React 电子表格组件（公式、选区、复制粘贴）；只要一小块可编辑表格区域、不需要完整 Excel 时选 | React | `npm install react react-dom scheduler react-spreadsheet` | 开源 |
| [react-data-grid](https://github.com/Comcast/react-data-grid) | 轻量的 React 虚拟化数据网格（可编辑、列冻结、分组）；想要比 AG Grid 轻、全 MIT 的可编辑表格时选（v7 长期处于 beta） | React | `npm install react-data-grid` | 开源 |
| [RevoGrid](https://rv-grid.com) | Web Component 实现的高性能虚拟数据网格，任何框架可用，百万单元格流畅；非 React 或多框架项目要 Excel 式表格时选（Pro 插件付费） | Web Components, React, Vue, Angular, Svelte | `npm i @revolist/revogrid --save` | 免费+付费 |
| [SVAR React DataGrid](https://svar.dev/react/datagrid/) | SVAR 的 MIT React 数据网格（虚拟滚动、行内编辑、树形数据），同系列还有 Gantt 等；要轻量可编辑表格且不想付费时选 | React | `npm install @svar-ui/react-grid` | 开源 |
| [tablecn](https://tablecn.com) | sadmann7 的 shadcn 数据表格模板（TanStack Table + 服务端排序/筛选/分页 + 高级过滤器）；做后台列表页时照抄这个仓库 | Next.js, shadcn, TanStack Table |  | 开源 |
| [Tabulator](https://tabulator.info) | 零依赖的原生 JS 交互表格（排序、筛选、分组、导出、树形）；传统多页应用或无框架页面要功能表格时选 | JS | `npm install tabulator-tables --save` | 开源 |

### 表单

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [AutoForm](https://autoform.vantezzen.io) | 从 Zod/Yup 等 schema 自动生成表单 UI（有 shadcn、MUI、Mantine 等适配）；内部工具或设置页想少写表单代码时选 | React, shadcn, Zod | `npx skills add https://github.com/vantezzen/autoform/tree/main/skills --skill autoform` | 开源 |
| [Downshift](https://www.downshift-js.com) | 构建自动完成/下拉/多选的无头 hooks（完整 WAI-ARIA）；要完全自定义样式的 Combobox 时选 | React | `npm install --save downshift` | 开源 |
| [Formik](https://formik.org) | 曾经最流行的 React 表单库；只在维护老项目时继续用，新项目请选 React Hook Form（维护模式，更新很少） | React |  | 开源 |
| [FormKit](https://formkit.com) | Vue 生态的表单框架（输入组件、校验、schema 生成、主题一体）；Vue/Nuxt 项目做表单的首选（Pro 输入组件付费） | Vue, Nuxt | `npx formkit skill` | 免费+付费 |
| [input-otp](https://input-otp.rodz.dev) | 无样式、可访问的一次性验证码输入框（支持粘贴与自动填充），shadcn 的 InputOTP 即基于它；做短信/邮箱验证码时选 | React | `npm install input-otp`<br>`npx shadcn@latest add input-otp` | 开源 |
| [JSON Forms](https://jsonforms.io) | EclipseSource 的 JSON Schema + UI Schema 表单框架，支持 React/Angular/Vue；需要把布局也用 JSON 描述的动态表单时选 | React, Angular, Vue |  | 开源 |
| [React Select](https://react-select.com) | 功能最全的 React 下拉选择器（多选、异步加载、可创建、分组）；原生 select 或 shadcn Combobox 不够用时选 | React | yarn add react-select | 开源 |
| [react-jsonschema-form](https://rjsf-team.github.io/react-jsonschema-form/) | 根据 JSON Schema 动态渲染表单（有 MUI、Ant Design、shadcn 等主题）；表单结构由后端或配置下发时选 | React | `npm install @rjsf/core` | 开源 |
| [react-number-format](https://s-yadav.github.io/react-number-format/) | 数字/金额/手机号等格式化与掩码输入组件；做金额、卡号、百分比输入框时选 | React | `npm install react-number-format` | 开源 |
| [react-phone-number-input](https://catamphetamine.gitlab.io/react-phone-number-input/) | 带国家区号选择与 libphonenumber 校验的国际手机号输入框；需要国际化手机号录入时选 | React | `npm install react-phone-number-input --save` | 开源 |
| [shadcn Form Builder](https://www.shadcn-form.com) | 可视化拖拽生成 shadcn + React Hook Form + Zod 表单代码的在线工具；想先拖出表单再拷代码时用 | React, shadcn, Zod |  | 免费 |
| [Superforms](https://superforms.rocks) | SvelteKit 的表单库（服务端/客户端同构校验、渐进增强、嵌套数据）；SvelteKit 项目做表单的首选 | SvelteKit | `npm i -D sveltekit-superforms` | 开源 |
| [SurveyJS](https://surveyjs.io) | 问卷/多步表单引擎（条件逻辑、分页、计分，JSON 驱动）；做问卷调查、测评类产品时选（⚠ 渲染库 MIT，可视化 Creator 等需商业授权） | React, Angular, Vue, JS | `npm install survey-react-ui` | 免费+付费 |

### 编辑器（富文本 / 代码 / Markdown）

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Tiptap](https://tiptap.dev) | 基于 ProseMirror 的无头富文本编辑器框架（v3，扩展丰富，React/Vue 皆可）；做 Notion 式或评论框式编辑器的默认选择（⚠ 核心 MIT，协同、AI、评论等为付费云服务） | React, Vue, JS | `npm install @tiptap/react @tiptap/pm @tiptap/starter-kit`<br>`npx skills add ueberdosis/tiptap --skill tiptap` | 免费+付费 |
| [@monaco-editor/react](https://github.com/suren-atoyan/monaco-react) | 免打包配置的 Monaco React 封装（从 CDN 懒加载）；在 React/Next.js 里用 Monaco 的最省事方式 | React | `npm install @monaco-editor/react` | 开源 |
| [@uiw/react-codemirror](https://uiwjs.github.io/react-codemirror/) | CodeMirror 6 最常用的 React 封装（主题、语言扩展打包好）；在 React 里用 CodeMirror 时直接装它 | React | `npm install @uiw/react-codemirror --save` | 开源 |
| [@uiw/react-md-editor](https://uiwjs.github.io/react-md-editor/) | 带实时预览的轻量 Markdown 文本编辑器（左写右看）；只要源码式 Markdown 输入框时选 | React | `npm i @uiw/react-md-editor` | 开源 |
| [BlockNote](https://www.blocknotejs.org) | 开箱即用的 Notion 式块编辑器（斜杠菜单、拖拽块、协同）；想最少代码得到块编辑器时选（⚠ 核心 MPL-2.0，XL 包为 GPL-3.0 或商业授权） | React | `npm install @blocknote/core @blocknote/react @blocknote/mantine` | 免费+付费 |
| [CKEditor 5](https://ckeditor.com/ckeditor-5/) | 企业级富文本编辑器（协同、修订、评论、导出 Word/PDF）；需要文档级协作功能时选（⚠ GPL-2.0+ 或商业授权） | JS, React, Vue, Angular | `npm install ckeditor5 ckeditor5-premium-features`<br>`npm install @ckeditor/ckeditor5-react` | 免费+付费 |
| [CodeMirror 6](https://codemirror.net) | 模块化的浏览器代码编辑器（体积小、移动端友好、可按需加载语言）；网页里嵌入代码输入框的默认选择 | JS |  | 开源 |
| [Editor.js](https://editorjs.io) | 输出干净 JSON 的块式编辑器（框架无关，插件化）；内容要以结构化 JSON 存储并多端渲染时选 | JS | `npm i @editorjs/editorjs` | 开源 |
| [Lexical](https://lexical.dev) | Meta 的可扩展文本编辑器框架（性能与无障碍好，核心很小）；需要高度定制且看重性能/包体时选，上手比 Tiptap 陡 | React | `npm install lexical @lexical/react` | 开源 |
| [MDXEditor](https://mdxeditor.dev) | 所见即所得的 Markdown/MDX React 编辑器（基于 Lexical，支持表格、代码块、JSX 组件）；让用户不看语法也能编辑 Markdown 时选 | React | `npm install --save @mdxeditor/editor` | 开源 |
| [Milkdown](https://milkdown.dev) | 插件驱动的所见即所得 Markdown 编辑器框架（Crepe 为开箱即用版）；要 Typora 式体验且需深度定制时选 | JS, React, Vue | `npm install @milkdown/crepe` | 开源 |
| [Minimal Tiptap](https://github.com/Aslam97/minimal-tiptap) | 极简的 shadcn + Tiptap 富文本编辑器组件（工具栏、图片、代码块齐备）；只要一个干净的文章/评论编辑框时选 | React, shadcn, Tiptap | `npx shadcn@latest add https://raw.githubusercontent.com/Aslam97/shadcn-minimal-tiptap/main/registry/block-registry.json` | 开源 |
| [Monaco Editor](https://microsoft.github.io/monaco-editor/) | VS Code 的编辑器内核（IntelliSense、diff、多光标）；做在线 IDE、SQL/JSON 编辑器等重型场景时选，包体大、不支持移动端 | JS | `npm install monaco-editor` | 开源 |
| [Novel](https://novel.sh) | 带 AI 自动补全的 Notion 式编辑器（Tiptap + Vercel AI SDK）；适合当 AI 写作编辑器的参考实现（维护模式，2025 年初后无更新） | React, Tiptap, Tailwind |  | 开源 |
| [Plate](https://platejs.org) | 基于 Slate 的 shadcn 风格富文本编辑器（插件 + 现成 UI，含 AI、协同、Markdown/MDX）；想直接装一个完整的 Notion 式编辑器到 shadcn 项目时选（Plate Plus 模板付费） | React, shadcn, Slate | `npx shadcn@latest add @plate/plate-ui` | 免费+付费 |
| [ProseKit](https://prosekit.dev) | 基于 ProseMirror 的跨框架富文本工具包（React/Vue/Preact/Svelte/Solid），提供 shadcn registry 示例；非 React 框架要现代编辑器时选 | React, Vue, Svelte, Solid, Preact | `npm install prosekit` | 开源 |
| [ProseMirror](https://prosemirror.net) | 富文本编辑器的底层工具包（Tiptap、BlockNote、Milkdown 都基于它）；只有需要完全掌控文档模型时才直接用 | JS |  | 开源 |
| [Quill](https://quilljs.com) | 经典的所见即所得富文本编辑器（v2，Delta 格式）；只要简单稳定的传统工具栏编辑器时选（更新放缓） | JS | `npm install quill` | 开源 |
| [Sandpack](https://sandpack.codesandbox.io) | CodeSandbox 的浏览器内代码运行组件（编辑器 + 实时预览）；文档站、教程里要可运行示例时选（更新放缓） | React | `npm i @codesandbox/sandpack-react` | 开源 |
| [shadcn-editor](https://shadcn-editor.vercel.app) | 基于 Lexical + shadcn/ui 的富文本编辑器区块，一条命令装进项目；shadcn 项目想用 Lexical 时选 | React, shadcn, Lexical | `npx shadcn@latest add @shadcn-editor/editor-x` | 开源 |
| [Slate](https://docs.slatejs.org) | 完全可定制的 React 富文本编辑框架（Plate 的底层）；要自己定义文档结构和渲染时选，长期处于 0.x、API 偶有变动 | React | yarn add slate slate-react | 开源 |
| [TinyMCE](https://www.tiny.cloud) | 老牌商业级所见即所得编辑器（类 Word 体验、表格、粘贴清洗）；CMS、邮件编辑等需要传统富文本时选（⚠ GPL-2.0+ 或商业授权，高级插件付费） | JS, React, Vue, Angular | `npm install @tinymce/tinymce-react` | 免费+付费 |

### 日期与日历

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [React DayPicker](https://daypicker.dev) | 可访问、可定制的日期选择日历（v10 起包名为 @daypicker/react），shadcn Calendar 的底层；React 日期选择器的默认选择 | React | `npm install @daypicker/react` | 开源 |
| [CalendarCN](https://calendarcn.xyz) | 仿 Notion Calendar 的 shadcn 日历区块（日/周/月/议程视图、拖拽缩放、ICS 导入导出）；shadcn 项目要成品日程界面时选，项目较新 | React, shadcn | `npx shadcn@latest add @calendarcn/<item>` | 免费 |
| [Cally](https://wicky.nillia.ms/cally/) | 极小的 Web Component 日历（单选/范围/多选，可访问），daisyUI 官方推荐；非 React 或任意框架要日历时选 | Web Components | `npm install cally` | 开源 |
| [FullCalendar](https://fullcalendar.io) | 最成熟的日程日历（月/周/日/列表视图、拖拽改期、重复事件），多框架可用；做排班、预约、日程管理时选（⚠ 时间线/资源视图为付费 Premium 插件） | JS, React, Vue, Angular | `npm install @fullcalendar/react temporal-polyfill` | 免费+付费 |
| [React Big Calendar](https://github.com/bigcalendar/react-big-calendar) | 类 Google Calendar 的 React 事件日历（月/周/日/议程视图，可拖拽）；要全免费的 React 日程视图时选，样式需自己调 | React | `npm install --save react-big-calendar` | 开源 |
| [React Calendar](https://projects.wojtekmaj.pl/react-calendar/) | 轻量的月/年/十年视图日历组件，不依赖日期库；只要一个可点选的日历面板时选 | React | `npm install react-calendar` | 开源 |
| [React Datepicker](https://reactdatepicker.com) | 自带输入框与弹层的日期/时间选择器，开箱即用；不想自己拼 Popover 的传统表单场景选 | React | `npm install react-datepicker --save` | 开源 |
| [Schedule-X](https://schedule-x.dev) | 现代风格的事件日历（Material 风、拖拽、响应式），支持 React/Vue/Svelte/Angular；想要比 FullCalendar 更现代外观时选（⚠ 资源视图、拖拽创建等为付费 Premium） | React, Vue, Svelte, Angular | `npm install @schedule-x/react` | 免费+付费 |

### 拖拽与排序

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [dnd kit](https://dndkit.com) | 现代的拖拽工具包（可访问、支持触摸与键盘、可排序/看板/网格），新版为框架无关核心 + @dnd-kit/react；React 拖拽排序的默认选择 | React, Vue, Svelte, Solid | `npm install @dnd-kit/react` | 开源 |
| [@hello-pangea/dnd](https://github.com/hello-pangea/dnd) | react-beautiful-dnd 的社区维护分支（列表与看板拖拽，动效自然）；从 rbd 迁移或只做列表/看板排序时选 | React |  | 开源 |
| [FormKit Drag and Drop](https://drag-and-drop.formkit.com) | 约 5KB 的数据优先拖拽排序库（React/Vue/Solid/原生皆可），直接改数组即可；简单列表排序想要最小 API 时选 | React, Vue, Solid, JS | `npm install @formkit/drag-and-drop` | 开源 |
| [gridstack.js](https://gridstackjs.com) | 框架无关的拖拽仪表盘网格布局库（有 React/Vue/Angular 封装）；非 React 项目做可拖拽看板布局时选 | JS | `npm install --save gridstack` | 开源 |
| [Headless Tree](https://headless-tree.lukasbach.com) | 无头的 React 树形组件逻辑（拖拽、多选、搜索、异步加载、虚拟化友好）；做文件树、目录树时选 | React | `npm install @headless-tree/core @headless-tree/react` | 开源 |
| [Pragmatic drag and drop](https://atlassian.design/components/pragmatic-drag-and-drop/about) | Atlassian 出品的框架无关拖拽库（基于原生 HTML5 拖拽，核心约 4.7KB，支持文件拖入）；追求性能或要跨窗口/文件拖拽时选 | JS, React | yarn add @atlaskit/pragmatic-drag-and-drop | 开源 |
| [React Arborist](https://github.com/jameskerr/react-arborist) | 开箱即用的 React 树视图（虚拟化、拖拽排序、重命名、键盘导航）；想快速得到类 VS Code 侧边栏文件树时选 | React | `npm install react-arborist` | 开源 |
| [React Grid Layout](https://github.com/react-grid-layout/react-grid-layout) | 可拖拽、可缩放的响应式网格布局（v2）；做用户可自定义的仪表盘卡片布局时选 | React | `npm install react-grid-layout` | 开源 |
| [SortableJS](https://sortablejs.github.io/Sortable/) | 零依赖的原生 JS 拖拽排序库（列表、网格、跨列表），有各框架封装；非 React 或传统页面做拖拽排序时选 | JS | `npm install sortablejs --save` | 开源 |

### 流程图 / 白板 / 节点编辑

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [React Flow（xyflow）](https://reactflow.dev) | 节点式流程图/工作流编辑器的事实标准（同仓库含 Svelte Flow），另有 shadcn 版 React Flow UI 组件；做工作流、Agent 编排、思维导图界面的默认选择（Pro 示例付费） | React, Svelte | `npm install @xyflow/react` | 免费+付费 |
| [bpmn-js](https://bpmn.io) | Camunda 团队的 BPMN 2.0 渲染与建模工具包；要符合 BPMN 标准的流程设计器时选（⚠ 授权要求保留 bpmn.io 水印） | JS |  | 免费 |
| [Fabric.js](https://fabricjs.com) | 带对象模型的 Canvas 库（选中、缩放、旋转、SVG 互转）；做图片/设计编辑器这类对象操作密集的画布时选 | JS | `npm install fabric --save` | 开源 |
| [FlowGram](https://flowgram.ai) | 字节跳动开源的工作流画布开发框架（固定布局 + 自由布局、表单引擎、变量引擎，Coze 同源）；做 AI 工作流搭建平台时选 | React | `npx @flowgram.ai/create-app@latest` | 开源 |
| [GoJS](https://gojs.net) | 商业级交互式图表库（流程图、组织架构、甘特、桑基，布局算法丰富）；预算充足且需要复杂图编辑时选（⚠ 商业授权，未授权有水印） | JS | `npm install gojs` | 付费 |
| [JointJS](https://www.jointjs.com) | 老牌图表/流程建模库（UML、BPMN、ER 图、拓扑图）；做专业建模工具时选（⚠ 核心 MPL-2.0，JointJS+ 的高级组件为商业授权） | JS | `npm add @joint/core` | 免费+付费 |
| [Konva / react-konva](https://konvajs.org) | 2D Canvas 图形框架（图层、拖拽、变换、导出图片），有 React/Vue 绑定；做海报编辑器、标注工具、自定义画布时选 | JS, React, Vue | `npm install react-konva konva` | 开源 |
| [Rete.js](https://retejs.org) | 可视化编程框架（节点编辑器 + 数据流/控制流执行引擎，可用 React/Vue/Angular/Svelte 渲染）；节点图不仅要画还要能执行时选 | JS, React, Vue, Angular, Svelte | `npx rete-kit app` | 开源 |
| [tldraw](https://tldraw.dev) | 功能完整的无限画布白板 SDK（绘图、形状、多人协作、AI 画布）；要嵌入白板或做画布类产品时选（⚠ 非开源授权：生产环境必须有 license key，商用付费、非商业可申请免费 hobby 授权） | React | `npm install tldraw` | 付费 |
| [Vue Flow](https://vueflow.dev) | React Flow 的 Vue 3 对应实现（节点、连线、缩放、小地图）；Vue 项目做流程图/节点编辑器时选 | Vue | `npm i @vue-flow/core` | 开源 |

### 地图

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [MapLibre GL JS](https://maplibre.org) | 开源的 WebGL 矢量瓦片地图引擎（Mapbox GL v1 的社区分支，无需 token）；自托管或想避开 Mapbox 计费时的默认选择，瓦片可配 OpenFreeMap | JS | `npm install maplibre-gl` | 开源 |
| [@vis.gl/react-google-maps](https://visgl.github.io/react-google-maps/) | Google 官方参与维护的 Google Maps React 组件库；必须用 Google 地图数据（海外 POI、街景）时选（⚠ 需 API key，按用量计费） | React | `npm install @vis.gl/react-google-maps` | 免费+付费 |
| [CesiumJS](https://cesium.com/platform/cesiumjs/) | 3D 地球与三维地理空间引擎（3D Tiles、地形、时间动态）；做数字孪生、三维城市、卫星轨迹时选 | JS | `npm install cesium --save` | 开源 |
| [COBE](https://cobe.vercel.app) | 约 5KB 的 WebGL 旋转地球仪；落地页想要一个带标记点的 3D 地球装饰时选 | JS |  | 开源 |
| [deck.gl](https://deck.gl) | WebGL/WebGPU 大规模地理数据可视化框架（散点、热力、轨迹、3D 图层）；百万级地理数据叠加到地图上时选 | JS, React | `npm install deck.gl` | 开源 |
| [Leaflet](https://leafletjs.com) | 最轻量普及的栅格瓦片地图库，插件极多；只要标点、画区域的普通地图且不需要 WebGL 时选 | JS |  | 开源 |
| [Mapbox GL JS](https://docs.mapbox.com/mapbox-gl-js/) | Mapbox 的矢量地图引擎（3D 地形、样式工作室、导航数据最完善）；要顶级底图设计和配套服务时选（⚠ v2 起为专有协议，必须 access token 并按加载量计费） | JS | `npm install mapbox-gl` | 免费+付费 |
| [mapcn](https://mapcn.dev) | 基于 MapLibre 的 shadcn 地图组件（标记、弹窗、路线、控件，零配置免 key）；shadcn 项目加地图最快的方式 | React, shadcn, MapLibre | `pnpm dlx shadcn@latest add @mapcn/map` | 开源 |
| [OpenFreeMap](https://openfreemap.org) | 免费、免注册、无限量的 OpenStreetMap 矢量瓦片服务（也可自托管）；给 MapLibre 找免 key 底图时用 | MapLibre |  | 免费 |
| [OpenLayers](https://openlayers.org) | 功能最全的专业 GIS 地图库（多投影、WMS/WFS、矢量编辑）；对接政企 GIS 服务或要坐标系转换时选 | JS | `npm install ol` | 开源 |
| [React Leaflet](https://react-leaflet.js.org) | Leaflet 的 React 组件封装；React 项目要用 Leaflet 时选（⚠ 采用 Hippocratic 2.1 伦理许可证，非标准开源协议，商用前先确认） | React |  | 免费 |
| [react-map-gl](https://visgl.github.io/react-map-gl/) | vis.gl 的 MapLibre / Mapbox GL React 封装（声明式图层、标记、弹窗）；在 React 里用这两个引擎时选 | React | `npm install react-map-gl maplibre-gl` | 开源 |
| [shadcnmaps](https://shadcnmaps.com) | 170+ 纯 SVG 的交互地图组件（世界、各大洲、国家、美国各州），无瓦片无 key；做分地区数据着色图时选 | React, shadcn | `npx shadcn@latest add @shadcnmaps/<item>` | 免费 |
| [高德地图 JS API 2.0](https://lbs.amap.com/api/javascript-api-v2/summary) | 高德的 Web 地图 SDK（国内底图、POI 搜索、路线规划合规可用）；面向中国大陆用户的地图功能选它（⚠ 需申请 key 与安全密钥，超出免费配额计费） | JS | `npm i @amap/amap-jsapi-loader --save` | 免费+付费 |

### 轮播

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Embla Carousel](https://www.embla-carousel.com) | 轻量无依赖的轮播引擎（拖拽手感好、插件化），shadcn Carousel 的底层；React 轮播的默认选择 | JS, React, Vue, Svelte, Solid | `npm install embla-carousel-react --save` | 开源 |
| [Keen Slider](https://keen-slider.io) | 零依赖的触摸轮播库（原生手感、多框架）；老项目在用可以继续，新项目优先 Embla（维护模式，2023 年后无新版本） | JS, React, Vue | `npm install keen-slider` | 开源 |
| [PhotoSwipe](https://photoswipe.com) | 经典的原生 JS 图片灯箱（手势缩放、移动端体验好）；非 React 项目要相册浏览时选（v5 稳定，更新不频繁） | JS | `npm i photoswipe --save` | 开源 |
| [Swiper](https://swiperjs.com) | 功能最全的触摸滑动轮播（3D 效果、视差、虚拟滑块、缩略图联动）；要现成的花式切换效果或移动端全屏滑动时选 | JS, React, Vue | `npm install swiper` | 开源 |
| [Yet Another React Lightbox](https://yet-another-react-lightbox.com) | 现代 React 图片灯箱（缩放、缩略图、视频、全屏等插件）；点击图片放大并左右翻看时选 | React | `npm install yet-another-react-lightbox` | 开源 |

### 弹层 / 通知 / 命令面板

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Sonner](https://sonner.emilkowal.ski) | Emil Kowalski 的堆叠式 Toast 组件（动效细腻、Promise 状态、API 极简），shadcn 默认 Toast；React 通知提示的默认选择 | React | `npm install sonner` | 开源 |
| [cmdk](https://github.com/dip/cmdk) | 无样式的 ⌘K 命令面板组件（内置模糊搜索与键盘导航），shadcn Command 的底层；做命令面板或可搜索菜单时选（更新放缓但稳定） | React | `pnpm install cmdk` | 开源 |
| [Floating UI](https://floating-ui.com) | 浮层定位引擎（Tooltip、Popover、下拉的碰撞检测与自动翻转），Radix/Base UI 等都在用；自己造浮层组件时选 | JS, React, Vue | `npm install @floating-ui/react` | 开源 |
| [kbar](https://kbar.vercel.app) | 带动作注册、嵌套与快捷键管理的 ⌘K 命令面板；需要把全站动作集中注册并支持层级时选 | React | `npm install kbar` | 开源 |
| [React Hot Toast](https://react-hot-toast.com) | 轻量的 React Toast（约 5KB，支持无头模式）；想要更小体积或完全自定义渲染时选 | React | `npm install react-hot-toast` | 开源 |
| [React-Toastify](https://fkhadra.github.io/react-toastify/introduction) | 功能最丰富的 React 通知库（进度条、位置、拖动关闭、通知中心）；需要通知中心或大量配置项时选 | React | `npm install --save react-toastify` | 开源 |
| [Silk](https://silkhq.com) | 原生级手感的可滑动 Sheet 组件（底部抽屉、侧栏、卡片堆叠、详情页转场）；对移动端手势质感要求很高时选（⚠ 商业授权，商用需购买） | React | `npm install @silk-hq/components` | 付费 |
| [SweetAlert2](https://sweetalert2.github.io) | 零依赖的美化弹窗（确认框、输入框、Toast），任何框架可用；传统页面想替换原生 alert/confirm 时选 | JS |  | 开源 |
| [Vaul](https://vaul.emilkowal.ski) | 移动端手感的底部抽屉组件（可拖拽关闭、吸附点），shadcn Drawer 的底层；能用但不要期待新功能（维护模式，作者已声明不再维护） | React | `npm install vaul` | 开源 |

### 虚拟列表

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [React Virtuoso](https://virtuoso.dev) | 自动测量高度的虚拟列表（分组、反向滚动、表格、瀑布流）；聊天记录、信息流等高度不定的列表选它（⚠ 聊天专用的 Message List 为商业授权） | React | `npm install react-virtuoso`<br>`npx skills add virtuoso-dev/skills --skill react-virtuoso` | 免费+付费 |
| [react-window](https://react-window.vercel.app) | 经典的 React 列表/网格虚拟化组件（v2 重写，API 更简单）；只要固定或可测高度的长列表时选 | React | `npm install react-window` | 开源 |
| [virtua](https://github.com/inokawa/virtua) | 零配置的虚拟列表（约 3KB，支持 React/Vue/Solid/Svelte，动态高度自动处理）；想最少代码完成虚拟滚动时选 | React, Vue, Solid, Svelte | `npm install virtua` | 开源 |

### 文件上传

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [react-dropzone](https://react-dropzone.js.org) | 拖拽选文件的无头 React hook（只管文件选择与校验，不管上传）；自己写上传逻辑时做拖拽区的默认选择 | React | `npm install react-dropzone` | 开源 |
| [Better Upload](https://better-upload.com) | 直传任意 S3 兼容存储的 React 上传库（预签名 URL、分片、shadcn 上传组件）；想用自己的 S3/R2 桶而不是托管服务时选 | React, shadcn | `npm i @better-upload/server @better-upload/client` | 开源 |
| [Cropper.js](https://fengyuanchen.github.io/cropperjs/) | 原生 JS 图片裁剪库（v2 改为 Web Components 架构）；非 React 项目或需要精细裁剪控制时选 | JS, Web Components | `npm install cropperjs` | 开源 |
| [FilePond](https://pqina.nl/filepond/) | 带精致动效的上传控件（图片预览、裁剪、压缩等插件，多框架适配）；想要开箱即用的漂亮上传框时选 | JS, React, Vue, Svelte, Angular | `npm install filepond` | 开源 |
| [react-easy-crop](https://github.com/ValentinH/react-easy-crop) | 手势友好的图片/视频裁剪组件（缩放、旋转、固定比例）；做头像或封面上传前的裁剪时选 | React | `npm install react-easy-crop --save` | 开源 |

### 媒体（视频 / 音频 / PDF）

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Video.js 10](https://videojs.org) | Video.js、Vidstack、Plyr、Media Chrome 四个团队合并后的新一代播放器（可组合控件、React/HTML 两套、HLS/DASH）；现在做网页视频播放器的默认选择 | React, Web Components | `npm install @videojs/react`<br>`npx @videojs/cli agents init` | 开源 |
| [@react-pdf/renderer](https://react-pdf.org) | 用 React 组件生成 PDF 文件（浏览器与服务端皆可）；做发票、报告、证书导出时选（注意与上面的 PDF 查看器不是同一个库） | React | yarn add @react-pdf/renderer | 开源 |
| [audio/ui](https://www.audio-ui.dev) | 面向音频应用的 React 控件库（旋钮、推子、XY 垫、电平表、波形、音序器、钢琴卷帘），支持 shadcn CLI；做 DAW、合成器类界面时选 | React, shadcn | `npm install @audio-ui/react`<br>`npx shadcn@latest add @audio-ui/knob` | 开源 |
| [EmbedPDF](https://www.embedpdf.com) | 基于 PDFium WASM 的开源 PDF 查看器（批注、涂黑、搜索、缩略图，无头 + 现成 UI）；需要批注/签署等比 react-pdf 更完整的阅读器时选 | React, Vue, Svelte, JS | `npm install @embedpdf/viewer-react` | 开源 |
| [hls.js](https://github.com/video-dev/hls.js) | 在不原生支持 HLS 的浏览器里播放 m3u8 流的底层库；自己控制 video 元素并需要 HLS 直播/点播时用 | JS | `npm install --save hls.js` | 开源 |
| [Limeplay](https://limeplay.winoffrg.dev) | 基于 Shaka Player 的 shadcn 风格播放器 UI 组件（复制到项目自行改样式）；shadcn 项目要自定义播放器皮肤时选，项目较小 | React, shadcn | `npx shadcn@latest add @limeplay/video-player` | 开源 |
| [PDF.js](https://mozilla.github.io/pdf.js/) | Mozilla 的 PDF 解析与渲染引擎（npm 包 pdfjs-dist）；需要底层控制或在非 React 环境渲染 PDF 时直接用 | JS |  | 开源 |
| [Plyr](https://plyr.io) | 轻量的 HTML5/YouTube/Vimeo 播放器皮肤；老项目可继续用，新项目请转 Video.js 10（维护模式，官方已宣布弃用、仅安全更新） | JS |  | 开源 |
| [React-PDF（wojtekmaj）](https://projects.wojtekmaj.pl/react-pdf/) | 在 React 中显示 PDF 的组件（基于 PDF.js，按页渲染、文本层可选中）；只需要在页面里展示 PDF 时选 | React | `npm install react-pdf` | 开源 |
| [ReactPlayer](https://github.com/cookpete/react-player) | 一个组件播放多种来源（本地文件、HLS、YouTube、Vimeo、Mux 等）；需要统一嵌入各平台视频链接时选 | React | `npm install react-player` | 开源 |
| [Vidstack Player](https://vidstack.io) | 现代可定制的视频/音频播放器组件（React 与 Web Components）；已在用可继续，新项目请转 Video.js 10（维护模式，仅安全更新至 2028 年 1 月） | React, Web Components |  | 开源 |
| [wavesurfer.js](https://wavesurfer.xyz) | 音频波形可视化与播放库（区域标注、时间轴、录音、频谱插件）；做播客、语音消息、音频剪辑界面时选 | JS | `npm install --save wavesurfer.js` | 开源 |

### Markdown 渲染与代码高亮

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [Code Hike](https://codehike.org) | 把 Markdown 代码块变成交互式讲解的工具包（滚动联动、聚焦、标注、代码动画）；写技术教程或逐步讲解代码时选 | React, MDX |  | 开源 |
| [Diffs（@pierre/diffs）](https://diffs.com) | Pierre 开源的代码 diff 渲染库（基于 Shiki，分栏/内联、虚拟化、行内批注，React 与原生 API）；做代码评审或 AI 改动预览界面时选 | React, JS | `npm install @pierre/diffs`<br>`npx skills add pierrecomputer/pierre --skill diffs` | 开源 |
| [git-diff-view](https://github.com/MrWangJustToDo/git-diff-view) | GitHub 风格的 diff 视图组件（React/Vue/Solid/Svelte，支持高亮与评论插槽）；要还原 GitHub PR 文件对比界面时选 | React, Vue, Solid, Svelte | `npm install @git-diff-view/react` | 开源 |
| [highlight.js](https://highlightjs.org) | 老牌的运行时代码高亮库（自动识别语言，零依赖）；需要在浏览器端对动态内容即时高亮时选 | JS | `npm install highlight.js` | 开源 |
| [KaTeX](https://katex.org) | 最快的网页数学公式渲染库（LaTeX 语法，可服务端渲染）；Markdown 或聊天界面需要显示公式时选 | JS | `npm install katex` | 开源 |
| [markdown-to-jsx](https://markdown-to-jsx.quantizor.dev) | 轻量的 Markdown 转 JSX 组件（无 remark 依赖，体积小）；对包体敏感且不需要插件生态时选 | React | `npm i markdown-to-jsx` | 开源 |
| [Marked](https://marked.js.org) | 快速的 Markdown 转 HTML 解析器（框架无关）；非 React 环境或服务端批量转换时选（⚠ 输出需自行做 XSS 清洗） | JS | `npm install marked` | 开源 |
| [react-syntax-highlighter](https://github.com/react-syntax-highlighter/react-syntax-highlighter) | 基于 Prism / highlight.js 的 React 代码高亮组件；配合 react-markdown 在客户端高亮代码块的常见方案 | React | `npm install react-syntax-highlighter --save` | 开源 |
| [Rehype Pretty Code](https://rehype-pretty.pages.dev) | 基于 Shiki 的 rehype 插件（行高亮、词高亮、标题、行号）；MDX/Markdown 管线里要漂亮代码块时选 | MDX, Shiki | `npm install rehype-pretty-code shiki` | 开源 |

### 认证界面

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Clerk Components](https://clerk.com/docs/reference/components/overview) | Clerk 的现成认证组件（SignIn、SignUp、UserButton、组织切换，另有 shadcn registry）；想最快得到完整登录注册与用户管理界面时选（⚠ 托管服务，超出免费用户数收费） | React, Next.js | `npm install @clerk/nextjs` | 免费+付费 |
| [Better Auth UI](https://better-auth-ui.com) | Better Auth 的即插即用认证界面（登录、注册、账号设置、组织等，shadcn 与 HeroUI 两种实现）；自托管认证选了 Better Auth 时配它 | React, shadcn, Better Auth | `bunx --bun shadcn@latest add @better-auth-ui/auth` | 开源 |

### 其他

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Driver.js](https://driverjs.com) | 轻量零依赖的产品导览与元素高亮库（框架无关）；做新手引导、功能聚光灯的默认选择 | JS | `npm install driver.js` | 开源 |
| ⭐ [qrcode.react](https://github.com/zpao/qrcode.react) | 把字符串渲染成二维码的 React 组件（SVG/Canvas，可嵌 logo）；React 里生成二维码的默认选择 | React | `npm install qrcode.react` | 开源 |
| ⭐ [react-resizable-panels](https://react-resizable-panels.vercel.app) | 可拖拽调整大小的分栏面板（可折叠、布局持久化、键盘可用），shadcn Resizable 的底层；做 IDE 式分栏布局的默认选择 | React | `npm install react-resizable-panels` | 开源 |
| ⭐ [xterm.js](https://xtermjs.org) | 浏览器里的终端模拟器（VS Code 终端同款，WebGL 渲染、插件体系）；做 Web 终端、云 IDE、SSH 面板的默认选择 | JS | `npm install --save @xterm/xterm` | 开源 |
| [<model-viewer>](https://modelviewer.dev) | Google 的 3D 模型展示 Web Component（glTF/GLB，旋转缩放、AR 预览）；电商商品 3D 展示这类只读场景选它，比手写 Three.js 省事 | Web Components | `npm install @google/model-viewer` | 开源 |
| [@uiw/react-color](https://uiwjs.github.io/react-color/) | 一整套取色器组件（Sketch、Chrome、Wheel、Swatch、Compact 等十多种样式）；需要仿设计软件的各式取色面板时选 | React | `npm i @uiw/react-color` | 开源 |
| [@uiw/react-json-view](https://uiwjs.github.io/react-json-view/) | 可折叠的 JSON 树查看/编辑组件（主题、复制、类型标注）；调试面板、API 响应预览时选 | React | `npm install @uiw/react-json-view` | 开源 |
| [@yudiel/react-qr-scanner](https://github.com/yudielcurbelo/react-qr-scanner) | 调用摄像头扫描二维码/条形码的 React 组件；需要在网页里扫码时选 | React | `npm install @yudiel/react-qr-scanner` | 开源 |
| [Allotment](https://allotment.mulberryhousesoftware.com) | 源自 VS Code 分割视图的 React 分栏组件；想要与 VS Code 一致的拖拽分隔手感时选 | React | `npm install allotment` | 开源 |
| [asciinema player](https://docs.asciinema.org/manual/player/) | 播放终端录屏（.cast 文件）的网页播放器，文字可复制；文档或落地页展示 CLI 操作演示时选 | JS | `npm install --save-dev asciinema-player` | 开源 |
| [BillingSDK](https://billingsdk.com) | 面向 SaaS 的计费界面组件（价格表、订阅管理、用量、发票、取消流程），shadcn 方式安装；做订阅计费页面时选（⚠ GPL-3.0 许可） | React, shadcn | `npx @billingsdk/cli init`<br>`npx shadcn@latest add @billingsdk/[component-name]` | 开源 |
| [Bryntum](https://bryntum.com) | 商业级的 Gantt、Scheduler、Calendar、Grid、看板组件套件（React/Vue/Angular 皆可）；做排程、资源调度类重型产品且有预算时选（⚠ 纯商业授权） | JS, React, Vue, Angular |  | 付费 |
| [c15t](https://c15t.com) | 开源的 Cookie 同意与隐私偏好方案（横幅、偏好弹窗、脚本拦截，支持 Next.js/React/TanStack Start）；需要合规的 Cookie 弹窗时选 | React, Next.js | `npx @inth/cli c15t`<br>`npx skills add c15t/skills` | 开源 |
| [canvas-confetti](https://www.kirilv.com/canvas-confetti/) | 浏览器里的五彩纸屑/烟花动画（Canvas，可自定义形状与发射方向）；支付成功、任务完成等庆祝时刻用 | JS | `npm install --save canvas-confetti` | 开源 |
| [DHTMLX Gantt](https://dhtmlx.com/docs/products/dhtmlxGantt/) | 老牌的企业级甘特图组件（资源负载、关键路径、基线、导出）；做专业项目管理软件时选（⚠ 标准版开源，资源管理等 PRO 功能需商业授权） | JS | `npm install dhtmlx-gantt` | 免费+付费 |
| [Dockview](https://dockview.dev) | 零依赖的停靠式布局管理器（标签页、分组、浮动面板、弹出窗口）；做类 IDE 的可拖拽停靠工作台时选 | JS, React, Vue, Angular | `npm install dockview` | 开源 |
| [Emoji Mart](https://github.com/missive/emoji-mart) | 曾经最流行的表情选择器（Web Component，可用于任何框架）；老项目在用可继续，新项目优先 Frimousse（维护模式，2024 年后无更新） | Web Components, React | `npm install --save emoji-mart @emoji-mart/data @emoji-mart/react` | 开源 |
| [emoji-picker-element](https://nolanlawson.github.io/emoji-picker-element/) | 轻量的 Web Component 表情选择器（数据存 IndexedDB、内存占用低）；非 React 项目要表情选择时选 | Web Components | `npm install emoji-picker-element` | 开源 |
| [emoji-picker-react](https://github.com/ealush/emoji-picker-react) | 自带完整 UI 的 React 表情选择器（搜索、肤色、多套表情风格）；想直接放一个成品面板时选 | React | `npm install emoji-picker-react` | 开源 |
| [Frappe Gantt](https://frappe.io/gantt) | 简洁的开源 SVG 甘特图（拖拽调整工期、依赖连线、多时间粒度）；只要一个轻量的项目排期图时选 | JS | `npm install frappe-gantt` | 开源 |
| [Frimousse](https://frimousse.liveblocks.io) | Liveblocks 出的无样式可组合表情选择器（轻量、数据按需加载，提供 shadcn 版）；React 表情选择器的首选 | React, shadcn | `npm i frimousse`<br>`npx shadcn@latest add https://frimousse.liveblocks.io/r/emoji-picker` | 开源 |
| [ghostty-web](https://github.com/coder/ghostty-web) | Coder 把 Ghostty 终端内核编译成 WASM 的网页终端，API 兼容 xterm.js；想要更准确的终端转义序列与 Unicode 处理时可替换试用，尚在 0.x | JS, WASM | `npm install ghostty-web` | 开源 |
| [giscus](https://giscus.app) | 基于 GitHub Discussions 的评论系统（无广告、免数据库，有 React/Vue/Svelte 组件）；给博客或文档站加评论区时选 | React, Vue, Svelte, Web Components | `npm i @giscus/react` | 免费 |
| [GrapesJS](https://grapesjs.com) | 框架无关的网页/邮件模板可视化搭建框架（拖拽块、样式管理器、输出 HTML/CSS）；做建站器或邮件编辑器时选（Studio SDK 为付费） | JS | `npm i grapesjs` | 免费+付费 |
| [Intro.js](https://introjs.com) | 老牌的分步引导与提示库；传统页面要快速加引导时可选（⚠ AGPL-3.0，商业使用需购买授权） | JS | `npm install intro.js --save` | 免费+付费 |
| [JsBarcode](https://lindell.me/JsBarcode/) | 生成 CODE128、EAN、UPC 等一维条形码的 JS 库；做商品标签、票据条码时选 | JS | `npm install jsbarcode --save` | 开源 |
| [LDRS](https://uiball.com/ldrs/) | 40+ 个轻量加载动画（Web Component，可调颜色/大小/速度）；想要比转圈更有设计感的 loading 时选 | Web Components, React | `npm install ldrs` | 开源 |
| [Masonic](https://github.com/jaredLunde/masonic) | 高性能虚拟化瀑布流网格（自动测量、可渲染上万条）；做 Pinterest 式无限滚动图片墙时选 | React | `npm i masonic` | 开源 |
| [NextStep.js](https://nextstepjs.com) | 面向 Next.js / React Router 的轻量引导库（可跨路由、Motion 动画）；Next.js 项目做跨页面 onboarding 时选 | React, Next.js, Motion | `npm i nextstepjs motion` | 开源 |
| [NumberFlow](https://number-flow.barvian.me) | 数字滚动过渡动画组件（React/Vue/Svelte，支持 Intl 格式化、无依赖）；价格、统计数字、计数器变化要有动画时选 | React, Vue, Svelte |  | 开源 |
| [Puck](https://puckeditor.com) | 面向 React 的开源可视化页面编辑器（拖拽你自己的组件、输出 JSON、可自托管，带 AI 生成）；给 CMS 或后台加页面搭建能力时选 | React, Next.js | `npx create-puck-app my-app` | 开源 |
| [QR Code Styling](https://qr-code-styling.com) | 可高度美化的二维码生成库（圆点、渐变、logo、导出图片）；要品牌化的花式二维码时选 | JS | `npm install qr-code-styling` | 开源 |
| [React Joyride](https://react-joyride.com) | React 的分步导览组件（v3，受控模式、自定义气泡、带 Agent Skill）；导览流程要和 React 状态深度联动时选 | React | `npm i react-joyride`<br>`npx skills add gilbarbara/react-joyride` | 开源 |
| [React Photo Album](https://react-photo-album.com) | 响应式相册布局组件（行式、列式、瀑布流三种，SSR 友好）；做摄影作品集、图片画廊时选 | React | `npm install react-photo-album` | 开源 |
| [react-colorful](https://github.com/omgovich/react-colorful) | 约 2.8KB 的 React 取色器（HEX/RGB/HSL，零依赖、可访问）；只要一个小巧的颜色选择面板时选 | React | `npm install react-colorful` | 开源 |
| [react-tweet](https://react-tweet.vercel.app) | Vercel 的静态推文嵌入组件（无需官方 iframe 脚本，支持 RSC）；在落地页或博客里嵌入 X/Twitter 帖子时选 | React, Next.js | `npm install react-tweet` | 开源 |
| [react-zoom-pan-pinch](https://github.com/BetterTyped/react-zoom-pan-pinch) | 给任意元素加缩放、平移、双指捏合的 React 组件；做图片查看器、地图式大图浏览时选 | React | `npm install --save react-zoom-pan-pinch` | 开源 |
| [Shepherd.js](https://www.shepherdjs.dev) | 功能完整的产品导览库（多框架封装、可访问）；需要成熟导览方案时可选（⚠ AGPL-3.0 或商业授权，商业产品需付费） | JS | `npm install shepherd.js` | 免费+付费 |
| [Signature Pad](https://github.com/szimek/signature_pad) | 基于 Canvas 的平滑手写签名库（贝塞尔插值、可导出 PNG/SVG）；做电子签名、手写输入时选 | JS | `npm install --save signature_pad` | 开源 |
| [Stepperize](https://stepperize.vercel.app) | 类型安全的无头步骤条/向导逻辑库（配 shadcn Stepper 示例）；做多步表单、注册向导的流程控制时选 | React | `pnpm add @stepperize/react` | 开源 |
| [SVAR React Gantt](https://svar.dev/react/gantt/) | 功能较全的 MIT React 甘特图（任务树、依赖、拖拽、虚拟滚动）；要免费且交互完整的甘特图时选（PRO 版另含关键路径等高级功能） | React |  | 免费+付费 |
| [vanilla-cookieconsent](https://cookieconsent.orestbida.com) | 零依赖的原生 JS Cookie 同意插件（多语言、分类同意、可访问）；任何技术栈都能用的轻量 Cookie 横幅 | JS | `npm i vanilla-cookieconsent` | 开源 |
