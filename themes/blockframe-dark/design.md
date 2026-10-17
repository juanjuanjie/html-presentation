---
version: alpha
name: BlockFrame Dark
description: "A dark neobrutalist presentation system built on a near-black canvas, 4px solid white borders, 8px hard offset shadows, and a high-key candy palette of five saturated pastels plus cream and yellow. Display type runs Inter at weight 800-900; secondary chrome uses Space Grotesk as a quasi-monospace label face. Tilted decorative shapes (rotated stars, rectangles, badges) puncture the borders and break the grid intentionally. Pastels are paired loudly: pink, blue, green, yellow, cream cycle through accents and small decorative regions; each stat card carries a soft glow matching its accent. The aesthetic borrows from zine layout, 1990s-revival sticker books, and contemporary toy packaging — bold, joyful, slightly chaotic, never timid. For video output the template is self-contained, uses no external images, keeps navigation chrome in selectors that the screenshot script hides automatically, and adds generous 10vw horizontal padding so platform UI never overlaps content."

colors:
  black: "#0a0a0a"
  card: "#141414"
  card-elevated: "#1c1c1c"
  white: "#f6f6f6"
  muted: "#a0a0a0"
  pink: "#FE90E8"
  blue: "#C0F7FE"
  green: "#99E885"
  yellow: "#F7CB46"
  cream: "#FFDC8B"

backgrounds:
  full_page:
    - "#0a0a0a"
  note: "Full-page backgrounds are intentionally limited to near-black only. Pastels and yellow are reserved for labels, icons, cards, and small decorative accents only."

borders:
  primary: "4px solid {colors.white}"
  thin: "3px solid {colors.white}"

shadows:
  default: "8px 8px 0px rgba(246, 246, 246, 0.15)"
  small: "4px 4px 0px rgba(246, 246, 246, 0.15)"
  hover: "6px 6px 0px rgba(246, 246, 246, 0.25)"
  close-yellow: "12px 12px 0px {colors.yellow}"
  close-white: "6px 6px 0px {colors.white}"
  glow-pink: "0 0 24px rgba(254, 144, 232, 0.35)"
  glow-blue: "0 0 24px rgba(192, 247, 254, 0.30)"
  glow-green: "0 0 24px rgba(153, 232, 133, 0.30)"
  glow-yellow: "0 0 24px rgba(247, 203, 70, 0.35)"

typography:
  heading-xl:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 900
    fontSize: "clamp(48px, 6vw, 96px)"
    lineHeight: 0.95
    letterSpacing: -0.03em
    textTransform: uppercase
  heading-lg:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 800
    fontSize: "clamp(32px, 4vw, 64px)"
    lineHeight: 1
    letterSpacing: -0.02em
    textTransform: uppercase
  heading-md:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 700
    fontSize: "clamp(24px, 2.5vw, 40px)"
    lineHeight: 1.1
    letterSpacing: -0.01em
  close-title:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 900
    fontSize: "clamp(40px, 5vw, 80px)"
    lineHeight: 0.95
    letterSpacing: -0.03em
    textTransform: uppercase
  quote-text:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 900
    fontSize: "clamp(28px, 3.5vw, 52px)"
    lineHeight: 1.15
    letterSpacing: -0.02em
    textTransform: uppercase
  stat-number:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 900
    fontSize: "clamp(36px, 4vw, 64px)"
    lineHeight: 1
  card-title:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 700
    fontSize: 22px
    lineHeight: 1.2
    textTransform: uppercase
  step-num:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 900
    fontSize: 48px
    lineHeight: 1
  body:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 500
    fontSize: "clamp(16px, 1.2vw, 20px)"
    lineHeight: 1.6
  body-card:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 500
    fontSize: 15px
    lineHeight: 1.6
  list-body:
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 500
    fontSize: 16px
    lineHeight: 1.5
  label:
    fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace"
    fontWeight: 600
    fontSize: 13px
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  mono-tag:
    fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace"
    fontWeight: 600
    fontSize: 14px
    lineHeight: 1
    letterSpacing: 0.05em
    textTransform: uppercase
  mono-meta:
    fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace"
    fontWeight: 500
    fontSize: 15px
    letterSpacing: 0.02em
  subtitle-mono:
    fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace"
    fontWeight: 500
    fontSize: 18px
    lineHeight: 1.5
  counter:
    fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace"
    fontWeight: 700
    fontSize: 14px
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  legend-item:
    fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace"
    fontWeight: 600
    fontSize: 13px

spacing:
  slide-pad-x: "10vw"
  slide-pad-y: 56px
  card-pad-lg: 60px
  card-pad-md: 36px
  card-pad-sm: 28px
  card-pad-xs: 22px
  gap-lg: 48px
  gap-md: 32px
  gap-sm: 24px
  gap-xs: 16px
  pad-bottom-clearance: 110px

canvas:
  width: 100vw
  height: 100vh
  default-background: "{colors.black}"

components:
  card-elevated:
    border: "4px solid {colors.white}"
    background: "{colors.card}"
    boxShadow: "{shadows.default}"
    description: "Primary elevated card. 4px white border + 8px white offset shadow at 15% opacity. Background is dark card by default; pastel fills may be used for accent cards."
  card-flat:
    border: "4px solid {colors.white}"
    background: "{colors.card}"
    description: "Bordered card without elevation shadow. Used for secondary content cells inside multi-card grids where the shadow would compound."
  card-small:
    border: "3px solid {colors.white}"
    background: "{colors.card}"
    boxShadow: "{shadows.small}"
    description: "Compact card with thinner border + smaller offset shadow. Used for intro-cards, stat-cards, team-cards, and timeline-steps."
  label-pill:
    border: "3px solid {colors.white}"
    padding: "6px 16px"
    fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace"
    fontSize: 13px
    fontWeight: 600
    letterSpacing: 0.08em
    textTransform: uppercase
    background: "{colors.card}"
    boxShadow: "{shadows.small}"
    description: "Universal section eyebrow. Dark base by default; pink, blue, green, yellow, cream variants swap background and use black text. Always sits on a 3px white border with a 4px hard offset shadow."
  button-primary:
    border: "3px solid {colors.white}"
    background: "{colors.yellow}"
    color: "{colors.black}"
    padding: "14px 32px"
    fontFamily: "'Inter', 'Noto Sans SC', sans-serif"
    fontWeight: 700
    fontSize: 16px
    boxShadow: "{shadows.small}"
    description: "Primary CTA. Yellow fill with black text, 3px white border, 4px offset shadow. Hover lifts the button -2/-2 and grows shadow to 6px."
  corner-bracket:
    width: 24px
    height: 24px
    border: "3px solid {colors.white}"
    description: "Two L-shaped brackets at opposite corners of a card or frame (tl + br + tr + bl pattern available). Sits inside the card edge as a decorative frame-within-frame."
  icon-square:
    width: 64px
    height: 64px
    border: "3px solid {colors.white}"
    description: "Solid pastel square (pink/blue/green) holding a single uppercase letter glyph at weight 700 / 28px. Used as feature-card icons."
  feature-deco:
    width: 48px
    height: 48px
    border: "3px solid {colors.white}"
    background: "{colors.yellow}"
    position: "absolute top -12px right 24px"
    description: "Yellow square notch that protrudes from the top edge of a feature card, breaking the card's top border line."
  stat-deco-dot:
    width: 12px
    height: 12px
    borderRadius: 50%
    border: "2px solid {colors.white}"
    description: "Small colored dot placed at the top-right of a stat card to identify its series."
  stat-glow:
    description: "Each stat card uses a soft glow shadow matching its series accent (pink/green/yellow) to lift it from the black canvas."

decorations:
  pink-rect:
    description: "Rotated pink rectangle breaking the top-right corner of the cover frame; includes pink glow."
  green-circle:
    description: "Green circle at the bottom-right of the cover frame; includes green glow."
  yellow-bar:
    description: "Tilted yellow tab that sits on the bottom edge of the cover frame; includes yellow glow."
  star:
    description: "Yellow clip-path star used on the closing slide."
  stripes:
    description: "Repeating white/green diagonal stripe block used as a quote-slide accent."
  dot-grid:
    description: "Low-opacity white dot grid used as a background texture on some slides."

layout_rules:
  - "Every elevated element gets a 4px or 8px hard white offset shadow at reduced opacity, except closing frame which uses solid yellow/white shadows."
  - "All corners are square (0px radius) except small decorative dots."
  - "Full-page backgrounds are limited to near-black only."
  - "Yellow and light blue are accent-only colors: labels, icons, small deco shapes, chart fills."
  - "Headings are heavy (700-900) and may use uppercase for English; CJK text ignores uppercase."
  - "Leave generous padding around slide edges so content never touches the viewport border; use 10vw horizontal padding for video safety."
  - "Tilted decorations should break the frame intentionally but must not overlap critical text."

video_notes:
  - "Navigation chrome uses .nav-controls and .slide-counter classes; screenshot_html_slides.py hides them automatically."
  - "No external images or fonts are required beyond Google Fonts links; all shapes are CSS/SVG."
  - "Slides use absolute positioning with display:none/flex; the screenshot script forces transitions off."
  - "Recommended viewport: 1920x1080. The template already uses vw/vh units and 10vw horizontal padding for platform UI safety."

cjk:
  - "Always include 'Noto Sans SC' in the font stack after Inter / Space Grotesk."
  - "Set letter-spacing to 0 for CJK text; the existing negative letter-spacing is for Latin display type only."
  - "Increase line-height slightly for dense CJK paragraphs (1.7-1.8) if readability suffers."
  - "Avoid forcing uppercase transforms on CJK labels; text-transform has no effect but should not be relied upon."
  - "Keep Chinese labels short; Space Grotesk mono styling is intended for short English chrome."

dont:
  - "Do not use pink, blue, green, cream, or yellow as full-page backgrounds."
  - "Do not remove the white borders — they are the system's signature in dark mode."
  - "Do not add blur or soft shadows except the controlled glow on stat/decor accents; keep card shadows as hard offset rectangles."
  - "Do not round card corners."
  - "Do not place navigation chrome inside the slide content area; keep it fixed at the viewport edges."
  - "Do not use low-contrast text on pastel backgrounds."

## Agent 提示词规则

> 本页“说明”相当于模板使用手册，供用户阅读；`design.md` 本身不会被首页读取，也不会直接写入复制出的 Agent 提示词。

### 当前参与情况

BlockFrame · 暗黑糖果目前没有额外的模板专属硬规则参与 Agent 提示词。首页生成时会传入暗色模板的完整 `template.html`、当前配色变量，以及通用的字幕、转场、对比和生成规则；Agent 主要通过模板源码继承近黑背景、白色粗边框、硬阴影和糖果色小面积强调。

本说明中的 `backgrounds`、`layout_rules`、`dont` 等内容目前仅作为人工使用规范，不会因为写在这里而自动约束 Agent。
