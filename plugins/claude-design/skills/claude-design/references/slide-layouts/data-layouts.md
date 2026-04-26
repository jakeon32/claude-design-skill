---
name: data-layouts
description: "슬라이드 데이터/차트 레이아웃 HTML 템플릿 — Bar/Column Chart, Line Chart, Funnel, Timeline, Venn, 2×2 Matrix. 모두 SVG/CSS 직접 구현."
---

# Data / Chart Layouts

차트는 SVG 또는 CSS로 HTML 내 직접 구현. 외부 라이브러리 최소화.

**공통 원칙**:
- Visual (차트 영역): 70%+
- 차트 제목 + 레이블: 최소 14px (PPTX 모드에서도 readable)
- 데이터 없는 상태: placeholder 값으로 구조만 보여줌

---

## Bar / Column Chart

세로 막대(Column) 또는 가로 막대(Bar) 그래프.

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
      <!-- 막대 1 -->
      <div style="
        flex:1; display:flex; flex-direction:column;
        align-items:center; gap:8px;
      ">
        <!-- 값 레이블 -->
        <p style="
          font-family:var(--h-font); font-size:20px; font-weight:700;
          color:var(--text);
        ">42%</p>
        <!-- 막대 -->
        <div style="
          width:100%; background:var(--accent);
          border-radius:4px 4px 0 0;
          height:240px; /* 값에 따라 조정 */
        "></div>
      </div>
      <!-- 막대 2 (더 낮은 높이 예시) -->
      <div style="flex:1; display:flex; flex-direction:column; align-items:center; gap:8px;">
        <p style="
          font-family:var(--h-font); font-size:20px; font-weight:700;
          color:var(--text);
        ">28%</p>
        <div style="
          width:100%; background:var(--secondary);
          border-radius:4px 4px 0 0; height:160px;
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

### Bar Chart (가로 막대) — 순위 비교

```html
<!-- [Bar Chart] Horizontal Bars -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row;
  background:var(--bg); overflow:hidden;
">
  <!-- 좌: 제목/설명 (30%) -->
  <div style="
    flex:0 0 360px; display:flex; flex-direction:column;
    justify-content:center; padding:64px 40px 64px 80px;
  ">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); line-height:1.15; letter-spacing:-0.02em;
    ">[차트 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:16px;
      color:var(--muted); margin-top:16px;
    ">[설명]</p>
  </div>
  <!-- 우: 가로 막대 차트 (70%) -->
  <div style="
    flex:1; display:flex; flex-direction:column;
    justify-content:center; gap:20px;
    padding:64px 80px 64px 40px;
  ">
    <!-- 행 1 -->
    <div style="display:flex; align-items:center; gap:16px;">
      <!-- 레이블 -->
      <p style="
        flex:0 0 140px; font-family:var(--b-font); font-size:15px;
        color:var(--text); text-align:right;
      ">[항목 이름]</p>
      <!-- 막대 -->
      <div style="
        flex:1; height:36px; background:var(--surface);
        border-radius:4px; overflow:hidden;
      ">
        <div style="
          width:72%; height:100%;
          background:var(--accent); border-radius:4px;
        "></div>
      </div>
      <!-- 값 -->
      <p style="
        flex:0 0 48px; font-family:var(--h-font); font-size:18px;
        font-weight:700; color:var(--text);
      ">72%</p>
    </div>
    <!-- 행 2, 3... 동일 구조 -->
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

## Funnel

단계별 줄어드는 흐름. CSS clip-path 사용.

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
