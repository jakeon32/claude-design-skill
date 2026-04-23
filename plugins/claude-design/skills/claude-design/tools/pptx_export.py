#!/usr/bin/env python3
"""
AI 인플루언서 슬라이드 덱  v4
pptx_utils.PptxBuilder 기반으로 리팩터.
커스텀 디자인 시스템을 주입하려면 build() 에 ds= 를 전달하세요.

  from pptx_export import build
  from pptx_utils import DesignSystem
  from pptx.dml.color import RGBColor

  my_ds = DesignSystem(colors={...})   # 토큰 override
  build(output='out.pptx', ds=my_ds)
"""
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx_utils import DesignSystem, PptxBuilder, build_pptx


# ══════════════════════════════════════════════════════
# S1 — COVER
# ══════════════════════════════════════════════════════
def slide_cover(prs, b: PptxBuilder):
    sl = b.blank(prs)
    b.set_bg(sl, b.C['fg'])
    b.add_oval(sl, Inches(6.8),  Inches(-1.5), Inches(5.0), Inches(5.0), b.C['v'], alpha=22)
    b.add_oval(sl, Inches(-0.8), Inches(3.2),  Inches(3.8), Inches(3.8), b.C['p'], alpha=14)
    b.add_oval(sl, Inches(5.5),  Inches(2.2),  Inches(1.8), Inches(1.8), b.C['y'], alpha=18)

    b.add_mixed(sl, Inches(1.2), Inches(1.9), Inches(7.6), Inches(1.8),
        [
            [('초사실적 ', b.C['w']), ('AI', b.C['v']), (' 인플루언서', b.C['w'])],
            [('생성 전략 지침서', b.C['w'])],
        ], size=42, align=PP_ALIGN.CENTER)

    b.add_txt(sl, Inches(1.2), Inches(3.25), Inches(7.6), Inches(0.5),
              '프롬프트 아키텍처로 완성하는 5대 전략',
              size=18, color=b.C['w60'], align=PP_ALIGN.CENTER, font=b.FB)

    b.pn(sl, 1, 8, dark_bg=True)
    return sl


# ══════════════════════════════════════════════════════
# S2 — 서론
# ══════════════════════════════════════════════════════
def slide_intro(prs, b: PptxBuilder):
    sl = b.blank(prs)
    b.set_bg(sl, b.C['bg'])

    LW = Inches(4.4)
    RW = Inches(3.9)
    RX = b.M + LW + Inches(0.3)
    START_Y = Inches(1.05)

    y = b.badge(sl, b.M, START_Y, 'Chapter 01 — 서론', b.C['v'])

    b.add_mixed(sl, b.M, y, LW, Inches(1.15),
        [
            [('AI 인플루언서는', b.C['fg'])],
            [('브랜드 자산', b.C['v']), ('입니다', b.C['fg'])],
        ], size=24)

    b.add_txt(sl, b.M, y + Inches(1.18), LW, Inches(0.85),
              '디지털 대전환 시대, 정교하게 설계된 AI 모델은\n소비자 몰입도를 극대화하고 구매 전환율·마케팅 ROI를 견인합니다.',
              size=13, color=b.C['mfg'], font=b.FB)

    sy = y + Inches(2.18)
    stat_items = [('CVR', '구매 전환율 향상'), ('ROI', '마케팅 효율'), ('Brand', '에쿼티 형성')]
    sw = Inches(1.44)
    for i, (val, label) in enumerate(stat_items):
        sx = b.M + i * sw
        b.add_txt(sl, sx, sy, sw, Inches(0.52), val,
                  size=26, bold=True, color=b.C['fg'], align=PP_ALIGN.CENTER)
        b.add_txt(sl, sx, sy + Inches(0.5), sw, Inches(0.28), label,
                  size=10, color=b.C['mfg'], align=PP_ALIGN.CENTER, font=b.FB)
        if i < 2:
            b.add_rect(sl, sx + sw - Inches(0.01), sy + Inches(0.05),
                       Inches(0.015), Inches(0.65), fill=b.C['bdr'])

    icons  = ['🎯', '💡', '✦']
    titles = ['고부가가치 비주얼', '인지 심리학 + 미학', '상업적 무결성 지향']
    bodies = [
        '전략적으로 설계된 비주얼은 독보적인 브랜드 에쿼티를 형성합니다.',
        '소비자의 시선을 사로잡으면서 브랜드 품격을 유지하는 전략적 접근.',
        "자극적 노출이 아닌 '고급스러운 섹시함'과 상업적 무결성의 균형.",
    ]
    ic = [b.C['v'], b.C['p'], b.C['y']]
    ch = Inches(1.45)
    for i in range(3):
        cy = Inches(0.42) + i * (ch + b.GAP)
        b.card(sl, RX, cy, RW, ch)
        b.add_oval(sl, RX + Inches(0.18), cy + Inches(0.22), Inches(0.38), Inches(0.38), ic[i])
        b.add_txt(sl, RX + Inches(0.68), cy + Inches(0.22), RW - Inches(0.78),
                  Inches(0.38), titles[i], size=13, bold=True, color=b.C['fg'], font=b.FB,
                  anchor=MSO_ANCHOR.MIDDLE)
        b.add_txt(sl, RX + Inches(0.18), cy + Inches(0.65), RW - Inches(0.3),
                  Inches(0.72), bodies[i], size=11, color=b.C['mfg'], font=b.FB)

    b.pn(sl, 2, 8)
    return sl


# ══════════════════════════════════════════════════════
# S3 — 전략 1 (Header + 2×2 Grid)
# ══════════════════════════════════════════════════════
def slide_s3(prs, b: PptxBuilder):
    sl = b.blank(prs)
    b.set_bg(sl, b.C['bg'])
    CW = b.W - 2 * b.M
    START_Y = Inches(0.42)

    y = b.badge(sl, b.M, START_Y, '전략 01', b.C['v'])

    b.add_mixed(sl, b.M, y, CW, Inches(0.75),
        [[('의도적 긴장감과 ', b.C['fg']), ('심리적 거리감', b.C['v']), ('의 설계', b.C['fg'])]],
        size=26)

    b.add_txt(sl, b.M, y + Inches(0.68), CW, Inches(0.35),
              '섹시함의 본질은 노출 수위가 아닌 관찰자와 모델 사이의 심리적 기류에서 나온다',
              size=13, color=b.C['mfg'], font=b.FB)

    gw = (CW - b.GAP) / 2
    gh = Inches(1.5)
    gcols = [b.M, b.M + gw + b.GAP]
    grows = [y + Inches(1.12), y + Inches(1.12) + gh + b.GAP]
    ic_colors = [b.C['v'], b.C['p'], b.C['y'], b.C['m']]
    items = [
        ('Intimate Mood',    '모델과 사적인 공간을 공유하는 듯한 친밀감으로 소비자 몰입도를 극대화합니다.'),
        ('Private Moment',   "비공개된 비밀스러운 찰나를 포착한 느낌으로 '특권적 시선'을 부여합니다."),
        ('Corner Glance',    '직접 정면 응시 대신 구석에서의 시선 처리로 신비로움과 긴장감을 형성합니다.'),
        ('Slow Breath Vibe', '정적 이미지에 동적 호흡의 흔적을 추가해 관찰자의 본능적 감각을 자극합니다.'),
    ]
    for idx, (title, body) in enumerate(items):
        col = idx % 2; row = idx // 2
        gx = gcols[col]; gy = grows[row]
        ac = ic_colors[idx]
        b.card(sl, gx, gy, gw, gh)
        b.add_oval(sl, gx + Inches(0.2), gy + Inches(0.18), Inches(0.38), Inches(0.38), ac)
        b.add_txt(sl, gx + Inches(0.70), gy + Inches(0.18), gw - Inches(0.78),
                  Inches(0.38), title, size=14, bold=True, color=b.C['fg'], font=b.FB,
                  anchor=MSO_ANCHOR.MIDDLE)
        b.add_txt(sl, gx + Inches(0.2), gy + Inches(0.65), gw - Inches(0.35),
                  Inches(0.78), body, size=12, color=b.C['mfg'], font=b.FB)

    b.pn(sl, 3, 8)
    return sl


# ══════════════════════════════════════════════════════
# S4 — 전략 2 (Header + 3 Cards + Dark Note)
# ══════════════════════════════════════════════════════
def slide_s4(prs, b: PptxBuilder):
    sl = b.blank(prs)
    b.set_bg(sl, b.C['bg'])
    CW = b.W - 2 * b.M
    START_Y = Inches(1.0)

    y = b.badge(sl, b.M, START_Y, '전략 02', b.C['p'])

    b.add_mixed(sl, b.M, y, CW, Inches(0.75),
        [[('자연스러운 신체 곡선과 ', b.C['fg']), ('포즈', b.C['p']), (' 아키텍처', b.C['fg'])]],
        size=26)

    b.add_txt(sl, b.M, y + Inches(0.68), CW, Inches(0.35),
              "인위적 포즈는 '불쾌한 골짜기'를 유발한다 — 일상 맥락 속 자연스러운 텐션이 상업적 가치를 만든다",
              size=13, color=b.C['mfg'], font=b.FB)

    cy = y + Inches(1.12)
    pw = (CW - 2 * b.GAP) / 3
    ch = Inches(1.72)
    items = [
        (b.C['p'], 'S자 곡선 형성',    'S자 곡선이나 기울어진 골반은 신체 입체감을 구현하는 핵심. 평면적 포즈를 입체적으로 전환합니다.',  'Hips Angled Forward'),
        (b.C['y'], '물리적 텐션 배합', '등에서 골반으로 이어지는 라인을 강조하여 역동성과 우아한 실루엣을 동시에 완성합니다.',           'Arched Long Curve'),
        (b.C['m'], '임계값 설정 원칙', "포즈가 '작위적'으로 느껴지는 순간 상업적 가치는 급락합니다. 일상 맥락을 유지하세요.",            'Naturalness Threshold'),
    ]
    for i, (ac, title, body, tag) in enumerate(items):
        cx = b.M + i * (pw + b.GAP)
        b.card(sl, cx, cy, pw, ch)
        b.add_rect(sl, cx + Inches(0.15), cy + Inches(0.1), pw - Inches(0.3), Inches(0.035), fill=ac)
        b.add_txt(sl, cx + Inches(0.18), cy + Inches(0.14), pw, Inches(0.38),
                  title, size=14, bold=True, color=b.C['fg'], font=b.FH)
        b.add_rect(sl, cx + Inches(0.18), cy + Inches(0.6),
                   pw - Inches(0.36), Inches(0.22), fill=b.C['mute'], rounded=True, radius=50)
        b.add_txt(sl, cx + Inches(0.18), cy + Inches(0.59),
                  pw - Inches(0.36), Inches(0.24), tag, size=9,
                  color=b.C['mfg'], align=PP_ALIGN.CENTER, font=b.FH)
        b.add_txt(sl, cx + Inches(0.18), cy + Inches(0.92), pw - Inches(0.3),
                  Inches(0.72), body, size=11, color=b.C['mfg'], font=b.FB)

    ny = cy + ch + Inches(0.16)
    nh = Inches(0.7)
    b.add_rect(sl, b.M, ny, CW, nh, fill=b.C['fg'], rounded=True, radius=6)
    b.add_txt(sl, b.M + Inches(0.22), ny + Inches(0.08), Inches(1.8), nh,
              "Architect's Note", size=12, bold=True, color=b.C['y'], font=b.FH)
    b.mixed_body(sl, b.M + Inches(1.94), ny + Inches(0.1), CW - Inches(2.1), nh - Inches(0.18),
                 pre='무릎을 살짝 올린 자세, 의자에 걸터앉은 자세 등 일상적 맥락을 유지하면서 신체 텐션을 확보하는 것이 전문가의 기술. ',
                 emph='과유불급의 원칙.',
                 emph_color=b.C['y'], size=11)

    b.pn(sl, 4, 8)
    return sl


# ══════════════════════════════════════════════════════
# S5 — 전략 3·4 (Header + Dark/Light Split)
# ══════════════════════════════════════════════════════
def slide_s5(prs, b: PptxBuilder):
    sl = b.blank(prs)
    b.set_bg(sl, b.C['bg'])
    CW = b.W - 2 * b.M
    START_Y = Inches(0.42)

    y = b.badge(sl, b.M, START_Y, '전략 03 · 04', b.C['y'], text_color=b.C['fg'])

    b.add_mixed(sl, b.M, y, CW, Inches(0.75),
        [[('파워-휴머니티 ', b.C['fg']), ('밸런스', b.C['y'])]],
        size=26)

    b.add_txt(sl, b.M, y + Inches(0.68), CW, Inches(0.35),
              '지배적 시선(Power)과 미세 신호(Humanity)의 결합이 하이엔드 브랜딩을 완성한다',
              size=13, color=b.C['mfg'], font=b.FB)

    pw = (CW - b.GAP) / 2
    py = y + Inches(1.12)
    ph = b.H - py - Inches(0.32)

    b.add_rect(sl, b.M, py, pw, ph, fill=b.C['fg'], rounded=True, radius=6)
    b.add_oval(sl, b.M + Inches(0.22), py + Inches(0.20), Inches(0.30), Inches(0.30), b.C['y'])
    b.add_txt(sl, b.M + Inches(0.60), py + Inches(0.20), pw - Inches(0.4), Inches(0.30),
              'POWER — 지배적 시선', size=11, color=b.C['w60'], font=b.FH, anchor=MSO_ANCHOR.MIDDLE)
    pow_items = [
        ('Dominant Gaze',          '상황을 주도하는 주체로 격상. 브랜드 위엄을 세우는 결정적 차이.'),
        ('Unwavering Eye Contact', '흔들림 없는 눈빛. 소비되는 객체가 아닌 브랜드 권위의 상징.'),
        ('Commanding Energy',      '저급 이미지와 하이엔드 브랜딩을 구분 짓는 결정적 에너지.'),
    ]
    for i, (name, desc) in enumerate(pow_items):
        iy = py + Inches(0.75) + i * Inches(0.88)
        b.add_oval(sl, b.M + Inches(0.22), iy + Inches(0.1), Inches(0.14), Inches(0.14), b.C['y'])
        b.add_txt(sl, b.M + Inches(0.46), iy, pw - Inches(0.52), Inches(0.34),
                  name, size=14, bold=True, color=b.C['w'], font=b.FB, anchor=MSO_ANCHOR.MIDDLE)
        b.add_txt(sl, b.M + Inches(0.46), iy + Inches(0.34), pw - Inches(0.52), Inches(0.48),
                  desc, size=11, color=b.C['w60'], font=b.FB)

    rx = b.M + pw + b.GAP
    b.add_rect(sl, rx, py, pw, ph, fill=b.C['w'], line=b.C['bdr'], rounded=True, radius=6)
    b.add_oval(sl, rx + Inches(0.22), py + Inches(0.20), Inches(0.30), Inches(0.30), b.C['m'])
    b.add_txt(sl, rx + Inches(0.60), py + Inches(0.20), pw - Inches(0.4), Inches(0.30),
              'HUMANITY — 미세 신호', size=11, color=b.C['mfg'], font=b.FH, anchor=MSO_ANCHOR.MIDDLE)
    hum_items = [
        ('Half-closed Eyes',     '반쯤 감긴 눈. 정지 프레임에 리듬을 부여합니다.'),
        ('Slightly Parted Lips', '살짝 벌린 입술. 인간적 생동감과 온기를 더합니다.'),
        ('Slow Breath Vibe',     '인위성을 제거하고 감성적 몰입을 유도하는 고도의 기술.'),
    ]
    for i, (name, desc) in enumerate(hum_items):
        iy = py + Inches(0.75) + i * Inches(0.88)
        b.add_oval(sl, rx + Inches(0.22), iy + Inches(0.1), Inches(0.14), Inches(0.14), b.C['m'])
        b.add_txt(sl, rx + Inches(0.46), iy, pw - Inches(0.52), Inches(0.34),
                  name, size=14, bold=True, color=b.C['fg'], font=b.FB, anchor=MSO_ANCHOR.MIDDLE)
        b.add_txt(sl, rx + Inches(0.46), iy + Inches(0.34), pw - Inches(0.52), Inches(0.48),
                  desc, size=11, color=b.C['mfg'], font=b.FB)

    b.pn(sl, 5, 8)
    return sl


# ══════════════════════════════════════════════════════
# S6 — 전략 5 (Header + 3 Cards + Quote)
# ══════════════════════════════════════════════════════
def slide_s6(prs, b: PptxBuilder):
    sl = b.blank(prs)
    b.set_bg(sl, b.C['bg'])
    CW = b.W - 2 * b.M
    START_Y = Inches(0.78)

    y = b.badge(sl, b.M, START_Y, '전략 05', b.C['m'], text_color=b.C['fg'])

    b.add_mixed(sl, b.M, y, CW, Inches(0.75),
        [[('옷감의 질감으로 전달하는 ', b.C['fg']), ('촉각적 사실성', b.C['m'])]],
        size=26)

    b.add_txt(sl, b.M, y + Inches(0.68), CW, Inches(0.35),
              '시각 정보가 뇌 내에서 촉각적 경험으로 전이될 때 인간은 가장 강한 사실성을 느낀다',
              size=13, color=b.C['mfg'], font=b.FB)

    tw = (CW - 2 * b.GAP) / 3
    ty = y + Inches(1.12)
    th = Inches(1.72)
    accents = [b.C['m'], b.C['v'], b.C['p']]
    t_items = [
        ('🧶',  'Ribbed Knit',          '골지 니트',    '빛의 굴절과 그림자를 통해 신체 굴곡을 입체적으로 증명. 소재 자체가 비주얼 아키텍처입니다.'),
        ('〰️', 'Fabric Tension Lines', '텐션 라인',    '옷감이 신체에 밀착될 때 발생하는 미세한 물리적 변화. 촉각적 상상력을 극도로 자극합니다.'),
        ('✦',  'Micro Wrinkles',       '마이크로 주름', '세련된 섹시함은 노출보다 신체 라인의 암시에서 비롯됩니다. 디테일이 현실감을 완성합니다.'),
    ]
    for i, (icon, title, tag, body) in enumerate(t_items):
        tx = b.M + i * (tw + b.GAP)
        b.card(sl, tx, ty, tw, th)
        b.add_rect(sl, tx + Inches(0.15), ty + Inches(0.1), tw - Inches(0.3), Inches(0.035), fill=accents[i])
        b.add_txt(sl, tx + Inches(0.18), ty + Inches(0.16), tw - Inches(0.3), Inches(0.28),
                  icon, size=18, color=accents[i], font='Segoe UI Emoji')
        b.add_txt(sl, tx + Inches(0.18), ty + Inches(0.44), tw, Inches(0.32),
                  title, size=14, bold=True, color=b.C['fg'], font=b.FH)
        b.add_rect(sl, tx + Inches(0.18), ty + Inches(0.80),
                   tw - Inches(0.36), Inches(0.22), fill=b.C['mute'], rounded=True, radius=50)
        b.add_txt(sl, tx + Inches(0.18), ty + Inches(0.79),
                  tw - Inches(0.36), Inches(0.24), tag, size=9,
                  color=b.C['mfg'], align=PP_ALIGN.CENTER, font=b.FH, anchor=MSO_ANCHOR.MIDDLE)
        b.add_txt(sl, tx + Inches(0.18), ty + Inches(1.08), tw - Inches(0.3),
                  Inches(0.60), body, size=11, color=b.C['mfg'], font=b.FB)

    qy = ty + th + Inches(0.14)
    qh = Inches(0.72)
    b.add_rect(sl, b.M, qy, CW, qh, fill=b.C['fg'], rounded=True, radius=6)
    b.add_txt(sl, b.M + Inches(0.18), qy, Inches(0.42), qh,
              '"', size=30, bold=True, color=b.C['m'], font=b.FH, anchor=MSO_ANCHOR.MIDDLE)
    b.mixed_body(sl, b.M + Inches(0.6), qy + Inches(0.14), CW - Inches(0.75), Inches(0.5),
                 pre='세련된 섹시함은 직접적인 노출보다 ',
                 emph='옷감의 텍스처를 통해 전달되는 신체 라인의 암시',
                 post='에서 비롯됩니다.',
                 emph_color=b.C['m'], size=12)

    b.pn(sl, 6, 8)
    return sl


# ══════════════════════════════════════════════════════
# S7 — 아키텍처 (Header + 4 Layers)
# ══════════════════════════════════════════════════════
def slide_s7(prs, b: PptxBuilder):
    sl = b.blank(prs)
    b.set_bg(sl, b.C['bg'])
    CW = b.W - 2 * b.M
    START_Y = Inches(0.5)

    y = b.badge(sl, b.M, START_Y, '통합 프롬프트 아키텍처', b.C['v'])

    b.add_mixed(sl, b.M, y, CW, Inches(0.75),
        [[('표준 ', b.C['fg']), ('프롬프트 템플릿', b.C['v'])]],
        size=26)

    b.add_txt(sl, b.M, y + Inches(0.68), CW, Inches(0.35),
              '대괄호 안의 변수만 수정하여 즉시 전문적인 결과물을 도출하는 4레이어 구조',
              size=13, color=b.C['mfg'], font=b.FB)

    ac     = [b.C['v'], b.C['p'], b.C['y'], b.C['m']]
    ac_txt = [b.C['v'], b.C['p'], b.C['y_dk'], b.C['g_dk']]
    layers = [
        ('Technical Parameters — 기술 파라미터',
         'Photorealistic, 8k, Ultra-detailed, 85mm lens, f/1.8, Soft cinematic lighting, Film grain'),
        ('Strategic Core — 핵심 전략 키워드 (전략 1·3·4)',
         'Intimate mood, Private moment, Dominant gaze, Unwavering eye contact, Slightly parted lips'),
        ('Environmental Setting — 환경 설정',
         'Inside {Location: luxury car / Private hallway / Rooftop}, Dimly lit, Volumetric fog'),
        ('Variable Input — 가변 입력 (전략 2·5)',
         'Pose: {Knee up, Hips angled forward} / Outfit: {Ribbed knit, Tension lines, Micro wrinkles}'),
    ]
    lh = Inches(0.78)
    for i, (title, code) in enumerate(layers):
        ly = y + Inches(1.0) + i * (lh + Inches(0.07))
        b.card(sl, b.M, ly, CW, lh)
        b.add_rect(sl, b.M, ly, Inches(0.05), lh, fill=ac[i])
        b.add_oval(sl, b.M + Inches(0.15), ly + Inches(0.23), Inches(0.38), Inches(0.38), ac[i], alpha=15)
        b.add_txt(sl, b.M + Inches(0.15), ly + Inches(0.23), Inches(0.38), Inches(0.38),
                  str(i + 1), size=13, bold=True, color=ac_txt[i],
                  align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        b.add_txt(sl, b.M + Inches(0.65), ly + Inches(0.1), CW - Inches(0.72), Inches(0.32),
                  title, size=12, bold=True, color=b.C['fg'], font=b.FB)
        b.add_txt(sl, b.M + Inches(0.65), ly + Inches(0.45), CW - Inches(0.72), Inches(0.32),
                  code, size=10, color=b.C['mfg'], font='Courier New')

    b.pn(sl, 7, 8)
    return sl


# ══════════════════════════════════════════════════════
# S8 — NotebookLM (Split + Pill tags)
# ══════════════════════════════════════════════════════
def slide_s8(prs, b: PptxBuilder):
    sl = b.blank(prs)
    b.set_bg(sl, b.C['bg'])
    LW = Inches(4.5)
    RW = Inches(3.8)
    RX = b.M + LW + Inches(0.3)
    START_Y = Inches(1.0)

    y = b.badge(sl, b.M, START_Y, '지식 자산화', b.C['v'])

    b.add_mixed(sl, b.M, y, LW, Inches(1.3),
        [
            [('Google ', b.C['fg']), ('NotebookLM', b.C['v']), ('으로', b.C['fg'])],
            [('AI 비주얼 전략 비서 구축', b.C['fg'])],
        ], size=22)

    b.add_txt(sl, b.M, y + Inches(1.34), LW, Inches(0.65),
              '습득한 기술을 휘발시키지 않고 개인의 지능형 지식 창고로 구축하는 것이 전문가의 필수 역량입니다.',
              size=13, color=b.C['mfg'], font=b.FB)

    bx = b.M; by = y + Inches(2.12)
    bw = LW;  bh = Inches(0.9)
    b.add_rect(sl, bx, by, bw, bh, fill=b.C['fg'], rounded=True, radius=6)
    b.add_txt(sl, bx + Inches(0.18), by + Inches(0.1), bw, Inches(0.26),
              '궁극의 목표', size=9, bold=True, color=b.C['y'], font=b.FH)
    b.add_txt(sl, bx + Inches(0.18), by + Inches(0.36), bw - Inches(0.3), Inches(0.5),
              '본 매뉴얼의 전략을 체계적으로 적용하여 상업적 경쟁력을 갖춘 독보적인 AI 인플루언서 자산을 구축하세요.',
              size=11, color=b.C['w80'], font=b.FB)

    pill_items = [
        ('5대 전략 완성',    b.C['v'], b.C['w']),
        ('지식 자산화',      b.C['p'], b.C['w']),
        ('상업적 가치 창출', b.C['y'], b.C['fg']),
    ]
    px = b.M; py_tag = by + bh + Inches(0.14)
    for text, bg, tc in pill_items:
        pw_pill = Inches(len(text) * 0.12 + 0.36)
        b.add_rect(sl, px, py_tag, pw_pill, Inches(0.3), fill=bg, rounded=True, radius=50)
        b.add_txt(sl, px, py_tag, pw_pill, Inches(0.3), text, size=11,
                  bold=True, color=tc, align=PP_ALIGN.CENTER, font=b.FB,
                  anchor=MSO_ANCHOR.MIDDLE)
        px += pw_pill + Inches(0.12)

    steps = [
        ('소스 구축 및 업로드',    '전략 매뉴얼·성공 프롬프트 로그·강의 자료를 NotebookLM에 소스로 업로드합니다.'),
        ('지능형 워크플로우 형성', '업로드 소스만 기반으로 답변 — 5대 전략에 충실한 프롬프트를 자동 생성합니다.'),
        ('상황별 자동 생성·확장',  '"테니스 코트 위 모델에 5대 전략 적용해줘" → AI가 자동으로 최적화 프롬프트를 구성합니다.'),
    ]
    sh = Inches(1.45)
    for i, (title, body) in enumerate(steps):
        sy = Inches(0.42) + i * (sh + b.GAP)
        b.card(sl, RX, sy, RW, sh)
        b.add_oval(sl, RX + Inches(0.18), sy + Inches(0.22), Inches(0.36), Inches(0.36), b.C['mute'])
        b.add_txt(sl, RX + Inches(0.18), sy + Inches(0.22), Inches(0.36), Inches(0.36),
                  str(i + 1), size=12, bold=True, color=b.C['mfg'],
                  align=PP_ALIGN.CENTER, font=b.FH, anchor=MSO_ANCHOR.MIDDLE)
        b.add_txt(sl, RX + Inches(0.64), sy + Inches(0.2), RW - Inches(0.74), Inches(0.38),
                  title, size=13, bold=True, color=b.C['fg'], font=b.FB,
                  anchor=MSO_ANCHOR.MIDDLE)
        b.add_txt(sl, RX + Inches(0.18), sy + Inches(0.6), RW - Inches(0.3), Inches(0.78),
                  body, size=11, color=b.C['mfg'], font=b.FB)

    b.pn(sl, 8, 8)
    return sl


# ══════════════════════════════════════════════════════
# 진입점
# ══════════════════════════════════════════════════════

SLIDES = [slide_cover, slide_intro, slide_s3, slide_s4,
          slide_s5, slide_s6, slide_s7, slide_s8]


def build(output: str = 'D:/tmp/slides_v4.pptx', ds: DesignSystem = None):
    """AI 인플루언서 슬라이드 덱을 생성합니다."""
    return build_pptx(SLIDES, output, ds=ds)


if __name__ == '__main__':
    build()
