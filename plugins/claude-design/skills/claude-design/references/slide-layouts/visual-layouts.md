---
name: visual-layouts
description: "슬라이드 비주얼/포토 레이아웃 HTML 템플릿 — Photo Split (3변형), Full Bleed Photo, 2/3-Col Image+Caption."
---

# Visual / Photo Layouts

## Photo Split

텍스트 패널(좌) + 이미지 패널(우). 가장 범용적인 콘텐츠 레이아웃.

### 구조 원칙

```
Visual (이미지 패널): 60~70%
Text (제목 + 본문):   25~35%
이미지 패널: 120% 확장 + gradient blend (HTML 모드)
PPTX 모드: gradient 제거, solid 패널 분리
```

### 변형 A: 텍스트 좌 + 이미지 우 (기본형)

```html
<!-- [Photo Split A] Text Left + Image Right -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row;
  background:var(--bg); overflow:hidden;
">
  <!-- 좌: 텍스트 패널 -->
  <div style="
    flex:0 0 520px; display:flex; flex-direction:column;
    justify-content:center; padding:64px 56px 64px 80px;
  ">
    <!-- 레이블 (선택) -->
    <p style="
      font-family:var(--b-font); font-size:13px;
      color:var(--accent); letter-spacing:0.1em;
      text-transform:uppercase; margin-bottom:16px;
    ">[레이블]</p>
    <!-- 제목 -->
    <p style="
      font-family:var(--h-font); font-size:48px; font-weight:700;
      color:var(--text); line-height:1.15; letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
    <!-- 본문 -->
    <p style="
      font-family:var(--b-font); font-size:18px; line-height:1.7;
      color:var(--muted); margin-top:24px; max-width:380px;
    ">[본문 내용. 핵심 메시지 1~2문장.]</p>
    <!-- CTA (선택) -->
    <div style="
      display:inline-flex; align-items:center; gap:8px;
      margin-top:32px; padding:12px 24px;
      background:var(--accent); border-radius:var(--radius);
      font-family:var(--b-font); font-size:15px;
      color:#fff; font-weight:600; cursor:pointer;
      width:fit-content;
    ">[버튼 텍스트] →</div>
  </div>
  <!-- 우: 이미지 패널 (120% 확장 + seam 오버랩) -->
  <div style="flex:1.44; overflow:hidden; position:relative; margin-left:-8px;">
    <img src="[이미지URL]" style="
      width:100%; height:100%; object-fit:cover;
    ">
    <!-- Gradient Blend (HTML 모드 전용 — PPTX 시 제거) -->
    <div style="
      position:absolute; inset:0;
      background:linear-gradient(to right, var(--bg) 0%, transparent 45%);
      pointer-events:none;
    "></div>
  </div>
</section>
```

### 변형 B: 이미지 좌 + 텍스트 우 (역방향)

```html
<!-- [Photo Split B] Image Left + Text Right -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row;
  background:var(--bg); overflow:hidden;
">
  <!-- 좌: 이미지 패널 (120% 확장) -->
  <div style="flex:1.44; overflow:hidden; position:relative; margin-right:-8px;">
    <img src="[이미지URL]" style="
      width:100%; height:100%; object-fit:cover;
    ">
    <!-- Gradient Blend (HTML 모드 전용) -->
    <div style="
      position:absolute; inset:0;
      background:linear-gradient(to left, var(--bg) 0%, transparent 45%);
      pointer-events:none;
    "></div>
  </div>
  <!-- 우: 텍스트 패널 -->
  <div style="
    flex:0 0 520px; display:flex; flex-direction:column;
    justify-content:center; padding:64px 80px 64px 56px;
  ">
    <p style="
      font-family:var(--b-font); font-size:13px;
      color:var(--accent); letter-spacing:0.1em;
      text-transform:uppercase; margin-bottom:16px;
    ">[레이블]</p>
    <p style="
      font-family:var(--h-font); font-size:48px; font-weight:700;
      color:var(--text); line-height:1.15; letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:18px; line-height:1.7;
      color:var(--muted); margin-top:24px;
    ">[본문 내용]</p>
  </div>
</section>
```

### 변형 C: 상단 이미지 + 하단 텍스트 (분할 수평)

```html
<!-- [Photo Split C] Top Image + Bottom Text -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <!-- 상: 이미지 패널 (55%) -->
  <div style="flex:0 0 396px; overflow:hidden; position:relative;">
    <img src="[이미지URL]" style="
      width:100%; height:100%; object-fit:cover;
    ">
    <!-- Gradient Blend (HTML 모드 전용) -->
    <div style="
      position:absolute; inset:0;
      background:linear-gradient(to bottom, transparent 50%, var(--bg) 100%);
      pointer-events:none;
    "></div>
  </div>
  <!-- 하: 텍스트 패널 (45%) -->
  <div style="
    flex:1; display:flex; flex-direction:column;
    justify-content:center; padding:0 80px 48px;
  ">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); line-height:1.15; letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:18px; line-height:1.7;
      color:var(--muted); margin-top:16px; max-width:800px;
    ">[본문 내용]</p>
  </div>
</section>
```

---

## Full Bleed Photo

전체화면 이미지 + 오버레이 텍스트. 감성·분위기 슬라이드.

### 구조 원칙

```
Visual: 75%+
Text: 15% 이하 (하단 또는 중앙)
z-index 3레이어 구조 필수
```

```html
<!-- [Full Bleed Photo] -->
<section class="slide" id="sN" style="
  position:relative; overflow:hidden;
  background:var(--bg);
">
  <!-- Layer 1: 이미지 -->
  <img src="[이미지URL]" style="
    position:absolute; inset:0;
    width:100%; height:100%; object-fit:cover;
    opacity:0.5; z-index:1; pointer-events:none;
  ">
  <!-- Layer 2: 오버레이 -->
  <div style="
    position:absolute; inset:0;
    background:rgba(10,10,20,0.68);
    z-index:2; pointer-events:none;
  "></div>
  <!-- Layer 3: 텍스트 (하단 좌측 정렬) -->
  <div style="
    position:absolute; left:80px; right:80px; bottom:80px;
    z-index:3;
  ">
    <p style="
      font-family:var(--b-font); font-size:14px;
      color:rgba(255,255,255,0.45); letter-spacing:0.1em;
      text-transform:uppercase; margin-bottom:12px;
    ">[레이블]</p>
    <p style="
      font-family:var(--h-font); font-size:56px; font-weight:700;
      color:#fff; line-height:1.1; letter-spacing:-0.02em;
      max-width:700px;
    ">[슬라이드 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:18px;
      color:rgba(255,255,255,0.55); margin-top:16px;
      max-width:540px;
    ">[서브텍스트]</p>
  </div>
</section>
```

**이미지 opacity 기준**:
| 배경 분위기 | 이미지 opacity | 오버레이 opacity |
|------------|--------------|-----------------|
| Cool/Dark 배경 | 0.35~0.50 | 0.70~0.85 |
| Warm/Light 배경 | 0.20~0.35 | 0.55~0.70 |

---

## 2-Col Image+Caption

이미지 2개 나란히 + 각 캡션. 비교·병렬 콘텐츠.

```html
<!-- [2-Col Image+Caption] -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <!-- 헤더 -->
  <div style="
    flex-shrink:0; padding:48px 80px 32px;
  ">
    <p style="
      font-family:var(--h-font); font-size:44px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
  </div>
  <!-- 이미지 + 캡션 컨테이너 -->
  <div style="
    flex:1; display:flex; gap:24px;
    padding:0 80px 56px; min-height:0;
  ">
    <!-- 이미지 카드 1 -->
    <div style="flex:1; display:flex; flex-direction:column; gap:16px;">
      <div style="flex:1; overflow:hidden; border-radius:var(--radius);">
        <img src="[이미지1URL]" style="
          width:100%; height:100%; object-fit:cover;
        ">
      </div>
      <div>
        <p style="
          font-family:var(--h-font); font-size:20px; font-weight:600;
          color:var(--text);
        ">[이미지 1 제목]</p>
        <p style="
          font-family:var(--b-font); font-size:15px; line-height:1.6;
          color:var(--muted); margin-top:6px;
        ">[이미지 1 설명]</p>
      </div>
    </div>
    <!-- 이미지 카드 2 -->
    <div style="flex:1; display:flex; flex-direction:column; gap:16px;">
      <div style="flex:1; overflow:hidden; border-radius:var(--radius);">
        <img src="[이미지2URL]" style="
          width:100%; height:100%; object-fit:cover;
        ">
      </div>
      <div>
        <p style="
          font-family:var(--h-font); font-size:20px; font-weight:600;
          color:var(--text);
        ">[이미지 2 제목]</p>
        <p style="
          font-family:var(--b-font); font-size:15px; line-height:1.6;
          color:var(--muted); margin-top:6px;
        ">[이미지 2 설명]</p>
      </div>
    </div>
  </div>
</section>
```

---

## 3-Col Image+Caption

이미지 3개 나란히 + 각 캡션.

```html
<!-- [3-Col Image+Caption] -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <!-- 헤더 -->
  <div style="flex-shrink:0; padding:44px 80px 28px;">
    <p style="
      font-family:var(--h-font); font-size:40px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
  </div>
  <!-- 이미지 3열 -->
  <div style="
    flex:1; display:flex; gap:20px;
    padding:0 80px 52px; min-height:0;
  ">
    <!-- 이미지 카드 1, 2, 3 반복 -->
    <div style="flex:1; display:flex; flex-direction:column; gap:14px;">
      <div style="flex:1; overflow:hidden; border-radius:var(--radius);">
        <img src="[이미지URL]" style="width:100%; height:100%; object-fit:cover;">
      </div>
      <div>
        <p style="
          font-family:var(--h-font); font-size:18px; font-weight:600;
          color:var(--text);
        ">[제목]</p>
        <p style="
          font-family:var(--b-font); font-size:14px; line-height:1.6;
          color:var(--muted); margin-top:4px;
        ">[설명]</p>
      </div>
    </div>
    <!-- (2번, 3번 동일 구조 반복) -->
  </div>
</section>
```
