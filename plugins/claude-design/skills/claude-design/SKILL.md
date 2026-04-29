---
name: claude-design
description: "Claude Design methodology skill v3 — Claude Code에서 디자인 결과물 생성 (프로토타입, 슬라이드, A4 문서, 자유형식). 31+ 스타일 라이브러리 자동 추천 + 4개 모드 + agent orchestration. Trigger: 디자인 만들어줘, 프로토타입, 슬라이드, 슬라이드 덱, 피치덱, 발표자료, PPT, PPTX, 랜딩페이지, 매뉴얼, 가이드, A4 문서, 'Claude Design v3 시작해', design, prototype, slide deck, pitch deck, landing page, dashboard, email template, social graphic, banner, infographic. Do NOT use for: code-only implementation without design intent, pure content writing."
---

# Claude Design Skill

Claude Design 워크플로우를 Claude Code에서 재현하는 마스터 스킬. 같은 콘텐츠를 31+ 스타일로 즉시 재해석.

**Core Philosophy**: 모드 선택 + 콘텐츠 수집 → DESIGN_SYSTEM 확정 → 모드별 생성 → 핸드오프

## Activation

- `/claude-design` 또는 자연어 트리거(description 키워드 매칭) → 자동 진입
- `"Claude Design 시작해"` → MANDATORY GATE 즉시 진입

## Agent Orchestration

```
ProjectPlanner → DesignSystemManager → Generator(모드별) → [QA] → VisualRefiner → Handoff
                                       │                    │
                                       ├─ ① prototype-agent │
                                       ├─ ② slide-deck-agent → slide-qa-agent (자동·필수)
                                       │     └─ slide-pptx-agent (선택 — "PPTX로" 요청 시)
                                       ├─ ③ other-agent
                                       └─ ④ document-agent

선택적 병렬: copywriting / animation / responsive / accessibility
```

**규칙**:
- DESIGN_SYSTEM 미확정 시 Generator 실행 불가
- Generator 종료 후 QA 단계(slide-qa-agent)와 VisualRefiner는 **메인이 자동 호출 의무** — 메인이 직접 자체 처리 금지
- 전문 에이전트(copywriting/animation 등)는 명시 요청 또는 QA 신호로 호출

## 트리거 감지 후 강제 진입 절차 (MANDATORY GATE)

트리거 워드 감지 즉시 — HTML/코드 생성 전 반드시 아래 순서를 실행한다.
**어떤 생성 단계도 이 게이트를 통과하지 않으면 실행 불가.**

```
STEP 1. project-planner 위임 (Agent tool 호출 — subagent_type: "claude-design:project-planner")
  → BRIEF 출력 (mode + content + language + content_signals + style_assets)
  → 내부 처리: 모드 선택 / 콘텐츠·원본 수집 / 언어(KR/EN) 판단 / 신호(mood·industry·tone·audience·complexity) 추출 / 스타일 자산 수집

STEP 2. design-system-manager 위임 (Agent tool 호출 — subagent_type: "claude-design:design-system-manager")
  → 입력: BRIEF
  → 내부 처리: 자동 추천 (top 3 + "직접 원하는 느낌 있나요?" 동시 질문) / 사용자 컨셉 선택 / 모드별 출력 환경 반영 / 한국어 자동 병합 / 자산 보강
  → 출력: DESIGN_SYSTEM 블록 + 확정 컨셉

STEP 3. 모드별 에이전트 위임 (Agent tool 호출 — 4모드 통일)
  → 입력: BRIEF + DESIGN_SYSTEM + 확정 컨셉
  → 모드별 에이전트가 시각 프리뷰·선택·본 작업까지 일임

  ① Prototype     → Agent tool 호출 (subagent_type: "claude-design:prototype-agent")
  ② Slide Deck    → Agent tool 호출 (subagent_type: "claude-design:slide-deck-agent") ★ 2회 호출 패턴 — 아래 참조
  ③ Other         → Agent tool 호출 (subagent_type: "claude-design:other-agent")
  ④ Document      → Agent tool 호출 (subagent_type: "claude-design:document-agent")

STEP 4 (Slide Deck 모드 자동·필수). slide-qa-agent 위임 (Agent tool 호출 — subagent_type: "claude-design:slide-qa-agent")
  → 트리거: slide-deck-agent 2차 호출 종료 직후 — 메인이 자동 발동
  → 입력: 완성된 deck.html 경로
  → 산출: Tier 1·2·3·4 코드 검수 리포트 + 자동 수정 결과
  → **금지**: 메인이 slide-qa-agent를 건너뛰고 자체 코드 분석으로 대체. sda의 self-screenshot은 시각 검증일 뿐 코드 분석(폰트·letter-spacing·그리드·공간 문법)을 대체하지 않음.

STEP 5 (모든 모드 자동·필수). visual-refiner 위임 (Agent tool 호출 — subagent_type: "claude-design:visual-refiner")
  → 트리거: STEP 3 (또는 STEP 4) 종료 직후 — 메인이 자동 발동
  → 입력: 완성된 HTML 경로 + DESIGN_SYSTEM
  → 산출: 스크린샷 시각 QA + 5차원 디자인 품질 평가(25점) + **수정 제안(diff)** — 자동 적용 X
  → **금지**: 메인이 직접 take_screenshot으로 visual QA를 처리. visual-refiner sub-agent 호출이 필수.
  → **금지**: visual-refiner의 자율 Edit/Write tool 호출 (visual-refiner.md 절대 규칙). visual-refiner는 평가·제안만 출력.

STEP 5.5 (자동·필수 게이트). 사용자 컨펌 게이트 — visual-refiner 제안 처리
  → 트리거: STEP 5 종료 직후 — 메인이 visual-refiner 제안을 받아 사용자에게 컨펌 요청
  → 메인 행동:
    (a) visual-refiner 제안 블록을 사용자에게 그대로 보여줌 (요약 X — 원본 제안 출력)
    (b) "다음 중 선택해주세요" 한 줄 명시: 전부 적용 / 일부 선택 / 넘어가기 / 직접 수정안 제시
    (c) 사용자 응답 수신할 때까지 STEP 6 진입 금지
    (d) 사용자 응답 후 메인이 Edit tool로 적용 (visual-refiner 재호출 X — 메인이 직접 적용)
    (e) 적용 후 필요 시 visual-refiner 재호출해 결과 재검증 (사용자 요청 시에만)
  → **❌ 0건 + ⚠️ 0건이면 게이트 스킵 가능**: 메인이 "QA 통과 — 제안 없음. 핸드오프로 진행합니다" narrate 후 STEP 6 직행
  → **금지**: 사용자 컨펌 없이 메인이 자율적으로 visual-refiner 제안 적용. 사용자에게 알리지 않고 산출물 변경.
  → **금지**: 메인이 제안을 요약·축약해 사용자가 무엇이 바뀔지 정확히 모르게 만드는 행위.

STEP 6. 결과물 핸드오프 (사용자에게 전달)
  → DESIGN_SYSTEM + 산출물 경로 + QA 리포트 요약 + (STEP 5.5 적용 내역 — 있으면) + 다음 단계 옵션

STEP 7 (선택 — "PPTX로" 요청 시). slide-pptx-agent 위임 (Agent tool 호출 — subagent_type: "claude-design:slide-pptx-agent")
  → 입력: 완성된 HTML 슬라이드 경로 + DESIGN_SYSTEM
  → 산출: .pptx 파일 (편집 가능한 PowerPoint) — 변환 시점에 자동 호환 처리(gradient → solid, div/span → p 등)
```

**STEP 4·5 자동 호출 강화 (2026-04-29 검증 결과 반영)**:
실제 테스트에서 메인이 slide-qa-agent와 visual-refiner를 sub-agent로 호출하지 않고 자체 처리하는 패턴이 발생했음. 사용자 요청은 "QA 단계 거치기"가 아니라 "디자인 결과물 받기"이기 때문에 메인이 효율을 위해 단계 통합 시도. 이는 **mandate 위반**:
- slide-qa-agent의 코드 분석(Tier 1·2·3·4)은 sub-agent의 시스템 프롬프트로 동작해야 깊이 있음. 메인의 ad-hoc 검토로 대체 불가.
- visual-refiner의 5차원 평가도 sub-agent의 심사 기준 적용 필요.
- 자동 호출 누락 시 사용자에게 "QA를 건너뛰었다"는 사실을 알리지 않으면 검증 안 된 결과물이 핸드오프됨.

**STEP 5.5 사용자 컨펌 게이트 신설 (2026-04-29 Phase 2 강화)**:
이전엔 visual-refiner가 자체 판단으로 "자동 수정"을 적용해 산출물을 변경했음. 사용자 신뢰 보호 위해 변경:
- visual-refiner는 **평가·제안만** (visual-refiner.md 절대 규칙). Edit/Write 자율 호출 금지.
- 메인이 제안을 받아 사용자에게 **명시 컨펌** 요청 → 사용자 응답 수신 후에만 Edit tool로 적용.
- ❌·⚠️ 0건이면 게이트 스킵 — "QA 통과" narrate 후 STEP 6 직행.
- 자동 적용은 사용자가 "전부 적용" 명시할 때만 가능. 사일런트 적용 절대 금지.

**큰 방향 변경 시 예외**: 사용자가 "컨셉 자체 다시" 같은 큰 변경을 요청하면 메인이 STEP 2로 돌아가 DSM 재호출. 부분 수정·시각 미세 조정은 sub-agent 안에서 처리.

### ★ Slide Deck 모드 — 메인 2회 호출 패턴 (필수)

slide-deck-agent는 **반드시 두 단계로 호출**한다. 한 번의 호출로 본 작업까지 끌고 가지 않는다.

```
[1차 호출] subagent_type: "claude-design:slide-deck-agent"
  목적: 쇼케이스 5장 (Cover 3안 + 본문 2안) 생성 + showcase-grid.html 브라우저 실행
  메인 BRIEF에 명시할 것:
    - "Step 1 → Step 2 쇼케이스까지만 진행. 본 작업 진입 금지."
    - 사용자 컨펌 받기 전엔 전체 N장 빌드 시도 금지
  산출물: showcase.html, showcase-grid.html, 5장 PNG, grid PNG

[메인이 사용자 컨펌 응답 수신]
  - "Cover-B로 가자" / "A안 좋다" / "쇼케이스 OK" / "본 작업 진행" 등
  - 컨펌이 없거나 NG면 1차 호출에 SendMessage로 재작업 지시

[2차 호출] subagent_type: "claude-design:slide-deck-agent" (또는 1차 agentId에 SendMessage)
  목적: 컨펌된 쇼케이스 산출물을 본 작업 N장으로 확장
  메인 BRIEF에 명시할 것:
    - 사용자 컨펌 응답 원문 인용 ("사용자가 'Cover-B로' 답변함")
    - 쇼케이스 산출물 그대로 재사용 원칙 (재디자인 금지)
  산출물: 본 작업 N장 deck.html + color-tuner.html (★ 페어 의무 — 둘 다 출력)

[메인 자동 후속 — 2차 종료 직후 즉시 발동]
  → STEP 4: slide-qa-agent 위임 (코드 검수 Tier 1·2·3·4)
  → STEP 5: visual-refiner 위임 (5차원 평가 + 수정 제안 — 자동 적용 X)
  → STEP 5.5: 사용자 컨펌 게이트 — 제안 보여주고 응답 대기 (❌·⚠️ 0건이면 스킵)
  → STEP 6: 핸드오프
  메인이 위 4단계를 자체 처리로 대체 금지 — 각 sub-agent를 명시적으로 호출. STEP 5.5는 사용자 응답 없이 STEP 6 진입 금지.
```

**금지 패턴**:
- 메인이 1차 호출에서 "13~14장 자동 빌드해" 같은 본 작업 직접 지시
- 사용자 컨셉 제공받았다고 쇼케이스 생략
- 분량 적다고(3~5장) 쇼케이스 생략
- 컨펌 응답 없이 2차 호출 진입

**왜 메인이 강제하는가**: slide-deck-agent.md 자체 절대 규칙(쇼케이스 의무)이 있지만, 메인 BRIEF가 본 작업을 직접 지시하면 에이전트가 SKILL 의무를 무시할 수 있음. 메인이 호출 패턴 자체를 2회로 분리해 구조적으로 막는다.

**핵심 원칙**:
- 메인은 큰 흐름(에이전트 호출 순서)만 관장. 각 sub-agent 내부 루프(사용자 OK·재시도·반복)에 간섭 안 함.
- sub-agent끼리 직접 호출 금지 — 메인이 orchestrate.
- 각 에이전트 파일이 그 모드의 유일한 생성 규칙 소스 — SKILL.md는 흐름만 정의.

## 6-Step Pipeline (+ 5.5 게이트)

| # | Step | Owner | 단일 출처 |
|---|------|-------|----------|
| 1 | 모드 선택 + 콘텐츠 수집 + 신호 추출 | project-planner | `agents/project-planner.md` |
| 2 | DESIGN_SYSTEM 확정 + 컨셉 추천 | design-system-manager | `agents/design-system-manager.md` |
| 3 | 생성 (모드별 빌드) | 모드별 generator | `agents/[mode]-agent.md` |
| 4 | 코드 QA (Slide Deck 모드만) | slide-qa-agent | `agents/slide-qa-agent.md` |
| 5 | 시각 QA + 5차원 평가 + **수정 제안** | visual-refiner | `agents/visual-refiner.md` |
| 5.5 | **사용자 컨펌 게이트** (제안 → Y/일부/스킵) | (메인) | MANDATORY GATE STEP 5.5 |
| 6 | 핸드오프 (적용 내역 포함) | (메인) | DESIGN_SYSTEM + 산출물 경로 + QA 리포트 + 적용 diff |

세부 절차는 owner 에이전트.md / reference 단일 출처. SKILL.md는 흐름만 정의 (MANDATORY GATE 참조).
Step 4·5는 메인의 자동 호출 의무 — 직접 자체 처리 금지. Step 5.5는 사용자 컨펌 의무 — 사일런트 적용 금지.

## Progress Reporting (사용자 가시성 — 필수)

Claude Code의 `Agent` tool은 sub-agent가 끝날 때까지 메인 스레드에 한 메시지만 돌아온다 → sub-agent 내부 텍스트는 종료 시점에 한 번에 dump되며 마디별 streaming은 메인 채팅에 visible하지 않다 (2026-04-29 검증 결과). 따라서 **사용자 가시성은 메인 스레드의 narration이 결정**한다.

### 메인 스레드 의무 (필수)

1. **TodoWrite 선행** — 2개 이상 phase가 예상되는 작업은 시작 시 phase 전체를 TodoWrite로 등록.
   Slide Deck 모드 표준 phase: BRIEF / DESIGN_SYSTEM / 쇼케이스 / 본 작업 / **slide-qa(코드)** / **visual-refiner(시각)** / **사용자 컨펌 게이트** / 핸드오프 (★ QA·게이트 분리 — 단일 phase로 묶지 말 것)
2. **Agent 호출 직전 — 예상 마디 미리 narrate** (3줄 형식):
   ```
   "[에이전트명] 실행 — [목적 1줄]"
   "예상 마디: [마디1] → [마디2] → ... → [통합 결과]"
   ```
   예:
   ```
   "slide-qa-agent 실행 — Tier 1·2·3·4 코드 검수 시작"
   "예상 마디: Tier 1 (자동수정) → Tier 2 (블로킹) → Tier 3 (경고) → Tier 4 (디자인 정보) → 통합 리포트"
   ```
3. **Agent 반환 직후 — 결과를 마디별로 분해 narrate**:
   ```
   "[에이전트명] 완료. 결과:
    - [마디1]: [수치·요약]
    - [마디2]: [수치·요약]
    - ...
    [핵심 1줄 요약]"
   ```
   예:
   ```
   "slide-qa-agent 완료. 결과:
    - Tier 1 (자동수정): 5건 (A5×3, B1×2)
    - Tier 2 (블로킹): 0건
    - Tier 3 (경고): 3건 (C1, E3, G1)
    - Tier 4 (디자인 정보): 2건 (H1, H2)
    종합: 위반 0 · 경고 3 · 자동수정 완료, 핸드오프 가능 수준."
   ```
4. **TodoWrite 마킹** — 호출 직전 해당 phase `in_progress`, 반환 후 `completed` (+ 다음 phase `in_progress`)
5. **사용자 입력 대기 시점**도 명시 — `"... 컨펌 대기 중"` 한 줄

### Sub-agent 의무 (best-effort)

Sub-agent는 종료 시 **통합 결과(표·요약)** 1개를 emit한다. 이게 메인에 visible한 유일한 텍스트다.
중간 마디 narration은 sub-agent .md에 명시되어 있지만 메인에 streaming 안 됨 — 메인의 "사후 분해 narrate"가 사용자 가시성을 만든다.

### 금지 패턴

- 메인이 Agent 호출만 하고 narration 생략 → 사용자가 "진행되고 있는지" 알 수 없음
- 메인이 호출 직전 "예상 마디" narrate 없이 곧장 Agent 호출 → 5~10분 침묵 발생
- 메인이 호출 후 결과를 통째로 dump (분해 안 함) → 사용자가 결과 구조 파악 어려움
- TodoWrite phase를 "QA + 핸드오프"로 단일화 → slide-qa·visual-refiner 두 단계 가시성 사라짐
- Sub-agent를 호출하지 않고 메인이 자체 처리 → STEP 4·5 mandate 위반 (위 MANDATORY GATE 참조)

## 한국어 처리

한국어 콘텐츠는 design-system-manager가 BRIEF의 `language` 필드를 보고 자동 병합한다 (`references/korean-typography.md`).

**우선순위**: 스타일 non-negotiable > Korean Localization. 스타일이 라틴 폰트를 시그니처로 명시(non-negotiable)한 경우, 한글은 Pretendard, 라틴 글리프는 스타일 폰트로 듀얼 페어링. 단일 출처는 design-system-manager.

## 모드 = 납품형식 (핵심 원칙)

모드 선택 = 결과물 종류 결정. 사용자 입력은 **내용 + 스타일** 두 카테고리로만 수집. 스타일에는 자동 추천 / 사용자 직접 느낌 / 사용자 제공 레퍼런스(이미지/URL/md 텍스트)가 포함됨.

| 모드 | 납품형식 |
|------|---------|
| ① Prototype | 웹페이지 (HTML) |
| ② Slide Deck | HTML 슬라이드 (기본) — "PPTX로" 요청 시 STEP 5에서 변환 |
| ③ Other | 이메일·배너·카드뉴스 등 (HTML/이미지) |
| ④ Document | A4 매뉴얼·가이드 (HTML, @media print) |

## Anti-Slop Rules

- 금지: generic AI 퍼플 그라데이션, 과도한 shadow, Inter 폰트 고집
  - **예외**: 선택한 스타일이 brand-defined 인디고·바이올렛 그라디언트를 시그니처로 정의한 경우 (예: Corporate Trust)
- 수정 시 전체 재생성 금지 — 변경 부분만 부분 적용
