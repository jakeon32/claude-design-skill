# Claude Design Skill

Claude Code용 디자인 에이전트 플러그인. HTML 프로토타입, 슬라이드 덱, A4 문서, 템플릿 재건, PowerPoint 변환을 포함한다.

## 흐름 (B 흐름)

```
모드 선택 + 콘텐츠 수집 → DESIGN_SYSTEM 확정 → 모드별 생성 → 핸드오프
```

ProjectPlanner → DesignSystemManager → Generator(5개 모드 중 1개) → Handoff.
"PPTX로" 요청 시 메인이 `slide-pptx-agent` 추가 호출.

sub-agent끼리 직접 호출 금지 — 메인이 orchestrate.

## 플러그인 구조

```
plugins/claude-design/
  package.json
  skills/claude-design/
    SKILL.md              ← 스킬 진입점
    agents/               ← 에이전트 14개
                            (project-planner / design-system-manager /
                             prototype / slide-deck / slide-qa / slide-pptx /
                             template / document / other / visual-refiner +
                             선택적: copywriting / animation / responsive / accessibility)
    references/           ← 디자인 레퍼런스
                            (korean-typography, output-common, color-rules,
                             cover-patterns, photo-layouts, pptx-alignment-patterns,
                             qa-pipeline, style-recommender, style-deck-personality,
                             slide-layouts/, styles/, templates/)
    tools/                ← Python 유틸리티
      pptx_utils.py       ← PptxBuilder + DesignSystem (범용 라이브러리)
      pptx_export.py      ← AI 인플루언서 슬라이드 빌더
      pptx_to_png.py      ← PPTX → PNG (Windows COM)
      capture_compare.py  ← Playwright HTML 스크린샷
      make_compare.py     ← HTML vs PPTX 비교 이미지
      requirements.txt
```

## PPTX 도구 설치

```bash
pip install -r plugins/claude-design/skills/claude-design/tools/requirements.txt
playwright install chromium
```

**전제 조건**:
- Python 3.10+
- Microsoft PowerPoint (PPTX → PNG 변환 시)
- Pretendard 폰트 설치 (`C:\Windows\Fonts\`)
- Plus Jakarta Sans 폰트 설치 (선택)

## PPTX 생성 (빠른 시작)

```python
# 기존 AI 인플루언서 덱 생성
from tools.pptx_export import build
build(output='D:/tmp/slides.pptx')

# 커스텀 디자인 시스템 적용
from tools.pptx_utils import DesignSystem, build_pptx
from pptx.dml.color import RGBColor

ds = DesignSystem(colors={**DesignSystem().colors, 'v': RGBColor(0x00, 0x7A, 0xFF)})
build_pptx([cover_fn, content_fn], 'D:/tmp/custom.pptx', ds=ds)
```

## 정렬 보정 참조

`references/pptx-alignment-patterns.md` — python-pptx 정렬 패턴 10가지.
핵심: textbox는 `anchor=MSO_ANCHOR.MIDDLE` 없이 shape과 세로 정렬이 맞지 않는다.
