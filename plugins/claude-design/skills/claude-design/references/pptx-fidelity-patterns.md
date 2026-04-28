# PPTX Fidelity Patterns — HTML→PPTX 정밀 변환 가이드

> 본 가이드는 ferrari deck v1→v2→v3→v3.1 검증을 거쳐 도출된 패턴 모음.
> v3.1 기준 6 핵심 슬라이드(S03/S04/S07/S08/S13/S14)에서 100% 해소율 검증 완료.
> 한국어 hero·data 영역에서 PPTX runtime이 ascender+descender에 자동 leading을 추가해
> CSS line-height가 1.15~1.25배 늘어나는 현상이 핵심 문제. 본 패턴들은 그 보상 규칙.

## 핵심 원칙 (3줄)
1. PPTX runtime은 한국어 폰트 line-height를 시각적으로 1.15~1.25배 늘림 → HTML에서 미리 좁게.
2. line_spacing은 ratio가 아닌 Pt 절대값 — font_size별 매핑 테이블 사용.
3. hero와 footer는 zone-separation — clamp 대신 사전 배치.

## 패턴 매트릭스

| 코드 | 명칭 | 적용 위치 | 효과 | 검증 |
|------|------|----------|------|------|
| C-1 | line-height ratio 매핑 (table cell) | table cell | cell line_spacing 1.5 명시 | v2 |
| C-2 | size별 Pt 절대값 line_spacing | hero/data 영역 (size ≥ 40pt) | 한국어 ascender 보상 | v3 |
| C-3 | hero anchor TOP | add_hero_mixed | textbox 정렬 안정화 | v3 |
| D-1' | hero guard footer 사전 배치 | s3·s8·s13·s14 | 660 → 645 사전, hero 면제 | v3 |
| D-2 | mt-auto BOTTOM anchor | flex 자식 mt-auto | 카드 하단 정렬 | v2 |
| D-3 | textbox margin = 0 강제 | 모든 helper | 누적 오차 차단 | v3 |
| F-1 | multiline hero | 두 줄 이상 hero | line_height 직접 계산 (table 우회) | v3.1 |
| B-1 | object-fit:cover crop | 사진 textbox | 비율 보존 | v2 |
| E-1 | 1px rule → rect 0.75pt | divider | connector 거부 회피 | v2 |
| (rule) | 단일 줄 빅 데이터 hero=False | data-xl/md 단일 줄 | label 충돌 방지 | v3.1 |
| (rule) | size_override (4-tuple) | 인라인 size 변경 | "1·tap" 같은 mixed 표현 | v3.1 |

---

## 패턴 디테일

### C-1: line-height 매핑 (table cell)

**증상**: 표 셀에서 한국어 본문이 빽빽하게 보임 (line-height 1.0 ~ 1.2 수준).

**원인**: python-pptx 기본 `paragraph.line_spacing` 미설정 시 PowerPoint가 폰트 metric의 leading만 사용.

**적용 시점**: `slide.shapes.add_table()` 셀 본문(특히 한국어 paragraph cell).

**규칙**:
- 본문 셀(긴 한국어): `p.line_spacing = 1.5`
- 헤더/짧은 라벨 셀: `p.line_spacing = 1.4` 또는 `1.3`
- 영문/숫자 전용 셀(SFR ID, 숫자 토큰 등): `p.line_spacing = 1.3` 충분

**코드 예시** (v3.1 S06 SFR table):
```python
for ri, row in enumerate(rows_data, start=1):
    for ci, val in enumerate(row):
        cell = tbl.cell(ri, ci)
        tf = cell.text_frame
        p = tf.paragraphs[0]
        # [C-1] 본문 셀(한국어) 1.5, 영문/숫자 셀 1.3
        p.line_spacing = 1.5 if ci == 3 else 1.3
```

**예외**: 영문 짧은 라벨 한 줄 셀은 1.0~1.2도 무방.

---

### C-2: size별 Pt 절대값 line_spacing

**증상**: hero 텍스트(56pt 이상)에서 CSS `line-height: 1.0` 의도가 PPTX에서 1.15~1.25로 보임. 두 줄 hero에서 위 줄 마침표(.)와 다음 줄 첫 자가 충돌.

**원인**: PPTX runtime은 한국어 폰트의 ascender+descender를 합산해 시각 line-box를 자동 확장. `paragraph.line_spacing` 을 `1.0` ratio로 주면 그 위에 leading이 또 더해진다.

**해결**: ratio 대신 **Pt 절대값**으로 line_spacing 지정. size별 사전 캘리브레이션.

**LINE_SPACING_PT_TABLE** (v3.1 검증값):
| size_pt 임계값 ≥ | line_spacing_pt |
|------|------|
| 96 | 91 |
| 84 | 80 |
| 72 | 70 |
| 56 | 58 |
| 40 | 44 |
| 28 | 34 |
| 20 | 26 |
| 16 | 24 |
| 14 | 20 |
| 12 | 17 |
| 10 | 14 |
| 8 | 12 |

**코드 예시**:
```python
LINE_SPACING_PT_TABLE = [
    (96, 91), (84, 80), (72, 70), (56, 58), (40, 44),
    (28, 34), (20, 26), (16, 24), (14, 20), (12, 17),
    (10, 14), (8, 12),
]

def line_spacing_pt(size_pt, hero=False):
    """font_size(pt) → line_spacing absolute Pt 값.
    hero=True 시 한 단계 더 압축 (3% 추가)."""
    for thr, sp in LINE_SPACING_PT_TABLE:
        if size_pt >= thr:
            base = sp
            break
    else:
        base = int(size_pt * 1.4)
    if hero and size_pt >= 56:
        base = int(round(base * 0.97))   # [v3.1 F-1] 5%→3% 완화
    return Pt(base)
```

**적용 시점**:
- size ≥ 40pt hero/data 텍스트 → `p.line_spacing = line_spacing_pt(size, hero=True)`
- 20 ≤ size < 40 중형 헤딩 → `line_spacing_pt(size, hero=False)`
- size < 20 본문 → `line_spacing_pt(size)` (Pt 절대값 그대로)

**예외**: 두 줄 이상 hero (multiline=True) → F-1 패턴으로 직접 계산 (테이블 우회).

---

### C-3: hero anchor TOP

**증상**: hero textbox의 첫 줄이 컨테이너 중앙에 붙어 보이거나 위치가 빌드마다 달라짐.

**원인**: textbox `vertical_anchor` 미지정 시 PowerPoint가 기본값을 쓰는데, slide layout 6(blank)에서 placeholder 미사용 시 컨테이너 정렬 규칙이 불안정.

**해결**: hero·heading 모든 textbox에 `tf.vertical_anchor = MSO_ANCHOR.TOP` 명시.

**코드 예시**:
```python
def add_hero_mixed(b, slide, x, y, w, h, lines_parts, size=80, ...):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    _zero_margins(tf)                       # D-3
    tf.vertical_anchor = MSO_ANCHOR.TOP     # ← C-3
    ...
```

**참고**: D-2 BOTTOM 케이스(카드 mt-auto)와 짝. 명시 안 하면 빌드 환경마다 렌더링 차이 발생.

---

### D-1' hero guard (footer 사전 배치)

**증상**: 통합 footer clamp(670px 한계) 로직이 hero 슬라이드(s3/s8/s13/s14)에서 hero 영역을 침식하거나 footer를 본문 위로 끌어올림.

**원인**: clamp는 "본문 bottom + footer가 670px 초과 시 footer를 위로" 끌어올리는 단순 규칙. hero 자체가 큰 size로 본문 ≈ 본 슬라이드 거의 전체 높이를 차지하면 footer 자리가 없어짐.

**해결**: hero 슬라이드는 **clamp를 면제**하고 footer Y 좌표를 사전 배치.

**규칙**:
- hero 슬라이드 footer Y: `645px` (HTML 660 → 사전 -15px)
- hero size 96pt + 두 줄 → 끝 Y ≈ 467px → footer 620~700 zone과 100+ gap 확보
- hero size 78pt + 두 줄 → 끝 Y ≈ 480px → footer 645 OK

**코드 예시** (v3.1 S03/S08/S13):
```python
# [v3 D-1' hero guard] footer Y 660 → 645로 사전 위치 (clamp 불필요)
# 645 + 20 = 665 < 670 OK. body(515+80=595)와도 50px gap 확보.
f_top = 645
add_para(b, sl, px(80), px(f_top), px(400), px(20),
         "— 본 과업의 핵심 명제",
         size=10, color=b.C['mute50'])
```

**적용 슬라이드**: statement 페이지(s3, s8, s13), thankyou(s14).

**S14 zone-separation 예시**:
```
hero:    y=275~480 (size 96, 2줄 × line_spacing 91pt = 약 200px 시각 높이)
footer:  y=620~700 (80px) — hero 침범 불가 zone
```

---

### D-2 mt-auto → BOTTOM anchor

**증상**: 카드 내부 마지막 라벨(`PRIMARY USER · …`)이 카드 하단에 붙지 않고 본문 바로 아래에 위치.

**원인**: HTML `flex` + `margin-top: auto`는 부모 flex 컨테이너의 남은 공간을 모두 위로 밀어내는 패턴. python-pptx textbox는 flex 개념이 없음.

**해결**: 라벨 textbox의 height를 **카드 bottom까지 확장**하고 `vertical_anchor = MSO_ANCHOR.BOTTOM`.

**코드 예시**:
```python
def add_para_bottom(b, slide, x, y, w, h, text, size=12, color=None, ...):
    """flex 자식에 margin-top:auto 적용된 요소 → 하단 정렬 textbox.
    parent box를 전체로 확장하고 anchor=BOTTOM 사용."""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    _zero_margins(tf)                           # D-3
    tf.vertical_anchor = MSO_ANCHOR.BOTTOM      # ← D-2 핵심
    p = tf.paragraphs[0]
    if size <= 18:
        p.line_spacing = line_spacing_pt(size)  # C-2 적용
    ...
```

**적용 위치**: s2 4 pillars sub label, s5 module 카드 PRIMARY USER 라인.

**핵심**: parent box 높이를 의미있게(예: h=28→44) 키워야 anchor=BOTTOM 차이가 보인다.

---

### D-3 textbox margin = 0 강제

**증상**: 다단 본문에서 줄 간격이 미세하게 누적되어 박스가 1~3px씩 어긋남. 특히 footer 클램프 계산 시 오차 누적.

**원인**: python-pptx `text_frame`은 기본 `margin_left/right/top/bottom`이 약 `0.05inch` (≈4.8px) 들어있음. 헬퍼별로 setting이 다르면 누적 오차.

**해결**: 모든 helper에서 textframe 생성 직후 4-margin을 0으로 강제.

**코드 예시**:
```python
def _zero_margins(tf):
    """textframe 내부 padding 모두 0 — 누적 오차 차단."""
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
```

**적용**: `add_hero_mixed`, `add_para`, `add_para_bottom`, 그 외 모든 textbox 생성 헬퍼.

**예외 없음**. 단일 라벨/카운터에도 무조건 적용.

---

### F-1 multiline hero (line_height 직접 계산)

**증상**: 두 줄 이상 hero에서 C-2 테이블 압축(0.97)이 너무 강해 위 줄 마침표(.) descender + 다음 줄 ascender 충돌.

**원인**: 한 줄 hero는 leading 압축이 효과적. 그러나 두 줄 hero는 줄 간 충돌이 시각적으로 더 두드러짐 → 테이블의 일률적 압축이 부적합.

**해결**: `multiline=True` 시 LINE_SPACING_PT_TABLE 우회 → CSS `line_height` 그대로 곱셈 적용.

**코드 예시** (v3.1 S03/S07/S08/S13/S14):
```python
def add_hero_mixed(b, slide, x, y, w, h, lines_parts, size=80,
                   line_height=1.0, multiline=False, hero=True, ...):
    ...
    # [v3.1 F-1b] multiline 명시 시 HTML line_height 그대로 적용
    if multiline and size >= 40:
        ls = Pt(int(round(size * line_height)))    # ← 직접 계산
    elif size >= 40:
        ls = line_spacing_pt(size, hero=hero)      # ← 테이블
    else:
        ls = map_line_height(line_height)          # ← ratio
    ...
```

**적용 사례**:
- S03 `1차년도의 한계를 넘어, / 완성형 MaaS로.` size=72, line_height=1.04, multiline=True
- S07 `Tech. / Differen- / tiation.` size=80, line_height=0.98, multiline=True
- S14 `Thank / You.` size=96, line_height=1.0, multiline=True

**HTML 권장 line_height**: 두 줄 한국어 hero는 0.96~1.04 (한 줄은 0.92도 OK).

---

### B-1 object-fit:cover crop

**증상**: 컨테이너가 16:9인데 원본 사진이 4:3 → `add_picture(width=w, height=h)` 시 사진이 stretch되어 비율 깨짐.

**원인**: python-pptx `add_picture(width, height)`는 강제 stretch. CSS `object-fit: cover`처럼 컨테이너에 맞춰 crop하는 옵션 없음.

**해결**: PIL로 원본 비율 측정 → 컨테이너 비율과 비교 → `pic.crop_left/right/top/bottom`로 초과분 crop.

**코드 예시**:
```python
def add_image_cover(slide, path, x, y, w, h):
    """object-fit:cover 시뮬레이션."""
    with Image.open(path) as im:
        iw, ih = im.size
    img_ratio = iw / ih
    cont_ratio = int(w) / int(h)

    pic = slide.shapes.add_picture(path, x, y, width=w, height=h)

    if img_ratio > cont_ratio:
        # 이미지가 더 가로형 → 좌우 crop
        keep = cont_ratio / img_ratio
        crop = (1 - keep) / 2
        pic.crop_left = crop
        pic.crop_right = crop
    elif img_ratio < cont_ratio:
        # 이미지가 더 세로형 → 위아래 crop
        keep = img_ratio / cont_ratio
        crop = (1 - keep) / 2
        pic.crop_top = crop
        pic.crop_bottom = crop
    return pic
```

**적용**: s1 ferry photo (16:9), s7 van photo (4:5), s10 harbor photo (16:9).

**fallback**: python-pptx <0.6.21 에서는 `pic.crop_*` 미지원 → XML `srcRect` 직접 조작.

---

### E-1 1px rule → rect 0.75pt + connector 금지

**중요: MSO_CONNECTOR_TYPE 사용 절대 금지.**

**증상**: PowerPoint Application.Open() 시 슬라이드가 깨지거나 PPT가 cxnSp(connector shape)를 거부.

**원인**: `MSO_CONNECTOR_TYPE.STRAIGHT` + `schemeClr` 또는 색상 RGBColor 직접 적용 조합이 PowerPoint 2019/365 일부 버전에서 reject.

**해결**: connector 대신 **얇은 직사각형(rect)** 사용. height = `Pt(0.75)` 정도면 1px 라인처럼 보임.

**코드 예시**:
```python
def add_rule_line(slide, x, y, w, color, weight_pt=0.75):
    """수평 1px rule → 얇은 직사각형 (rect h=0.75pt).
    cxnSp connector는 PowerPoint COM/Export에서 가끔 거부 → rect로 안정화."""
    h_emu = Pt(weight_pt)
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h_emu)
    s.fill.solid()
    s.fill.fore_color.rgb = color
    s.line.fill.background()
    spPr = s._element.spPr
    for el in list(spPr):
        if el.tag == qn('a:effectLst'):
            spPr.remove(el)
    etree.SubElement(spPr, qn('a:effectLst'))
    return s
```

**적용**: 모든 1px divider, 카드 내부 hairline rule, 테이블 외 vertical/horizontal rule.

**vertical 1px rule 예시** (S12):
```python
v = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, div_x, data_y, Pt(0.75), px(220))
v.fill.solid(); v.fill.fore_color.rgb = b.C['rule']
v.line.fill.background()
```

**예외**: 2px 이상 thick rule은 `line_rule(slide, x, y, w, color, thickness_px=2)` 별도 헬퍼 (Emu 기반).

---

## Rules

### 단일 줄 빅 데이터 hero=False

**증상**: HTML data 토큰(`95M / 125.9 / 7M / 3 / 1·tap`)이 PPTX에서 위 라벨과 충돌하거나 ascender가 라벨에 닿음.

**규칙**: 단일 줄(한 줄) 빅 데이터 textbox는 `hero=False` 명시 → C-2 hero 압축 미적용.

**코드 예시** (v3.1 S12):
```python
# [v3 C-3] hero=False — 단일 줄 데이터는 line_spacing 압축 불필요
add_hero_mixed(b, sl, cx, data_y + px(36), cw, px(120),
    [[(num, ncolor, True), (unit, b.C['mute50'], True)]],
    size=80, line_height=1.0, hero=False)
```

**대비**: 두 줄 이상 → `multiline=True, hero=True` (F-1 적용).

---

### size_override (4-tuple)

**증상**: 한 hero 라인 안에서 일부 토큰만 size 다르게 (예: `1` 큰 size + `·tap` 작은 size) 표현하고 싶음.

**규칙**: `add_hero_mixed`의 `lines_parts`에 4-tuple `(text, color, bold, size_override)` 지원.

**코드 예시** (v3.1 S09):
```python
# "1·tap" — 1은 size 48, ·tap은 size 18
add_hero_mixed(b, sl, lx + px(190), bb_y, px(220), px(72),
    [[("1", b.C['ink90'], True),
      ("·tap", b.C['mute50'], True, 18)]],     # 4-tuple
    size=48, line_height=1.0)
```

**lines_parts 지원 형식**:
- 2-tuple `(text, color)` — bold=True 기본, size=base
- 3-tuple `(text, color, bold)` — size=base
- 4-tuple `(text, color, bold, size_override)` — 인라인 size 변경

---

## 통합 적용 패턴 (헬퍼별 매트릭스)

| 헬퍼 | C-2 | C-3 | D-3 | F-1 | 비고 |
|------|-----|-----|-----|-----|------|
| `add_hero_mixed` | ✓ | ✓ | ✓ | ✓ | hero/multiline 분기 |
| `add_para` | ✓ | (옵션) | ✓ | — | size별 자동 분기 |
| `add_para_bottom` | ✓ (size≤18) | (anchor=BOTTOM) | ✓ | — | D-2 결합 |
| `add_image_cover` | — | — | — | — | B-1 전용 |
| `add_rule_line` | — | — | — | — | E-1 전용 |

## 검증 결과 (v3.1)

- 6 핵심 슬라이드 (S03 / S04 / S07 / S08 / S13 / S14): 100% 해소.
- 한국어 hero 마침표↔다음줄 충돌: 0건.
- footer 침범: 0건 (clamp 로직 + D-1' hero guard 짝).
- connector 거부: 0건 (전 divider rect 0.75pt 적용).
