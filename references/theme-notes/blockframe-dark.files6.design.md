---
version: alpha
name: BlockFrame Dark
description: "A dark neobrutalist presentation system built on a near-black canvas, 4px solid white borders, 8px hard offset shadows, and a high-key candy palette of five saturated pastels plus cream and yellow. Display type runs Inter at weight 800-900; secondary chrome uses Space Grotesk as a quasi-monospace label face. Tilted decorative shapes puncture the borders and break the grid intentionally; each stat card carries a soft glow matching its accent. For video output the template is self-contained, uses no external images, keeps navigation chrome in selectors that the screenshot script hides automatically, and adds generous 10vw horizontal padding so platform UI never overlaps content."

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
  heading-xl: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 900, fontSize: "clamp(48px, 6vw, 96px)", lineHeight: 0.95, letterSpacing: -0.03em, textTransform: uppercase }
  heading-lg: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 800, fontSize: "clamp(32px, 4vw, 64px)", lineHeight: 1, letterSpacing: -0.02em, textTransform: uppercase }
  heading-md: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 700, fontSize: "clamp(24px, 2.5vw, 40px)", lineHeight: 1.1, letterSpacing: -0.01em }
  close-title: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 900, fontSize: "clamp(40px, 5vw, 80px)", lineHeight: 0.95, letterSpacing: -0.03em, textTransform: uppercase }
  quote-text: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 900, fontSize: "clamp(28px, 3.5vw, 52px)", lineHeight: 1.15, letterSpacing: -0.02em, textTransform: uppercase }
  stat-number: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 900, fontSize: "clamp(36px, 4vw, 64px)", lineHeight: 1 }
  card-title: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 700, fontSize: 22px, lineHeight: 1.2, textTransform: uppercase }
  body: { fontFamily: "'Inter', 'Noto Sans SC', sans-serif", fontWeight: 500, fontSize: "clamp(16px, 1.2vw, 20px)", lineHeight: 1.6 }
  label: { fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace", fontWeight: 600, fontSize: 13px, lineHeight: 1, letterSpacing: 0.08em, textTransform: uppercase }
  counter: { fontFamily: "'Space Grotesk', 'Noto Sans SC', monospace", fontWeight: 700, fontSize: 14px, lineHeight: 1, letterSpacing: 0.1em, textTransform: uppercase }

spacing:
  slide-pad-x: "10vw"
  slide-pad-y: 56px
  card-pad-lg: 60px
  gap-lg: 48px
  gap-md: 32px
  pad-bottom-clearance: 110px

canvas:
  width: 100vw
  height: 100vh
  default-background: "{colors.black}"

components:
  card-elevated: { border: "4px solid {colors.white}", background: "{colors.card}", boxShadow: "{shadows.default}", description: "Primary elevated card. 4px white border + 8px white offset shadow at 15% opacity." }
  card-small: { border: "3px solid {colors.white}", background: "{colors.card}", boxShadow: "{shadows.small}", description: "Compact card: thinner border + smaller offset shadow." }
  label-pill: { border: "3px solid {colors.white}", background: "{colors.card}", boxShadow: "{shadows.small}", description: "Universal section eyebrow. Dark base; pastel variants swap background and use black text." }
  button-primary: { border: "3px solid {colors.white}", background: "{colors.yellow}", color: "{colors.black}", boxShadow: "{shadows.small}", description: "Primary CTA. Yellow fill, black text." }
  stat-glow: { description: "Each stat card uses a soft glow shadow matching its series accent (pink/green/yellow) to lift it from the black canvas." }

decorations:
  pink-rect: "Rotated pink rectangle breaking the top-right corner of the cover frame; includes pink glow."
  green-circle: "Green circle at the bottom-right of the cover frame; includes green glow."
  yellow-bar: "Tilted yellow tab on the bottom edge of the cover frame; includes yellow glow."
  star: "Yellow clip-path star used on the closing slide."
  stripes: "Repeating white/green diagonal stripe block used as a quote-slide accent."
  dot-grid: "Low-opacity white dot grid used as a background texture on some slides."

layout_rules:
  - "Every elevated element gets a 4px or 8px hard white offset shadow at reduced opacity, except the closing frame which uses solid yellow/white shadows."
  - "All corners are square (0px radius) except small decorative dots."
  - "Full-page backgrounds are limited to near-black only."
  - "Yellow and light blue are accent-only colors: labels, icons, small deco shapes, chart fills."
  - "Headings are heavy (700-900) and may use uppercase for English; CJK text ignores uppercase."
  - "Use 10vw horizontal padding for video safety; content never touches the viewport border."
  - "Tilted decorations should break the frame intentionally but must not overlap critical text."

video_notes:
  - "Navigation chrome uses .nav-controls and .slide-counter classes; screenshot_html_slides.py hides them automatically."
  - "No external images or fonts are required beyond Google Fonts links; all shapes are CSS/SVG."
  - "Slides use absolute positioning with display:none/flex; the screenshot script forces transitions off."
  - "Recommended viewport: 1920x1080. The template uses vw/vh units and 10vw horizontal padding."

cjk:
  - "Always include 'Noto Sans SC' in the font stack after Inter / Space Grotesk."
  - "Set letter-spacing to 0 for CJK text; the existing negative letter-spacing is for Latin display type only."
  - "Increase line-height slightly for dense CJK paragraphs (1.7-1.8)."
  - "Avoid forcing uppercase transforms on CJK labels."
  - "Keep Chinese labels short; Space Grotesk mono styling is for short English chrome."

dont:
  - "Do not use pink, blue, green, cream, or yellow as full-page backgrounds."
  - "Do not remove the white borders — they are the system's signature in dark mode."
  - "Do not add blur or soft shadows except the controlled glow on stat/decor accents; keep card shadows as hard offset rectangles."
  - "Do not round card corners."
  - "Do not place navigation chrome inside the slide content area; keep it fixed at the viewport edges."
  - "Do not use low-contrast text on pastel backgrounds."

---
