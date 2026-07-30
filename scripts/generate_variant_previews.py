#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_variant_previews.py
为同一模板的不同配色变量生成封面预览图。

用法示例：
    python scripts/generate_variant_previews.py
"""

import asyncio
import json
import sys
from pathlib import Path
from urllib.parse import quote

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
PREVIEWS_DIR = ROOT / "assets" / "previews"

# 定义需要生成的配色变体。
# 每个条目指定模板文件、输出文件名、以及要注入的 CSS 变量。
VARIANTS = [
    {
        "template": "themes/blockframe/template.html",
        "output": "blockframe-retro-paper.png",
        "vars": {
            "offwhite": "#F6E7C8",
            "black": "#1F1714",
            "white": "#FFF8EA",
            "pink": "#D94F7B",
            "blue": "#2B6CB0",
            "green": "#3E8F5B",
            "yellow": "#E9B949",
            "cream": "#F0C987",
        },
    },
    {
        "template": "themes/blockframe/template.html",
        "output": "blockframe-mono-pop.png",
        "vars": {
            "offwhite": "#FFFFFF",
            "black": "#000000",
            "white": "#FFFFFF",
            "pink": "#FFE45C",
            "blue": "#A8FF3E",
            "green": "#A8FF3E",
            "yellow": "#FFE45C",
            "cream": "#FFFFFF",
        },
    },
    {
        "template": "themes/apple-bento-grid/template.html",
        "output": "apple-bento-grid-dark-green.png",
        "vars": {
            "bg": "#0A0A0A",
            "surface": "#141414",
            "surface-strong": "#1C1C1E",
            "text": "#F5F5F7",
            "muted": "#86868B",
            "line": "#2C2C2E",
            "dark": "#000000",
            "white": "#FFFFFF",
            "blue": "#a8ff3e",
            "green": "#7ee02d",
            "orange": "#c8ff66",
            "purple": "#5cb816",
            "lavender": "#1A1A1A",
        },
    },
]

VIEWPORT_WIDTH = 1920
VIEWPORT_HEIGHT = 1080
DEVICE_SCALE = 1
WAIT_MS = 1200
TRANSITION_WAIT_MS = 300


def safe_print(msg):
    encoded = (msg + "\n").encode(sys.stdout.encoding, errors="replace")
    sys.stdout.buffer.write(encoded)


async def generate():
    PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(
            viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT},
            device_scale_factor=DEVICE_SCALE,
        )

        for variant in VARIANTS:
            template_path = ROOT / variant["template"]
            if not template_path.exists():
                safe_print(f"[!] 跳过，模板不存在: {template_path}")
                continue

            output_path = PREVIEWS_DIR / variant["output"]
            file_url = template_path.resolve().as_uri()
            encoded_vars = quote(json.dumps(variant["vars"]))
            url = f"{file_url}?vars={encoded_vars}"

            safe_print(f"[...] 生成 {output_path.name}")
            await page.goto(url, wait_until="networkidle")
            await page.wait_for_timeout(WAIT_MS)

            # 隐藏导航控件，确保画面干净
            hide_selectors = [
                ".controls",
                ".dots",
                ".progress",
                ".hint",
                ".nav-controls",
                ".nav-btn",
                ".nav-arrows",
                ".nav-dots",
                ".slide-counter",
                ".keyboard-hint",
                ".theme-switcher",
            ]
            css = ", ".join(hide_selectors)
            await page.add_style_tag(content=f"{css} {{ display: none !important; }}")

            # 只显示第一张 slide
            await page.evaluate(
                """
                () => {
                  const slides = Array.from(document.querySelectorAll('.slide'));
                  slides.forEach((slide, i) => {
                    slide.classList.toggle('active', i === 0);
                    slide.style.display = i === 0 ? '' : 'none';
                  });
                }
                """
            )
            await page.wait_for_timeout(TRANSITION_WAIT_MS)

            # 截图第一张 slide 的边界
            clip = await page.evaluate(
                """
                () => {
                  const slide = document.querySelector('.slide.active') || document.querySelector('.slide');
                  if (!slide) return null;
                  const rect = slide.getBoundingClientRect();
                  return { x: rect.x, y: rect.y, width: rect.width, height: rect.height };
                }
                """
            )
            if not clip:
                safe_print(f"[!] 未找到 .slide: {output_path.name}")
                continue

            await page.screenshot(path=str(output_path), clip=clip, scale="device")
            safe_print(f"[OK] {output_path.name} ({int(clip['width'])}x{int(clip['height'])})")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(generate())
