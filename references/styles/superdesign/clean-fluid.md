# Clean Fluid Organic Intelligence Style
source: superdesign.dev
category: light

```yaml
palette: { bg: "#fcfbf9", dark: "#171717", indigo: "#4338ca", border: "#e5e5e5", mesh: "indigo-200/50 purple-200/40" }
typography: { heading: "Playfair Display", label: "JetBrains Mono", body: "Inter", weight: "Playfair Display: 400 italic / JetBrains Mono: uppercase 0.3–0.5em 10–14px / Inter: 400–500", size_hero: "11vw–14vw", tracking: "0.3em+ (mono) / tight (serif)" }
style_traits: [Premium Fluidity, Organic Intelligence, serif+mono editorial hybrid, wave section transition, mix-blend-difference nav, mesh gradient drift]
radius: "1rem (cards) / 50% 50% 0 0 (wave transition 120% width) / 5rem (footer top)"
effects:
  mix_blend_nav: "header mix-blend-difference — visible across all bg luminance"
  mesh_gradient: "30s infinite linear rotation/scale drift, indigo/purple blur orbs"
  wave_container: "position absolute bottom-0, 120% width div, border-radius: 50% 50% 0 0, bg #fcfbf9, transform: translate(-10%, 20%)"
  card_hover: "scale(1.02) translateY(-16px) + soft indigo-500/10 shadow 500ms"
  button_pulse: "scale(1.02) + 20px blur indigo shadow, 3s loop"
animation:
  timing: "cubic-bezier(0.22, 1, 0.36, 1) 1000ms"
  reveal: "translateY(40px)→0 + opacity 0→1, 1000ms Premium Ease"
  card_action_pill: "opacity 0 translateY(1rem) → opacity 1 translateY(0), 500ms"
layout: [fixed 80px nav (mix-blend-difference, italic serif logo, mono links grow-underline, status-pill 'System Online' green dot), 100vh hero (indigo/purple mesh gradient, serif 11–14vw leading-0.85, wave-container bridge), 2col staggered 4:3 card grid (colored bg + blur orb, mono category, serif title), 2col service accordion (sticky serif + right interactive vertical list), dark #171717 footer (5rem radius, radial indigo glow, serif quote, 3col grid)]
components:
  nav: "mix-blend-difference, italic serif logo, JetBrains Mono links 1px grow-underline, right: 'System Online' pill (pulsing green dot)"
  hero: "drifting indigo/purple mesh, serif leading-0.85, wave-container at bottom with CTA at crest"
  work_grid: "2col staggered, 4:3 ratio, rounded-2xl, colored bg + blur orb, hover: scale+lift+reveal 'View' pill"
  accordion: "sticky serif header L, interactive vertical list R — serif titles neutral→black hover, mono bracket tags"
  footer: "#171717 5rem-radius top, radial indigo glow, large serif quote, 3col mono footer"
  wave_btn: "white bg black text bold uppercase mono, positioned at wave crest"
special_notes:
  - "mix-blend-difference 헤더 필수 — 색상 전환 구간 가독성 확보"
  - "Playfair Display italic 강조 단어 필수"
  - "mono 폰트 letter-spacing 0.3em 이상 유지"
  - "box-shadow 금지 — 소프트 컬러 blur 또는 1px border만"
  - "cubic-bezier(0.22,1,0.36,1) 모든 애니메이션 필수"
```
