# Slide Generation Rules — sda 제약 + 자가검수 단일 출처

> **Phase 5 진입용 stub** (2026-04-29). 이번 세션은 매핑 표 + 작업 가이드까지. 풀 룰 본문은 다음 세션(Phase 5 5A)에서 작성.
>
> **목적**: slide-qa-agent의 27개 코드 룰을 sda 생성 제약 + 자가검수 체크리스트로 흡수하기 위한 단일 출처. sda·slide-qa(개발 테스트용) 양쪽이 이 파일을 참조.
>
> **패러다임**: 만들기 → 검사 → 수정 ❌ → **제약 → 만들기 → 자가검증** ✅
>
> 결정 근거: [옵션 E 결정 노트](../../../../../../../C:/MyNote/groundk-vault/06%20Claude/claude-design-history/2026-04-29-option-e-decision.md) (옵시디안 vault 외부 참조 — 동일 내용 IMPROVEMENT_PLAN.md Phase 5 섹션에도 영속).

---

## 1. 매핑 결과 요약

slide-qa-agent.md 27개 검사 항목 → sda 현황:

| 카테고리 | 건수 | 항목 |
|---------|------|------|
| 🟢 sda 룰 + 자가검수 모두 있음 | 3 | G1, G2, G4 |
| 🟡 sda 룰은 있으나 자가검수 누락 | 16 | A3-A9, B1, B2, D1, D2, E1-E3, G3, G5 |
| 🔴 sda에 룰 자체 없음 | 8 | A1, A2, C1, C2, D3, H1, H2, H3 |

---

## 2. 27개 룰 매핑 표

> sda 룰 위치는 `agents/slide-deck-agent.md` 라인 번호 기준 (2026-04-29 본문 1364줄).

### Group A — HTML 구조 무결성 (9건)

| # | 항목 | 통과 기준 | sda 룰 | 자가검수 | 액션 |
|---|------|---------|--------|---------|------|
| A1 | 슬라이드 ID 연속 | `s1~sN` 누락·중복 없음 | ❌ | ❌ | 🔴 신설 |
| A2 | total 변수 일치 | `const total = N` = .slide 개수 | △ | ❌ | 🔴 신설 |
| A3 | 첫 슬라이드 active | s1에 `active` 클래스 | ✅ L700 | ❌ | 🟡 자가검수 |
| A4 | display 패턴 | `.slide{display:none}` + `.slide.active{display:flex}` | ✅ L621-622 | ❌ | 🟡 자가검수 |
| A5 | inline display 금지 | section 인라인 display 없음 | ✅ L662-672 | △ | 🟡 자가검수 |
| A6 | body padding 없음 | body padding 0 | ✅ 묵시 | ❌ | 🟡 자가검수 |
| A7 | stage radius 없음 | #deck/.stage radius 없음 | ✅ L593 | ❌ | 🟡 자가검수 |
| A8 | nav UI 금지 | button/nav 요소 없음 | ✅ L593 | ❌ | 🟡 자가검수 |
| A9 | @keyframes 금지 | CSS에 없음 (요청 시 예외) | ✅ L593 | ❌ | 🟡 자가검수 |

### Group B — 한국어 폰트 렌더링 (2건)

| # | 항목 | 통과 기준 | sda 룰 | 자가검수 | 액션 |
|---|------|---------|--------|---------|------|
| B1 | 한국어에 비한국어 폰트 금지 | Clash Display·Satoshi·Space Grotesk·Playfair·Cormorant·Fraunces·Canela·Editorial New·Neue Haas Grotesk·DM Serif Display·Plus Jakarta Sans 직접 지정 X | ✅ L752 | △ Inter만 | 🟡 강화 |
| B2 | Pretendard CDN 로딩 | `https://cdn.jsdelivr.net/gh/orioncactus/pretendard` | ✅ L617 | ❌ | 🟡 자가검수 |

### Group C — Letter-spacing 규칙 (2건)

| # | 항목 | 통과 기준 | sda 룰 | 자가검수 | 액션 |
|---|------|---------|--------|---------|------|
| C1 | 40px+ 음수 letter-spacing 금지 | display 폰트 자체 자간 좁음 | ❌ | ❌ | 🔴 신설 |
| C2 | -0.01em 이하 ⚠️ | 의도적 타이트닝 예외 | ❌ | ❌ | 🔴 신설 |

### Group D — 카운터 시스템 (3건)

| # | 항목 | 통과 기준 | sda 룰 | 자가검수 | 액션 |
|---|------|---------|--------|---------|------|
| D1 | `#counter.dark` 규칙 존재 | CSS 패턴 | ✅ L625 | ❌ | 🟡 자가검수 |
| D2 | lightSlides vs 실제 배경 일치 | 카운터 위치 영역 배경 | △ | ❌ | 🟡 자가검수 |
| D3 | 전체 다크 덱 예외 | lightSlides 비어 있어도 OK | ❌ | ❌ | 🔴 신설 |

### Group E — 그리드 다양성 (3건)

| # | 항목 | 통과 기준 | sda 룰 | 자가검수 | 액션 |
|---|------|---------|--------|---------|------|
| E1 | 커버 그리드 재사용 금지 | S1 그리드가 S2~SN에서 반복 X | ✅ L91 | ❌ | 🟡 자가검수 |
| E2 | 연속 동일 그리드 금지 | S(n) ≠ S(n+1) | ✅ L91 | ❌ | 🟡 자가검수 |
| E3 | 동일 그리드 ≤ 2회 | 같은 그리드 3회+ 금지 | ✅ L91 | ❌ | 🟡 자가검수 |

### Group G — 일반 규칙 (5건)

| # | 항목 | 통과 기준 | sda 룰 | 자가검수 | 액션 |
|---|------|---------|--------|---------|------|
| G1 | 본문 16px+ | font-size < 16 없음 | ✅ | ✅ L525 | 🟢 유지 |
| G2 | 금지 폰트 | Inter/Roboto/Arial/Helvetica 없음 | ✅ L1016 | ✅ L515 | 🟢 유지 |
| G3 | Pretendard CDN | jsdelivr | ✅ L617 | ❌ | 🟡 자가검수 |
| G4 | 캔버스 1280×720 | 고정 (1920×1080 금지) | ✅ | ✅ L512 | 🟢 유지 |
| G5 | body 어두운 배경 | #111 또는 어두운 계열 | ✅ L617 | ❌ | 🟡 자가검수 |

### Group H — 공간 문법 다양성 (3건)

| # | 항목 | 통과 기준 | sda 룰 | 자가검수 | 액션 |
|---|------|---------|--------|---------|------|
| H1 | 패널 채움 비율 | 스타일별 기대값 (Swiss ≤40%, Minimalist ≤20%, Brutalism 100% 등) | ❌ | ❌ | 🔴 신설 |
| H2 | S2 커버 유사성 | S2가 S1과 공간 문법 중복 X | ❌ | ❌ | 🔴 신설 |
| H3 | 스타일별 기대 공간 문법 | 패널 채움/타이포 주도/플로팅/룰 분리 | ❌ | ❌ | 🔴 신설 |

---

## 3. Phase 5 작업 7건 (다음 세션 가이드)

| ID | 작업 | 위치 | 입력 | 출력 |
|----|------|------|------|------|
| **5A** | 풀 룰 본문 작성 | 이 파일 | 본 매핑 표 + slide-qa-agent.md Group A-H 본문 | 27개 룰의 정확한 정의 + 통과 기준 + 자동 처리 가능 여부 명시 |
| **5B** | sda 신설 룰 8건 추가 | `agents/slide-deck-agent.md` | 5A의 A1·A2·C1·C2·D3·H1·H2·H3 | 각 룰을 생성 가이드 표현으로 sda에 명문화 |
| **5C** | sda 자가검수 16건 확장 | `agents/slide-deck-agent.md` (L398 Step 2 진입 검사 + L492 쇼케이스 자가검수 + L1306 Self-verification) | 5A의 16건 | sda 자가검수 체크리스트에 16건 추가 |
| **5D** | slide-qa-agent 강등 | `agents/slide-qa-agent.md` + `SKILL.md` | - | 운영 흐름 호출 폐지, 개발 테스트용 명시 |
| **5E** | SKILL.md MANDATORY GATE 정정 | `SKILL.md` | - | STEP 4 폐지, visual-refiner 위치 쇼케이스 직후로 이동, 본 작업은 새 레이아웃 시 조건부 |
| **5F** | STEP 5.5 ↔ 쇼케이스 컨펌 통합 | `SKILL.md` + `visual-refiner.md` | - | 쇼케이스 컨펌 = 디자인 컨펌 + QA 결과 컨펌 이중 의미 |
| **5G** | CHANGELOG·CLAUDE.md·메모리 룰 정정 | 메모리 + 워크스페이스 | - | "Current Version" 갱신 + project_test03_validation.md 메모리 정정 |

총 영향: 5~6 파일, **~500 lines**.

---

## 4. 패러다임 전환 원칙 (Phase 5 작업 시 절대 룰)

### 룰을 생성 제약으로 표현하는 방법

❌ **잘못된 표현 (검수 관점)**:
> "C1: font-size 40px 이상 요소에 음수 letter-spacing 없음 — 위반 시 자동 수정"

✅ **올바른 표현 (제약 관점)**:
> "40px 이상 디스플레이 텍스트는 letter-spacing을 0(생략) 또는 양수만 사용. 디스플레이 폰트(Clash Display·Satoshi·Space Grotesk 등)는 자체 자간이 이미 좁게 설계되어 음수 letter-spacing은 글자 충돌 유발."

### 자가검수는 안전망, 메인 룰은 제약

- 사용자(LLM 디자이너)가 룰 알고 시작 → 처음부터 지켜서 생성
- 자가검수는 LLM이 빠뜨릴 때 잡는 안전망 (보조 메커니즘)
- 자가검수 자체에 의존해 "사후 수정" 패턴으로 회귀 금지

### visual-refiner와의 경계

- 코드로 환원 가능한 정량 룰 = sda 제약 + 자가검수 (이 파일)
- 코드로 환원 불가한 정성 평가 = visual-refiner (5차원·시각 무게·Hero 명확성)
- visual-refiner는 본질적 QA로 유지. 폐지 대상 아님.

---

## 5. 영속 위치 cross-reference

| 항목 | 위치 |
|------|------|
| Phase 5 마스터플랜 | `D:\Works\2026\claude-design\IMPROVEMENT_PLAN.md` Phase 5 섹션 (로컬) + 옵시디안 `06 Claude/claude-design-improvement-plan.md` mirror |
| 옵션 E 결정 history | 옵시디안 `06 Claude/claude-design-history/2026-04-29-option-e-decision.md` |
| 결함 카탈로그 (M·O·Q·S 근거) | 로컬 `_test/sessions/2026-04-29_test03.md` + 옵시디안 `06 Claude/Sessions/2026-04-29-test03-skill-validation.md` |
| 단일 출처 룰 본문 (Phase 5 5A 진입 후) | 이 파일 |
| sda 룰 통합 (5B·5C 후) | `agents/slide-deck-agent.md` |
| slide-qa 강등 (5D 후) | `agents/slide-qa-agent.md` |
| 흐름 정정 (5E·5F 후) | `skills/claude-design/SKILL.md` |
