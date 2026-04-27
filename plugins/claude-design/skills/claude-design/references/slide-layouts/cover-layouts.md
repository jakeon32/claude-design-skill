---
name: cover-layouts
description: "슬라이드 커버/타이틀/섹션 구분 레이아웃 HTML 템플릿. Title/Cover (6가지 장식 패턴), Section Title."
---

# Cover / Title Layouts

## 공통 규칙

```
허용 텍스트 요소: 최대 2개 (Title + Subtitle 중 1개)
이미지 역할: 정보 전달 X → 분위기/배경 역할만
장식 요소: 타이틀보다 눈에 띠지 않을 것
배경 기반: 스타일 파일의 base theme (라이트↔다크) 준수
```

## ⚠️ Anti-Pattern (절대 금지)

### 1. 메타 row 나열 금지

```
❌ 날짜·사업규모·등급·담당부서 등 메타 정보를 row로 나열
     → .cover-meta { display:flex; } + .mi 항목 여러 개
     → "사업예산 / 사업기간 / 제안사" 같은 3~4칸 정보 테이블

✅ 대신: 날짜 1줄 또는 발표자 1줄만 — 서브타이틀 역할로
```

### 2. 4블록 구조 금지

```
❌ 태그(badge) + 제목(title) + 서브타이틀 + 메타 row = 4개 독립 블록
❌ 카테고리 라벨 + 제목 + 설명 단락 + 날짜·발표자 row = 4개 독립 블록

✅ 허용 구조:
   [장식 요소 (선/아크/도형)] + 제목 — 1개 블록
   [장식 요소] + 제목 + 서브타이틀 — 2개 블록 (최대)
   태그+제목 묶음(1블록) + 날짜(1블록) — 2개 블록
```

### 3. 커버 생성 전 의무 체크리스트

커버 HTML 작성 전 반드시 확인:
```
□ 텍스트 블록이 2개 이하인가?
□ 메타 row(정보 나열 테이블) 없는가?
□ 이미지가 정보(텍스트·차트·UI)를 담지 않고 배경 역할만 하는가?
□ 장식 요소가 타이틀보다 눈에 덜 띄는가?
□ 스타일 파일의 base theme(라이트/다크)를 그대로 쓰는가?
□ 1280×720 캔버스를 사용하는가? (1920×1080 금지)
```

---

## 커버 유형 선택 가이드

커버는 3개의 독립 축으로 결정된다. 같은 덱을 여러 스타일로 제안할 때 **동일 조합 사용 금지** — 축 중 하나 이상을 반드시 다르게 선택한다.

| 축 | 선택지 |
|----|--------|
| **레이아웃** | 1-col 전면 / 2-col 좌→우 / 2-col 역순(우→좌) / 사선 |
| **비율** | 1:1 / 1:2 / 1:3 / 2:1 / 3:1 (2-col일 때) |
| **경계 표현** | 면(패널 채움) / 선(룰 라인 1~4px) / 여백(텍스트 위치만) |

### 변형별 축 매핑

| 변형 | 레이아웃 | 비율 | 경계 표현 | 이미지 | 적합 스타일 |
|------|---------|------|---------|--------|-----------|
| A Full Bleed | 1-col | — | 면+오버레이 | 필수 | 감성·분위기 |
| B Photo Split | 2-col 좌→우 | 45:55 | 면 | 우측 필수 | 기업·제품 |
| C Solid+Geo | 1-col | — | 면+장식 | 없음 | 브랜드·강렬 |
| D Dark Arc | 1-col | — | 면+장식 | 없음 | 럭셔리·다크 |
| E Text 1:1 | 2-col 좌→우 | 1:1 | 선(rule) | 없음 | Swiss·Editorial |
| F Typo-Led | 1-col | — | 여백 | 없음 | Swiss·Minimal |
| G Reversed | 2-col 역순 | 70:30 | 면 | 없음 | Bold·Magazine |
| H Diagonal | 사선 | ~52:48 | 면+clip-path | 없음 | 역동·에너지 |

---

## Title/Cover

### 구조 원칙

```
Visual (배경 이미지 + 장식): 80~90%
Text (타이틀 + 서브):        10~20%
White Space:                  가장자리 최소 80px
```

### 변형 A: Full Bleed Image + 오버레이 텍스트

배경 이미지 전체 + 어두운 오버레이 위 텍스트. 감성·분위기 강조.

```html
<!-- [Cover A] Full Bleed + Overlay -->
<section class="slide active" id="s1" style="
  position:relative; overflow:hidden;
  background:var(--bg);
">
  <!-- z-index 1: 배경 이미지 -->
  <img src="[이미지URL]" style="
    position:absolute; inset:0;
    width:100%; height:100%; object-fit:cover;
    opacity:0.45; z-index:1; pointer-events:none;
  ">
  <!-- z-index 2: 어두운 오버레이 -->
  <div style="
    position:absolute; inset:0;
    background:rgba(10,15,30,0.72);
    z-index:2; pointer-events:none;
  "></div>
  <!-- z-index 3: 텍스트 콘텐츠 -->
  <div style="
    position:relative; z-index:3;
    display:flex; flex-direction:column;
    justify-content:center; align-items:flex-start;
    width:100%; height:100%;
    padding:0 120px;
  ">
    <!-- 장식 라인 (선택) -->
    <div style="width:48px; height:3px; background:var(--accent); margin-bottom:32px;"></div>
    <!-- 타이틀 -->
    <p style="
      font-family:var(--h-font); font-size:72px; font-weight:700;
      color:#fff; line-height:1.1; letter-spacing:-0.02em;
      max-width:700px;
    ">[덱 제목]</p>
    <!-- 서브타이틀 (선택 — 날짜 또는 발표자 중 1개만) -->
    <p style="
      font-family:var(--b-font); font-size:20px;
      color:rgba(255,255,255,0.55);
      margin-top:24px;
    ">[서브타이틀 또는 날짜]</p>
  </div>
</section>
```

### 변형 B: Photo Split (텍스트 좌 + 이미지 우)

이미지를 오른쪽 패널로 분리. PPTX 모드에서도 안전.

```html
<!-- [Cover B] Photo Split Cover -->
<section class="slide active" id="s1" style="
  display:flex; flex-direction:row;
  background:var(--bg); overflow:hidden;
">
  <!-- 좌: 텍스트 패널 (45%) -->
  <div style="
    flex:0 0 580px; display:flex; flex-direction:column;
    justify-content:center; padding:80px 64px 80px 80px;
    background:var(--bg);
  ">
    <div style="width:40px; height:3px; background:var(--accent); margin-bottom:28px;"></div>
    <p style="
      font-family:var(--h-font); font-size:64px; font-weight:700;
      color:var(--text); line-height:1.1; letter-spacing:-0.02em;
    ">[덱 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:18px;
      color:var(--muted); margin-top:20px;
    ">[서브타이틀 또는 날짜]</p>
  </div>
  <!-- 우: 이미지 패널 (55% + 120% 확장) -->
  <div style="flex:1.4; overflow:hidden; position:relative; margin-left:-8px;">
    <img src="[이미지URL]" style="
      width:100%; height:100%; object-fit:cover;
    ">
    <!-- gradient blend (HTML 모드만 — PPTX 모드에서 제거) -->
    <div style="
      position:absolute; inset:0;
      background:linear-gradient(to right, var(--bg) 0%, transparent 40%);
      pointer-events:none;
    "></div>
  </div>
</section>
```

### 변형 C: 솔리드 배경 + 기하 장식 (이미지 없음)

이미지 없이 솔리드 컬러 배경 + 기하학적 장식 요소. 브랜드 색상 강조.

```html
<!-- [Cover C] Solid + Geometric Decoration -->
<section class="slide active" id="s1" style="
  position:relative; overflow:hidden;
  background:var(--primary); display:flex;
  align-items:center; justify-content:flex-start;
">
  <!-- 장식: 우측 하단 큰 원 (Pattern B 스타일) -->
  <div style="
    position:absolute; right:-80px; bottom:-80px;
    width:360px; height:360px; border-radius:50%;
    border:2px solid rgba(255,255,255,0.25);
    pointer-events:none;
  "></div>
  <div style="
    position:absolute; right:40px; bottom:40px;
    width:200px; height:200px; border-radius:50%;
    background:rgba(255,255,255,0.08);
    pointer-events:none;
  "></div>
  <!-- 장식: 좌상단 소형 원 -->
  <div style="
    position:absolute; left:60px; top:60px;
    width:80px; height:80px; border-radius:50%;
    border:1.5px solid rgba(255,255,255,0.2);
    pointer-events:none;
  "></div>
  <!-- 텍스트 -->
  <div style="
    position:relative; z-index:1;
    padding:0 120px;
  ">
    <p style="
      font-family:var(--h-font); font-size:72px; font-weight:800;
      color:#fff; line-height:1.1; letter-spacing:-0.03em;
      max-width:680px;
    ">[덱 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:20px;
      color:rgba(255,255,255,0.6); margin-top:24px;
    ">[서브타이틀]</p>
  </div>
</section>
```

### 변형 D: 다크 배경 + 톤온톤 아크 (Pattern F)

강한 단색 배경 + 같은 계열 더 어두운 아크. 세련된 임팩트.

```html
<!-- [Cover D] Dark + Tone-on-Tone Arc -->
<section class="slide active" id="s1" style="
  position:relative; overflow:hidden;
  background:#0B0E1A; display:flex;
  align-items:center; justify-content:flex-start;
">
  <!-- 아크 1: 우하단 대형 1/4 원 -->
  <div style="
    position:absolute; right:-120px; bottom:-120px;
    width:500px; height:500px; border-radius:50%;
    background:rgba(255,255,255,0.04);
    pointer-events:none;
  "></div>
  <!-- 아크 2: 아웃라인 원 -->
  <div style="
    position:absolute; right:-60px; bottom:-60px;
    width:380px; height:380px; border-radius:50%;
    border:1.5px solid rgba(255,255,255,0.10);
    pointer-events:none;
  "></div>
  <!-- × 마크 장식 -->
  <span style="
    position:absolute; right:120px; top:80px;
    font-size:24px; color:rgba(255,255,255,0.2);
    font-family:var(--b-font); pointer-events:none;
  ">×</span>
  <span style="
    position:absolute; left:80px; bottom:80px;
    font-size:18px; color:rgba(255,255,255,0.15);
    font-family:var(--b-font); pointer-events:none;
  ">×</span>
  <!-- 텍스트 -->
  <div style="position:relative; z-index:1; padding:0 120px;">
    <div style="
      display:inline-block; padding:6px 16px;
      background:var(--accent); border-radius:4px;
      font-family:var(--b-font); font-size:13px;
      color:#fff; letter-spacing:0.06em; text-transform:uppercase;
      margin-bottom:28px;
    ">[태그/카테고리]</div>
    <p style="
      font-family:var(--h-font); font-size:68px; font-weight:700;
      color:#fff; line-height:1.1; letter-spacing:-0.02em;
      max-width:700px;
    ">[덱 제목]</p>
    <p style="
      font-family:var(--b-font); font-size:18px;
      color:rgba(255,255,255,0.45); margin-top:20px;
    ">[날짜 / 발표자]</p>
  </div>
</section>
```

---

### 변형 E: 텍스트 2-col 균등 (1:1) — 선 분할

이미지 없음. 좌: 제목 / 우: 설명. 얇은 룰 라인 하나로만 구획. 차분하고 세련된 인상. Swiss·Editorial 계열.

```html
<!-- [Cover E] Text 2-Col Equal (1:1) — Rule Line -->
<section class="slide active" id="s1" style="
  flex-direction:row; background:var(--bg);
">
  <div style="
    flex:0 0 640px; display:flex; flex-direction:column;
    justify-content:center; padding:80px;
    border-right:2px solid var(--border);
  ">
    <p style="
      font-family:var(--b-font); font-size:12px; font-weight:700;
      color:var(--accent); letter-spacing:0.14em; text-transform:uppercase;
      margin-bottom:32px;
    ">[카테고리 라벨]</p>
    <p style="
      font-family:var(--h-font); font-size:72px; font-weight:900;
      color:var(--text); line-height:0.92; letter-spacing:-0.02em;
      text-transform:uppercase;
    ">[덱 제목]</p>
  </div>
  <div style="
    flex:1; display:flex; flex-direction:column;
    justify-content:flex-end; padding:80px;
  ">
    <p style="
      font-family:var(--b-font); font-size:20px; font-weight:400;
      color:var(--muted); line-height:1.55; max-width:400px;
      margin-bottom:40px;
    ">[설명 한두 줄]</p>
    <div style="width:40px; height:2px; background:var(--accent);"></div>
    <p style="
      font-family:var(--b-font); font-size:12px; font-weight:700;
      color:var(--muted); letter-spacing:0.1em; text-transform:uppercase;
      margin-top:16px;
    ">[날짜 / 버전]</p>
  </div>
</section>
```

---

### 변형 F: 타이포그래피 주도 — 여백 분할

패널도 선도 없다. 텍스트 덩어리의 위치·크기 차이가 구획을 만든다. 공간 전체가 캔버스. Swiss·Minimal.

```html
<!-- [Cover F] Typography-Led — Whitespace Division -->
<section class="slide active" id="s1" style="
  flex-direction:column; justify-content:space-between;
  background:var(--bg); padding:72px 96px;
">
  <div style="display:flex; justify-content:space-between; align-items:flex-start;">
    <p style="
      font-family:var(--b-font); font-size:11px; font-weight:700;
      color:var(--accent); letter-spacing:0.14em; text-transform:uppercase;
    ">[카테고리]</p>
    <p style="
      font-family:var(--b-font); font-size:11px; font-weight:700;
      color:var(--muted); letter-spacing:0.1em; text-transform:uppercase;
    ">[날짜]</p>
  </div>
  <p style="
    font-family:var(--h-font); font-size:120px; font-weight:900;
    color:var(--text); line-height:0.86; letter-spacing:-0.04em;
    text-transform:uppercase;
  ">[덱<br>제목]</p>
  <div style="display:flex; justify-content:space-between; align-items:flex-end;">
    <p style="
      font-family:var(--b-font); font-size:18px; font-weight:400;
      color:var(--muted); max-width:480px; line-height:1.5;
    ">[서브타이틀]</p>
    <div style="width:40px; height:2px; background:var(--accent);"></div>
  </div>
</section>
```

---

### 변형 G: 2-col 역순 (70:30) — 면 분할

타이포 좌측 대형 + 우측 좁은 액센트 패널. 일반 2-col과 무게 방향 역전. Bold·Magazine.

```html
<!-- [Cover G] Reversed 2-Col (70:30) — Fill Accent Right -->
<section class="slide active" id="s1" style="
  flex-direction:row; background:var(--bg);
">
  <div style="
    flex:1; display:flex; flex-direction:column;
    justify-content:space-between; padding:80px;
  ">
    <p style="
      font-family:var(--b-font); font-size:12px; font-weight:700;
      color:var(--accent); letter-spacing:0.14em; text-transform:uppercase;
    ">[카테고리]</p>
    <div>
      <p style="
        font-family:var(--h-font); font-size:96px; font-weight:900;
        color:var(--text); line-height:0.88; letter-spacing:-0.03em;
        text-transform:uppercase;
      ">[덱<br>제목]</p>
      <p style="
        font-family:var(--b-font); font-size:18px; font-weight:400;
        color:var(--muted); margin-top:28px; max-width:440px;
      ">[서브타이틀]</p>
    </div>
  </div>
  <div style="
    flex:0 0 280px; background:var(--primary);
    display:flex; flex-direction:column;
    justify-content:flex-end; padding:64px 48px;
  ">
    <p style="
      font-family:var(--b-font); font-size:13px; font-weight:700;
      color:rgba(255,255,255,0.6); letter-spacing:0.1em;
      text-transform:uppercase; line-height:2;
    ">[날짜]<br>[버전]</p>
  </div>
</section>
```

---

### 변형 H: 사선 분할 (Diagonal) — clip-path

사선 경계로 두 영역 분할. 역동적 인상. 2-col에서만 효과적. 3-col에는 사용 금지.

```html
<!-- [Cover H] Diagonal Split — clip-path -->
<section class="slide active" id="s1" style="
  position:relative; background:var(--bg); overflow:hidden;
">
  <div style="
    position:absolute; inset:0;
    background:var(--primary);
    clip-path:polygon(0 0, 52% 0, 34% 100%, 0 100%);
    pointer-events:none;
  "></div>
  <div style="
    position:relative; z-index:1; width:100%; height:100%;
    display:flex; align-items:stretch;
  ">
    <div style="
      flex:0 0 480px; padding:80px;
      display:flex; flex-direction:column; justify-content:space-between;
    ">
      <p style="
        font-family:var(--b-font); font-size:11px; font-weight:700;
        color:rgba(255,255,255,0.5); letter-spacing:0.14em; text-transform:uppercase;
      ">[카테고리]</p>
      <div>
        <p style="
          font-family:var(--h-font); font-size:80px; font-weight:900;
          color:#fff; line-height:0.9; letter-spacing:-0.02em;
          text-transform:uppercase;
        ">[덱<br>제목]</p>
        <div style="width:40px; height:3px; background:var(--accent); margin-top:32px;"></div>
      </div>
    </div>
    <div style="
      flex:1; padding:80px;
      display:flex; flex-direction:column; justify-content:flex-end;
    ">
      <p style="
        font-family:var(--b-font); font-size:20px; font-weight:400;
        color:var(--muted); line-height:1.55; max-width:360px; margin-bottom:32px;
      ">[설명 또는 부제]</p>
      <p style="
        font-family:var(--b-font); font-size:12px; font-weight:700;
        color:var(--muted); letter-spacing:0.1em; text-transform:uppercase;
      ">[날짜]</p>
    </div>
  </div>
</section>
```

---

## Section Title

섹션 구분 슬라이드. H1 단독 중앙 배치. 여백이 메시지.

### 구조 원칙

```
Visual (배경 색상 + 최소 장식): 60~70%
Text (섹션 번호 + 섹션명):       20~30%
White Space:                     40%+ (여백이 핵심)
```

### 변형 A: 심플 중앙 정렬

```html
<!-- [Section Title A] Centered -->
<section class="slide" id="sN" style="
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  background:var(--primary); overflow:hidden;
  position:relative;
">
  <!-- 섹션 번호 -->
  <p style="
    font-family:var(--b-font); font-size:14px;
    color:rgba(255,255,255,0.4); letter-spacing:0.12em;
    text-transform:uppercase; margin-bottom:20px;
  ">SECTION 01</p>
  <!-- 섹션명 -->
  <p style="
    font-family:var(--h-font); font-size:80px; font-weight:700;
    color:#fff; line-height:1.05; letter-spacing:-0.02em;
    text-align:center; max-width:800px;
  ">[섹션명]</p>
  <!-- 하단 구분선 -->
  <div style="
    width:60px; height:3px; background:var(--accent);
    margin-top:40px;
  "></div>
</section>
```

### 변형 B: 좌측 정렬 + 숫자 강조

```html
<!-- [Section Title B] Left + Number -->
<section class="slide" id="sN" style="
  display:flex; align-items:center;
  background:var(--bg); overflow:hidden;
  position:relative;
">
  <!-- 대형 섹션 번호 (배경 장식) -->
  <p style="
    position:absolute; left:60px; top:50%;
    transform:translateY(-50%);
    font-family:var(--h-font); font-size:280px; font-weight:900;
    color:var(--border); line-height:1; letter-spacing:-0.05em;
    user-select:none; pointer-events:none;
  ">01</p>
  <!-- 텍스트 -->
  <div style="
    position:relative; z-index:1;
    padding:0 80px 0 280px;
  ">
    <p style="
      font-family:var(--b-font); font-size:13px;
      color:var(--accent); letter-spacing:0.1em;
      text-transform:uppercase; margin-bottom:16px;
    ">PART ONE</p>
    <p style="
      font-family:var(--h-font); font-size:72px; font-weight:700;
      color:var(--text); line-height:1.1; letter-spacing:-0.02em;
    ">[섹션명]</p>
    <p style="
      font-family:var(--b-font); font-size:20px;
      color:var(--muted); margin-top:20px; max-width:480px;
    ">[섹션 한 줄 설명]</p>
  </div>
</section>
```
