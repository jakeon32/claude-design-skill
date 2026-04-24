---
name: claude-design
description: "Claude Design methodology skill v2.4 — replicates Anthropic's Claude Design (claude.ai/design) workflow in Claude Code. Integrates designprompts.dev 73 style library + auto style recommendation. Orchestrates 12 agents: DesignSystemManager(+StyleRecommender) → ProjectPlanner → [PrototypeAgent | SlideDeckAgent | TemplateAgent(+5 industry presets) | OtherAgent | DocumentAgent] → [CopywritingAgent | AnimationAgent | ResponsiveAgent | AccessibilityAgent] → VisualRefiner(+auto QA) → handoff. Trigger when: user wants to create UI prototype, slide deck, pitch deck, one-pager, mockup, design exploration, landing page, wireframe, dashboard, email template, social graphic, banner, A4 document, manual, guide, 디자인 만들어줘, 프로토타입, 슬라이드 덱, 원페이저, 목업, 와이어프레임, 피치덱, 랜딩페이지, 이메일 템플릿, 소셜 그래픽, 매뉴얼, 가이드, A4 문서, Claude Design v2 시작해, XXX 스타일로 만들어줘. Do NOT use for: code-only implementation without design intent, pure content writing."
---

# Claude Design Skill v2.4

Claude Design의 워크플로우를 Claude Code에서 완전히 재현하는 마스터 스킬.
designprompts.dev의 31+ 스타일 라이브러리 통합 — 같은 콘텐츠를 다른 미학으로 즉시 재해석 가능.

**Core Philosophy**: 디자인 시스템 먼저 → (선택) 스타일 지정 → 4개 모드 분기 → 소스 수집 → 생성 → 반복 수정 → Claude Code 핸드오프

## v2.1 신기능: designprompts.dev Style Library

사용자가 "XXX 스타일로" 또는 특정 스타일명을 언급하면:
1. `references/styles/style-library.md`에서 해당 스타일 정의 로드
2. DESIGN_SYSTEM에 팔레트/타이포/레이아웃 traits 주입
3. 사용자 브랜드 색상이 있으면 스타일보다 우선 적용 (하이브리드)

## v2.4 신기능: Document 모드 (A4 문서/매뉴얼)

매뉴얼, 가이드, 운영 문서 등 A4 페이지 기반 문서를 생성:
1. 6+1 페이지 유형: A(조회/리스트), B(입력/폼), C(번호 어노테이션), D(상세/액션), E(대시보드/맵), F(2단 레이아웃)
2. 7단계 정보 계층: L1(제목)~L7(본문) — Notion 블록 구조와 동일한 계층
3. block-filling 레이아웃: 794px × 1020px A4 시뮬레이션, `@media print` 지원
4. SaaS 화면 기반 매뉴얼 자동 생성: Chrome DevTools MCP 스크린샷 + DOM 분석

→ `agents/document-agent.md` 전용 에이전트 처리

## v2.2 신기능: 스타일 자동 추천

스타일 미지정 시 DesignSystemManager가 자동으로 top 3 추천:
1. 사용자 설명에서 tone/mood/industry 신호 추출
2. `references/style-recommender.md` 태그 인덱스 (73개 스타일) 매칭
3. 가중치 점수 계산 → 다양성 확보된 top 3 후보 제시
4. 선택 즉시 DESIGN_SYSTEM 주입 → 기존 워크플로우 합류

지원 스타일 (31+): Bauhaus Light, SaaS Light, Luxury Light, Swiss Minimalist Light, Neo Brutalism Light, Flat Design Light, Art Deco Light/Dark, Material Design Light, Academia Light, Playful Geometric Light, Professional Light, Claymorphism Light, Botanical Light, Sketch Light, Industrial Light, Neumorphism Light, Organic Light, Maximalism Light, Retro Light, Monochrome, Modern Dark, Terminal Dark, Kinetic Dark, Bold Typography Dark, Cyberpunk Dark, Web3 Dark, Minimal Dark, Vaporwave Dark

## Activation

- `/claude-design` 또는 자연어로 디자인 작업 요청 시 자동 트리거
- `"Claude Design v2.1 시작해"` 또는 `"Claude Design v2 시작해"` → ProjectPlanner 즉시 호출
- `"XXX 스타일로 만들어줘"` → DesignSystemManager에서 스타일 로드 후 진행
- 첫 메시지: 디자인 시스템 설정 여부 + 스타일 지정 여부 확인 → 4개 모드 선택

## 에이전트 구조 (Master Orchestration)

```
[MASTER]
    │
    ├─ 1. DesignSystemManager  ← 항상 먼저 (DESIGN_SYSTEM 확정)
    │       └─ style-recommender  ← 스타일 미지정 시 top 3 자동 추천
    │
    ├─ 2. ProjectPlanner       ← 모드 분기 + 소스 수집
    │
    ├─ 3. Generator (모드별)
    │       ├─ prototype-agent    (① Prototype — UI 목업 + One-Pager 포함)
    │       ├─ slide-deck-agent   (② Slide Deck)
    │       ├─ template-agent     (③ From Template — 파일 or 업종별 프리셋)
    │       │       └─ references/templates/  ← 5개 업종 구조 프리셋
    │       ├─ document-agent     (⑤ Document — A4 문서, 매뉴얼, 가이드)
    │       │       └─ 6+1 page types, L1-L7 정보 계층, block-filling
    │       └─ other-agent        (④ Other)
    │
    ├─ 4. 선택적 전문 에이전트 (필요 시 병렬 실행)
    │       ├─ copywriting-agent  ← 카피/헤드라인/CTA 문구 요청 시
    │       ├─ animation-agent    ← 인터랙션/hover/스크롤 애니메이션 요청 시
    │       ├─ responsive-agent   ← 모바일/반응형 요청 시
    │       └─ accessibility-agent ← QA ❌ 감지 또는 접근성 요청 시
    │
    ├─ 5. VisualRefiner        ← 반복 수정 + 자동 QA 체크 (모든 모드 공통)
    │
    └─ 6. Handoff              ← Claude Code 핸드오프
```

**규칙**: DESIGN_SYSTEM 없으면 어떤 Generator도 실행 불가.
**전문 에이전트**: 명시 요청 또는 QA 결과에 따라 자동 호출, 병렬 실행 가능.

## Step 0: 디자인 시스템 설정 (DesignSystemManager)

세션 시작 시 항상 먼저 실행. 기존 브랜드/코드베이스가 있으면 읽어오고, 없으면 기본값으로 생성.

**입력 요청 (optional, 있는 것만):**
```
다음 중 있는 것을 공유해주세요 (모두 선택사항):
1. 코드베이스 폴더 또는 GitHub URL (프론트엔드 서브폴더 추천)
2. Figma 스크린샷 또는 기존 UI 이미지
3. 브랜드 가이드 문서 (색상, 폰트, 톤앤매너)
4. 기존 웹사이트 URL
5. 없으면 → 어떤 분위기의 디자인을 원하는지 한 줄로
```

**출력: DESIGN_SYSTEM 블록** (이후 모든 에이전트가 참조)
```yaml
DESIGN_SYSTEM:
  project_name: ""
  colors:
    primary: "#"
    secondary: "#"
    accent: "#"
    background: "#"
    surface: "#"
    text: "#"
    text_muted: "#"
  typography:
    heading_font: ""
    body_font: ""
    scale: { h1: "48px", h2: "36px", h3: "24px", body: "16px", small: "14px" }
  spacing:
    base: "8px"
    section: "80px"
    component: "24px"
  radius: "8px"
  shadow: "0 4px 16px rgba(0,0,0,0.08)"
  tone: ""
  components: []
```

## Step 1: 프로젝트 모드 선택

디자인 시스템 설정 후 4개 모드 중 선택:

```
어떤 유형의 결과물이 필요한가요?

① Prototype      — 앱/웹 UI 목업, 랜딩페이지, 원페이저
                   (Wireframe / High-fidelity / One-Pager 선택)
② Slide Deck     — 발표자료, 피치덱, 보고서
                   (슬라이드 수 + 스피커 노트 ON/OFF)
③ From Template  — 유저 제공 파일(HTML/Figma/PPTX/스크린샷) 기반 재건
④ Other          — 이메일, 소셜 그래픽, 배너, 인포그래픽 등 자유 형식
⑤ Document       — A4 매뉴얼, 가이드, 운영 문서, 인쇄 가능한 보고서
                   (6+1 페이지 유형 / L1-L7 계층 / @media print 지원)
```

→ 선택된 모드에 따라 전용 에이전트 실행: [agents/ 폴더 참조]

## Step 2: 소스 수집 (모드 공통)

선택 후 1-2개 핵심 질문만:

| 수집 항목 | 방법 |
|-----------|------|
| 목적/목표 | 텍스트 프롬프트 |
| 레퍼런스 이미지 | 이미지 업로드 또는 URL |
| 기존 문서 | DOCX / PPTX / XLSX 업로드 |
| 실제 제품 | 웹사이트 URL (캡처해서 분석) |
| 추가 설명 | 자유 텍스트 |

## Step 3: 생성 → 프리뷰 → 수정 루프 (VisualRefiner)

### Preview Loop (Chrome DevTools MCP — 필수)

HTML 생성 후 항상 아래 순서 실행:

```
1. 생성: self-contained HTML (Tailwind CDN + Google Fonts CDN)
2. 저장: d:\tmp\preview.html (또는 d:\tmp\preview-v1.html 등)
3. 브라우저: mcp__chrome-devtools__new_page (file:///d:/tmp/preview.html)
4. 스크린샷: mcp__chrome-devtools__take_screenshot
5. 채팅에 표시 → 사용자 피드백
6. 수정 후 저장 → 다시 navigate_page → 다시 스크린샷
```

**출력 형식**: 항상 self-contained HTML (빌드 없이 바로 열림)
- Tailwind: `<script src="https://cdn.tailwindcss.com"></script>`
- 폰트: Google Fonts CDN link
- 아이콘: Heroicons SVG 인라인 또는 unpkg CDN

### 다중 시안 (병렬)

"N가지 변형" 요청 시:
```
d:\tmp\preview-v1.html, v2.html, v3.html 각각 저장
→ 각각 new_page + take_screenshot
→ 스크린샷 나란히 표시
→ 사용자가 선택한 번호로 계속 진행
```

### 수정 방법 (시각 확인 후)

1. **대화형**: "버튼을 더 크게", "색상을 primary로", "레이아웃 바꿔"
2. **인라인 코멘트**: [섹션명] 앞에 `//` 붙여서 특정 부분만 지정
3. **슬라이더 시뮬레이션**: "간격 +20px", "폰트 크기 -2px", "배경 어둡게"

수정 후 항상: 저장 → 스크린샷 → `✅ 변경 적용. 확인 후 추가 수정 또는 핸드오프 요청.`

## Step 4: 핸드오프

"핸드오프", "Claude Code로 넘겨", "코드 만들어" → 출력:
- DESIGN_SYSTEM 블록 전체
- HTML/React 컴포넌트 코드
- 파일 구조 제안
- 다음 구현 단계

## Korean Localization Layer

한국어 콘텐츠 또는 한국 시장 대상 디자인 시 **항상** 적용:
→ `references/korean-typography.md` 로드 후 DESIGN_SYSTEM.typography 재조정

**트리거**: 한국어 입력 / "한국 시장·사용자·KR·국내" 언급 / Jake의 모든 작업(기본)

**원칙**: 원본 스타일의 색상·레이아웃은 유지, 타이포그래피·스페이싱만 재조정
- Pretendard 우선 적용 (heading/body 모두)
- line-height 영어 대비 1.1~1.3배 (body 1.65~1.8)
- letter-spacing heading -0.02~-0.04em
- 한 줄 글자 수: 제목 10~18자, 본문 18~24자

## Anti-Slop Rules

- 퍼플 그라데이션, 과도한 shadow, Inter 고집 금지
- DESIGN_SYSTEM 항상 명시적으로 참조하며 적용
- generic AI 디자인 패턴 피하고 브랜드 특성 반영
- 불필요한 전체 재생성 피하기 (수정은 부분 적용)
