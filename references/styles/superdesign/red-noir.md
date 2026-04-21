# Red Noir
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#000000", surface_grad: "#1a0505→#000000", accent: "#ef233c", accent_glow: "rgba(239,35,60,0.5)", fg: "#ffffff", fg_muted: "#a1a1aa", fg_dim: "#71717a", border: "rgba(255,255,255,0.1)", border_dark: "#27272a" }
typography: { heading: "Manrope", body: "Inter", weight: "200~800 / 300~600", tracking: "-0.05em (heading)", mono_label: "uppercase tracking-wider text-xs font-mono" }
style_traits: [다크 테크 누아르, 레드 액센트 글로우, 글래스모피즘 네비, 별 파티클 배경, 스크롤 페이드업 애니메이션, 스피닝 코닉-그라디언트 버튼]
css_vars: "--accent-red: #ef233c / --accent-red-glow: rgba(239,35,60,0.5)"
selection: "background #ef233c, color #ffffff"
texture:
  bg_gradient: "fixed, from-[#1a0505] to-black (top→down)"
  star_field: "box-shadow 별 패턴 2종 (1px/2px), animStar 50s/80s linear infinite translateY"
  red_sphere: "fixed center, 800×800px, bg-red-600/5, blur(120px)"
  grid_overlay: "40×40px linear-gradient 그리드, rgba(255,255,255,0.03), radial-mask center 40%→80% fade"
  gradient_blur: "fixed top, 120px height, bg linear-gradient to-b black/80→transparent, backdrop-blur(8px), mask-image linear-gradient"
effects:
  shiny_cta: "spinning conic-gradient border — @property --gradient-angle 0→360deg 2.5s linear infinite / border: 2px solid transparent / background: black padding-box + conic-gradient(from var(--gradient-angle), transparent, #ef233c 5%~30%, transparent) border-box / dot-pattern ::before rgba 4px bg-size"
  nav_spin_hover: "inset conic-gradient spin 3s on hover, opacity 0→1 transition"
  card_glow: "absolute inset-0, radial-gradient red at top-right, opacity 0→10% on group-hover"
  pricing_highlight: "border-[#ef233c], shadow-[0_0_30px_rgba(239,35,60,0.1)], scale-105, -top-3 pill badge"
  text_stroke: "-webkit-text-stroke: 1px rgba(255,255,255,0.1), color: transparent (ghost footer text)"
animation:
  fade_in_up: "translateY(20px)→0, opacity 0→1, 0.8s ease-out, staggered delay 0.1s~0.4s"
  anim_star: "translateY(0→-2000px), 50s/80s linear infinite (2종 속도 차이로 parallax)"
  border_spin: "--gradient-angle 0→360deg, 2.5s linear infinite"
  cta_arrow: "group-hover:translate-x-1, transition-transform"
layout: [fixed pill 네비(max-w-5xl, backdrop-blur-xl, bg-black/60, border-white/10, rounded-full), 100vh 중앙정렬 히어로, 통합 브랜드 로고 스트립(border-y white/5, opacity 60%→100%), 4-col 벤토 피처 그리드(lg:h-700px), 풀와이드 #ef233c 테스티모니얼 배너, 3-col 가격표(중앙 scale-105), 이메일 웨이트리스트 CTA, black 푸터]
components:
  nav: "좌: 45deg rotate #ef233c 사각 + Manrope bold 브랜드 / 중: text-zinc-400 링크 / 우: Log In + spinning-border Get Access 버튼"
  hero_badge: "ping 애니메이션 #ef233c dot + Manrope xs 텍스트, rounded-full bg-white/5 border-white/10 backdrop-blur"
  hero_headline: "Manrope semibold tracking-tighter, bg-clip-text gradient white→white/40, 6xl~8xl, accent span #ef233c with SVG underline curve"
  shiny_button: "pill, black bg, spinning conic border #ef233c, dot-pattern ::before, white text + arrow"
  feature_card_main: "lg:col-span-2 row-span-2, from-zinc-900/50 to-black, border-white/10, hover red glow, fade-up 하단 CTA"
  testimonial_banner: "풀와이드 bg-[#ef233c], black text + 5-star, 3xl~5xl Manrope bold quote, avatar circle"
  pricing_pro: "border-[#ef233c], bg-zinc-900/40, scale-105, red glow shadow, -top-3 Recommended badge, #ef233c CTA button"
  footer_ghost: "text-[15vw] Manrope bold, text-stroke (outline only), opacity-20 pointer-events-none"
  footer_label: "text-xs uppercase tracking-widest text-[#ef233c] (섹션 헤더)"
special_notes:
  - "#ef233c 레드가 유일한 액센트 — 파란/보라 등 혼합 금지"
  - "별 파티클 필수 — flat dark 방지"
  - "shiny CTA @property --gradient-angle 사용 (CSS Houdini 필요)"
  - "글래스모피즘 네비 반드시 backdrop-blur-xl 유지"
  - "텍스티모니얼 섹션만 풀 레드 배경 — 강한 대비 포인트"
  - "pricing 중앙 카드 scale-105 + z-10으로 앞으로 튀어나온 느낌"
```
