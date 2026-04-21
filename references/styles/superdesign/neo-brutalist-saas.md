# Neo-Brutalist SaaS
source: superdesign.dev
category: light

```yaml
palette: { bg: "#ffe17c", charcoal: "#171e19", sage: "#b7c6c2", white: "#ffffff", black: "#000000" }
typography: { heading: "Cabinet Grotesk", body: "Satoshi", weight: "800/500", tracking_heading: "tighter" }
style_traits: [Neo-Brutalism SaaS, 고대비 블랙 보더, 하드 오프셋 섀도우, 기하학 타이포, 전문적 자신감+플레이풀]
border: "2px solid #000000 (모든 카드/버튼/섹션 필수)"
shadow:
  standard: "box-shadow: 4px 4px 0px 0px #000000 (no blur)"
  large: "box-shadow: 8px 8px 0px 0px #000000 (대형 컨테이너)"
  hero_mockup: "box-shadow: 12px 12px 0px 0px #000000"
radius: "0.75rem (버튼), 3xl (카드) — 버튼 12px 초과 라운드 금지"
texture:
  dot_pattern: "32×32px radial dot, opacity 10%, #ffe17c 배경에만 적용"
effects:
  outline_text: "-webkit-text-stroke: 2px black, color: transparent (히어로 키워드)"
  image_grayscale: "hover시 컬러 reveal"
animation:
  button_hover: "transform: translate(4px, 4px), box-shadow: 4px→0px (press 시뮬레이션), 0.2s cubic-bezier(0.175,0.885,0.32,1.275)"
  marquee: "linear infinite, slow pace"
layout: [고정 h-20 네비(#ffe17c bg, border-b-2 black), 2-col 히어로(#ffe17c + dot pattern), 전폭 마키(#171e19), 화이트 Problem/Solution 2-col, 3-col 피처 그리드(#ffe17c), 다크 How It Works(#171e19), 화이트 3-col 페르소나 벤토, #b7c6c2 테스티모니얼, #ffe17c CTA, #171e19 풋터]
components:
  nav: "#ffe17c bg, 좌: 10×10 블랙 박스(#ffe17c bolt 아이콘), 중: Satoshi bold 링크, 우: Start Free Trial(black bg, white text, 2px border, hard shadow)"
  hero: "좌: 'NEW: AI Content Assistant 2.0' pill 배지(white, 2px border) + 8xl Cabinet Grotesk + CTA 그룹 / 우: browser mockup(white, 2px border, 12px shadow)"
  browser_mockup: "white bg, 2px solid black, border-radius 1rem, 12px hard shadow / 헤더바: black bg + 3-dot(#ff5f57/#febc2e/#28c840) / 내용: sage+charcoal 내부 카드 그리드"
  marquee_bar: "#171e19 bg, border-b-2 black, Cabinet Grotesk #b7c6c2 50% opacity 브랜드명"
  problem_solution: "Card A: #f4f4f5, dashed gray border, 70% opacity / Card B: #ffe17c, 2px solid black, 8px shadow"
  feature_card: "white, 2px border, 4px shadow / 상단 16×16 icon box: #b7c6c2→#ffe17c on hover"
  how_it_works: "#171e19, 3-step 수평 흐름, 24×24 circle + 4px colored glow border(sage/yellow/white), #272727 연결선"
  persona_bento: "Card1: #b7c6c2 / Card2: #ffe17c + 8px shadow / Card3: #272727 + white text, 상단 white pill 배지"
  testimonial_card: "asymmetric radius — top-right + bottom-left: 3xl / top-left + bottom-right: 2px, 5-star #ffbc2e"
  push_button: "bg #000, color #fff, 2px border, border-radius 0.75rem, 8px hard shadow → hover: translate(4px,4px) + shadow→4px"
  social_icon: "10×10 square #272727, light gray border → hover: yellow bg + black border"
special_notes:
  - "모든 인터랙티브 요소 border-width 2px 필수"
  - "브랜드 섹션 hex값 #ffe17c/#171e19/#b7c6c2만 사용"
  - "모든 섀도우 blur 0 필수"
  - "그라데이션/소프트 섀도우 금지"
  - "버튼 radius 12px 초과 금지"
```
