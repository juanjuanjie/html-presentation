# html-studio 使用说明

按注册视觉风格生成**可离线打开的单文件 HTML**。两种产物：

- **page（单页）**：一张风格页（四象限周报、暗金三栏、极光封面…）。
- **deck（多页）**：一套视频友好幻灯片，带翻页/进度条/页码/导航点，**可一键导出 1920×1080 PNG 分镜**。

一句话记法：**风格是风格，结构是结构。换风格不改页序，deck 换主题时忠于该主题、不串主题。**

---

## 1. 安装

把整个 `html-studio/` 放进 Agent skills 目录，例如 `~/.claude/skills/html-studio/`。skill 自包含，不依赖机器本地路径。deck 的 PNG 导出需要 Python：

```bash
pip install -r requirements.txt
playwright install chromium
```

---

## 2. 说人话就能用

| 你说 | 归一 |
|---|---|
| 用蓝白汇报风做一个四象限项目周报 | page · weekly_report_mflex · weekly_report_2x2 |
| 暗金风做一页数据洞察 | page · dark_gold_insight · dark_gold_three_col |
| 用这份材料做一套演示 | deck · purple-gold-presentation（默认）· compact_report_6 |
| 把稿子做成视频分镜并导出 PNG | deck · purple-gold-presentation · storyboard · export |
| 做一套粗野风的产品发布 slides | deck · blockframe · compact_report_6 |
| 商务蓝、给投资人的 12 页 | deck · blue-professional · enterprise_report_12 |

规则：只说风格不说结构时，page 用该风格默认版式、deck 用 `compact_report_6`；deck 没说主题时按你的氛围（mood/tone/scheme）匹配，兜底 `purple-gold-presentation`。

---

## 3. 显式 YAML（更可控）

### page
```yaml
mode: page
style_id: dark_gold_insight
layout_id: dark_gold_three_col
content:
  title: 数据之光，洞见未来
  columns:
    - { heading: 主观·洞察, body: 数据是业务的镜子。 }
    - { heading: 筛选·过滤, body: 去噪去伪，留下有价值的数据。 }
    - { heading: 建模·预测, body: 构建模型，预测未来。 }
```

### deck（含导出）
```yaml
mode: deck
theme_id: purple-gold-presentation
slide_structure: compact_report_6
content:
  title: 数据平台建设周报
  source_material: |
    本周接入 75%，核心模型 60%，看板 40%……（贴原始材料即可，按结构拆页）
export:
  enabled: true
  out_dir: slides_out
  mode: standard      # standard | balanced | compact | auto
```

`examples/` 有 3 个 page + 2 个 deck 样例。

---

## 4. 可选风格 / 主题

**page 风格（6，离线）**：`weekly_report_mflex` / `dark_gold_insight` / `raw_paper_notes` / `social_card_layering_v2a` / `social_dashboard_v2b` / `aurora_ui`。

**deck 主题（4，视频友好）**：

| theme_id | 气质 | scheme |
|---|---|---|
| `blockframe` | 新粗野·糖果亮色·硬阴影 | light |
| `blockframe-dark` | 新粗野·黑底荧光 | dark |
| `blue-professional` | 奶油+钴蓝·咨询级 | light |
| `purple-gold-presentation` | 紫金暗色电影感（默认）| dark |

每个主题的完整规范在 `references/themes/<slug>.design.md`；选择元数据在 `references/themes_index.json`。

## 5. 可选结构（deck）
`enterprise_report_12`(12) / `compact_report_6`(6，默认) / `storyboard`(6)。

---

## 6. deck 换主题 / 换肤

- 用某个已注册主题：给 `theme_id` 即可，skill 会读它的 `design.md` 并忠实套用（字体、配色、装饰、组件、间距）。
- 想快速试暗色默认风：直接改 `templates/presentation.html` 顶部 `:root` 的 `--title / --accent / --bg` 等变量，页序与引擎不用动。
- **铁律**：同一 deck 不混两个主题；不替换主题字体、不改配色、不删标志性装饰；缺某种版式时用该主题的设计系统就地设计（见 `references/AGENTS.md`）。

翻页：底部按钮、右侧导航点、键盘 `←/→/Home/End/空格`、触摸滑动。

---

## 7. 导出视频分镜 PNG

```bash
python screenshot_html_slides.py my-deck.html -o slides_out
```
输出 `slides_out/page_1.png…`，1920×1080，自动隐藏控件，可直接拖进剪辑软件。常用参数：`--prefix`、`--mode standard|balanced|compact|auto`、`--device-scale 2`。若主题用了 Google Fonts 又要纯离线出图，先把字体换成系统字体栈（`export.offline: true` 的含义）。

---

## 8. 验收
对照 `checklist.md`：page 查 tokens/must_have/avoid、离线；deck 另查引擎四件套、两个已知修复、忠于 design.md、无串主题、导出正常。

## 9. 边界
- page 强离线；deck 主题可用 Google Fonts。
- 复杂视觉细节是「尽量接近参考」，非像素级复刻。
