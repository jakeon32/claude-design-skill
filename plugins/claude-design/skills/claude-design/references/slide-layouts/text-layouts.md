---
name: text-layouts
description: "슬라이드 텍스트 레이아웃 HTML 템플릿 — Highlight, Simple List, 2×2 Grid, 3/4-Column Text, Numbered List, Asymmetric."
---

# Text Layouts

텍스트 중심 레이아웃. 모두 이미지 없이 동작하며, 아이콘(Lucide/Heroicons SVG)으로 보완 가능.

---

## Highlight

H2(주제) 좌 + 본문(설명) 우. 2컬럼 텍스트 기본형.

```
Visual (배경 + 장식): 40%
Text:                 55%
```

```html
<!-- [Highlight] H2 Left + Body Right -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row; align-items:center;
  background:var(--bg); overflow:hidden; padding:0 80px;
">
  <!-- 좌: 주제 헤딩 (45%) -->
  <div style="flex:0 0 540px; padding-right:64px;">
    <!-- 레이블 (선택) -->
    <p style="
      font-family:var(--b-font); font-size:13px;
      color:var(--accent); letter-spacing:0.1em;
      text-transform:uppercase; margin-bottom:20px;
    ">[레이블]</p>
    <p style="
      font-family:var(--h-font); font-size:60px; font-weight:700;
      color:var(--text); line-height:1.1; letter-spacing:-0.02em;
    ">[핵심 메시지 또는 주제]</p>
    <!-- 구분선 -->
    <div style="width:48px; height:3px; background:var(--accent); margin-top:32px;"></div>
  </div>
  <!-- 구분선 (수직) -->
  <div style="
    flex-shrink:0; width:1px; height:200px;
    background:var(--border); margin:0 40px;
  "></div>
  <!-- 우: 본문 설명 (55%) -->
  <div style="flex:1;">
    <p style="
      font-family:var(--b-font); font-size:20px; line-height:1.75;
      color:var(--muted);
    ">[본문 설명. 2~4문장. 핵심 메시지를 뒷받침하는 내용.]</p>
    <!-- 보조 포인트 (선택) -->
    <div style="display:flex; flex-direction:column; gap:16px; margin-top:32px;">
      <div style="display:flex; align-items:flex-start; gap:12px;">
        <div style="
          flex-shrink:0; width:6px; height:6px;
          background:var(--accent); border-radius:50%; margin-top:9px;
        "></div>
        <p style="
          font-family:var(--b-font); font-size:17px; line-height:1.6;
          color:var(--text);
        ">[포인트 1]</p>
      </div>
      <div style="display:flex; align-items:flex-start; gap:12px;">
        <div style="
          flex-shrink:0; width:6px; height:6px;
          background:var(--accent); border-radius:50%; margin-top:9px;
        "></div>
        <p style="
          font-family:var(--b-font); font-size:17px; line-height:1.6;
          color:var(--text);
        ">[포인트 2]</p>
      </div>
    </div>
  </div>
</section>
```

---

## Simple List

H2(주제) 좌 + 세로 리스트 우. 3~4항목.

```html
<!-- [Simple List] H2 Left + Vertical List Right -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row; align-items:center;
  background:var(--bg); overflow:hidden; padding:0 80px;
">
  <!-- 좌: 제목 (38%) -->
  <div style="flex:0 0 460px; padding-right:56px;">
    <p style="
      font-family:var(--b-font); font-size:13px;
      color:var(--accent); letter-spacing:0.1em;
      text-transform:uppercase; margin-bottom:16px;
    ">[레이블]</p>
    <p style="
      font-family:var(--h-font); font-size:52px; font-weight:700;
      color:var(--text); line-height:1.1; letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
  </div>
  <!-- 우: 리스트 (62%) -->
  <div style="flex:1; display:flex; flex-direction:column; gap:24px;">
    <!-- 항목 1 -->
    <div style="
      display:flex; align-items:flex-start; gap:20px;
      padding:20px 24px; background:var(--surface);
      border-radius:var(--radius);
    ">
      <!-- 순서 숫자 또는 아이콘 -->
      <div style="
        flex-shrink:0; width:40px; height:40px;
        background:var(--primary); border-radius:8px;
        display:flex; align-items:center; justify-content:center;
        font-family:var(--h-font); font-size:18px; font-weight:700;
        color:var(--accent);
      ">01</div>
      <div>
        <p style="
          font-family:var(--h-font); font-size:20px; font-weight:600;
          color:var(--text);
        ">[항목 제목]</p>
        <p style="
          font-family:var(--b-font); font-size:15px; line-height:1.6;
          color:var(--muted); margin-top:4px;
        ">[항목 설명. 1~2줄.]</p>
      </div>
    </div>
    <!-- 항목 2, 3 동일 구조 반복 (최대 4개) -->
  </div>
</section>
```

---

## 2×2 Grid

4개 항목을 2×2 그리드로 배치. 동등한 특징 비교.

```html
<!-- [2×2 Grid] -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <!-- 헤더 -->
  <div style="flex-shrink:0; padding:48px 80px 32px;">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:18px;
      color:var(--muted); margin-top:8px;
    ">[서브타이틀 (선택)]</p>
  </div>
  <!-- 2×2 그리드 -->
  <div style="
    flex:1; display:flex; flex-wrap:wrap; gap:16px;
    padding:0 80px 56px; min-height:0;
  ">
    <!-- 각 셀 (4개) — flex-basis 계산: (1280 - 160 - 16) / 2 = 552px -->
    <div style="
      flex:0 0 calc(50% - 8px); display:flex; flex-direction:column;
      padding:28px 28px; background:var(--surface);
      border-radius:var(--radius);
    ">
      <!-- 아이콘 또는 액센트 숫자 -->
      <div style="
        width:40px; height:40px; border-radius:8px;
        background:var(--primary); display:flex;
        align-items:center; justify-content:center;
        margin-bottom:16px;
      ">
        <!-- SVG 아이콘 또는 숫자 -->
        <p style="
          font-family:var(--h-font); font-size:20px; font-weight:700;
          color:var(--accent);
        ">01</p>
      </div>
      <p style="
        font-family:var(--h-font); font-size:22px; font-weight:600;
        color:var(--text); margin-bottom:8px;
      ">[항목 제목]</p>
      <p style="
        font-family:var(--b-font); font-size:15px; line-height:1.6;
        color:var(--muted);
      ">[항목 설명. 2~3줄 내외.]</p>
    </div>
    <!-- 나머지 3개 동일 구조 -->
  </div>
</section>
```

---

## 3-Column Text

상단 제목 + 3열 콘텐츠 블록.

```html
<!-- [3-Column Text] -->
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
  </div>
  <!-- 3열 컨테이너 -->
  <div style="
    flex:1; display:flex; gap:24px;
    padding:0 80px 56px; min-height:0;
  ">
    <!-- 열 1 -->
    <div style="
      flex:1; padding:28px 24px; background:var(--surface);
      border-radius:var(--radius);
    ">
      <!-- 상단 액센트 바 -->
      <div style="width:32px; height:3px; background:var(--accent); margin-bottom:20px;"></div>
      <p style="
        font-family:var(--h-font); font-size:22px; font-weight:600;
        color:var(--text); margin-bottom:12px;
      ">[열 제목]</p>
      <p style="
        font-family:var(--b-font); font-size:16px; line-height:1.7;
        color:var(--muted);
      ">[열 내용. 3~5줄 내외.]</p>
    </div>
    <!-- 열 2, 3 동일 구조 -->
  </div>
</section>
```

---

## 4-Column Text

상단 제목 + 4열. 짧은 내용 4개.

```html
<!-- [4-Column Text] -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <div style="flex-shrink:0; padding:44px 80px 24px;">
    <p style="
      font-family:var(--h-font); font-size:40px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
  </div>
  <div style="
    flex:1; display:flex; gap:16px;
    padding:0 80px 48px; min-height:0;
  ">
    <!-- 열 1~4 (각 flex:1) -->
    <div style="
      flex:1; padding:24px 20px; background:var(--surface);
      border-radius:var(--radius); display:flex; flex-direction:column;
    ">
      <!-- 아이콘 영역 (선택) -->
      <div style="
        width:36px; height:36px; border-radius:8px;
        background:var(--primary); margin-bottom:16px;
      "></div>
      <p style="
        font-family:var(--h-font); font-size:18px; font-weight:600;
        color:var(--text); margin-bottom:8px;
      ">[열 제목]</p>
      <p style="
        font-family:var(--b-font); font-size:14px; line-height:1.65;
        color:var(--muted);
      ">[열 내용. 2~3줄.]</p>
    </div>
    <!-- 나머지 3개 동일 -->
  </div>
</section>
```

---

## Numbered List

번호 강조 + 리스트 우측. 순서가 중요한 단계 설명.

```html
<!-- [Numbered List] -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row; align-items:center;
  background:var(--bg); overflow:hidden; padding:0 80px;
">
  <!-- 좌: 제목 + 대형 번호 배경 (35%) -->
  <div style="flex:0 0 420px; padding-right:48px; position:relative;">
    <!-- 배경 대형 번호 장식 -->
    <p style="
      position:absolute; top:50%; left:0;
      transform:translateY(-50%);
      font-family:var(--h-font); font-size:200px; font-weight:900;
      color:var(--border); line-height:1;
      user-select:none; pointer-events:none;
    ">N</p>
    <div style="position:relative; z-index:1;">
      <p style="
        font-family:var(--b-font); font-size:13px;
        color:var(--accent); letter-spacing:0.1em;
        text-transform:uppercase; margin-bottom:12px;
      ">[레이블]</p>
      <p style="
        font-family:var(--h-font); font-size:48px; font-weight:700;
        color:var(--text); line-height:1.1; letter-spacing:-0.02em;
      ">[슬라이드 제목]</p>
    </div>
  </div>
  <!-- 우: 번호 리스트 (65%) -->
  <div style="flex:1; display:flex; flex-direction:column; gap:20px;">
    <!-- 항목 (최대 4개) -->
    <div style="display:flex; align-items:flex-start; gap:20px;">
      <div style="
        flex-shrink:0; width:44px; height:44px;
        border:2px solid var(--accent); border-radius:50%;
        display:flex; align-items:center; justify-content:center;
        font-family:var(--h-font); font-size:18px; font-weight:700;
        color:var(--accent);
      ">1</div>
      <div style="padding-top:6px;">
        <p style="
          font-family:var(--h-font); font-size:20px; font-weight:600;
          color:var(--text);
        ">[항목 제목]</p>
        <p style="
          font-family:var(--b-font); font-size:15px; line-height:1.6;
          color:var(--muted); margin-top:4px;
        ">[항목 설명]</p>
      </div>
    </div>
    <!-- 2, 3, 4번 동일 구조 -->
  </div>
</section>
```

---

## Asymmetric

큰 텍스트 블록(좌) + 2×2 그리드(우). 정보 밀도 높은 레이아웃.

```html
<!-- [Asymmetric] Big Text Left + 2×2 Right -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row; align-items:stretch;
  background:var(--bg); overflow:hidden;
">
  <!-- 좌: 큰 텍스트 블록 (42%) -->
  <div style="
    flex:0 0 540px; display:flex; flex-direction:column;
    justify-content:center; padding:64px 56px 64px 80px;
    background:var(--primary);
  ">
    <p style="
      font-family:var(--b-font); font-size:13px;
      color:rgba(255,255,255,0.45); letter-spacing:0.1em;
      text-transform:uppercase; margin-bottom:16px;
    ">[레이블]</p>
    <p style="
      font-family:var(--h-font); font-size:52px; font-weight:700;
      color:#fff; line-height:1.1; letter-spacing:-0.02em;
    ">[핵심 메시지]</p>
    <p style="
      font-family:var(--b-font); font-size:18px; line-height:1.7;
      color:rgba(255,255,255,0.6); margin-top:24px;
    ">[뒷받침 설명. 2~3문장.]</p>
  </div>
  <!-- 우: 2×2 그리드 (58%) -->
  <div style="
    flex:1; display:flex; flex-wrap:wrap; gap:2px;
    padding:40px 56px 40px 40px; background:var(--bg);
    align-content:center;
  ">
    <!-- 4개 셀 -->
    <div style="
      flex:0 0 calc(50% - 1px); padding:28px 24px;
      background:var(--surface);
    ">
      <p style="
        font-family:var(--h-font); font-size:32px; font-weight:700;
        color:var(--accent); margin-bottom:8px;
      ">[숫자/키워드]</p>
      <p style="
        font-family:var(--b-font); font-size:15px; line-height:1.6;
        color:var(--muted);
      ">[설명]</p>
    </div>
    <!-- 나머지 3개 동일 -->
  </div>
</section>
```
