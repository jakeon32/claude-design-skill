---
name: diagram-layouts
description: "슬라이드 도해(Diagram) 레이아웃 SVG 템플릿 — 프로세스 플로우, 계층 트리, 사이클, 벤 다이어그램, 레이어 아키텍처. 노드 4개 기본·선 교차 0·화살표는 흐름일 때만. 도해를 그릴지 텍스트로 쓸지 판단하는 게이트 포함."
---

# Diagram Layouts

> **2026-07-14 신설.** 그 전까지 이 스킬에는 **도해 템플릿이 0개**였다.
> 더 나쁜 것은 `index.md` 카탈로그가 "Venn Diagram"을 **있다고 등재해놓고 실체가 없었다**는 점이다.
> AI가 그 안내를 따라가 없는 템플릿을 찾다가 매번 즉흥적으로 그렸다.
> **취약했던 게 아니라 잘못된 지도를 줬던 것이다.**

**근거 등급**: **[실증]** 통제 실험/메타분석 / **[이론]** 인지이론 유도 / **[관행]** 업계 컨벤션(실증 없음) / **[사실]** 수학적·기술적 사실

---

## 0. ★ 최상위 게이트 — 도해를 그릴 것인가

**도해는 기본값이 아니다.** 셋을 통과할 때만 그린다.

**게이트 1 — 구조가 있는가.**
내용에 명시적 구조(순서·위계·연결·교집합·순환·포함)가 없으면 도해는 리스트를 그림으로 감싼 장식이다.
Mayer 일관성 원리: 무관한 자료를 제거하면 학습이 개선된다. **23/23 실험 지지, d = 0.86** [실증]

**게이트 2 — 한 문장 테스트.**
"이 도해를 보면 ___를 알 수 있다"를 채울 수 있어야 한다.
채워지는 문장이 슬라이드 제목과 같은 말이면 **도해는 필요 없다.**

**게이트 3 — 공간 대비 정보량.**
1280×720에서 도해는 최소 400×280px을 먹는다.
그 면적이 **텍스트 3줄보다 많은 걸 전달하지 못하면 텍스트로 쓴다.**

> ⚠️ **이 스킬의 주요 실패 모드 예고**: 도해 템플릿이 생기면 AI는 **모든 슬라이드를 도해로 만들려 한다.**
> **"해당 없음 → 텍스트"가 정상 출구다.** 결정표에 억지로 끼워 맞추지 마라.

### Tversky의 두 원리 [이론] — 도해 설계의 상위 규범
- **적합성(congruence)**: 외부 표현의 구조가 전달하려는 내부 구조와 대응해야 한다
  → *화살표를 쓴다면 실제로 흐름이 있어야 한다.*
- **파악성(apprehension)**: 그 구조가 정확히 지각·이해될 수 있어야 한다
  → *복잡하면 실패한다. 화려함은 이해도가 아니다.*

---

## 1. 선택 결정표

| 내용의 형태 | 신호어 | 유형 | 템플릿 |
|---|---|---|---|
| 순서가 있고 **끝이 있음** | 그다음, 단계, 파이프라인 | **프로세스 플로우** | `flow-h` §3-1 |
| 순서가 있고 **끝이 시작으로 돌아옴** | 반복, 루프, 주기, 개선 | **사이클** | `cycle` §3-3 |
| 상위-하위, 소속, 분해 | 산하, 구성, 하위, 분류 | **계층 트리** | `tree` §3-2 |
| 구성요소 + 경계 + 의존 | 시스템, 스택, 레이어 | **레이어 아키텍처** | `arch` §3-5 |
| 겹치는 조건, **교집합이 결론** | 둘 다, 교차, 스위트스팟 | **벤** (2~3원) | `venn` §3-4 |
| 다대다 연결, **흐름 아님** | 관계, 상호작용 | 네트워크 (선만, 화살표 ✕) | — |
| 두 축의 4분면 | 높다/낮다 조합 | 2×2 매트릭스 | data-layouts.md |
| 수치 비교·추세 | %, 증가, 대비 | **차트** — 도해 아님 | data-layouts.md |
| **위 어디에도 안 맞음** | — | **도해 없음. 텍스트.** | — |

### 🔴 화살표 = 흐름. 선 = 연결. 섞지 마라.
SmartArt 문서의 규칙 [관행이지만 Tversky 적합성과 정합]:
> "화살표를 포함한 레이아웃은 **특정 방향의 흐름/진행을 함의**한다.
> 화살표 대신 연결선을 쓰면 **연결은 함의하되 흐름·진행은 함의하지 않는다.**"

**방향이 없으면 화살표를 쓰지 마라. 선을 써라.** 위반하면 독자는 **없는 순서를 읽는다.**

---

## 2. 공통 설계 규칙

### 2-1. 노드 개수 — 7±2를 쓰지 마라

**Miller의 7±2는 도해 설계 근거로 부적절하다.** [실증]
- Miller(1956) 본인이 "rough estimate이자 수사적 장치"로 썼다
- Cowan(2001): 청킹·리허설이 차단된 조건에서 실제 용량은 **4±1**
- 화해: 7은 청킹이 자유로울 때, 4는 그렇지 않을 때.
  **처음 보는 도해의 노드는 청킹이 안 된 상태** → **4가 맞는 기준**

**→ 노드 4개 기본, 5개 실용 상한, 6개는 예외, 7개 이상은 도해를 쪼갠다.**

| 유형 | 기본 | 상한 | 초과 시 |
|---|---|---|---|
| 프로세스 플로우 | 4 | 5 (1행) / 6 (3+3 2행) | 상위 4단계로 접기 |
| 사이클 | 4 | 6 | 사이클 2개로 분리 |
| 계층 트리 | 깊이 2, 총 7 | 깊이 3, 형제 4, 총 12 | 서브트리를 다음 슬라이드로 |
| 레이어 아키텍처 | 3층 × 3요소 | 4층 × 4요소 | 한 층을 확대 슬라이드로 |
| 벤 | 2원 | **3원** | **4원 이상은 원으로 작도 불가** |
| 네트워크 | 5 | 7 노드 / 10 엣지 | 클러스터로 접기 |

> **[사실]** 4개 집합의 벤 다이어그램은 **원으로 작도할 수 없다**(Venn 본인이 타원을 썼다).
> 4원 벤을 요구받으면 그리지 말고 **매트릭스나 표로 전환**할 것.

### 2-2. 선 교차 — 가장 강한 실증 규칙

Purchase의 그래프 드로잉 미학 실험: **선 교차(edge crossing) 최소화가 압도적 1위 요인.**
벤드(꺾임) 최소화와 대칭성은 훨씬 약한 근거. [실증]

1. **선 교차 0.** 교차가 생기면 노드를 재배치한다. 안 되면 **도해를 쪼갠다.**
   (교차 회피 > 예쁜 레이아웃)
2. 꺾임은 노드당 최대 2회. **직교 엘보만**(수직→수평→수직), 대각선 금지
3. 대칭은 있으면 좋지만, **대칭을 위해 교차를 만들지 마라**

### 2-3. 화살표
- **방향 일관성** [관행, 광범위 합의]: 좌→우 **또는** 위→아래 중 **하나만**. 섞지 않는다
- 되먹임(feedback)만 예외 — 반드시 **점선 + 곡선**으로 주 흐름과 시각적으로 구별
- **분기 화살표엔 반드시 레이블**(Yes/No). 무레이블 분기 금지
- 판별 테스트: **"화살표를 뒤집으면 틀린 말이 되는가?"** 아니면 그 화살표는 거짓 구조다

### 2-4. 레이블 — 근접성

Mayer **공간 근접성(spatial contiguity) d = 0.79** [실증] / **신호화(signaling) d = 0.46** [실증]

- 레이블은 **대상 안 또는 6px 이내**. **별도 범례로 빼지 마라.**
  도해에 범례가 필요하면 **도해가 잘못 설계된 것이다**
- 노드 텍스트는 **2~5 단어**. 문장을 노드에 넣지 않는다
- 노드당 최대 2줄: 제목(600) + 부연(muted)
- **강조는 딱 하나의 노드에만.** `--accent`는 "여기를 보라"는 신호다. 3개 이상 칠하면 신호가 죽는다

### 2-5. 기하 규격 (1280×720)

```
안전 여백    : 64px (좌우), 48px (상하)
제목 밴드    : y 48–140
도해 캔버스  : x 64–1216 (1152), y 160–656 (496)
격자 단위    : 8px — 모든 좌표는 8의 배수
노드 간격    : 최소 48px (연결선 있으면 64px — 화살촉이 숨 쉴 공간)
모서리 반경  : 컨테이너 12px / 노드 10px / 칩 8px   ← 개체 크기에 비례
선 두께      : 연결선 2px / 강조 3px / 노드 테두리 1.5px
```

---

## 3. 공통 CSS + 마커 (한 번만 정의해 재사용)

### 🔴 [사실·검증됨] SVG 프레젠테이션 속성에 CSS 변수를 쓰지 마라

```html
<!-- ✕ Chromium에서 작동하지 않음. 속성값은 캐스케이드 치환을 거치지 않는다 -->
<rect fill="var(--accent)"/>

<!-- ○ 반드시 style= 또는 CSS 클래스로 -->
<rect style="fill: var(--accent)"/>
<rect class="node-box"/>
```
아래 코드는 전부 이 규칙을 따르며 **헤드리스 Chromium에서 렌더 검증했다.**

```css
/* 도해 공통 — 슬라이드 테마 변수에 자동 종속 */
.node-box   { fill: var(--surface); stroke: var(--border); stroke-width: 1.5; }
.node-box.is-active { fill: var(--accent-soft); stroke: var(--accent); stroke-width: 2; }
.node-label { fill: var(--text);  font-size: 22px; font-weight: 600;
              text-anchor: middle; dominant-baseline: middle; }
.node-sub   { fill: var(--muted); font-size: 15px;
              text-anchor: middle; dominant-baseline: middle; }
.conn       { stroke: var(--border); stroke-width: 2; fill: none; }
.conn.is-accent { stroke: var(--accent); }
.edge-label { fill: var(--muted); font-size: 14px; text-anchor: middle; }
.badge      { fill: var(--accent); font-size: 13px; font-weight: 700;
              text-anchor: middle; dominant-baseline: middle; }
.region     { fill: var(--text); font-size: 15px; font-weight: 600;
              text-anchor: middle; dominant-baseline: middle; }
```

> `--accent-soft`(accent 12~18% 틴트)와 `--muted`가 팔레트에 없으면 추가할 것.
> 도해는 **"약한 강조" 단계가 없으면 강조가 전부 아니면 전무**가 된다.

### 화살표 마커

```html
<defs>
  <!-- refX=9 (viewBox 폭 10) → 촉 끝이 path 종점에 정확히 놓임 -->
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="6" markerHeight="6"
          orient="auto-start-reverse" markerUnits="strokeWidth">
    <path d="M 0 0 L 10 5 L 0 10 z" style="fill: var(--border)"/>
  </marker>
  <marker id="arrow-accent" viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="6" markerHeight="6"
          orient="auto-start-reverse" markerUnits="strokeWidth">
    <path d="M 0 0 L 10 5 L 0 10 z" style="fill: var(--accent)"/>
  </marker>
</defs>
```

**마커 함정 4개** [사실]
1. **`markerUnits` 기본값은 `strokeWidth`** — 선 굵기를 바꾸면 화살촉 크기가 같이 변한다.
   `markerWidth=6`은 "선 굵기의 6배". stroke-width 2 → 실제 12px 촉.
   고정 크기를 원하면 `markerUnits="userSpaceOnUse"`
2. **선 색과 마커 색은 자동 동기화되지 않는다.** 마커 `<path>`에 별도로 fill을 준다.
   (`context-stroke`는 Chrome만 지원 + PPTX에서 깨짐 → **색별로 마커를 복제하는 쪽을 권장**)
3. **`refX`로 촉 끝 정렬** — `refX=5`면 촉이 종점을 절반 지나친다
4. **선이 촉 뒤로 비침** — 색을 맞추거나 선 종점을 8px 당길 것

---

## 3-1. 가로 프로세스 플로우 (`flow-h`)

**언제**: 순서가 있고 **끝이 있는** 절차. "How" 질문.
**쓰지 말 것**: 순서 없는 항목 나열(→ 텍스트), 끝이 시작으로 돌아옴(→ 사이클).

| 항목 | 값 |
|---|---|
| 단계 | 4 (기본), 5 상한 |
| 박스 | 240×120, r=10 |
| 간격 | 64px |
| **4박스 총폭** | 4×240 + 3×64 = **1152 = 안전영역 정확히 채움** |
| 시작 x | 64, 368, 672, 976 |
| 박스 y | 300 / 연결선 y | 360 |
| 강조 | 핵심 단계 **1개**만 `.is-active` |

```html
<svg width="1280" height="720" viewBox="0 0 1280 720" role="img">
  <title>제작 파이프라인 4단계</title>
  <desc>수집 → 선별 → 제작 → 발행. 성과 데이터가 수집 단계로 되먹임된다.</desc>
  <!-- defs: 위 marker 블록 -->

  <g>
    <rect class="node-box" x="64" y="300" width="240" height="120" rx="10"/>
    <text class="badge"      x="88"  y="330">01</text>
    <text class="node-label" x="184" y="352">수집</text>
    <text class="node-sub"   x="184" y="384">RSS · X · 스크랩</text>
  </g>
  <g>
    <rect class="node-box" x="368" y="300" width="240" height="120" rx="10"/>
    <text class="badge"      x="392" y="330">02</text>
    <text class="node-label" x="488" y="352">선별</text>
    <text class="node-sub"   x="488" y="384">팩트체크 · 랭킹</text>
  </g>
  <g>
    <rect class="node-box is-active" x="672" y="300" width="240" height="120" rx="10"/>
    <text class="badge"      x="696" y="330">03</text>
    <text class="node-label" x="792" y="352">제작</text>
    <text class="node-sub"   x="792" y="384">대본 · TTS · 렌더</text>
  </g>
  <g>
    <rect class="node-box" x="976" y="300" width="240" height="120" rx="10"/>
    <text class="badge"      x="1000" y="330">04</text>
    <text class="node-label" x="1096" y="352">발행</text>
    <text class="node-sub"   x="1096" y="384">업로드 · 계측</text>
  </g>

  <!-- 연결선: 박스 우변 +8 → 다음 박스 좌변 -8 -->
  <line class="conn"           x1="312" y1="360" x2="360" y2="360" marker-end="url(#arrow)"/>
  <line class="conn is-accent" x1="616" y1="360" x2="664" y2="360" marker-end="url(#arrow-accent)"/>
  <line class="conn"           x1="920" y1="360" x2="968" y2="360" marker-end="url(#arrow)"/>

  <!-- 되먹임: 반드시 점선 + 곡선으로 주 흐름과 구별 -->
  <path class="conn" style="stroke-dasharray:6 5"
        d="M 1096 428 C 1096 520, 184 520, 184 428" marker-end="url(#arrow)"/>
  <text class="edge-label" x="640" y="545">성과 데이터 피드백</text>
</svg>
```

**되먹임 베지어 공식** (재사용): 마지막 박스 하단 `(xN, yB)` → 첫 박스 하단 `(x1, yB)`, 처짐 `sag = 92`
```
d = "M xN yB C xN (yB+sag), x1 (yB+sag), x1 yB"
```
제어점의 x를 시작·끝점과 같게 두면 곡선이 박스에서 **수직으로 떨어졌다 수직으로 올라간다**
→ 접선이 화살촉 방향과 일치한다.

---

## 3-2. 계층 트리 (`tree`)

**언제**: 위계·소속·분해. 조직도·분류.
**쓰지 말 것**: 노드 간 관계가 위계가 아니라 상호작용일 때(→ 네트워크).

| 항목 | 값 |
|---|---|
| 깊이 | 2 (기본), 3 상한 |
| 형제 | 3 (기본), 4 상한 |
| 레벨 y | 180 / 360 / 524 |
| 버스선 y | 부모 하단 + 48 (= 자식 상단 − 48, **정확히 중간**) |
| 노드 폭 | L1 260 / L2 240 / L3 200 (**하위로 갈수록 축소 = 위계 신호**) |
| 연결 | **직교 엘보만.** 대각선 금지 |

```html
<svg width="1280" height="720" viewBox="0 0 1280 720" role="img">
  <title>파이프라인 구성</title>
  <desc>유튜브 파이프라인은 소재·제작·배포 세 갈래로 나뉘고, 제작은 다시 TTS와 Remotion으로 나뉜다.</desc>

  <rect class="node-box is-active" x="510" y="180" width="260" height="84" rx="10"/>
  <text class="node-label" x="640" y="222">유튜브 파이프라인</text>

  <rect class="node-box" x="144" y="360" width="240" height="84" rx="10"/>
  <text class="node-label" x="264" y="402">소재</text>
  <rect class="node-box" x="520" y="360" width="240" height="84" rx="10"/>
  <text class="node-label" x="640" y="402">제작</text>
  <rect class="node-box" x="896" y="360" width="240" height="84" rx="10"/>
  <text class="node-label" x="1016" y="402">배포</text>

  <!-- 엘보 커넥터: 부모하단(264) → 버스(312) → 자식상단(360) -->
  <path class="conn" d="M 640 264 V 312 H 264  V 360"/>
  <path class="conn" d="M 640 264 V 312 H 640  V 360"/>
  <path class="conn" d="M 640 264 V 312 H 1016 V 360"/>

  <rect class="node-box" x="436" y="524" width="200" height="72" rx="10"/>
  <text class="node-label" x="536" y="560" style="font-size:19px">TTS</text>
  <rect class="node-box" x="660" y="524" width="200" height="72" rx="10"/>
  <text class="node-label" x="760" y="560" style="font-size:19px">Remotion</text>

  <path class="conn" d="M 640 444 V 486 H 536 V 524"/>
  <path class="conn" d="M 640 444 V 486 H 760 V 524"/>
</svg>
```

**엘보 공식**: `M px pBottom V busY H cx V cTop` (`busY = (pBottom + cTop) / 2`)
같은 부모의 자식들은 **같은 `busY`를 공유**해야 선들이 하나의 수평선으로 겹쳐 보인다.
어긋나면 계단처럼 보이고 교차가 발생한다.

**화살표를 쓰지 않는다** — **위계는 흐름이 아니다** (Tversky 적합성).

---

## 3-3. 사이클 (`cycle`)

**언제**: 끝이 시작으로 돌아오는 반복.
**쓰지 말 것**: 순서는 있으나 반복하지 않는 것(→ 플로우).
**원형은 "끝이 없음"을 강하게 함의하므로 잘못 쓰면 거짓 정보다.**

| 항목 | 값 |
|---|---|
| 스텝 | 4 (최적), 3~6 |
| 링 반경 R | 190 / 중심 (640, 400) |
| 노드 원 r | 62 |
| **아크 각도 갭** | 노드 양쪽 **26°** (= atan(62/190) ≈ 18° + 패딩 8°) |
| 스텝 각도 | 360/n. 4스텝 = −90°, 0°, 90°, 180° |
| 아크 | 3px + `--accent` (**사이클의 주인공은 화살표다**) |

**아크 좌표 공식**
```
점(θ)  = (640 + 190·cos θ,  400 + 190·sin θ)      // SVG는 y가 아래로 증가
아크 i : θ_start = θ_i + 26°,  θ_end = θ_{i+1} − 26°
d = "M sx sy A 190 190 0 0 1 ex ey"                // sweep-flag=1 = 시계방향
```

```html
<svg width="1280" height="720" viewBox="0 0 1280 720" role="img">
  <title>데일리 제작 루프</title>
  <desc>기획 → 제작 → 발행 → 분석이 순환하며, 분석 결과가 다시 기획에 반영된다.</desc>
  <defs>
    <marker id="arrow-c" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="5.5" markerHeight="5.5" orient="auto" markerUnits="strokeWidth">
      <path d="M 0 0 L 10 5 L 0 10 z" style="fill: var(--accent)"/>
    </marker>
  </defs>

  <!-- 4개 아크 (시계방향) — 위 공식으로 사전 계산된 좌표 -->
  <path class="conn is-accent" stroke-width="3" marker-end="url(#arrow-c)"
        d="M 723.3 229.4 A 190 190 0 0 1 810.8 316.9"/>
  <path class="conn is-accent" stroke-width="3" marker-end="url(#arrow-c)"
        d="M 810.8 483.1 A 190 190 0 0 1 723.3 570.6"/>
  <path class="conn is-accent" stroke-width="3" marker-end="url(#arrow-c)"
        d="M 556.7 570.6 A 190 190 0 0 1 469.2 483.1"/>
  <path class="conn is-accent" stroke-width="3" marker-end="url(#arrow-c)"
        d="M 469.2 316.9 A 190 190 0 0 1 556.7 229.4"/>

  <g><circle class="node-box is-active" cx="640" cy="210" r="62"/>
     <text class="node-label" x="640" y="205" style="font-size:20px">기획</text>
     <text class="node-sub"   x="640" y="228">주 1회</text></g>
  <g><circle class="node-box" cx="830" cy="400" r="62"/>
     <text class="node-label" x="830" y="395" style="font-size:20px">제작</text>
     <text class="node-sub"   x="830" y="418">일 1편</text></g>
  <g><circle class="node-box" cx="640" cy="590" r="62"/>
     <text class="node-label" x="640" y="585" style="font-size:20px">발행</text>
     <text class="node-sub"   x="640" y="608">21:00</text></g>
  <g><circle class="node-box" cx="450" cy="400" r="62"/>
     <text class="node-label" x="450" y="395" style="font-size:20px">분석</text>
     <text class="node-sub"   x="450" y="418">48h 조회</text></g>

  <text class="node-sub" x="640" y="400" style="font-size:17px">데일리 루프</text>
</svg>
```

**함정**: **아크는 노드 원 *뒤*가 아니라 사이에 그린다.**
노드를 나중에 그려 z-order로 덮으면 **화살촉이 노드에 파묻혀 방향이 사라진다.**
26° 갭으로 아예 떨어뜨려야 화살표가 읽힌다.

**링 중앙은 비워두거나 사이클 이름 한 단어만.** 중앙에 아이콘·로고를 넣는 것이 전형적 장식 실패다.

---

## 3-4. 벤 다이어그램 (`venn`)

**언제**: **교집합 자체가 결론일 때만.** "기술 × 수요 × 강점 = 우리가 할 것".
**쓰지 말 것**: 겹치는 영역에 쓸 내용이 없을 때. **교집합이 빈 벤은 100% 장식이다.**
**[사실] 4원 이상은 원으로 작도 불가** → 매트릭스·표로 전환.

| 항목 | 3원 | 2원 |
|---|---|---|
| 반경 r | 140 | 170 |
| 중심 배치 | 정삼각형, 한 변 **150** (= 1.07r) | 중심거리 **170** (= r, 표준 렌즈 비율) |
| 중심 좌표 | (565,357) (715,357) (640,487) | (555,400) (725,400) |
| 채움 | `fill-opacity: 0.30`, 테두리 불투명 2px | 동일 |
| 집합명 | **원 바깥** (겹침 위에 얹지 말 것) | 동일 |
| 교집합 레이블 | 영역 안, **`--text` + 600** | 동일 |

```html
<svg width="1280" height="720" viewBox="0 0 1280 720" role="img">
  <title>우리가 할 일의 조건</title>
  <desc>기술 가능성·시장 수요·우리 강점 세 조건이 모두 겹치는 영역이 코어다.</desc>

  <!-- 겹침: fill-opacity 단독으로 동작(PPTX 안전).
       mix-blend-mode는 HTML 전용 강화 옵션 — 다크=screen, 라이트=multiply -->
  <g style="mix-blend-mode: screen">
    <circle cx="565" cy="357" r="140"
            style="fill:var(--cat-1);fill-opacity:.30;stroke:var(--cat-1);stroke-width:2"/>
    <circle cx="715" cy="357" r="140"
            style="fill:var(--cat-2);fill-opacity:.30;stroke:var(--cat-2);stroke-width:2"/>
    <circle cx="640" cy="487" r="140"
            style="fill:var(--cat-3);fill-opacity:.30;stroke:var(--cat-3);stroke-width:2"/>
  </g>

  <text class="node-label" x="415" y="268" style="font-size:20px">기술 가능성</text>
  <text class="node-label" x="865" y="268" style="font-size:20px">시장 수요</text>
  <text class="node-label" x="640" y="662" style="font-size:20px">우리 강점</text>

  <text class="region" x="640" y="322">차별화</text>
  <text class="region" x="551" y="452">실현</text>
  <text class="region" x="729" y="452">니즈</text>
  <text class="region" x="640" y="408" style="font-size:18px;font-weight:700">코어</text>
</svg>
```

**🔴 검증에서 잡은 것**: 교집합 라벨을 `--muted`로 두면 **반투명 채움 위에서 거의 안 보인다.**
→ **`--text` + weight 600 필수.** 집합명은 원 바깥으로 뺄 것.

**겹침 처리 3가지**

| 방식 | 결과 | PPTX |
|---|---|---|
| `fill-opacity:.30` 단독 | 겹칠수록 진해짐. 무난 | ✅ 안전 |
| `mix-blend-mode` (screen/multiply) | 색 혼합 정확. 가장 예쁨 | ⚠️ 소실 → 래스터화 |
| `<clipPath>`로 교집합을 별도 도형 작도 | 영역별 개별 색 가능 | ✅ 안전, 코드량 3배 |

→ **기본은 `fill-opacity` 단독.** 블렌드는 HTML 전용 슬라이드에서만.

**벤 색상 주의**: 벤은 3색을 쓰므로 `--accent` 단색 팔레트를 벗어나는 **유일한 도해**다.
팔레트에 **`--cat-1/2/3`(범주색)을 정의**해두고 그것만 쓸 것.
임의 헥스를 인라인으로 박으면 테마 전환 시 깨진다.

---

## 3-5. 레이어 아키텍처 (`arch`)

**언제**: 구성요소 + 경계 + 의존 방향. "무엇으로 이뤄져 있나".
**쓰지 말 것**: 요소 간 관계가 계층 의존이 아니라 **시간적 순서**일 때(→ 플로우).

| 항목 | 값 |
|---|---|
| 레이어 | 3 (기본), 4 상한. **위=사용자에 가까움, 아래=인프라** |
| 컨테이너 | x=64, w=944(레일 있을 때) / 1152(없을 때), h=112, r=12 |
| 레이어 y | 176 / 328 / 480 (간격 152 = 112 + 갭 40) |
| 캡션 | 좌상단, 13px/700, letter-spacing .08em, `--muted`, 대문자 |
| 요소 칩 | h=52, r=8, 간격 24 |
| **레이어 간 연결** | **수직 화살표 1개** (요소마다 그으면 교차 지옥) |
| 횡단 관심사 | 우측 세로 레일, **점선 테두리** |

```html
<svg width="1280" height="720" viewBox="0 0 1280 720" role="img">
  <title>시스템 구성</title>
  <desc>인터페이스·오케스트레이션·런타임 3계층이며, brain 메모리가 전 계층을 횡단한다.</desc>
  <defs>
    <marker id="arrow-a" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto" markerUnits="strokeWidth">
      <path d="M 0 0 L 10 5 L 0 10 z" style="fill: var(--muted)"/>
    </marker>
  </defs>

  <g>
    <rect x="64" y="176" width="944" height="112" rx="12"
          style="fill:var(--surface);stroke:var(--border);stroke-width:1.5"/>
    <text x="88" y="204"
          style="fill:var(--muted);font-size:13px;font-weight:700;letter-spacing:.08em">INTERFACE</text>
    <rect x="88" y="216" width="280" height="52" rx="8"
          style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.5"/>
    <text class="node-label" x="228" y="243" style="font-size:18px">Discord Bot</text>
    <rect x="392" y="216" width="280" height="52" rx="8"
          style="fill:var(--bg);stroke:var(--border);stroke-width:1.5"/>
    <text class="node-label" x="532" y="243" style="font-size:18px">CLI</text>
    <rect x="696" y="216" width="288" height="52" rx="8"
          style="fill:var(--bg);stroke:var(--border);stroke-width:1.5"/>
    <text class="node-label" x="840" y="243" style="font-size:18px">Cron</text>
  </g>

  <g>
    <rect x="64" y="328" width="944" height="112" rx="12"
          style="fill:var(--surface);stroke:var(--border);stroke-width:1.5"/>
    <text x="88" y="356"
          style="fill:var(--muted);font-size:13px;font-weight:700;letter-spacing:.08em">ORCHESTRATION</text>
    <rect x="88" y="368" width="280" height="52" rx="8"
          style="fill:var(--bg);stroke:var(--border);stroke-width:1.5"/>
    <text class="node-label" x="228" y="395" style="font-size:18px">총괄 에이전트</text>
    <rect x="392" y="368" width="592" height="52" rx="8"
          style="fill:var(--bg);stroke:var(--border);stroke-width:1.5"/>
    <text class="node-label" x="688" y="395" style="font-size:18px">yt-* 서브에이전트 풀</text>
  </g>

  <g>
    <rect x="64" y="480" width="944" height="112" rx="12"
          style="fill:var(--surface);stroke:var(--border);stroke-width:1.5"/>
    <text x="88" y="508"
          style="fill:var(--muted);font-size:13px;font-weight:700;letter-spacing:.08em">RUNTIME</text>
    <rect x="88" y="520" width="280" height="52" rx="8"
          style="fill:var(--bg);stroke:var(--border);stroke-width:1.5"/>
    <text class="node-label" x="228" y="547" style="font-size:18px">ComfyUI / TTS</text>
    <rect x="392" y="520" width="280" height="52" rx="8"
          style="fill:var(--bg);stroke:var(--border);stroke-width:1.5"/>
    <text class="node-label" x="532" y="547" style="font-size:18px">Remotion</text>
    <rect x="696" y="520" width="288" height="52" rx="8"
          style="fill:var(--bg);stroke:var(--border);stroke-width:1.5"/>
    <text class="node-label" x="840" y="547" style="font-size:18px">ffmpeg</text>
  </g>

  <!-- 레이어 간 의존: 딱 1개씩 -->
  <line class="conn" x1="536" y1="288" x2="536" y2="320" marker-end="url(#arrow-a)"/>
  <line class="conn" x1="536" y1="440" x2="536" y2="472" marker-end="url(#arrow-a)"/>

  <!-- 횡단 관심사 레일 -->
  <rect x="1040" y="176" width="176" height="416" rx="12"
        style="fill:none;stroke:var(--border);stroke-width:1.5;stroke-dasharray:6 5"/>
  <text class="node-label" x="1128" y="360" style="font-size:17px;fill:var(--muted)">brain</text>
  <text class="node-sub"   x="1128" y="386">메모리 · 지식</text>
  <line class="conn" x1="1008" y1="232" x2="1032" y2="232" marker-end="url(#arrow-a)"/>
  <line class="conn" x1="1008" y1="384" x2="1032" y2="384" marker-end="url(#arrow-a)"/>
  <line class="conn" x1="1008" y1="536" x2="1032" y2="536" marker-end="url(#arrow-a)"/>
</svg>
```

---

## 4. 도해가 실패하는 패턴

### 4-1. 장식적 vs 설명적 — 판별 3문항

셋 다 통과해야 **설명적(explanatory)**이다:
1. **삭제 테스트**: 도해를 지우면 잃는 정보가 있는가? (없으면 장식)
2. **구조 테스트**: 도해의 **공간 배치**가 의미를 나르는가?
   상자 안 글씨만 읽어도 똑같다면 **상자는 무의미**하다
3. **화살표 테스트**: 화살표를 뒤집으면 틀린 말이 되는가? (안 되면 **거짓 구조**)

### 4-2. 빈발 실패 카탈로그

| 실패 | 증상 | 처방 |
|---|---|---|
| **리스트 세탁** | 순서 없는 항목 4개를 화살표로 이어붙임 | 화살표 제거 → 그리드 카드 또는 텍스트 |
| **빈 교집합 벤** | 겹침 영역에 라벨이 없음 | 벤 폐기 → 표 |
| **의미 없는 사이클** | 실제로는 반복 안 하는 절차를 원으로 | 플로우로 전환 |
| **전선 뭉치** | 선 교차 3개 이상 | 노드 재배치 → 안 되면 분할 [Purchase 실증] |
| **범례 의존** | 색·모양의 의미를 별도 범례에서 찾아야 함 | 라벨을 대상에 직접 [d=0.79] |
| **강조 인플레** | accent가 노드 절반에 칠해짐 | 강조 1개 원칙 [d=0.46] |
| **3D·그림자 과다** | 깊이가 의미가 아닌데 3D | 평면화 |
| **아이콘 나열** | 예쁜 아이콘만 있고 구조는 없음 | 유혹적 세부(seductive details) — 제거 |
| **애니메이션 대체** | 정적으로 못 보여줄 걸 애니로 때움 | **정적으로 못 그리면 도해 설계가 틀린 것** |

### 4-3. "장식은 무조건 악"은 과장이다

Tufte의 data-ink ratio는 널리 인용되지만 **실증적으로 반박된 부분이 있다.**
Bateman et al. *"Useful Junk?"* (CHI 2010): 시각적 장식이 들어간 차트가
메시지 전달과 **3주 후 회상**에서 미니멀 차트보다 나았다. [실증]

**우리의 결론**: 금지 대상은 "장식" 자체가 아니라 **구조를 왜곡하거나 없는 구조를 암시하는 장식**이다.
- ❌ 금지: 가짜 화살표, 가짜 위계, 3D 왜곡, 무관한 아이콘, 의미 없는 색 (= **잘못된 구조 신호**)
- ✅ 허용: 단계 번호 배지, 부드러운 모서리, 미묘한 그림자, accent 강조 (= **구조를 강화하는 요소**)

---

## 5. PPTX 내보내기 제약

| SVG 기능 | PPTX | 대응 |
|---|---|---|
| `<rect>`, `<circle>`, `<line>`, 단순 `<path>` | 네이티브 도형 매핑 가능 | 그대로 사용 |
| **`<marker>` 화살촉** | **표준 매핑 없음** — 소실 위험 | 도해를 **하나의 SVG로 두고 이미지로 임베드** |
| `mix-blend-mode` | 소실 | `fill-opacity`로 대체 |
| `<linearGradient>` | pptxgenjs 미지원 | 래스터 PNG로 대체 |
| `dominant-baseline` | 변환기별 처리 상이 → 수직 위치 틀어짐 | PPTX 경로에선 `y` 직접 조정 |

**권장 정책**: 도해는 `<svg>` 하나로 **자기완결**하게 만들고,
PPTX 내보내기 시 **도해 단위로 통째 래스터화(2× DPI PNG) + alt 텍스트 부여.**
도해 내부 도형을 개별 편집 가능하게 만들려는 시도는 **비용 대비 이득이 낮다.**

**접근성**: 각 `<svg>`에 `role="img"` + `<title>` + `<desc>`(한 문장 요약)를 넣는다.
**이 `<desc>` 문장은 §0 게이트 2의 "한 문장 테스트" 답과 동일해야 한다** — 못 쓰겠으면 도해가 틀린 것이다.

---

## 6. 체크리스트 (생성 전 게이트)

1. [ ] §1 결정표에서 유형이 **하나로** 정해지는가? (둘 이상 → 내용이 섞임 → 슬라이드 분할)
2. [ ] 노드 ≤5 (트리는 ≤12)? 초과 시 그룹핑해 접었는가?
3. [ ] **선 교차 = 0**인가?
4. [ ] 방향이 좌→우 **또는** 위→아래 하나로 통일됐는가? 되먹임은 점선인가?
5. [ ] 화살표가 있다면 **뒤집으면 틀린 말이 되는가?**
6. [ ] 강조(`--accent`) 노드가 **정확히 1개**인가?
7. [ ] **범례 없이** 라벨이 대상에 붙어 있는가?
8. [ ] 모든 좌표가 8의 배수, 안전영역(64/48) 안인가?
9. [ ] 색을 **`style=`/클래스**로 넣었는가? (프레젠테이션 속성 `fill="var(...)"` ✕)
10. [ ] `<desc>` 한 문장을 쓸 수 있는가?

---

## 출처

- [Dan Roam — The Back of the Napkin (6W 프레임워크)](https://readingraphics.com/book-summary-the-back-of-the-napkin/)
- [Microsoft — Choose a SmartArt graphic](https://support.microsoft.com/en-us/office/choose-a-smartart-graphic-e9a7a134-f8a5-4251-aba2-93f96b88644d)
- [Cowan (2001) — The magical number 4 in short-term memory](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/44023F1147D4A1D44BDC0AD226838496/S0140525X01003922a.pdf/the-magical-number-4-in-short-term-memory-a-reconsideration-of-mental-storage-capacity.pdf) · [Miller 7±2 재검토](https://pmc.ncbi.nlm.nih.gov/articles/PMC4486516/)
- [Purchase — Effective information visualisation: graph drawing aesthetics](https://www.sciencedirect.com/science/article/abs/pii/S0953543800000321) · [Validating Graph Drawing Aesthetics (PDF)](https://scispace.com/pdf/validating-graph-drawing-aesthetics-50bm3hv9u5.pdf)
- [Mayer — Principles for Reducing Extraneous Processing (PDF)](https://edtechuvic.ca/wp-content/uploads/sites/11/2022/09/principles-for-reducing-extraneous-processing-in-multimedia-learning-coherence-signaling-redundancy-spatial-contiguity-and-temporal-contiguity-principles.pdf)
- [Tversky, Morrison & Bétrancourt — Animation: can it facilitate? (PDF)](https://hci.stanford.edu/courses/cs448b/papers/Tversky_AnimationFacilitate_IJHCS02.pdf)
- [Bateman et al. — Useful Junk? (CHI 2010, PDF)](https://vis.csail.mit.edu/classes/6.859/readings/pdfs/Bateman-UsefulJunk.pdf) · [The Chartjunk Debate (Few)](https://www.perceptualedge.com/articles/visual_business_intelligence/the_chartjunk_debate.pdf)
- [MDN — SVG `<marker>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/marker) · [MDN — `fill`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill) · [W3C SVG WG — var() in presentation attributes](https://lists.w3.org/Archives/Public/public-svg-issues/2025Nov/0024.html)
- [Venn diagram — 4집합 원 작도 불가 (Wikipedia)](https://en.wikipedia.org/wiki/Venn_diagram)
- [PptxGenJS 문서](https://gitbrent.github.io/PptxGenJS/)
