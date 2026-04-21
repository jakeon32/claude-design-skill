# Season 04
source: superdesign.dev
category: light

```yaml
palette: { bg: "#E3E2DE", primary: "#1B0E0D", accent: "#C72A09", neon: "#31EF07", highlight: "#61220F", ghost: "#D9D9D9" }
typography: { heading: "Clash Grotesk", body: "General Sans / Mono", weight: "700/400", tracking: "-0.04em", leading: "0.85", size_hero: "13.5vw (desktop) / 16vw (mobile)", transform: "uppercase" }
style_traits: [하이패션 브루탈리즘, 럭셔리 에디토리얼 + 산업적, 네온 그린 마이크로인터랙션, 고대비 그레이스케일 이미지, 오더드 케이오스]
effects:
  noise: "SVG fractalNoise baseFrequency 0.9 numOctaves 3, opacity 0.08, mix-blend-mode: multiply, fixed z-index 50, pointer-events: none"
  image: "grayscale + high-contrast, hover scale(1.05)"
  link_hover: "2px neon green underline, scale 0→1, cubic-bezier(0.165,0.84,0.44,1)"
  nav_blend: "mix-blend-mode: difference, text #E3E2DE (배경 불문 가시성)"
animation:
  underline: "scaleX 0→1, cubic-bezier(0.165,0.84,0.44,1)"
  neon_badge: "hover 시 opacity 0→1, 300ms ease-in-out"
  quick_view: "#31EF07 배지 hover 출현"
layout: [sticky mix-blend-difference 네비, 100vh 다크 히어로(#1B0E0D bg, 60% opacity 이미지, 하단 정렬 CTA), 12-col 매니페스토, 리본형 카테고리 디바이더, 비대칭 상품 그리드, 베이지 멀티컬럼 푸터]
components:
  hero_headline: "Clash Grotesk 13.5vw, 1행 좌정렬 + 2행 20vw indent, leading 0.75, tracking -0.05em, 번트레드+베이지 믹스 컬러"
  manifesto: "12-col: 1-4col 레이블, 5-12col 32-48px 에디토리얼 텍스트, 3rem 인덴트, #61220F 키프레이즈"
  category_divider: "12vw #61220F 헤딩, 상하 border(#D9D9D9), 리본 효과"
  product_grid: "12-col 비대칭 오프셋 (7col 4:5 + 5col 3:4 +128px margin), mono 가격, hover 번트오렌지 border + #31EF07 Quick View 배지"
  neon_badge: "border-radius 0, #31EF07 bg, #1B0E0D 텍스트 10px uppercase bold, hover-only"
  footer: "#1B0E0D 뉴스레터 블록 + #31EF07 Send 버튼, 8vw ghost 브랜드 타이틀 #D9D9D9"
```
