# Cyber Serif Style
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#050505", fg: "#EBEBEB", emerald: "#10b981", border: "rgba(255,255,255,0.1)" }
typography: { heading: "Newsreader", body: "Inter", label: "Space Grotesk", weight: "Newsreader: 200–800 italic / Inter: normal / Space Grotesk: 10px uppercase 0.2em tracking", size_hero: "100px tracking-tighter leading-0.9", tracking: "tighter (headline) / widest (labels)" }
style_traits: [Classical-Tech Hybrid, 딥 블랙 에디토리얼, emerald surgical accent, glassmorphism blur 12px, shimmer border 애니메이션, spotlight cursor tracking]
radius: "rounded-3xl (cards) / rounded-full (pill buttons)"
effects:
  glass: "background: rgba(255,255,255,0.02), backdrop-filter: blur(12px), border: 1px solid rgba(255,255,255,0.1)"
  shimmer_border: "::after pseudo 1px inset, linear-gradient(transparent, rgba(16,185,129,0.3), transparent) 200% size, background-position 200%→-200%, 4s linear"
  spotlight: "::before radial-gradient(600px at var(--mouse-x,--mouse-y), rgba(16,185,129,0.15), transparent 40%), opacity 0→1 on hover, JS mousemove"
  morphing_glow: "384px div bg-emerald-500/10 blur-100px, border-radius morph 8s infinite"
  emerald_underline: "1px emerald underline width 0→100% on hover"
  pulse_glow: "#10b981 CTA button — pulse shadow 애니메이션"
animation:
  timing: "cubic-bezier(0.16, 1, 0.3, 1)"
  scroll_reveal: "staggered upward motion, cards"
  count_up: "수치 카운트 애니메이션 benchmark table"
layout: [fixed nav (transparent→glass blur on scroll, command icon 360deg hover, center 링크), 100vh hero (2col: uppercase label+pulse dot / Newsreader 100px + italic emerald word / dual pill CTA — right: floating glass UI mockup), 3col spotlight card grid, benchmark table (10px Space Grotesk header), massive serif CTA (gradient-text 애니메이션)]
components:
  nav: "scroll transparent→bg-black/80 backdrop-blur-md, command icon 360deg hover, emerald underline links, pulse-glow CTA"
  hero: "left: uppercase 기술 레이블 emerald dot + 100px Newsreader italic emerald word + dual pill / right: floating glass UI mockup parallax"
  spotlight_card: "40px padding, rounded-3xl, shimmer border, icon rounded-2xl container hover rotate, serif title"
  benchmark: "Space Grotesk 10px header, 1px rgba(255,255,255,0.05) rows, emerald text 강조"
  cta: "massive serif + gradient-text (white→emerald) + emerald pulse shadow pill"
special_notes:
  - "Newsreader 세리프 — 모든 주요 헤드라인 필수"
  - "#10b981 sparingly — 큰 배경 블록 금지"
  - "scroll reveal cubic-bezier 필수"
  - "rounded-3xl 또는 full-pill — 표준 rounded-lg 금지"
```
