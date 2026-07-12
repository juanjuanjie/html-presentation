from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright


DEFAULT_SELECTOR = ".slide"
DEFAULT_HIDDEN_SELECTORS = [".controls", ".dots", ".progress", ".hint", ".nav-controls", ".nav-btn", ".nav-arrows", ".nav-dots", ".slide-counter", ".keyboard-hint"]
DEFAULT_VIEWPORT_WIDTH = 1920
DEFAULT_VIEWPORT_HEIGHT = 1080
DEFAULT_DEVICE_SCALE = 2
TARGET_ASPECT_RATIO = 16 / 9
MODES = ("standard", "balanced", "compact", "auto")
CONTENT_SCALE_PRESETS = {
    "1.0x": 1.0,
    "1.5x": 1.5,
    "1.6x": 1.6,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capture each slide in an HTML presentation as a 16:9 PNG image."
    )
    parser.add_argument(
        "html_path",
        nargs="?",
        default="",
        help="Path to the HTML presentation file. If omitted, the script looks for youmind-rss-presentation (5).html beside the script.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="slides_out",
        help="Directory to save PNG screenshots.",
    )
    parser.add_argument(
        "-s",
        "--selector",
        default=DEFAULT_SELECTOR,
        help="CSS selector for slide elements.",
    )
    parser.add_argument(
        "-W",
        "--viewport-width",
        type=int,
        default=DEFAULT_VIEWPORT_WIDTH,
        help="Viewport width in pixels.",
    )
    parser.add_argument(
        "-H",
        "--viewport-height",
        type=int,
        default=DEFAULT_VIEWPORT_HEIGHT,
        help="Viewport height in pixels.",
    )
    parser.add_argument(
        "--prefix",
        default="page",
        help="Output filename prefix.",
    )
    parser.add_argument(
        "--wait",
        type=int,
        default=1000,
        help="Initial wait time in milliseconds after load.",
    )
    parser.add_argument(
        "--transition-wait",
        type=int,
        default=650,
        help="Wait time in milliseconds after switching slides.",
    )
    parser.add_argument(
        "--device-scale",
        type=int,
        default=DEFAULT_DEVICE_SCALE,
        help="Device pixel ratio for sharper screenshots.",
    )
    parser.add_argument(
        "--content-scale-preset",
        choices=CONTENT_SCALE_PRESETS.keys(),
        default=None,
        help="Quick content scale preset.",
    )
    parser.add_argument(
        "--content-scale",
        type=float,
        default=0.0,
        help="Custom content scale factor. If set to a positive number, it overrides the preset.",
    )
    parser.add_argument(
        "--mode",
        choices=MODES,
        default="standard",
        help="Screenshot mode: standard keeps a full 16:9 canvas; balanced crops around content but keeps 16:9; compact crops tightly around content; auto picks balanced or compact based on content density.",
    )
    parser.add_argument(
        "--hide-selectors",
        nargs="*",
        default=DEFAULT_HIDDEN_SELECTORS,
        help="Space-separated list of CSS selectors to hide.",
    )
    return parser.parse_args()


def choose_content_scale_preset(default_preset: str | None) -> str:
    if default_preset in CONTENT_SCALE_PRESETS:
        return default_preset

    # Default to no extra scaling. Project templates already enlarge content
    # via .content-wrapper { transform: scale(1.5); }, so applying an extra
    # zoom here would double-scale and clip the slide edges.
    if not sys.stdin.isatty():
        return "1.0x"

    print("Choose content scale:")
    print("  1) 1.0x (no extra scaling, recommended for built-in scaled templates)")
    print("  2) 1.5x")
    print("  3) 1.6x")

    while True:
        choice = input("Enter 1, 2 or 3 [1]: ").strip()
        if choice in ("", "1"):
            return "1.0x"
        if choice == "2":
            return "1.5x"
        if choice == "3":
            return "1.6x"
        print("Please enter 1, 2 or 3.")


def resolve_html_path(raw_value: str) -> Path:
    if raw_value:
        return Path(raw_value)

    project_root = Path(__file__).resolve().parent.parent
    preferred = project_root / "workspace-series-ep01.html"
    if preferred.exists():
        return preferred

    candidates = sorted(project_root.glob("*.html"), key=lambda item: item.stat().st_mtime, reverse=True)
    if candidates:
        return candidates[0]

    raise FileNotFoundError(
        "No HTML file was provided and no .html file was found beside the script."
    )


def to_file_url(html_path: Path) -> str:
    return html_path.resolve().as_uri()


async def capture_slides(args: argparse.Namespace) -> None:
    html_path = resolve_html_path(args.html_path)
    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    file_url = to_file_url(html_path)
    selected_preset = choose_content_scale_preset(args.content_scale_preset)
    content_scale = args.content_scale if args.content_scale and args.content_scale > 0 else CONTENT_SCALE_PRESETS[selected_preset]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(
            viewport={"width": args.viewport_width, "height": args.viewport_height},
            device_scale_factor=args.device_scale,
        )
        await page.goto(file_url, wait_until="networkidle")
        await page.wait_for_timeout(args.wait)

        if args.hide_selectors:
            css = ", ".join(args.hide_selectors)
            await page.add_style_tag(content=f"{css} {{ display: none !important; }}")

        await page.add_script_tag(
            content="""
            () => {
              document.querySelectorAll('deck-stage').forEach((ds) => {
                if (ds.shadowRoot) {
                  const overlay = ds.shadowRoot.querySelector('.overlay');
                  if (overlay) overlay.style.display = 'none';
                }
              });
            }
            """
        )

        await page.add_style_tag(
            content="""
            * {
              transition: none !important;
            }
            .anim,
            .anim * {
              opacity: 1 !important;
              animation: none !important;
              transform: none !important;
            }
            """
        )
        if content_scale != 1:
            await page.add_style_tag(
                content=f"""
                .slide.active {{
                  zoom: {content_scale};
                }}
                """
            )

        slides = page.locator(args.selector)
        total = await slides.count()
        if total == 0:
            await browser.close()
            raise RuntimeError(f"No slides found with selector: {args.selector}")

        async def show_slide(index: int) -> None:
            await page.evaluate(
                """
                ({ index, total }) => {
                  const slides = Array.from(document.querySelectorAll('.slide'));
                  const dots = Array.from(document.querySelectorAll('.dot'));
                  const counter = document.getElementById('counter');
                  const prevBtn = document.getElementById('prev');
                  const nextBtn = document.getElementById('next');

                  if (!slides.length || index < 0 || index >= total) {
                    return;
                  }

                  slides.forEach((slide, i) => {
                    slide.classList.toggle('active', i === index);
                    if (i === index) {
                      slide.setAttribute('data-deck-active', '');
                    } else {
                      slide.removeAttribute('data-deck-active');
                    }
                  });
                  dots.forEach((dot, i) => dot.classList.toggle('active', i === index));

                  if (counter) {
                    counter.textContent = `${index + 1} / ${total}`;
                  }
                  if (prevBtn) {
                    prevBtn.disabled = index === 0;
                  }
                  if (nextBtn) {
                    nextBtn.disabled = index === total - 1;
                  }
                }
                """,
                {"index": index, "total": total},
            )

        async def get_compact_clip() -> dict[str, float]:
            return await page.evaluate(
                """
                () => {
                  const active = document.querySelector('.slide.active');
                  if (!active) {
                    return null;
                  }

                  const viewportWidth = window.innerWidth;
                  const viewportHeight = window.innerHeight;
                  const rects = [];

                  const collect = (el) => {
                    if (!el) return;
                    const style = window.getComputedStyle(el);
                    if (style.display === 'none' || style.visibility === 'hidden' || parseFloat(style.opacity || '1') === 0) {
                      return;
                    }
                    const rect = el.getBoundingClientRect();
                    if (rect.width <= 0 || rect.height <= 0) {
                      return;
                    }
                    rects.push(rect);
                  };

                  active.querySelectorAll('*').forEach(collect);

                  if (!rects.length) {
                    const fallback = active.getBoundingClientRect();
                    return {
                      x: Math.max(0, fallback.left),
                      y: Math.max(0, fallback.top),
                      width: Math.max(1, fallback.width),
                      height: Math.max(1, fallback.height),
                    };
                  }

                  let left = Math.min(...rects.map(r => r.left));
                  let top = Math.min(...rects.map(r => r.top));
                  let right = Math.max(...rects.map(r => r.right));
                  let bottom = Math.max(...rects.map(r => r.bottom));

                  const paddingX = 24;
                  const paddingY = 20;
                  left -= paddingX;
                  top -= paddingY;
                  right += paddingX;
                  bottom += paddingY;

                  if (left < 0) {
                    right -= left;
                    left = 0;
                  }
                  if (top < 0) {
                    bottom -= top;
                    top = 0;
                  }
                  if (right > viewportWidth) {
                    const overflow = right - viewportWidth;
                    left = Math.max(0, left - overflow);
                    right = viewportWidth;
                  }
                  if (bottom > viewportHeight) {
                    const overflow = bottom - viewportHeight;
                    top = Math.max(0, top - overflow);
                    bottom = viewportHeight;
                  }

                  return {
                    x: Math.max(0, left),
                    y: Math.max(0, top),
                    width: Math.max(1, right - left),
                    height: Math.max(1, bottom - top),
                  };
                }
                """,
                {},
            )

        async def get_balanced_clip() -> dict[str, float]:
            return await page.evaluate(
                """
                ({ targetRatio }) => {
                  const active = document.querySelector('.slide.active');
                  if (!active) {
                    return null;
                  }

                  const viewportWidth = window.innerWidth;
                  const viewportHeight = window.innerHeight;
                  const rects = [];

                  const collect = (el) => {
                    if (!el) return;
                    const style = window.getComputedStyle(el);
                    if (style.display === 'none' || style.visibility === 'hidden' || parseFloat(style.opacity || '1') === 0) {
                      return;
                    }
                    const rect = el.getBoundingClientRect();
                    if (rect.width <= 0 || rect.height <= 0) {
                      return;
                    }
                    rects.push(rect);
                  };

                  active.querySelectorAll('*').forEach(collect);

                  if (!rects.length) {
                    const fallback = active.getBoundingClientRect();
                    return {
                      x: Math.max(0, fallback.left),
                      y: Math.max(0, fallback.top),
                      width: Math.max(1, fallback.width),
                      height: Math.max(1, fallback.height),
                    };
                  }

                  let left = Math.min(...rects.map(r => r.left));
                  let top = Math.min(...rects.map(r => r.top));
                  let right = Math.max(...rects.map(r => r.right));
                  let bottom = Math.max(...rects.map(r => r.bottom));

                  const paddingX = 48;
                  const paddingY = 32;
                  left -= paddingX;
                  top -= paddingY;
                  right += paddingX;
                  bottom += paddingY;

                  let width = right - left;
                  let height = bottom - top;
                  const currentRatio = width / height;
                  const centerX = left + width / 2;
                  const centerY = top + height / 2;

                  if (Math.abs(currentRatio - targetRatio) > 0.01) {
                    if (currentRatio > targetRatio) {
                      height = width / targetRatio;
                    } else {
                      width = height * targetRatio;
                    }
                  }

                  left = centerX - width / 2;
                  top = centerY - height / 2;
                  right = left + width;
                  bottom = top + height;

                  if (left < 0) {
                    right -= left;
                    left = 0;
                  }
                  if (top < 0) {
                    bottom -= top;
                    top = 0;
                  }
                  if (right > viewportWidth) {
                    const overflow = right - viewportWidth;
                    left = Math.max(0, left - overflow);
                    right = viewportWidth;
                  }
                  if (bottom > viewportHeight) {
                    const overflow = bottom - viewportHeight;
                    top = Math.max(0, top - overflow);
                    bottom = viewportHeight;
                  }

                  return {
                    x: Math.max(0, left),
                    y: Math.max(0, top),
                    width: Math.max(1, right - left),
                    height: Math.max(1, bottom - top),
                  };
                }
                """,
                {"targetRatio": TARGET_ASPECT_RATIO},
            )

        async def save_slide(index: int) -> None:
            filename = output_dir / f"{args.prefix}_{index + 1:02d}.png"
            if args.mode == "compact":
                clip = await get_compact_clip()
                await page.screenshot(path=str(filename), clip=clip, scale="device")
            elif args.mode == "balanced":
                clip = await get_balanced_clip()
                await page.screenshot(path=str(filename), clip=clip, scale="device")
            elif args.mode == "auto":
                compact_clip = await get_compact_clip()
                viewport_area = args.viewport_width * args.viewport_height
                compact_area = compact_clip["width"] * compact_clip["height"]
                density = compact_area / viewport_area if viewport_area else 1.0
                if density < 0.62:
                    await page.screenshot(path=str(filename), clip=compact_clip, scale="device")
                else:
                    clip = await get_balanced_clip()
                    await page.screenshot(path=str(filename), clip=clip, scale="device")
            else:
                await page.screenshot(path=str(filename), full_page=False, scale="device")

        await show_slide(0)
        await page.wait_for_timeout(args.transition_wait)
        await save_slide(0)

        for index in range(1, total):
            await show_slide(index)
            await page.wait_for_timeout(args.transition_wait)
            await save_slide(index)

        await browser.close()


def main() -> None:
    args = parse_args()
    asyncio.run(capture_slides(args))


if __name__ == "__main__":
    main()
