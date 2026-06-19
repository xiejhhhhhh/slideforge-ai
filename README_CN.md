<div align="center">

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](./requirements.txt)
[![Flask](https://img.shields.io/badge/Flask-Demo%20Backend-000000?style=flat-square&logo=flask&logoColor=white)](./trae-demo/app.py)
[![Playwright](https://img.shields.io/badge/Playwright-HTML%20Rendering-2EAD33?style=flat-square&logo=playwright&logoColor=white)](#快速开始)
[![PPTX Export](https://img.shields.io/badge/PPTX-Export-D24726?style=flat-square&logo=microsoftpowerpoint&logoColor=white)](./scripts/export_html_to_pptx.py)
[![Markdown](https://img.shields.io/badge/Markdown-Outline-000000?style=flat-square&logo=markdown&logoColor=white)](./prompts/01_outline_prompt.md)
[![HTML Preview](https://img.shields.io/badge/HTML-Preview-E34F26?style=flat-square&logo=html5&logoColor=white)](./templates/academic-16x9/template.html)
[![AI Workflow](https://img.shields.io/badge/AI-PPT%20Workflow-5C4D7D?style=flat-square)](#slideforge-ai)
[![License MIT](https://img.shields.io/badge/License-MIT-4C956C?style=flat-square)](./LICENSE)

# SlideForge AI（幻灯锻造厂）

**AI PPT 生产线：需求 -> Markdown 大纲 -> HTML 幻灯片 -> 演讲备注 -> PPTX。**

[English](./README.md) | [中文](./README_CN.md)

</div>

## SlideForge AI Demo Studio

SlideForge AI Demo Studio 是一个面向本地运行的可交互 Demo，用来把一段 PPT 需求变成可检查、可修改、可导出的幻灯片。

它面向办公白领、科研人员、学生、教师和产品团队，目标是把一段 PPT 需求稳定地变成可检查、可修改、可交付的幻灯片，而不是依赖一次性生成。

```text
PPT 需求 + 可选参考图片 + 可选 PPT 模板
  -> AI 深度需求分析
  -> Markdown PPT 大纲
  -> 16:9 HTML 幻灯片预览
  -> 演讲稿备注
  -> PPTX 导出
```

每个阶段都可以继续和 AI 对话调整：大纲可以改，HTML 可以改，演讲稿也可以改，最后再导出 PPTX。

## Demo 截图

| 首页 | 需求输入 | 大纲生成 |
| --- | --- | --- |
| ![Demo 首页](./docs/assets/trae-demo/screen-02-demo-home.png) | ![需求输入](./docs/assets/trae-demo/screen-04-requirement-input.png) | ![大纲生成](./docs/assets/trae-demo/screen-05-outline-generation.png) |

| HTML 预览 | 演讲稿备注 | PPTX 导出 |
| --- | --- | --- |
| ![HTML 预览](./docs/assets/trae-demo/screen-06-html-preview.png) | ![演讲稿备注](./docs/assets/trae-demo/screen-08-speaker-notes.png) | ![PPTX 导出](./docs/assets/trae-demo/screen-09-export-pptx.png) |

更多开发截图保存在 [docs/assets/trae-demo](./docs/assets/trae-demo)。

## 快速开始

克隆仓库：

```bash
git clone https://github.com/xiejhhhhhh/slideforge-ai.git
cd slideforge-ai/trae-demo
```

安装 Demo 依赖：

```bash
pip install -r requirements.txt
playwright install chromium
```

启动 Demo：

```bash
python app.py
```

浏览器访问：

```text
http://127.0.0.1:5000
```

Windows 用户也可以双击：

```text
trae-demo/start.bat
```

如果只想看前端界面，也可以直接打开 [trae-demo/index.html](./trae-demo/index.html)，但 PPTX 导出需要 Flask 后端。

## AI API 配置

Demo 在浏览器端调用 OpenAI 兼容 API，可配置：

- API Base URL
- 模型名称
- API Key
- 可选视觉模型

API Key 仅保存在浏览器 `localStorage` 中。仓库只提交 [.env.example](./trae-demo/.env.example)，不会提交私钥或真实 API Key。

## 核心功能

- AI 深度理解需求，拆解主题、受众、时长、风格和交付格式。
- 生成 Markdown 大纲，包含时间分配、主标题、内容要点、讲述重点、视觉建议和版式要求。
- 根据当前 Markdown 大纲生成 HTML 幻灯片，严格保持页数一致。
- 支持上传 PNG/JPG/JPEG/WEBP/SVG/GIF 等图片资源。
- HTML 确认后逐页生成演讲稿备注。
- 支持三种 PPTX 导出模式：截图嵌入、原生可编辑绘制、模板填充。
- 可选上传 `.pptx` 模板，解析配色、字体、比例和样式提示。
- 大纲、HTML、演讲稿和 PPTX 均可在本地下载。

## 项目结构

```text
slideforge-ai/
  trae-demo/                    可交互 Demo
    index.html                  前端应用
    app.py                      Flask 辅助后端
    start.bat                   Windows 一键启动脚本
    requirements.txt            Demo 依赖
    sample_input/               安全示例需求
  docs/
    assets/trae-demo/           README 展示截图
    workflow.md                 原始工作流说明
    layout-guidelines.md        排版与修正规范
  prompts/                      可复用 AI 提示词模板
  templates/academic-16x9/      16:9 HTML 幻灯片模板
  examples/research-demo/       脱敏演示案例
  scripts/                      HTML 渲染与 PPTX 导出脚本
```

生成输出、私有测试材料、`.trae/`、缓存文件、`.pptx`、PDF 和本地临时截图默认不提交。

## 文档

- [Demo 使用说明](./trae-demo/README.md)
- [工作流指南](./docs/workflow.md)
- [排版规范](./docs/layout-guidelines.md)

## 适用场景

- 科研组会汇报
- 论文进展展示
- 课程报告
- 项目路演
- 项目答辩
- 带图片和演讲备注的技术总结

## 设计原则

SlideForge AI 的目标不是替代人的判断，而是把 AI PPT 生成拆成可检查的阶段，让人类能够审查结构、排版、图片、备注和最终导出质量。

## 开源协议

MIT License.
