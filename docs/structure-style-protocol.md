# HTML Presentation Structure × Style Protocol

This protocol separates HTML generation into two product modes and three layers:

```text
content_outline + slide_structure + visual_style
```

In Chinese:

```text
风格是风格，结构是结构。
可以替换风格，但是结构不变。
```

## Responsibilities

| Layer | Responsibility | Example |
|---|---|---|
| Content | What to say | source material, topic, claims, data |
| Structure | How to tell it | cover, agenda, background, method, result |
| Style | How it looks | dark video theme, blue corporate, Aurora, etc. |
| Engine | How it runs | slide switching, progress bar, dots, screenshots |

## Modes

| mode | Output | Structure key | Style key |
|---|---|---|---|
| `page` | Single-page styled HTML | `layout_id` | `style_id` |
| `deck` | Multi-page HTML presentation | `slide_structure` | `theme_id` |

## Standard Request Shape

### Page

```yaml
mode: page
style_id: weekly_report_mflex
layout_id: weekly_report_2x2
content:
  title: 项目汇报
```

### Deck

```yaml
task: html_presentation
mode: deck
source_material: "Raw notes, docs, transcript, or topic"
slide_structure: enterprise_report_12
theme_id: purple-gold-presentation
output:
  format: html
  offline_only: true
```

Deck `theme_id` accepts both native deck themes and page-style adapter themes:

- Native deck themes: `blockframe`, `blockframe-dark`, `blue-professional`, `purple-gold-presentation`.
- Page-style adapter themes: `weekly_report_mflex`, `dark_gold_insight`, `raw_paper_notes`, `social_card_layering_v2a`, `social_dashboard_v2b`, `aurora_ui`.

When a page style is used as `theme_id`, the deck keeps `slide_structure` as the page order and reads visual tokens from `../references/styles.yaml`.
It does not repeat the fixed one-page layout on every slide.

## Structure Options

Deck structures are defined in [`../slide_structures.yaml`](../slide_structures.yaml):

- `enterprise_report_12`: formal enterprise/project report
- `compact_report_6`: concise report
- `storyboard`: video storyboard / educational explainer

Page layouts and styles are defined in [`../references/styles.yaml`](../references/styles.yaml). The same style tokens can also be used by deck as page-style adapter themes.

## Style Replacement Rules

When a `style_id` or theme is provided:

1. Keep the selected `slide_structure` unchanged.
2. Keep the slide engine unchanged.
3. Keep controls, progress, dots, and screenshot hiding behavior unchanged.
4. Replace only:
   - background
   - palette
   - typography feel
   - card/panel surface
   - decorative language
   - emphasis color
5. Validate that the final output still satisfies the video-friendly rules:
   - one core point per slide
   - large readable type
   - strong contrast
   - no external dependencies unless explicitly intended

## Example

Same structure, different style:

```yaml
slide_structure: enterprise_report_12
style_id: blue_professional
```

```yaml
slide_structure: enterprise_report_12
style_id: video_dark_default
```

The page order and content logic remain the same; only the visual skin changes.
