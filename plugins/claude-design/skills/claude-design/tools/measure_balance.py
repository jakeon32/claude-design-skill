"""
measure_balance.py — 시각 밸런스를 측정한다.

─ 왜 필요한가 ────────────────────────────────────────────────
Jake: "밀도를 올리는 것보다 중요한 것이 밸런스입니다."

measure_density.py 만 있으면 위험하다.
"12% 미만 = 비어 있음" 이라고만 알려주면 AI는 **밀도를 올리려고 아무거나 채운다.**
30%를 채웠어도 한쪽에 몰려 있으면 더 나쁘다.

    밀도 15%인데 균형 잡힌 화면  >  밀도 35%인데 한쪽에 쏠린 화면

**밀도는 목표가 아니라 진단 지표다. 밸런스가 먼저다.**
밀도가 낮으면 "채워라"가 아니라 "왜 낮은가"를 본다:
  · 요소가 아예 없나?   → 색면 · 이미지 · 도해를 넣는다
  · 한쪽만 채웠나?      → 밀도가 아니라 **배치**를 고친다
──────────────────────────────────────────────────────────────

측정:
  ① 무게중심(centroid)  — 잉크의 무게중심이 화면 중앙에서 얼마나 벗어났나
  ② 4분면 분포          — 좌상/우상/좌하/우하에 얼마씩
  ③ 좌우·상하 편차      — 한쪽이 다른 쪽의 몇 배인가
  ④ 최대 공백 영역      — 아무것도 없는 가장 큰 사각형 (구멍)

사용:
    python measure_balance.py slide.png [slide2.png ...]
"""
import sys
import os
from collections import Counter

try:
    from PIL import Image
except ImportError:
    sys.exit("PIL 필요")

# ── 🔴 슬라이드 유형이 밸런스 기준을 정한다 ────────────────
#
# 초판은 모든 슬라이드를 같은 잣대로 쟀고, 그래서 **실제 제안서 표지를
# "우측 과중, 배치를 고쳐라"로 오판했다.** 그 표지는 좌 색면 + 우 인물사진으로,
# 비대칭이 **의도이자 강점**이었다.
#
#   기계적 균형 ≠ 좋은 디자인.
#   표지는 비대칭이 강하고, 본문은 균형이 옳다.
#
# 유형을 지정하지 않으면 'body'로 본다.
PROFILES = {
    # 표지·간지 — 강한 대비가 목적. 비대칭 허용
    "cover":   {"centroid": 26.0, "lr": 5.0, "tb": 3.0, "quad": 12.0},
    # 좌우 대비 구조 (Before/After, 대비 관계) — 대칭이 정상
    "compare": {"centroid": 6.0,  "lr": 1.4, "tb": 2.2, "quad": 3.0},
    # 일반 본문 — 균형이 정상
    "body":    {"centroid": 10.0, "lr": 2.0, "tb": 2.4, "quad": 3.5},
    # 풀블리드 이미지 — 밀도·밸런스 판정 대상 아님
    "bleed":   {"centroid": 50.0, "lr": 99.0, "tb": 99.0, "quad": 99.0},
}


def analyze(path: str) -> dict:
    im = Image.open(path).convert("L")
    im.thumbnail((640, 640), Image.LANCZOS)
    px = im.load()
    w, h = im.size

    # 배경색 자동 판별
    hist = Counter()
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            hist[px[x, y] // 8] += 1
    bg = hist.most_common(1)[0][0] * 8

    ink = []                       # (x, y, weight)
    total = 0.0
    for y in range(h):
        for x in range(w):
            d = abs(px[x, y] - bg)
            if d > 28:
                wgt = d / 255.0    # 대비가 클수록 시각 무게가 크다
                ink.append((x, y, wgt))
                total += wgt

    if not total:
        return {"empty": True}

    # ① 무게중심 (%)
    cx = sum(x * wgt for x, _, wgt in ink) / total / w * 100
    cy = sum(y * wgt for _, y, wgt in ink) / total / h * 100

    # ② 4분면 분포 (%)
    quads = {"좌상": 0.0, "우상": 0.0, "좌하": 0.0, "우하": 0.0}
    for x, y, wgt in ink:
        k = ("좌" if x < w / 2 else "우") + ("상" if y < h / 2 else "하")
        quads[k] += wgt
    quads = {k: v / total * 100 for k, v in quads.items()}

    # ③ 좌우 / 상하 무게비
    left = quads["좌상"] + quads["좌하"]
    right = quads["우상"] + quads["우하"]
    top = quads["좌상"] + quads["우상"]
    bottom = quads["좌하"] + quads["우하"]
    lr = max(left, right) / max(1e-6, min(left, right))
    tb = max(top, bottom) / max(1e-6, min(top, bottom))

    # ④ 밀도
    density = len(ink) / (w * h) * 100

    return {
        "empty": False,
        "density": density,
        "cx": cx, "cy": cy,
        "quads": quads,
        "left": left, "right": right, "top": top, "bottom": bottom,
        "lr": lr, "tb": tb,
    }


def verdict(a: dict, kind: str = "body") -> list:
    """무엇을 고쳐야 하는지 구체적으로. 유형(kind)에 따라 잣대가 다르다."""
    out = []
    if a["empty"]:
        return ["🔴 콘텐츠 없음"]

    P = PROFILES.get(kind, PROFILES["body"])

    # ── 밸런스 먼저 (밀도보다 우선) ──
    dx = a["cx"] - 50
    if abs(dx) > P["centroid"]:
        side = "좌측" if dx < 0 else "우측"
        other = "우측" if dx < 0 else "좌측"
        out.append(f"🔴 무게가 {side}으로 {abs(dx):.0f}%p 쏠림 → {other}이 비었다. 배치를 고친다")
    if a["lr"] > P["lr"]:
        heavy = "좌" if a["left"] > a["right"] else "우"
        out.append(f"🔴 좌우 무게비 {a['lr']:.1f}배 ({heavy}측 과중) → 대칭·앵커 요소 검토")
    if a["tb"] > P["tb"]:
        heavy = "상" if a["top"] > a["bottom"] else "하"
        out.append(f"🟡 상하 무게비 {a['tb']:.1f}배 ({heavy}단 과중)")

    qv = list(a["quads"].values())
    if min(qv) > 0 and max(qv) / min(qv) > P["quad"]:
        lo = min(a["quads"], key=a["quads"].get)
        out.append(f"🟡 4분면 편차 {max(qv)/min(qv):.1f}배 → {lo} 사분면이 비었다")

    # ── 밀도는 밸런스 다음. 그리고 "채워라"가 아니다 ──
    d = a["density"]
    if kind != "bleed":
        if d < 12:
            out.append(
                f"🔴 밀도 {d:.1f}% (레퍼런스 24.9%의 {d/24.9*100:.0f}%)\n"
                f"        → ⚠️ 채우는 것이 목적이 되면 안 된다. 왜 낮은지 먼저 물어라:\n"
                f"           ① 내용이 부족한가?      → 보강하거나 슬라이드를 합친다\n"
                f"           ② 시각화가 없나?        → 도해·차트로 구조화한다\n"
                f"           ③ 화면을 못 쓰고 있나?  → 요소를 키운다 · 색면 · 이미지\n"
                f"           넣는 것마다: 결론을 증명하는가? 내용과 시너지를 내는가?\n"
                f"           아니면 넣지 마라 (장식은 이해를 떨어뜨린다)"
            )
        elif d < 16:
            out.append(f"🟡 밀도 {d:.1f}% — 다소 성김 (의도라면 무시)")
        elif d > 55:
            out.append(f"🟡 밀도 {d:.1f}% — 과밀. 삭제·분할 검토")

    if not out:
        out.append(f"✅ 밸런스·밀도 적정 ({kind})")
    return out


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        print("유형: --cover | --compare | --body(기본) | --bleed")
        sys.exit(1)

    kind = "body"
    files = []
    for a in args:
        if a.startswith("--"):
            k = a[2:]
            if k in PROFILES:
                kind = k
        else:
            files.append(a)

    for t in files:
        a = analyze(t)
        print()
        print("=" * 68)
        print(f"  {os.path.basename(t)}   [유형: {kind}]")
        print("-" * 68)
        if a["empty"]:
            print("  콘텐츠 없음")
            continue
        print(f"  밀도        {a['density']:5.1f}%")
        print(f"  무게중심    ({a['cx']:.0f}%, {a['cy']:.0f}%)   [중앙 = 50%, 50%]")
        print(f"  4분면       좌상 {a['quads']['좌상']:4.0f}%  우상 {a['quads']['우상']:4.0f}%")
        print(f"              좌하 {a['quads']['좌하']:4.0f}%  우하 {a['quads']['우하']:4.0f}%")
        print(f"  좌우        {a['left']:.0f}% : {a['right']:.0f}%   (비율 {a['lr']:.1f})")
        print(f"  상하        {a['top']:.0f}% : {a['bottom']:.0f}%   (비율 {a['tb']:.1f})")
        print("-" * 68)
        for v in verdict(a, kind):
            print(f"  {v}")
    print("=" * 68)
    print()
    print("  ⚠️ 밀도는 목표가 아니라 진단 지표다. 밸런스가 먼저다.")
    print("     밀도 15% + 균형  >  밀도 35% + 쏠림")
    print()
    print("  ⚠️ 채우는 것이 목적이 되면 안 된다.")
    print("     더할 때는 이유가 있어야 하고, 내용과 어우러져 시너지를 내야 한다.")
    print()
    print("  ⚠️ 유형을 지정하라. 표지는 비대칭이 강하고, 본문은 균형이 옳다.")
    print("     --cover  표지·간지 (비대칭 허용)")
    print("     --compare 좌우 대비 (대칭 요구)")
    print("     --body   일반 본문 (기본)")
    print("     --bleed  풀블리드 이미지 (판정 제외)")
    print()


if __name__ == "__main__":
    main()
