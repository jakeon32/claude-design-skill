"""
measure_density.py — 슬라이드의 '콘텐츠 밀도'를 재고 레퍼런스와 비교한다.

─ 왜 필요한가 ────────────────────────────────────────────────
Jake: "레퍼런스는 기준을 만들기 위해 수집하는 거야. 검증을 위한 도구이기도 하고."

레퍼런스를 구경만 하면 구경거리다. **측정해서 기준값을 뽑아야** 검증 도구가 된다.

2026-07-14 실측 — 같은 자로 잰 결과:

    슬라이드 레퍼런스 101종   중앙값 24.9%  (Q1 16.2 / Q3 37.1)
    실제 제안서 덱 표지        30.4%
    실제 제안서 덱 카드         13~15%
    ─────────────────────────────────────
    우리가 만든 덱             3.0 ~ 4.5%   ← 레퍼런스의 1/6

**우리 눈에는 "깔끔하다"였는데, 자로 재니 레퍼런스의 1/6이었다.**
감으로는 절대 못 잡는다. 이것이 "스샷 같다"는 지적의 정체였다.

밀도를 올리는 방법은 **글자를 더 넣는 것이 아니다**:
  · 색면 (배경 블록 · 강조 영역)
  · 이미지 · 사진
  · 도형 · 도해
  · 요소를 키우기 (숫자 · 제목)
──────────────────────────────────────────────────────────────

사용:
    python measure_density.py slide.png [slide2.png ...]
    python measure_density.py deck.pdf
"""
import sys
import os
from collections import Counter

try:
    from PIL import Image
except ImportError:
    sys.exit("PIL 필요: pip install pillow")

# ── 기준값 (2026-07-14 실측) ────────────────────────────────
BASELINE = {
    "slide_ref_q1":     16.2,   # 슬라이드 레퍼런스 101종 Q1
    "slide_ref_median": 24.9,   # 중앙값 ← 목표
    "slide_ref_q3":     37.1,   # Q3
}
FLOOR = 12.0    # 이 밑이면 "비어 있다"
CEIL  = 55.0    # 이 위면 "과밀"


def content_ratio(path: str) -> float:
    """비배경 픽셀 비율(%). 텍스트·도형·이미지를 모두 콘텐츠로 센다."""
    im = Image.open(path).convert("L")
    im.thumbnail((900, 900), Image.LANCZOS)
    px = im.load()
    w, h = im.size

    # 배경색 = 최빈값 (흰 배경이든 다크 배경이든 자동 판별)
    hist = Counter()
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            hist[px[x, y] // 8] += 1
    bg = hist.most_common(1)[0][0] * 8

    cnt = tot = 0
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            tot += 1
            if abs(px[x, y] - bg) > 28:      # 배경과 충분히 다르면 콘텐츠
                cnt += 1
    return cnt / tot * 100


def verdict(r: float) -> str:
    if r < FLOOR:
        return f"🔴 비어 있음 (레퍼런스 중앙값 {BASELINE['slide_ref_median']}%의 {r/BASELINE['slide_ref_median']*100:.0f}%)"
    if r > CEIL:
        return "🟡 과밀 — 삭제·분할 검토"
    if r < BASELINE["slide_ref_q1"]:
        return "🟡 성김 — 색면·이미지·도해 투입 검토"
    return "✅ 적정"


def pdf_pages(path: str):
    import fitz
    doc = fitz.open(path)
    tmp = []
    for i, page in enumerate(doc):
        p = f"_dens_{i+1:03d}.png"
        page.get_pixmap(dpi=70).save(p)
        tmp.append(p)
    return tmp


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    targets, cleanup = [], []
    for a in args:
        if a.lower().endswith(".pdf"):
            ps = pdf_pages(a)
            targets += ps
            cleanup += ps
        else:
            targets.append(a)

    print()
    print("콘텐츠 밀도 측정 (비배경 픽셀 %)")
    print("=" * 66)
    print(f"기준: 레퍼런스 101종 중앙값 {BASELINE['slide_ref_median']}% "
          f"(Q1 {BASELINE['slide_ref_q1']} / Q3 {BASELINE['slide_ref_q3']})")
    print(f"목표 구간 {FLOOR}~{CEIL}%")
    print("-" * 66)

    vals = []
    for t in targets:
        try:
            r = content_ratio(t)
            vals.append(r)
            print(f"  {os.path.basename(t):<34}{r:5.1f}%   {verdict(r)}")
        except Exception as e:
            print(f"  {os.path.basename(t):<34}  ERROR {e}")

    if vals:
        vs = sorted(vals)
        med = vs[len(vs) // 2]
        print("-" * 66)
        print(f"  {'중앙값':<34}{med:5.1f}%   {verdict(med)}")
        gap = med / BASELINE["slide_ref_median"]
        print(f"  레퍼런스 대비: {gap*100:.0f}%")
    print("=" * 66)

    for f in cleanup:
        try:
            os.remove(f)
        except OSError:
            pass


if __name__ == "__main__":
    main()
