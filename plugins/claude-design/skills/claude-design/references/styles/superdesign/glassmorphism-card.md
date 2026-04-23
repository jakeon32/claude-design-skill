# Glassmorphism Card Style
source: superdesign.dev
category: dark

```yaml
palette: { bg_dark: "#000000", bg_light: "#F4F4F5", zinc_accent: "#18181B", emerald: "#34D399", border: "rgba(255,255,255,0.1)", zinc_muted: "#71717A" }
typography: { heading: "Inter", body: "Inter", weight: "Inter: 500–700 heading / 300–400 body", tracking: "-0.05em (heading) / 0.2em uppercase (labels 10px)", leading: "1.05 (heading)" }
style_traits: [Glassmorphism Depth, dual dark/light mode, grain overlay 15%, emerald highlight, bento-grid pricing, 2.5rem large radius]
radius: "2.5rem (40px) major containers / 1rem–1.5rem internal cards / rounded-full nav"
effects:
  glass: "background: rgba(255,255,255,0.05), backdrop-filter: blur(12px), border: 1px solid rgba(255,255,255,0.1)"
  grain: "noise SVG fixed overlay 15% opacity on dark sections"
  floating_nav: "backdrop-blur 20px, rounded-full, 1.5px padding, links bg-white/10 rounded-full hover"
  hero_bg: "abstract image 60% opacity + gradient zinc-950/40→zinc-950/90"
  hero_text_bg: "22vw 'CREATE' bg text 3% opacity + blur filter"
  dark_block_grid: "grayscale grid lineart overlay on #18181B"
  card_hover: "scale(105%) 300ms"
animation:
  timing: "cubic-bezier(0.16, 1, 0.3, 1) 0.8s"
  reveal: "translateY(20px)→0 + opacity 0→1"
  card_scale: "scale(1.05) on hover 300ms"
layout: [max-w-1600px, floating glass rounded-full nav, 92vh 2.5rem-radius hero (split: left serif + right glass stat cards), 2col feature grid (sticky serif L + display card hover R with glass analysis), dark #18181B productivity block (3D-rotated mockup 3deg + glass code + bounce tag), 3col pricing bento (white 2rem-radius, gradient image top)]
components:
  nav: "floating rounded-full blur-20px, text-white/80, hover: bg-white/10 rounded-full"
  hero: "92vh 2.5rem-radius, abstract 60% + gradient overlay, 22vw ghost text 3%, split L-text R-glass-stats"
  glass_stat: "72px width, bg rgba(255,255,255,0.05) blur-12px, 1px white/10 border, metric 3xl + desc white/60"
  feature_grid: "2col — sticky serif 4xl–5xl L + 2x3 icon grid / R: large display card 105% hover + glass system analysis"
  dark_block: "#18181B grayscale-grid overlay, 2col: steps L / 3D-rotated mockup R with glass code + bounce tag"
  pricing_bento: "3col, white 2rem-radius, thin zinc-100 border, top: 64px img gradient-to-black, bottom: features + action btn"
  action_btn: "pill white bg black text, nested circular icon (zinc-900 bg white icon), hover: scale(1.05) + icon→zinc-700"
special_notes:
  - "2.5rem radius 모든 major section 필수 — 시각적 리듬"
  - "dark bg grain texture 필수 — flat 방지 analog depth"
  - "모든 glass 요소 1px white/10 border 필수"
  - "dark bg 플랫 컬러 금지 — subtle bottom-heavy gradient 필수"
```
