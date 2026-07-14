"""
레퍼런스를 '검증 도구'로 바꾼다.

Jake: "레퍼런스는 기준을 만들기 위해 수집하는 거야. 검증을 위한 도구이기도 하고."

구경만 하면 레퍼런스가 아니라 구경거리다.
BCG 덱 112장을 **측정해서 기준값(baseline)을 뽑는다.**
그러면 우리 덱을 같은 자로 재서 "레퍼런스 수준인가"를 판정할 수 있다.

측정 항목 (전부 자동):
  ① 텍스트 잉크 밀도    — 페이지에서 글자가 차지하는 면적 비율
  ② 여백 비율          — 아무것도 없는 영역
  ③ 폰트 크기 분포      — 위계가 몇 층인가
  ④ 색 사용 수         — 강조가 분산됐나
  ⑤ 텍스트 블록 수      — 요소가 몇 개인가
"""
import fitz
from collections import Counter
import statistics as st

doc = fitz.open("bcg_nycha.pdf")
print(f"BCG NYCHA — {len(doc)}장 측정\n")

rows = []
for i, page in enumerate(doc):
    W, H = page.rect.width, page.rect.height
    area = W * H

    d = page.get_text("dict")
    sizes, ink, blocks, colors = [], 0.0, 0, set()

    for b in d["blocks"]:
        if b["type"] != 0:
            continue
        blocks += 1
        for line in b["lines"]:
            for sp in line["spans"]:
                sizes.append(round(sp["size"], 1))
                x0, y0, x1, y1 = sp["bbox"]
                ink += (x1 - x0) * (y1 - y0)
                colors.add(sp["color"])

    if not sizes:
        continue

    # 위계 층수 = 유의미하게 다른 폰트 크기의 개수 (1pt 이상 차이나는 것만)
    uniq = sorted(set(sizes), reverse=True)
    tiers, last = [], None
    for s in uniq:
        if last is None or last - s >= 1.0:
            tiers.append(s)
            last = s

    rows.append({
        "page": i + 1,
        "ink_pct": ink / area * 100,          # 텍스트가 덮은 면적 %
        "tiers": len(tiers),                  # 위계 층수
        "max_pt": max(sizes),                 # 제목 크기
        "min_pt": min(sizes),                 # 최소 크기
        "body_pt": st.median(sizes),          # 중앙값 = 본문
        "blocks": blocks,                     # 텍스트 블록 수
        "colors": len(colors),                # 색 종류
    })


def q(key, f=lambda x: x):
    v = sorted(f(r[key]) for r in rows)
    n = len(v)
    return v[n // 4], v[n // 2], v[3 * n // 4]     # Q1 / 중앙값 / Q3


print("=" * 74)
print(f"{'항목':<22}{'Q1':>10}{'중앙값':>12}{'Q3':>10}   해석")
print("-" * 74)

a, b, c = q("ink_pct")
print(f"{'텍스트 잉크 밀도(%)':<20}{a:>10.1f}{b:>12.1f}{c:>10.1f}   페이지에서 글자가 덮은 면적")
a, b, c = q("tiers")
print(f"{'위계 층수':<22}{a:>10}{b:>12}{c:>10}   폰트 크기가 몇 단계인가")
a, b, c = q("max_pt")
print(f"{'제목 크기(pt)':<21}{a:>10.1f}{b:>12.1f}{c:>10.1f}")
a, b, c = q("body_pt")
print(f"{'본문 크기(pt, 중앙)':<19}{a:>10.1f}{b:>12.1f}{c:>10.1f}")
a, b, c = q("min_pt")
print(f"{'최소 크기(pt)':<21}{a:>10.1f}{b:>12.1f}{c:>10.1f}   각주·출처")
a, b, c = q("blocks")
print(f"{'텍스트 블록 수':<21}{a:>10}{b:>12}{c:>10}   요소 개수")
a, b, c = q("colors")
print(f"{'색 종류 수':<22}{a:>10}{b:>12}{c:>10}   강조가 분산됐나")
print("=" * 74)

# 제목/본문 비율 = 위계 대비
ratios = [r["max_pt"] / r["body_pt"] for r in rows if r["body_pt"]]
print(f"\n제목/본문 크기비: 중앙값 {st.median(ratios):.2f}배  "
      f"(Q1 {sorted(ratios)[len(ratios)//4]:.2f} / Q3 {sorted(ratios)[3*len(ratios)//4]:.2f})")

# 밀도 상위/하위 페이지
rows.sort(key=lambda r: r["ink_pct"])
print(f"\n가장 성긴 페이지: {[r['page'] for r in rows[:5]]}  (잉크 {rows[0]['ink_pct']:.1f}%)")
print(f"가장 빽빽한 페이지: {[r['page'] for r in rows[-5:]]}  (잉크 {rows[-1]['ink_pct']:.1f}%)")
