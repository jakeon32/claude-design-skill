# Korean Typography & Localization Layer
applies: 한국어 콘텐츠 또는 한국 시장 대상 디자인 시 항상 적용

> ## 🔴 2026-07-14 — 웹 기준 스케일 전면 폐기
>
> 이 문서에 있던 **웹 문서용 크기 스케일(Body 16~18px, line-height 1.65~1.8,
> 본문 18~24자)을 전부 삭제**했다. 이유:
>
> - **Body 16~18px는 투사 시 ISO 9241-303 최소 글자 크기(16 arcmin)에 미달**한다.
>   뒷줄에서 읽히지 않는다. 이 문서가 "한국어면 항상 적용"으로 트리거되므로,
>   **한글 슬라이드가 자동으로 못 읽는 크기로 생성되고 있었다.**
> - line-height 1.65~1.8은 슬라이드의 유한한 줄 예산을 낭비한다.
> - "본문 18~24자"는 근거 없이 좁게 잡은 값이었다 (실제 한글 최적은 20~40자).
>
> **이 문서는 이제 슬라이드 기준만 말한다.**
> 크기·줄수·여백의 정본은 [`density-rules.md`](density-rules.md) (밀도 등급 D1/D2/D3).
> 이 문서는 **폰트 스택 · 자간 · 한글 조판 규칙**만 담당한다.
> 같은 값을 두 문서가 다르게 말하면 규격은 조용히 이탈한다. **정본은 하나여야 한다.**

---

## 핵심 규칙

원래 스타일의 미학(레이아웃 구조, 컬러 로직, hierarchy)은 유지하되,
**타이포그래피와 스페이싱만 아래 규칙으로 재조정**.

### 폰트 스택 (우선순위) — ✅ 이 문서가 정본
```
Heading:  "Pretendard", "SUITE", system-ui, sans-serif
Body/UI:  "Pretendard", "Noto Sans KR", system-ui, sans-serif
```
- 스타일 원본의 영문 폰트(Inter, Outfit, Plus Jakarta Sans 등)는 영문 전용으로 유지 가능
- 한글이 포함되는 모든 텍스트는 Pretendard 우선 적용
- **표에 숫자가 있으면 `tnum`(tabular figures) 지원 폰트만**: Pretendard · Inter · Arial.
  미지원 폰트에서는 `font-variant-numeric: tabular-nums`가 **조용히 무시**되어 자릿수 정렬이 깨진다
  (→ [`table-layouts.md`](slide-layouts/table-layouts.md))

### 크기 — 정본은 density-rules.md. 여기 중복 기재하지 않는다.

| 밀도 등급 | 용도 | 본문 | **절대 하한** |
|---|---|---|---|
| **D1** | 투사(발표장) | 32–40px | **32px** |
| **D2** | 화면공유·영상 | 26–32px | **24px** |
| **D3** | 배포 PDF(혼자 읽음) | 18–22px | **16px** |

제목·각주·항목수 등 나머지 수치는 [`density-rules.md` §4](density-rules.md)를 볼 것.

### 🔴 폰트 웨이트 — 한글은 영문보다 덜 써야 한다 (실측)

**영문처럼 웨이트를 올리면 한글은 뭉친다.** 이유를 측정했다(`tools/weight_measure.js`).

**① 한글의 속공간(카운터)은 영문의 1/4밖에 안 된다**

| 44px | 한글 카운터 면적 | 영문 카운터 면적 | 비율 |
|---|---|---|---|
| weight 400 | 0.0330 | 0.1241 | **27%** |
| weight 600 | 0.0204 | 0.0805 | 25% |
| weight 800 | **0.0146** | 0.0570 | 26% |

한글은 자음+모음 조합이라 획이 많고, **글자 안의 빈 구멍이 애초에 작다.**

**② 웨이트를 올리면 한글이 훨씬 빨리 차오른다** (잉크 밀도 증가율, 400 → 800)

| | 44px | 19px |
|---|---|---|
| **한글** | **+101%** | **+102%** |
| 영문 | +73% | +58% |

**한글은 웨이트 증가에 2배로 민감하다.** 속공간은 1/4인데 밀도는 2배로 차오르니
**같은 800에서 한글만 먼저 막힌다.** (19px 영문 800에서 카운터 2개가 실제로 막혔다)

### 웨이트 상한 (한글)

| 크기 | **한글 상한** | 영문 상한 | 비고 |
|---|---|---|---|
| 40px+ (대형 제목) | **700** | 800~900 | 800은 표지처럼 크게 쓸 때만 |
| 24~36px (제목) | **700** | 800 | |
| 19~23px (본문) | **600** | 700 | 700은 짧은 강조어만 |
| 16~18px (각주) | **500** | 600 | |

**작을수록 더 낮춰야 한다.** 밀도 증가율은 같은데 절대 공간이 없기 때문이다.

```css
/* 한글 — 웨이트를 아낀다 */
.L1-assert { font-weight: 700; }   /* 800 아님 */
.L3-support{ font-weight: 700; }
.L4-detail { font-weight: 400; }
.L5-figure { font-weight: 800; }   /* 숫자는 카운터가 커서 800 견딤 */

/* 영문 전용 요소는 더 굵게 가능 */
.en-title  { font-weight: 800; }
.kicker    { font-weight: 700; }   /* 대문자 라틴 */
```

> **숫자는 예외**: 아라비아 숫자는 획이 단순하고 카운터가 커서 **800~900까지 견딘다.**
> L5(수치 강조)에 800을 쓰는 건 문제없다.

### 자간 — ✅ 이 문서가 정본
```
Heading:  letter-spacing -0.02em ~ -0.04em  (너무 벌리지 말 것)
Body:     letter-spacing 0 ~ 0.02em
```
- **자간 축소로 오버플로를 해결하지 말 것** (density-rules.md §5 STEP 5 금지 항목)
- ⚠️ **웨이트가 높을수록 자간을 조금 더 준다** — 굵으면 글자끼리 붙어 보인다

### 한글 특화 규칙 — ✅ 이 문서가 정본

- **한 줄당 글자 수**: 제목 10~18자 / **본문 20~40자**
  - 널리 인용되는 **"45~75자"는 라틴 기준**이다. 한글 자폭은 라틴의 약 2배
    (라틴 ≈ 0.5em / 한글 ≈ 1.0em)라, 정보량 등가로 환산하면 한글 최적은 **20~40자**.
  - **41자 초과 → 2단으로 전환.** 1280px 캔버스에서 1단 본문(1152px)은 대부분 너무 길다.
    **한글 슬라이드는 2단이 기본형이다.**

  | 구성 | 열 폭 | 24px | 28px | 32px |
  |---|---|---|---|---|
  | 1단 | 1152px | 48자 | 41자 | 36자 |
  | **2단** | 564px | 23자 | 20자 | 17자 |
  | 3단 | 368px | 15자 | 13자 | 11자 |

- **line-height (슬라이드)**: 본문 **1.45~1.6**, 하한 1.35. 제목 1.2~1.25.
  슬라이드는 줄 예산이 유한하다 — 웹처럼 1.8로 벌리면 담을 수 있는 줄이 급감한다.
- **양쪽 정렬(justify) 금지** — 한글은 어절 간격이 튄다. 좌측 정렬 고정.
- **줄바꿈**: `word-break: keep-all` (한글 단어 중간 절단 방지) + `overflow-wrap: break-word`
- 긴 제목은 자연스럽게 2줄 줄바꿈 유도 (3줄은 하드 실패)
- 영어+한글 혼용: 영어는 Pretendard와 잘 맞는 weight 조정
- 과도한 UPPERCASE 피하기 (한글은 대문자 개념 약함)
- Vertical rhythm: **4px 베이스라인 그리드** (한글에 8px 배수는 거칠다)

---

## 스타일별 폰트 조합 추천

### 1. 범용 (거의 모든 프로젝트 — 1순위)
- Heading: **Pretendard Black / ExtraBold** (700~900)
- Body: **Pretendard Regular / Medium** (line-height 1.65~1.8)

### 2. 현대적·세련된 (현재 가장 핫)
- Heading: **SUITE ExtraBold / Black**
- Body: **SUITE Regular / Medium** 또는 Pretendard Medium

### 3. 피치덱·프레젠테이션 (강한 임팩트)
- Heading: **Pretendard Black**
- Body: **Noto Sans KR Medium** 또는 SUITE Medium
- 대안: Wanted Sans Bold + Pretendard Regular

### 4. 고급·프리미엄 브랜드
- Heading: **SUITE Black** 또는 Sandoll Gothic Neo Heavy
- Body: **Pretendard Light / Regular** (여백 넉넉히)
- 트렌드: Sandoll Press Bold (2026)

### 5. 미니멀·테크·기업
- Heading: **Pretendard ExtraBold**
- Body: **Pretendard Regular** 또는 Manrope / Plus Jakarta Sans (영문 혼용)
- 대안: IBM Plex Sans Bold + Pretendard Medium

### 6. 크리에이티브·따뜻한 브랜드
- Heading: **Pretendard Black**
- Body: **Paperlogy** 또는 Gmarket Sans
- 대안: Nanum Square Neo Bold + Pretendard

---

## DESIGN_SYSTEM 적용 시 override 방법

스타일의 DESIGN_SYSTEM.typography를 아래처럼 재작성.
**크기는 밀도 등급(density)에 따라 달라진다** — 아래는 D2(화면공유·영상, 가장 흔한 경우) 기준.

```yaml
typography:
  heading_font: '"Pretendard", "SUITE", system-ui, sans-serif'
  body_font: '"Pretendard", "Noto Sans KR", system-ui, sans-serif'
  density: "D2"          # D1 투사 / D2 화면공유 / D3 배포 — density-rules.md §4
  scale:                 # D2 기준. 등급이 바뀌면 density-rules.md 표를 따를 것
    h1:    "48px"        # weight 800-900, line-height 1.1~1.25, letter-spacing -0.03em
    h2:    "40px"        # weight 700,     line-height 1.15,      letter-spacing -0.02em
    h3:    "30px"        # weight 600,     line-height 1.2
    body:  "28px"        # weight 400,     line-height 1.45~1.6   ← 하한 24px
    small: "17px"        # 각주·출처
  floor: "24px"          # D2 본문 절대 하한. 이 밑으로 축소하면 빌드 실패
  note: "Korean localization — Pretendard. 크기 정본은 density-rules.md"
```

> ⚠️ **옛 스케일(body 17px)은 폐기됐다.** 투사 시 판독 불가 크기였다.

---

## 트리거 조건 (언제 이 파일을 로드하는가)

- 사용자가 한국어로 콘텐츠 작성
- "한국 시장", "한국 사용자", "KR", "국내" 언급
- 한글이 포함된 텍스트/슬라이드 생성 요청
- 기본값: Jake(한국 디자이너)의 모든 작업에 적용
