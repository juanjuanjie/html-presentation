"""Local browser smoke test for the static prompt builder (requires Playwright)."""
import functools
import http.server
from pathlib import Path
import threading

from playwright.sync_api import sync_playwright


def main():
    root = Path(__file__).resolve().parents[1]
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as p:
            chrome = Path("C:/Program Files/Google/Chrome/Application/chrome.exe")
            browser = p.chromium.launch(**({"executable_path": str(chrome)} if chrome.exists() else {}))
            page = browser.new_page(viewport={"width": 1440, "height": 1000})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(f"http://127.0.0.1:{server.server_port}/index.html")
            page.locator('[data-appearance="light"]').click()
            assert page.locator("#generation-build").evaluate("e => getComputedStyle(e).backgroundColor") == "rgb(185, 142, 255)"
            assert page.locator('[data-page-link="generator"]').evaluate("e => getComputedStyle(e).color") == "rgb(185, 142, 255)"
            page.locator("#generation-name").fill("测试标题")
            page.locator("#generation-source").fill("Hello，大家好。这是完整逐字稿。")
            page.locator("#generation-build").click()
            page.wait_for_function("!document.querySelector('#generation-copy').disabled")
            prompt = page.locator("#generation-prompt").input_value()
            assert "【演讲 HTML 规则】" in prompt and "<!DOCTYPE" in prompt.upper()
            assert "这是完整逐字稿。" in prompt
            assert page.locator("#templates").is_hidden()
            assert page.locator("#motion").is_hidden()
            assert page.locator("#lab-grid iframe").count() == 0
            page.locator('[data-page-link="templates"]').click()
            page.wait_for_function("!document.querySelector('#templates').hidden")
            assert page.locator("#generator").is_hidden()
            page.locator('[data-page-link="motion"]').click()
            page.wait_for_function("!document.querySelector('#motion').hidden")
            assert page.locator("#lab-grid iframe").count() == 12
            page.locator('[data-page-link="generator"]').click()
            page.wait_for_function("!document.querySelector('#generator').hidden")
            assert page.locator("#generation-prompt").input_value() == prompt
            assert page.locator("#lab-grid iframe").count() == 0
            page.locator('[value="director"]').check()
            assert page.locator("#generation-copy").is_disabled()
            assert page.locator("#director-guide").is_visible()
            page.locator("#director-guide summary").click()
            assert "镜 01｜开场提问" in page.locator("#director-guide").inner_text()
            source = "\n\n".join(f"**镜 {i:02}｜画面**\n> **口播（配音）**：第{i}镜原文。" for i in range(1, 36))
            page.locator("#generation-source").fill(source)
            page.locator("#generation-build").click()
            page.wait_for_function("!document.querySelector('#generation-copy').disabled")
            prompt = page.locator("#generation-prompt").input_value()
            assert "镜头总数：35" in prompt and source in prompt
            assert "renderFrame" in prompt and "【导演 HTML 规则】" in prompt
            page.locator("#generation-source").fill("**镜 01｜开场**\n**镜 03｜结尾**")
            page.locator("#generation-build").click()
            assert page.locator("#generation-copy").is_disabled()
            assert "跳号" in page.locator("#generation-check").inner_text()
            page.set_viewport_size({"width": 390, "height": 844})
            assert page.locator("#generator").evaluate("e => e.getBoundingClientRect().right <= innerWidth")
            assert not errors, errors
            browser.close()
            print("PASS: lecture/director prompts, 35 shots, missing shot rejection, invalidation, mobile bounds, no JS errors")
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
