# Win98 Retro 90s Style
source: designprompts.dev
category: light

```yaml
palette: { bg: "#C0C0C0", fg: "#000000", muted: "#808080", blue: "#0000FF", red: "#FF0000", yellow: "#FFFF00", green: "#00AA00", titlebar: "#000080", titlebar_end: "#1084D0", panel_yellow: "#FFFFCC", visited: "#800080" }
typography: { heading: "Arial Black / Impact", body: "MS Sans Serif / Segoe UI / Verdana", mono: "Courier New", weight: "heading: bold/black only / body: default / labels: UPPERCASE bold", size_hero: "48–96px", tracking: "tight to wide uppercase — no expanded", leading: "1.2–1.4 headings / 1.5–1.6 body" }
style_traits: [Win95/98 Authentic, 3D bevel outset/inset, tiled crosshatch bg, system fonts, title bar gradient, animated GIF era, construction warning stripes, dotted focus ring, NO smooth transitions]
radius: "0px — 1990s had no border-radius"
shadow: "3D bevel system — NO soft shadows"
effects:
  bevel_outset: "border: 2px solid, border-color: #fff #808080 #808080 #fff, box-shadow: inset -1px -1px 0 #404040, inset 1px 1px 0 #dfdfdf"
  bevel_inset: "border-color: #808080 #fff #fff #808080 (REVERSED), box-shadow: inset 1px 1px 0 #404040, inset -1px -1px 0 #dfdfdf"
  btn_active: "bevel_inset + transform: translate(1px,1px)"
  bg_crosshatch: "linear-gradient 4-way #b8b8b8 45deg, 4px 4px tiled — subtle diagonal texture"
  construction_stripes: "repeating-linear-gradient(45deg, #ffff00 10px, #000 10px 20px) — emphasis areas"
  hr_groove: "4px linear-gradient #808080→#808080 top/bottom #fff — etched divider"
  titlebar: "linear-gradient #000080→#1084D0 horizontal — Windows 98 active window"
  text_3d: "text-shadow: 2px 2px 0 #808080 — no blur, hard edge"
  focus_ring: "outline: dotted 2px #000, outline-offset: 2px — Windows 95 focus"
animation:
  timing: "NONE or 50ms max — no smooth easing"
  btn: "active: inset + translate(1px,1px) instant"
  links: "Blue→Purple(visited)→Red(hover) instant"
layout: [max 800px or 1024px viewport reference, tiled crosshatch bg, window frames with titlebar+close/min/max buttons, content panels with bevel, dense information layout, hit counter + guestbook elements]
components:
  titlebar: "#000080→#1084D0 gradient, white text bold, window control buttons bevel"
  buttons: "bevel_outset bg-#C0C0C0 black text UPPERCASE / primary: blue bg bevel-tinted / danger: red / active: inset+translate"
  cards: "bevel_outset or sunken panel, #C0C0C0 or #FFFFCC bg"
  inputs: "bevel_inset sunken white bg, 0px radius, instant focus no ring"
  links: "pure blue #0000FF / visited #800080 / hover red — underlined"
  nav: "horizontal bar bevel_outset, Arial Black uppercase"
  hr: "groove effect 4px linear-gradient"
special_notes:
  - "0px border-radius — 1990s 절대 원칙"
  - "soft shadow 금지 — 3D bevel system only"
  - "smooth transition 금지 — instant or 50ms max"
  - "시스템 폰트 필수 (Arial Black, MS Sans Serif, Courier New)"
  - "bg flat 금지 — 4px crosshatch tiled texture 필수"
  - "construction stripes는 emphasis 섹션에 사용"
  - "모든 button 클릭시 bevel inset + translate(1px,1px)"
```
