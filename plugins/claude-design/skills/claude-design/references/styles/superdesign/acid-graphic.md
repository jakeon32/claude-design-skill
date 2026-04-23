# Acid Graphic
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#000000", surface: "#0A0A0A", acid: "#CCFF00", pink: "#FF00FF", cyan: "#00F0FF", chrome: "linear-gradient(#FFFFFF, #888888, #E0E0E0)" }
typography: { heading: "Syne Extra Bold / Clash Display", body: "Plus Jakarta Sans / Space Grotesk", weight: "900/400", size: "7xl~12rem", tracking: "-0.05em", transform: "uppercase", distortion: "scaleX(1.5) 또는 italic 극단 변형" }
style_traits: [액시드 그래픽, 리퀴드 크롬, 테크노 서리얼리즘, 디지털 사이키델리아, 언더그라운드 럭셔리 2099]
effects:
  chrome_filter: "backdrop-filter: contrast(200%) brightness(150%) + silver gradient"
  chromatic_aberration: "text-shadow: 1px 0 red, -1px 0 blue (RGB 분리 글리치)"
  grain: "high-contrast noise 5-10% opacity"
  iridescent_border: "2px gradient border from #CCFF00 via #FFFFFF to #FF00FF"
  warped_image: "filter: url(#wavy) — 수중/녹아내림 왜곡"
  outline_text: "color transparent, -webkit-text-stroke 1px #CCFF00 (acid green 윤곽)"
animation:
  liquid_drift: "chrome blob 요소들 20s float 무한 drift"
  glitch_hover: "아이콘 hover → RGB 채널 분리 flickering"
  breathe: "SVG filter 리플링 border (진동 호흡)"
  timing: "cubic-bezier(0.19,1,0.22,1) expo-out (고에너지 스냅)"
layout: [최상단+최하단 acid 마키 (데이터 오버로드), 비대칭 혼돈 레이아웃 (오버랩 허용), blob 컨테이너, chrome 버튼]
components:
  blob_card: "bg-black/40, backdrop-blur-3xl, border 2px iridescent gradient, border-radius 20%_80%_30%_70%/50%_20%_80%_50% (아메바 형태)"
  chrome_button: "bg-gradient-to-b from-white via-gray-400 to-white (금속 실린더), hover scale(1.1)+rotate(2deg)+shadow 0 0 30px #CCFF00/60%, text mix-blend-difference"
  acid_marquee: "animate-marquee, 상하단 2개 동시, 끊임없는 모션+데이터 과부하 느낌"
  thorn_accent: "SVG spike/star 형태 불릿/모서리 장식"
  vertical_nav: "수평 이동 네비, 텍스트 세로 방향 유지"
special_notes:
  - "표준 안전 간격 금지 — 요소 오버랩 권장"
  - "부드러운 자연 그림자 금지 — 네온 글로우/금속 반사만"
  - "중앙 균형 레이아웃 금지 — 무겁고 비대칭+혼돈"
  - "헤딩 극단 왜곡(scaleX 150%, italic) — 가독성 경계까지"
```
