# Korean Typography & Localization Layer
source: d:\Works\2026\claude-design\font.md
applies: 한국어 콘텐츠 또는 한국 시장 대상 디자인 시 항상 적용

---

## 핵심 규칙 (designprompts.dev / superdesign 스타일 위에 덮어쓰기)

원래 스타일의 미학(레이아웃 구조, 컬러 로직, hierarchy)은 유지하되,
**타이포그래피와 스페이싱만 아래 규칙으로 재조정**.

### 폰트 스택 (우선순위)
```
Heading:  "Pretendard", "SUITE", system-ui, sans-serif
Body/UI:  "Pretendard", "Noto Sans KR", system-ui, sans-serif
```
- 스타일 원본의 영문 폰트(Inter, Outfit, Plus Jakarta Sans 등)는 영문 전용으로 유지 가능
- 한글이 포함되는 모든 텍스트는 Pretendard 우선 적용

### 크기 & 계층
```
H1 / 메인 타이틀:  40~56px, weight 700~900, line-height 1.1~1.25
H2:                32~40px, line-height 1.15
H3 / 섹션 제목:    24~28px, line-height 1.2
Body:              16~18px, line-height 1.65~1.8  ← 영어보다 넉넉히
Small / Caption:   13~14px, line-height 1.5
```

### 자간
```
Heading:  letter-spacing -0.02em ~ -0.04em  (너무 벌리지 말 것)
Body:     letter-spacing 0 ~ 0.02em
```

### 한글 특화 규칙
- 한 줄당 글자 수: 제목 10~18자, 본문 18~24자 제한
- 긴 제목은 자연스럽게 2줄 줄바꿈 유도
- 영어+한글 혼용: 영어는 Pretendard와 잘 맞는 weight 조정
- 과도한 UPPERCASE 피하기 (한글은 대문자 개념 약함)
- 슬라이드에서 텍스트 비율 영어 기준보다 15~25% 줄여 여백 확보
- Vertical rhythm: 한글 많을 경우 8px 배수 대신 4px 또는 6px 배수로 세밀 조정

---

## 스타일별 폰트 조합 추천

### 1. 범용 (거의 모든 프로젝트 — 1순위)
- Heading: **Pretendard Black / ExtraBold** (700~900)
- Body: **Pretendard Regular / Medium** (line-height 1.65~1.8)

### 2. 현대적·세련된 (현재 가장 핫)
- Heading: **SUITE ExtraBold / Black**
- Body: **SUITE Regular / Medium** 또는 Pretendard Medium

### 3. 피치덱·프레젠테이션 (강한 임팩트)
- Heading: **Pretendard Black**
- Body: **Noto Sans KR Medium** 또는 SUITE Medium
- 대안: Wanted Sans Bold + Pretendard Regular

### 4. 고급·프리미엄 브랜드
- Heading: **SUITE Black** 또는 Sandoll Gothic Neo Heavy
- Body: **Pretendard Light / Regular** (여백 넉넉히)
- 트렌드: Sandoll Press Bold (2026)

### 5. 미니멀·테크·기업
- Heading: **Pretendard ExtraBold**
- Body: **Pretendard Regular** 또는 Manrope / Plus Jakarta Sans (영문 혼용)
- 대안: IBM Plex Sans Bold + Pretendard Medium

### 6. 크리에이티브·따뜻한 브랜드
- Heading: **Pretendard Black**
- Body: **Paperlogy** 또는 Gmarket Sans
- 대안: Nanum Square Neo Bold + Pretendard

---

## DESIGN_SYSTEM 적용 시 override 방법

스타일의 DESIGN_SYSTEM.typography를 아래처럼 재작성:

```yaml
typography:
  heading_font: '"Pretendard", "SUITE", system-ui, sans-serif'
  body_font: '"Pretendard", "Noto Sans KR", system-ui, sans-serif'
  scale:
    h1: "48px"     # weight: 800-900, line-height: 1.1~1.25, letter-spacing: -0.03em
    h2: "36px"     # weight: 700, line-height: 1.15, letter-spacing: -0.02em
    h3: "24px"     # weight: 600, line-height: 1.2
    body: "17px"   # weight: 400, line-height: 1.7
    small: "13px"  # weight: 400, line-height: 1.5
  note: "Korean localization applied — Pretendard override"
```

---

## 트리거 조건 (언제 이 파일을 로드하는가)

- 사용자가 한국어로 콘텐츠 작성
- "한국 시장", "한국 사용자", "KR", "국내" 언급
- 한글이 포함된 텍스트/슬라이드 생성 요청
- 기본값: Jake(한국 디자이너)의 모든 작업에 적용
