# 动画引擎与底层库

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-animation-engines"></a>

## 动画引擎 / 滚动 / 3D 底层库

组件库背后的引擎。自己写动效时选这里。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [GSAP](https://gsap.com) | 时间轴与滚动动画（ScrollTrigger）。2025-04-30 起完全免费（含 SplitText、MorphSVG） | JS | `npx skills add https://github.com/greensock/gsap-skills` | 免费 |
| ⭐ [Lenis](https://lenis.dev) | 平滑滚动，高级感网站标配 |  | llms.txt: https://lenis.dev/llms.txt | 免费 |
| ⭐ [Motion（原 Framer Motion）](https://motion.dev) | React/JS/Vue 动画首选。布局动画、手势、滚动 | React, JS, Vue | `npx motion-ai` | 免费+付费 |
| ⭐ [Three.js](https://threejs.org) | WebGL/WebGPU 3D |  | `npx skills add cloudai-x/threejs-skills` | 免费 |
| [Anime.js](https://animejs.com) | 轻量 JS 动画引擎（v4），无 llms.txt，用 Context7 | JS |  | 免费 |
| [AutoAnimate](https://auto-animate.formkit.com) | 零配置列表/布局过渡，一行代码 | React, Vue, Svelte |  | 免费 |
| [Barba.js](https://barba.js.org) | 多页面网站的页面转场 |  |  | 免费 |
| [Lottie](https://lottie.airbnb.tech/) | AE 导出的 JSON 矢量动画 |  | LottieFiles MCP | 免费 |
| [OGL](https://github.com/oframe/ogl) | 极简 WebGL 库（React Bits 很多背景特效基于它） |  |  | 免费 |
| [React Spring](https://www.react-spring.dev) | 弹簧物理动画 | React |  | 免费 |
| [React Three Fiber / drei](https://r3f.docs.pmnd.rs) | three.js 的 React 渲染器 + 常用辅助组件 | React | pmndrs MCP | 免费 |
| [Remotion](https://www.remotion.dev) | 用 React 写视频 |  | `npx skills add remotion-dev/skills` | 免费+付费 |
| [Rive](https://rive.app) | 带状态机的交互动画 |  | llms.txt: https://rive.app/llms.txt | 免费+付费 |
| [Theatre.js](https://www.theatrejs.com) | 可视化时间轴编辑器（已基本停更，2024-08 后无提交） |  |  | 免费 |
