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
ProjectPlanner → DesignSystemManager → Generator(모드별) → VisualRefiner → Handoff
                                       │
                                       ├─ ① prototype-agent
                                       ├─ ② slide-deck-agent → slide-qa-agent (자동)
                                       │     └─ slide-pptx-agent (선택 — "PPTX로" 요청 시)
                                       ├─ ③ other-agent
                                       └─ ④ document-agent

선택적 병렬: copywriting / animation / responsive / accessibility
```

**규칙**: DESIGN_SYSTEM 미확정 시 Generator 실행 불가. 전문 에이전트는 명시 요청 또는 QA 신호로 호출.

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

STEP 4. 결과물 핸드오프 (사용자에게 전달)

STEP 5 (선택 — "PPTX로" 요청 시). slide-pptx-agent 위임 (Agent tool 호출 — subagent_type: "claude-design:slide-pptx-agent")
  → 입력: 완성된 HTML 슬라이드 경로 + DESIGN_SYSTEM
  → 산출: .pptx 파일 (편집 가능한 PowerPoint) — 변환 시점에 자동 호환 처리(gradient → solid, div/span → p 등)
```

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
  산출물: 본 작업 N장 deck.html + color-tuner.html
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

## 4-Step Pipeline

| # | Step | Owner | 단일 출처 |
|---|------|-------|----------|
| 1 | 모드 선택 + 콘텐츠 수집 + 신호 추출 | project-planner | `agents/project-planner.md` |
| 2 | DESIGN_SYSTEM 확정 + 컨셉 추천 | design-system-manager | `agents/design-system-manager.md` |
| 3 | 생성 → 프리뷰 → 수정 (반복) | 모드별 generator → visual-refiner | `agents/[mode]-agent.md` + `references/output-common.md` |
| 4 | 핸드오프 | (메인) | DESIGN_SYSTEM + 코드 + 파일 구조 + 다음 단계 출력 |

세부 절차는 owner 에이전트.md / reference 단일 출처. SKILL.md는 흐름만 정의 (MANDATORY GATE 참조).

## Progress Reporting (사용자 가시성 — 필수)

Claude Code의 `Agent` tool은 sub-agent가 끝날 때까지 메인 스레드에 한 메시지만 돌아온다 → sub-agent 내부 작업은 사용자에게 보이지 않는다. 긴 작업(슬라이드 빌드·QA·문서 페이지 다회 생성·수정 반복)에서 사용자가 답답하지 않도록 메인 스레드와 sub-agent **양쪽 모두** narration 의무를 진다.

### 메인 스레드 의무

1. **TodoWrite 선행** — 2개 이상 phase가 예상되는 작업은 시작 시 phase 전체를 TodoWrite로 등록 (예: BRIEF / DESIGN_SYSTEM / 쇼케이스 / 본 작업 / QA / 수정·핸드오프). Claude Code 우측 UI에 phase가 visible해진다.
2. **Agent 호출 직전 한 줄** — `"[에이전트명] 실행 — [무엇을 할지 1줄]"`
   예: `"slide-qa-agent 실행 — Tier 1·2·3·4 코드 검수 시작"`
3. **Agent 반환 직후 한 줄** — `"[에이전트명] 완료 — [핵심 결과 요약]"`
   예: `"slide-qa-agent 완료 — 자동 수정 5건 / 위반 2건 / 경고 3건"`
4. **TodoWrite 마킹** — 호출 직전 해당 phase `in_progress`, 반환 후 `completed` (+ 다음 phase `in_progress`)
5. **사용자 입력 대기 시점**도 명시 — `"... 컨펌 대기 중"` 한 줄

### Sub-agent 의무

1. 시작 시 자신이 수행할 마디(phase) 1줄 선언 — `"🔍 Slide QA 시작 — slides.html / 8장 / Tier 1·2·3·4 순차 검사"`
2. 각 마디 진입/완료마다 한 줄 출력 — `"[Tier 1] 진입 — A5/A6/A7/A8/A9/B1/D1 검사"` / `"[Tier 1] 완료 — 자동 수정 5건"`
3. 종료 시 통합 결과(표·요약) 1개

각 에이전트.md는 자신의 마디 목록을 `## Progress Narration (의무)` 섹션에 명시한다.

### 금지 패턴

- 메인 스레드가 Agent 호출만 하고 narration 생략 → 사용자가 "진행되고 있는지" 알 수 없음
- sub-agent가 침묵 후 최종 결과만 한 번에 dump → 중간 마디 가시성 0
- TodoWrite 없이 다단계 진행 → phase 추적 불가

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
