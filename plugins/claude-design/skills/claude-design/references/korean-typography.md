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

### 🔴 폰트 웨이트 — 한글은 영문보다 덜 써야 한다 (Pretendard 실측)

**영문처럼 웨이트를 올리면 한글은 뭉친다.** 그런데 **한글 안에서도 편차가 크다.**
`tools/weight_measure.js`로 Canvas에 렌더해 **속공간(카운터)을 직접 셌다.**

**핵심 발견: 막히는 건 "복잡한 글자"뿐이다**

19px, 웨이트별 카운터 생존:

| 텍스트 | 400 | 700 | 800 | 900 |
|---|---|---|---|---|
| **영문** "Verified Capability" | 7개 | 7개 | 7개 | **7개 (손실 0%)** |
| 한글 **단순** "이 수가 나아" | 2 | 2 | 2 | 2 (손실 0%) |
| 한글 **복잡** "뚫렸던 확률과 넓혔다" | 6개 | **4개 (−33%)** | **3개 (−50%)** | **1개 (−83%)** |

**영문은 900에서도 속공간이 하나도 안 막힌다.**
한글 복잡 글자는 **700에서 이미 1/3이 막히고, 900에서는 83%가 사라진다.**

44px에서도 같다 — 복잡 글자의 **카운터 면적**:
`400 → 0.0159` / **`700 → 0.0072`** (이미 임계 0.010 아래) / `900 → 0.0034` (거의 소멸)

> **→ 상한은 "복잡한 글자 + 작은 크기" 기준으로 잡아야 한다.**
> "규격은 코드에" 같은 널널한 예시로 재면 안전해 보이지만,
> 실무 문장에는 **겹받침·복모음·된소리**가 섞인다.

### 웨이트 상한 — 텍스트 복잡도에 따라 달라진다

| 크기 | 한글 **복잡** (겹받침 많음) | 한글 **일반** | 영문 |
|---|---|---|---|
| 40px+ (대형 제목) | **600** | 700 | 900 |
| 24~36px (제목) | **600** | 700 | 800 |
| 19~23px (본문) | **500** | 600 | 700 |
| 16~18px (각주) | **400** | 500 | 600 |

**복잡도는 계산할 수 있다** — `tools/hangul_complexity.js`

```bash
node tools/hangul_complexity.js
```
```
텍스트                     px   복잡도  상한   구성
규격은 코드에 둔다          44   0.112   700   —
뚫렸던 확률과 넓혔다        44   0.539   600   겹받침4 · 복모음2 · 된소리3
뚫렸던 확률과 넓혔다        19   0.539   500   겹받침4 · 복모음2 · 된소리3
```

복잡도 = 겹받침(+0.45) · 복모음(+0.25) · 된소리·ㅎ(+0.15) · 받침(+0.30) 의 음절당 평균.
**0.40 이상이면 웨이트를 한 단계 낮춘다.**

```js
const { maxWeight, check } = require('tools/hangul_complexity.js');
maxWeight('뚫렸던 확률과 넓혔다', 19);   // → 500
check('뚫렸던 확률과 넓혔다', 19, 700);  // → "복잡도 0.539 → 상한 500 (현재 700)"
```

```css
/* 한글 — 웨이트를 아낀다 */
.L1-assert { font-weight: 700; }   /* 복잡한 제목이면 600 */
.L3-support{ font-weight: 700; }   /* 복잡하면 600 */
.L4-detail { font-weight: 400; }
.L5-figure { font-weight: 800; }   /* 숫자는 예외 — 카운터가 커서 견딤 */

/* 영문 전용 요소는 굵게 가능 */
.en-title  { font-weight: 800; }
.kicker    { font-weight: 700; }
```

> **숫자·영문은 예외**: 아라비아 숫자와 라틴은 획이 단순하고 카운터가 커서
> **800~900까지 견딘다.** L5(수치 강조)에 800을 쓰는 건 문제없다.

### ⚠️ 폰트 스택 확인
Pretendard는 **사용자 폰트 폴더**(`%LOCALAPPDATA%\Microsoft\Windows\Fonts`)에 설치될 수 있다.
시스템 폰트 폴더만 확인하면 "없다"고 오판한다.
**렌더 폭으로 검증할 것**: 다른 폰트와 폭이 같으면 fallback된 것이다.

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
