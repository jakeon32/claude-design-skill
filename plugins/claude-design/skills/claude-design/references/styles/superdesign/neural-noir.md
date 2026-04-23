# Neural Noir Interface Style
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#0a0a0a", gold: "#a78b71", gold_light: "#c9b8a0", gold_hover: "#e8d5b7", fg: "#FFFFFF", border: "rgba(255,255,255,0.1)" }
typography: { heading: "Playfair Display", body: "Inter", weight: "Playfair Display: bold italic / Inter: 300–700", size_hero: "clamp(2.5rem,8vw,6rem)", tracking: "wide uppercase (labels/roles) / tight (serif)" }
style_traits: [Luxury AI Dark, gold/bronze spectrum, radial dot grid 32px 8%, neural SVG connections, satellite media cards, glassmorphism 0.03 opacity]
radius: "24px–48px major containers / rounded-full nav + pill btn / rounded-20px satellite cards"
effects:
  glass: "background: rgba(255,255,255,0.03), backdrop-filter: blur(10px), border: 1px solid rgba(255,255,255,0.1)"
  bg_dots: "radial dot grid 32px spacing white 8% opacity"
  central_glow: "box-shadow: 0 0 100px rgba(167,139,113,0.2)"
  neural_lines: "SVG path stroke-width 2.5, linear-gradient stroke #c9b8a0(90%)→#a78b71(10%), pulsing-branch opacity 0.4→0.7, secondary dashed stroke-dasharray: 5 15"
  satellite_cards: "glass 220px–340px, grayscale img rounded-20px, hover: scale(1.05) + grayscale→color 0.7s + gold glow"
  icon_hover: "scale(1.1x) + card border brightens"
  live_pill: "glass pill border-white/10, 8px green-400 animate-pulse, 'LIVE' green 8px bold"
animation:
  timing: "cubic-bezier(0.4, 0, 0.2, 1)"
  reveal: "power4.out entrance, translateY(20px)→0 + opacity 0→1"
  satellite: "mouse-interactive floating + grayscale→color 0.7s hover"
layout: [fixed 100% nav (PD bold italic logo, center Inter 11px uppercase links, white pill CTA), 16:9 glass central node hero (PD italic heading gold highlights, floating satellite cards + neural SVG bezier, dual CTA), 4col glassmorphic feature grid (gold/10 icon box, hover border+scale), 3col pricing (gold/40 border Pro card + 'Most Popular', monthly/annual toggle), 2col team 4:5 grayscale→color, 5col footer (circular social icons, 'Join Digest' input)]
components:
  nav: "fixed px-6–px-12, PD bold italic logo, 11px uppercase wide links, white rounded-full pill CTA"
  hero: "central 16:9 glass card, satellite media cards floating, neural SVG bezier connections, PD italic clamp headline gold highlights"
  feature_grid: "4col glass cards, 48px gold/10 icon box, Inter bold 20px title, gray-400 body"
  pricing: "3-tier, Pro: gold/40 border + 'Most Popular' badge, 48px bold price, monthly/annual toggle"
  team: "2col 4:5 grayscale→color 0.7s, serif name + ultra-thin wide uppercase gold role"
  footer: "5col, circular border social icons L, 'Join Digest' low-opacity input + circular arrow-btn R"
  neural_lines: "SVG paths stroke-width 2.5, gold gradient, pulsing-branch + dashed flow"
special_notes:
  - "blue/purple gradient 금지 — gold/bronze spectrum 엄격 유지"
  - "소형 uppercase 텍스트 heavy letter-spacing 필수"
  - "backdrop-filter: blur(10px) 모든 overlapping 레이어 필수"
  - "#0a0a0a bg + white/gold 고대비 유지"
```
