# Poster Modernist
source: superdesign.dev
category: light

```yaml
palette: { bg: "#E3E2DE", primary: "#141414", accent: "#1351AA", body: "#444343", muted: "#7A7A7A", border: "#C7C7C7" }
typography:
  heading: "General Sans / Aileron"
  body: "General Sans / Aileron"
  weight: "900/400"
  hero: { size: "8rem~12rem", weight: 900, leading: 0.85, tracking: "-0.04em", transform: "uppercase" }
  section: { size: "5rem~7rem", weight: 700, leading: 0.9, tracking: "-0.03em" }
  label: { size: "0.75rem", weight: 700, transform: "uppercase", tracking: "0.2em", color: "#7A7A7A" }
style_traits: [포스터 모더니즘, 리얼리티 퍼스트, 플랫 컬러 no-shadow, 레이블 사이드바 그리드, 기술적 권위감]
radius: "0px (전체 — 곡선 절대 금지)"
border: "1px solid #C7C7C7 (섹션 구분)"
shadow: "없음 — flat 색상 블록으로 깊이 표현"
animation: "0.3s linear (color 전환), no bouncy easing"
grid:
  columns: 12
  sidebar: "col 1-3 (레이블/메타데이터/스티키 사이드바)"
  content: "col 4-12 (메인 콘텐츠)"
layout: [sticky 80px cream 네비(col1-3 로고, col10-12 링크), 85vh 히어로(사이드바 매니페스토 + 9xl 헤딩 cobalt 키워드), SYSTEM 피처 그리드(3-col 셀 border+index), WHY DIFFERENT 비교 리스트(100-150px 아이템), ACCESS 섹션]
components:
  hero: "6xl~9xl 헤딩, 핵심 단어 #1351AA span, 하단 2-col(400px 문단 + CTA 클러스터)"
  feature_cell: "1px border, mono 인덱스(01/02/03), bold h3, hover bg-white/20"
  comparison_item: "100-150px 높이, 1px top border, mono 인덱스 + 5xl bold 타이틀, hover→#1351AA"
  poster_button: "border-radius 0, 16px 32px padding, 14px bold uppercase tracking-wider / primary: #1351AA bg / secondary: #141414 bg, hover→#141414 0.3s linear"
  sidebar_label: "sticky top-32, 12px bold #7A7A7A uppercase tracking-0.2em, col 1-3 고정"
  cta_cluster: "solid blue 직사각 버튼 + 밑줄 텍스트 링크 조합"
special_notes:
  - "border-radius 0px 전체 — 둥글기 금지"
  - "그림자/그라데이션 일체 금지 — flat only"
  - "0.3s linear 애니메이션만 — 유기적 easing 금지"
  - "12-col 그리드 엄격 준수 — 사이드바 3col 항상 레이블/메타"
```
