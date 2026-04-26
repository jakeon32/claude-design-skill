---
name: statement-layouts
description: "슬라이드 Statement/Quote 레이아웃 — Centered Statement, Big Number, Quote. 임팩트 강조 레이아웃."
---

# Statement / Quote Layouts

임팩트 있는 숫자, 인용문, 핵심 메시지를 위한 레이아웃. 여백이 메시지를 강조한다.

---

## Centered Statement

핵심 메시지 1개를 중앙에 크게 배치. 여백이 40%+.

```
Visual (배경 + 장식): 30%
Text:                 25% (1개 메시지만)
White Space:          45%+ (여백이 핵심)
```

```html
<!-- [Centered Statement] -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  background:var(--bg); overflow:hidden;
  text-align:center; padding:80px;
">
  <!-- 레이블 (선택) -->
  <p style="
    font-family:var(--b-font); font-size:13px;
    color:var(--accent); letter-spacing:0.12em;
    text-transform:uppercase; margin-bottom:28px;
  ">[레이블 또는 카테고리]</p>
  <!-- 핵심 메시지 (Hero) -->
  <p style="
    font-family:var(--h-font); font-size:76px; font-weight:700;
    color:var(--text); line-height:1.1; letter-spacing:-0.03em;
    max-width:900px;
  ">[핵심 메시지 — 1문장 또는 키워드]</p>
  <!-- 서브 설명 (선택) -->
  <p style="
    font-family:var(--b-font); font-size:20px; line-height:1.65;
    color:var(--muted); margin-top:32px; max-width:640px;
  ">[메시지를 뒷받침하는 짧은 설명]</p>
  <!-- 하단 장식 (선택) -->
  <div style="width:48px; height:3px; background:var(--accent); margin-top:40px;"></div>
</section>
```

---

## Big Number

KPI, 임팩트 있는 수치를 Hero로 배치.

```html
<!-- [Big Number] Stat Highlight -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  background:var(--bg); overflow:hidden;
  text-align:center; padding:80px;
">
  <!-- 대형 숫자 (Hero) -->
  <p style="
    font-family:var(--h-font); font-size:160px; font-weight:900;
    color:var(--accent); line-height:1; letter-spacing:-0.05em;
  ">[숫자]</p>
  <!-- 단위 (선택) -->
  <p style="
    font-family:var(--h-font); font-size:40px; font-weight:700;
    color:var(--text); margin-top:8px; letter-spacing:-0.02em;
  ">[단위 또는 지표명]</p>
  <!-- 설명 -->
  <p style="
    font-family:var(--b-font); font-size:20px; line-height:1.65;
    color:var(--muted); margin-top:24px; max-width:560px;
  ">[이 숫자가 의미하는 것]</p>
</section>
```

### 변형: 3개 지표 나열 (Key Metrics)

```html
<!-- [Key Metrics] 3 Stats -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  background:var(--bg); overflow:hidden; padding:64px 80px;
">
  <!-- 상단 제목 (선택) -->
  <p style="
    font-family:var(--h-font); font-size:40px; font-weight:700;
    color:var(--text); letter-spacing:-0.02em;
    margin-bottom:64px; text-align:center;
  ">[섹션 제목]</p>
  <!-- 3개 지표 가로 나열 -->
  <div style="
    display:flex; gap:0; width:100%;
    border-top:1px solid var(--border);
    border-bottom:1px solid var(--border);
  ">
    <!-- 지표 1 -->
    <div style="
      flex:1; display:flex; flex-direction:column;
      align-items:center; padding:40px 24px;
      border-right:1px solid var(--border);
    ">
      <p style="
        font-family:var(--h-font); font-size:80px; font-weight:900;
        color:var(--accent); line-height:1; letter-spacing:-0.04em;
      ">[숫자]</p>
      <p style="
        font-family:var(--b-font); font-size:14px;
        color:var(--muted); margin-top:12px;
        letter-spacing:0.05em; text-transform:uppercase;
      ">[지표명]</p>
    </div>
    <!-- 지표 2 (border-right 없이) -->
    <div style="
      flex:1; display:flex; flex-direction:column;
      align-items:center; padding:40px 24px;
      border-right:1px solid var(--border);
    ">
      <p style="
        font-family:var(--h-font); font-size:80px; font-weight:900;
        color:var(--accent); line-height:1; letter-spacing:-0.04em;
      ">[숫자]</p>
      <p style="
        font-family:var(--b-font); font-size:14px;
        color:var(--muted); margin-top:12px;
        letter-spacing:0.05em; text-transform:uppercase;
      ">[지표명]</p>
    </div>
    <!-- 지표 3 -->
    <div style="
      flex:1; display:flex; flex-direction:column;
      align-items:center; padding:40px 24px;
    ">
      <p style="
        font-family:var(--h-font); font-size:80px; font-weight:900;
        color:var(--accent); line-height:1; letter-spacing:-0.04em;
      ">[숫자]</p>
      <p style="
        font-family:var(--b-font); font-size:14px;
        color:var(--muted); margin-top:12px;
        letter-spacing:0.05em; text-transform:uppercase;
      ">[지표명]</p>
    </div>
  </div>
</section>
```

---

## Quote

고객 인용문 또는 핵심 메시지를 큰 따옴표와 함께 배치.

### 변형 A: 텍스트 전용

```html
<!-- [Quote A] Text Only -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  align-items:flex-start; justify-content:center;
  background:var(--primary); overflow:hidden;
  padding:80px 120px;
">
  <!-- 큰 따옴표 장식 -->
  <p style="
    font-family:Georgia, serif; font-size:160px;
    color:rgba(255,255,255,0.12); line-height:0.7;
    margin-bottom:16px; user-select:none;
  ">"</p>
  <!-- 인용문 -->
  <p style="
    font-family:var(--h-font); font-size:44px; font-weight:500;
    color:#fff; line-height:1.35; letter-spacing:-0.01em;
    max-width:880px; margin-top:-40px;
  ">[인용문 내용. 2~3줄 내외.]</p>
  <!-- 출처 -->
  <div style="display:flex; align-items:center; gap:16px; margin-top:40px;">
    <!-- 프로필 이미지 (선택) -->
    <div style="
      width:48px; height:48px; border-radius:50%;
      background:rgba(255,255,255,0.15); overflow:hidden; flex-shrink:0;
    ">
      <img src="[프로필이미지URL]" style="width:100%;height:100%;object-fit:cover;">
    </div>
    <div>
      <p style="
        font-family:var(--h-font); font-size:18px; font-weight:600;
        color:#fff;
      ">[이름]</p>
      <p style="
        font-family:var(--b-font); font-size:14px;
        color:rgba(255,255,255,0.5);
      ">[직함 / 회사]</p>
    </div>
  </div>
</section>
```

### 변형 B: 배경 이미지 + 인용문

```html
<!-- [Quote B] Background Image + Quote -->
<section class="slide" id="sN" style="
  position:relative; overflow:hidden;
  background:var(--bg);
">
  <!-- Layer 1: 배경 이미지 -->
  <img src="[이미지URL]" style="
    position:absolute; inset:0;
    width:100%; height:100%; object-fit:cover;
    opacity:0.35; z-index:1; pointer-events:none;
  ">
  <!-- Layer 2: 오버레이 -->
  <div style="
    position:absolute; inset:0;
    background:rgba(8,8,16,0.78);
    z-index:2; pointer-events:none;
  "></div>
  <!-- Layer 3: 인용문 -->
  <div style="
    position:absolute; inset:0; z-index:3;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    padding:80px 120px; text-align:center;
  ">
    <p style="
      font-family:Georgia, serif; font-size:120px;
      color:rgba(255,255,255,0.1); line-height:0.6;
      margin-bottom:8px; user-select:none;
    ">"</p>
    <p style="
      font-family:var(--h-font); font-size:40px; font-weight:500;
      color:#fff; line-height:1.4; letter-spacing:-0.01em;
      max-width:840px; margin-top:-20px;
    ">[인용문]</p>
    <p style="
      font-family:var(--b-font); font-size:16px;
      color:rgba(255,255,255,0.45); margin-top:32px;
      letter-spacing:0.05em;
    ">— [이름], [직함]</p>
  </div>
</section>
```
