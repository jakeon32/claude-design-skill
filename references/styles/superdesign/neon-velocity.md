# Neon Velocity Countdown Style
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#050505", lime: "#BFFF00", fg: "#FFFFFF", fg_muted: "rgba(255,255,255,0.4)", border: "rgba(255,255,255,0.1)" }
typography: { heading: "Plus Jakarta Sans", label: "Geist Mono", body: "Inter", weight: "Plus Jakarta Sans: 800 / Geist Mono: 400–600 uppercase 0.2–0.5em tracking / Inter: 300–400", size_hero: "clamp(2.6rem,10vw,8.75rem)", tracking: "-0.05em uppercase (headline) / 0.3em (nav links)" }
style_traits: [Brutalist + Futuristic, 네온 라임 고에너지, 3D perspective hero glass card, bento luminosity cards, laser button sweep 효과, 노이즈 grain 3%, mobile bottom pill nav]
radius: "2rem (cards) / rounded-full (laser button, avatar stack)"
effects:
  noise: "SVG fractalNoise 3% opacity, fixed viewport"
  refraction_glow: "#BFFF00 15% opacity large radial-gradient ambiance"
  glass: "backdrop-filter: blur(12px), 1px solid white/8% opacity"
  laser_button: "bg #BFFF00, text #000, rounded-full, box-shadow: 0 0 20px rgba(191,255,0,0.3), hover: linear-gradient sweep pseudo 45deg 0.6s"
  luminosity_card: "radial-gradient top-left white/3% → transparent, border white/5%, hover: border lime/30% + bg lime/5%"
  hero_3d: "perspective(1000px) rotateX(15deg) glass card, 12px border-width box"
  countdown: "tabular-nums, Plus Jakarta Sans"
  avatar_stack: "2px #BFFF00 border + neon shadow"
animation:
  timing: "cubic-bezier(0.16, 1, 0.3, 1)"
  scroll_reveal: "translateY(40px)→0 + opacity, staggered"
  laser_sweep: "0.6s 45deg gradient sweep on hover"
layout: [max-width 1600px, full-width header (로고 PJS bold uppercase / right Geist Mono 0.3em links), stacked hero (3D glass card 15deg + 12px border headline box + split metadata: location/status + countdown), 3col bento luminosity cards (01/ETHOS index + large headline + description), avatar stack + pill form (blur background), fixed bottom mobile nav pill]
components:
  header: "PJS bold uppercase logo, Geist Mono 10px 0.3em right links, 'Laser Button' CTA rounded-full"
  hero: "central 3D glass 15deg card, 12px border-box headline, left: location/status tag, right: PJS countdown tabular-nums"
  bento_card: "2rem radius, min-height 450px, top-left radial glow, 01/ETHOS mono index, large headline, description"
  form: "pill rgba(255,255,255,0.05) blur container, borderless mono input, 'Laser Button' submit"
  mobile_nav: "fixed bottom-6 center, rgba(10,10,10,0.8) backdrop-blur, pill shape, 5 items, white CTA middle, #BFFF00 hover"
  laser_btn: "#BFFF00 bg, #000 text, rounded-full, glow shadow, hover sweep pseudo"
special_notes:
  - "uppercase 모든 기술 레이블 필수"
  - "tabular-nums 카운트다운 — layout shift 방지"
  - "Hero border-box: sharp 0px — 아래 카드 둥근 것과 대비"
  - "순수 검정 #000 금지 — #050505 유지"
```
