# python-pptx 정렬 패턴 가이드
source: pptx_export.py 실무 경험 (2026-04)
applies: python-pptx로 슬라이드 생성 시 항상 확인

---

## 핵심 원칙

python-pptx의 textbox는 기본 `anchor=TOP` + 내부 상단 여백(~0.05")을 가진다.
Shape(oval, rect)은 정확히 지정한 Y에서 시작한다.
→ 같은 Y 값으로 배치해도 텍스트와 shape의 **시각적 위치가 불일치**한다.

**항상 지켜야 할 규칙**: oval/shape과 나란히 놓이는 모든 textbox에 `anchor=MSO_ANCHOR.MIDDLE` 적용.

---

## 패턴 1: 원(Oval) + 제목 텍스트 세로 정렬

### 문제
```python
# ❌ 원과 텍스트가 시각적으로 어긋남
add_oval(slide, x + Inches(0.2), y + Inches(0.22), Inches(0.38), Inches(0.38), color)
add_txt(slide, x + Inches(0.7), y + Inches(0.22), w, Inches(0.38), title, size=14, bold=True)
```
- oval center: `y + 0.22 + 0.19 = y + 0.41"`
- 텍스트 실제 렌더: `y + 0.22 + 0.05(내부여백) = y + 0.27"` 시작 → 시각 중심 `y + 0.37"`
- 원이 텍스트보다 아래에 보임

### 해결
```python
# ✅ anchor=MSO_ANCHOR.MIDDLE 로 텍스트박스 세로 중앙 정렬
add_oval(slide, x + Inches(0.2), y + Inches(0.18), Inches(0.38), Inches(0.38), color)
add_txt(slide, x + Inches(0.70), y + Inches(0.18), w, Inches(0.38), title,
        size=14, bold=True, anchor=MSO_ANCHOR.MIDDLE)
```

**규칙**: oval과 title textbox를 **동일 Y**에 배치하고, textbox에 반드시 `anchor=MSO_ANCHOR.MIDDLE` 적용.
textbox 높이는 oval 높이(0.38~0.42")와 맞춤.

---

## 패턴 2: 장식 문자(따옴표 등) + 본문 텍스트 세로 정렬

### 문제
```python
# ❌ 큰 따옴표가 박스 상단에 붙고 본문과 어긋남
add_txt(slide, x + Inches(0.18), box_y + Inches(0.02), Inches(0.42), box_h,
        '"', size=38, bold=True, color=accent)
mixed_body(slide, x + Inches(0.6), box_y + Inches(0.18), ...)
```

### 해결
```python
# ✅ 장식 문자도 anchor=MIDDLE로 박스 내 세로 중앙
add_txt(slide, x + Inches(0.18), box_y, Inches(0.42), box_h,
        '"', size=30, bold=True, color=accent, anchor=MSO_ANCHOR.MIDDLE)
mixed_body(slide, x + Inches(0.6), box_y + Inches(0.14), ...)
```

**규칙**:
- 장식 문자 textbox Y = 박스 Y (오프셋 없이), height = 박스 전체 높이
- `anchor=MSO_ANCHOR.MIDDLE` 적용
- 폰트 크기는 박스 높이의 ~40% 수준이 적절 (box_h=0.72" → size≈28~32)

---

## 패턴 3: 카드 높이와 페이지번호 겹침 방지

### 계산 공식
```
# 페이지번호 위치: H - Inches(0.36) = 5.265" (16:9 기준)
# 카드 하단 여유: 최소 Inches(0.2) 확보

max_card_bottom = H - Inches(0.56)  # = 5.065"

# N행 카드 높이 계산:
# start_y + (N * card_h) + ((N-1) * gap) ≤ max_card_bottom
```

### 2×2 그리드 권장값 (16:9, margin=0.7")
```python
gh = Inches(1.5)    # 행당 카드 높이 (1.75" → 겹침 발생)
gap = Inches(0.18)  # 카드 간격
# 2행 하단: ~5.07" → 페이지번호(5.27") 위로 안전
```

---

## 패턴 4: 소형 원(작은 bullet 원) + 아이템 타이틀 정렬

### 문제
```python
# ❌ 소형 원(0.14") 옆 텍스트 상단 정렬 → 원이 텍스트 상단에만 걸림
add_oval(slide, x + Inches(0.22), iy + Inches(0.1), Inches(0.14), Inches(0.14), color)
add_txt(slide, x + Inches(0.46), iy, w, Inches(0.34), name, size=14, bold=True)
```
- oval center: `iy + 0.1 + 0.07 = iy + 0.17"`
- 텍스트 TOP anchor 시각 중심: `iy + 0.05 + 0.097 = iy + 0.147"` → 0.023" 차이 → 미세 어긋남

### 해결
```python
# ✅ textbox 높이가 원과 같다면 anchor=MIDDLE만으로 완벽히 맞춤
add_oval(slide, x + Inches(0.22), iy + Inches(0.1), Inches(0.14), Inches(0.14), color)
add_txt(slide, x + Inches(0.46), iy, w, Inches(0.34), name,
        size=14, bold=True, anchor=MSO_ANCHOR.MIDDLE)
```

**수식**: textbox 높이 = `oval_top_offset × 2 + oval_h` 일 때 anchor=MIDDLE로 정확히 맞음.
(예: oval_top=0.1", oval_h=0.14" → textbox_h=0.34" → textbox center=iy+0.17" ✓)

---

## 패턴 5: 패널 헤더 소형 oval + 레이블 텍스트 정렬

### 문제
```python
# ❌ 헤더 레이블 Y가 oval Y보다 아래로 지정되어 수직 불일치
add_oval(slide, x + Inches(0.22), py + Inches(0.20), Inches(0.30), Inches(0.30), color)
add_txt(slide, x + Inches(0.60), py + Inches(0.24), w, Inches(0.36), 'LABEL', size=11)
# oval center: py+0.35" / 텍스트 center(TOP anchor): py+0.24+0.05+0.076=py+0.366" → 오차 0.016"
```

### 해결
```python
# ✅ 텍스트 Y = oval Y, 높이 = oval 높이, anchor=MIDDLE
add_oval(slide, x + Inches(0.22), py + Inches(0.20), Inches(0.30), Inches(0.30), color)
add_txt(slide, x + Inches(0.60), py + Inches(0.20), w, Inches(0.30), 'LABEL',
        size=11, anchor=MSO_ANCHOR.MIDDLE)
```

**규칙**: 헤더 레이블 textbox는 oval과 **완전히 동일한 Y + 동일한 높이**, anchor=MIDDLE.

---

## 패턴 6: 번호 원(Numbered Circle) 내 숫자 텍스트 중앙 정렬

### 문제
```python
# ❌ 번호 원 안의 숫자 텍스트가 상단에 붙음
add_oval(slide, M + Inches(0.15), ly + Inches(0.23), Inches(0.38), Inches(0.38), color, alpha=15)
add_txt(slide, M + Inches(0.15), ly + Inches(0.23), Inches(0.38), Inches(0.38),
        str(i+1), size=13, bold=True, align=PP_ALIGN.CENTER)
# oval center: ly+0.42" / 숫자 TOP anchor 시각 중심: ly+0.23+0.05+0.09=ly+0.37" → 어긋남
```

### 해결
```python
# ✅ textbox와 oval이 동일 Y + 동일 크기 → anchor=MIDDLE
add_txt(slide, M + Inches(0.15), ly + Inches(0.23), Inches(0.38), Inches(0.38),
        str(i+1), size=13, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
```

**적용 범위**: 모든 번호 원(numbered circle), 스텝 원(step circle), badge 숫자 등.

---

## 패턴 7: Pill(알약형) 버튼 텍스트 세로 중앙 정렬

### 문제
```python
# ❌ pill 높이 0.3" 안에서 텍스트가 상단에 붙음
add_rect(slide, px, py, pw, Inches(0.3), fill=bg, rounded=True, radius=50)
add_txt(slide, px, py, pw, Inches(0.3), text, size=11, align=PP_ALIGN.CENTER)
```

### 해결
```python
# ✅ anchor=MIDDLE로 pill 내 세로 중앙 정렬
add_txt(slide, px, py, pw, Inches(0.3), text, size=11,
        align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
```

**규칙**: pill, badge, tag 등 height가 고정된 컨테이너 안 텍스트는 항상 anchor=MIDDLE.

---

## 패턴 8: 카드 내 아이콘(emoji) 삽입

HTML 슬라이드의 emoji/아이콘을 PPTX에 재현할 때:

```python
# ✅ Segoe UI Emoji 폰트로 emoji 텍스트 삽입
add_txt(slide, tx + Inches(0.18), ty + Inches(0.16), tw - Inches(0.3), Inches(0.28),
        '🧶', size=18, color=accent_color, font='Segoe UI Emoji')
```

**주의사항**:
- emoji 삽입 시 카드 내 하위 요소(title, pill, body) Y 좌표를 아이콘 높이만큼 아래로 이동
- 권장 아이콘 크기: `size=18~20`, height=`Inches(0.26~0.30)`
- `Segoe UI Emoji` 폰트 지정 필수 (미지정 시 emoji 렌더링 불안정)
- 비-emoji 특수문자(✦, 〰️ 등)도 동일 폰트 적용 권장

### 카드 레이아웃 조정 예시 (아이콘 추가 전→후)
```
[before]          [after]
ty+0.10  accent bar    ty+0.10  accent bar
ty+0.14  title         ty+0.16  icon  (0.28" height)
ty+0.60  tag pill      ty+0.44  title
ty+0.92  body text     ty+0.80  tag pill
                        ty+1.08  body text
```

---

## 패턴 9: 세로 정렬이 필요한 모든 경우 체크리스트

| 상황 | 적용 |
|------|------|
| Oval + 제목 텍스트 (대형 0.38"+) | `anchor=MIDDLE`, 동일 Y, 동일 높이 |
| Oval + 제목 텍스트 (소형 0.14") | `anchor=MIDDLE`, textbox h = oval_offset×2 + oval_h |
| 번호 원 + 숫자 텍스트 | `anchor=MIDDLE`, 동일 Y, 동일 크기 |
| 장식 따옴표 + 본문 | `anchor=MIDDLE`, box_y 기준, h = box 전체 |
| 패널 헤더 oval + 레이블 | `anchor=MIDDLE`, 동일 Y, 동일 높이 |
| Pill / badge 텍스트 | `anchor=MIDDLE` |
| emoji 아이콘 | `font='Segoe UI Emoji'`, size=18~20 |

---

## 패턴 10: 좌측 컬러 바(Left Accent Bar) 두께

HTML card의 좌측 컬러 강조 바를 PPTX로 재현할 때 최소 두께:

```python
# ❌ 너무 얇아서 시각적으로 잘 안 보임
add_rect(slide, M, ly, Inches(0.032), lh, fill=color)

# ✅ 충분히 보이는 두께
add_rect(slide, M, ly, Inches(0.05), lh, fill=color)
```

권장 두께: `Inches(0.05)` (≈ 4.8px @ 96dpi)

---

## 구현 참고: add_txt 헬퍼

```python
from pptx.enum.text import MSO_ANCHOR

def add_txt(slide, x, y, w, h, text, size=13, bold=False, color=None,
            align=PP_ALIGN.LEFT, font=None, wrap=True, anchor=None):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    if anchor:
        tf.vertical_anchor = anchor   # ← 핵심
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color or C['fg']
    r.font.name = font or FH
    return tb
```

## 변환 파이프라인 (HTML → PPTX 비교 검증)

```
1. python pptx_export.py          → slides_v4.pptx 생성
2. PowerShell COM export           → pptx_check/v4_s01~08.png
3. python capture_compare.py       → compare/html_s01~08.png  (Playwright)
4. python make_compare.py          → compare/new_cmp_s01~08.png
5. 비교 이미지 눈으로 확인 → 보정값 추가 → 1번으로 반복
```

### PowerShell COM PPTX→PNG 변환 스니펫
```powershell
$ppt = New-Object -ComObject PowerPoint.Application
$ppt.Visible = [Microsoft.Office.Core.MsoTriState]::msoTrue
$pres = $ppt.Presentations.Open($pptxPath, $false, $false, $false)
for ($i = 1; $i -le $pres.Slides.Count; $i++) {
    $pres.Slides($i).Export("$outDir\s{0:D2}.png" -f $i, "PNG", 1280, 720)
}
$pres.Close(); $ppt.Quit()
```
