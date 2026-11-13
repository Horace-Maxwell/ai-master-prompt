# 国内生态：组件库、中后台、小程序、图表、字体

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-china"></a>

## 国内生态（Ant Design / Element / TDesign / 小程序 / AntV…）

面向国内用户、中后台、小程序、微信生态的项目优先看这里。

本类分组：React 组件库 · Vue 组件库 · 移动端 H5 · 小程序与跨端 · 中后台模板与框架 · 图表与可视化 · 低代码与工程 · 图标与设计资源 · 中文字体

### React 组件库

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Ant Design](https://ant.design) | 蚂蚁出品的企业级 React 组件库（100k★，当前 v6），中后台项目默认首选；官方提供 llms.txt、CLI 和 MCP，国内镜像 ant-design.antgroup.com | React, TS | `npm install antd`<br>llms.txt: https://ant.design/llms.txt<br>`npm install -g @ant-design/cli`<br>`npx skills add ant-design/ant-design-cli`<br>MCP: npx -y @ant-design/cli mcp | 开源 |
| [ahooks](https://ahooks.js.org) | 阿里出品的 React Hooks 工具库（useRequest、useAntdTable 等），国内 React 中后台项目几乎标配 | React, TS | `npm install --save ahooks` | 开源 |
| [Ant Design Web3](https://web3.ant.design) | Ant Design 风格的 Web3 组件（连接钱包、地址、NFT 展示等），antd 项目做 DApp 界面时选 | React, Ant Design | `npm i antd @ant-design/web3 --save` | 开源 |
| [Ant Design X](https://x.ant.design) | Ant Design 官方 AI 界面组件库（气泡、输入框、思维链等，配套 x-markdown 流式渲染和 x-sdk 模型接入），antd 技术栈做聊天 / Agent 界面时选 | React, Ant Design | `npm install @ant-design/x` | 开源 |
| [antd-style](https://ant-design.github.io/antd-style/) | 基于 Ant Design token 体系的 CSS-in-JS 方案，需要在 antd 项目里写跟随主题 / 暗色模式的自定义样式时用 | React, Ant Design, CSS-in-JS | `pnpm i antd-style -S` | 开源 |
| [Arco Design（React）](https://arco.design/react/docs/start) | 字节跳动出品的企业级 React 组件库，风格比 antd 更轻更现代，想要中后台但不想撞脸 antd 时选 | React, TS | `npm install @arco-design/web-react` | 开源 |
| [Lobe UI](https://ui.lobehub.com) | LobeHub 开源的 AIGC 应用组件库（基于 antd，含聊天、Markdown、代码高亮等），做 LobeChat 那种精致 AI 应用界面时选 | React, Ant Design | `pnpm add @lobehub/ui @lobehub/icons @lobehub/fluent-emoji motion`<br>llms.txt: https://ui.lobehub.com/llms.txt | 开源 |
| [ProComponents](https://pro-components.antdigital.dev) | 基于 Ant Design 的重型模板组件（ProTable / ProForm / ProLayout），要用配置快速堆 CRUD 页面时选；⚠ 封装层厚，深度定制成本高 | React, Ant Design | `pnpm install @ant-design/pro-components`<br>llms.txt: https://pro-components.antdigital.dev/llms.txt | 开源 |
| [Semi Design](https://semi.design) | 抖音前端出品的 React 设计系统（10k★），组件全、主题定制强，自带 Figma 设计稿转代码（D2C）和官方 MCP | React, TS | `npm install @douyinfe/semi-ui`<br>MCP: npx -y @douyinfe/semi-mcp | 开源 |
| [TDesign React](https://tdesign.tencent.com/react/overview) | 腾讯 TDesign 的 React 桌面端实现，与 Vue / 小程序 / 移动端共用同一套设计规范，多端统一风格时选 | React, TS | `npm i tdesign-react`<br>llms.txt: https://tdesign.tencent.com/llms.txt<br>MCP: npx -y tdesign-mcp-server@latest | 开源 |

### Vue 组件库

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Element Plus](https://element-plus.org) | 国内使用最广的 Vue 3 桌面端组件库（饿了么 Element 的继任者），Vue 中后台项目默认首选，官方提供 llms.txt | Vue 3, TS | `npm install element-plus --save`<br>llms.txt: https://element-plus.org/llms.txt | 开源 |
| [Ant Design Vue](https://antdv.com) | Ant Design 的 Vue 3 社区实现，想在 Vue 里用 antd 设计语言时选；⚠ npm 最新版仍是 2024-11 的 4.2.6，跟进 React 版较慢 | Vue 3, TS | `npm install ant-design-vue --save` | 开源 |
| [Ant Design X Vue](https://ant-design-x-vue.netlify.app) | Ant Design X 的 Vue 社区移植版，Ant Design Vue 项目做 AI 聊天界面时选（⚠ 非官方） | Vue 3, Ant Design Vue | `npm i ant-design-vue ant-design-x-vue` | 开源 |
| [Arco Design Vue](https://arco.design/vue/docs/start) | 字节跳动 Arco Design 的 Vue 3 版本，Vue 中后台想换一套比 Element Plus 更现代的视觉时选 | Vue 3, TS | `npm install @arco-design/web-vue` | 开源 |
| [Element Plus X](https://element-plus-x.com) | 基于 Element Plus 的企业级 AI 组件库（气泡、发送框、思考链等），Element Plus 项目加 AI 对话界面时选；v2 文档在 v2.element-plus-x.com | Vue 3, Element Plus | `npm install vue-element-plus-x` | 开源 |
| [MateChat](https://matechat.gitcode.com) | 华为 DevUI 团队的 AI 对话界面组件库（气泡、输入、提示词卡片），Vue 项目快速搭 Copilot 式助手时选 | Vue 3, DevUI | `npm i vue-devui @matechat/core @devui-design/icons` | 开源 |
| [Naive UI](https://www.naiveui.com) | 图森未来出品的 Vue 3 组件库（18k★），全 TypeScript、主题用 JS 对象定制无需 CSS 变量预处理，偏好类型安全和清爽风格时选 | Vue 3, TS | `npm i naive-ui`<br>llms.txt: https://www.naiveui.com/llms.txt | 开源 |
| [Pro Naive UI](https://naive-ui.pro-components.cn) | Naive UI 的高阶封装（ProForm / ProTable 等），Naive UI 项目想要 ProComponents 式开发体验时选（社区项目，体量小） | Vue 3, Naive UI | `npm i pro-naive-ui` | 开源 |
| [TDesign](https://tdesign.tencent.com) | 腾讯企业级设计体系总站，一套规范覆盖 Vue / React / 移动端 / 小程序 / uni-app / Flutter，多端同品牌时首选；官方提供 llms.txt 和 MCP Server | Vue 3, React, 小程序, Flutter | llms.txt: https://tdesign.tencent.com/llms.txt<br>MCP: npx -y tdesign-mcp-server@latest | 开源 |
| [TDesign Vue Next](https://tdesign.tencent.com/vue-next/overview) | TDesign 的 Vue 3 桌面端组件库，另有配套 AI 对话组件包 @tdesign-vue-next/chat，腾讯系或多端统一项目选 | Vue 3, TS | `npm i tdesign-vue-next`<br>MCP: npx -y tdesign-mcp-server@latest | 开源 |
| [TinyRobot（OpenTiny）](https://opentiny.design/tiny-robot/) | OpenTiny 的 Vue AI 对话组件库（聊天套件、工具调用与 MCP 管理界面），TinyVue 技术栈做 Agent 界面时选（较新，star 少） | Vue 3 | `npx @opentiny/tiny-robot-cli create my-app --template basic`<br>`pnpm add @opentiny/tiny-robot @opentiny/tiny-robot-chat` | 开源 |
| [TinyVue（OpenTiny）](https://opentiny.design/tiny-vue) | 华为云 OpenTiny 出品的企业级组件库，一套代码同时支持 Vue 2 / Vue 3、PC / 移动端，老 Vue 2 项目要平滑升级时选 | Vue 3, Vue 2 | `npm i @opentiny/vue@3`<br>`npx skills add opentiny/agent-skills -g --skill tiny-vue-skill --agent cursor` | 开源 |
| [Vexip UI](https://www.vexipui.com) | 高度可定制的 Vue 3 组件库，CSS 变量主题、组件覆盖全，想要小众不撞脸的中后台风格时选 | Vue 3, TS | `pnpm add vexip-ui` | 开源 |
| [View UI Plus](https://www.iviewui.com/view-ui-plus) | 原 iView 的 Vue 3 版本，主要用于维护存量 iView 项目；⚠ 社区活跃度已明显低于 Element Plus | Vue 3 | `npm install view-ui-plus --save` | 开源 |
| [Vue DevUI](https://devui.design) | 华为 DevUI 设计体系的 Vue 3 组件库（另有 Angular 版 ng-devui），偏研发工具 / 云控制台风格时选 | Vue 3, Angular | `npm install vue-devui --save` | 开源 |
| [vxe-table（Vxe UI）](https://vxeui.com) | 国内最流行的 Vue 重型表格（虚拟滚动、可编辑、树表、导出），Element / antd 自带表格扛不住大数据量或复杂编辑时选，官方提供 llms.txt | Vue 3, Vue 2 | `npm install vxe-table`<br>llms.txt: https://vxeui.com/llms.txt | 开源 |

### 移动端 H5

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Vant](https://vant-ui.github.io/vant/) | 有赞开源的 Vue 3 移动端组件库（24k★），国内 H5 电商 / 营销页事实标准，国内镜像 vant.pro | Vue 3, TS | `npm i vant` | 开源 |
| [Ant Design Mobile](https://mobile.ant.design) | Ant Design 官方移动端 React 组件库，React 技术栈做 H5 / 移动端 Web 时的国内首选 | React, TS | `npm install antd-mobile` | 开源 |
| [Arco Design Mobile](https://arco.design/mobile/react) | 字节跳动 Arco 的 React 移动端组件库，手势和动效细节好，React H5 想要 antd-mobile 之外的选择时用 | React, TS | `npm install @arco-design/mobile-react` | 开源 |
| [NutUI](https://nutui.jd.com) | 京东风格的 Vue 3 移动端组件库，同时提供 Taro 版（@nutui/nutui-taro）可一套代码出 H5 和小程序，电商场景选 | Vue 3, Taro |  | 开源 |
| [NutUI React](https://nutui.jd.com/react/) | NutUI 的 React 版本，含 H5 版和 Taro 多端版（@nutui/nutui-react-taro），React + Taro 做京东风电商小程序时选 | React, Taro |  | 开源 |
| [TDesign Mobile（Vue / React）](https://tdesign.tencent.com/mobile-vue/overview) | TDesign 的移动端 H5 组件库，Vue 版成熟、React 版刚到 1.0，和 TDesign 小程序 / 桌面端保持同一视觉时选 | Vue 3, React | `npm i tdesign-mobile-vue` | 开源 |
| [Varlet](https://varletjs.org) | Material Design 风格的 Vue 3 移动端组件库，更新勤快，想要 Material 风而不是电商风的 H5 时选 | Vue 3, TS | `npm i @varlet/ui -S` | 开源 |
| [WeUI](https://weui.io) | 微信官方设计团队的基础样式库，让 H5 页面与微信原生视觉一致，做微信内网页 / 公众号页面时用 | CSS |  | 开源 |

### 小程序与跨端

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Taro](https://taro-docs.jd.com/docs/) | 京东开源的多端统一开发框架（37k★），用 React / Vue 写一套代码编译到微信等各家小程序、H5、RN 和鸿蒙，React 团队做小程序首选；⚠ 文档域名 docs.taro.zone 证书异常，用 taro-docs.jd.com | React, Vue 3, 小程序 | `npm install -g @tarojs/cli`<br>taro init myApp<br>`npx @tarojs/cli init myApp` | 开源 |
| ⭐ [uni-app](https://uniapp.dcloud.net.cn) | DCloud 出品的 Vue 跨端框架（41k★），一套代码发 iOS / Android / 鸿蒙 / 各家小程序 / H5，国内 Vue 团队做小程序和 App 的最常见选择，官方提供 llms.txt | Vue 3, 小程序, App | `npx degit dcloudio/uni-preset-vue#vite-ts my-vue3-project`<br>llms.txt: https://uniapp.dcloud.net.cn/llms.txt | 开源 |
| [Ant Design Mini](https://mini.ant.design) | Ant Design 的小程序组件库，支持支付宝和微信小程序，支付宝小程序开发首选 | 支付宝小程序, 微信小程序 | `npm install antd-mini` | 开源 |
| [Ant Design Mobile RN](https://rn.mobile.ant.design) | Ant Design 的 React Native 组件库，RN 项目想沿用 antd 设计语言时选，官方提供 llms.txt | React Native | `npm install @ant-design/react-native @ant-design/icons-react-native`<br>llms.txt: https://rn.mobile.ant.design/llms.txt | 开源 |
| [ArkUI（HarmonyOS）](https://developer.huawei.com/consumer/cn/arkui/) | 鸿蒙原生声明式 UI 框架（ArkTS），开发 HarmonyOS NEXT 原生应用必用；华为开发者文档提供 llms.txt | ArkTS, HarmonyOS | llms.txt: https://developer.huawei.com/llms.txt | 免费 |
| [HarmonyOS Samples](https://gitee.com/harmonyos_samples) | 华为官方的鸿蒙应用示例代码合集（托管在 Gitee），学 ArkUI 写法或找某个 API 的可运行示例时用 | ArkTS, HarmonyOS |  | 开源 |
| [Lynx](https://lynxjs.org) | 字节跳动开源的跨端原生渲染框架（TikTok 在用），用 React + CSS 写原生 UI，想要 RN 之外的高性能跨端方案时评估；⚠ 生态仍在早期 | React, Rspeedy | `npm create rspeedy@latest`<br>llms.txt: https://lynxjs.org/llms.txt | 开源 |
| [Mpx](https://mpxjs.cn) | 滴滴开源的增强型小程序框架，以微信小程序语法为基础跨端输出，对小程序性能和包体积要求高的大型项目选 | 小程序, Vue-like | `npm i -g @mpxjs/cli`<br>mpx create mpx-project<br>llms.txt: https://mpxjs.cn/llms.txt | 开源 |
| [OpenHarmony 三方库中心仓（ohpm）](https://ohpm.openharmony.cn) | 鸿蒙生态的包管理中心（相当于 npm），找 ArkUI 组件库和工具库时先到这里搜 | ArkTS, HarmonyOS |  | 免费 |
| [Taro UI](https://taro-ui.jd.com) | Taro 官方配套的 React 多端组件库，Taro + React 项目的基础 UI；自带 Agent Skill | React, Taro | `npm install taro-ui@latest` | 开源 |
| [TDesign Flutter](https://tdesign.tencent.com/flutter/overview) | TDesign 的 Flutter 组件库，国内团队用 Flutter 做 App 又想要中文产品习惯的组件（如中文日期 / 地区选择）时选 | Flutter, Dart |  | 开源 |
| [TDesign UniApp](https://tdesign.tencent.com/uniapp/overview) | TDesign 官方 uni-app 组件库（刚到 1.0），uni-app 项目想用腾讯设计规范时选；⚠ 较新，生态案例少 | uni-app, Vue 3 | `npm i @tdesign/uniapp` | 开源 |
| [TDesign 小程序](https://tdesign.tencent.com/miniprogram/overview) | 腾讯 TDesign 的微信原生小程序组件库，更新活跃，原生小程序新项目推荐 | 微信小程序 | `npm i tdesign-miniprogram -S --production`<br>MCP: npx -y tdesign-mcp-server@latest | 开源 |
| [uni-app x](https://doc.dcloud.net.cn/uni-app-x/) | uni-app 的下一代引擎，用 UTS 语言编译为各平台原生代码（Kotlin / Swift / ArkTS），对 App 性能要求高时选；⚠ 生态和插件比 uni-app 少 | UTS, Vue 3 | llms.txt: https://doc.dcloud.net.cn/uni-app-x/llms.txt | 开源 |
| [uni-ui](https://uniapp.dcloud.net.cn/component/uniui/uni-ui.html) | DCloud 官方的 uni-app 扩展组件库，兼容性最稳、全端可用，求稳不求花哨时选 | uni-app, Vue | `npm i @dcloudio/uni-ui` | 开源 |
| [unibest](https://unibest.tech) | uni-app + Vue 3 + TS + Vite + UnoCSS + Wot UI 的开箱即用起手模板，脱离 HBuilderX 用 VS Code 开发 uni-app 时首选，官方提供 llms.txt | uni-app, Vue 3, UnoCSS | `pnpm create unibest`<br>llms.txt: https://unibest.tech/llms.txt | 开源 |
| [uview-plus](https://uview-plus.jiangruyi.com) | uView 的 Vue 3 延续版，兼容 nvue / 鸿蒙 / uni-app x，从 uView 2 迁移到 Vue 3 或需要大而全的 uni-app 组件时选 | uni-app, Vue 3 | `npm install uview-plus` | 开源 |
| [Vant Weapp](https://vant-ui.github.io/vant-weapp/) | Vant 的微信原生小程序版（18k★），原生小程序开发最常用的组件库；⚠ npm 最新版停在 2024-12 的 1.11.7，更新慢 | 微信小程序 | `npm i @vant/weapp -S --production` | 开源 |
| [WeUI 小程序版（weui-wxss）](https://github.com/Tencent/weui-wxss) | 微信官方 WeUI 的小程序样式库，配合 weui-miniprogram 扩展组件使用，要与微信原生界面完全一致时选 | 微信小程序, WXSS |  | 开源 |
| [Wot UI（原 Wot Design Uni）](https://wot-ui.cn) | 轻量美观、TypeScript 友好的 uni-app Vue 3 组件库，v2 改名 @wot-ui/ui 并提供官方 CLI / MCP / Skills 和 llms.txt，新 uni-app 项目推荐；v1（wot-design-uni）文档在 v1.wot-ui.cn | uni-app, Vue 3, TS | `npm i @wot-ui/ui`<br>`npm install -g @wot-ui/cli`<br>llms.txt: https://wot-ui.cn/llms.txt（MCP：安装 CLI 后运行 wot mcp） | 开源 |
| [图鸟 UI（TuniaoUI）](https://vue3.tuniaokj.com) | 酷炫风格的 uni-app Vue 3 组件库，自带大量页面模板，想做视觉偏潮的小程序时参考；⚠ 仓库 2024 年后更新很少 | uni-app, Vue 3 |  | 开源 |
| [微信小程序官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/) | 微信小程序框架、组件和 API 的官方文档，写原生小程序或排查 Taro / uni-app 编译产物时的权威依据 | 微信小程序 |  | 免费 |
| [微信小程序设计指南](https://developers.weixin.qq.com/miniprogram/design/) | 微信官方的小程序界面与交互设计规范，小程序上架审核前对照导航、反馈、适配等要求时用 | 微信小程序 |  | 免费 |

### 中后台模板与框架

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [Ant Design Pro](https://pro.ant.design) | Ant Design 官方的中后台前端脚手架（umi + antd + ProComponents，38k★），React 中后台从零起步的标准答案，仓库自带 Agent Skills | React, umi, Ant Design | `git clone --depth=1 https://github.com/ant-design/ant-design-pro.git myapp`<br>`npx skills add ant-design/ant-design-pro` | 开源 |
| [Art Design Pro](https://www.artd.pro) | 注重视觉设计和体验的 Vue 3 + Element Plus 后台模板，嫌普通 admin 模板丑、想要更精致的界面时选 | Vue 3, Element Plus, Vite |  | 开源 |
| [Fantastic-admin](https://fantastic-admin.hurui.me) | 面向 AI 编程的 Vue 3 管理系统框架，兼容 PC 和移动端，提供 llms.txt；⚠ 基础版开源，专业版付费 | Vue 3, Vite | llms.txt: https://fantastic-admin.hurui.me/llms.txt | 免费+付费 |
| [Geeker Admin](https://github.com/HalseySpicy/Geeker-Admin) | Vue 3 + TS + Vite + Pinia + Element Plus 的后台管理框架（8k★），ProTable 封装好用，中小项目想快速出活时选 | Vue 3, Element Plus |  | 开源 |
| [JeecgBoot](https://jeecg.com) | Java 低代码开发平台（48k★），在线表单 / 报表 / 代码生成加 Vue 3 前端，并内置 AI 应用平台，企业信息化快速交付时选；提供 llms.txt，⚠ 部分高级功能为商业版 | Spring Boot, Vue 3, Ant Design Vue | llms.txt: https://jeecg.com/llms.txt | 免费+付费 |
| [Layui](https://layui.dev) | 原生 HTML / CSS / JS 的经典组件库（30k★），不用构建工具、后端模板直接引入即可，给 PHP / Java 服务端渲染的后台页面加 UI 时选；⚠ 非 MVVM，不适合 SPA | 原生 JS, HTML | `npm i layui` | 开源 |
| [Naive UI Admin](https://github.com/jekip/naive-ui-admin) | 基于 Vue 3 + Vite + Naive UI 的开源中后台方案，内置权限、动态菜单和二次封装组件，Naive UI 路线的另一个成熟选择 | Vue 3, Naive UI |  | 开源 |
| [NG-ZORRO](https://ng.ant.design) | Ant Design 的 Angular 实现，紧跟 Angular 大版本，Angular 中后台项目首选，官方提供 llms.txt | Angular, TS | ng add ng-zorro-antd<br>llms.txt: https://ng.ant.design/llms.txt | 开源 |
| [RuoYi 若依](https://doc.ruoyi.vip) | 国内最普及的 Java（Spring Boot）权限管理后台全家桶的官方文档，外包和政企项目的事实模板，接手若依项目时先看这里 | Spring Boot, Vue, Java |  | 开源 |
| [RuoYi-Vue-Plus](https://plus-doc.dromara.org) | Dromara 社区重写的若依增强版（多租户、Sa-Token、MyBatis-Plus、工作流），需要多租户 SaaS 后台时选 | Spring Boot, Vue 3, Java |  | 开源 |
| [RuoYi-Vue3](https://github.com/yangzongzhuan/RuoYi-Vue3) | 若依官方的 Vue 3 + Vite + Element Plus 前端，对接 RuoYi-Vue 后端，需要现成的用户 / 角色 / 菜单管理前端时直接用 | Vue 3, Element Plus, Spring Boot |  | 开源 |
| [Soybean Admin](https://docs.soybeanjs.cn) | Vue 3 + Naive UI + UnoCSS 的清新风中后台模板（15k★），代码规范严格，Naive UI 路线首选，文档提供 llms.txt | Vue 3, Naive UI, UnoCSS | `git clone https://github.com/soybeanjs/soybean-admin.git`<br>llms.txt: https://docs.soybeanjs.cn/llms.txt | 开源 |
| [TDesign Starter](https://tdesign.tencent.com/starter/) | TDesign 官方中后台模板（Vue 3 / React 等版本）和脚手架，腾讯技术栈做后台时的起手项目 | Vue 3, React, TDesign | `npm i tdesign-starter-cli@latest -g` | 开源 |
| [Umi](https://umijs.org) | 蚂蚁的插件化企业级 React 应用框架（约定式路由、内置 antd / 请求 / 权限 / 微前端插件），Ant Design Pro 的底座，官方提供 llms.txt | React, TS | `npx create-umi@latest`<br>llms.txt: https://umijs.org/llms.txt | 开源 |
| [Vue Vben Admin](https://doc.vben.pro) | 最流行的 Vue 3 中后台模板（33k★），monorepo 架构，同时提供 Ant Design Vue / Element Plus / Naive UI 等多个 UI 版本，Vue 中后台首选起手模板 | Vue 3, Vite, TS | `git clone https://github.com/vbenjs/vue-vben-admin.git` | 开源 |
| [vue-pure-admin](https://pure-admin.cn) | Vue 3 + Element Plus + Tailwind 的中后台模板（20k★），提供精简版和官方 CLI，想要 Element Plus 版且代码干净时选 | Vue 3, Element Plus, Tailwind | `npm install -g @pureadmin/cli`<br>pure create | 开源 |
| [vue3-element-admin（有来）](https://github.com/youlaitech/vue3-element-admin) | vue-element-admin 的 Vue 3 + Element Plus 继任模板，配套 Java 后端源码，熟悉老版 vue-element-admin 的团队升级时选；⚠ 原版 PanJiaChen/vue-element-admin 停在 Vue 2 已不维护 | Vue 3, Element Plus, Vite | `npx skills add https://github.com/youlaitech/youlai-skills --skill vue3-element-admin` | 开源 |
| [芋道 yudao-ui-admin-vue3](https://github.com/yudaocode/yudao-ui-admin-vue3) | 芋道源码的 Vue 3 + Element Plus 管理后台，配套后端含工作流、支付、商城、CRM、ERP 等业务模块，需要大量现成业务功能时选 | Vue 3, Element Plus, Spring Boot |  | 开源 |

### 图表与可视化

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Apache ECharts](https://echarts.apache.org) | 百度发起、Apache 孵化毕业的图表库（67k★，当前 v6），图表类型最全、中文文档和示例最多，国内项目做图表默认首选 | JS, Canvas, SVG | `npm install echarts --save` | 开源 |
| [Ant Design Charts](https://ant-design-charts.antgroup.com) | AntV 的 React 图表封装，开箱即用且风格与 antd 统一，antd 中后台里画常规图表时选 | React, AntV | `npm install @ant-design/charts` | 开源 |
| [AntV](https://antv.antgroup.com) | 蚂蚁数据可视化总站，按场景分为 G2（统计图）、G6（关系图）、X6（流程图编辑）、S2（透视表）、L7（地图）、F2（移动端），不确定用哪个时先看这里；提供 llms.txt | JS, TS | llms.txt: https://antv.antgroup.com/llms.txt | 开源 |
| [AntV F2](https://f2.antv.antgroup.com) | 专为移动端设计的轻量图表库，支持 H5 和小程序，移动端图表嫌 ECharts 包体大时选 | JS, Canvas, 小程序 | `npm install @antv/f2` | 开源 |
| [AntV G2](https://g2.antv.antgroup.com) | 基于图形语法的统计图表库，用声明式 API 组合出自定义图表，需要比 ECharts 更灵活的数据映射时选 | JS, TS | `npm install @antv/g2`<br>llms.txt: https://g2.antv.antgroup.com/llms.txt | 开源 |
| [AntV G6](https://g6.antv.antgroup.com) | 图可视化引擎（关系图、知识图谱、拓扑图，内置多种布局），画节点-边关系数据时选 | JS, TS | `npm install @antv/g6`<br>llms.txt: https://g6.antv.antgroup.com/llms.txt | 开源 |
| [AntV Infographic](https://infographic.antv.vision) | AI 时代的信息图生成与渲染框架，用声明式语法让大模型直接输出信息图，把文字报告变成可视化卡片时选 | JS, TS, SVG | `npm install @antv/infographic` | 开源 |
| [AntV L7](https://l7.antv.antgroup.com) | WebGL 地理空间数据可视化引擎，可叠加高德 / Mapbox 底图，做地图大屏、热力、轨迹时选 | JS, WebGL | `npm install @antv/l7`<br>llms.txt: https://l7.antv.antgroup.com/llms.txt | 开源 |
| [AntV MCP Server Chart](https://github.com/antvis/mcp-server-chart) | AntV 官方图表 MCP 服务器，让 Agent 直接生成柱状图、流程图、地图等图表图片，对话里要出图时装 | MCP, Node | `npx -y @antv/mcp-server-chart`<br>`npx skills add antvis/chart-visualization-skills` | 开源 |
| [AntV S2](https://s2.antv.antgroup.com) | 多维交叉分析表格（透视表 / 明细表，Canvas 渲染大数据量），做 BI 报表类表格时选 | JS, TS, Canvas | `npm install @antv/s2 --save` | 开源 |
| [AntV X6](https://x6.antv.antgroup.com) | 图编辑引擎（流程图、DAG、ER 图、脑图的拖拽编辑），要让用户自己画图 / 编排流程时选 | JS, TS, SVG | `npm install @antv/x6 --save`<br>llms.txt: https://x6.antv.antgroup.com/llms.txt | 开源 |
| [echarts-for-react](https://github.com/hustcc/echarts-for-react) | ECharts 的 React 封装，React 项目里用 ECharts 最简单的方式 | React, ECharts | `npm install --save echarts-for-react`<br>`npm install --save echarts` | 开源 |
| [GPT-Vis](https://gpt-vis.antv.vision) | AntV 面向大模型的可视化组件，用类 Markdown 语法让 LLM 输出图表并在聊天流里渲染，AI 对话产品里嵌图表时选；提供 llms.txt | React, JS | `npm install @antv/gpt-vis`<br>llms.txt: https://gpt-vis.antv.vision/llms.txt | 开源 |
| [LogicFlow](https://site.logic-flow.cn) | 滴滴开源的流程图编辑框架（11k★），内置 BPMN 等扩展，做审批流 / 工作流设计器时选 | JS, TS | `npm install @logicflow/core @logicflow/extension --save` | 开源 |
| [VChart（VisActor）](https://www.visactor.io/vchart) | 字节跳动 VisActor 的图表库，叙事动画强、跨端（含小程序 / 飞书），并提供官方 MCP 和 llms.txt，想要比 ECharts 更好的动画和 AI 生成支持时选 | JS, TS, Canvas | `npm install @visactor/vchart`<br>MCP: npx -y @visactor/vchart-mcp-server<br>llms.txt: https://www.visactor.io/llms.txt | 开源 |
| [VisActor Skills](https://www.visactor.io/skills) | VisActor 官方 Agent Skills 合集（图表助手、数据叙事、看板等），让编码 Agent 按规范生成 VChart 可视化时装 | Skill, VChart | `npx skills add VisActor/skills --skill chart-assistant` | 开源 |
| [VTable（VisActor）](https://www.visactor.io/vtable) | 字节跳动的 Canvas 高性能表格（百万级数据、透视表、甘特图），DOM 表格卡顿时选 | JS, TS, Canvas | `npm install @visactor/vtable` | 开源 |
| [vue-echarts](https://vue-echarts.dev) | ECharts 的 Vue 组件封装（10k★），Vue 项目里用 ECharts 时省去手动 init / resize / dispose | Vue 3, ECharts | `npm install echarts vue-echarts` | 开源 |

### 低代码与工程

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [amis](https://baidu.github.io/amis/) | 百度开源的低代码前端框架（18k★），用 JSON 配置生成后台页面，适合让后端或 AI 直接产出 CRUD 页面；⚠ 自定义交互越多越难维护 | React, JSON | `npm i amis` | 开源 |
| [dumi](https://d.umijs.org) | 蚂蚁的组件库文档与研发工具（antd 生态文档站都用它），自己发布 React 组件库需要带 demo 的文档站时选 | React, Markdown | `npx create-dumi` | 开源 |
| [MicroApp](https://jd-opensource.github.io/micro-app/) | 京东开源的微前端框架，以类 WebComponent 的标签方式接入子应用、接入成本低，嫌 qiankun 改造多时选；⚠ 1.0 仍为 rc 版 | JS, 微前端 | yarn add @micro-zoe/micro-app | 开源 |
| [qiankun 乾坤](https://qiankun.umijs.org) | 蚂蚁开源的微前端框架（16k★，基于 single-spa），把多个不同技术栈的老系统拼成一个中后台时最常用；仓库自带 Agent Skill | JS, 微前端 | `npm i qiankun`<br>`npx skills add umijs/qiankun` | 开源 |
| [TinyEngine](https://opentiny.design/tiny-engine) | OpenTiny 的低代码引擎，用来搭建自己的可视化搭建平台（画布、物料、出码都可扩展），要自研低代码平台时选 | Vue 3 | `npx @opentiny/tiny-engine-cli@latest create-platform <name>` | 开源 |
| [Univer](https://univer.ai) | Luckysheet 原团队的新一代开源办公套件 SDK（电子表格 / 文档，22k★），要在产品里嵌入类 Excel 在线表格时选，提供 llms.txt；⚠ 协同编辑、导入导出等高级能力为商业版 | TS, React, Canvas | `pnpm add @univerjs/presets @univerjs/preset-sheets-core`<br>llms.txt: https://univer.ai/llms.txt | 免费+付费 |
| [无界 wujie](https://wujie-micro.github.io/doc/) | 腾讯开源的微前端框架，用 iframe + WebComponent 做到强 JS 隔离且支持 Vite 子应用，隔离性要求高时选 | JS, 微前端 | `npm install wujie -S` | 开源 |

### 图标与设计资源

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [Ant Design Icons](https://ant.design/components/icon) | Ant Design 官方图标（线框 / 实底 / 双色三套），antd 项目里用 @ant-design/icons 按需引入 | React, SVG |  | 开源 |
| [iconfont 阿里巴巴矢量图标库](https://www.iconfont.cn) | 国内最大的图标 / 插画素材平台，可建项目图标库并导出 Symbol、字体或 SVG，中文团队协作管理图标的事实标准；⚠ 素材由用户上传，商用前逐个确认版权 | SVG, Icon Font |  | 免费 |
| [Lobe Icons](https://icons.lobehub.com) | 最全的 AI / 大模型品牌 Logo 图标集（OpenAI、Claude、DeepSeek、通义等），做模型选择器或 AI 产品落地页时用，提供 llms.txt | React, SVG, React Native, Vue | `npm i @lobehub/icons @lobehub/ui`<br>llms.txt: https://icons.lobehub.com/llms.txt | 开源 |
| [MasterGo](https://mastergo.com) | 国产在线 UI 设计工具（对标 Figma），官方提供 Magic MCP 让 Agent 直接读取设计稿生成代码，团队设计稿在 MasterGo 时用；⚠ 个人免费版不支持 MCP，需 Token | 设计工具, MCP | `npx @mastergo/magic-mcp --token=YOUR_TOKEN` | 免费+付费 |
| [Pixso](https://pixso.cn) | 万兴旗下的国产 UI 设计协作平台，支持私有化部署，对数据合规有要求的企业替代 Figma 时选 | 设计工具 |  | 免费+付费 |
| [Remix Icon](https://remixicon.com) | 国内团队出品的开源中性风图标集（3200+ 个，线性 / 面性成对），风格统一、可免费商用，找不到合适图标时的稳妥默认 | SVG, React, Vue | `npm install remixicon --save`<br>`npm install @remixicon/react` | 开源 |
| [TDesign Icons](https://tdesign.tencent.com/icons) | TDesign 配套图标库，提供 Vue / React 等框架包和 SVG，TDesign 项目直接用 | SVG, Vue, React |  | 开源 |
| [中国传统颜色手册](https://colors.ichuantong.cn) | 按色系整理的中国传统色速查表，点击即可复制色值，国风配色的第二参考 | 配色 |  | 免费 |
| [中国色](http://zhongguose.com) | 中国传统颜色百科（500+ 种带名称的传统色及 RGB / CMYK / HEX），做国风 / 新中式配色时取色，提供 llms.txt | 配色 | llms.txt: http://zhongguose.com/llms.txt | 免费 |
| [优设网 UISDC](https://www.uisdc.com) | 国内设计师学习平台，有大量 UI 设计教程、大厂设计规范解读和 AIGC 教程，查中文设计方法论时用；⚠ 站点屏蔽爬虫（curl 返回 403），需浏览器访问 | 教程, 灵感 |  | 免费 |
| [即时设计](https://js.design) | 国产在线 UI 设计协作工具，中文社区资源库丰富（大量大厂组件库设计稿可直接复用），国内团队替代 Figma 时选 | 设计工具 |  | 免费+付费 |
| [站酷 ZCOOL](https://www.zcool.com.cn) | 国内最大的设计师作品社区，找中文语境下的品牌、插画、UI、电商视觉参考时看 | 灵感 |  | 免费 |
| [花瓣网](https://huaban.com) | 国内的设计灵感采集站（类 Pinterest），按关键词攒中文审美的情绪板时用 | 灵感 |  | 免费+付费 |

### 中文字体

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [100font](https://www.100font.com) | 免费商用字体大全，按风格分类并附授权说明，猫啃网之外的第二个核对来源 | 字体目录 |  | 免费 |
| [HarmonyOS Sans](https://developer.huawei.com/consumer/cn/design/resource/) | 华为鸿蒙系统字体，在 HarmonyOS 设计资源页免费下载（同页还有图标、设计模板），做鸿蒙应用或想要中性现代的中文界面字时选 | TTF |  | 免费 |
| [Maple Mono](https://font.subf.dev) | 带圆角和连字的开源等宽字体（29k★），CN 版内置完整中文字符集，代码块、终端风页面需要中英文混排等宽字时选 | TTF, WOFF2, Nerd Font | `brew install --cask font-maple-mono-nf-cn` | 开源 |
| [MiSans](https://hyperos.mi.com/font/) | 小米发布的免费中文字体家族（可变字重，覆盖多语种），界面字体想要更现代的字面时选；⚠ 使用须遵守小米字体许可协议 | TTF, Variable |  | 免费 |
| [OPPO Sans](https://www.coloros.com/article/A00000050/) | OPPO 官方声明免费授权全社会使用（含商用）的中文字体（3.0 版），字形简洁，可作为思源黑体之外的界面字体备选 | TTF |  | 免费 |
| [ZeoSeven Fonts（ZSFT）](https://fonts.zeoseven.com) | 免费商用字体的预览、下载和 CSS API（类似中文版 Google Fonts），想用一行 CSS 引入中文字体时用 | CSS API, WOFF2 |  | 免费 |
| [中文网字计划](https://chinese-font.netlify.app) | 中文 Web 字体分包方案与在线字体库：用 cn-font-split 把几 MB 的中文字体切成按需加载的小分片，网页要用自定义中文字体时必看 | WOFF2, CDN, Node | `pnpm i cn-font-split` | 开源 |
| [得意黑 Smiley Sans](https://atelier-anchor.com/typefaces/smiley-sans) | 开源的窄斜体中文黑体（OFL，15k★ 可免费商用），标题、海报、活动页想要有态度的中文字时选；⚠ 只适合标题，不适合正文 | OTF, TTF, WOFF2 | `brew install font-smiley-sans` | 开源 |
| [思源宋体 Source Han Serif](https://github.com/adobe-fonts/source-han-serif) | 思源系列的开源宋体（Google 侧名为 Noto Serif CJK，OFL），长文阅读、编辑风或出版物风格的中文排版选 | OTF, Variable |  | 开源 |
| [思源黑体 Source Han Sans](https://github.com/adobe-fonts/source-han-sans) | Adobe 与 Google 联合开发的开源泛 CJK 黑体（Google 侧名为 Noto Sans CJK，OFL），中文 UI 正文最安全的默认选择 | OTF, Variable |  | 开源 |
| [猫啃网](https://www.maoken.com) | 持续更新的免费商用中文字体索引站，逐个标注授权来源，选字体前查「能不能商用」时用 | 字体目录 |  | 免费 |
| [阿里巴巴普惠体](https://www.alibabafonts.com) | 阿里巴巴发布的免费商用中文黑体家族（多字重），电商和企业站想要思源黑体之外的正文字体时选 | TTF, WOFF2 |  | 免费 |
| [霞鹜文楷 LXGW WenKai](https://github.com/lxgw/LxgwWenKai) | 最受欢迎的开源中文楷体（OFL，26k★），兼顾屏幕阅读，博客、阅读类产品和文艺风页面的正文首选 | TTF |  | 开源 |
