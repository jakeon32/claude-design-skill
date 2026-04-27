# Claude Design Skill

Claude Code용 디자인 에이전트 플러그인. 자연어 요청만으로 UI 프로토타입, 슬라이드 덱, A4 문서, 자유 형식 그래픽, PowerPoint 파일까지 생성한다.

---

## 목적

Claude Code는 기본적으로 코드를 잘 쓰지만, **디자인 산출물**을 체계적으로 만들려면 별도의 워크플로우가 필요하다.

이 스킬은 다음 흐름을 자동화한다:

```
모드 선택 + 콘텐츠 수집 → DESIGN_SYSTEM 확정 → 모드별 생성 → 핸드오프
```

Anthropic의 [claude.ai/design](https://claude.ai/design) 워크플로우를 Claude Code CLI/IDE 환경에서 그대로 재현하는 것이 목표다.

---

## 주요 기능

### 1. 4가지 출력 모드 (모드 = 납품형식)

| 모드 | 설명 | 주요 산출물 |
|------|------|------------|
| **① Prototype** | UI 목업, 대시보드, 랜딩페이지 | Self-contained HTML |
| **② Slide Deck** | 발표자료, 피치덱, 투자자 보고서 | HTML 슬라이드 (기본) — "PPTX로" 요청 시 변환 |
| **③ Other** | 소셜 그래픽, 배너, 이메일 템플릿 등 | HTML |
| **④ Document** | A4 매뉴얼, 가이드, 보고서 | HTML + `@media print` |

> 사용자가 제공하는 레퍼런스(이미지·URL·md 텍스트)는 별도 모드가 아니라 `design-system-manager`의 스타일 입력으로 흡수됨.

### 2. 73종 디자인 스타일 라이브러리

`"미니멀 다크 스타일로"`, `"네오 브루탈리즘으로"` 등 자연어 지정 즉시 적용.  
스타일 미지정 시 콘텐츠 + 사용자 신호를 분석해 `design-system-manager`가 Top 3 자동 추천.

**지원 카테고리 (일부)**

| Light | Dark |
|-------|------|
| Bauhaus, Swiss Style, Luxury Editorial, Art Deco | Minimalist Dark, Terminal CLI, Cyberpunk, Vaporwave |
| Neo Brutalism, Flat Design, Material You, Claymorphism | Neural Noir, Kinetic Typography, Bold Editorial |
| Botanical, Organic, Sketch, Neumorphism | Web3/DeFi, Neon Velocity, Cinematic Noir |

→ 전체 목록: [`references/styles/index.md`](plugins/claude-design/skills/claude-design/references/styles/index.md)

### 3. PPTX 변환 파이프라인

HTML 슬라이드 완성 후 `"PPTX로"` 요청 시 별도 에이전트(`slide-pptx-agent`)가 실제 `.pptx` 파일로 변환:

```
HTML 슬라이드 → python-pptx → PPTX → PowerPoint COM → PNG → 비교 이미지
```

- `pptx_utils.py` — `DesignSystem` + `PptxBuilder` 범용 라이브러리
- `pptx_export.py` — 슬라이드 빌더 + `build(ds=None)` 진입점
- `capture_compare.py` / `make_compare.py` — 시각 검증 도구

### 4. 한국어 타이포그래피 최적화

콘텐츠 언어가 한국어로 판정되면 자동 적용:
- Pretendard 기본 폰트
- 행간·자간 한국어 기준값
- 단어 단위 줄바꿈 (`word-break: keep-all`)

---

## 에이전트 구조

13개 에이전트가 역할을 분담하며 순차·병렬 실행한다.

```
[MASTER — claude-design]
    │
    ├─ 1. ProjectPlanner        ← 모드 선택 + 내용·스타일 수집 (BRIEF 산출)
    ├─ 2. DesignSystemManager   ← BRIEF + 콘텐츠 컨텍스트로 DESIGN_SYSTEM + 컨셉 확정
    │                              (사용자 제공 레퍼런스 이미지·URL·md 텍스트 흡수)
    │
    ├─ 3. Generator (4개 모드 중 1개 — Agent tool 위임 통일)
    │       ├─ prototype-agent      UI 목업, 랜딩페이지, 대시보드 (HTML)
    │       ├─ slide-deck-agent     슬라이드 덱 (HTML 기본)
    │       │     ├─ slide-qa-agent     ← 자동 QA (코드 정합성)
    │       │     └─ slide-pptx-agent   ← "PPTX로" 요청 시 자동 호환 변환
    │       ├─ document-agent       A4 매뉴얼 / 가이드 / 보고서
    │       └─ other-agent          이메일·배너·카드뉴스·인포그래픽
    │
    ├─ 4. 선택적 전문 에이전트 (필요 시 병렬)
    │       ├─ copywriting-agent    카피/헤드라인/CTA
    │       ├─ animation-agent      인터랙션/hover/스크롤 애니메이션
    │       ├─ responsive-agent     모바일/반응형
    │       └─ accessibility-agent  접근성 QA
    │
    ├─ 5. VisualRefiner         ← 반복 수정
    └─ 6. Handoff               ← Claude Code 핸드오프
```

> **규칙**: BRIEF + DESIGN\_SYSTEM이 확정되지 않으면 Generator 실행 불가.  
> sub-agent끼리 직접 호출 금지 — 메인이 orchestrate.

---

## 프로젝트 구조

```
claude-design-skill/
├── README.md
├── CLAUDE.md                          설치·사용법 요약
├── CHANGELOG.md
├── .gitignore
├── docs/
│   └── model-str.md                   AI 인플루언서 프롬프트 엔지니어링 문서
└── plugins/
    └── claude-design/
        ├── package.json
        └── skills/claude-design/
            ├── SKILL.md               마스터 스킬 진입점
            ├── agents/                에이전트 13개
            │   ├── project-planner.md
            │   ├── design-system-manager.md
            │   ├── prototype-agent.md
            │   ├── slide-deck-agent.md
            │   ├── slide-qa-agent.md           슬라이드 자동 QA
            │   ├── slide-pptx-agent.md         HTML → PPTX 자동 호환 변환 (선택)
            │   ├── document-agent.md
            │   ├── other-agent.md
            │   ├── visual-refiner.md
            │   ├── copywriting-agent.md
            │   ├── animation-agent.md
            │   ├── responsive-agent.md
            │   └── accessibility-agent.md
            ├── references/
            │   ├── korean-typography.md         한국어 타이포그래피 규칙
            │   ├── output-common.md             모드 공통 출력 패턴
            │   ├── cover-patterns.md            커버 장식 패턴 6종
            │   ├── photo-layouts.md             사진 배치 패턴 + Unsplash IDs
            │   ├── color-rules.md               색상 분배 + photo gradient blend + z-index
            │   ├── pptx-alignment-patterns.md   python-pptx 정렬 보정값
            │   ├── qa-pipeline.md               QA 파이프라인 정의
            │   ├── style-recommender.md         스타일 자동 추천 로직
            │   ├── style-deck-personality.md    발표 성격 차원 (덱 적합성)
            │   ├── slide-layouts/               그리드×구성요소 레이아웃 카탈로그
            │   ├── styles/
            │   │   ├── index.md
            │   │   ├── designprompts/           31종 스타일 프롬프트
            │   │   └── superdesign/             42종 슈퍼디자인 스타일
            │   └── templates/                   업종별 구조 프리셋 5종
            └── tools/
                ├── README.md
                ├── pptx_utils.py                PptxBuilder + DesignSystem (범용)
                ├── pptx_export.py               AI 인플루언서 슬라이드 빌더
                ├── pptx_to_png.py               PPTX → PNG (Windows COM)
                ├── capture_compare.py           Playwright HTML 스크린샷
                ├── make_compare.py              HTML vs PPTX 비교 이미지
                └── requirements.txt
```

---

## 설치

### 전제 조건

| 항목 | 설명 |
|------|------|
| Claude Code | CLI / VSCode Extension / Desktop App |
| Python 3.10+ | PPTX 도구 사용 시 |
| Pretendard 폰트 | 한국어 UI 출력 품질 (`C:\Windows\Fonts\` 설치) |
| Microsoft PowerPoint | PPTX → PNG 변환 시 (Windows 전용) |

### 플러그인 등록

Claude Code 설정 파일(`~/.claude/settings.json`)에 플러그인 경로 추가:

```json
{
  "plugins": [
    "D:/claude/claude-design-skill/plugins/claude-design"
  ]
}
```

### Python 패키지 설치

```bash
pip install -r plugins/claude-design/skills/claude-design/tools/requirements.txt
playwright install chromium
```

---

## 사용법

### 자연어 트리거

Claude Code 채팅에서 아래와 같이 입력하면 스킬이 자동 실행된다.

```
"랜딩페이지 만들어줘"
"피치덱 만들어줘"
"네오 브루탈리즘 스타일로 대시보드 프로토타입"
"A4 매뉴얼 만들어줘"
"Claude Design 시작해"
```

### 슬래시 커맨드

```
/claude-design
```

### PPTX 직접 생성 (Python)

```python
# 기존 AI 인플루언서 덱
from tools.pptx_export import build
build(output='D:/tmp/slides.pptx')

# 커스텀 디자인 시스템으로 신규 덱
from tools.pptx_utils import DesignSystem, PptxBuilder, build_pptx
from pptx.util import Inches
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

ds = DesignSystem(
    colors={
        **DesignSystem().colors,
        'v': RGBColor(0x00, 0x7A, 0xFF),   # accent 색상만 교체
    }
)

def my_cover(prs, b: PptxBuilder):
    sl = b.blank(prs)
    b.set_bg(sl, b.C['fg'])
    b.add_mixed(sl, Inches(1), Inches(2), Inches(8), Inches(1.5),
        [[('제목', b.C['w'])]], size=48, align=PP_ALIGN.CENTER)
    b.pn(sl, 1, 1, dark_bg=True)

build_pptx([my_cover], 'D:/tmp/custom.pptx', ds=ds)
```

---

## 슬라이드 덱 워크플로우

```
Step 0  콘텐츠 재편성      (원본 문서 있을 때 — 선택)
Step 1  슬라이드 구성안    그리드×구성요소 + 핵심 메시지 확정
Step 2  HTML 슬라이드 생성 키보드 네비게이션 포함 (←→ Space F S)
Step 3  Preview Loop       Chrome DevTools 스크린샷 → 반복 수정
Step 4  다중 시안          병렬 생성 후 비교 선택
Step 5  PPTX 변환          slide-pptx-agent 호출 → .pptx (선택, "PPTX로" 요청 시)
```

HTML 슬라이드는 `d:\tmp\slides.html`에 저장되며 브라우저에서 바로 열 수 있다.

---

## python-pptx 정렬 보정

python-pptx의 textbox는 기본 `anchor=TOP` + 내부 상단 여백(~0.05")을 가진다.  
Shape(oval, rect)과 같은 Y에 배치해도 **시각적으로 어긋난다**.

→ 핵심 규칙: shape과 나란한 모든 textbox에 `anchor=MSO_ANCHOR.MIDDLE` 적용

10가지 패턴 상세: [`references/pptx-alignment-patterns.md`](plugins/claude-design/skills/claude-design/references/pptx-alignment-patterns.md)

---

## 라이선스

MIT
