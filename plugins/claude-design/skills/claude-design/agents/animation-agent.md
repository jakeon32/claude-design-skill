---
name: animation-agent
description: "Claude Design — 애니메이션 & 인터랙션 전담 에이전트. 두 모드 지원: ① CSS/JS 인터랙션(기본) — keyframe 레시피, scroll-triggered, hover 마이크로인터랙션. ② HyperFrames 비디오 렌더링 — HTML+GSAP → MP4 파이프라인, data-* 타임라인, 씬 전환. 사용자가 '영상', '비디오', 'MP4', '렌더링', 'HyperFrames'를 언급하면 모드 ②로 자동 분기."
---

# Animation Agent

## 모드 분기

| 키워드 | 모드 |
|--------|------|
| 애니메이션, hover, 스크롤, 인터랙션, 살아있는 느낌 | ① CSS/JS 인터랙션 |
| 영상, 비디오, MP4, 렌더링, HyperFrames, 녹화 | ② HyperFrames 비디오 |

---

## 스타일별 권장 애니메이션

| 스타일 계열 | 권장 | 금지 |
|-----------|------|------|
| minimal / editorial | fade-in, 미묘한 translate Y(20px→0) | bounce, elastic, 빠른 전환 |
| futuristic / saas | glitch, typing cursor, 슬라이드 | 너무 느린 전환 |
| playful / geometric | bounce, scale pop, 색상 전환 | 딱딱한 linear easing |
| brutalist | 즉각 전환(0ms), 하드 슬라이드 | 부드러운 ease |
| luxurious | 느린 fade(800ms+), parallax | 빠르고 튀는 효과 |
| organic / botanical | 웨이브, 블롭 변형, 천천히 | 기계적 직선 이동 |

---

## ① CSS/JS 인터랙션 레시피

### 1. Scroll Fade-In (범용)

```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('visible');
  });
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

적용: 섹션 제목, 카드, 이미지에 `class="reveal"` 추가.

---

### 2. Stagger (순차 등장)

```css
.stagger-item {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.stagger-item.visible {
  opacity: 1;
  transform: translateY(0);
}
```

```js
document.querySelectorAll('.stagger-item').forEach((el, i) => {
  el.style.transitionDelay = `${i * 0.1}s`;
  observer.observe(el);
});
```

---

### 3. Hover Scale (카드)

```css
.card {
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.card:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 12px 32px rgba(0,0,0,0.12);
}
```

---

### 4. CTA 버튼 애니메이션

```css
.btn-fill {
  position: relative;
  overflow: hidden;
  z-index: 0;
}
.btn-fill::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(255,255,255,0.15);
  transform: translateX(-100%);
  transition: transform 0.3s ease;
  z-index: -1;
}
.btn-fill:hover::before {
  transform: translateX(0);
}
```

---

### 5. Typing Cursor (SaaS / 터미널 스타일)

```css
.typing-cursor::after {
  content: '|';
  animation: blink 1s step-end infinite;
}
@keyframes blink {
  50% { opacity: 0; }
}
```

---

### 6. Marquee (로고 스트립 / Social Proof)

```css
.marquee-track {
  display: flex;
  gap: 48px;
  animation: marquee 20s linear infinite;
  width: max-content;
}
@keyframes marquee {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}
```

HTML: 로고 목록을 **두 번 반복**해서 이음매 없는 루프.

---

### 7. Blob 배경 (organic / wellness)

```css
.blob {
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  animation: morph 8s ease-in-out infinite;
}
@keyframes morph {
  0%, 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
  50%       { border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%; }
}
```

---

## 적용 원칙 (CSS/JS 공통)

- **duration**: 빠른 피드백 200-300ms / 등장 500-700ms / 느린 강조 800ms+
- **easing**: `ease` 기본 / 자연스러운 등장 `cubic-bezier(0.16, 1, 0.3, 1)` / 즉각 `steps(1)`
- **prefers-reduced-motion** 반드시 적용:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      transition-duration: 0.01ms !important;
    }
  }
  ```

---

## ② HyperFrames 비디오 렌더링

HTML + CSS + GSAP 타임라인으로 작성하면 `npx hyperframes render`가 MP4로 변환한다.

### 사전 요건

```bash
npx hyperframes doctor          # Node 22+, FFmpeg, Chrome 확인
npx hyperframes browser ensure  # Chrome Headless Shell 없으면 설치
```

### 프로젝트 구조

```
my-video/
├── index.html    ← 컴포지션 (data-* + GSAP)
└── output.mp4    ← 렌더 결과
```

### 핵심 HTML 패턴

```html
<!-- 루트 컴포지션 -->
<div id="main" data-composition-id="main"
     data-width="1920" data-height="1080"
     data-start="0" data-duration="10">

  <!-- 씬 1: 처음부터 보임 (no style) -->
  <div class="scene clip" id="s1"
       data-start="0" data-duration="4" data-track-index="0">
    <div class="scene-content">
      <h1 id="s1-title">제목</h1>
      <p id="s1-sub">부제목</p>
    </div>
  </div>

  <!-- 씬 2: 처음엔 숨김 -->
  <div class="scene clip" id="s2"
       data-start="4" data-duration="6" data-track-index="0"
       style="visibility:hidden;">
    <div class="scene-content">
      <h1 id="s2-title">두 번째 씬</h1>
    </div>
  </div>
</div>
```

**씬 레이아웃 규칙**:
- `.scene-content`는 반드시 `width:100%; height:100%; padding:Npx;` + flex
- 절대 하드코딩 `top:/left:` 금지 — padding으로 내부 여백 처리
- 데코 요소만 `position:absolute` 허용

### GSAP 타임라인 규칙

```html
<script>
  window.__timelines = window.__timelines || {};
  var tl = gsap.timeline({ paused: true }); // 반드시 paused

  // --- 씬 visibility 토글 (autoAlpha 필수) ---
  tl.set("#s1", { autoAlpha: 0 }, 4.0);   // s1 종료 시점
  tl.set("#s2", { autoAlpha: 1 }, 4.0);   // s2 시작 시점

  // --- 씬 1 입장 애니메이션 ---
  tl.from("#s1-title", { y: 60, autoAlpha: 0, duration: 0.7, ease: "power3.out" }, 0.2);
  tl.from("#s1-sub",   { y: 30, autoAlpha: 0, duration: 0.5, ease: "power2.out" }, 0.6);

  // --- 씬 2 입장 ---
  tl.from("#s2-title", { x: -60, autoAlpha: 0, duration: 0.6, ease: "expo.out" }, 4.2);

  // 마지막 씬만 exit 허용
  tl.to("#s2-title", { autoAlpha: 0, duration: 0.4, ease: "power2.in" }, 9.4);

  window.__timelines["main"] = tl; // key = data-composition-id 값과 일치
</script>
```

**금지 사항**:
- `repeat: -1` → `repeat: Math.ceil(duration / cycle) - 1`로 계산
- `Math.random()`, `Date.now()` → 결정론적 값 사용
- `video.play()` / `audio.play()` → 프레임워크가 제어
- 마지막 씬이 아닌 곳에서 `gsap.to(..., { opacity: 0 })`
- async/setTimeout 안에서 타임라인 생성

### 씬 전환: Shader Transition

```html
<!-- 셰이더 앵커 씬은 opacity:0 -->
<div class="scene clip" id="s3" data-start="8" data-duration="4"
     data-track-index="0" style="opacity:0;">...</div>
<div class="scene clip" id="s4" data-start="12" data-duration="4"
     data-track-index="0" style="opacity:0;">...</div>
```

```html
<script src="https://cdn.jsdelivr.net/npm/@hyperframes/shader-transitions/dist/index.global.js"></script>
<script>
  // 첫 번째 앵커는 명시적으로 표시해야 함
  tl.set("#s3", { opacity: 1 }, 8.0);

  window.HyperShader.init({
    bgColor: "#0a0a0d",
    scenes: ["s3", "s4"],
    timeline: tl,
    transitions: [{ time: 11.75, shader: "cinematic-zoom", duration: 0.5 }]
  });
</script>
```

사용 가능한 셰이더 14종:
`domain-warp`, `ridged-burn`, `whip-pan`, `sdf-iris`, `ripple-waves`,
`gravitational-lens`, `cinematic-zoom`, `chromatic-split`, `swirl-vortex`,
`thermal-distortion`, `flash-through-white`, `cross-warp-morph`, `light-leak`, `glitch`

| 에너지 | 셰이더 |
|--------|--------|
| 차분·에디토리얼 | `cross-warp-morph`, `light-leak`, `domain-warp` |
| 중간·프로페셔널 | `cinematic-zoom`, `whip-pan`, `sdf-iris` |
| 강렬·공격적 | `glitch`, `chromatic-split`, `ridged-burn` |
| 몽환·미스터리 | `gravitational-lens`, `ripple-waves`, `swirl-vortex` |

**규칙**: 6-8 씬 영상에 셰이더 2개가 적정. 모든 컷에 셰이더 사용 금지.

### 렌더링 워크플로우

```bash
npx hyperframes lint    # 0 errors 확인 후 진행
npx hyperframes render . -o output.mp4   # 디렉토리를 인자로 (index.html 아님)
```

렌더 옵션:
```bash
npx hyperframes render . -o out.mp4 --fps 60
npx hyperframes render . -o out.mp4 --resolution 3840x2160
```

### HyperFrames GSAP 패턴 레퍼런스

**카운터 애니메이션** (숫자 올라가기):
```js
var obj = { v: 0 };
tl.to(obj, {
  v: 1900000000000,
  duration: 2.0, ease: "power2.out",
  onUpdate: function() {
    document.getElementById("stat").textContent = "$" + (obj.v / 1e12).toFixed(1) + "T";
  }
}, 3.5);
```

**Breathing Float** (mid-scene 유지 동작):
```js
tl.to("#logo", { y: -5, duration: 1.5, ease: "sine.inOut", yoyo: true, repeat: 1 }, 1.2);
```

**Character Stagger** (글자 순차 등장):
```html
<h1><span class="char">H</span><span class="char">i</span></h1>
```
```js
tl.from(".char", {
  y: 60, autoAlpha: 0, duration: 0.5, ease: "power3.out",
  stagger: { each: 0.12, from: "start" }
}, 0.3);
```

**Bar Chart Fill**:
```js
["#bar1","#bar2","#bar3"].forEach(function(sel, i) {
  tl.from(sel, { scaleY: 0, transformOrigin: "bottom", duration: 0.6, ease: "expo.out" }, 2.0 + i * 0.15);
});
```

**SVG Stroke Draw**:
```html
<path id="line" stroke-dasharray="440" stroke-dashoffset="440" .../>
```
```js
tl.to("#line", { strokeDashoffset: 0, duration: 1.0, ease: "power2.out" }, 1.5);
```

**Grain 텍스처** (SVG filter 금지 → CSS radial-gradient 사용):
```css
.grain {
  position:absolute; inset:0; pointer-events:none; z-index:50; opacity:0.18;
  background-image:
    radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1.2px),
    radial-gradient(rgba(0,0,0,0.18) 1px, transparent 1.2px);
  background-size: 3px 3px, 5px 5px;
  background-position: 0 0, 1px 2px;
  mix-blend-mode: overlay;
}
```

### 필수 CDN 스크립트 순서

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@hyperframes/core/dist/hyperframe.runtime.iife.js"></script>
<!-- 셰이더 전환 사용 시 -->
<script src="https://cdn.jsdelivr.net/npm/@hyperframes/shader-transitions/dist/index.global.js"></script>
```

순서 변경 금지. 렌더러가 CDN 스크립트를 자동 인라인 처리한다.

### 씬 타이밍 가이드

| 텍스트 양 | 권장 씬 길이 |
|-----------|-------------|
| 없음 (로고, 아이콘) | 1.5-2s |
| 1-3단어 | 2-3s |
| 4-10단어 (헤드라인+부제목) | 3-4s |
| 11-20단어 | 4-6s |
| 21-35단어 | 6-8s |

마지막 입장 애니메이션은 씬 길이의 50% 시점 이전에 완료해야 함.
