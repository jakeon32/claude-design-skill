# 색상 시스템 규칙 (Color Rules)

슬라이드에 색상을 분배·적용하는 규칙. DSM이 결정한 토큰(palette, primary, secondary, accent)을 슬라이드에 어떻게 쓸지의 가이드.

> 외부 레퍼런스: `d:\Works\2026\claude-design\color-framework.md`

---

## 팔레트 결정 순서

1. 스타일 파일명 → color-framework.md Section 5에서 해당 행 확인
2. 배경 타입 판단 → Section 2 매트릭스 행 적용
3. Primary / Secondary / Accent Hex 결정

## 60-30-10 원칙

- 60% Primary: 메인 배경, 대영역
- 30% Secondary: 카드/패널 배경, 그래프 영역, 섹션 구분
- 10% Accent: CTA 버튼, 핵심 숫자, 강조 라인 — **슬라이드당 최대 3곳**

## 혼합 덱 Accent 통일

- Master Accent 1개 고정 → 전체 덱에서 변경 금지
- 10% 초과 위험 요소(라벨·구조적 텍스트)는 `#94A3B8` 중립색으로 격하

---

## 이미지 패널 그라데이션 블렌드 (Photo Panel Gradient Blend)

이미지가 전체 높이 또는 너비로 인접 패널과 함께 사용될 때, 이미지 위에 인접 패널의 배경색으로 페이드되는 그라데이션 오버레이를 적용한다.  
→ 이미지가 인접 패널로 자연스럽게 녹아드는 효과. 경계선 없이 레이아웃이 하나로 연결되어 보인다.

**방향 규칙**:
| 이미지 위치 | 그라데이션 방향 | 패턴 |
|------------|--------------|------|
| 오른쪽 | `to right` | `linear-gradient(to right, [왼쪽패널색] 0%, transparent 50%)` |
| 왼쪽 | `to left` | `linear-gradient(to left, [오른쪽패널색] 0%, transparent 50%)` |
| 아래쪽 | `to bottom` | `linear-gradient(to bottom, [위패널색] 0%, transparent 50%)` |
| 위쪽 | `to top` | `linear-gradient(to top, [아래패널색] 0%, transparent 50%)` |

**구현 패턴**:
```html
<div style="position:relative; overflow:hidden;">
  <img style="width:100%; height:100%; object-fit:cover;">
  <!-- 인접 패널 색상으로 페이드 — pointer-events:none 필수 -->
  <div style="position:absolute; inset:0;
    background:linear-gradient(to right, [인접패널배경색] 0%, transparent 50%);
    pointer-events:none;"></div>
</div>
```

**보더라인 처리**: 그라데이션 블렌드를 사용하는 경우 인접 패널 경계의 `border` 전체(`border-top/right/bottom/left` 모두)를 제거한다. 단축속성(`border:`)으로 설정된 경우도 마찬가지. 보더가 남아 있으면 그라데이션 효과가 무너진다.

**120% 할당 규칙 (Gradient Axis Extension)**:  
그라데이션 방향축 기준으로 포토 패널의 크기를 원래 할당량의 120%로 늘린다.  
→ 그라데이션이 사용할 "블리드 존"을 확보해 이미지 콘텐츠 손실을 방지.
```
flex 사용 시: flex 값 × 1.2  (예: flex:2 → flex:2.4)
고정 width 사용 시: width × 1.2
```
또한 `margin-left: -8px` (또는 그라데이션 방향 반대쪽 margin)을 추가해  
flex 경계 렌더링 seam을 그라데이션이 덮도록 약간 오버랩시킨다.

```html
<!-- 120% 할당 + seam 제거 패턴 (이미지가 오른쪽인 경우) -->
<div style="flex:2.4; overflow:hidden; position:relative; margin-left:-8px;">
  <img style="width:100%; height:100%; object-fit:cover;">
  <div style="position:absolute; inset:0;
    background:linear-gradient(to right, [인접패널색] 0%, transparent 50%);
    pointer-events:none;"></div>
</div>
```

**페이드 범위 기준**:
- `30%` — 날카로운 블렌드 (강한 대비 원할 때)
- `50%` — 자연스러운 블렌드 (기본값 권장)
- `65%` — 부드러운 블렌드 (이미지를 많이 살리고 싶을 때)

**생성 전 자기 체크에 추가**:
- [ ] 이미지가 인접 패널과 경계 없이 자연스럽게 연결되는가?

---

## 전체화면 배경 이미지 — z-index 3레이어 구조 (필수)

z-index 구조가 없으면 오버레이가 콘텐츠를 덮어 텍스트가 사라진다.

```html
<section style="position:relative; overflow:hidden;">
  <img style="position:absolute; inset:0; width:100%; height:100%;
    object-fit:cover; opacity:0.45; z-index:1; pointer-events:none;">
  <div style="position:absolute; inset:0;
    background:rgba(10,15,30,0.75); z-index:2; pointer-events:none;"></div>
  <div style="position:relative; z-index:3;">
    <!-- 모든 텍스트/버튼/통계 여기에 -->
  </div>
</section>
```

| 상황 | 이미지 opacity | 오버레이 opacity |
|------|---------------|-----------------|
| Cool/Dark 배경 + 어두운 이미지 | 0.35~0.50 | 0.70~0.85 |
| Warm/Light 배경 + 밝은 이미지 | 0.20~0.35 | 0.55~0.70 |
