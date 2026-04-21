# Minimalist Beta Capture Style
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#080808", fg: "#FFFFFF", silver: "#E2E8F0", silver_grad: "linear-gradient(135deg,#F8FAFC 0%,#94A3B8 100%)", border: "rgba(255,255,255,0.08)" }
typography: { heading: "DM Serif Display", label: "Geist Mono", body: "Inter", weight: "DM Serif Display: italic, clamp(42px,10vw,140px) / Geist Mono: 100–900 uppercase 0.2–0.5em 8–14px / Inter: 300–600 14–18px", tracking: "0.2–0.5em (mono labels) / tighter (serif)" }
style_traits: [Modern Obsidian, 순수 흑백+실버 팔레트, DM Serif italic silver-gradient, 92vw fluid width, frosted glass UI, noise grain 5%, editorial 베타 캡처]
radius: "4rem hero (2rem mobile) / 1rem cards / rounded-xl beta form button"
effects:
  glass: "background: rgba(255,255,255,0.02), backdrop-filter: blur(24px)"
  noise: "SVG fractalNoise 0.05 opacity"
  silver_grad_text: "linear-gradient(135deg, #F8FAFC 0%, #94A3B8 100%) background-clip text"
  silver_btn: "silver gradient bg, black text, 1px lift hover + box-shadow: 0 0 20px rgba(255,255,255,0.15)"
animation:
  timing: "cubic-bezier(0.16, 1, 0.3, 1) 0.8s"
  reveal: "translateY + opacity fade-up 0.8s"
layout: [92vw containers, 80% opacity nav (bg-white/5 border-white/10 pill links / white solid 'Join'), 92vw hero (frosted glass 30% opacity 4rem radius / DM Serif italic silver-gradient headline / 3col mono metadata bar), max-w-2xl beta form (frosted glass 2xl radius / mono input / silver button), full-width urgency section, 4col bento (border-y border-r white/10), 2col testimonials (pl-16 border-left / 5xl serif quote / mono attribution), final CTA, footer]
components:
  nav: "full 92vw, left: mono brand uppercase tracking, right: border-separated links (bg-white/5) + white 'Join' pill"
  hero: "frosted glass 30% opacity 4rem radius, DM Serif italic silver-gradient span, 3col metadata bar (Est./Description/Limit mono)"
  beta_form: "max-w-2xl frosted-glass 2xl radius, mono placeholder input no-border, silver-btn rounded-xl black mono bold uppercase"
  bento: "1→2→4 col, border-y border-r white/10 grid, 01/EFFICIENCY mono index, 4xl serif headline, mono body"
  testimonials: "full-width bg-white/[0.01], 5xl serif quote, pl-16 border-left, mono attribution, grayscale contrast-125 avatar"
  countdown: "DM Serif Display 5xl–120px, '/' separator 10% opacity, fixed-width HH:MM:SS"
  mobile_nav: "fixed bottom-6 pill, blur 24px obsidian 85%, 5 items, white center action"
special_notes:
  - "silver+monochrome palette 엄격 유지 — 파랑/빨강/녹색 금지"
  - "Geist Mono 모든 기술 레이블 필수"
  - "92vw fluid width — 표준 Tailwind container 금지"
  - "box-shadow/gradient 깊이 표현 금지 — border/backdrop-blur만"
  - "serif 헤드라인 반드시 italic"
```
