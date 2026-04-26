# Tools — PPTX 변환 + 시각 검증 파이프라인

`slide-deck-agent` 모드에서 HTML 슬라이드를 PPTX로 변환하고, 시각 회귀를 비교할 때 사용하는 Python 도구 4종.

## 빠른 설치

```bash
pip install -r requirements.txt
playwright install chromium
```

전제 조건:
- Python 3.10+
- Pretendard / Plus Jakarta Sans 폰트 (`C:\Windows\Fonts\` 설치)
- Microsoft PowerPoint (PPTX → PNG 변환 시 — Windows 전용)

---

## 도구 5종 개요

| 파일 | 역할 | 호출 주체 | 호출 시점 | 진입점 |
|------|------|----------|---------|---------|
| **pptx_utils.py** | 라이브러리 | 다른 모듈 (import) | 항상 | `from pptx_utils import DesignSystem, PptxBuilder, build_pptx` |
| **pptx_export.py** | 슬라이드 빌더 (CLI) | `slide-deck-agent` 모드 | "PPTX로 변환해줘" / "납품 형식 C 선택" 시 | `python pptx_export.py` 또는 `from pptx_export import build` |
| **capture_compare.py** | HTML 슬라이드 스크린샷 | `visual-refiner` / `slide-qa-agent` | HTML 시안 검증 시 | `python capture_compare.py` |
| **pptx_to_png.py** | PPTX → PNG 변환 (Windows COM) | `visual-refiner` (회귀 검증) | PPTX 생성 직후 | `python pptx_to_png.py [pptx] [out_dir] [prefix]` |
| **make_compare.py** | HTML vs PPTX 비교 이미지 | `visual-refiner` (회귀 검증) | `pptx_to_png` 직후 | `python make_compare.py` |

---

## pptx_utils.py — 라이브러리 (직접 실행 ✗)

`DesignSystem` + `PptxBuilder` 두 클래스 제공. 슬라이드 빌더의 기반.

### DesignSystem (디자인 토큰)

```python
from pptx_utils import DesignSystem
from pptx.dml.color import RGBColor

ds = DesignSystem(
    slide_w=10.0, slide_h=5.625,    # inches (16:9)
    margin=0.7, gap=0.18,
    colors={
        'bg':   RGBColor(0xFF, 0xFD, 0xF5),
        'fg':   RGBColor(0x1E, 0x29, 0x3B),
        'v':    RGBColor(0x00, 0x7A, 0xFF),  # accent
        # ...
    }
)
```

### PptxBuilder (슬라이드 헬퍼)

```python
from pptx_utils import PptxBuilder

b = PptxBuilder(ds)
prs = b.new_prs()
sl = b.blank(prs)
b.set_bg(sl, b.C['fg'])
b.add_oval(sl, x, y, w, h, color, alpha=22)
b.add_txt(sl, x, y, w, h, text, size=18, color=b.C['w'], align=PP_ALIGN.CENTER)
b.add_mixed(sl, x, y, w, h, lines, size=42)  # 부분 컬러 텍스트
b.pn(sl, 1, 8, dark_bg=True)                 # 페이지 번호
prs.save('out.pptx')
```

### build_pptx (배치 진입점)

```python
from pptx_utils import build_pptx

build_pptx(
    slide_fns=[slide_cover, slide_intro, slide_content_1, ...],
    output='D:/tmp/slides.pptx',
    ds=ds  # 선택 — 미지정 시 DEFAULT_DS
)
```

---

## pptx_export.py — AI 인플루언서 덱 빌더 (참조 구현)

8개 슬라이드 함수 정의 + `build(output, ds)` 진입점.
**실제 사용 시 이 파일을 복사해 새 콘텐츠용 빌더로 사용하는 것이 권장 패턴.**

### 직접 실행
```bash
cd plugins/claude-design/skills/claude-design/tools/
python pptx_export.py                          # 기본 출력 경로
python pptx_export.py --out D:/tmp/slides.pptx
```

### 모듈 import
```python
from pptx_export import build
from pptx_utils import DesignSystem
from pptx.dml.color import RGBColor

my_ds = DesignSystem(colors={
    **DesignSystem().colors,
    'v': RGBColor(0x00, 0x7A, 0xFF),  # accent만 교체
})
build(output='D:/tmp/custom.pptx', ds=my_ds)
```

### 새 콘텐츠용 빌더 작성 패턴
```python
# my_deck.py
from pptx.util import Inches
from pptx.enum.text import PP_ALIGN
from pptx_utils import DesignSystem, PptxBuilder, build_pptx

def slide_cover(prs, b: PptxBuilder):
    sl = b.blank(prs)
    b.set_bg(sl, b.C['fg'])
    b.add_mixed(sl, Inches(1), Inches(2), Inches(8), Inches(1.5),
        [[('제목', b.C['w'])]], size=48, align=PP_ALIGN.CENTER)
    b.pn(sl, 1, 1, dark_bg=True)
    return sl

build_pptx([slide_cover, ...], 'D:/tmp/out.pptx')
```

---

## capture_compare.py — HTML 슬라이드 스크린샷

Playwright로 `D:/tmp/preview.html`을 열고 ←→ 키 네비게이션하며 각 슬라이드를 1280×720 PNG로 저장.

### 실행
```bash
python capture_compare.py
# → D:/tmp/compare/html_s01.png ~ html_s08.png
```

### 설정 (스크립트 상단 상수)
```python
HTML_PATH = "file:///D:/tmp/preview.html"  # 대상 HTML
TOTAL = 8                                   # 슬라이드 개수
OUT = Path("D:/tmp/compare")                # 출력 폴더
```

호출 시점:
- `slide-qa-agent`가 코드 검수 후 시각 검증을 위해 스크린샷이 필요할 때
- `visual-refiner`가 5차원 품질 평가 전 스크린샷 일괄 캡처 시
- 사용자가 "스크린샷으로 비교" 요청 시

> Chrome DevTools MCP를 단일 슬라이드 검증에 쓰고, 이 스크립트는 **다중 슬라이드 일괄 캡처** 시 사용한다.

---

## pptx_to_png.py — PPTX → PNG 변환 (Windows COM)

PowerPoint COM 자동화로 각 슬라이드를 1280×720 PNG로 export. `make_compare.py`의 입력을 만든다.

### 실행
```bash
python pptx_to_png.py                                          # 기본 경로
python pptx_to_png.py D:/tmp/slides.pptx                       # 입력 지정
python pptx_to_png.py D:/tmp/slides.pptx D:/tmp/pptx_check     # 출력 폴더 지정
python pptx_to_png.py D:/tmp/slides.pptx D:/tmp/pptx_check v5_s  # 파일명 prefix 지정
# → D:/tmp/pptx_check/v4_s01.png ~ v4_sN.png (또는 prefix 변경 시 v5_s*)
```

### 모듈 import
```python
from pptx_to_png import export_pptx_to_png

n = export_pptx_to_png(
    pptx_path="D:/tmp/slides.pptx",
    out_dir="D:/tmp/pptx_check",
    prefix="v4_s",
    width=1280, height=720,
)
print(f"{n} slide(s) exported")
```

### 환경 요구
- **Windows + Microsoft PowerPoint 설치** (COM Automation)
- `pip install pywin32` (requirements.txt에 환경 마커로 포함됨)

> Mac/Linux는 추후 LibreOffice headless (`soffice --headless --convert-to png`) 백엔드 추가 예정. 현재는 Windows 전용.

호출 시점:
- `slide-deck-agent`가 PPTX 모드(C)에서 PPTX 생성 직후
- `visual-refiner`가 회귀 검증 전 PNG 입력 준비 시

---

## make_compare.py — HTML vs PPTX 회귀 비교

`capture_compare.py` 결과(`html_*.png`) + `pptx_to_png.py` 결과(`pptx_check/v4_*.png`)를 좌우로 합쳐 비교 이미지 생성.

### 실행
```bash
python make_compare.py
# → D:/tmp/compare/new_cmp_s01.png ~ new_cmp_s08.png
```

### 입력 파일 위치 (스크립트 내 하드코딩)
```python
html_path = rf"D:\tmp\compare\html_s{i:02d}.png"      # capture_compare.py 출력
pptx_path = rf"D:\tmp\pptx_check\v4_s{i:02d}.png"     # pptx_to_png.py 출력
```

호출 시점:
- HTML → PPTX 변환 후 두 결과의 시각 차이가 의심스러울 때
- `slide-deck-agent`가 PPTX 모드(C)에서 산출물 검증 시
- `visual-refiner`가 회귀 점검 시

---

## 표준 작업 플로 (PPTX 모드)

```
1. slide-deck-agent → HTML 슬라이드 생성
   → D:/tmp/preview.html

2. capture_compare.py → HTML 스크린샷 N장
   → D:/tmp/compare/html_s01.png ...

3. slide-qa-agent → HTML 코드 검수 (자동)

4. visual-refiner → 5차원 품질 평가 (스크린샷 기반)

5. (PPTX 모드) pptx_export.py 또는 사용자 빌더 → PPTX 생성
   → D:/tmp/slides.pptx

6. pptx_to_png.py → PPTX → PNG 변환 (Windows COM)
   → D:/tmp/pptx_check/v4_s01.png ...

7. make_compare.py → HTML vs PPTX 비교 이미지
   → D:/tmp/compare/new_cmp_s01.png ...

8. visual-refiner → 회귀 결과 확인
```

---

## 정렬 보정 참조

python-pptx의 textbox는 기본 `anchor=TOP` + 내부 상단 여백(~0.05")을 가진다.
Shape(oval, rect)과 같은 Y에 배치해도 시각적으로 어긋난다.

→ **핵심 규칙**: shape과 나란한 모든 textbox에 `anchor=MSO_ANCHOR.MIDDLE` 적용.

10가지 정렬 패턴 상세: [`../references/pptx-alignment-patterns.md`](../references/pptx-alignment-patterns.md)
