---
version: alpha
name: Purple Gold Presentation
description: "A dark cinematic presentation system that inherits the spacious, video-friendly layout vocabulary of Blue Professional and applies a near-black canvas (#08090d) with purple structural accents (#b98eff) and gold emphasis (#ffc402). Display type runs Space Grotesk; Inter handles body and chrome. The system is designed for video tutorials, tech explainers, and knowledge-sharing decks that need a polished, low-density dark look."

colors:
  bg: "#08090d"
  bg-cover: "#070609"
  primary: "#b98eff"
  accent-gold: "#ffc402"
  text: "#f6f2e8"
  text-muted: "#aaa59a"
  text-light: "#746f66"
  accent-light: "rgba(185, 142, 255, 0.10)"
  accent-medium: "rgba(185, 142, 255, 0.18)"
  border: "rgba(255, 255, 255, 0.16)"
  card-bg: "rgba(255, 255, 255, 0.055)"

colors-light:
  bg: "#FFFDF5"
  bg-cover: "#F7F3E6"
  primary: "#111111"
  accent-gold: "#F7CB46"
  text: "#111111"
  text-muted: "#444444"
  text-light: "#777777"
  accent-light: "rgba(247, 203, 70, 0.18)"
  accent-medium: "rgba(247, 203, 70, 0.30)"
  border: "rgba(0, 0, 0, 0.12)"
  card-bg: "rgba(0, 0, 0, 0.04)"

typography:
  h1:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: "clamp(72px, 7vw, 112px)"
    lineHeight: 1.1
    letterSpacing: -0.02em
    color: "{colors.text}"
  h2:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(45px, 4.2vw, 61px)"
    lineHeight: 1.1
    letterSpacing: -0.02em
    color: "{colors.primary}"
  h3:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: "clamp(26px, 2.2vw, 32px)"
    lineHeight: 1.3
    letterSpacing: -0.02em
    color: "{colors.text}"
  h4-eyebrow:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(13px, 1.2vw, 16px)"
    lineHeight: 1.1
    letterSpacing: 0.08em
    textTransform: uppercase
    color: "{colors.primary}"
  body:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: "clamp(22px, 1.75vw, 27px)"
    lineHeight: 1.7
    color: "{colors.text-muted}"
  metric-value:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: "clamp(40px, 3.4vw, 52px)"
    lineHeight: 1
    color: "{colors.primary}"
  metric-label:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 600
    fontSize: "clamp(16px, 1.3vw, 18px)"
    lineHeight: 1.3
    color: "{colors.text}"
  metric-desc:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: "clamp(14px, 0.95vw, 15px)"
    lineHeight: 1.5
    color: "{colors.text-muted}"

spacing:
  pad-y: "5.5vw"
  pad-x: "5.5vw"
  pad-bottom: "8vh"
  content-max-width: "1200px"
  card-radius: "14px"
  card-pad: "28px"
  gap-grid: "24px"
  gap-md: "32px"

canvas:
  width: 1920
  height: 1080

components:
  slide:
    position: "absolute"
    display: "flex"
    flexDirection: "column"
    padding: "5.5vw 5.5vw 8vh 5.5vw"
    background: "var(--bg)"
    opacity: 0
    transform: "translateX(40px)"
    transition: "opacity 0.5s ease, transform 0.5s ease"
  slide-active:
    opacity: 1
    transform: "translateX(0)"
  slide-header:
    display: "flex"
    alignItems: "center"
    justifyContent: "space-between"
    marginBottom: "3.5vh"
  tag:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    color: "{colors.primary}"
    background: "{colors.accent-light}"
    padding: "0.55rem 1.35rem"
    borderRadius: "100px"
  card:
    background: "{colors.card-bg}"
    border: "1.5px solid {colors.border}"
    borderRadius: "{spacing.card-radius}"
    padding: "{spacing.card-pad}"
  metric-card:
    background: "{colors.card-bg}"
    border: "1.5px solid {colors.border}"
    borderRadius: "{spacing.card-radius}"
    padding: "{spacing.card-pad}"
  timeline-step:
    display: "flex"
    alignItems: "center"
    gap: "1.5rem"
    textAlign: "left"
  timeline-connector:
    width: "2rem"
    height: "3px"
    background: "{colors.border}"
  step-circle:
    width: "5.4rem"
    height: "5.4rem"
    borderRadius: "50%"
    background: "{colors.primary}"
    color: "{colors.text}"
    display: "flex"
    alignItems: "center"
    justifyContent: "center"
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: "2rem"
    fontWeight: 700
  highlight-mark:
    background: "linear-gradient(180deg, transparent 28%, rgba(255, 196, 2, 0.45) 28%)"
    color: "{colors.text}"
    padding: "0 0.35rem"
    borderRadius: "4px"
    fontWeight: 700
  nav-controls:
    position: "fixed"
    bottom: "2.5vh"
    right: "3vw"
    display: "flex"
    gap: "0.8rem"
    zIndex: 100
  slide-counter:
    position: "fixed"
    bottom: "2.5vh"
    left: "3vw"
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: "0.8rem"
    color: "{colors.text-muted}"
    letterSpacing: "0.05em"

layout:
  cover:
    background: "{colors.bg-cover}"
    justifyContent: "center"
    alignItems: "flex-start"
    paddingLeft: "16vw"
  content:
    flexDirection: "column"
    justifyContent: "center"

rules:
  - "Purple carries structure: titles, dividers, eyebrow tags, step circles, metric values, and progress indicators."
  - "Gold carries emphasis: highlighted keywords, conclusions, important data, and the highlighter mark. Gold text is always forced to warm white for readability."
  - "Use the cover layout for title slides with a top pill tag and large headline; no decorative dots."
  - "Content slides use h2 in purple, body in muted warm gray, and cards with translucent white backgrounds."
  - "Process diagrams use the vertical inline timeline: a numbered circle, title + note, and a short horizontal connector to the next step."
  - "Keep slides low-density and video-friendly: generous whitespace, large type, and clear focal points."
  - "No gradients, no glow, no glassmorphism. The look is flat, cinematic, and restrained."
  - "Optional light theme: a warm cream background (#FFFDF5) with black structure text and yellow emphasis (#F7CB46). Toggle via the theme switcher in the top-right corner of the rendered deck."

best_for:
  - "Video tutorial slides and screen recordings"
  - "Tech explainers and coding walkthroughs"
  - "Knowledge-sharing and investor-update decks"
  - "Any context that wants a dark, confident, cinematic look without playful rainbow accents"

avoid_for:
  - "Bright, playful, or rainbow palettes"
  - "Corporate blue / formal business style requirements"
  - "Heavy gradients, glow, or glassmorphism"
  - "Light-background or high-density information layouts"
