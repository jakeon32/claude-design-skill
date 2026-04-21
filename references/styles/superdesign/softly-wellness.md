# Softly - Digital Wellness App Style
source: superdesign.dev
category: light

```yaml
palette: { bg: "#FDFCF8", sage: "#E8EFE8", lavender: "#EFEDF4", coral: "#FFB7B2", dark: "#292524", muted: "#78716C", stone_200: "#e7e5e0" }
typography: { heading: "Outfit", accent: "Reenie Beanie", weight: "Outfit: 400–600 / Reenie Beanie: 400 cursive", tracking: "-0.025em (heading)", size_hero: "72px–96px", case: "sentence-case only" }
style_traits: [Digital Minimalism + Gen-Z Lifestyle, soft pastel 웰니스, grain texture 0.35 opacity, large border-radius 2rem–4rem, 아날로그 온기, 플로팅 blob 애니메이션]
radius: "2rem–4rem (containers) / rounded-3xl (cards 24px) / rounded-full (nav pill, buttons)"
shadow: "soft 0 4px 20px -2px rgba(0,0,0,0.05)"
effects:
  grain_overlay: "fixed div z-50, SVG feTurbulence baseFrequency 0.65, mix-blend-mode: overlay, opacity: 0.35, pointer-events: none"
  blob_bg: "#FFE4E1 + #E6E6FA 60% opacity large blur blobs, 6s floating 애니메이션"
  blob_float: "translateY ±10px, 6s ease-in-out infinite"
  diary_cards: "약간 +1/-1deg rotation, white bg, Reenie Beanie signature style"
animation:
  reveal: "translateY(30px)→0 + opacity 0→1, 0.8s ease-out"
  blob: "translateY ±10px, 6s ease-in-out infinite"
layout: [floating pill nav (70% white opacity, 20px blur, coral CTA, -32px mobile margin), centered hero (72px Outfit + Reenie Beanie 강조어 + coral CTA pill), 288px×160px 가로 스크롤 scenario cards, 3-mockup 스택 (center 300×620 + left/right 280×580), 2col 다이어리 testimonial 그리드, 중앙 waitlist 전환 섹션]
components:
  nav: "pill 70% white opacity, 20px backdrop-blur, 동그란 로고 coral #FFB7B2 + white dot, 14px Outfit, #292524 pill CTA"
  hero: "center, Outfit 72px + Reenie Beanie 강조어, coral CTA pill + soft shadow, secondary white 1px border pill"
  scenario_scroll: "288×160px white rounded-3xl, 14px stone-400 timestamp, 20px stone-800 text, hover pastel color"
  mockups: "center 300×620 full opacity + left/right 80% opacity + vertical cascade (+48/+96px)"
  testimonials: "±1deg rotate, white bg, 32px hr + Reenie Beanie 24px stone-500"
  faq: "white bg 16px radius 1px stone-100 border, plus icon 45deg rotate, 500ms ease-in-out"
special_notes:
  - "Outfit + Reenie Beanie 조합 — 다른 폰트 혼용 금지"
  - "grain overlay 0.35 opacity 필수 — analog 온기"
  - "radius 절대 2rem 이하 금지"
  - "sentence-case — uppercase 금지"
```
