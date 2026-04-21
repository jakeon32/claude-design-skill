# Mosaic Grid Architecture Style
source: superdesign.dev
category: light

```yaml
palette: { bg: "#F7F7F5", fg: "#3A3A38", forest: "#1A3C2B", coral: "#FF8C69", mint: "#9EFFBF", gold: "#F4D35E", border: "#3A3A38" }
typography: { heading: "Space Grotesk", body: "General Sans", label: "JetBrains Mono", weight: "Space Grotesk: bold tight-tracking / JetBrains Mono: 10–12px 0.1em tracking", size_hero: "64–96px leading-0.9", tracking: "tracking-tight (heading) / 0.1em (mono labels)" }
style_traits: [Technical Minimalist, SVG 모자이크 배경 격자, 레이저 얇은 hairline 1px 보더, 블루프린트 도면 미학, 벤토 그리드, 플랫 2D 노 섀도우]
radius: "0px 또는 2px (sm) — 절대 이상 금지"
shadow: "없음 — 모든 깊이는 1px 보더로만"
effects:
  mosaic_bg: "전페이지 SVG 모자이크 — 다양한 크기 직사각 패널, 0.5px hairlines #3A3A38 at 0.3 opacity, #F7F7F5 채움, 반복 패턴"
  image_treatment: "기본 mix-blend-luminosity 90% opacity, hover 시 full color 전환"
  corner_markers: "폼 컨테이너 4모서리 L자형 마커 10px×10px in #1A3C2B"
  network_orbit: "원형 SVG — 중앙 16px Forest 노드, 3개 orbiting 노드 dashed path 140px radius, 20s linear infinite 회전"
animation:
  timing: "linear / standard ease-out — snappy"
  image_hover: "grayscale→full color transition"
  network: "20s linear infinite orbit"
layout: [Fixed 1px 하단 보더 네비, 8xl Space Grotesk 히어로 + 와이어프레임 우측 그래픽, 1px gap 벤토 2×2 그리드 (Coral/Mint/Gold left-border 액센트), 640px 폼 컨테이너 (L-shape 코너 마커), 네트워크 SVG 토폴로지 컴포넌트]
components:
  nav: "1px border-bottom, 32px 로고박스 #1A3C2B white icon, center: JetBrains Mono 10px uppercase numbered links, ghost + forest solid CTA"
  hero: "Space Grotesk 8xl tracking-tight forest green, JetBrains Mono 14px all-caps sub, 추상 와이어프레임 우측 (dashed orbit + luminosity image)"
  bento: "2×2 grid 1px #3A3A38 gap, 32px padding, monospace header + colored left-border (Coral/Mint/Gold/Forest), 내부 코드/UI 모형"
  form: "640px 1px border box + 4 L-shape corner markers in #1A3C2B"
  status_badge: "1px border #1A3C2B/20, 8px solid square dot + 10px JetBrains Mono uppercase, 4px 12px padding"
special_notes:
  - "Space Grotesk + JetBrains Mono 조합 — General Sans 보디"
  - "SVG 모자이크 배경 전체 페이지 고정 필수"
  - "그림자 전면 금지 — 1px hairline으로만 구조 표현"
  - "이미지 luminosity blend 기본, hover 시 full color"
```
