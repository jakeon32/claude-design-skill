#!/usr/bin/env python3
"""
HTML vs PPTX 비교용 슬라이드 캡처
- HTML: Playwright로 각 슬라이드 스크린샷
- PPTX: python-pptx 파싱 후 PIL로 개략 렌더링 (색상/레이아웃 구조 확인용)
"""
import asyncio, os, json
from pathlib import Path
from playwright.async_api import async_playwright

OUT = Path("D:/tmp/compare")
OUT.mkdir(exist_ok=True)

HTML_PATH = "file:///D:/tmp/preview.html"
TOTAL = 8

async def capture_html():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 720})
        await page.goto(HTML_PATH)
        await page.wait_for_timeout(800)   # fonts load

        for n in range(1, TOTAL + 1):
            path = str(OUT / f"html_s{n:02d}.png")
            await page.screenshot(path=path, clip={"x":0,"y":0,"width":1280,"height":720})
            print(f"HTML S{n} -> {path}")
            # Next slide
            await page.keyboard.press("ArrowRight")
            await page.wait_for_timeout(120)

        await browser.close()

asyncio.run(capture_html())
print("Done.")
