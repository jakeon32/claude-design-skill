# Red Sun Style
source: superdesign.dev
category: light

```yaml
palette: { coral: "#EF4623", ink: "#2D3B42", peach: "#FDF1EE", white: "#FFFFFF" }
typography: { heading: "Instrument Serif", body: "Manrope", weight: "Instrument Serif: tracking-tight / Manrope: 300–700", size_hero: "10rem (mobile 4rem)", tracking: "tight (heading) / widest (uppercase labels xs)" }
style_traits: [Coral and Ink Editorial, 비대칭 모듈 구조, bento grid features, glassmorphism nav, rotating logo mark, scroll-triggered fade-up 2deg 회전]
radius: "rounded-3xl to rounded-[3rem] (48px) — 최소 24px"
effects:
  glassmorphism_nav: "backdrop-blur 12px, rgba(255,255,255,0.8) on scroll, bottom border"
  ambient_blur: "#EF4623 10% opacity + blur 100–120px 배경 orbs"
  rotating_logo: "36px square #EF4623, 3deg default rotate, italic serif letter, hover→12deg 300ms"
  ui_simulator: "#2D3B42 bg 40px radius, white inner rounded-3xl, skeleton loaders, glassmorphism code bar"
  dot_grid_cta: "white dot grid 20% opacity 30px spacing, full-width #EF4623 4rem radius container"
animation:
  timing: "cubic-bezier(0.16, 1, 0.3, 1)"
  reveal: "translateY + opacity 0→1 + rotate(2deg)→0, entry"
  button_pulse: "scale(1.02) + 20px blur shadow"
layout: [fixed nav (glassmorphism scroll, 로고 rotating mark, #EF4623 pill CTA), centered hero (pill badge + 2-line Instrument Serif italic second line coral / subtext + dual pill CTA + ambient orbs), 2col bento (text+icon-list / UI Simulator mockup), 3col feature bento (3rem radius, dark/light/standard cards), full-width coral CTA (4rem radius + dot grid), #2D3B42 5col footer]
components:
  nav: "glassmorphism scroll-triggered, rotating #EF4623 logo mark, Manrope sm links, #EF4623 pill CTA uppercase xs"
  hero: "pill badge #FDF1EE + sparkles, Instrument Serif 10rem (second line italic coral), Manrope body, primary pill shadow-2xl, ghost 2px border-ink/10"
  bento_left: "2col, 56px rounded-2xl 아이콘 컨테이너, serif H2"
  ui_sim: "#2D3B42 card 40px radius, white inner rounded-3xl, skeleton loaders, green check glassmorphism footer bar"
  feature_card_dark: "#2D3B42 bg, white text, #EF4623 accent icons"
  cta_section: "full-width #EF4623 rounded-[4rem], dot grid pattern, serif 8rem, trust-bar footer"
  footer: "#2D3B42, 5col, circular white/10 social icons, serif H4 링크 헤더"
special_notes:
  - "Instrument Serif 대형 헤드라인 필수"
  - "cubic-bezier(0.16,1,0.3,1) 모든 entry 애니메이션"
  - "최소 24px radius — 날카로운 모서리 금지"
  - "#EF4623 strictly — blue/green primary 대체 금지"
```
