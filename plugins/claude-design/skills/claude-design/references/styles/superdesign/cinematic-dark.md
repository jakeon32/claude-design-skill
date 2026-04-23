# Cinematic Dark
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#050505", surface: "#111111", primary: "#FFFFFF", secondary: "#999999", accent: "linear-gradient(to right, #06B6D4, #EC4899)", glow: "#7C3AED" }
typography: { heading: "Aspekta", body: "Aspekta", weight: "900/300", size_hero: "12vw", tracking_hero: "tighter", tracking_label: "0.2em", transform: "uppercase" }
style_traits: [시네마틱 다크모드, 3D 공간감, 브루탈리스트+하이테크, 글래스모피즘, mix-blend-difference 네비]
border: "1px solid rgba(255,255,255,0.1)"
effects:
  perspective: "2000px (필수 유지)"
  backdrop_blur: "blur(8px)"
  glass: "background rgba(255,255,255,0.05), backdrop-filter blur(8px)"
  purple_glow: "background #7C3AED, filter blur(100px), centered"
  image_hover: "grayscale(1)→grayscale(0), 0.2s"
animation:
  hero_cube: "rotateX(360deg) infinite, 4-face 3D prism (preserve-3d, perspective 2000px)"
  button_hover: "scale(1.02)"
  nav: "mix-blend-mode: difference (배경색 반전으로 항상 가시성 확보)"
  live_dot: "red-500 pulse (로고 옆 라이브 상태 표시)"
layout: [fixed mix-blend-difference 헤더, 100vh 3D 롤로덱스 히어로, 90rem 케이스스터디 그리드, #0B0216 pricing section, 에디토리얼 풋터]
components:
  hero_cube: "50vh×50vh 4-face 프리즘, 각 face rotateX 90deg + translateZ 30vh, 이미지+uppercase 타이틀"
  case_grid: "풀와이드 피처드(aspect-video)+2col 서브, macOS 트래픽라이트 dot, grayscale→color"
  pricing: "3-tier 카드, 중앙 Growth 카드 scale(1.05) white bg, 사이드 glassmorphism"
  calculator: "#1A0B2E container, 커스텀 range 슬라이더, thumb 24px + #7C3AED 글로우 링"
special_notes:
  - "그림자 사용 금지 — border-white/10 + backdrop-blur로만 깊이 표현"
  - "헤딩 전체 uppercase 필수"
  - "perspective: 2000px 히어로 컨테이너 필수"
```
