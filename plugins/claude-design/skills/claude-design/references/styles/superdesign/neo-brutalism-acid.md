# Neo-Brutalism Acid Style
source: superdesign.dev
category: light

```yaml
palette: { bg: "#F8F4E8", fg: "#09090B", acid: "#D2E823", border: "#09090B" }
typography: { heading: "Dela Gothic One", body: "Space Grotesk", weight: "Dela Gothic One: all-caps tracking-tighter / Space Grotesk: 400–700", size_hero: "8rem leading-0.85", tracking: "tighter (heading) / normal (body)" }
style_traits: [Neo-Brutalism Acid, 고대비 hard shadow 4px offset, paper-like 배경, 글리치 텍스트 호버, 스티커 배지, mix-blend-difference 커서]
radius: "max 32px — 박스 브루탈 무결성 유지"
shadow: "hard shadow — box-shadow: 4px 4px 0px 0px #09090B (no blur)"
effects:
  hard_shadow: "4px/8px solid offset 그림자, 0 blur — 클릭 시 translate(2px,2px) + shadow 제거로 물리 누름 표현"
  noise_overlay: "SVG 노이즈 3% opacity 전역"
  glitch_text: "Dela Gothic One 호버 — 5 keyframe ±2px translation, 0.3s infinite"
  cursor: "32px circle, bg-white, mix-blend-mode: difference, 링크 호버 시 2.5x scale"
  bento_radial: "소형 카드 radial dot 패턴 1px dots 20px 간격 텍스처"
animation:
  timing: "standard ease-out"
  glitch: "±2px rapid translation on hover"
  marquee: "linear 20s highlights"
  floating: "y-axis ±10px 액센트 카드"
layout: [16px margin 스티키 네비 (backdrop-blur 24px, #F8F4E8/90, 2px border, 12px radius, #D2E823 hover), 12컬럼 히어로 (7col 글리치 헤드라인 + 스티커 배지 / 5col 이미지 카드 + 8px hard-shadow 플로팅), 벤토 카테고리 그리드 (다크 2×2 + 도트 텍스처), 가로 스크롤 'NEW DROPS' 섹션 (320px 카드), #09090B 푸터]
components:
  nav: "#F8F4E8/90, 2px border, 12px radius, Dela Gothic One 로고, #D2E823 hover 버튼"
  hero: "8rem Dela Gothic One uppercase glitch-hover, 스티커 배지 (-2deg rotate, #D2E823), 8px hard-shadow float 카드"
  hard_shadow_btn: "#09090B bg, #D2E823 text, 4px shadow, hover: translate+shadow 제거, active: 4px translate"
  bento: "2col 큰 카드 (#09090B + image 40% mix-blend-overlay) + 2col 소형 (dot 패턴 텍스처)"
  product_cards: "320px, 2px border, 8px shadow, Sold Out: grayscale 60% opacity"
  footer: "#09090B bg, inverted text, mono labels, #D2E823 submit 버튼"
special_notes:
  - "Dela Gothic One + Space Grotesk 조합"
  - "2px solid border 모든 인터랙티브 요소 필수"
  - "그림자 blur 금지 — solid offset만"
  - "#D2E823 Acid 유지 — primary accent"
  - "32px 초과 rounded corners 금지"
```
