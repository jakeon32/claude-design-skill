---
name: mockup-layouts
description: "슬라이드 목업 레이아웃 HTML 템플릿 — Mobile Mockup (1/3/Annotated), Desktop Mockup, Desktop Full. CSS로 기기 프레임 구현."
---

# Mockup Layouts

기기 프레임을 CSS로 구현. 외부 SVG 이미지 없이 순수 CSS 기기 형태.

**기기 비율 기준**:
| 기기 | 비율 | CSS 크기 예시 |
|------|------|-------------|
| iPhone (현대) | 9:19.5 | 220×477px |
| Android | 9:20 | 220×489px |
| MacBook 화면 | 16:10 | 500×313px |

---

## Mobile Mockup (1)

텍스트 좌 + 폰 1대 우.

```html
<!-- [Mobile Mockup 1] Text Left + 1 Phone Right -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row; align-items:center;
  background:var(--bg); overflow:hidden;
">
  <!-- 좌: 텍스트 (45%) -->
  <div style="
    flex:0 0 560px; display:flex; flex-direction:column;
    justify-content:center; padding:64px 56px 64px 80px;
  ">
    <p style="
      font-family:var(--b-font); font-size:13px;
      color:var(--accent); letter-spacing:0.1em;
      text-transform:uppercase; margin-bottom:16px;
    ">[레이블]</p>
    <p style="
      font-family:var(--h-font); font-size:52px; font-weight:700;
      color:var(--text); line-height:1.1; letter-spacing:-0.02em;
    ">[앱 이름 또는 기능 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:18px; line-height:1.7;
      color:var(--muted); margin-top:24px;
    ">[기능 설명. 2~3문장.]</p>
    <!-- 앱스토어 배지 (선택) -->
    <div style="display:flex; gap:12px; margin-top:32px;">
      <div style="
        padding:10px 20px; background:var(--text);
        border-radius:8px; display:flex; align-items:center; gap:8px;
      ">
        <p style="
          font-family:var(--b-font); font-size:14px; font-weight:600;
          color:var(--bg);
        ">App Store</p>
      </div>
      <div style="
        padding:10px 20px; background:var(--surface);
        border:1px solid var(--border);
        border-radius:8px; display:flex; align-items:center; gap:8px;
      ">
        <p style="
          font-family:var(--b-font); font-size:14px; font-weight:600;
          color:var(--text);
        ">Google Play</p>
      </div>
    </div>
  </div>
  <!-- 우: 폰 목업 (55%) -->
  <div style="
    flex:1; display:flex; align-items:center; justify-content:center;
  ">
    <!-- iPhone CSS 프레임 -->
    <div style="
      width:220px; height:477px;
      background:#111; border-radius:36px;
      border:8px solid #222;
      box-shadow:
        0 0 0 2px #333,
        0 24px 48px rgba(0,0,0,0.4),
        0 8px 16px rgba(0,0,0,0.3);
      overflow:hidden; position:relative;
    ">
      <!-- 상단 노치 -->
      <div style="
        position:absolute; top:0; left:50%;
        transform:translateX(-50%);
        width:80px; height:24px;
        background:#111; border-radius:0 0 16px 16px;
        z-index:10;
      "></div>
      <!-- 앱 화면 (스크린샷 또는 placeholder) -->
      <div style="
        width:100%; height:100%;
        background:var(--surface);
        display:flex; align-items:center; justify-content:center;
      ">
        <img src="[앱스크린샷URL]" style="
          width:100%; height:100%; object-fit:cover;
        ">
      </div>
    </div>
  </div>
</section>
```

---

## Mobile Mockup (3)

폰 3대 나란히. 다화면 비교 또는 앱 흐름 시연.

```html
<!-- [Mobile Mockup 3] 3 Phones Side by Side -->
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
  <!-- 폰 3대 -->
  <div style="
    flex:1; display:flex; gap:40px;
    align-items:center; justify-content:center;
    padding:0 80px 48px;
  ">
    <!-- 폰 1 (중간 높이 — 배경 느낌) -->
    <div style="
      width:180px; height:390px; transform:translateY(20px);
      background:#111; border-radius:30px;
      border:6px solid #222;
      box-shadow:0 20px 40px rgba(0,0,0,0.3);
      overflow:hidden; opacity:0.75;
    ">
      <div style="width:100%;height:100%;background:var(--surface);">
        <img src="[스크린1URL]" style="width:100%;height:100%;object-fit:cover;">
      </div>
    </div>
    <!-- 폰 2 (앞으로 튀어나온 메인) -->
    <div style="
      width:200px; height:432px;
      background:#111; border-radius:32px;
      border:7px solid #1a1a1a;
      box-shadow:
        0 0 0 2px #333,
        0 32px 64px rgba(0,0,0,0.5);
      overflow:hidden; z-index:1;
    ">
      <!-- 노치 -->
      <div style="
        position:absolute; top:0; left:50%;
        transform:translateX(-50%);
        width:70px; height:20px;
        background:#111; border-radius:0 0 12px 12px;
        z-index:10;
      "></div>
      <div style="width:100%;height:100%;background:var(--surface);">
        <img src="[스크린2URL]" style="width:100%;height:100%;object-fit:cover;">
      </div>
    </div>
    <!-- 폰 3 (우측, 배경 느낌) -->
    <div style="
      width:180px; height:390px; transform:translateY(20px);
      background:#111; border-radius:30px;
      border:6px solid #222;
      box-shadow:0 20px 40px rgba(0,0,0,0.3);
      overflow:hidden; opacity:0.75;
    ">
      <div style="width:100%;height:100%;background:var(--surface);">
        <img src="[스크린3URL]" style="width:100%;height:100%;object-fit:cover;">
      </div>
    </div>
  </div>
</section>
```

---

## Mobile + Annotations

기기 + 기능 콜아웃 화살표.

```html
<!-- [Mobile + Annotations] Phone + Feature Callouts -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row; align-items:center;
  background:var(--bg); overflow:hidden; padding:0 80px;
">
  <!-- 좌: 콜아웃 리스트 -->
  <div style="
    flex:0 0 380px; display:flex; flex-direction:column;
    justify-content:center; gap:24px;
  ">
    <!-- 콜아웃 항목 -->
    <div style="display:flex; align-items:center; gap:16px;">
      <!-- 번호 배지 -->
      <div style="
        flex-shrink:0; width:32px; height:32px; border-radius:50%;
        background:var(--accent); display:flex;
        align-items:center; justify-content:center;
        font-family:var(--h-font); font-size:14px; font-weight:700;
        color:#fff;
      ">1</div>
      <div>
        <p style="
          font-family:var(--h-font); font-size:18px; font-weight:600;
          color:var(--text);
        ">[기능 제목]</p>
        <p style="
          font-family:var(--b-font); font-size:14px; line-height:1.5;
          color:var(--muted);
        ">[기능 설명]</p>
      </div>
    </div>
    <!-- 2, 3, 4번 동일 구조 -->
  </div>
  <!-- 중앙: 폰 목업 -->
  <div style="
    flex:0 0 280px; display:flex; align-items:center; justify-content:center;
  ">
    <div style="
      width:220px; height:477px;
      background:#111; border-radius:36px;
      border:8px solid #222;
      box-shadow:0 0 0 2px #333, 0 24px 48px rgba(0,0,0,0.4);
      overflow:hidden;
    ">
      <div style="width:100%;height:100%;background:var(--surface);">
        <img src="[앱스크린샷URL]" style="width:100%;height:100%;object-fit:cover;">
      </div>
    </div>
  </div>
  <!-- 우: 우측 콜아웃 -->
  <div style="
    flex:1; display:flex; flex-direction:column;
    justify-content:center; gap:24px; padding-left:24px;
  ">
    <div style="display:flex; align-items:center; gap:16px;">
      <div style="
        flex-shrink:0; width:32px; height:32px; border-radius:50%;
        background:var(--secondary); border:2px solid var(--border);
        display:flex; align-items:center; justify-content:center;
        font-family:var(--h-font); font-size:14px; font-weight:700;
        color:var(--text);
      ">3</div>
      <div>
        <p style="
          font-family:var(--h-font); font-size:18px; font-weight:600;
          color:var(--text);
        ">[기능 제목]</p>
        <p style="
          font-family:var(--b-font); font-size:14px; line-height:1.5;
          color:var(--muted);
        ">[기능 설명]</p>
      </div>
    </div>
  </div>
</section>
```

---

## Desktop Mockup

텍스트 좌 + MacBook 프레임 우.

```html
<!-- [Desktop Mockup] Text Left + Laptop Right -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:row; align-items:center;
  background:var(--bg); overflow:hidden;
">
  <!-- 좌: 텍스트 -->
  <div style="
    flex:0 0 480px; display:flex; flex-direction:column;
    justify-content:center; padding:64px 48px 64px 80px;
  ">
    <p style="
      font-family:var(--b-font); font-size:13px;
      color:var(--accent); letter-spacing:0.1em;
      text-transform:uppercase; margin-bottom:16px;
    ">[레이블]</p>
    <p style="
      font-family:var(--h-font); font-size:48px; font-weight:700;
      color:var(--text); line-height:1.15; letter-spacing:-0.02em;
    ">[제목]</p>
    <p style="
      font-family:var(--b-font); font-size:18px; line-height:1.7;
      color:var(--muted); margin-top:20px;
    ">[설명]</p>
  </div>
  <!-- 우: MacBook CSS 프레임 -->
  <div style="
    flex:1; display:flex; align-items:center; justify-content:center;
    padding:40px 80px 40px 24px;
  ">
    <!-- MacBook 외장 -->
    <div style="width:100%; max-width:560px;">
      <!-- 화면 부분 -->
      <div style="
        background:#1a1a1a; border-radius:8px 8px 0 0;
        padding:12px 12px 0; position:relative;
      ">
        <!-- 카메라 -->
        <div style="
          width:8px; height:8px; border-radius:50%;
          background:#333; margin:0 auto 8px;
        "></div>
        <!-- 스크린 -->
        <div style="
          background:var(--surface); border-radius:4px; overflow:hidden;
          aspect-ratio:16/10;
        ">
          <img src="[웹앱스크린샷URL]" style="
            width:100%; height:100%; object-fit:cover;
          ">
        </div>
      </div>
      <!-- 하단 받침대 -->
      <div style="
        background:#222; height:16px;
        border-radius:0 0 4px 4px;
      "></div>
      <!-- 키보드 심볼 -->
      <div style="
        background:#1a1a1a; height:6px; border-radius:0 0 8px 8px;
        margin:0 20px;
      "></div>
    </div>
  </div>
</section>
```

---

## Desktop Full

MacBook/모니터 전체 화면 강조.

```html
<!-- [Desktop Full] Full Screen Desktop App -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  background:var(--bg); overflow:hidden;
">
  <!-- 상단 제목 -->
  <div style="flex-shrink:0; padding:40px 80px 24px;">
    <p style="
      font-family:var(--h-font); font-size:40px; font-weight:700;
      color:var(--text); letter-spacing:-0.02em;
    ">[슬라이드 제목]</p>
  </div>
  <!-- MacBook 전체 화면 -->
  <div style="
    flex:1; display:flex; align-items:center; justify-content:center;
    padding:0 80px 48px; min-height:0;
  ">
    <div style="width:100%; max-width:800px;">
      <!-- 화면 -->
      <div style="
        background:#1a1a1a; border-radius:10px 10px 0 0;
        padding:14px 14px 0;
      ">
        <div style="
          width:10px; height:10px; border-radius:50%;
          background:#444; margin:0 auto 10px;
        "></div>
        <div style="
          background:var(--surface); border-radius:4px; overflow:hidden;
          aspect-ratio:16/10; box-shadow:0 4px 20px rgba(0,0,0,0.3);
        ">
          <img src="[앱스크린샷URL]" style="
            width:100%; height:100%; object-fit:cover;
          ">
        </div>
      </div>
      <!-- 받침대 -->
      <div style="background:#282828; height:20px; border-radius:0 0 4px 4px;"></div>
      <div style="background:#1e1e1e; height:8px; border-radius:0 0 12px 12px; margin:0 40px;"></div>
    </div>
  </div>
</section>
```
