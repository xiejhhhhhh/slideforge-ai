<div align="center">

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](./requirements.txt)
[![Playwright](https://img.shields.io/badge/Playwright-HTML%20Rendering-2EAD33?style=flat-square&logo=playwright&logoColor=white)](#快速开始)
[![PPTX Export](https://img.shields.io/badge/PPTX-Export-D24726?style=flat-square&logo=microsoftpowerpoint&logoColor=white)](./scripts/export_html_to_pptx.py)
[![Markdown](https://img.shields.io/badge/Markdown-Outline-000000?style=flat-square&logo=markdown&logoColor=white)](./prompts/01_outline_prompt.md)
[![HTML Preview](https://img.shields.io/badge/HTML-Preview-E34F26?style=flat-square&logo=html5&logoColor=white)](./templates/academic-16x9/template.html)
[![AI Workflow](https://img.shields.io/badge/AI-PPT%20Workflow-5C4D7D?style=flat-square)](#slideforge-ai)
[![License MIT](https://img.shields.io/badge/License-MIT-4C956C?style=flat-square)](./LICENSE)

# SlideForge AI（幻灯锻造厂）

**从 Markdown 大纲到 HTML 预览，再到可交付 PPTX。**

[English](./README.md) | [中文](./README_CN.md)

</div>

## 项目概览

SlideForge AI 是一套开源 AI PPT 工作流，用来把 AI 生成的展示想法转化为可编辑、可检查、可交付的幻灯片。

它不追求让 AI 一步生成最终 PPT，而是把 PPT 制作拆成稳定的阶段：

```text
资料输入
  -> Markdown 大纲
  -> 16:9 HTML 预览
  -> 人工排版修正
  -> PPTX 导出
  -> 演讲备注与检查清单
```

## 为什么需要它

AI 可以很快生成 PPT 内容，但一步生成的 PPT 往往会在细节上失控：排版不稳定、文本过密、换行难看、备注缺失、图片变形、提示词难以复用。

SlideForge AI 把 PPT 制作看作一个可复现的工程流程。HTML 预览是中间验收层，用户可以在浏览器中检查并修正行距、对齐、图片、文本框和演讲备注，然后再导出 PPTX。

## 核心功能

- Markdown 优先的 PPT 大纲生成
- 16:9 HTML 幻灯片预览
- 面向人工校正的排版规范
- 基于截图的 PPTX 高保真导出
- 可复用的大纲、HTML、修正和备注提示词
- 学术汇报 / 项目报告风格示例模板

## 快速开始

安装依赖：

```bash
pip install -r requirements.txt
playwright install chromium
```

把 demo HTML 渲染为幻灯片截图：

```bash
python scripts/render_html_screenshots.py examples/research-demo/demo.html outputs/demo-rendered
```

把 demo HTML 导出为 PPTX：

```bash
python scripts/export_html_to_pptx.py examples/research-demo/demo.html outputs/slideforge-demo.pptx
```

## 项目结构

```text
slideforge-ai/
  docs/                         工作流与排版指南
  prompts/                      可复用 AI 提示词模板
  templates/academic-16x9/      16:9 HTML 幻灯片模板
  examples/research-demo/       脱敏演示案例
  scripts/                      HTML 渲染与 PPTX 导出脚本
  outputs/                      生成文件目录，默认不提交
```

## 适用场景

- 科研组会汇报
- 论文进展展示
- 课程报告
- 项目路演
- 比赛答辩
- 带图片和备注的技术总结

## 设计原则

SlideForge AI 的目标不是替代人的判断，而是让 AI 负责结构和初稿，让人类在清晰的 HTML 预览层中完成审美、表达和逻辑校正。

## 开源协议

MIT License.
