# Tectonic Stone
source: superdesign.dev
category: dark

```yaml
palette: { obsidian: "#050505", basalt: "#1A1C1E", granite: "#2D3033", magma: "#FF4800", gold: "#D4AF37", ash: "#E0E0E0" }
typography: { heading: "Cormorant Garamond / Cinzel", body: "Inter / Space Grotesk", weight: "700/400" }
style_traits: [디지털 지질학, 흑요석 미니멀리즘, 고대-미래주의, 단단하고 무거운 물질감, 용암 글로우 액센트]
radius: "0px (rounded-none 기본, 곡선 절대 금지)"
shadow: "20px 20px 40px rgba(0,0,0,0.8) (무거운 물질감)"
text_effect: "etched — text-shadow: 1px 1px 0 rgba(255,255,255,0.1), -1px -1px 0 rgba(0,0,0,0.5)"
texture:
  grain: "stony noise filter 12% opacity (모든 배경)"
  pattern: "반복 수직 육각형 (basalt 기둥 패턴)"
  fault_line: "SVG path 불규칙 균열선, stroke ash-white 20% opacity"
  topo: "지형 등고선 overlay, magma-glow 5% opacity"
effects:
  card_cut: "clip-path 45도 챔퍼 (우상단 모서리)"
  card_border: "top + left만 1px solid ash-white 10% (상단광 표현)"
  magma_button: "기본 obsidian + 2px magma border → hover inset glow rgba(255,72,0,0.4) → click 순간 brightening"
  headline_gradient: "linear-gradient (상단 어둡게→하단 밝게) — 조각 깊이 표현"
  mineral_mask: "background-clip: text + 흑요석/대리석 사진 → 대형 타이포에 광물 텍스처"
animation:
  thud: "drop + 화면 미세 쉐이크 (camera-shake) — fade 금지"
  parallax: "섹션별 다른 스크롤 속도 (지각판 이동)"
  pulse: "slow deep-orange pulse on 버튼/상태 표시기 (냉각 용암)"
  timing: "duration-700, cubic-bezier(0.22,1,0.36,1) (무거운 움직임)"
layout: [겹치는 플레이트 레이아웃, SVG 균열선 섹션 구분, 50vh 단일 granite 블록 푸터]
components:
  monolith_card: "basalt bg, 20px 40px 그림자, 45도 챔퍼 우상단, top+left border only"
  magma_button: "obsidian bg + 2px magma border, hover 내부 발열 glow, click 순간 용해 brightening"
  fault_divider: "hr 대신 SVG 불규칙 균열 path, ash-white 20%"
  footer: "50vh 단일 granite 블록, 최소화된 tiny 흰 텍스트"
special_notes:
  - "border-radius 0 전체 — 45도 챔퍼만 허용"
  - "부드러운 현대 그라데이션 금지 — 거친 노이즈 텍스처만"
  - "빠른 통통 튀는 애니메이션 금지 — 질량감 있는 무거운 움직임만"
  - "투명도/유리 효과 금지 — 불투명 솔리드만"
```
