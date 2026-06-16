# SlideForge AI Workflow

## 1. Collect Source Materials

Prepare the input package:

- paper, notes, report, or project summary
- figures and result images
- target audience
- slide count and presentation time
- required template or visual style

## 2. Generate Markdown Outline

Ask AI to produce a slide-level Markdown outline. Each slide should include:

- title
- message
- content blocks
- figure suggestions
- speaker note draft

This stage is about structure, not visual polish.

## 3. Generate HTML Preview

Turn the Markdown outline into a 16:9 HTML deck. The HTML should make every slide inspectable in a browser.

Recommended constraints:

- one `.slide` section per page
- fixed 16:9 canvas
- separate text boxes for separate points
- real image assets instead of placeholders when available
- speaker notes stored near each slide or in a structured block

## 4. Human Revision

Review the HTML visually:

- fix line wrapping
- adjust paragraph spacing
- align blocks
- resize images
- avoid bottom whitespace
- check whether every page fits in 16:9

See `docs/layout-guidelines.md`.

## 5. Export PPTX

Export the reviewed HTML to PPTX.

The first stable implementation uses screenshot-based export. This preserves the HTML visual result exactly. A future editable export mode can map HTML text blocks into PPT text boxes.

## 6. Final QA

Open the PPTX and check:

- no overflow
- no clipped table
- no distorted image
- notes exist
- slide numbers are correct
- total speaking time is controlled
