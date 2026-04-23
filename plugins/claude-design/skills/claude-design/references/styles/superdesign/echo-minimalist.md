# Echo Minimalist
source: superdesign.dev
category: light

```yaml
palette: { bg: "#F2F2F2", primary: "#111111", secondary: "#B6B5B5", muted: "#838282", surface: "#FFFFFF", dark: "#1E1E1E" }
echo_layers: ["#BFBFBF", "#C9C9C9", "#D1D1D1", "#D9D9D9"]
typography: { heading: "Clash Display", body: "Satoshi", weight: "700/500", tracking: "-0.05em", leading: "0.9" }
style_traits: [스위스 미니멀리즘, 타이포그래피 에코 스택, 럭셔리 브루탈리즘, 에디토리얼, 아이콘 없음 순수 기하학]
border: "1px solid rgba(30,30,30,0.1)"
effects:
  echo_stack: "동일 텍스트 5레이어, 각 -0.04em씩 offset, 뒷레이어 #BFBFBF→#D9D9D9 페이드"
  image_reveal: "clip-path: inset, 700ms cubic-bezier(0.77,0,0.175,1)"
  image_hover: "grayscale(0.2)→0, scale(1.05)"
  card_hover: "background transparent→#FFFFFF"
  icon_hover: "rotate(12deg)"
animation:
  nav_link: "color transition 120ms → #B6B5B5"
  cta_pill: "border invert on hover (black↔white)"
layout: [sticky 80px header + backdrop-blur(12px), 70-100vh echo hero, 12-col asymmetric showcase, 3-col philosophy grid, 3-col service cards, dark footer #1E1E1E]
components:
  echo_hero: "11vw 헤딩, 5레이어 에코 스택, 순수 타이포그래피 (이미지 없음)"
  showcase_grid: "8col 사각 + 4col 필 쉐이프 + 5col 원형 + 7col 와이드 혼합"
  pill_showcase: "height 500px, border-radius 9999px, 호버 시 원형 오버레이"
  service_card: "64x64 기하학 아이콘 컨테이너, 호버 12deg 회전, arrow-right CTA"
  footer: "#1E1E1E, 4-col, 상단 5% 흰 border"
```
