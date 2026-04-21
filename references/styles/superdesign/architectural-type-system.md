# Architectural Type System
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#000000", fg: "#FFFFFF", accent: "#6366f1" }
typography:
  heading: "Inter Tight"
  body: "Inter"
  mono: "JetBrains Mono"
  heading_spec: { weight: 900, tracking: "-0.06em", transform: "uppercase" }
  mono_spec: { weight: 500, tracking: "0.2em~0.4em", size: "8px~11px" }
  body_spec: { weight: "300~400" }
style_traits: [스위스 브루탈리즘 + IDE, 순수 흑백 + 인디고 액센트, 그리드 매트릭스 철학, 헤어라인 보더, 타이포가 유일한 비주얼 언어]
border: "0.5px, color: rgba(255,255,255,0.15) — 개별 면 적용으로 이중선 방지"
radius: "0px (pill 버튼 제외)"
shadow: "없음 — 선과 대비만으로 깊이 표현"
texture:
  noise: "SVG fractal noise, opacity 0.05, 전체 인터페이스 레이어"
effects:
  hover: "300ms transition, black/white 스왑 또는 #6366f1 전환"
  accent_rule: "인디고 #6366f1 — 주요 액션 1개 또는 특정 데이터포인트에만"
animation:
  geo_card_rotate: "45deg→90deg on parent hover, 700ms cubic-bezier(0.4,0,0.2,1)"
layout: [72px 네비(bg-black/80 backdrop-blur, 0.5px bottom border), 2×2 그리드 히어로(각 셀 0.5px hairline), 4-col 커맨드 바, 3-col 벤토 피처 그리드]
components:
  nav: "좌: Inter Tight 900 uppercase 브랜드 + 6px white dot + JetBrains Mono 버저닝(BETA_V.01) / 우: 40px circular hairline 소셜 아이콘 + pill GET ACCESS 버튼(10px mono bold)"
  hero_grid: "2×2 viewport fill, 각 셀 0.5px hairline 분리, 대형 단어 분절(e.g. SU/PER/DE/SIGN), Inter Tight 900, clamp(5rem,18vw,24vw), 셀 좌하단/좌상단 정렬 + 오버플로우 허용"
  command_bar: "4-col: [이메일 input(mono placeholder, 보더 없음)] [JOIN btn white bg/black text tracking-0.3em] [카운트다운 24px mono HH:MM:SS] [3-line 시스템 레이블 8px mono tracking-0.4em]"
  bento_card: "400px, 0.5px hairline 분리, 좌상단 SYSTEM_01 mono 태그, 중앙 아이콘 opacity 20%→100% hover, 좌하단 Inter Tight 900 24px 타이틀"
  countdown: "JetBrains Mono, HH:MM:SS 포맷, ':' 구분자 opacity 20%, 고정폭(jitter 방지), white 24px"
  hairline: "border-width 0.5px, rgba(255,255,255,0.15), 단면 적용(hairline-b/hairline-r)"
  geo_card: "0.5px hairline 정사각 컨테이너, 내부 45deg 회전 정사각(hairline) → hover 90deg, 700ms"
special_notes:
  - "인디고 #6366f1 단 하나의 주요 액션/데이터에만 — 남발 금지"
  - "mono 레이블은 언더스코어 사용 필수 (NO_CREDIT_CARD, FREE_ACCESS)"
  - "텍스트 그리드 셀 엣지에 밀착 정렬 — 건축적 느낌"
  - "그리드 셀/인풋 라운드 코너 금지"
  - "섀도우/그라데이션 금지 — 선과 대비만으로 깊이"
```
