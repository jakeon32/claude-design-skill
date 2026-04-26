---
name: layout-variation-spec
description: "레이아웃 3축 베리에이션 시스템 — 분할표현(기본형/면/선) × 비율 × 패딩. 에이전트가 Step 1-C에서 이 파일을 참조해 레이아웃 변수를 결정한다."
---

# 레이아웃 베리에이션 스펙

> **목적**: 같은 레이아웃 유형도 3개의 독립 변수를 조합하면 시각적으로 전혀 다른 슬라이드가 된다.  
> 에이전트는 각 슬라이드 HTML 생성 전 이 3축을 먼저 결정하고, 해당 CSS 패턴을 템플릿에 적용한다.

---

## 3축 변수 정의

### 축 A — 분할 표현 (Expression)

경계를 어떻게 보이게 할 것인가.

| 값 | 이름 | 설명 |
|----|------|------|
| `whitespace` | 기본형 (여백 분할) | 배경색 동일. 콘텐츠 위치·크기·정렬로만 구획 형성. 경계가 보이지 않아야 성공. |
| `panel` | 면 분할 | 구역마다 다른 배경색 (var(--primary) / var(--bg)). 명확한 구획, 강한 대비. |
| `line` | 선 분할 | 배경 동일 + 얇은 border 1개로 경계. 세련, 모던. |

#### CSS 패턴

**`whitespace` — 기본형**
```css
/* 공유 배경, 경계 없음. 여백과 정렬로 구분. */
background: var(--bg);
/* 구분선, 패널 배경 없음 */
```

**`panel` — 면 분할**
```css
/* 좌/상 패널 */
background: var(--primary);   /* 또는 var(--surface), var(--accent-10) */
color: var(--on-primary);

/* 우/하 패널 */
background: var(--bg);
```

**`line` — 선 분할**
```css
/* 수직 구분선 (2-col) */
border-right: 1px solid var(--border);
/* 또는 */
border-left: 1px solid var(--border);

/* 수평 구분선 (2-row / header+body) */
border-bottom: 1px solid var(--border);
/* 또는 accent 강조선 */
border-bottom: 2px solid var(--accent);
```

---

### 축 B — 비율 (Proportion)

각 구역의 상대적 크기.

#### 2-col (좌:우)

| 비율 이름 | 좌:우 | 좌측 flex | 우측 flex | 용도 |
|---------|-------|---------|---------|------|
| `20:80` | 20:80 | `flex:0 0 256px` | `flex:1` | 이미지·비주얼 중심 |
| `30:70` | 30:70 | `flex:0 0 384px` | `flex:1` | 헤딩 좌 + 본문 우 (기본) |
| `40:60` | 40:60 | `flex:0 0 512px` | `flex:1` | 균형 잡힌 2열 |
| `50:50` | 50:50 | `flex:0 0 640px` | `flex:1` | 완전 균등, 비교 |
| `60:40` | 60:40 | `flex:1` | `flex:0 0 512px` | 본문 좌 + 액센트 우 |
| `70:30` | 70:30 | `flex:1` | `flex:0 0 384px` | 역순 (r) — 타이포 좌 + 강조 우 |
| `80:20` | 80:20 | `flex:1` | `flex:0 0 256px` | 역순 — 비주얼 좌 + 라벨 우 |

#### 2-row (상:하)

| 비율 이름 | 상:하 | 상단 height | 하단 |
|---------|-------|---------|------|
| `20:80` | 20:80 | `flex:0 0 144px` | `flex:1` | 좁은 레이블 밴드 |
| `30:70` | 30:70 | `flex:0 0 216px` | `flex:1` | 소제목 밴드 (기본) |
| `40:60` | 40:60 | `flex:0 0 288px` | `flex:1` | 제목+서브 밴드 |
| `50:50` | 50:50 | `flex:0 0 360px` | `flex:1` | 균등 상하 |

#### header+cards (헤더:카드영역)

| 비율 이름 | 헤더 높이 | 카드 패딩 |
|---------|---------|---------|
| `compact` | `padding:32px 80px 20px` | `padding:0 80px 40px` |
| `standard` | `padding:44px 80px 28px` | `padding:0 80px 48px` |
| `tall` | `padding:56px 80px 36px` | `padding:0 80px 56px` |

---

### 축 C — 패딩 (Padding)

슬라이드 외부 여백과 내부 간격.

| 값 | 이름 | 외부 여백 | 내부 gap | 느낌 |
|----|------|---------|---------|------|
| `tight` | 조밀 | `48px` | `16px` | 정보 밀도 높음, 비즈니스 |
| `standard` | 표준 | `64px` | `24–32px` | 균형 (기본값) |
| `airy` | 여유 | `80–96px` | `40–48px` | 공간감, 럭셔리·미니멀 |

#### CSS 적용

**`tight`**
```css
/* 외부 */
padding: 0 48px;          /* 2-col 수평형 */
padding: 40px 48px 40px;  /* 상하 여백 포함 */
/* 내부 */
gap: 16px;
padding-right: 40px;      /* 좌측 콘텐츠 패딩 */
```

**`standard`**
```css
padding: 0 64px;
padding: 48px 64px 48px;
gap: 24px;
padding-right: 48px;
```

**`airy`**
```css
padding: 0 80px;           /* 또는 96px */
padding: 56px 80px 56px;
gap: 40px;
padding-right: 60px;
```

---

## 구조 패턴별 유효 조합 매트릭스

### 패턴 1 — 2-col-LR (좌우 2열)

해당 레이아웃: `Highlight`, `Simple List`, `Photo Split`, `Numbered List`, `Asymmetric`, `Mobile Mockup (1)`, `Desktop Mockup`

| 축 | 유효 값 | 권장 기본값 |
|----|---------|-----------|
| Expression | `whitespace` / `panel` / `line` | 스타일별 결정 (아래 표 참고) |
| Proportion | `30:70` / `40:60` / `50:50` / `70:30` | `30:70` |
| Padding | `standard` / `airy` | `standard` |

**스타일별 Expression 권장**:

| 스타일 계열 | 권장 Expression | 이유 |
|-----------|----------------|------|
| Swiss / Editorial | `line` 또는 `whitespace` | 타이포가 구조를 만듦 |
| Corporate / Trust | `panel` | 명확한 구획, 안정감 |
| Minimal / Luxury | `whitespace` | 공간 자체가 메시지 |
| Neo-Brutalism | `panel` (강한 대비) | 명확한 경계가 핵심 |
| Midnight / Dark Editorial | `whitespace` | 단일 다크 캔버스 위 플로팅 |

**Photo Split 주의**: `whitespace` Expression 사용 시 이미지 패널에 gradient blend 적용. `line` 사용 시 gradient 제거 + 명확한 border.

---

### 패턴 2 — header+cards (헤더+카드/열)

해당 레이아웃: `3-Column Text`, `4-Column Text`, `2×2 Grid`, `Feature Cards (2/3/4-col)`, `Key Metrics`, `Team Grid`, `Bar/Column Chart`, `Pie/Donut`, 기타 data layouts

| 축 | 유효 값 | 권장 기본값 |
|----|---------|-----------|
| Expression | `whitespace` / `panel`(헤더 배경) | `whitespace` |
| Proportion (헤더 높이) | `compact` / `standard` / `tall` | `standard` |
| Padding | `tight` / `standard` / `airy` | `standard` |

**Expression 패턴**:
- `whitespace`: 헤더 배경 = var(--bg). 폰트 크기 차이로 구분.
- `panel`: 헤더 배경 = var(--primary) 또는 var(--surface). 헤더가 독립 밴드처럼 보임.

**카드 내부 Expression**:
- `whitespace`: 카드 배경 없음. 내용 배치로만 구분. `border: none; background: transparent;`
- `panel`: 카드 = `background: var(--surface)` (기본값)
- `line`: 카드 = `border: 1px solid var(--border); background: transparent;`

---

### 패턴 3 — full-canvas (단일 전체화면)

해당 레이아웃: `Centered Statement`, `Big Number`, `Full Bleed Photo`, `Feature Highlight`, `Section Title`, `Closing/CTA`

| 축 | 유효 값 | 권장 기본값 |
|----|---------|-----------|
| Expression | — (단일 영역, 해당 없음) | — |
| Alignment | `center` / `left` / `bottom-left` | `center` |
| Padding | `standard` / `airy` | `airy` |

**Alignment CSS**:
```css
/* center */
align-items: center; justify-content: center; text-align: center;

/* left */
align-items: center; justify-content: flex-start;
padding-left: 80px;  /* outer padding에 따라 조정 */

/* bottom-left */
align-items: flex-end; justify-content: flex-start;
padding: 0 80px 80px;
```

---

### 패턴 4 — 2-row-TB (상하 2행)

해당 레이아웃: `Horizontal Timeline`, `Roadmap`, `2-row-30` 기반 레이아웃

| 축 | 유효 값 | 권장 기본값 |
|----|---------|-----------|
| Expression | `whitespace` / `panel` / `line` | `line` (수평 구분선) |
| Proportion | `20:80` / `30:70` / `40:60` | `30:70` |
| Padding | `tight` / `standard` | `standard` |

**Timeline 전용**: 하단 콘텐츠 영역 내부 패딩은 `airy` 금지 — 타임라인 노드 간격이 넓어져 선이 단조로워짐.

---

### 패턴 5 — card-grid (카드 그리드, 동등 N분할)

해당 레이아웃: `Feature Cards 3-col`, `Feature Cards 4-col`, `Team Grid`, `3-Column Text`, `4-Column Text` (카드 셀 독립 처리 시)

| 축 | 유효 값 | 권장 기본값 |
|----|---------|-----------|
| Card Expression | `filled` / `outlined` / `borderless` | `filled` |
| Gap | `tight(16px)` / `standard(24px)` / `airy(40px)` | `standard` |
| Padding | `tight` / `standard` | `standard` |

**Card Expression CSS**:
```css
/* filled — 카드 배경 */
background: var(--surface);
border-radius: var(--radius);
border: none;

/* outlined — 아웃라인만 */
background: transparent;
border: 1px solid var(--border);
border-radius: var(--radius);

/* borderless — 경계 없음 */
background: transparent;
border: none;
border-radius: 0;
/* 내부 요소 위치로만 구분 */
```

---

## 에이전트 사용 프로토콜

### Step 1-C에서 3축 결정 순서

```
1. 스타일 파일 확인
   → 스타일이 면분할을 강조하는가? 선분할? 여백?
   → 해당 Expression을 우선 선택

2. 콘텐츠 밀도 확인
   → 정보 많음 → tight / standard 패딩
   → 강조 슬라이드 → airy 패딩

3. 전체 덱 다양성 확인
   → 이전 슬라이드와 같은 Expression? → 다른 값 선택
   → 모든 슬라이드 panel fill → 40% 이하 권장

4. 비율 결정
   → 콘텐츠 무게중심이 어느 쪽인가?
   → 이미지·비주얼 중심 → 해당 쪽 비율 ↑
   → 균등 비교 → 50:50
```

### Step 1-D 구성안 출력 형식 (확장)

```markdown
| # | 슬라이드명 | 그리드 | Expression | Proportion | Padding | 핵심 메시지 |
|---|-----------|-------|-----------|-----------|---------|-----------|
| 1 | Cover | 2-col-LR | panel | 40:60 | airy | 덱 제목 |
| 2 | Statement | full-canvas | — | center | airy | 핵심 선언 |
| 3 | Feature | header+cards | whitespace | standard | standard | 기능 3종 |
| 4 | Data | 2-row-TB | line | 30:70 | tight | 성장 지표 |
```

---

## 덱 내 Expression 다양성 규칙

```
규칙 V1: panel Expression → 덱 전체의 40% 이하
규칙 V2: 연속 2장 동일 Expression 금지
규칙 V3: 전체 3가지 Expression을 덱 내에 최소 2가지 이상 사용 (10장 이상 덱)
규칙 V4: 패딩은 슬라이드 밀도에 따라 다르게 — 고밀도(차트/표) → tight, 저밀도(선언/CTA) → airy
```

---

## 빠른 참조 — 스타일별 기본 3축 조합

| 스타일 | Expression 기본 | Proportion 기본 | Padding 기본 |
|-------|----------------|----------------|-------------|
| Swiss International | `line` | `30:70` | `airy` |
| Corporate Trust | `panel` | `40:60` | `standard` |
| Midnight Editorial | `whitespace` | `50:50` | `airy` |
| Neo-Brutalism | `panel` (강한 대비) | `50:50` | `tight` |
| Minimal Modern | `whitespace` | `30:70` | `airy` |
| Bold Editorial | `panel` | `40:60` | `standard` |
| Raw Form | `line` + `whitespace` 혼용 | `30:70` | `standard` |
