# files (6) Merge Plan and Landing Notes

Date: 2026-07-08

## Goal

Merge the enhancement package from `E:\tool\.ai\files (6)` into `html-presentation` without renaming the skill to `html-studio`.

The chosen direction:

```text
Keep html-presentation as the canonical skill.
Add page/deck dual mode.
```

## Landed

### Root protocol files

- `schema.yaml`
- `aliases.yaml`
- `checklist.md`
- `USAGE.md`
- `MERGE_NOTES.md`

### References

- `references/styles.yaml`
- `references/generation_protocol.md`
- `references/style_spec.md`
- `references/themes_index.json`
- `references/frontend-slides/STYLE_PRESETS.md`
- `references/frontend-slides/animation-patterns.md`
- `references/frontend-slides/html-template.md`
- `references/frontend-slides/viewport-base.css`

### Examples

- `examples/page_weekly_report_mflex.yaml`
- `examples/page_dark_gold_insight.yaml`
- `examples/page_aurora_ui.yaml`
- `examples/deck_blockframe.yaml`
- `examples/deck_purple_gold.yaml`

### Templates

- `templates/blue-professional.html`

### Theme notes

The uploaded `*.design.md` files from `files (6)` were not used to overwrite the existing repository themes. Existing upstream `themes/*/design.md` files are fuller and remain canonical.

Uploaded notes were preserved under:

- `references/theme-notes/blockframe.files6.design.md`
- `references/theme-notes/blockframe-dark.files6.design.md`
- `references/theme-notes/blue-professional.files6.design.md`
- `references/theme-notes/purple-gold-presentation.files6.design.md`

## Updated

- `SKILL.md`
  - Added page/deck mode distinction.
  - Added schema / aliases / checklist flow.
  - Kept original video-friendly deck rules.

- `README.md`
  - Added page/deck examples.
  - Clarified `style_id` for page and `theme_id` for deck.

- `docs/structure-style-protocol.md`
  - Extended from deck-only structure/style protocol to page/deck protocol.

## Validation

Parsed successfully:

- `schema.yaml`
- `aliases.yaml`
- `slide_structures.yaml`
- `references/styles.yaml`
- `references/themes_index.json`
- `examples/page_weekly_report_mflex.yaml`
- `examples/deck_purple_gold.yaml`

## Local sync

The merged repository has been synced to:

- `E:\tool\.ai\skills\html-presentation`
- `C:\Users\86183\.codex\skills\html-presentation`

Backups were created before sync:

- `E:\tool\.ai\skills\_archive\html-presentation_before_repo_sync_20260708_151607`
- `E:\tool\.ai\skills\_archive\html-presentation_before_files6_merge_20260708_152813`

## Next step

Commit these changes to the GitHub working copy and open/update a PR.
