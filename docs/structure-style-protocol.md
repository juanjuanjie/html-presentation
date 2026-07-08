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

## Structure Options

Deck structures are defined in [`../slide_structures.yaml`](../slide_structures.yaml):

- `enterprise_report_12`: formal enterprise/project report
- `compact_report_6`: concise report
- `storyboard`: video storyboard / educational explainer

Page layouts and styles are defined in [`../references/styles.yaml`](../references/styles.yaml).

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
