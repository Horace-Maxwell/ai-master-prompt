# 动效 / 特效词汇速查表

> 用途：把「我想要那种……的感觉」翻译成 AI 听得懂的专业名称。说出名称 + 一句描述 + 实现方式，AI 的还原度会高很多。
> 想看实时演示：[motion-prompt 画廊](https://showheyohtaki.github.io/motion-prompt/)（192 个，可按编号引用）、[Motion Library](https://chengwq95.github.io/motion-library/)（510 个）、[aimotions](https://aimotions.art)（文字动效 195 种）。
> 「推荐实现」一列是常见做法，不是唯一做法。写成 `@命名空间/条目名` 的可以直接 `npx shadcn@latest add <它>` 安装（均已核实存在）；React Bits 的条目名必须带 `-TS-TW` 这类变体后缀。

## 滚动类（Scroll）

| 名称 | 中文 | 看起来是什么样 | 推荐实现 |
|---|---|---|---|
| Smooth Scroll | 平滑滚动 | 滚轮滚动带惯性，丝滑不卡顿 | Lenis |
| Scroll-triggered Reveal | 滚动触发显现 | 元素滚到视口时淡入/上移/缩放出现 | Motion `whileInView` / GSAP ScrollTrigger |
| Parallax | 视差 | 前景和背景以不同速度移动，产生纵深 | Motion `useScroll` + `useTransform` |
| Pinned Section / Scrollytelling | 固定区块 / 滚动叙事 | 某区块固定在屏幕上，滚动时内容在其中逐步切换 | GSAP ScrollTrigger `pin` |
| Horizontal Scroll Section | 横向滚动区 | 竖向滚动时，一段内容横向平移 | GSAP ScrollTrigger + `xPercent` |
| Scroll Progress Bar | 滚动进度条 | 顶部细条随阅读进度增长 | Motion `scrollYProgress` |
| Scroll-linked Video / Image Sequence | 滚动驱动视频 / 帧序列 | 滚动控制视频或图片帧播放（苹果产品页那种） | canvas + 帧序列 + ScrollTrigger |
| Sticky Stack Cards | 堆叠卡片 | 卡片滚动时依次叠在上一张上面 | CSS `position: sticky` + scale |
| Zoom Parallax | 缩放视差 | 滚动时图片从小放大到全屏 | Motion `useScroll` |
| Text Reveal on Scroll | 滚动逐字显现 | 文字随滚动从灰变亮，逐词点亮 | SplitText + ScrollTrigger |

## 文字类（Text）

| 名称 | 中文 | 看起来是什么样 | 推荐实现 |
|---|---|---|---|
| Typewriter | 打字机 | 文字一个个打出来，带闪烁光标 | React Bits / 自写 |
| Text Scramble / Decrypt | 乱码解密 | 字母快速乱跳后定格成正确文字 | `@react-bits/DecryptedText-TS-TW` |
| Split Text Stagger | 拆字错峰入场 | 每个字/词依次从下方滑入 | GSAP SplitText / Motion stagger |
| Gradient Text / Animated Gradient | 渐变文字 / 流动渐变 | 文字填充渐变色并缓慢流动 | `background-clip: text` |
| Shimmer / Shine Text | 扫光文字 | 一道高光从左到右扫过文字 | `@magicui/animated-shiny-text` |
| Text Rotate / Flip Words | 轮换词 | 标题中的一个词循环切换 | `@aceternity/flip-words` |
| Blur In | 模糊入场 | 文字从模糊到清晰出现 | Motion `filter: blur` |
| Glitch Text | 故障文字 | RGB 分离、抖动、错位 | CSS 伪元素 + clip-path |
| Number Ticker / Counter | 数字滚动 | 数字从 0 滚动到目标值 | `@magicui/number-ticker` |
| Variable Font Hover | 可变字体悬停 | 鼠标靠近时字重/宽度变化 | 可变字体 + `font-variation-settings` |
| Marquee | 跑马灯 | 文字或 Logo 无限横向滚动 | `@magicui/marquee` |

## 悬停与微交互（Hover / Micro-interaction）

| 名称 | 中文 | 看起来是什么样 | 推荐实现 |
|---|---|---|---|
| Magnetic Button | 磁吸按钮 | 鼠标靠近时按钮被「吸」过去 | `@react-bits/Magnet-TS-TW`；或自写：Motion `useSpring` 跟随指针位置，离开时回弹 |
| 3D Tilt Card | 3D 倾斜卡片 | 卡片跟随鼠标倾斜，有透视感 | `@aceternity/3d-card` |
| Spotlight / Glow Follow | 聚光灯跟随 | 光斑跟着鼠标在卡片上移动 | `@aceternity/spotlight` / radial-gradient |
| Border Beam | 边框流光 | 一道光沿卡片边框绕圈 | `@magicui/border-beam` |
| Ripple | 涟漪 | 点击处扩散出波纹 | CSS / Magic UI |
| Hover Underline (from center) | 中心展开下划线 | 下划线从中间向两边展开 | Hover.css |
| Shine Sweep | 扫光 | 悬停时一道斜光扫过按钮 | CSS 伪元素 |
| Spring Press | 弹簧按压 | 按下缩小、松开回弹 | Motion `whileTap` |
| Dock Magnification | Dock 放大 | 像 macOS Dock，鼠标附近图标放大 | `@magicui/dock` |
| Skeleton Shimmer | 骨架屏扫光 | 加载占位块上有光带扫过 | shadcn `Skeleton` |
| Confetti | 撒花 | 成功时彩纸爆开 | `@magicui/confetti` |

## 布局与转场（Layout / Transition）

| 名称 | 中文 | 看起来是什么样 | 推荐实现 |
|---|---|---|---|
| Shared Element / Layout Animation | 共享元素过渡 | 卡片点击后平滑放大成详情页 | Motion `layoutId` |
| View Transition | 视图过渡 | 页面切换时元素平滑变形 | View Transitions API |
| Page Transition (curtain/wipe) | 幕布转场 | 色块扫过屏幕后切到新页面 | Motion `AnimatePresence` / Barba |
| Staggered Grid | 网格错峰 | 网格项依次入场 | Motion stagger |
| Bento Grid | 便当网格 | 大小不一的卡片拼成的网格（苹果发布会风） | `@magicui/bento-grid` |
| Accordion / Disclosure | 手风琴 | 点击展开收起（注意组件名有多种叫法） | shadcn `Accordion` |
| Morphing Dialog | 变形弹窗 | 按钮直接变形成弹窗 | Motion Primitives |
| Expandable Card | 可展开卡片 | 卡片展开占满屏幕 | Aceternity |
| Infinite Carousel | 无限轮播 | 无缝循环的轮播 | Embla |
| FLIP Reorder | 列表重排动画 | 列表排序变化时元素平滑移动 | AutoAnimate |

## 背景与氛围（Background）

| 名称 | 中文 | 看起来是什么样 | 推荐实现 |
|---|---|---|---|
| Aurora | 极光背景 | 柔和流动的彩色光带 | `@aceternity/aurora-background` / `@react-bits/Aurora-TS-TW` |
| Mesh Gradient | 网格渐变 | 多色柔和渐变缓慢流动 | Paper Shaders / ShaderGradient |
| Grain / Noise Overlay | 颗粒噪点 | 整体覆盖胶片颗粒质感 | SVG feTurbulence / Paper Shaders |
| Dot / Grid Pattern | 点阵 / 网格背景 | 细点或细线网格，常带渐隐遮罩 | `@magicui/dot-pattern` |
| Particles / Starfield | 粒子 / 星空 | 漂浮粒子，可随鼠标互动 | tsParticles / React Bits |
| Beams / Light Rays | 光束 | 从某点射出的光线 | `@aceternity/background-beams` |
| Meteors | 流星 | 斜向划过的流星线 | `@magicui/meteors` |
| Globe | 地球 | 可旋转的 3D 地球（带连线/光点） | `@magicui/globe` / cobe |
| Liquid / Metaball / Gooey | 液态 / 融球 | 元素像液体一样拉伸、融合、滴落 | SVG goo filter / goopUI（Vue） |
| Fluid Simulation | 流体模拟 | 鼠标拖动产生烟雾般流体 | WebGL fluid / `@react-bits/SplashCursor-TS-TW` |
| Glassmorphism | 玻璃拟态 | 半透明毛玻璃面板 | Web：`backdrop-filter: blur`；React Native：`expo-blur` |
| Liquid Glass | 液态玻璃 | 苹果 iOS 26 风，带折射和高光的玻璃 | Web：glasscn / liquid-glass-react；React Native：`expo-glass-effect` |

## 光标（Cursor）

| 名称 | 中文 | 看起来是什么样 | 推荐实现 |
|---|---|---|---|
| Custom Cursor / Cursor Follower | 自定义光标 | 圆点光标延迟跟随，悬停时变大 | Motion spring |
| Cursor Trail | 光标拖尾 | 光标后面拖出轨迹 | canvas |
| Image Trail | 图片拖尾 | 鼠标移动时沿路径冒出图片 | React Bits / Codrops |
| Blend-mode Cursor | 反色光标 | 光标经过处颜色反转 | `mix-blend-mode: difference` |

## 3D 与 WebGL

| 名称 | 中文 | 看起来是什么样 | 推荐实现 |
|---|---|---|---|
| Hero 3D Model | 3D 主视觉 | 可旋转/随滚动转动的 3D 模型 | React Three Fiber / Spline |
| Distortion Hover | 扭曲悬停 | 鼠标悬停图片时产生水波扭曲 | WebGL shader / Unicorn Studio |
| Displacement Transition | 置换转场 | 图片切换时用噪声贴图溶解过渡 | three.js shader |
| Infinite 3D Gallery | 无限 3D 画廊 | 图片在 3D 空间中排列可拖拽 | R3F + drei |

## 镜头运动（视频 / 动画 / 3D 场景）

| 名称 | 中文 | 说明 |
|---|---|---|
| Pan / Tilt | 横摇 / 纵摇 | 机位不动，镜头左右 / 上下转 |
| Truck / Pedestal | 横移 / 升降 | 整个机位左右 / 上下平移 |
| Dolly In / Out | 推 / 拉 | 机位向主体靠近 / 远离 |
| Dolly Zoom (Vertigo) | 希区柯克变焦 | 推拉同时反向变焦，背景透视扭曲 |
| Orbit / Arc | 环绕 | 绕主体旋转拍摄 |
| Crane / Jib | 摇臂 | 大幅度升降 + 移动 |
| Tracking / Follow Shot | 跟拍 | 跟随运动主体 |
| Whip Pan | 甩镜 | 快速横摇产生动态模糊，常做转场 |
| Rack Focus | 移焦 | 焦点从前景转到背景 |
| FPV Drone | 穿越机 | 高速穿梭的第一视角飞行 |
| Match Cut | 匹配剪辑 | 形状/动作相同的两个画面硬切 |

## 摄影与画面风格（图像生成）

| 名称 | 说明 |
|---|---|
| Golden Hour / Blue Hour | 日出日落暖光 / 日落后冷蓝光 |
| Rembrandt / Butterfly / Split Lighting | 经典人像布光：三角光 / 蝴蝶光 / 侧光 |
| Rim Light / Backlight | 轮廓光 / 逆光 |
| Chiaroscuro / Low-key / High-key | 明暗对比 / 暗调 / 亮调 |
| Shallow Depth of Field / Bokeh | 浅景深 / 焦外光斑 |
| Tilt-shift | 移轴（微缩模型感） |
| Long Exposure | 长曝光（光轨、丝滑流水） |
| Film Grain / Kodak Portra / Cinestill 800T | 胶片颗粒 / 胶片型号色调 |
| Anamorphic Lens Flare | 变形宽银幕镜头的横向光晕 |
| Isometric / Flat Lay / Macro | 等距视角 / 平铺俯拍 / 微距 |

更多：[Google Veo 提示指南](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)、[StudioBinder 镜头大全](https://www.studiobinder.com/blog/different-types-of-camera-movements-in-film/)、[Midlibrary](https://midlibrary.io)。
