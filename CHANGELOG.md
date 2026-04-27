# Changelog

Claude Design Skill의 변경 이력. 형식은 [Keep a Changelog](https://keepachangelog.com/) 기반.

---

## [Unreleased] — v3 진행 중

### Phase 6.1 (2026-04-27): 실 빌드 테스트 기반 robustness 패턴 (4건 fix)

테스트 덱(AI 인플루언서 프롬프트 매뉴얼·9장 Digital Luxury Editorial) 빌드 + Color Tuner 라이트/다크 팔레트 randomize 검증 과정에서 발견된 4건 수정:

- **쇼케이스 임계값 제거** — "10장 이상 시 필수" → 슬라이드 수 무관 모든 덱 의무. 짧은 덱에서도 커버 인상·본문 톤 비교 검증 가치 있음.
- **본문 슬라이드 vertical 분포 패턴** — 720px 캔버스에서 상단 쏠림 방지를 위해 `justify-content:space-between` 또는 3-zone(top·middle·bottom) 분배 의무. 자가검수에 "vertical 분포 균형" 항목 추가. bottom meta row는 커버 금지·본문 권장으로 명문화.
- **color-mix 의무 강화** — `:root` 토큰뿐 아니라 **인라인 style의 rgba(255,255,255,X) / rgba(0,0,0,X)도 절대 금지** 명문화. 자가검수에 "인라인 rgba 0건" + ":root alpha 토큰 color-mix 기반" 두 항목 추가. 위반 사고 사례(Color Tuner Randomize 라이트 팔레트 전환 시 hardcode white text 가독성 0) 명시.
- (후속 commit) 고정 inverse panel 위 텍스트 anchor 패턴

### Phase 6 (2026-04-27): 4모드 구조 + 잔재 일괄 폐기

**구조 변경**:
- 5모드 → **4모드** (③ From Template 폐기). `agents/template-agent.md` **파일 삭제**.
- Sub-agent 14개 → **13개**.
- "**모드 = 납품형식**" 원칙 SKILL.md에 명문화. 사용자 수집 = 내용 + 스타일 두 카테고리만.
- BRIEF 필드 `brand_assets` → `style_assets` 명칭 변경 (사용자 제공 레퍼런스 흡수 위해).
- DESIGN_SYSTEM에 `style_assets.user_references = { images, urls, texts }` 신설 — 사용자가 제공한 이미지·URL·md 텍스트를 스타일 입력으로 활용.

**잔재 일괄 제거**:
- Figma 입력·출력 분기 (project-planner / template / slide-deck / DSM 5곳)
- React 출력 분기 (slide-deck "React로")
- PDF delivery 옵션 (project-planner / slide-deck "Step 0-pre 납품 형식 묻기" 블록)
- Wireframe / High-fidelity / One-Pager 분기 (prototype-agent 본체 + project-planner 매핑)
- `pptx_mode` 플래그 (SKILL/DSM/SDA/slide-qa/qa-pipeline 전 5곳)
- project-planner Junior 3-체크포인트 → **2-체크포인트**로 단순화 (콘텐츠/스타일 수집)

**규칙 명확화 (SKILL.md)**:
- Anti-slop: "**generic AI 퍼플 그라디언트 금지** / **brand-defined 인디고·바이올렛은 예외**" 명문화 (Corporate Trust 등 시그니처 보호).
- 폰트 우선순위: "**스타일 non-negotiable > Korean Localization**" 명문화 — 한글 Pretendard / 라틴 스타일폰트 듀얼 페어링 (DSM 4단계 책임).

**slide-deck ↔ slide-pptx 책임 분리**:
- `slide-deck-agent` = HTML 자유 (gradient·shadow·복합 마크업 OK).
- `slide-pptx-agent` = "PPTX로" 요청 시 변환. 4개 하드 제약(1280×720 / `<p>` 태그 / no bg / no gradient) + gradient → solid 자동 대체 + Photo Panel solid 분리 패턴이 본 에이전트로 이전. 변환 시점 자동 호환 처리.
- `slide-qa-agent`에서 PPTX 호환 검사(Tier 5 / Group F) 폐기.

### Added
- **slide-qa-agent** — HTML 슬라이드 코드 검수 전담 에이전트 (`agents/slide-qa-agent.md`).
  - 8개 그룹·30개 항목 자동 체크: 구조 무결성(A·9)·한국어 폰트(B·2)·letter-spacing(C·2)·카운터 시스템(D·3)·그리드 다양성(E·3)·PPTX 호환(F·3)·일반 규칙(G·5)·공간 문법 다양성(H·3).
  - `slide-deck-agent` 완료 직후 자동 실행. ❌ 항목 자동 수정 후 VisualRefiner로 인계.
  - ⚠️ slide-qa-agent.md / SKILL.md description의 "7그룹 24항목" 표기는 outdated — Phase 2(SKILL.md 슬림화) + slide-qa-agent description 정정 시 일괄 갱신 예정.
- **qa-pipeline.md** — 슬라이드 생성 → QA → 검증 카탈로그 빌드 6단계 자동 루프 정의 (`references/qa-pipeline.md`).
- **style-deck-personality.md** — 73개 스타일을 슬라이드 덱 발표 맥락(권위/설득/감성/분석/혁신)으로 분류 (`references/style-deck-personality.md`).
- **slide-layouts/** — 30+ 레이아웃 정의 카탈로그를 별도 폴더로 분리 (`references/slide-layouts/`).
  - `cover-layouts.md`, `text-layouts.md`, `visual-layouts.md`, `statement-layouts.md`, `data-layouts.md`, `mockup-layouts.md`, `card-layouts.md`, `layout-variation-spec.md`, `variations.md`, `index.md`.
  - 스타일과 직교(orthogonal): 같은 레이아웃을 어떤 스타일에도 조합 가능.

### Changed
- **Phase 0 (2026-04-26): B 흐름 도입 — DESIGN_SYSTEM은 모드+콘텐츠 후 확정**
  - **SKILL.md** — MANDATORY GATE 3 STEP (A·B·C) → **4 STEP** (project-planner → DSM → 모드별 에이전트 → 핸드오프) 재작성. Activation의 "XXX 스타일로" 진입 제거. Korean Localization Layer 섹션 → DSM 흡수("한국어 처리" 한 줄로 축소). Agent Orchestration 도식 ProjectPlanner → DesignSystemManager 순서로 swap.
  - **agents/project-planner.md** — 트리거 위치 변경 (DESIGN_SYSTEM 확정 후 → 트리거 직후), 0.5단계 스타일 선택 삭제(DSM으로 이관), **콘텐츠 신호 추출 단계 신규** (language·content_signals: mood/industry/tone/audience/complexity), BRIEF 출력 형식 정비. Generator 직접 호출 → 메인 orchestrate.
  - **agents/design-system-manager.md** — 6분기(Figma/스타일라이브러리/코드베이스/자산/텍스트/자동추천) → **자동 추천 단일 경로**로 단순화. BRIEF 입력 명세 추가. 자동 추천 표준 흐름(top 3 + "직접 원하는 느낌 있나요?" 동시 질문). 모드별 출력 환경 반영(slide=16:9·본문 16px / document=A4 인쇄 고려 타이포). 한국어 자동 병합(SKILL.md Korean Layer 흡수). 자산 보강.
  - **agents/document-agent.md** — frontmatter 추가 (5모드 통일 위임 prerequisite 해결).
  - **references/styles/index.md** — "XXX 스타일로 해줘" 사용법 안내 → 자동 추천 사용법으로 한 줄 수정.
- **SKILL.md** — v2.4 → v3 (13 에이전트). MANDATORY GATE의 STEP C에서 모드별 에이전트를 **Agent tool로 위임 강제**. 이전: "에이전트 파일 규칙에 따라 진행" → 이후: "Agent tool 호출 (subagent_type: ...)" 명시.
- **design-system-manager.md** — Figma MCP·스타일 라이브러리·코드베이스·텍스트·자동 추천 5개 분기 명문화.
- **project-planner.md** — Junior Designer 3-체크포인트 워크플로(요구사항·자산·스켈레톤) 도입.
- **slide-deck-agent.md** — Cover 장식 패턴 라이브러리 6종 추가 + 수치 검증, 1280×720 캔버스 표준화, Anti-slop 규칙 적용. (v3 슬림화 진행 중)
- **visual-refiner.md** — 5차원 디자인 품질 평가, 시각적 지배 계층(Dominance Hierarchy), 시각적 무게 균형 체크리스트 추가. (v3에서 코드 분석 QA 섹션은 slide-qa-agent로 이관 예정)

### Tools
- **pptx_to_png.py** 추가 — PowerPoint COM 자동화로 PPTX 각 슬라이드를 1280×720 PNG로 export. `make_compare.py` 입력 자동화. Windows 전용, Mac/Linux는 추후 LibreOffice headless 지원 예정.
- **tools/README.md** 추가 — 5개 도구 역할 매트릭스 + 표준 8단계 워크플로 + import/CLI 사용 패턴.
- **requirements.txt** — `pywin32>=306; sys_platform == 'win32'` 추가.

### 진행 중 구조 재구성 (예정)
- agents/ 평면 + prefix 그룹화 (orch-/gen-/spec-/qa-).
- references/ 하위 분류 (core/, pptx/, styles/, slide-layouts/, templates/).
- SKILL.md 슬림화 (v* 신기능 섹션 통합 → CHANGELOG로 이전).
- visual-refiner.md의 코드 분석 QA 섹션 → slide-qa-agent로 이관.
- slide-deck-agent.md 슬림화 (1304줄 → ~400줄).

### Fixed
- `references/slide-layouts/index.md`의 Timeline 카탈로그 링크 — 존재하지 않는 `timeline-layouts.md`를 가리키던 것을 `data-layouts.md#horizontal-timeline`로 수정. Roadmap은 추후 추가 표시.
- `.gitignore`에 `.claude/worktrees/` 추가 (`.claude/` 전체가 아닌 이유: 향후 settings.json·agents 공유 가능성).

---

## [2.4] — 2026-04 (커밋 c0b6cd6 ~ c17b1f2)

### Added — Document 모드
- **document-agent** — A4 매뉴얼·가이드·운영 문서 생성 전용.
- 6+1 페이지 유형: A(조회/리스트), B(입력/폼), C(번호 어노테이션), D(상세/액션), E(대시보드/맵), F(2단 레이아웃).
- 7단계 정보 계층: L1(제목)~L7(본문) — Notion 블록 구조와 동일.
- block-filling 레이아웃: 794px × 1020px A4 시뮬레이션, `@media print` 지원.
- SaaS 화면 기반 매뉴얼 자동 생성: Chrome DevTools MCP 스크린샷 + DOM 분석.

### Added — Slide Deck 강화
- **Cover 장식 패턴 라이브러리 6종** + 수치 검증 (c17b1f2).
- **Cover 장식 요소 원칙** (70d826e).
- **모드별 MANDATORY GATE 구조 완성** (dd32981).
- **1280×720 캔버스 표준화** + Anti-slop 규칙 적용 (694befb).
- **Animation Agent 강화**: HyperShader 렌더 환경 제한, validate 워크플로우, contrast 주의사항, HyperFrames 비디오 렌더링 파이프라인 섹션 (be35aae ~ fc6e799).
- **카드 height flexbox 패턴** + outer bg #111 고정 (e15e312).
- **Huashu Design 분석 기반 워크플로 개선** + `output-common.md` 추가 (be35aae).

---

## [2.2] — 2026-04 초

### Added — 스타일 자동 추천
- 스타일 미지정 시 DesignSystemManager가 자동으로 top 3 추천:
  1. 사용자 설명에서 tone/mood/industry 신호 추출
  2. `references/style-recommender.md` 태그 인덱스(73개 스타일) 매칭
  3. 가중치 점수 계산 → 다양성 확보된 top 3 후보 제시
  4. 선택 즉시 DESIGN_SYSTEM 주입 → 기존 워크플로우 합류

---

## [2.1] — 2026-03 (커밋 e561b8e)

### Added — designprompts.dev Style Library 통합
- 31+ 스타일 라이브러리 통합 — 같은 콘텐츠를 다른 미학으로 즉시 재해석 가능.
- 사용자가 "XXX 스타일로" 또는 특정 스타일명 언급 시:
  1. `references/styles/style-library.md`에서 해당 스타일 정의 로드
  2. DESIGN_SYSTEM에 팔레트/타이포/레이아웃 traits 주입
  3. 사용자 브랜드 색상이 있으면 스타일보다 우선 적용 (하이브리드)

### Added — PPTX 파이프라인
- **Photo Panel Gradient Blend 규칙** (771a3ee).
- **120% gradient axis extension rule** + seam elimination (e4612e5).
- 플러그인 레이아웃 재구성 + `pptx_utils.py` 일반화 (3d92fac).

---

## [2.0] — 초기

### 핵심 워크플로우
- 디자인 시스템 먼저 → (선택) 스타일 지정 → 4개 모드 분기 → 소스 수집 → 생성 → 반복 수정 → Claude Code 핸드오프
- 4개 출력 모드: Prototype / Slide Deck / From Template / Other
- 5차원 디자인 품질 평가 (VisualRefiner)
- Korean Localization Layer (Pretendard, line-height, letter-spacing 한국어 기준값)
