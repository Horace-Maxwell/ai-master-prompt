# 风格配方：风格 → 用什么库 → 怎么跟 AI 说

> 每个配方写了：适合什么场景、关键视觉特征（直接放进 Prompt）、推荐的库和安装命令、要避免什么。
> 更多风格（80 种）：UI UX Pro Max Skill；要照着某个知名品牌做：[awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 里找对应的 DESIGN.md。

## 1. 手绘笔记本 / Sketch

- **适合**：教育、个人博客、创意工具、轻松可爱的产品、原型演示
- **视觉特征**：纸张纹理背景（横线或方格），抖动的钢笔描边，胶带和贴纸装饰，手写体标题（Caveat、Kalam、Patrick Hand），略微旋转的卡片，黄色荧光笔高亮
- **库**：
  - React + shadcn 项目：**Looseleaf**（123 组件，直接替换 shadcn，不改 JSX）
  - 轻量 React：**Sketchbook UI**（`npm i sketchbook-ui`）
  - 任意框架：Wired Elements；标注用 RoughNotation；底层 Rough.js
- **避免**：手绘元素铺满全屏导致可读性差；正文也用手写体

## 2. 新粗野主义 / Neo-brutalism

- **适合**：开发者工具、创意工作室、年轻化 SaaS、作品集
- **视觉特征**：粗黑描边（2–4px），硬阴影（`4px 4px 0 #000`，无模糊），高饱和撞色（亮黄、品红、青），无圆角或小圆角，粗体无衬线字体，按钮按下时阴影消失、位移
- **库**：`npx shadcn add @neobrutalism/<item>`（neobrutalism.dev）或 `@retroui`（neobrutalism.com）
- **避免**：颜色超过 4 种；加渐变

## 3. 复古像素 / 8-bit / 老系统

- **适合**：游戏、黑客松、怀旧主题、彩蛋页
- **视觉特征**：像素字体（Press Start 2P、VT323），像素边框，有限调色板，CRT 扫描线；或 Windows 95/98/XP 窗口外观
- **库**：`@8bitcn`、`@pixelact-ui`、NES.css；Windows 风：98.css / XP.css / 7.css / React95；小游戏：`@gamekitui`

## 4. 终端 / Hacker / TUI

- **适合**：CLI 工具官网、开发者产品、AI Agent 控制台
- **视觉特征**：等宽字体（JetBrains Mono、Berkeley Mono、IBM Plex Mono），深色背景，绿色或琥珀色字符，方括号按钮 `[ OK ]`，ASCII 框线，闪烁光标，打字机输出
- **库**：WebTUI、Terminal CSS；赛博朋克切角：augmented-ui

## 5. 玻璃拟态 / 液态玻璃

- **适合**：音乐/天气/系统类应用、苹果生态风格产品、Hero 展示
- **视觉特征**：半透明面板 + 背景模糊（`backdrop-filter: blur(20px)`），细白色描边，柔和高光；液态玻璃要加折射和边缘高光。背景必须足够丰富（渐变或图片），否则玻璃效果看不出来
- **库**：`@glasscn`（Apple 液态玻璃）、`@glassyui`（含 RN 版）、liquid-glass-react、css.glass 生成器；移动端 ExpoKit
- **避免**：所有元素都玻璃化；文字对比度不足

## 6. 暗色科技 / 「Linear 风」

- **适合**：SaaS、AI 产品、开发者工具落地页（最常见也最容易撞款）
- **视觉特征**：近黑背景（#0A0A0A 而非纯黑），细微网格/点阵背景加渐隐遮罩，边框流光，聚光灯跟随，渐变描边卡片，Bento 网格，紧凑的字距，单一品牌强调色
- **库**：Magic UI、Aceternity UI、React Bits；配色参考 awesome-design-md 的 Linear / Vercel DESIGN.md
- **避免撞款**：换掉 Inter（试 Geist、Satoshi、General Sans），强调色别用紫蓝渐变，加入一个独特的签名元素（自定义插画、3D、品牌动效）

## 7. 编辑 / 杂志风 Editorial

- **适合**：内容站、品牌官网、作品集、高端消费品
- **视觉特征**：大号衬线标题（Fraunces、Instrument Serif、PP Editorial），非对称网格，大量留白，细分隔线，大图出血，小号大写字母标签，缓慢优雅的滚动显现
- **库**：shadcn 基础组件 + Lenis + GSAP SplitText；字体从 Fontshare / Google Fonts

## 8. 极简 / 瑞士国际主义

- **适合**：工具类产品、文档、个人主页
- **视觉特征**：严格网格，黑白 + 一个强调色，Helvetica/Neue Haas 类无衬线，信息层级靠字号和字重而非颜色和阴影，几乎没有装饰
- **库**：shadcn 默认组件 + 精心调过的 token（tweakcn）

## 9. 柔和拟物 / Claymorphism / 可爱风

- **适合**：儿童、健康、消费类 App、插画驱动产品
- **视觉特征**：大圆角（24px+），柔和内外双阴影形成「黏土」凸起，马卡龙色，圆润字体（Nunito、Quicksand），3D 小图标
- **库**：自定义 Tailwind token；3D 图标可用 Spline 导出

## 10. 液体 / 有机 / 物理感

- **适合**：创意实验、品牌活动页、作品集
- **视觉特征**：元素会滴落、拉伸、融合（metaball / gooey），弹性物理，网格渐变背景，颗粒噪点
- **库**：goopUI（Vue/Nuxt，pre-alpha）；React 用 SVG goo filter + Motion spring；物理用 Matter.js；背景用 Paper Shaders

## 11. AI 产品 / Agent 控制台

- **适合**：Chatbot、Copilot、Agent 运维面板
- **视觉特征**：清晰的消息流，可折叠的推理/工具调用块，流式输出光标，引用来源卡片，Agent 状态时间线，成本与 token 计量，审批按钮
- **库**：AI Elements（`@ai-elements`）、assistant-ui、prompt-kit；Agent 可观测性用 affectUI（trace 瀑布、上下文窗口地图、审批闸门）

---

## 通用 Prompt 模板（选好风格后填空）

```
用 [风格名] 风格做一个 [页面类型]。
视觉特征：[从上面复制关键视觉特征]
技术栈：[Next.js + Tailwind + shadcn/ui]，组件优先从 [库名] 安装（[安装命令]）。
字体：标题 [字体]，正文 [字体]。配色：[主色/背景/强调色 hex]。
动效：[从 effect-vocabulary.md 里选 2–4 个名称]，动效强度 [克制/适中/炫]，尊重 prefers-reduced-motion。
避免：紫蓝渐变、Inter 字体、emoji 当图标、所有区块都淡入上移。
完成后用浏览器截图自检桌面端和 375px 移动端。
```
