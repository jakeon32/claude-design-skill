#!/usr/bin/env python3
"""
PPTX → PNG 변환 (Windows + PowerPoint COM)

용도: HTML → PPTX 변환 후 시각 회귀 검증을 위해 각 슬라이드를 PNG로 export.
       make_compare.py가 입력으로 사용하는 D:\\tmp\\pptx_check\\v4_s01.png 등을 생성.

전제: Windows + Microsoft PowerPoint 설치 + pywin32.
추후: LibreOffice headless 백엔드도 지원 예정 (현재는 Windows 전용).

사용법:
    python pptx_to_png.py [pptx_path] [out_dir] [prefix]

    기본값:
      pptx_path = D:\\tmp\\slides.pptx
      out_dir   = D:\\tmp\\pptx_check
      prefix    = v4_s
"""
import os
import sys
import platform


def export_pptx_to_png(pptx_path: str, out_dir: str, prefix: str = "v4_s",
                       width: int = 1280, height: int = 720) -> int:
    """
    각 슬라이드를 1280×720 PNG로 export. 성공한 슬라이드 수 반환.

    파일명 패턴: {prefix}{N:02d}.png  (예: v4_s01.png, v4_s02.png ...)
    """
    if platform.system() != "Windows":
        raise RuntimeError(
            "현재 PPTX → PNG는 Windows + PowerPoint COM 전용. "
            "Mac/Linux는 추후 LibreOffice headless 지원 예정."
        )

    try:
        import win32com.client  # type: ignore
    except ImportError as e:
        raise RuntimeError(
            "pywin32 미설치. `pip install pywin32` 후 재실행."
        ) from e

    pptx_path = os.path.abspath(pptx_path)
    out_dir = os.path.abspath(out_dir)
    if not os.path.exists(pptx_path):
        raise FileNotFoundError(f"PPTX 파일 없음: {pptx_path}")
    os.makedirs(out_dir, exist_ok=True)

    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    # PowerPoint COM은 Visible=False를 거부하는 경우가 있어 1로 둠.
    powerpoint.Visible = 1

    count = 0
    presentation = powerpoint.Presentations.Open(pptx_path, WithWindow=False)
    try:
        for i, slide in enumerate(presentation.Slides, start=1):
            out_path = os.path.join(out_dir, f"{prefix}{i:02d}.png")
            slide.Export(out_path, "PNG", width, height)
            print(f"S{i} -> {out_path}")
            count += 1
    finally:
        presentation.Close()
        powerpoint.Quit()

    return count


if __name__ == "__main__":
    pptx_path = sys.argv[1] if len(sys.argv) > 1 else r"D:\tmp\slides.pptx"
    out_dir   = sys.argv[2] if len(sys.argv) > 2 else r"D:\tmp\pptx_check"
    prefix    = sys.argv[3] if len(sys.argv) > 3 else "v4_s"

    n = export_pptx_to_png(pptx_path, out_dir, prefix)
    print(f"Done. {n} slide(s) exported to {out_dir}")
