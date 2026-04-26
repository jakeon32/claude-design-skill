---
name: slide-layouts-index
description: "슬라이드 레이아웃 정의 카탈로그 — 커버/텍스트/비주얼/데이터/목업 등 30+ 레이아웃 유형. 각 레이아웃의 구조 원칙, 비율, HTML 템플릿 포함. style 라이브러리와 직교(orthogonal): 어떤 스타일에도 조합 가능."
---

# Slide Layout Library

## 개념

슬라이드 레이아웃 = **어디에 무엇을 놓는가**의 구조적 틀.  
스타일(색상·폰트·분위기)과 독립적으로 정의된다.

```
레이아웃 × 스타일 = 결과물

Photo Split + corporate-trust = 깔끔한 기업 발표
Photo Split + cyberpunk       = 사이버펑크 기술 덱
Photo Split + minimal-white   = 미니멀 포트폴리오
```

모든 템플릿은 `1280×720px` 캔버스 기준. CSS 변수(`--primary`, `--bg`, `--text` 등)는 DESIGN_SYSTEM에서 주입.

---

## 레이아웃 카탈로그

### A. Cover / Title

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Title/Cover | [cover-layouts.md](cover-layouts.md#titlecover) | 80~90% | 덱 첫 장, 8가지 변형 — 레이아웃×비율×경계표현 3축 조합 (A~H) |
| Section Title | [cover-layouts.md](cover-layouts.md#section-title) | 30~40% | 섹션 구분, H1 단독 중앙 |

### B. Text Layouts

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Highlight | [text-layouts.md](text-layouts.md#highlight) | 40% | H2 좌 + 본문 우 2컬럼 |
| Simple List | [text-layouts.md](text-layouts.md#simple-list) | 50% | H2 좌 + 세로 리스트 우 (3~4항목) |
| 2×2 Grid | [text-layouts.md](text-layouts.md#2x2-grid) | 50% | 제목 + 4개 텍스트 그리드 |
| 3-Column Text | [text-layouts.md](text-layouts.md#3-column-text) | 55% | 상단 제목 + 3열 |
| 4-Column Text | [text-layouts.md](text-layouts.md#4-column-text) | 55% | 상단 제목 + 4열 |
| Numbered List | [text-layouts.md](text-layouts.md#numbered-list) | 50% | 번호 강조 + 리스트 우측 |
| Asymmetric | [text-layouts.md](text-layouts.md#asymmetric) | 60% | 큰 텍스트 블록 좌 + 2×2 우 |

### C. Visual / Photo

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Photo Split | [visual-layouts.md](visual-layouts.md#photo-split) | 60~70% | 텍스트 패널 + 이미지 패널 (3변형) |
| Full Bleed Photo | [visual-layouts.md](visual-layouts.md#full-bleed-photo) | 75%+ | 전체화면 이미지 + 오버레이 텍스트 |
| 2-Col Image+Caption | [visual-layouts.md](visual-layouts.md#2col-image-caption) | 70% | 이미지 2개 + 각 캡션 |
| 3-Col Image+Caption | [visual-layouts.md](visual-layouts.md#3col-image-caption) | 70% | 이미지 3개 + 각 캡션 |

### D. Statement / Quote

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Centered Statement | [statement-layouts.md](statement-layouts.md#centered-statement) | 30% | 핵심 메시지 1개 중앙 |
| Big Number | [statement-layouts.md](statement-layouts.md#big-number) | 35% | 대형 숫자 + 설명 |
| Quote | [statement-layouts.md](statement-layouts.md#quote) | 60~70% | 큰 따옴표 + 배경 이미지 |

### E. Data / Chart

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Bar/Column Chart | [data-layouts.md](data-layouts.md#bar-column-chart) | 70% | 막대 그래프 크게, 설명 최소 |
| Line Chart | [data-layouts.md](data-layouts.md#line-chart) | 70% | 선 그래프, 추이 강조 |
| Pie/Donut Chart | [data-layouts.md](data-layouts.md#pie-donut) | 65% | 비율 표현 (5항목 이하) |
| Scatter Plot | [data-layouts.md](data-layouts.md#scatter-plot) | 70% | 산점도, 좌측 설명 |
| Venn Diagram | [data-layouts.md](data-layouts.md#venn-diagram) | 65% | 교집합 비교 |
| Funnel | [data-layouts.md](data-layouts.md#funnel) | 65% | 퍼널/단계 흐름 |
| Key Metrics | [data-layouts.md](data-layouts.md#key-metrics) | 40% | KPI 숫자 3~4개 강조 |
| 2×2 Matrix | [data-layouts.md](data-layouts.md#2x2-matrix) | 70% | 포지셔닝 매트릭스 |

### F. Timeline

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Horizontal Timeline | [data-layouts.md](data-layouts.md#horizontal-timeline) | 65~75% | 가로 흐름, 최대 5단계 |
| Roadmap | _(추후 추가)_ | 65% | 분기 있는 로드맵 |

### G. Mockup

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Mobile Mockup (1) | [mockup-layouts.md](mockup-layouts.md#mobile-1) | 70% | 텍스트 좌 + 폰 우 |
| Mobile Mockup (3) | [mockup-layouts.md](mockup-layouts.md#mobile-3) | 80% | 3대 나란히 |
| Mobile + Annotations | [mockup-layouts.md](mockup-layouts.md#mobile-annotated) | 75% | 기기 + 기능 콜아웃 |
| Desktop Mockup | [mockup-layouts.md](mockup-layouts.md#desktop) | 70% | 텍스트 좌 + 맥북 우 |
| Desktop Full | [mockup-layouts.md](mockup-layouts.md#desktop-full) | 85% | 맥북 전체 화면 |

### H. Cards / Features

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Feature Highlight | [card-layouts.md](card-layouts.md#feature-highlight) | 40% | 핵심 기능 1개 중앙 |
| Feature Cards 2-col | [card-layouts.md](card-layouts.md#feature-2col) | 55% | 2종 와이드 카드 |
| Feature Cards 3-col | [card-layouts.md](card-layouts.md#feature-3col) | 55% | 3종 카드 |
| Feature Cards 4-col | [card-layouts.md](card-layouts.md#feature-4col) | 55% | 4종 카드 |
| Team Grid | [card-layouts.md](card-layouts.md#team-grid) | 60% | 팀원 사진 + 이름 그리드 |
| Closing/CTA | [card-layouts.md](card-layouts.md#closing-cta) | 75%+ | 마무리, 강렬한 CTA |

---

## 레이아웃 선택 기준

콘텐츠 유형으로 레이아웃을 결정한다:

| 전달하려는 것 | 레이아웃 |
|-------------|---------|
| 덱 제목 + 슬로건 | Title/Cover |
| 새 섹션 시작 | Section Title |
| 텍스트 핵심 메시지 1개 | Highlight |
| 임팩트 있는 숫자/지표 1개 | Big Number / Centered Statement |
| 고객 인용 1개 | Quote |
| 리스트 3~4개 항목, 설명 있음 | Simple List |
| 4개 항목, 각 설명 필요 | 2×2 Grid |
| 3개 원칙/가치 | 3-Column Text |
| 핵심 KPI/지표 3개 | Key Metrics |
| 사진 1장 + 설명 | Photo Split |
| 감정/분위기 사진 | Full Bleed Photo |
| 이미지 2~3장 비교 | 2/3-Col Image+Caption |
| 개념 간 겹침/관계 | Venn Diagram |
| 2가지 기준 포지셔닝 | 2×2 Matrix |
| 단계별 줄어드는 흐름 | Funnel |
| 날짜 기반 마일스톤 | Horizontal Timeline |
| 앱 화면 (1개) | Mobile Mockup (1) |
| 앱 화면 (3개) | Mobile Mockup (3) |
| 앱 기능 콜아웃 | Mobile + Annotations |
| 웹/데스크톱 앱 화면 | Desktop Mockup |
| 팀원 소개 | Team Grid |
| 마무리 + CTA | Closing/CTA |

---

## 공통 CSS 변수 (모든 템플릿 공유)

```css
/* DESIGN_SYSTEM에서 주입되는 변수 */
:root {
  --primary:   /* DESIGN_SYSTEM.colors.primary */;
  --secondary: /* DESIGN_SYSTEM.colors.secondary */;
  --accent:    /* DESIGN_SYSTEM.colors.accent */;
  --bg:        /* DESIGN_SYSTEM.colors.background */;
  --surface:   /* DESIGN_SYSTEM.colors.surface */;
  --text:      /* DESIGN_SYSTEM.colors.text */;
  --muted:     /* DESIGN_SYSTEM.colors.text_muted */;
  --border:    /* DESIGN_SYSTEM.colors.border */;
  --h-font:    /* DESIGN_SYSTEM.typography.heading_font */;
  --b-font:    /* DESIGN_SYSTEM.typography.body_font */;
  --radius:    /* DESIGN_SYSTEM.radius */;
  --shadow:    /* DESIGN_SYSTEM.shadow */;
}
```

---

## 베리에이션 스펙

레이아웃 유형이 결정된 후, **3축 변수**를 추가로 결정해 다양한 표현을 만든다.

| 파일 | 내용 |
|------|------|
| [layout-variation-spec.md](layout-variation-spec.md) | Expression × Proportion × Padding 3축 정의 + 구조 패턴별 유효 조합 매트릭스 |
| [variations.md](variations.md) | 그리드×컴포넌트 조합 카탈로그 + 발표 유형별 추천 시퀀스 |

---

## 공통 구조 규칙

1. **캔버스**: 모든 슬라이드 `1280×720px` 고정
2. **여백**: 가장자리 최소 `60~80px` (슬라이드 전체의 8~12%)
3. **8px 그리드**: 모든 spacing은 8px 배수
4. **텍스트 최소 크기**: 본문 16px, 제목 40px
5. **카드/컬럼 height**: CSS Grid 사용 금지 → Flexbox `flex:1 + min-height:0`
6. **색상 사용**: 60/30/10 원칙 — Primary 60%, Secondary 30%, Accent 10%
