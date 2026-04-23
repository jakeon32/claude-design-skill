# Sketch Hand-Drawn Style
source: designprompts.dev
category: light

```yaml
palette: { bg: "#fdfbf7", fg: "#2d2d2d", muted: "#e5e0d8", red: "#ff4d4d", blue: "#2d5da1", post_it: "#fff9c4" }
typography: { heading: "Kalam", body: "Patrick Hand", weight: "Kalam: 700 thick felt-tip / Patrick Hand: 400 handwritten", tracking: "natural handwritten" }
style_traits: [Hand-Drawn Human Touch, organic imperfection, wobbly borders, hard offset shadows, handwritten fonts, tape/thumbtack decorations, dashed lines, playful rotation, paper texture]
radius: "wobbly irregular — border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px (custom per element)"
shadow: "solid offset no-blur: 4px 4px 0px 0px #2d2d2d / 8px 8px 0px 0px #2d2d2d emphasized"
effects:
  paper_texture: "radial-gradient(#e5e0d8 1px, transparent 1px) 24px 24px bg-size — notebook grain"
  tape: "translucent gray bar top-center slight rotation — sticker decoration"
  thumbtack: "red circle at top center — card pin decoration"
  post_it: "#fff9c4 bg feature cards"
  speech_bubble: "border-based triangle tail for testimonials"
  dashed_overlays: "border-dashed secondary elements, dividers, sketchy frames"
  arrow_svg: "hand-drawn dashed SVG arrow pointing to hero CTA"
  squiggle_steps: "squiggly SVG connecting line between 'How It Works' steps"
  corner_marks: "hand-drawn corner frame marks on hero image"
  wavy_underline: "wavy underline decoration on nav links + footer headers"
animation:
  bounce: "gentle 3s duration decorative elements"
  rotation_hover: "hover:rotate-1 or hover:-rotate-1 on cards"
  button_press: "translate+4px fill-shadow-gap on active"
layout: [dot-pattern paper bg, max-w-5xl/max-w-3xl containers, py-20 section rhythm, rotation cards -2deg to +2deg, overlapping decorative elements, z-index layered SVG backgrounds]
components:
  buttons: "wobbly oval, white bg 3px black border, 4px 4px hard shadow / hover: red fill white text 2px shadow translate / active: shadow 0 translate+4px"
  cards: "white wobbly border-2, 3px 3px shadow subtle, tape or tack decoration, hover: rotate + scale"
  post_it: "#fff9c4 bg wobbly card for featured content"
  testimonials: "speech bubble with border-triangle tail"
  inputs: "wobbly border-2, Patrick Hand font, focus: blue border + ring-2"
  nav: "Kalam links, wavy underline hover"
  stats: "organic shape varied border-radius (not perfect circles)"
special_notes:
  - "straight line 금지 — 모든 container wobbly border-radius 필수"
  - "blur shadow 금지 — solid offset only"
  - "handwritten fonts only (Kalam, Patrick Hand) — sans/serif 금지"
  - "small rotations (-2deg to 2deg) 레이아웃 적극 활용"
  - "tape/thumbtack/speech-bubble decorations으로 authentic paper feel"
  - "dot-pattern paper bg 필수"
```
