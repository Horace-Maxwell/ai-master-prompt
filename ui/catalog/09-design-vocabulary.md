# 效果词汇表与 Prompt 库（教你怎么跟 AI 描述）

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

## 动效 / 特效词汇与可复制 Prompt

不知道一个效果叫什么？在这些画廊里点开演示，复制它的专业名称和 Prompt。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Emil Kowalski skills](https://github.com/emilkowalski/skills) | 含 animation-vocabulary（教 AI 用正确的动效术语）、animate、choreograph、apple-design、review-animations；作者是 Sonner/Vaul 作者 |  | `npx skills add emilkowalski/skills` | 免费 |
| ⭐ [motion-prompt](https://github.com/showheyohtaki/motion-prompt) | 192 个带专业名称的效果（8 包×24：动态图形、镜头运动与转场、UI 组件名、落地页/网页特效、摄影风格灯光），每个都有实时演示 + Copy Prompt；可按编号引用（#012）。画廊：showheyohtaki.github.io/motion-prompt |  | `npx skills add showheyohtaki/motion-prompt` | 免费 |
| [aimotions.art](https://aimotions.art) | 195 种命名文字动画风格（故障、材质 3D、光效 shader…），可复制 Prompt |  | `copy prompt` | 免费 |
| [Animate.css](https://animate.style) | CSS 入场/出场动画的「标准命名」来源 |  |  | 免费 |
| [Animista](https://animista.net) | CSS 动画预设及其标准名称（slide-in-blurred、flip-scale…），可在线调参 |  |  | 免费 |
| [CSSFX](https://cssfx.netlify.app) | 命名 CSS 效果，点击复制代码 |  |  | 免费 |
| [cubic-bezier.com](https://cubic-bezier.com) | 贝塞尔缓动曲线编辑器 |  |  | 免费 |
| [design-motion-principles](https://github.com/kylezantos/design-motion-principles) | 设计或审查「有目的」的动效 |  | `npx skills add kylezantos/design-motion-principles` | 免费 |
| [Easings.net](https://easings.net) | 缓动曲线标准名称（easeOutExpo…）对照图 |  |  | 免费 |
| [Hover.css](https://ianlunn.github.io/Hover/) | 命名 hover 效果（grow、sweep、underline-from-center…） |  |  | 免费 |
| [LottieFiles motion-design-skill](https://github.com/LottieFiles/motion-design-skill) | 时长、缓动、编排、迪士尼动画原则 |  | `npx skills add LottieFiles/motion-design-skill` | 免费 |
| [Motion Effects 325](https://sueun-dev.github.io/motion-effects/) | 325 个 Canvas/WebGL/three.js 效果，5 秒视频演示 + 英/韩 Prompt（新项目） |  | `copy prompt` | 免费 |
| [Motion Library（510 效果）](https://chengwq95.github.io/motion-library/) | 510 个网页效果（文字/按钮/卡片/导航…），可搜索筛选，有 React/Vue 版本，每个可复制 Prompt（新项目，星数少） |  | `copy prompt` | 免费 |
| [motion-prompt 动态画廊](https://showheyohtaki.github.io/motion-prompt/) | motion-prompt 的在线画廊，所有效果可实时播放，点 Copy Prompt 直接复制给 AI |  | `copy prompt` | 免费 |
| [NN/g UI Elements Glossary](https://www.nngroup.com/articles/ui-elements-glossary/) | 权威 UI 元素术语表 |  |  | 免费 |
| [SheCodes: Animations for AI Coders](https://books.shecodes.io/animations) | 入门级 hover/入场/循环动效术语表（Wiggle、Shimmer、Typing Dots），带 Prompt |  | `copy prompt` | 免费 |
| [Superdesign Prompt Library](https://superdesign.dev/library) | 社区设计 Prompt，按风格和页面区块分类（如 GSAP 横向画廊） |  | `Use this prompt / llms.txt` | 免费 |
| [The Component Gallery](https://component.gallery) | 90+ 设计系统里同一组件的标准叫法（Accordion/Disclosure/Collapse…），用来查组件到底叫什么 |  |  | 免费 |
| [TypeUI UI Animations](https://typeui.sh/ui-animations) | 约 281 个命名 UI 微交互（Spring slide、Dot ripple…） |  | `copy prompt / TypeUI MCP` | 免费+付费 |
| [UI-Patterns](https://ui-patterns.com) | 命名 UX 模式库 |  |  | 免费 |
| [userinterface.wiki](https://userinterface.wiki) | 「更好界面的活手册」，带演示，站内提供 Skill |  |  | 免费 |

## 设计风格 / 审美类 Skill 与 DESIGN.md

让 Agent 有审美、去 AI 味；或直接套用知名网站的设计系统（DESIGN.md）。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Anthropic 官方「去 AI 味」前端审美 Skill，避免千篇一律的紫色渐变 + Inter 字体 |  | `npx skills add anthropics/skills --skill frontend-design` | 免费 |
| ⭐ [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 从 Claude、Stripe、Linear、Vercel 等名站提取的 DESIGN.md，丢进项目根目录即可让 AI 照着这个风格做（126k★） |  | `drop-in DESIGN.md` | 免费 |
| ⭐ [Impeccable](https://impeccable.style) | 「给编码 Agent 的设计词汇」：polish/bolder/critique/audit 等命令 + AI-slop 检测器（107k★） |  | `npx impeccable install` | 免费 |
| ⭐ [Taste Skill](https://github.com/Leonxlnx/taste-skill) | 艺术指导、参考图、浏览器自检，避免通用 AI 外观（112k★） |  | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` | 免费 |
| ⭐ [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 可检索的设计数据库：80 种 UI 风格、192 种产品类型、192 套配色、74 组字体搭配 + UX 规则，自动生成设计系统（147k★） |  | `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill → /plugin install ui-ux-pro-max@ui-ux-pro-max-skill；或 npm i -g ui-ux-pro-max-cli && uipro init --ai claude` | 免费 |
| [awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design) | 68 个为 Claude Design 调过的 DESIGN.md 灵感 |  |  | 免费 |
| [awesome-design-skills](https://github.com/bergside/awesome-design-skills) | 67 个 DESIGN.md / SKILL.md 风格文件，带 pull CLI |  |  | 免费 |
| [daisyUI UI design prompts](https://trends.daisyui.com/ui-design-prompts/) | 命名风格 Prompt，做出有辨识度的界面 |  | `copy prompt` | 免费 |
| [DESIGN.md 规范（Google Labs）](https://github.com/google-labs-code/design.md) | 向 Agent 描述视觉识别的官方格式规范，附 lint 工具 |  | `npx @google/design.md lint DESIGN.md` | 免费 |
| [DesignPrompts](https://designprompts.dev) | 落地页风格构建器，选好风格后复制 Prompt 给 Agent；含词汇表 + JSON Schema |  | `copy prompt / llms.txt` | 免费+付费 |
| [getdesign.md](https://getdesign.md) | awesome-design-md 的网站版，550+ DESIGN.md 目录 |  | `copy DESIGN.md` | 免费+付费 |
| [interface-design](https://github.com/Dammyjay93/interface-design) | 跨会话保持 UI 决策一致性 |  | `npx skills add https://github.com/dammyjay93/interface-design --skill interface-design` | 免费 |
| [make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) | 界面打磨与微交互 Skill |  | `npx skills add jakubkrehel/make-interfaces-feel-better` | 免费 |
| [MengTo Skills](https://github.com/MengTo/Skills) | 视频→超级 Prompt、HTML→交互 Prompt、14 种 SVG 插画风格、3D Skill |  |  | 免费 |
| [PostHog: Engineer's guide to vibe design](https://newsletter.posthog.com/p/an-engineers-guide-to-vibe-design) | 工程师视角的 vibe design 提示指南，带示例 Prompt |  |  | 免费 |
| [Refero Styles](https://styles.refero.design) | 2000+ 真实产品的 AI 可读设计系统，每个带 DESIGN.md |  | `Refero MCP` | 免费+付费 |
| [TypeUI](https://typeui.sh) | 设计 Skill 注册表、UI Prompt、布局指导 |  | `TypeUI MCP / npx typeui.sh pull <slug>` | 免费+付费 |
| [UI Skills](https://www.ui-skills.com) | 设计工程师 Skill 注册表（含 motion 分类） |  | `npx ui-skills get baseline-ui；MCP https://www.ui-skills.com/mcp` | 免费 |
| [Vercel Web Interface Guidelines](https://vercel.com/design/guidelines) | 界面质量规则；也作为 web-design-guidelines Skill 发布 |  | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` | 免费 |

## 官方 Prompt 指南（v0 / Lovable / Bolt / Stitch / Claude）

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Claude Cookbook: Prompting for frontend aesthetics](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb) | 排版、主题、动效的 Prompt 模块，可直接拼进系统提示 |  |  | 免费 |
| [Anthropic: Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | frontend-design Skill 背后的思路与提示方法 |  |  | 免费 |
| [Bolt: Prompting effectively](https://support.bolt.new/best-practices/prompting-effectively) | Bolt 官方提示最佳实践 |  |  | 免费 |
| [Google Stitch Prompt Guide](https://stitch.withgoogle.com/docs/learn/prompting/) | Stitch 官方 UI 生成提示指南 |  |  | 免费 |
| [Lovable Prompting Handbook](https://docs.lovable.dev/prompting/prompting-one) | Lovable 官方提示手册 |  |  | 免费 |
| [Stitch Skills（Google Labs）](https://github.com/google-labs-code/stitch-skills) | Stitch MCP 配套的 design-md、shadcn-ui 等 Skill |  | `npx skills add google-labs-code/stitch-skills` | 免费 |
| [v0 text-prompting docs](https://v0.app/docs/text-prompting) | v0 官方提示指南 |  |  | 免费 |

## 镜头 / 摄影 / 灯光词汇（图像与视频生成）

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Google Veo 视频提示指南](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide) | 官方镜头运动、景别、镜头焦段、风格术语 |  |  | 免费 |
| [Atlabs: 27 种电影级布光](https://www.atlabs.ai/blog/27-cinematic-lighting-looks-ai-prompts-guide) | 命名布光风格 + 可复制修饰词 |  | `copy prompt` | 免费 |
| [FilmGrab](https://film-grab.com) | 电影截图参考库（找画面风格） |  |  | 免费 |
| [Midlibrary](https://midlibrary.io) | Midjourney 风格库：艺术家、流派、技法、胶片质感 |  |  | 免费+付费 |
| [Promptomania](https://promptomania.com) | 可视化图像 Prompt 构建器，含风格与镜头术语 |  |  | 免费 |
| [Runway AI camera prompts](https://runwayml.com/resources/ai-camera-prompts) | 镜头术语（pan vs truck、pedestal…） |  |  | 免费 |
| [StudioBinder 镜头运动大全](https://www.studiobinder.com/blog/different-types-of-camera-movements-in-film/) | 电影镜头运动/景别标准词汇，带示例 |  |  | 免费 |
