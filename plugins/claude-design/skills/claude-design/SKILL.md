---
name: claude-design
description: "Claude Design methodology skill v3 — Claude Code에서 디자인 결과물 생성 (프로토타입, 슬라이드, A4 문서, 템플릿, 자유형식). 31+ 스타일 라이브러리 자동 추천 + 5개 모드 + 13-agent orchestration. Trigger: 디자인 만들어줘, 프로토타입, 슬라이드, 슬라이드 덱, 피치덱, 발표자료, PPT, PPTX, 원페이저, 목업, 와이어프레임, 랜딩페이지, 매뉴얼, 가이드, A4 문서, 'XXX 스타일로 만들어줘', 'Claude Design v3 시작해', design, prototype, slide deck, pitch deck, one-pager, mockup, wireframe, landing page, dashboard, email template, social graphic, banner, infographic. Do NOT use for: code-only implementation without design intent, pure content writing."
---

# Claude Design Skill

Claude Design 워크플로우를 Claude Code에서 재현하는 마스터 스킬. 같은 콘텐츠를 31+ 스타일로 즉시 재해석.

**Core Philosophy**: DESIGN_SYSTEM 먼저 → 5개 모드 분기 → 생성 → 반복 수정 → Claude Code 핸드오프

## Activation

- `/claude-design` 또는 자연어 트리거(description 키워드 매칭) → 자동 진입
- `"Claude Design 시작해"` → MANDATORY GATE 즉시 진입
- `"XXX 스타일로"` → DesignSystemManager가 스타일 파일 로드 후 진행

## Agent Orchestration

```
DesignSystemManager → ProjectPlanner → Generator(모드별) → VisualRefiner → Handoff
                                       │
                                       ├─ ① prototype-agent
                                       ├─ ② slide-deck-agent → slide-qa-agent (자동)
                                       ├─ ③ template-agent
                                       ├─ ④ other-agent
                                       └─ ⑤ document-agent

선택적 병렬: copywriting / animation / responsive / accessibility
```

**규칙**: DESIGN_SYSTEM 미확정 시 Generator 실행 불가. 전문 에이전트는 명시 요청 또는 QA 신호로 호출.

## 트리거 감지 후 강제 진입 절차 (MANDATORY GATE)

트리거 워드 감지 즉시 — HTML/코드 생성 전 반드시 아래 순서를 실행한다.
**어떤 생성 단계도 이 게이트를 통과하지 않으면 실행 불가.**

```
STEP A. 스타일 파일 의무 로드 (파일을 실제로 Read — 기억에 의존 금지)
  → 스타일 지정됨:
      Read references/styles/[style].md 전체 읽기
  → 스타일 미지정:
      Features의 Style System 절차 따름 (style-recommender → top 3 → 사용자 선택 → 선택된 스타일 파일 Read)
  → 스타일 파일에서 base theme(light/dark) 추출 → DESIGN_SYSTEM에 기록

STEP B. 디자인 시스템 확인 (사용자 OK 필수)
  → DESIGN_SYSTEM 핵심 요약 출력:
    • 대표 색상 3개 (primary, accent, background)
    • heading_font / body_font
    • base theme (light/dark)
  → "이 방향으로 진행할까요?" → OK 전까지 생성 금지

STEP C. 모드별 에이전트 위임 (Agent tool 사용 — 직접 생성 금지)
  → 아래 에이전트를 Agent tool로 호출한다. 직접 생성하지 않는다.

  ② Slide Deck:
     Agent tool 호출 (subagent_type: "slide-deck-agent")
     prompt에 포함: DESIGN_SYSTEM 블록 전체 + 콘텐츠 요약 + 사용자 요청
     → 에이전트가 Step 0~Step 5 전체를 관리한다

  ① Prototype  → prototype-agent.md 규칙에 따라 직접 진행
  ③ From Template → template-agent.md 규칙에 따라 직접 진행
  ④ Other → other-agent.md 규칙에 따라 직접 진행
  ⑤ Document → document-agent.md 규칙에 따라 직접 진행
```

**핵심 원칙**: 각 에이전트 파일이 그 모드의 유일한 생성 규칙 소스 — SKILL.md는 흐름만 정의.

## 4-Step Pipeline

| # | Step | Owner | 단일 출처 |
|---|------|-------|----------|
| 1 | DESIGN_SYSTEM 확정 | design-system-manager | `agents/design-system-manager.md` |
| 2 | 모드 선택 + 소스 수집 | project-planner | `agents/project-planner.md` |
| 3 | 생성 → 프리뷰 → 수정 (반복) | 모드별 generator → visual-refiner | `agents/[mode]-agent.md` + `references/output-common.md` |
| 4 | Claude Code 핸드오프 | (메인) | DESIGN_SYSTEM + 코드 + 파일 구조 + 다음 단계 출력 |

세부 절차는 owner 에이전트.md / reference 단일 출처. SKILL.md는 흐름만 정의 (MANDATORY GATE 참조).

## Korean Localization Layer

**트리거**: 한국어 입력 / "한국 시장·사용자·KR·국내" 언급 / Jake의 모든 작업(기본).
→ `references/korean-typography.md` 로드 후 DESIGN_SYSTEM.typography 재조정. 원본 스타일의 색상·레이아웃은 유지, 타이포·스페이싱만 재조정. 세부 규칙은 단일 출처.

## Anti-Slop Rules

- 금지: 퍼플 그라데이션, 과도한 shadow, Inter 폰트 고집
- 수정 시 전체 재생성 금지 — 변경 부분만 부분 적용
