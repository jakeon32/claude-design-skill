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

> 🔴 **모든 차트는 `tools/chart_scale.js`의 `niceScale()` → `valueToPx()`를 거쳐야 한다.**
> 템플릿에 픽셀을 하드코딩하지 마라(옛 `height:240px /* 값에 따라 조정 */`이 눈대중 렌더의 원인이었다).
> 렌더 전 `assertChart()`가 "값 비율 = 픽셀 비율"을 검증한다.

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Bar/Column Chart | [data-layouts.md](data-layouts.md#bar--column-chart) | 70% | 막대 그래프. **Y축 0 시작 필수** |
| Line Chart | [data-layouts.md](data-layouts.md#line-chart) | 70% | 선 그래프, 추이 강조 |
| 100% Stacked Bar | [data-layouts.md](data-layouts.md#100-stacked-bar) | 70% | **부분→전체 구성.** 파이의 대안(권장) |
| Donut Chart | [data-layouts.md](data-layouts.md#donut-chart) | 65% | ⚠️ **조건부 허용** — 항목 ≤3 + 근사 인상만. IBCS "Bottom 1" |
| Funnel | [data-layouts.md](data-layouts.md#funnel) | 65% | 단계별 전환. 폭으로 값 인코딩 |
| Key Metrics | [data-layouts.md](data-layouts.md#key-metrics) | 40% | KPI 숫자 3~4개 강조 |
| 2×2 Matrix | [data-layouts.md](data-layouts.md#2x2-matrix) | 70% | 포지셔닝. **정성 분류 — 축에 눈금 X** |

### F. Table

> 🔴 **2026-07-14 신설.** 그 전까지 표 템플릿이 0개였다.

| 레이아웃 | 파일 | 주요 특징 |
|---------|------|---------|
| 요금표 (행 강조) | [table-layouts.md](table-layouts.md#9-1-요금표-행-강조) | 결론 행 틴트 + 핵심 값만 굵게 |
| 비교표 (열 강조) | [table-layouts.md](table-layouts.md#9-2-비교표-열-강조) | 추천 열 전체 틴트 |
| 스펙표 | [table-layouts.md](table-layouts.md#9-템플릿-3종) | 항목명 + 값. 행 ≥6 시 줄무늬 |

**하드 룰**: 데이터 행 ≤7 / 총 열 ≤6 (ISO 9241-303 역산) · 본문 ≥24px ·
**수직 격자선 금지** · 숫자 우측정렬 + `tabular-nums` · **얼룩말 무늬 기본 OFF**(행≥6 AND 열≥5일 때만)

### G. Diagram

> 🔴 **2026-07-14 신설.** 그 전까지 도해 템플릿이 0개였고, 카탈로그는
> Venn을 "있다"고 등재해놓고 실체가 없었다. AI가 매번 즉흥적으로 그린 원인.

| 레이아웃 | 파일 | 언제 |
|---------|------|------|
| Process Flow | [diagram-layouts.md](diagram-layouts.md#3-1-가로-프로세스-플로우-flow-h) | 순서가 있고 **끝이 있음** |
| Cycle | [diagram-layouts.md](diagram-layouts.md#3-3-사이클-cycle) | 순서가 있고 **시작으로 돌아옴** |
| Hierarchy Tree | [diagram-layouts.md](diagram-layouts.md#3-2-계층-트리-tree) | 위계·소속·분해 |
| Venn (2~3원) | [diagram-layouts.md](diagram-layouts.md#3-4-벤-다이어그램-venn) | **교집합 자체가 결론일 때만.** 4원 이상은 작도 불가 |
| Layer Architecture | [diagram-layouts.md](diagram-layouts.md#3-5-레이어-아키텍처-arch) | 구성요소 + 경계 + 의존 |

**하드 룰**: 노드 4개 기본·5개 상한 · **선 교차 0** · **화살표 = 흐름 / 선 = 연결**(방향 없으면 화살표 금지) ·
강조 노드 정확히 1개 · **SVG 색은 `style=`로**(`fill="var(--x)"`는 Chromium에서 작동 안 함)

### H. Timeline

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Horizontal Timeline | [data-layouts.md](data-layouts.md#horizontal-timeline) | 65~75% | 가로 흐름, 최대 5단계. **정량 차트 아님** |
| Roadmap | _(추후 추가)_ | 65% | 분기 있는 로드맵 |

### I. Mockup

| 레이아웃 | 파일 | Visual% | 주요 특징 |
|---------|------|---------|---------|
| Mobile Mockup (1) | [mockup-layouts.md](mockup-layouts.md#mobile-1) | 70% | 텍스트 좌 + 폰 우 |
| Mobile Mockup (3) | [mockup-layouts.md](mockup-layouts.md#mobile-3) | 80% | 3대 나란히 |
| Mobile + Annotations | [mockup-layouts.md](mockup-layouts.md#mobile-annotated) | 75% | 기기 + 기능 콜아웃 |
| Desktop Mockup | [mockup-layouts.md](mockup-layouts.md#desktop) | 70% | 텍스트 좌 + 맥북 우 |
| Desktop Full | [mockup-layouts.md](mockup-layouts.md#desktop-full) | 85% | 맥북 전체 화면 |

### J. Cards / Features

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

> **0단계 — 밀도부터 정한다.** 레이아웃을 고르기 전에 [`density-rules.md`](../density-rules.md)로
> ① 밀도 등급(D1/D2/D3) 선언 ② 줄 예산 계산 ③ 초과 시 삭제·분할.
> **넘칠 게 확정이면 HTML을 만들지 말고 먼저 쪼갠다.**

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
| **정확한 값 비교 (요금·스펙·지원여부)** | **Table** — 요금표/비교표/스펙표 |
| **단위가 서로 다른 항목 나열** (가격/용량/기간) | **Table** — 차트로는 불가능 |
| **순서가 있고 끝이 있는 절차** | **Process Flow** (도해) |
| **반복·순환하는 과정** | **Cycle** (도해) |
| **위계·소속·분해 구조** | **Hierarchy Tree** (도해) |
| **시스템 구성요소 + 의존** | **Layer Architecture** (도해) |
| **개념 간 겹침 — 교집합이 결론일 때만** | **Venn** (도해, 2~3원. 4원 이상 작도 불가) |
| 항목 간 크기 비교 (6개 이상) | Bar Chart |
| 시간에 따른 추이 | Line Chart |
| **부분 → 전체 구성** | **100% Stacked Bar** (파이보다 권장) |
| 2가지 기준 포지셔닝 | 2×2 Matrix |
| 단계별 줄어드는 흐름 | Funnel |
| 날짜 기반 마일스톤 | Horizontal Timeline |
| 사진 1장 + 설명 | Photo Split |
| 감정/분위기 사진 | Full Bleed Photo |
| 이미지 2~3장 비교 | 2/3-Col Image+Caption |
| 앱 화면 (1개 / 3개) | Mobile Mockup |
| 웹/데스크톱 앱 화면 | Desktop Mockup |
| 팀원 소개 | Team Grid |
| 마무리 + CTA | Closing/CTA |
| **위 어디에도 안 맞음** | **도해·차트를 억지로 만들지 말고 텍스트로 쓴다** |

### 표 vs 차트 (헷갈릴 때)

| 조건 | 선택 |
|---|---|
| 값 자체가 결론 / 단위가 섞임 / 숫자 20개 이하 | **표** |
| 패턴·순위·추이가 결론 / 숫자 25개 이상 | **차트** |

> Tufte: *"표는 20개 이하의 작은 데이터 집합에서 그래픽을 능가한다."*
> 상세 결정표 → [`table-layouts.md` §1](table-layouts.md#1--먼저-이게-표여야-하는가-표-vs-차트)

### 도해를 그리기 전 게이트

1. **구조가 있는가?** (순서·위계·연결·교집합·순환) 없으면 도해는 장식이다
2. **"이 도해를 보면 ___를 알 수 있다"**를 채울 수 있는가? 제목과 같은 말이면 도해 불필요
3. 그 면적이 **텍스트 3줄보다 많은 걸 전달**하는가?

> ⚠️ 도해 템플릿이 생기면 AI는 모든 슬라이드를 도해로 만들려 한다.
> **"해당 없음 → 텍스트"가 정상 출구다.** → [`diagram-layouts.md` §0](diagram-layouts.md#0--최상위-게이트--도해를-그릴-것인가)

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
2. **여백**: 좌우 64px / 상하 40px (안전영역 1152×640)
3. **4px 베이스라인 그리드**: 모든 spacing은 4px 배수 (한글은 8px 배수가 거칠다)
4. **🔴 텍스트 최소 크기 — 밀도 등급이 정한다** (옛 "본문 16px"는 폐기.
   투사 시 ISO 9241-303 최소치 미달이라 뒷줄에서 못 읽는다):

   | 등급 | 용도 | 본문 | **절대 하한** |
   |---|---|---|---|
   | D1 | 투사(발표장) | 32–40px | **32px** |
   | D2 | 화면공유·영상 | 26–32px | **24px** |
   | D3 | 배포 PDF | 18–22px | **16px** |

   → 정본 [`density-rules.md` §4](../density-rules.md)
5. **여백은 개체 크기의 종속 변수다** — 공간이 부족하면 **여백을 깎지 말고 개체를 줄인다.**
   여백을 `em`으로 묶어 개체가 줄면 여백이 자동으로 따라 줄게 한다
   (행간을 "12px"이 아니라 "140%"로 쓰는 것과 같은 원리).
6. **카드/컬럼 height**: CSS Grid 사용 금지 → Flexbox `flex:1 + min-height:0`
7. **색상 사용**: 60/30/10 원칙 — Primary 60%, Secondary 30%, Accent 10%
8. **넘침은 빌드 실패다.** `overflow:hidden`으로 삼키지 않는다 — 검수기가 잡아 exit 1.
   대응 순서: **삭제 → 분할 → 부록 → 열/등급 → 폰트(1단계) → 실패**
