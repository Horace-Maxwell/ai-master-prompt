# 大厂设计系统

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-design-systems"></a>

## 大厂设计系统与官方实现

要对齐某个平台的规范（Material、Apple、Fluent…）或想借鉴成熟设计系统时用。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) | 苹果全平台（iOS / iPadOS / macOS / watchOS / visionOS）官方界面设计规范，做苹果生态应用或想让 Web 界面有 iOS 质感时必读 | 设计规范, iOS, macOS |  | 免费 |
| ⭐ [Carbon Design System](https://carbondesignsystem.com) | IBM 的开源设计系统，规范文档极完整、数据密集型企业界面范例多，React / Web Components 双实现，并提供 llms.txt 和官方 Carbon MCP | React, Web Components, Sass | `npm install @carbon/react`<br>llms.txt: https://carbondesignsystem.com/llms.txt（Carbon MCP 设置见 https://www.carbondesignsystem.com/getting-started/carbon-mcp/overview） | 开源 |
| ⭐ [Material Design 3](https://m3.material.io) | Google 的开源设计系统规范（动态配色、形状、动效、组件指南），做 Android 应用或需要一套完整可引用的设计 token 体系时的权威参考 | 设计规范, Android, Web |  | 免费 |
| ⭐ [React Aria](https://react-aria.adobe.com) | Adobe 的无样式 React 组件与 hooks，键盘、读屏、触屏交互和国际化处理业界标杆，自建设计系统需要最强无障碍底座时首选；提供 llms.txt、MCP 和 Agent Skills | React, TS, Headless | `claude mcp add react-aria npx @react-aria/mcp@latest`<br>`npx skills add https://react-aria.adobe.com`<br>llms.txt: https://react-aria.adobe.com/llms.txt | 开源 |
| [Adobe Spectrum](https://spectrum.adobe.com) | Adobe 的设计系统规范（已更新到 Spectrum 2），创意工具类、面板密集型界面的设计参考 | 设计规范 |  | 免费 |
| [Agriculture Design System（AgDS）](https://design-system.agriculture.gov.au) | 澳大利亚农业部的 React 设计系统（@ag.ds-next/react），做政务类 React 项目时参考 | React, TS |  | 开源 |
| [Astro UXDS](https://www.astrouxds.com) | Rocket Communications 面向航天任务控制类应用的设计系统（Web Components），做监控大屏、状态指示、时间轴类暗色控制台时的独特参考 | Web Components, React | `npm i @astrouxds/react` | 开源 |
| [Atlassian Design System](https://atlassian.design) | Atlassian（Jira / Confluence）的设计系统与 @atlaskit 组件，做 Atlassian 插件或协作类 SaaS 时参考，提供 llms.txt 和官方 MCP（本地 npx 或远程地址） | React, TS | llms.txt: https://atlassian.design/llms.txt<br>MCP: npx -y @atlaskit/ads-mcp（远程 https://mcp.atlassian.com/v1/ads/public/mcp） | 开源 |
| [Base Web（Uber）](https://baseweb.design) | Uber 的 React 组件库（基于 Styletron），Overrides 机制可深度改造每个组件内部；⚠ 官方声明仓库处于有限维护状态，新项目慎选 | React, Styletron | `npm install baseui@next styletron-react styletron-engine-monolithic` | 开源 |
| [Blueprint（Palantir）](https://blueprintjs.com) | Palantir 的 React 组件库（22k★），专为桌面端复杂数据密集型界面优化（表格、树、日期范围、热键），做类 IDE / 分析工具时选；⚠ 不适合移动端 | React, TS, Sass | `npm install --save @blueprintjs/core` | 开源 |
| [Braid（SEEK）](https://seek-oss.github.io/braid-design-system/) | SEEK 的 React 设计系统，以 Box / Stack / Inline 等布局原语和类型安全的间距 token 闻名，想学「用布局组件代替手写 CSS」的做法时参考 | React, vanilla-extract | `npm install --save braid-design-system` | 开源 |
| [Clarity Design System](https://clarity.design) | VMware 发起的 Angular 设计系统（数据表格、向导、树等企业组件），Angular 企业后台的成熟选择，提供 llms.txt | Angular, Web Components | `npm install @clr/ui @clr/angular`<br>llms.txt: https://clarity.design/llms.txt | 开源 |
| [Cloudscape（AWS）](https://cloudscape.design) | AWS 控制台同款的开源设计系统，表格、向导、分栏布局等云控制台模式最完整，做云产品 / 运维后台时选，提供 llms.txt | React, TS | `npm install @cloudscape-design/components @cloudscape-design/global-styles`<br>llms.txt: https://cloudscape.design/llms.txt | 开源 |
| [DSFR（法国政府设计系统）](https://github.com/GouvernementFR/dsfr) | 法国政府官方设计系统，组件与无障碍规范完整；⚠ 许可仅限法国政府网站使用，其他项目只可作参考，且官网屏蔽爬虫 | HTML, CSS, JS | `npm create @gouvfr/dsfr@latest` | 开源 |
| [Elastic UI（EUI）](https://eui.elastic.co) | Elastic（Kibana）的 React 设计系统，数据表格、查询栏、图表配色等分析型界面组件齐全，做日志 / 监控 / 数据分析产品时选；⚠ 使用 Elastic License 2.0 与 SSPL 双许可，非 MIT | React, Emotion | yarn add @elastic/eui | 开源 |
| [Evergreen（Segment）](https://evergreen.segment.com) | Segment 的 React UI 框架，API 简单、风格中性，做内部工具和 SaaS 控制台够用；⚠ 更新频率较低 | React | `npm install --save evergreen-ui` | 开源 |
| [Fluent 2 Design System](https://fluent2.microsoft.design) | 微软的设计系统规范（Microsoft 365 / Windows 11 的视觉语言），做 Teams / Office 插件或 Windows 风格产品时的设计依据 | 设计规范, Web, Windows |  | 免费 |
| [Fluent UI React v9](https://react.fluentui.dev) | Fluent 2 的官方 React 组件库（@fluentui/react-components），做微软生态应用或想要 Office 风企业界面时选，提供 llms.txt | React, TS, Griffel | yarn add @fluentui/react-components<br>llms.txt: https://react.fluentui.dev/llms.txt | 开源 |
| [Fluent UI Web Components](https://web-components.fluentui.dev) | Fluent 2 的 Web Components 实现，非 React 技术栈或需要框架无关嵌入时选 | Web Components | `npm i @fluentui/web-components` | 开源 |
| [Garden（Zendesk）](https://garden.zendesk.com) | Zendesk 的设计系统和 React 组件（styled-components），做工单 / 客服类产品界面时参考 | React, styled-components | `npm install @zendeskgarden/react-components@next styled-components` | 开源 |
| [Geist（Vercel）](https://vercel.com/geist/introduction) | Vercel 的设计系统文档（配色、图标、组件规范）和 Geist 字体，想做 Vercel 那种黑白极简开发者产品风时参考；⚠ 组件未作为公开 npm 包发布，可安装的只有 Geist 字体 | 设计规范, 字体 | `npm i geist` | 免费 |
| [GOV.UK Design System](https://design-system.service.gov.uk) | 英国政府数字服务的设计系统，表单、报错、分步流程的可用性经过大量用户研究验证，做政务 / 办事类表单时的最佳范本 | HTML, Nunjucks, Sass | `npm install govuk-frontend --save` | 开源 |
| [Gravity UI（Yandex）](https://gravity-ui.com) | Yandex 开源的 React 设计系统，除基础组件外还有表格、图表、Markdown 编辑器等配套包，提供 llms.txt | React, TS | `npm install @gravity-ui/uikit`<br>llms.txt: https://gravity-ui.com/llms.txt | 开源 |
| [Grommet](https://v2.grommet.io) | HPE 支持的 React 组件框架，内置响应式布局与主题、无障碍好，想要与 Material / antd 不同的轻量企业风时选 | React, styled-components | `npm install grommet styled-components --save` | 开源 |
| [Helios（HashiCorp）](https://helios.hashicorp.design) | HashiCorp 的设计系统，文档细致，组件为 Ember 实现（非 Ember 项目主要参考规范），官方提供 MCP 包 @hashicorp/design-system-mcp | Ember, CSS | `pnpm add @hashicorp/design-system-components`<br>`pnpm add --save-dev @hashicorp/design-system-mcp` | 开源 |
| [HPE Design System](https://design-system.hpe.design) | 慧与（HPE）基于 Grommet 的企业设计系统，模板和页面级范例多，用 Grommet 时可直接参考它的用法 | React, Grommet |  | 开源 |
| [Jetpack Compose Material 3](https://developer.android.com/develop/ui/compose/designsystems/material3) | Android 官方的 Compose Material 3 组件与主题文档，写原生 Android 界面时 Material 3 的落地实现 | Kotlin, Jetpack Compose |  | 免费 |
| [Kumo（Cloudflare）](https://kumo-ui.com) | Cloudflare 开源的 React 组件库（基于 Base UI），自带面向 Agent 的 CLI 文档查询和 llms.txt，想做 Cloudflare 控制台风格的现代 Web 应用时选 | React, TS, Base UI | `pnpm add @cloudflare/kumo`<br>`npx @cloudflare/kumo docs`<br>llms.txt: https://kumo-ui.com/llms.txt | 开源 |
| [LeafyGreen UI（MongoDB）](https://www.mongodb.design) | MongoDB 的设计系统与 React 组件（按组件分包安装），做数据库 / 开发者平台控制台时参考 | React, TS | `pnpm add @leafygreen-ui/button` | 开源 |
| [Lightning Design System 2（SLDS）](https://www.lightningdesignsystem.com) | Salesforce 的设计系统（SLDS 2），做 Salesforce 平台应用或 CRM 类数据密集界面时参考；⚠ 旧的开源 CSS 仓库已归档，规范以官网为准 | 设计规范, CSS, LWC |  | 免费 |
| [Material Web](https://material-web.dev) | Google 官方的 Material 3 Web Components 实现，框架无关；⚠ 已进入维护模式（等待新维护者），新项目用 React 建议改选 MUI | Web Components, Lit | `npm install @material/web` | 开源 |
| [Momentum Design（Cisco）](https://momentum.design) | 思科 Webex 的设计系统，组件为 Web Components，做会议 / 协作类产品时参考 | Web Components |  | 开源 |
| [Mozilla Protocol](https://protocol.mozilla.org) | Mozilla 官网系站点使用的设计系统（HTML / CSS 组件），做内容型品牌官网时参考 | HTML, CSS, Sass | `npm install @mozilla-protocol/core --save` | 开源 |
| [NHS.UK Design System](https://service-manual.nhs.uk/design-system) | 英国国民医疗服务体系的设计系统，面向医疗健康场景的内容与组件规范，做医疗 / 健康类服务页面时参考 | HTML, Nunjucks, Sass | `npm install nhsuk-frontend --save` | 开源 |
| [Nord Design System](https://nordhealth.design) | Nordhealth 的医疗 / 兽医软件设计系统，基于 Web Components 框架无关，做医疗 SaaS 时参考，提供 llms.txt | Web Components, Lit | llms.txt: https://nordhealth.design/llms.txt | 开源 |
| [Pajamas（GitLab）](https://design.gitlab.com) | GitLab 的设计系统，文档公开透明，配套 Vue 组件库 @gitlab/ui，做 DevOps 类产品或 Vue 设计系统时参考 | Vue, Sass | yarn add @gitlab/ui | 开源 |
| [Paste（Twilio）](https://github.com/twilio-labs/paste) | Twilio 的 React 设计系统，以无障碍和可组合 primitives 著称，做客服 / 通信类控制台时参考；⚠ 原文档域名 paste.twilio.design 现已跳转到 GitHub 仓库 | React, TS |  | 开源 |
| [PatternFly（Red Hat）](https://www.patternfly.org) | 红帽的开源设计系统，面向企业 IT / 云平台控制台（OpenShift 同款），官方提供 MCP | React, CSS | `npm install @patternfly/react-core --save`<br>MCP: npx -y @patternfly/patternfly-mcp@latest | 开源 |
| [Porsche Design System](https://designsystem.porsche.com) | 保时捷的设计系统，Web Components 加 React / Angular / Vue 封装，想参考高端品牌官网的克制排版与组件实现时看 | Web Components, React, Angular, Vue | `npm install @porsche-design-system/components-react` | 开源 |
| [Primer（GitHub）](https://primer.style) | GitHub 的设计系统（React 组件、CSS、Octicons 图标），想做开发者工具 / GitHub 风格的克制界面时选，官方提供 MCP | React, CSS | `npm install @primer/react`<br>MCP: npx @primer/mcp@latest | 开源 |
| [Radix Themes](https://www.radix-ui.com/themes/docs/overview/getting-started) | Radix 团队在 Primitives 之上做的带样式成品组件库，用 Theme 组件配置强调色 / 圆角 / 缩放即可成套换肤，想要开箱即用而不是自己写样式时选 | React, TS | `npm install @radix-ui/themes` | 开源 |
| [React Spectrum（S2）](https://react-spectrum.adobe.com) | Adobe Spectrum 2 的官方 React 实现，无障碍和国际化做得最彻底的成品组件库之一，接受 Adobe 视觉时选；提供 llms.txt、MCP 和 Agent Skills | React, TS | `claude mcp add react-spectrum-s2 npx @react-spectrum/mcp@latest`<br>`npx skills add https://react-spectrum.adobe.com`<br>llms.txt: https://react-spectrum.adobe.com/llms.txt | 开源 |
| [Ring UI（JetBrains）](https://jetbrains.github.io/ring-ui/master/index.html) | JetBrains Web 产品（YouTrack、TeamCity 等）使用的 React 组件库，想做 IDE 周边 / 开发者工具风界面时参考 | React, TS | `npm install @jetbrains/ring-ui-built` | 开源 |
| [Salesforce Design System React](https://github.com/salesforce/design-system-react) | SLDS 的官方 React 组件库，在 Salesforce 之外用 React 实现 Lightning 风格时选；⚠ 面向 React 19 / SLDS 2 的 v11 重写仍是 alpha，稳定版为 0.10.x | React, SLDS | `npm install @salesforce/design-system-react@alpha` | 开源 |
| [Salt（J.P. Morgan）](https://www.saltdesignsystem.com) | 摩根大通的开源设计系统，面向金融类高密度界面，支持多种密度与主题，做交易 / 金融后台时参考 | React, TS | `npm install @salt-ds/core @salt-ds/theme @salt-ds/lab @salt-ds/icons` | 开源 |
| [Scale（Deutsche Telekom）](https://telekom.github.io/scale/) | 德国电信的开源设计系统，Web Components 实现并提供去品牌的 neutral 主题包，想要可白标的 Web Components 套件时选；⚠ 3.0 长期处于 beta | Web Components, Stencil | `npm install @telekom/scale-components@next` | 开源 |
| [Shopify Polaris](https://shopify.dev/docs/api/polaris) | Shopify 的设计系统，现以 Web Components 形式提供，做 Shopify 应用 / 后台扩展时必须用；⚠ 旧的 polaris-react 仓库已归档，polaris.shopify.com 已跳转到这里 | Web Components, Shopify | `claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest` | 免费 |
| [Siemens Industrial Experience（iX）](https://ix.siemens.io) | 西门子的工业软件设计系统，Web Components 加 React / Angular / Vue 封装，做工控、IoT、设备监控类界面时选，提供 llms.txt 和官方 MCP | Web Components, React, Angular, Vue | llms.txt: https://ix.siemens.io/llms.txt<br>MCP: npx @siemens/ix-mcp init | 开源 |
| [Spectrum Web Components](https://opensource.adobe.com/spectrum-web-components/) | Adobe Spectrum 的 Web Components（Lit）实现，非 React 项目或要做 Adobe 插件界面时选 | Web Components, Lit | yarn add @spectrum-web-components/bundle | 开源 |
| [Stacks（Stack Overflow）](https://stackoverflow.design) | Stack Overflow 的设计系统，以原子化 CSS 类和组件为主，提供 llms.txt，做社区 / 问答类产品时参考 | CSS, Svelte | llms.txt: https://stackoverflow.design/llms.txt | 开源 |
| [U.S. Web Design System（USWDS）](https://designsystem.digital.gov) | 美国联邦政府的设计系统，无障碍合规（Section 508）与设计 token 完整，做公共服务类网站时参考，提供 llms.txt | HTML, Sass, JS | `npm install --save @uswds/uswds@latest`<br>llms.txt: https://designsystem.digital.gov/llms.txt | 开源 |
| [UI5 Web Components（SAP Fiori）](https://ui5.github.io/webcomponents/) | SAP Fiori 设计语言的框架无关 Web Components（另有 React 封装），做 SAP 生态或 ERP 类企业应用时选，官方提供 MCP | Web Components, React | `npm install @ui5/webcomponents`<br>MCP: npx -y @ui5/webcomponents-mcp-server | 开源 |
| [Wise Design](https://wise.design) | Wise（原 TransferWise）的设计系统，金融消费产品的文案语气、配色与组件规范写得很好，做支付 / 钱包类产品时参考 | 设计规范, React |  | 免费 |
| [Wix Design System](https://www.wixdesignsystem.com) | Wix 的 React 设计系统，面向商家后台和仪表盘，组件多，提供 llms.txt 和官方 MCP | React, TS | `npm install @wix/design-system`<br>MCP: npx -y @wix/design-system-mcp<br>llms.txt: https://www.wixdesignsystem.com/llms.txt | 开源 |
| [Workday Canvas](https://design.workday.com) | Workday 的设计系统，配套 React 组件库 Canvas Kit，做 HR / 财务类企业应用时参考 | React, TS | `npm install @workday/canvas-kit-react @workday/canvas-tokens-web` | 开源 |
