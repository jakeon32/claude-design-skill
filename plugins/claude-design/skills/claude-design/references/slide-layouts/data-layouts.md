---
name: data-layouts
description: "슬라이드 데이터/차트 레이아웃 템플릿 — Bar/Column, Line, 100% Stacked Bar, Donut(조건부), Funnel, Timeline, 2×2 Matrix. 값→픽셀 환산은 tools/chart_scale.js 필수 경유. Venn은 diagram-layouts.md로 이동."
---

# Data / Chart Layouts

차트는 SVG 또는 CSS로 HTML 내 직접 구현. 외부 라이브러리 최소화.

> ## 🔴 2026-07-14 정정 — 이 문서는 두 가지 거짓말을 하고 있었다
>
> 1. **frontmatter가 "Venn"을 있다고 적어놨는데 본문에 없었다.**
>    → Venn은 [`diagram-layouts.md`](diagram-layouts.md#3-4-벤-다이어그램-venn)에 신설(2~3원).
>    카탈로그가 등재했던 Pie/Donut·Scatter·Key Metrics도 실체가 없었다.
> 2. **막대 템플릿에 `height:240px /* 값에 따라 조정 */`이라고만 적혀 있었다.**
>    값→픽셀 환산 규칙이 없으니 **AI가 눈대중으로 막대를 그렸다.** 데이터와 그림이 안 맞을 수 있었다.

## ★ 모든 차트는 스케일 계산을 먼저 거친다 — 픽셀 하드코딩 금지

```js
const { niceScale, valueToPx, valueToPct, assertChart } = require('tools/chart_scale.js');

// 1) 축 확정 — 데이터 최댓값이 아니라 "예쁜 수"로 올림한다
const s = niceScale(0, Math.max(...data.map(d => d.value)));   // 86 → 축 0~100, step 20

// 2) 값 → 픽셀. 🔴 정규화 기준은 scale.max (dataMax 아님)
const px = valueToPx(v, s, PLOT_H);        // SVG
const pct = valueToPct(v, s);              // HTML/CSS (%)

// 3) 렌더 전 검증 — 값 비율 ≠ 픽셀 비율이면 에러
assertChart(data, s, rendered);
```

**흔한 오류 3가지**
1. `v / dataMax * H` — 최대 막대가 항상 천장에 닿아 **축 눈금과 어긋난다.** 반드시 `scale.max` 기준
2. `<g transform="scale(1,-1)">`로 y축 뒤집기 — **텍스트까지 뒤집힌다.** 좌표 계산으로만 뒤집을 것
3. 반올림 누적 — tick 좌표와 막대 상단이 1~2px 어긋난다. `Math.round()`는 최종 출력 직전 한 번만

**공통 원칙**
- Visual (차트 영역): 70%+
- **차트 제목은 서술형 메시지** (IBCS SAY) — "분기별 매출" ✕ → **"매출 3분기 연속 감소"** ○
- 값 라벨을 막대 끝에 직접 표기하면 **격자선·축 눈금을 제거할 수 있다** (IBCS CONDENSE)
- **차트 정크 금지**: 3D · 그림자 · 그라디언트 · 이중 축 · 막대 사이 세로 격자선 · `border-radius > 2px`
- **색은 편차(빨강/초록)에만.** 실적/계획/예측은 색이 아니라 **채우기 패턴**으로 구분 (IBCS 시나리오)
- 계열 색은 **Okabe-Ito 팔레트**(색맹 대응, `chart_scale.js`의 `SERIES`)

---

## Bar / Column Chart

세로 막대(Column) 또는 가로 막대(Bar) 그래프.

**하드 룰**
- **Y축은 반드시 0에서 시작한다. 예외 없음.** 막대는 *길이*로 값을 인코딩하므로
  축을 자르면 길이 비율 자체가 거짓이 된다. (라인 차트는 예외 허용 — 위치로 인코딩하므로)
- **정렬**: 순서에 의미 없으면(제품·지역) **값 내림차순**. 의미 있으면(시간·연령) **자연 순서 유지**
- **가로 막대(Bar)** = 라벨이 길거나 항목이 많을 때 / **세로 막대(Column)** = 시간축
- **막대 두께 대 간격**: `gap = barW × 0.3` (범위 0.2~0.4). `barGeometry()`가 계산해준다

### Column Chart (세로 막대)

```html
<!-- [Column Chart] CSS Bar Chart -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <!-- 헤더 -->
  <div style="flex-shrink:0; padding:44px 80px 24px;">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">[차트 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:16px;
      color:var(--muted); margin-top:8px;
    ">[차트 설명 — 출처 또는 단위]</p>
  </div>
  <!-- 차트 영역 -->
  <div style="
    flex:1; padding:0 80px 56px; min-height:0;
    display:flex; flex-direction:column;
  ">
    <!-- 차트 컨테이너 -->
    <div style="
      flex:1; display:flex; align-items:flex-end; gap:20px;
      border-bottom:2px solid var(--border);
      padding-bottom:0; min-height:0;
    ">
      <!-- 🔴 막대 높이는 절대 손으로 적지 않는다.
           height는 valueToPct(v, s) 결과를 % 로 넣는다 (컨테이너 기준 = 축 최댓값).
           옛 버전의 `height:240px /* 값에 따라 조정 */` 이 눈대중 렌더의 원인이었다. -->
      <!-- 막대 1 -->
      <div style="
        flex:1; display:flex; flex-direction:column;
        align-items:center; justify-content:flex-end; gap:8px; height:100%;
      ">
        <p style="
          font-family:var(--h-font); font-size:24px; font-weight:700;
          color:var(--text); font-variant-numeric:tabular-nums;
        ">42</p>
        <div style="
          width:100%; background:var(--accent);
          height:42%;            /* ← valueToPct(42, s) — s.max=100 이면 42% */
        "></div>
      </div>
      <!-- 막대 2 -->
      <div style="
        flex:1; display:flex; flex-direction:column;
        align-items:center; justify-content:flex-end; gap:8px; height:100%;
      ">
        <p style="
          font-family:var(--h-font); font-size:24px; font-weight:700;
          color:var(--text); font-variant-numeric:tabular-nums;
        ">28</p>
        <div style="
          width:100%; background:var(--secondary);
          height:28%;            /* ← valueToPct(28, s) */
        "></div>
      </div>
      <!-- 추가 막대... -->
    </div>
    <!-- X축 레이블 -->
    <div style="
      display:flex; gap:20px; padding-top:12px;
    ">
      <p style="
        flex:1; text-align:center;
        font-family:var(--b-font); font-size:14px;
        color:var(--muted);
      ">[카테고리 1]</p>
      <p style="
        flex:1; text-align:center;
        font-family:var(--b-font); font-size:14px;
        color:var(--muted);
      ">[카테고리 2]</p>
    </div>
  </div>
</section>
```

### Bar Chart (가로 막대) — 순위 비교 ★ 권장 형태

**폭을 `%`로 내보내면 컨테이너 크기와 무관하게 항상 정확하다.**
`width`는 반드시 `valueToPct(v, s)`로 계산한다 — **직접 적지 마라.**

```js
// 생성기: 눈대중이 불가능한 구조
const s = niceScale(0, Math.max(...data.map(d => d.value)));   // 축 확정
const rows = [...data].sort((a, b) => b.value - a.value).map(d => {
  const pct = valueToPct(d.value, s);          // ← 여기가 유일한 환산 지점
  return `<div class="row">
    <div class="lbl">${d.label}</div>
    <div class="track"><div class="bar" style="width:${pct.toFixed(2)}%"></div></div>
    <div class="val">${fmt(d.value, s)}</div>
  </div>`;
}).join('');
```

```css
/* barThickness 28px, gap 8px ≈ 0.29 비율 (하드 룰 준수) */
.chart { width: 1000px; }
.row   { display: grid; grid-template-columns: 200px 1fr 90px;
         align-items: center; column-gap: 16px; margin-bottom: 8px; }
.lbl   { font-size: 24px; color: var(--text); text-align: right;      /* ≥24px */
         white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.track { position: relative; height: 28px; }        /* 100% = 축 최댓값 */
.bar   { height: 28px; background: var(--accent); } /* 그라디언트·라운드 금지 */
.val   { font-size: 24px; font-weight: 600; color: var(--text);
         font-variant-numeric: tabular-nums; }
```

```html
<!-- [Bar Chart] Horizontal Bars -->
<section class="slide" data-density="D2" style="
  display:flex; flex-direction:column; background:var(--bg); overflow:hidden;
">
  <!-- Action Title — 결론을 문장으로 -->
  <div style="flex-shrink:0; padding:40px 64px 24px;">
    <p style="font-family:var(--h-font); font-size:40px; font-weight:700;
              color:var(--text); line-height:1.22; letter-spacing:-0.02em;">
      백본 포맷이 뉴스형보다 3배 이상 조회된다
    </p>
    <p style="font-family:var(--b-font); font-size:20px; color:var(--muted); margin-top:8px;">
      24시간 조회수 (회)
    </p>
  </div>

  <!-- 차트 — 위 생성기가 만든 .chart 를 삽입 -->
  <div style="flex:1; padding:0 64px; min-height:0; display:flex; align-items:center;">
    <div class="chart" data-axis-max="[s.max]">
      <!-- rows -->
    </div>
  </div>

  <div style="flex-shrink:0; padding:0 64px 20px;">
    <p style="font-family:var(--b-font); font-size:17px; color:var(--muted);">
      Source: YouTube Data API (2026-07)
    </p>
  </div>
</section>
```

---

## Line Chart

추이·트렌드 강조. SVG로 구현.

```html
<!-- [Line Chart] SVG Line Graph -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <div style="flex-shrink:0; padding:44px 80px 24px;">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">[차트 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:16px;
      color:var(--muted); margin-top:8px;
    ">[기간 / 단위]</p>
  </div>
  <!-- SVG 차트 -->
  <div style="flex:1; padding:0 80px 56px; min-height:0;">
    <svg width="100%" height="100%" viewBox="0 0 1000 400" preserveAspectRatio="xMidYMid meet">
      <!-- 배경 그리드 -->
      <line x1="0" y1="100" x2="1000" y2="100" stroke="var(--border)" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="0" y1="200" x2="1000" y2="200" stroke="var(--border)" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="0" y1="300" x2="1000" y2="300" stroke="var(--border)" stroke-width="1" stroke-dasharray="4,4"/>
      <!-- 라인 (accent 색상) -->
      <polyline
        points="0,300 166,250 333,180 500,220 666,140 833,80 1000,100"
        fill="none"
        stroke="var(--accent)"
        stroke-width="3"
        stroke-linejoin="round"
      />
      <!-- Area fill (선택) -->
      <polygon
        points="0,300 166,250 333,180 500,220 666,140 833,80 1000,100 1000,400 0,400"
        fill="var(--accent)"
        opacity="0.08"
      />
      <!-- 데이터 포인트 -->
      <circle cx="333" cy="180" r="6" fill="var(--accent)"/>
      <circle cx="1000" cy="100" r="6" fill="var(--accent)"/>
      <!-- X축 레이블 -->
      <text x="0" y="390" font-size="14" fill="var(--muted)" font-family="var(--b-font)">Q1</text>
      <text x="166" y="390" font-size="14" fill="var(--muted)" font-family="var(--b-font)">Q2</text>
      <text x="333" y="390" font-size="14" fill="var(--muted)" font-family="var(--b-font)">Q3</text>
      <text x="500" y="390" font-size="14" fill="var(--muted)" font-family="var(--b-font)">Q4</text>
    </svg>
  </div>
</section>
```

---

## 100% Stacked Bar

> **★ 2026-07-14 신설 — 이 스킬에는 "구성(부분→전체)"을 표현할 수단이 아예 없었다.**
> 파이도 누적막대도 없어서 **구성 데이터가 일반 막대로 잘못 흘러갔다.**
> 부분-전체는 이 템플릿이 기본값이다. (파이는 조건부 예외 — 아래 Donut 참조)

**언제**: 부분 → 전체 구성. 항목 4~8개. 시간에 따른 구성 변화(누적 컬럼).
**왜 파이보다 나은가**: 길이로 인코딩하므로 **각도보다 정확하다**
(Cleveland & McGill 지각 정확도 순위: 위치 > 길이 > **각도** > 면적).

```js
// 각 조각의 폭 = 값 / 합계 × 100%  (여기선 축 스케일이 아니라 합계 기준)
const total = data.reduce((a, d) => a + d.value, 0);
const segs = data.map((d, i) => ({
  ...d,
  pct: d.value / total * 100,
  color: SERIES[i],                      // Okabe-Ito (색맹 대응)
}));
```

```html
<section class="slide" data-density="D2" style="
  display:flex; flex-direction:column; background:var(--bg); overflow:hidden;
">
  <div style="flex-shrink:0; padding:40px 64px 24px;">
    <p style="font-family:var(--h-font); font-size:40px; font-weight:700;
              color:var(--text); line-height:1.22;">
      제작 시간의 절반이 렌더에 쓰인다
    </p>
  </div>

  <div style="flex:1; padding:0 64px; min-height:0; display:flex;
              flex-direction:column; justify-content:center; gap:32px;">
    <!-- 누적 바 — 각 조각 width = pct -->
    <div style="display:flex; width:100%; height:88px; overflow:hidden; border-radius:2px;">
      <div style="width:48.0%; background:#0072B2; display:flex; align-items:center;
                  justify-content:center; color:#fff; font-size:24px; font-weight:700;">48%</div>
      <div style="width:27.0%; background:#E69F00; display:flex; align-items:center;
                  justify-content:center; color:#fff; font-size:24px; font-weight:700;">27%</div>
      <div style="width:15.0%; background:#009E73; display:flex; align-items:center;
                  justify-content:center; color:#fff; font-size:24px; font-weight:700;">15%</div>
      <div style="width:10.0%; background:#CC79A7; display:flex; align-items:center;
                  justify-content:center; color:#fff; font-size:22px; font-weight:700;">10%</div>
    </div>

    <!-- 라벨은 조각 아래 직접 배치 — 범례 분리 금지 (공간근접 d=0.79) -->
    <div style="display:flex; width:100%;">
      <div style="width:48%; font-size:22px; color:var(--text);">렌더</div>
      <div style="width:27%; font-size:22px; color:var(--text);">이미지</div>
      <div style="width:15%; font-size:22px; color:var(--text);">TTS</div>
      <div style="width:10%; font-size:22px; color:var(--muted);">기타</div>
    </div>
  </div>

  <div style="flex-shrink:0; padding:0 64px 20px;">
    <p style="font-family:var(--b-font); font-size:17px; color:var(--muted);">
      Source: 파이프라인 로그 (n=48편)
    </p>
  </div>
</section>
```

**규칙**
- 조각은 **큰 것부터** 왼쪽에 (단, 시계열·자연 순서는 유지)
- **"기타"는 항상 마지막**, 회색(`--muted`)
- 조각이 **5% 미만이면 라벨이 안 들어간다** → "기타"로 묶거나 리더선 사용
- 두 개 이상의 누적 바를 비교할 땐 **기준선(맨 왼쪽)을 정렬**해야 첫 조각끼리 비교된다

---

## Donut Chart

> ## ⚠️ 조건부 허용 — 기본값은 "쓰지 않는다"
>
> **IBCS는 파이/도넛을 "Bottom 1(최악의 시각화)"로 명시 지목한다.**
> 파이는 각도로 값을 인코딩하는데, Cleveland & McGill(1984) 지각 정확도 순위에서
> **각도는 공통 축 위의 위치·길이보다 명백히 부정확**하다.
> Stephen Few: 파이는 0/25/50/75/100% 근처에서만 크기 판단이 쉽다.

**허용 조건 — 아래를 전부 만족할 때만:**
```
1. 항목 수 ≤ 3  (도넛 중앙에 KPI를 넣으면 ≤ 2 + '기타')
2. 합계 = 100%  (부분-전체)
3. 정확한 비교가 목적이 아님 (근사 인상만 전달)
4. 각 조각에 % 값 라벨 직접 표기
그 외 전부 → 100% Stacked Bar 또는 정렬된 Bar Chart로 대체
```
**절대 금지**: 3D 파이 · 분리(exploded) 조각 · 조각 5개 초과 · **두 파이를 나란히 비교**

**각도 공식** (눈대중 금지)
```js
const total = values.reduce((a, b) => a + b, 0);
let a0 = -Math.PI / 2;                          // 12시 방향에서 시작
const arcs = values.map(v => {
  const a1 = a0 + (v / total) * 2 * Math.PI;    // 값에 비례한 각도
  const seg = { v, a0, a1, pct: v / total * 100 };
  a0 = a1;
  return seg;
});

const pt = (cx, cy, r, a) => [cx + r * Math.cos(a), cy + r * Math.sin(a)];

/** rInner > 0 이면 도넛 */
function arcPath(cx, cy, rOuter, rInner, a0, a1) {
  const large = (a1 - a0) > Math.PI ? 1 : 0;
  const [x0, y0] = pt(cx, cy, rOuter, a0), [x1, y1] = pt(cx, cy, rOuter, a1);
  const [x2, y2] = pt(cx, cy, rInner, a1), [x3, y3] = pt(cx, cy, rInner, a0);
  return `M${x0},${y0} A${rOuter},${rOuter} 0 ${large} 1 ${x1},${y1}
          L${x2},${y2} A${rInner},${rInner} 0 ${large} 0 ${x3},${y3} Z`;
}
```

---

## Funnel

단계별 줄어드는 흐름. CSS clip-path 사용.

> **규칙**: **면적이 아니라 폭으로 값을 인코딩한다.**
> 사다리꼴 면적으로 인코딩하면 값이 왜곡된다(면적은 폭의 제곱에 가깝게 증가).
> 단계별 % 라벨 필수.

```html
<!-- [Funnel Chart] CSS Funnel -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row; align-items:center;
  background:var(--bg); overflow:hidden; padding:0 80px;
">
  <!-- 좌: 제목 (30%) -->
  <div style="flex:0 0 360px; padding-right:48px;">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); line-height:1.15; letter-spacing:-0.02em;
    ">[차트 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:16px;
      color:var(--muted); margin-top:16px;
    ">[설명]</p>
  </div>
  <!-- 우: 퍼널 (70%) -->
  <div style="flex:1; display:flex; flex-direction:column; gap:6px; align-items:stretch;">
    <!-- 단계 1 (최대 너비) -->
    <div style="
      display:flex; align-items:center;
      background:var(--accent); border-radius:4px;
      padding:16px 24px; width:100%;
    ">
      <p style="
        font-family:var(--b-font); font-size:15px; font-weight:600;
        color:#fff; flex:1;
      ">[단계 1 — 인지]</p>
      <p style="
        font-family:var(--h-font); font-size:22px; font-weight:700;
        color:#fff;
      ">10,000</p>
    </div>
    <!-- 단계 2 (80% 너비) -->
    <div style="
      display:flex; align-items:center; align-self:center;
      background:var(--secondary); border-radius:4px;
      padding:16px 24px; width:80%;
    ">
      <p style="
        font-family:var(--b-font); font-size:15px; font-weight:600;
        color:var(--text); flex:1;
      ">[단계 2 — 관심]</p>
      <p style="
        font-family:var(--h-font); font-size:22px; font-weight:700;
        color:var(--text);
      ">6,500</p>
    </div>
    <!-- 단계 3 (60%), 4 (40%), 5 (25%) 동일 패턴 -->
    <div style="
      display:flex; align-items:center; align-self:center;
      background:var(--surface); border-radius:4px;
      padding:16px 24px; width:60%;
      border:1px solid var(--border);
    ">
      <p style="
        font-family:var(--b-font); font-size:15px; font-weight:600;
        color:var(--text); flex:1;
      ">[단계 3 — 전환]</p>
      <p style="
        font-family:var(--h-font); font-size:22px; font-weight:700;
        color:var(--accent);
      ">1,200</p>
    </div>
  </div>
</section>
```

---

## Horizontal Timeline

가로 흐름, 날짜 기반 마일스톤. 최대 5단계.

```html
<!-- [Horizontal Timeline] -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <!-- 헤더 -->
  <div style="flex-shrink:0; padding:44px 80px 0;">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">[타임라인 제목]</p>
  </div>
  <!-- 타임라인 -->
  <div style="
    flex:1; display:flex; align-items:center;
    padding:0 80px 64px;
  ">
    <!-- 전체 가로 라인 -->
    <div style="position:relative; width:100%;">
      <!-- 연결 라인 -->
      <div style="
        position:absolute; top:28px; left:28px; right:28px;
        height:2px; background:var(--border);
      "></div>
      <!-- 단계 컨테이너 -->
      <div style="
        display:flex; justify-content:space-between;
        position:relative; z-index:1;
      ">
        <!-- 단계 1 -->
        <div style="
          display:flex; flex-direction:column;
          align-items:center; gap:16px; max-width:180px;
        ">
          <!-- 원형 마커 -->
          <div style="
            width:56px; height:56px; border-radius:50%;
            background:var(--accent);
            display:flex; align-items:center; justify-content:center;
            font-family:var(--h-font); font-size:20px; font-weight:700;
            color:#fff;
          ">1</div>
          <!-- 날짜 -->
          <p style="
            font-family:var(--b-font); font-size:13px;
            color:var(--accent); letter-spacing:0.05em;
            text-align:center;
          ">2024 Q1</p>
          <!-- 설명 -->
          <p style="
            font-family:var(--h-font); font-size:17px; font-weight:600;
            color:var(--text); text-align:center;
          ">[마일스톤 제목]</p>
          <p style="
            font-family:var(--b-font); font-size:13px;
            color:var(--muted); text-align:center; line-height:1.5;
          ">[짧은 설명]</p>
        </div>
        <!-- 단계 2, 3, 4, 5 동일 구조 (미완료는 마커 색상: var(--border)) -->
        <div style="
          display:flex; flex-direction:column;
          align-items:center; gap:16px; max-width:180px;
        ">
          <div style="
            width:56px; height:56px; border-radius:50%;
            background:var(--surface); border:2px solid var(--border);
            display:flex; align-items:center; justify-content:center;
            font-family:var(--h-font); font-size:20px; font-weight:700;
            color:var(--muted);
          ">2</div>
          <p style="
            font-family:var(--b-font); font-size:13px;
            color:var(--muted); letter-spacing:0.05em;
            text-align:center;
          ">2024 Q2</p>
          <p style="
            font-family:var(--h-font); font-size:17px; font-weight:600;
            color:var(--text); text-align:center;
          ">[마일스톤 제목]</p>
          <p style="
            font-family:var(--b-font); font-size:13px;
            color:var(--muted); text-align:center; line-height:1.5;
          ">[짧은 설명]</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## 2×2 Matrix

포지셔닝 매트릭스. X축/Y축 기준 4사분면.

```html
<!-- [2×2 Matrix] Positioning Matrix -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row;
  background:var(--bg); overflow:hidden;
">
  <!-- 좌: 제목 (28%) -->
  <div style="
    flex:0 0 340px; display:flex; flex-direction:column;
    justify-content:center; padding:64px 40px 64px 80px;
  ">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); line-height:1.15; letter-spacing:-0.02em;
    ">[매트릭스 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:16px;
      color:var(--muted); margin-top:16px;
    ">[설명]</p>
  </div>
  <!-- 우: 매트릭스 (72%) -->
  <div style="
    flex:1; display:flex; flex-direction:column;
    padding:48px 80px 48px 40px;
  ">
    <!-- Y축 레이블 -->
    <div style="
      display:flex; justify-content:space-between;
      padding:0 0 8px;
    ">
      <p style="
        font-family:var(--b-font); font-size:13px;
        color:var(--muted); letter-spacing:0.05em;
        text-transform:uppercase;
      ">HIGH [Y축명]</p>
    </div>
    <!-- 4사분면 -->
    <div style="
      flex:1; display:flex; flex-wrap:wrap; gap:4px; min-height:0;
    ">
      <!-- 2사분면 (좌상) -->
      <div style="
        flex:0 0 calc(50% - 2px); background:var(--surface);
        border-radius:8px 0 0 0; padding:24px;
        display:flex; flex-direction:column;
      ">
        <p style="
          font-family:var(--b-font); font-size:12px;
          color:var(--muted); letter-spacing:0.06em;
          text-transform:uppercase; margin-bottom:12px;
        ">Question Mark</p>
        <!-- 아이템 점 찍기 -->
        <p style="
          font-family:var(--b-font); font-size:15px;
          color:var(--text);
        ">• [항목 이름]</p>
      </div>
      <!-- 1사분면 (우상 — 이상적 위치) -->
      <div style="
        flex:0 0 calc(50% - 2px); background:rgba(var(--accent-rgb),0.12);
        border-radius:0 8px 0 0; padding:24px;
        border:1.5px solid var(--accent);
      ">
        <p style="
          font-family:var(--b-font); font-size:12px;
          color:var(--accent); letter-spacing:0.06em;
          text-transform:uppercase; margin-bottom:12px;
        ">Star ★</p>
        <p style="
          font-family:var(--b-font); font-size:15px;
          color:var(--text);
        ">• [항목 이름]</p>
      </div>
      <!-- 3사분면 (좌하), 4사분면 (우하) 동일 구조 -->
    </div>
    <!-- X축 레이블 -->
    <div style="
      display:flex; justify-content:space-between;
      padding:8px 0 0;
    ">
      <p style="
        font-family:var(--b-font); font-size:13px;
        color:var(--muted); letter-spacing:0.05em;
        text-transform:uppercase;
      ">LOW [X축명]</p>
      <p style="
        font-family:var(--b-font); font-size:13px;
        color:var(--muted); letter-spacing:0.05em;
        text-transform:uppercase;
      ">HIGH [X축명]</p>
    </div>
  </div>
</section>
```
