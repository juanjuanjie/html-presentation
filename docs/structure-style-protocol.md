# HTML Presentation Structure × Style Protocol

This protocol separates presentation generation into three layers:

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

## Standard Request Shape

```yaml
task: html_presentation
source_material: "Raw notes, docs, transcript, or topic"
slide_structure: enterprise_report_12
style_id: video_dark_default
output:
  format: html
  offline_only: true
```

## Structure Options

Defined in [`../slide_structures.yaml`](../slide_structures.yaml):

- `enterprise_report_12`: formal enterprise/project report
- `compact_report_6`: concise report
- `storyboard`: video storyboard / educational explainer

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
