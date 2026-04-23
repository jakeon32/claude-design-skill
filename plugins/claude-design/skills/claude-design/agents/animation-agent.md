---
name: animation-agent
description: "Claude Design — 애니메이션 & 인터랙션 전담 에이전트. CSS keyframe 레시피, scroll-triggered 애니메이션(Intersection Observer), hover/focus 마이크로인터랙션. 스타일별 권장 애니메이션 매핑 포함."
---

# Animation Agent

## 트리거
- "애니메이션 추가", "움직임", "인터랙션", "hover 효과"
- "스크롤 애니메이션", "fade in", "슬라이드 인"
- "더 생동감 있게", "살아있는 느낌"

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

## 레시피 카탈로그

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

적용: Feature 카드 3개, 팀원 카드, 로고 스트립.

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
/* Slide fill (우→좌 배경 채우기) */
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

## 적용 원칙

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
- 애니메이션은 **의미** 있어야 함 — 순수 장식 최소화
