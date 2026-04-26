---
name: card-layouts
description: "슬라이드 카드/기능/팀/마무리 레이아웃 HTML 템플릿 — Feature Cards (2/3/4-col), Team Grid, Closing/CTA."
---

# Cards / Features / Closing Layouts

---

## Feature Highlight

핵심 기능 1개를 중앙에 임팩트 있게. 아이콘 + 제목 + 설명.

```html
<!-- [Feature Highlight] Single Feature Center -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  background:var(--bg); overflow:hidden; padding:80px;
  text-align:center;
">
  <!-- 아이콘 (Lucide SVG 또는 이모지 대신) -->
  <div style="
    width:80px; height:80px; border-radius:20px;
    background:var(--primary); display:flex;
    align-items:center; justify-content:center;
    margin-bottom:32px;
  ">
    <!-- SVG 아이콘 삽입 위치 -->
    <svg width="36" height="36" viewBox="0 0 24 24" fill="none"
      stroke="var(--accent)" stroke-width="2" stroke-linecap="round">
      <path d="M12 2L2 7l10 5 10-5-10-5z"/>
      <path d="M2 17l10 5 10-5"/>
      <path d="M2 12l10 5 10-5"/>
    </svg>
  </div>
  <!-- 레이블 -->
  <p style="
    font-family:var(--b-font); font-size:13px;
    color:var(--accent); letter-spacing:0.1em;
    text-transform:uppercase; margin-bottom:16px;
  ">[카테고리]</p>
  <!-- 기능명 (Hero) -->
  <p style="
    font-family:var(--h-font); font-size:64px; font-weight:700;
    color:var(--text); line-height:1.1; letter-spacing:-0.02em;
    max-width:800px;
  ">[핵심 기능명]</p>
  <!-- 설명 -->
  <p style="
    font-family:var(--b-font); font-size:20px; line-height:1.7;
    color:var(--muted); margin-top:24px; max-width:640px;
  ">[기능 설명. 2~3문장.]</p>
</section>
```

---

## Feature Cards 2-col

2개 기능을 나란히. 각 카드가 동등한 비중.

```html
<!-- [Feature Cards 2-col] -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <!-- 헤더 -->
  <div style="flex-shrink:0; padding:44px 80px 28px;">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:18px;
      color:var(--muted); margin-top:8px;
    ">[서브타이틀]</p>
  </div>
  <!-- 카드 2개 -->
  <div style="
    flex:1; display:flex; gap:24px;
    padding:0 80px 56px; min-height:0;
  ">
    <!-- 카드 1 -->
    <div style="
      flex:1; padding:36px; background:var(--surface);
      border-radius:var(--radius); display:flex; flex-direction:column;
    ">
      <!-- 아이콘 -->
      <div style="
        width:52px; height:52px; border-radius:12px;
        background:var(--primary); display:flex;
        align-items:center; justify-content:center;
        margin-bottom:24px;
      ">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none"
          stroke="var(--accent)" stroke-width="2" stroke-linecap="round">
          <rect x="3" y="3" width="18" height="18" rx="2"/>
          <path d="M3 9h18M9 21V9"/>
        </svg>
      </div>
      <p style="
        font-family:var(--h-font); font-size:28px; font-weight:700;
        color:var(--text); margin-bottom:12px;
      ">[기능 제목]</p>
      <p style="
        font-family:var(--b-font); font-size:17px; line-height:1.7;
        color:var(--muted); flex:1;
      ">[기능 설명. 3~5줄.]</p>
      <!-- 강조 수치 (선택) -->
      <div style="
        margin-top:24px; padding-top:20px;
        border-top:1px solid var(--border);
      ">
        <p style="
          font-family:var(--h-font); font-size:32px; font-weight:700;
          color:var(--accent);
        ">[수치]</p>
        <p style="
          font-family:var(--b-font); font-size:14px;
          color:var(--muted);
        ">[수치 레이블]</p>
      </div>
    </div>
    <!-- 카드 2 — 동일 구조 -->
    <div style="
      flex:1; padding:36px; background:var(--surface);
      border-radius:var(--radius); display:flex; flex-direction:column;
    ">
      <!-- ...동일 구조... -->
    </div>
  </div>
</section>
```

---

## Feature Cards 3-col

3개 기능 나열. 가장 범용적인 기능 소개 레이아웃.

```html
<!-- [Feature Cards 3-col] -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <div style="flex-shrink:0; padding:44px 80px 28px;">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
  </div>
  <div style="
    flex:1; display:flex; gap:20px;
    padding:0 80px 52px; min-height:0;
  ">
    <!-- 카드 1 (Hero — accent border) -->
    <div style="
      flex:1; padding:28px 24px; display:flex; flex-direction:column;
      background:var(--surface); border-radius:var(--radius);
      border:1.5px solid var(--accent);
    ">
      <div style="
        width:44px; height:44px; border-radius:10px;
        background:var(--primary); display:flex;
        align-items:center; justify-content:center;
        margin-bottom:20px;
      ">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
          stroke="var(--accent)" stroke-width="2">
          <path d="M5 12h14M12 5l7 7-7 7"/>
        </svg>
      </div>
      <p style="
        font-family:var(--h-font); font-size:22px; font-weight:600;
        color:var(--text); margin-bottom:10px;
      ">[기능 제목]</p>
      <p style="
        font-family:var(--b-font); font-size:15px; line-height:1.65;
        color:var(--muted); flex:1;
      ">[기능 설명. 2~4줄.]</p>
    </div>
    <!-- 카드 2 (중립 — border 없음) -->
    <div style="
      flex:1; padding:28px 24px; display:flex; flex-direction:column;
      background:var(--surface); border-radius:var(--radius);
    ">
      <div style="
        width:44px; height:44px; border-radius:10px;
        background:var(--primary); margin-bottom:20px;
      "></div>
      <p style="
        font-family:var(--h-font); font-size:22px; font-weight:600;
        color:var(--text); margin-bottom:10px;
      ">[기능 제목]</p>
      <p style="
        font-family:var(--b-font); font-size:15px; line-height:1.65;
        color:var(--muted); flex:1;
      ">[기능 설명]</p>
    </div>
    <!-- 카드 3 (중립) — 동일 구조 -->
    <div style="
      flex:1; padding:28px 24px; display:flex; flex-direction:column;
      background:var(--surface); border-radius:var(--radius);
    ">
      <div style="
        width:44px; height:44px; border-radius:10px;
        background:var(--primary); margin-bottom:20px;
      "></div>
      <p style="
        font-family:var(--h-font); font-size:22px; font-weight:600;
        color:var(--text); margin-bottom:10px;
      ">[기능 제목]</p>
      <p style="
        font-family:var(--b-font); font-size:15px; line-height:1.65;
        color:var(--muted); flex:1;
      ">[기능 설명]</p>
    </div>
  </div>
</section>
```

---

## Team Grid

팀원 소개. 2행 그리드, 최대 11명.

```html
<!-- [Team Grid] -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <div style="flex-shrink:0; padding:44px 80px 28px;">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">Team</p>
  </div>
  <!-- 팀원 그리드 (예: 5명 1행) -->
  <div style="
    flex:1; display:flex; gap:20px; align-items:center;
    padding:0 80px 56px;
  ">
    <!-- 팀원 카드 1 -->
    <div style="
      flex:1; display:flex; flex-direction:column;
      align-items:center; gap:12px;
    ">
      <!-- 프로필 이미지 -->
      <div style="
        width:100px; height:100px; border-radius:50%;
        background:var(--surface); overflow:hidden;
        border:2px solid var(--border);
      ">
        <img src="[프로필이미지URL]" style="
          width:100%; height:100%; object-fit:cover;
        ">
      </div>
      <div style="text-align:center;">
        <p style="
          font-family:var(--h-font); font-size:18px; font-weight:600;
          color:var(--text);
        ">[이름]</p>
        <p style="
          font-family:var(--b-font); font-size:14px;
          color:var(--accent); margin-top:4px;
        ">[직함]</p>
        <p style="
          font-family:var(--b-font); font-size:13px;
          color:var(--muted); margin-top:2px;
        ">[전문 분야]</p>
      </div>
    </div>
    <!-- 나머지 팀원 동일 구조 -->
  </div>
</section>
```

---

## Closing / CTA

마무리 슬라이드. 강렬한 비주얼 + 명확한 행동 유도.

### 변형 A: 솔리드 배경 + 중앙 CTA

```html
<!-- [Closing A] Solid + Center CTA -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  background:var(--primary); overflow:hidden;
  text-align:center; padding:80px; position:relative;
">
  <!-- 배경 장식 (선택) -->
  <div style="
    position:absolute; right:-100px; bottom:-100px;
    width:400px; height:400px; border-radius:50%;
    background:rgba(255,255,255,0.05);
    pointer-events:none;
  "></div>
  <!-- 컨텐츠 -->
  <div style="position:relative; z-index:1;">
    <p style="
      font-family:var(--b-font); font-size:14px;
      color:rgba(255,255,255,0.4); letter-spacing:0.12em;
      text-transform:uppercase; margin-bottom:24px;
    ">GET STARTED</p>
    <p style="
      font-family:var(--h-font); font-size:72px; font-weight:700;
      color:#fff; line-height:1.1; letter-spacing:-0.03em;
      max-width:800px;
    ">[마무리 메시지]</p>
    <p style="
      font-family:var(--b-font); font-size:20px;
      color:rgba(255,255,255,0.55); margin-top:24px;
    ">[연락처 또는 URL]</p>
    <!-- CTA 버튼 -->
    <div style="
      display:inline-flex; align-items:center; gap:8px;
      margin-top:40px; padding:16px 36px;
      background:#fff; border-radius:var(--radius);
      font-family:var(--h-font); font-size:18px;
      color:var(--primary); font-weight:700;
      cursor:pointer;
    ">[CTA 텍스트] →</div>
  </div>
</section>
```

### 변형 B: 배경 이미지 + 오버레이 CTA

```html
<!-- [Closing B] Image Background + CTA -->
<section class="slide" id="sN" style="
  position:relative; overflow:hidden; background:var(--bg);
">
  <!-- Layer 1: 이미지 -->
  <img src="[이미지URL]" style="
    position:absolute; inset:0;
    width:100%; height:100%; object-fit:cover;
    opacity:0.4; z-index:1; pointer-events:none;
  ">
  <!-- Layer 2: 오버레이 -->
  <div style="
    position:absolute; inset:0;
    background:rgba(8,8,20,0.80);
    z-index:2; pointer-events:none;
  "></div>
  <!-- Layer 3: CTA -->
  <div style="
    position:absolute; inset:0; z-index:3;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    text-align:center; padding:80px;
  ">
    <p style="
      font-family:var(--h-font); font-size:72px; font-weight:700;
      color:#fff; line-height:1.1; letter-spacing:-0.03em;
      max-width:800px;
    ">[마무리 메시지]</p>
    <p style="
      font-family:var(--b-font); font-size:20px;
      color:rgba(255,255,255,0.5); margin-top:24px;
    ">[연락처]</p>
    <div style="
      display:inline-flex; margin-top:40px;
      padding:16px 40px; background:var(--accent);
      border-radius:var(--radius);
      font-family:var(--h-font); font-size:18px;
      color:#fff; font-weight:700;
    ">[CTA 텍스트]</div>
  </div>
</section>
```
