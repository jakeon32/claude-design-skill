# Synapse Style
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#030303", violet: "#8B5CF6", cyan: "#06B6D4", emerald: "#10B981", fg: "#FFFFFF", border: "rgba(255,255,255,0.1)" }
typography: { heading: "Instrument Serif", body: "Inter", weight: "Instrument Serif: 400–500 -0.02em to -0.05em / Inter: 300–600", size_hero: "text-6xl–text-9xl", tracking: "widest 0.2em (data labels) / -0.05em (serif heading)" }
style_traits: [Synapse Futuristic Dark, violet+cyan dual glow, floating orbs 6–15s, metrics ticker infinite scroll, spinning conic CTA border, IDE code block, glassmorphism pill nav]
radius: "rounded-full (nav pill + CTA) / rounded-3xl (24px+ cards) / 24px (IDE window)"
effects:
  glass: "background: rgba(10,10,10,0.7), backdrop-filter: blur(16px), border: 1px solid rgba(255,255,255,0.1)"
  violet_glow: "rgba(139,92,246,0.4) blur(40px–120px) radial"
  cyan_glow: "rgba(6,182,212,0.08) blur(40px–120px) radial"
  shimmer_text: "linear-gradient(90deg,#a78bfa 0%,#fff 40%,#fff 60%,#22d3ee 100%) bg-size 200% animated"
  orbs: "translateY(-20px) scale(1.05) 6–15s infinite float"
  shiny_border_btn: "1px padding rounded-full overflow-hidden, ::before conic-gradient(#8b5cf6 40%,#06b6d4 50%) 200%x200% rotate 4s infinite"
  card_hover: "translateY(-12px) + violet/40 border + bg intensity increase + icon scale(1.1) + slight rotation"
animation:
  timing: "cubic-bezier(0.23, 1, 0.32, 1)"
  reveal: "translateY(20px)→0 opacity 0→1, 0.2s stagger delay"
  ticker: "40s linear infinite horizontal scroll"
  orb_float: "6–15s translateY(-20px) scale(1.05) infinite"
layout: [fixed pill nav (top-6 centered 95% max-w-672px, glass #0a0a0a/70, logo gradient circle+IS text, white CTA), centered hero (violet radial top + cyan left, IS 6xl–9xl leading-0.9 shimmer last word, dual CTA shiny+link), metrics ticker (60px border-y white/5 bg-black/40, mono pairs 40s), 3col feature cards rounded-3xl (serif title, hover lift+violet glow), dark IDE window (3 window controls, mono syntax violet/cyan/emerald), #050505 footer 4col (pulsing emerald status)]
components:
  nav: "fixed top-6 pill 95% max-672px, glass #0a0a0a/70 border white/10, gradient-circle logo IS text, white rounded-full CTA"
  hero: "violet/40 radial top-center + cyan/8 left-center bg, IS 6xl–9xl leading-0.9, shimmer last-word animation, shiny-border + text-link CTAs"
  ticker: "60px infinite 40s, mono 10px uppercase neutral-500 labels + accent value pairs, border-y white/5"
  feature_cards: "3col rounded-3xl border white/5 bg white/2 p-40px, IS serif title, hover: translateY(-12px) violet-glow"
  ide_window: "#080808/80 24px radius, traffic lights low-opacity, mono syntax highlight violet/cyan/emerald/grey"
  footer: "#050505 border-top white/5, 4col, IS large logo, 10px uppercase tracking-widest links, emerald pulsing 'All Systems Operational'"
  shiny_btn: "1px padding rounded-full, ::before conic-gradient violet→cyan rotating 4s"
special_notes:
  - "IS 32px 이상 또는 브랜드 요소에만 사용"
  - "glass blur 최소 16px — bg orb 위 가독성 필수"
  - "cubic-bezier(0.23,1,0.32,1) 기술적 snappy feel 필수"
  - "border 순수 grey 금지 — white/5 또는 white/10만"
```
