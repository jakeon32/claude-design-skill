# Architectural Blueprint
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#003366", lines: "rgba(255,255,255,0.8)", accent: "#FF3333", measure: "#00FFFF", surface: "transparent" }
typography: { heading: "Architects Daughter / Roboto Mono", body: "Roboto Mono", weight: "400/700", style_heading: "Block Caps", label: "tiny monospaced + serial number prefix (e.g. A-01)" }
style_traits: [사이아노타입 청사진, 기술 도면 미학, 진행 중인 작업, 와이어프레임 투명성, 정밀 그리드 정렬]
texture:
  grid: "CSS background 20px 반복 격자, rgba(255,255,255,0.1)"
  paper: "vellum/blueprint grain overlay — 파란 배경에 깊이 부여"
effects:
  dimension_lines: "요소 너비/높이 표시 화살표 라인 (e.g. <--- 1200px --->), #00FFFF"
  coordinate_labels: "x:140 y:220 포맷, 요소 모서리에 표시"
  redline_notes: "손글씨 주석, 오류 원형 표시, 여백 코멘트 (#FF3333)"
  crosshair_corners: "카드 4모서리 십자선 마커 (흰 선)"
  wireframe: "solid fill 없음 — 투명 레이어, 뼈대만 visible"
animation:
  draw_reveal: "SVG stroke-dashoffset 0→full, 선이 그려지듯 섹션 등장"
  cursor_crosshair: "마우스 따라다니는 십자선 + 실시간 X/Y 좌표 표시 (#00FFFF)"
layout: [10px/50px 마스터 그리드 (모든 요소 교차점 정렬), 청사진 스타일 섹션 구분, 기술 도면형 헤더]
components:
  card: "흰 thin outline, 4모서리 십자선 교차점, 투명 배경, 내부 레이어 visible"
  button: "기술 스탬프 형태, 'APPROVED' 박스 스타일, #FF3333 CTA"
  divider: "dimension arrow 라인 (<--- 1200px --->), #00FFFF"
  label: "serial number + monospaced text (A-01: Component Name)"
special_notes:
  - "모든 요소 solid fill 금지 — 투명 wireframe only"
  - "20px CSS 그리드 항상 visible (배경 레이어)"
  - "stroke-dashoffset 애니메이션으로 '실시간 드로잉' 느낌 필수"
  - "cursor 십자선 좌표 표시 — 기술 분석 무드 강화"
```
