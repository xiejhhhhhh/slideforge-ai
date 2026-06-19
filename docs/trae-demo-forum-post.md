# 【学习工作赛道】SlideForge AI Demo Studio：AI PPT 生产线，从需求到 PPTX 的完整闭环

## 一、Demo 简介

**是什么**：SlideForge AI Demo Studio 是一款 AI PPT 生产线 Web Demo。用户输入一段 PPT 需求后，可以依次完成「需求分析 -> Markdown 大纲 -> HTML 幻灯片 -> 演讲稿备注 -> PPTX 导出」的完整流程。

**面向谁**：完全不会代码的办公白领、科研工作者、研究生、教师、产品经理、比赛答辩选手，以及任何需要频繁做汇报的人。

**核心价值**：不让 AI 一步生成不可控的最终 PPT，而是把生成过程拆成多个可检查、可修改、可复用的阶段。每个阶段都能与 AI 对话调整，最后再导出可演示的 PPTX。

## 二、核心功能

1. **AI 深度需求分析 + Markdown 大纲**
   - 拆解主题、受众、汇报时长、页面结构、风格要求和交付格式。
   - 生成包含时间分配、主标题、内容要点、讲述重点、视觉建议和版式要求的大纲。
   - 大纲可下载为 Markdown。

2. **AI 生成专业 HTML 幻灯片**
   - 基于当前 Markdown 大纲生成 16:9 HTML PPT。
   - 保持大纲页数与 HTML 页数一致。
   - 参考学术报告和产品 Deck 的设计组件，减少空白、遮挡和错位。
   - 支持继续用 AI 修改 HTML 幻灯片。

3. **AI 生成演讲稿备注**
   - HTML 确认后逐页生成 150 到 300 字口播稿。
   - 备注可编辑、可再次对话调整。
   - 导出 PPTX 时写入备注栏。

4. **三种 PPTX 导出模式**
   - 截图嵌入：高保真，适合快速交付。
   - 原生绘制：文本和图片尽量可编辑。
   - 模板填充：上传 `.pptx` 模板后尽量套用模板比例、字体和配色。

## 三、Demo 截图

| 首页 | 需求输入 | 大纲生成 |
| --- | --- | --- |
| ![首页](assets/trae-demo/screen-02-demo-home.png) | ![需求输入](assets/trae-demo/screen-04-requirement-input.png) | ![大纲生成](assets/trae-demo/screen-05-outline-generation.png) |

| HTML 预览 | 演讲稿备注 | PPTX 导出 |
| --- | --- | --- |
| ![HTML 预览](assets/trae-demo/screen-06-html-preview.png) | ![演讲稿备注](assets/trae-demo/screen-08-speaker-notes.png) | ![PPTX 导出](assets/trae-demo/screen-09-export-pptx.png) |

## 四、创作思路

我在制作科研汇报 PPT 时发现，AI 写内容很快，但最终交付仍然需要大量人工修正：结构不稳、HTML 和大纲脱节、图片位置不对、文字遮挡、演讲备注缺失、PPTX 导出不可控。

SlideForge AI 的核心想法是把 PPT 生成变成一个可复现的工程流程：

```text
需求输入
  -> Markdown 大纲
  -> HTML 幻灯片预览
  -> 演讲稿备注
  -> PPTX 导出
```

HTML 是中间审稿层。它既方便 AI 生成，也方便人类检查排版、图片、行距、留白和叙事逻辑。确认 HTML 后，再用截图或模板填充方式生成 PPTX。

## 五、TRAE 实践过程

本 Demo 由 TRAE Work / TRAE IDE 辅助完成，主要经历了四个阶段：

### 阶段一：需求理解与方案设计

让 TRAE 读取 `trae_demo_generation_plan.md`，先输出产品方案、页面结构、交互流程和风险对策，再进入编码。

### 阶段二：前后端代码生成

让 TRAE 生成：

- `trae-demo/index.html`：前端 UI 和 AI 工作流。
- `trae-demo/app.py`：Flask 后端，用于模板解析、截图和 PPTX 导出。
- `trae-demo/start.bat`：Windows 一键启动脚本。

### 阶段三：真实流程测试与修复

用实际 PPT 需求测试生成大纲、HTML 和 PPTX 的闭环，重点修复：

- 大纲质量不够专业。
- HTML 没有严格遵循大纲。
- 图片没有进入对应页面布局。
- 预览页缩放不完整。
- PPTX 导出缺少备注或图片。

### 阶段四：参赛材料整理

补充 README、Session 证据清单、发帖草稿和展示截图，方便社区评审快速理解 Demo。

## 六、技术亮点

| 亮点 | 说明 |
| --- | --- |
| 深度大纲生成 | 先做需求分析，再生成含时间、视觉建议和讲述重点的大纲 |
| 大纲-HTML 对齐 | HTML 生成和修改都基于当前 Markdown 大纲 |
| 多步可对话 | 大纲、HTML、演讲稿都支持继续让 AI 修改 |
| 图片进入版面 | 图片作为幻灯片内容的一部分，而不是单独图库 |
| 演讲备注闭环 | 备注可编辑，并进入导出的 PPTX |
| 三种导出模式 | 覆盖快速交付、可编辑修改和模板套用三类场景 |
| 本地安全运行 | API Key 只保存在浏览器 localStorage，不写入仓库 |

## 七、体验方式

```bash
git clone https://github.com/xiejhhhhhh/slideforge-ai.git
cd slideforge-ai/trae-demo
pip install -r requirements.txt
playwright install chromium
python app.py
```

浏览器访问：

```text
http://127.0.0.1:5000
```

Windows 用户可以直接双击：

```text
trae-demo/start.bat
```

## 八、Session ID

> 发帖时请在这里填写不少于 3 个 TRAE Session ID。

- 需求分析与方案设计 Session ID：
- 前后端核心生成 Session ID：
- 测试修复与视觉优化 Session ID：
- 参赛材料整理 Session ID：

## 九、报名帖链接

> 发帖时请在这里填写已通过的报名帖链接。

## 十、作者与开源

作者 GitHub：[https://github.com/xiejhhhhhh](https://github.com/xiejhhhhhh)

项目地址：[https://github.com/xiejhhhhhh/slideforge-ai](https://github.com/xiejhhhhhh/slideforge-ai)

---

**本 Demo 由 TRAE Work / TRAE IDE 辅助生成 | TRAE AI 创造力大赛 · 学习工作赛道**
