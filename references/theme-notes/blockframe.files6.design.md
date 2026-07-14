---
version: alpha
name: BlockFrame
description: "A maximalist neobrutalist presentation system built on 4px solid black borders, 8px hard offset shadows, and a high-key candy palette of five saturated pastels plus cream and off-white. Display type runs Inter at weight 800-900; secondary chrome uses Space Grotesk as a quasi-monospace label face. Tilted decorative shapes (rotated stars, rectangles, badges) puncture the borders and break the grid intentionally. Pastels are paired loudly: pink, blue, green, yellow, cream cycle through accents and small decorative regions. The aesthetic borrows from zine layout, 1990s-revival sticker books, and contemporary toy packaging — bold, joyful, slightly chaotic, never timid. For video output the template is self-contained, uses no external images, and keeps navigation chrome in selectors that the screenshot script hides automatically."

colors:
  black: "#000000"
  white: "#FFFFFF"
  offwhite: "#FFFDF5"
  pink: "#FE90E8"
  blue: "#C0F7FE"
  green: "#99E885"
  yellow: "#F7CB46"
  cream: "#FFDC8B"

backgrounds:
  full_page:
    - "#FFDC8B"
    - "#FFFDF5"
    - "#000000"
  note: "Full-page backgrounds are intentionally limited to cream, off-white, and the closing black slide. Yellow and light blue are reserved for labels, icons, charts, and small decorative accents only."

borders:
  primary: "4px solid {colors.black}"
  thin: "3px solid {colors.black}"

shadows:
  default: "8px 8px 0px {colors.black}"
  small: "4px 4px 0px {colors.black}"
  hover: "6px 6px 0px {colors.black}"
  close-yellow: "12px 12px 0px {colors.yellow}"
  close-white: "6px 6px 0px {colors.white}"

typography:
  heading-xl: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 900, fontSize: "clamp(48px, 6vw, 96px)", lineHeight: 0.95, letterSpacing: -0.03em, textTransform: uppercase }
  heading-lg: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 800, fontSize: "clamp(32px, 4vw, 64px)", lineHeight: 1, letterSpacing: -0.02em, textTransform: uppercase }
  heading-md: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 700, fontSize: "clamp(24px, 2.5vw, 40px)", lineHeight: 1.1, letterSpacing: -0.01em }
  close-title: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 900, fontSize: "clamp(40px, 5vw, 80px)", lineHeight: 0.95, letterSpacing: -0.03em, textTransform: uppercase }
  quote-text: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 900, fontSize: "clamp(28px, 3.5vw, 52px)", lineHeight: 1.15, letterSpacing: -0.02em, textTransform: uppercase }
  stat-number: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 900, fontSize: "clamp(36px, 4vw, 64px)", lineHeight: 1 }
  card-title: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 700, fontSize: 22px, lineHeight: 1.2, textTransform: uppercase }
  step-num: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 900, fontSize: 48px, lineHeight: 1 }
  body: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 500, fontSize: "clamp(16px, 1.2vw, 20px)", lineHeight: 1.6 }
  label: { fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace", fontWeight: 600, fontSize: 13px, lineHeight: 1, letterSpacing: 0.08em, textTransform: uppercase }
  counter: { fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace", fontWeight: 700, fontSize: 14px, lineHeight: 1, letterSpacing: 0.1em, textTransform: uppercase }

spacing:
  slide-pad: 60px
  card-pad-lg: 60px
  card-pad-md: 36px
  gap-lg: 48px
  gap-md: 32px
  gap-sm: 24px
  pad-bottom-clearance: 110px

canvas:
  width: 100vw
  height: 100vh
  default-background: "{colors.offwhite}"

components:
  card-elevated: { border: "4px solid {colors.black}", background: "{colors.white}", boxShadow: "{shadows.default}", description: "Primary elevated card. 4px ink border + 8px ink offset shadow." }
  card-flat: { border: "4px solid {colors.black}", background: "{colors.white}", description: "Bordered card without elevation shadow. For secondary cells in multi-card grids." }
  card-small: { border: "3px solid {colors.black}", background: "{colors.white}", boxShadow: "{shadows.small}", description: "Compact card: thinner border + smaller offset shadow. Intro/stat/team cards, timeline steps." }
  label-pill: { border: "3px solid {colors.black}", background: "{colors.white}", boxShadow: "{shadows.small}", description: "Universal section eyebrow. White base; pink/blue/green/yellow/cream variants swap background. 3px black border + 4px hard offset shadow." }
  button-primary: { border: "3px solid {colors.black}", background: "{colors.yellow}", color: "{colors.black}", boxShadow: "{shadows.small}", description: "Primary CTA. Yellow fill, black text. Hover lifts -2/-2 and grows shadow to 6px." }
  corner-bracket: { border: "3px solid {colors.black}", description: "Two L-shaped brackets at opposite corners of a card/frame. Frame-within-frame." }
  icon-square: { width: 64px, height: 64px, border: "3px solid {colors.black}", description: "Solid pastel square (pink/blue/green) holding a single uppercase letter glyph." }
  feature-deco: { border: "3px solid {colors.black}", background: "{colors.yellow}", description: "Yellow square notch protruding from the top edge of a feature card, breaking its border." }
  stat-deco-dot: { borderRadius: 50%, border: "2px solid {colors.black}", description: "Small colored dot at the top-right of a stat card to identify its series." }

decorations:
  pink-rect: "Rotated pink rectangle breaking the top-right corner of the cover frame."
  green-circle: "Green circle at the bottom-right of the cover frame."
  yellow-bar: "Tilted yellow tab on the bottom edge of the cover frame."
  star: "Yellow clip-path star used on the closing slide."
  stripes: "Repeating black/green diagonal stripe block used as a quote-slide accent."
  dot-grid: "Low-opacity black dot grid used as a background texture on some slides."

layout_rules:
  - "Every elevated element gets a 4px or 8px hard black offset shadow."
  - "All corners are square (0px radius) except small decorative dots."
  - "Full-page backgrounds cycle through cream, off-white, and black only."
  - "Yellow and light blue are accent-only colors: labels, icons, small deco shapes, chart fills."
  - "Headings are heavy (700-900) and may use uppercase for English; CJK text ignores uppercase."
  - "Leave generous padding around slide edges so content never touches the viewport border."
  - "Tilted decorations should break the frame intentionally but must not overlap critical text."

video_notes:
  - "Navigation chrome uses .nav-controls and .slide-counter classes; screenshot_html_slides.py hides them automatically."
  - "No external images or fonts are required beyond Google Fonts links; all shapes are CSS/SVG."
  - "Slides use absolute positioning with display:none/flex; the screenshot script forces transitions off."
  - "Recommended viewport: 1920x1080. The template already uses vw/vh units."

cjk:
  - "Always include 'Noto Sans SC' in the font stack after Inter / Space Grotesk."
  - "Set letter-spacing to 0 for CJK text; the existing negative letter-spacing is for Latin display type only."
  - "Increase line-height slightly for dense CJK paragraphs (1.7-1.8) if readability suffers."
  - "Avoid forcing uppercase transforms on CJK labels."
  - "Keep Chinese labels short; Space Grotesk mono styling is intended for short English chrome."

dont:
  - "Do not use pink, blue, green, or yellow as full-page backgrounds."
  - "Do not remove the black borders — they are the system's signature."
  - "Do not add blur or soft shadows; keep all shadows as hard offset rectangles."
  - "Do not round card corners."
  - "Do not place navigation chrome inside the slide content area; keep it fixed at the viewport edges."
  - "Do not use low-contrast text on pastel backgrounds."

---
