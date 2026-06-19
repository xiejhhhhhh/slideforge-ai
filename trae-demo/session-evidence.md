# SlideForge AI Demo Session Evidence

> 用于 TRAE AI 创造力大赛初赛提交：记录关键 Session ID、开发截图和发布前检查项。

## 1. Session ID 记录表

> 至少填写 3 个 TRAE Session ID。Session ID 由用户在 TRAE Work / TRAE IDE 会话中自行补充。

| Session | 任务 | Session ID | 状态 |
| --- | --- | --- | --- |
| Session 1 | 需求理解与 Demo 方案设计 | 待填写 | ☐ |
| Session 2 | 前端 `index.html` 与后端 `app.py` 生成 | 待填写 | ☐ |
| Session 3 | 真实流程测试、Bug 修复与视觉优化 | 待填写 | ☐ |
| Session 4 | README、发帖草稿和证据材料整理 | 待填写 | ☐ |

## 2. 开发阶段说明

### Session 1：需求理解与方案设计

目标：

- 读取 `trae_demo_generation_plan.md`。
- 明确 SlideForge AI 的核心链路：需求 -> 大纲 -> HTML -> 备注 -> PPTX。
- 输出页面结构、交互流程、技术方案和风险对策。

建议截图：

- TRAE 读取需求文档并给出方案设计的对话画面。

### Session 2：前后端核心代码生成

目标：

- 生成 `trae-demo/index.html`。
- 生成 `trae-demo/app.py`。
- 生成 `trae-demo/start.bat` 和 `requirements.txt`。
- 支持本地运行、AI 配置、素材上传和导出入口。

建议截图：

- TRAE 生成前端代码。
- TRAE 生成 Flask 后端代码。
- 浏览器打开 Demo 首页。

### Session 3：测试驱动修复与视觉优化

目标：

- 检查大纲质量。
- 检查 HTML 是否严格基于当前大纲。
- 检查图片是否插入到页面布局中。
- 检查演讲稿和 PPTX 导出。
- 优化空白、错位、遮挡和预览缩放。

建议截图：

- 大纲生成页面。
- HTML 幻灯片预览页面。
- 演讲稿备注页面。
- PPTX 导出页面。

### Session 4：参赛材料整理

目标：

- 补齐 `README.md` 和 `README_CN.md`。
- 整理 `trae-demo/README.md`。
- 整理 `docs/trae-demo-forum-post.md`。
- 整理展示截图到 `docs/assets/trae-demo/`。

建议截图：

- TRAE 生成或修改 README 的画面。
- GitHub README 截图展示效果。

## 3. 已整理截图

这些截图已复制到 `docs/assets/trae-demo/`，可用于 README 和发帖草稿。

| 文件 | 内容 |
| --- | --- |
| `screen-01-requirement-analysis.png` | 需求分析 / 方案设计过程 |
| `screen-02-demo-home.png` | Demo 首页 |
| `screen-03-config-step.png` | API 配置步骤 |
| `screen-04-requirement-input.png` | PPT 需求与素材输入 |
| `screen-05-outline-generation.png` | Markdown 大纲生成 |
| `screen-06-html-preview.png` | HTML 幻灯片预览 |
| `screen-07-slide-revision.png` | HTML / 幻灯片修改 |
| `screen-08-speaker-notes.png` | 演讲稿备注生成 |
| `screen-09-export-pptx.png` | PPTX 导出 |
| `screen-10-demo-summary.png` | Demo 总结 / 交付展示 |

## 4. 发布前检查清单

- [ ] `trae-demo/index.html` 可正常打开。
- [ ] `python app.py` 可启动 Flask 服务。
- [ ] `http://127.0.0.1:5000/api/health` 返回成功。
- [ ] Step 0 可保存 OpenAI 兼容 API 配置。
- [ ] Step 1 可输入需求、上传图片、可选上传 `.pptx` 模板。
- [ ] Step 2 可生成或修改 Markdown 大纲。
- [ ] Step 3 可生成或修改 HTML 幻灯片。
- [ ] Step 4 可生成或修改演讲稿备注。
- [ ] Step 5 可导出 PPTX。
- [ ] README 中所有截图路径都能在 GitHub 正常显示。
- [ ] 仓库中没有真实 API Key。
- [ ] 仓库中没有上传私有 PPT 模板、PDF 或大体积输出。
- [ ] 已填写不少于 3 个 TRAE Session ID。
- [ ] 已准备比赛帖子所需截图。

## 5. 提交范围说明

应提交：

- `trae-demo/index.html`
- `trae-demo/app.py`
- `trae-demo/start.bat`
- `trae-demo/requirements.txt`
- `trae-demo/.env.example`
- `trae-demo/README.md`
- `trae-demo/session-evidence.md`
- `trae-demo/sample_input/`
- `docs/assets/trae-demo/`
- `docs/trae-demo-forum-post.md`
- 根目录 `README.md` 和 `README_CN.md`

不应提交：

- `.trae/`
- `trae-demo/outputs/`
- `trae-demo/Chenwei_Test/`
- `trae-demo/archive/`
- `__pycache__/`
- 真实 API Key、私有模板、私有论文、私有测试数据。
