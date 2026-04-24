# Output Common — 공통 출력 패턴

슬라이드(slide-deck-agent)와 문서(document-agent) 양쪽에서 공유하는 패턴.
각 에이전트는 이 파일을 참조하고 모드별 차이만 자체 파일에 정의한다.

---

## 1. Preview Loop (Chrome DevTools MCP — 필수)

모든 HTML 출력 후 반드시 아래 순서로 실행.

```
1. 저장   → d:\tmp\preview.html (슬라이드: slides.html / 문서: document.html)
2. 열기   → mcp__chrome-devtools__new_page("file:///d:/tmp/preview.html")
            또는 기존 탭이면 navigate_page(type="reload", ignoreCache=true)
3. 스크린샷 → mcp__chrome-devtools__take_screenshot()
4. 표시   → 채팅에 스크린샷 노출 + 수정 요청 대기
5. 수정   → 파일 저장 → navigate reload → 스크린샷 반복
6. 완료   → "✅ 변경 적용. 추가 수정 또는 핸드오프 요청."
```

**다중 시안(N가지 변형):**
```
d:\tmp\preview-v1.html, v2.html, v3.html 각각 저장
→ 각각 new_page + take_screenshot (병렬 실행)
→ 스크린샷 나란히 표시 → 선택한 번호로 계속
```

---

## 2. Self-contained HTML 보일러플레이트

빌드 없이 브라우저에서 바로 열리는 단일 파일 기본 구조.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[제목]</title>
<!-- Pretendard (한국어 필수) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<!-- Tailwind (Prototype/Slide에서만) -->
<!-- <script src="https://cdn.tailwindcss.com"></script> -->
<style>
  *{ margin:0; padding:0; box-sizing:border-box; word-break:keep-all; }
  body { font-family:'Pretendard','Apple SD Gothic Neo',sans-serif; }
</style>
</head>
<body>
  <!-- 콘텐츠 -->
</body>
</html>
```

**모드별 추가 CDN:**
- 슬라이드: Tailwind CDN + 아이콘 (Heroicons SVG 인라인 또는 unpkg)
- 문서: Pretendard만 (Tailwind 불필요, 자체 CSS로 충분)

---

## 3. DESIGN_SYSTEM 소비 패턴

모든 Generator 에이전트는 DESIGN_SYSTEM 블록을 참조하여 아래를 적용한다.

```
colors.primary     → 주요 강조색, CTA, 링크
colors.secondary   → 카드·패널 배경, 보조 그래픽 영역
colors.accent      → 슬라이드당 최대 3곳 / 문서에서는 L2 좌측 바
colors.background  → 페이지/슬라이드 배경
colors.text        → 본문 색상
colors.text_muted  → 설명·캡션·레이블

typography.heading_font → 제목 폰트 (없으면 Pretendard)
typography.body_font    → 본문 폰트 (없으면 Pretendard)
typography.scale        → h1/h2/h3/body/small px값 참조

spacing.base    → 8px 배수 기준
spacing.section → 섹션 간 여백
radius          → 카드·버튼 border-radius
shadow          → 기본 box-shadow
```

DESIGN_SYSTEM 없이 생성 시작 불가. 없으면 DesignSystemManager 먼저 실행.

---

## 4. 한국어 타이포그래피 자동 적용 조건

아래 조건 중 하나라도 해당하면 `references/korean-typography.md` 로드 후 적용:
- 한국어로 입력된 콘텐츠
- "한국 시장·KR·국내·한국어" 언급
- Jake의 모든 작업 (기본 적용)

적용 내용 요약:
```
font-family: 'Pretendard', 'Apple SD Gothic Neo', sans-serif
line-height (body): 1.65~1.8 (영어 대비 1.1~1.3배)
letter-spacing (heading): -0.02~-0.04em
한 줄 글자 수: 제목 10~18자, 본문 18~24자
word-break: keep-all (줄바꿈 제어)
```

---

## 5. 색상 규칙 요약 (60-30-10)

```
60% Primary   → 메인 배경, 대영역
30% Secondary → 카드·패널 배경, 섹션 구분
10% Accent    → CTA·강조 숫자·핵심 라인 (슬라이드: 최대 3곳)
```

Accent 초과 요소(라벨·구조적 텍스트) → `#94A3B8` 중립색으로 격하.

---

## 6. Anti-Slop 공통 규칙

모든 출력에서 금지:
- 퍼플 그라데이션 (`#7C3AED` 계열 그라데이션)
- box-shadow 3개 이상 중첩
- 모든 카드에 emoji 아이콘 남발
- Inter 폰트 고집 (Pretendard 우선)
- CSS剪影(SVG로 그린 사람 얼굴·제품 모형)로 실제 이미지 대체
- generic AI 템플릿 느낌 (모두가 똑같이 생긴 그라데이션 히어로 섹션)

---

## 7. 완성본 저장 경로 규칙

```
작업 중 프리뷰:   d:\tmp\[type].html
완성본:          d:\Works\2026\claude-design\_test\outputs\[name]-[type].html
```

`[type]`: slides / document / prototype / other
