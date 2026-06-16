<div align="center">

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](./requirements.txt)
[![Playwright](https://img.shields.io/badge/Playwright-HTML%20Rendering-2EAD33?style=flat-square&logo=playwright&logoColor=white)](#quick-start)
[![PPTX Export](https://img.shields.io/badge/PPTX-Export-D24726?style=flat-square&logo=microsoftpowerpoint&logoColor=white)](./scripts/export_html_to_pptx.py)
[![Markdown](https://img.shields.io/badge/Markdown-Outline-000000?style=flat-square&logo=markdown&logoColor=white)](./prompts/01_outline_prompt.md)
[![HTML Preview](https://img.shields.io/badge/HTML-Preview-E34F26?style=flat-square&logo=html5&logoColor=white)](./templates/academic-16x9/template.html)
[![AI Workflow](https://img.shields.io/badge/AI-PPT%20Workflow-5C4D7D?style=flat-square)](#slideforge-ai)
[![License MIT](https://img.shields.io/badge/License-MIT-4C956C?style=flat-square)](./LICENSE)

# SlideForge AI

**From Markdown outline to HTML preview, then to deliverable PPTX.**

[English](./README.md) | [中文](./README_CN.md)

</div>

## Project Overview

SlideForge AI is an open workflow for turning AI-generated presentation ideas into editable, reviewable, and deliverable slides.

Instead of asking AI to create a final PPT in one fragile step, SlideForge AI uses a staged pipeline:

```text
Source materials
  -> Markdown outline
  -> 16:9 HTML preview
  -> human layout revision
  -> PPTX export
  -> speaker notes and QA checklist
```

## Why This Exists

AI can produce slide content quickly, but one-shot PPT generation often fails in the details: unstable layout, dense text, poor line breaks, missing speaker notes, distorted figures, and hard-to-reuse prompts.

SlideForge AI treats PPT creation as a reproducible workflow. The HTML preview becomes the review surface, where humans can inspect and correct spacing, alignment, image placement, text boxes, and narration before exporting to PPTX.

## Key Features

- Markdown-first slide outlining
- 16:9 HTML slide preview
- human revision guidelines for layout polish
- screenshot-based PPTX export for high visual fidelity
- reusable prompts for outline, HTML, revision, and speaker notes
- academic/report-style demo template

## Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
playwright install chromium
```

Render the demo HTML into slide screenshots:

```bash
python scripts/render_html_screenshots.py examples/research-demo/demo.html outputs/demo-rendered
```

Export the demo HTML into PPTX:

```bash
python scripts/export_html_to_pptx.py examples/research-demo/demo.html outputs/slideforge-demo.pptx
```

## Project Structure

```text
slideforge-ai/
  docs/                         workflow and layout guides
  prompts/                      reusable AI prompt templates
  templates/academic-16x9/      base HTML slide template
  examples/research-demo/       sanitized demo presentation
  scripts/                      HTML rendering and PPTX export scripts
  outputs/                      generated files, ignored by git
```

## Best Use Cases

- research group meeting slides
- paper progress reports
- course presentations
- project roadshows
- competition proposal decks
- technical summaries with images and notes

## Design Principle

The goal is not to replace human judgment. The goal is to let AI draft structure and visuals, then give humans a clean inspection layer before the final PPT is produced.

## License

MIT License.
