# Futuristic SaaS Landing Page Style
source: superdesign.dev
category: dark

```yaml
palette: { dark: "#0f172a", indigo: "#6366f1", surface: "#f8f9fa", border_glass: "rgba(255,255,255,0.1)", card_dark: "rgba(30,41,59,0.7)" }
typography: { heading: "Lora", body: "Inter", display: "Space Grotesk", weight: "Lora: 400–700 / Inter: 400–600 / Space Grotesk: tracking-tight", size_hero: "text-7xl", tracking: "tight (heading) / normal (body)" }
style_traits: [Modern Atmospheric, 다크+라이트 혼합, glassmorphism, indigo 글로우 그라디언트, typing cursor 애니메이션, 세리프 감성 헤드라인]
radius: "rounded-2xl (글래스 패널) / rounded-full (pill nav, CTA)"
effects:
  glass_soft: "background: rgba(255,255,255,0.05), backdrop-filter: blur(12px), border: 1px solid rgba(255,255,255,0.1)"
  glass_strong: "background: rgba(30,41,59,0.7), backdrop-filter: blur(16px), border: 1px solid rgba(255,255,255,0.1), shadow: 0 4px 30px rgba(0,0,0,0.1)"
  glow_gradient: "radial-gradient from-indigo-500 via-purple-500 to-pink-500, blur(20px), opacity(0.3)"
  grid_overlay: "subtle 1px grid pattern with linear-gradient masks"
  typing_cursor: "서브헤딩 텍스트에 cursor 애니메이션"
  logo_rotate: "hover 시 180deg 회전"
animation:
  timing: "500ms ease-in-out (nav sticky transition)"
  nav_scroll: "transparent → glass blur transition 500ms"
  hero_input_glow: "multi-color outer glow on hover"
layout: [sticky/absolute nav (pill center), 110vh atmospheric hero (indigo badge + serif 7xl + 대형 input area), floating glass 통합 바, #f8f9fa feature scroll-spy (25% sticky sidebar + 75% main), slate-900 masonry testimonials, centered FAQ accordion]
components:
  nav: "pill 캡슐 bg-white/10 backdrop-blur-md center links, right CTA shadow-[0_0_20px_rgba(255,255,255,0.2)]"
  hero: "110vh dark bg + image gradient overlay, indigo badge, Lora serif 7xl, 대형 white input rounded-2xl + multi-color glow shadow"
  integration_bar: "floating glass max-w-4xl — left: 프레임워크 로고 / right: 통합 아이콘 마퀴"
  feature_spy: "25% sticky nav (dot indicator scroll-spy) + 75% 2col alternating 텍스트/비주얼"
  testimonials: "glass-strong 마소리 그리드, slate-900 bg, quote 14px text-slate-200"
  faq: "light gray #f3f4f6 rounded blocks, chevron rotate, smooth height transition"
special_notes:
  - "Lora (serif) 히어로 헤드라인 + Space Grotesk (display brand) + Inter (body)"
  - "다크(hero/testimonials) ↔ 라이트(features) 섹션 교차"
  - "typing cursor 서브헤딩 필수"
  - "pill nav 중앙 배치"
```
