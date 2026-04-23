"""
pptx_utils.py — python-pptx 공통 헬퍼 + DesignSystem

사용법:
    from pptx_utils import DesignSystem, PptxBuilder, DEFAULT_DS

    ds = DesignSystem(...)           # 커스텀 디자인 시스템
    b  = PptxBuilder(ds)
    prs = b.new_prs()
    sl  = b.blank(prs)
    b.add_txt(sl, ...)
    prs.save('out.pptx')
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree
from dataclasses import dataclass, field
from typing import Optional

RECT  = 1
RRECT = 5
OVAL  = 9


# ─────────────────────────────────────────────────────
# DesignSystem
# ─────────────────────────────────────────────────────

@dataclass
class DesignSystem:
    """모든 디자인 토큰을 담는 데이터 클래스. 변경하고 싶은 값만 override하세요."""

    # 슬라이드 크기
    slide_w: float = 10.0   # inches
    slide_h: float = 5.625  # inches
    margin:  float = 0.7    # side margin
    gap:     float = 0.18   # default gap between elements

    # 색상 팔레트
    colors: dict = field(default_factory=lambda: {
        'bg':   RGBColor(0xFF, 0xFD, 0xF5),
        'fg':   RGBColor(0x1E, 0x29, 0x3B),
        'mute': RGBColor(0xF1, 0xF5, 0xF9),
        'mfg':  RGBColor(0x64, 0x74, 0x8B),
        'v':    RGBColor(0x8B, 0x5C, 0xF6),   # violet / accent
        'p':    RGBColor(0xF4, 0x72, 0xB6),   # pink
        'y':    RGBColor(0xFB, 0xBF, 0x24),   # yellow
        'm':    RGBColor(0x34, 0xD3, 0x99),   # mint
        'bdr':  RGBColor(0xE2, 0xE8, 0xF0),   # border
        'w':    RGBColor(0xFF, 0xFF, 0xFF),
        'w60':  RGBColor(0x99, 0xAA, 0xBB),
        'w80':  RGBColor(0xCC, 0xD5, 0xDE),
        'y_dk': RGBColor(0x92, 0x69, 0x0A),
        'g_dk': RGBColor(0x0D, 0x7A, 0x55),
    })

    # 폰트
    font_heading:      str = 'Pretendard'
    font_body:         str = 'Pretendard'
    font_heading_bold: str = 'Pretendard Black'   # 900 weight family name
    font_english:      str = 'Plus Jakarta Sans'  # 영문 전용


# 기본 디자인 시스템 (AI 인플루언서 테마)
DEFAULT_DS = DesignSystem()


# ─────────────────────────────────────────────────────
# PptxBuilder
# ─────────────────────────────────────────────────────

class PptxBuilder:
    """DesignSystem을 받아 슬라이드 요소를 생성하는 빌더."""

    def __init__(self, ds: DesignSystem = None):
        self.ds = ds or DEFAULT_DS
        self.W  = Inches(self.ds.slide_w)
        self.H  = Inches(self.ds.slide_h)
        self.M  = Inches(self.ds.margin)
        self.GAP = Inches(self.ds.gap)

    @property
    def C(self):
        return self.ds.colors

    @property
    def FH(self):  return self.ds.font_heading
    @property
    def FB(self):  return self.ds.font_body
    @property
    def FHB(self): return self.ds.font_heading_bold
    @property
    def FE(self):  return self.ds.font_english

    # ── Presentation ─────────────────────────────────

    def new_prs(self) -> Presentation:
        prs = Presentation()
        prs.slide_width  = self.W
        prs.slide_height = self.H
        return prs

    def blank(self, prs: Presentation):
        return prs.slides.add_slide(prs.slide_layouts[6])

    # ── Background / Fill ────────────────────────────

    def set_bg(self, slide, color: RGBColor):
        fill = slide.background.fill
        fill.solid()
        fill.fore_color.rgb = color

    def set_alpha(self, shape, pct: float):
        solid = shape.fill._xPr.find('.//' + qn('a:solidFill'))
        if solid is None or len(solid) == 0:
            return
        clr = solid[0]
        for a in clr.findall(qn('a:alpha')):
            clr.remove(a)
        el = etree.SubElement(clr, qn('a:alpha'))
        el.set('val', str(int(pct * 1000)))

    # ── Shapes ───────────────────────────────────────

    def add_rect(self, slide, x, y, w, h, fill: RGBColor,
                 line: Optional[RGBColor] = None, lw=None,
                 rounded=False, alpha=None, radius=None):
        lw = lw or Pt(1.5)
        s = slide.shapes.add_shape(RRECT if rounded else RECT, x, y, w, h)
        s.fill.solid()
        s.fill.fore_color.rgb = fill
        if alpha is not None:
            self.set_alpha(s, alpha)
        if line:
            s.line.color.rgb = line
            s.line.width = lw
        else:
            s.line.fill.background()
        if rounded and radius is not None:
            self.set_radius(s, radius)
        self.no_shadow(s)
        return s

    def add_oval(self, slide, x, y, w, h, fill: RGBColor, alpha=100):
        s = slide.shapes.add_shape(OVAL, x, y, w, h)
        s.fill.solid()
        s.fill.fore_color.rgb = fill
        s.line.fill.background()
        if alpha < 100:
            self.set_alpha(s, alpha)
        self.no_shadow(s)
        return s

    def no_shadow(self, shape):
        spPr = shape._element.spPr
        for el in list(spPr):
            if el.tag in (qn('a:effectLst'), qn('a:effectDag')):
                spPr.remove(el)
        etree.SubElement(spPr, qn('a:effectLst'))

    def set_radius(self, shape, pct=8):
        prstGeom = shape._element.find('.//' + qn('a:prstGeom'))
        if prstGeom is None:
            return
        avLst = prstGeom.find(qn('a:avLst'))
        if avLst is None:
            avLst = etree.SubElement(prstGeom, qn('a:avLst'))
        for gd in avLst.findall(qn('a:gd')):
            avLst.remove(gd)
        gd = etree.SubElement(avLst, qn('a:gd'))
        gd.set('name', 'adj')
        gd.set('fmla', f'val {int(pct * 1000)}')

    # ── Text ─────────────────────────────────────────

    def add_txt(self, slide, x, y, w, h, text, size=13, bold=False,
                color: Optional[RGBColor] = None,
                align=PP_ALIGN.LEFT, font=None, wrap=True, anchor=None):
        color = color or self.C['fg']
        tb = slide.shapes.add_textbox(x, y, w, h)
        tf = tb.text_frame
        tf.word_wrap = wrap
        if anchor:
            tf.vertical_anchor = anchor
        p = tf.paragraphs[0]
        p.alignment = align
        r = p.add_run()
        r.text = text
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = color
        r.font.name = font or self.FH
        return tb

    def add_mixed(self, slide, x, y, w, h, lines_parts,
                  size=36, wrap=True, align=PP_ALIGN.LEFT):
        """
        Multi-line heading with per-run colors.
        lines_parts: [ [(text, color), ...], ... ]
        """
        tb = slide.shapes.add_textbox(x, y, w, h)
        tf = tb.text_frame
        tf.word_wrap = wrap
        first = True
        for line in lines_parts:
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            first = False
            p.alignment = align
            for text, color in line:
                r = p.add_run()
                r.text = text
                r.font.size = Pt(size)
                r.font.bold = False
                r.font.color.rgb = color
                r.font.name = self.FHB
        return tb

    def add_lines(self, slide, x, y, w, h, lines, wrap=True):
        """
        Multi-paragraph text box.
        lines: [{'t': text, 's': size, 'b': bold, 'c': color, 'f': font,
                 'align': PP_ALIGN, 'sp': space_before_pt}, ...]
        """
        tb = slide.shapes.add_textbox(x, y, w, h)
        tf = tb.text_frame
        tf.word_wrap = wrap
        first = True
        for ln in lines:
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            first = False
            p.alignment = ln.get('align', PP_ALIGN.LEFT)
            if ln.get('sp'):
                p.space_before = Pt(ln['sp'])
            r = p.add_run()
            r.text = ln.get('t', '')
            r.font.size = Pt(ln.get('s', 13))
            r.font.bold = ln.get('b', False)
            r.font.color.rgb = ln.get('c', self.C['fg'])
            r.font.name = ln.get('f', self.FH)
        return tb

    # ── Composite widgets ────────────────────────────

    def pn(self, slide, n: int, total: int, dark_bg=False):
        """Page number (bottom-right)."""
        color = RGBColor(0x44, 0x55, 0x66) if dark_bg else RGBColor(0xC8, 0xD2, 0xDC)
        self.add_txt(slide,
                     self.W - Inches(1.3), self.H - Inches(0.36),
                     Inches(1.1), Inches(0.28),
                     f'{n:02d}  -  {total:02d}',
                     size=9, color=color, align=PP_ALIGN.RIGHT)

    def badge(self, slide, x, y, text, bg_color: RGBColor,
              text_color: Optional[RGBColor] = None):
        """Pill badge. Returns next y position."""
        tc = text_color or self.C['w']
        bw = max(Inches(1.5), Inches(len(text) * 0.085 + 0.4))
        bh = Inches(0.27)
        s = self.add_rect(slide, x, y, bw, bh, fill=bg_color, rounded=True)
        self.set_radius(s, 50)
        self.add_txt(slide, x, y, bw, bh, text.upper(), size=9, bold=True,
                     color=tc, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        return y + bh + Inches(0.08)

    def card(self, slide, x, y, w, h, line=True):
        """White rounded card."""
        lc = self.C['bdr'] if line else None
        s = self.add_rect(slide, x, y, w, h, fill=self.C['w'], line=lc,
                          lw=Pt(1.5), rounded=True)
        self.set_radius(s, 6)
        return s

    def mixed_body(self, slide, x, y, w, h, pre, emph, post='',
                   emph_color: Optional[RGBColor] = None, size=11):
        """Body text with inline color emphasis (single paragraph)."""
        ec = emph_color or self.C['m']
        tb = slide.shapes.add_textbox(x, y, w, h)
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        for txt, clr, bold in [
            (pre,  self.C['w80'], False),
            (emph, ec,            True),
            (post, self.C['w80'], False),
        ]:
            if not txt:
                continue
            r = p.add_run()
            r.text = txt
            r.font.size = Pt(size)
            r.font.color.rgb = clr
            r.font.name = self.FB
            r.font.bold = bold
        return tb


# ─────────────────────────────────────────────────────
# build_pptx — 범용 진입점
# ─────────────────────────────────────────────────────

def build_pptx(slide_builders, output_path: str,
               ds: DesignSystem = None) -> Presentation:
    """
    Parameters
    ----------
    slide_builders : list[callable]
        각 함수는 (prs, builder) → slide 시그니처.
        예: [cover_slide, intro_slide, ...]
    output_path : str
        저장 경로 (.pptx)
    ds : DesignSystem, optional
        디자인 시스템. None이면 DEFAULT_DS 사용.

    Returns
    -------
    Presentation
    """
    b = PptxBuilder(ds)
    prs = b.new_prs()
    for fn in slide_builders:
        fn(prs, b)
    prs.save(output_path)
    print(f'Saved: {output_path}  ({len(prs.slides)} slides)')
    return prs
