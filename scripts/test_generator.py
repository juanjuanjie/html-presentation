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
            page.set_default_timeout(5000)
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(f"http://127.0.0.1:{server.server_port}/index.html", wait_until="domcontentloaded")
            if page.locator("html").get_attribute("data-appearance") != "light":
                page.locator("#theme-cycle").click()
            assert page.locator("html").get_attribute("data-ui-style") == "doodle"
            assert page.locator("#generation-build").evaluate("e => getComputedStyle(e).backgroundColor") == "rgb(255, 228, 119)"
            assert page.locator('[data-page-link="generator"]').evaluate("e => getComputedStyle(e).color") == "rgb(23, 23, 23)"
            page.locator("#theme-cycle").click()
            assert page.locator("html").get_attribute("data-appearance") == "light"
            assert page.locator("html").get_attribute("data-ui-style") == "current"
            page.locator("#theme-cycle").click()
            assert page.locator("html").get_attribute("data-appearance") == "dark"
            assert page.locator(".icon-moon").is_visible()
            page.locator('[data-page-link="readme"]').click()
            page.wait_for_function("!document.querySelector('#readme').hidden && !document.querySelector('#readme-content').hidden")
            assert page.locator("#readme-content img").count() == 9
            page.locator("#theme-cycle").click()
            assert page.locator("html").get_attribute("data-appearance") == "light"
            assert page.locator("html").get_attribute("data-ui-style") == "doodle"
            assert page.locator(".icon-sun").is_visible()
            page.locator('[data-page-link="generator"]').click()
            page.wait_for_function("!document.querySelector('#generator').hidden")
            assert "HTML" in page.locator("#hero-title").inner_text()
            assert page.locator("#generation-template-button img").count() == 1
            assert page.locator("#presentation-planner").is_visible()
            title_box = page.locator("#generation-name").bounding_box()
            template_box = page.locator("#generation-template-button").bounding_box()
            assert title_box["width"] > 250 and title_box["height"] >= 40
            assert template_box["width"] > 250 and template_box["height"] >= 40
            page.locator("#generation-template-button").click()
            assert page.locator("#generation-template-menu").is_visible()
            assert page.locator("#generation-template-menu img").count() > 3
            page.locator('.generation-template-option[data-template-index="2"]').click()
            assert page.locator("#generation-template").input_value() == "2"
            assert page.locator('.generation-template-option[data-template-index="2"]').get_attribute("aria-selected") == "true"
            assert page.locator("#generation-template-menu").is_hidden()
            page.locator("#generation-name").fill("测试标题")
            page.locator("#generation-source").fill("Hello，大家好。这是完整逐字稿。")
            page.locator("#generation-occasion").select_option("课堂演讲")
            page.locator("#generation-page-count").select_option("6–8 页")
            page.locator("#generation-goal").fill("理解核心方法，并愿意尝试第一步")
            page.locator("#generation-build").click()
            page.wait_for_function("!document.querySelector('#generation-copy').disabled")
            prompt = page.locator("#generation-prompt").input_value()
            assert "【演讲 HTML 规则】" in prompt and "<!DOCTYPE" in prompt.upper()
            assert "这是完整逐字稿。" in prompt
            assert "Story Plan" in prompt
            assert "【字幕与无字幕输出规则】" in prompt
            assert "每个 .slide 内必须有且只有一个 .slide-subtitle" in prompt
            assert "?subtitles=0" in prompt
            assert "window.presentation.setSubtitles" in prompt
            assert "data-subtitle-system" in prompt
            assert "【系列转变页规则】" in prompt
            assert ".transition-slide" in prompt
            assert "后续转变页只允许更换编号、旧状态文字、新状态文字与对应字幕" in prompt
            assert "禁止使用任何默认小人" in prompt
            assert "classic-character.png" not in prompt
            assert "使用场景：课堂演讲" in prompt
            assert "期望页数：6–8 页" in prompt
            assert "理解核心方法，并愿意尝试第一步" in prompt
            assert "不得自动更换或另行匹配风格" in prompt
            page.locator("#generation-template").select_option("0")
            page.locator("#generation-template").dispatch_event("input")
            page.locator("#generation-build").click()
            page.wait_for_function("!document.querySelector('#generation-copy').disabled")
            doodle_prompt = page.locator("#generation-prompt").input_value()
            assert "Doodle Cream 页面背景硬规则（最高优先级）" in doodle_prompt
            assert "#FFFEFB" in doodle_prompt
            assert "不得为了制造节奏而交替使用黄色页" in doodle_prompt
            page.locator("#generation-template").select_option("4")
            page.locator("#generation-template").dispatch_event("input")
            page.locator("#generation-build").click()
            page.wait_for_function("!document.querySelector('#generation-copy').disabled")
            professional_prompt = page.locator("#generation-prompt").input_value()
            assert "Doodle Cream 页面背景硬规则（最高优先级）" not in professional_prompt
            assert "Professional 页面背景硬规则（最高优先级）" not in professional_prompt
            page.locator("#generation-template").select_option("0")
            page.locator("#generation-template").dispatch_event("input")
            page.locator("#generation-character").set_input_files(str(root / "themes/purple-gold-presentation/classic-character.png"))
            page.wait_for_function("document.querySelector('#generation-character-status').textContent.includes('已载入')")
            page.locator("#generation-build").click()
            page.wait_for_function("!document.querySelector('#generation-copy').disabled")
            prompt_with_character = page.locator("#generation-prompt").input_value()
            assert "唯一允许使用的人物素材" in prompt_with_character
            assert "data:image/" in prompt_with_character
            assert "classic-character.png" not in prompt_with_character
            assert page.locator("#templates").is_hidden()
            assert page.locator("#motion").is_hidden()
            assert page.locator("#lab-grid iframe").count() == 0
            page.locator('[data-page-link="templates"]').click()
            page.wait_for_function("!document.querySelector('#templates').hidden")
            page.wait_for_function("!document.querySelector('#preview-modal').hidden")
            assert page.locator("#generator").is_hidden()
            assert page.locator(".template-card").count() == 3
            assert page.locator(".template-use-inline").count() == 3
            assert page.locator('.template-card[data-card-slug="doodle-cream"]').evaluate("e => e.classList.contains('is-designing')")
            assert page.locator(".template-edit-notice").is_visible()
            assert page.locator(".author-line").is_hidden()
            columns = page.locator("#template-grid").evaluate("e => getComputedStyle(e).gridTemplateColumns.split(' ').length")
            assert columns == 3
            palette_trigger = page.locator(".template-card").nth(1).locator(".card-palette-trigger")
            palette_trigger.click()
            assert palette_trigger.get_attribute("aria-expanded") == "true"
            page.locator(".template-card").nth(1).locator(".card-palette-option").first.click()
            page.locator(".template-card").nth(1).locator(".preview").click()
            assert page.locator("#preview-modal").is_visible()
            assert page.locator("#theme-picker .theme-option.active").count() == 1
            modal_columns = page.locator("#preview-modal-body").evaluate("e => getComputedStyle(e).gridTemplateColumns.split(' ').length")
            assert modal_columns == 2
            page.keyboard.press("Escape")
            assert page.locator("#preview-modal").is_hidden()
            page.locator(".template-card").first.locator("[data-use-template]").click()
            page.wait_for_function("!document.querySelector('#generator').hidden")
            assert page.locator("#generation-template-button strong").inner_text() == "Doodle Cream · 白纸暖黄"
            page.locator('[data-page-link="templates"]').click()
            page.wait_for_function("!document.querySelector('#templates').hidden")
            page.locator('[data-page-link="motion"]').click()
            page.wait_for_function("!document.querySelector('#motion').hidden")
            assert page.locator("#lab-grid iframe").count() == 7
            page.locator('[data-page-link="generator"]').click()
            page.wait_for_function("!document.querySelector('#generator').hidden")
            assert page.locator("#generation-prompt").input_value() == ""
            assert page.locator("#generation-copy").is_disabled()
            assert page.locator("#lab-grid iframe").count() == 0
            page.locator('[value="director"]').check()
            assert page.locator("#generation-copy").is_disabled()
            assert page.locator("#director-guide").is_visible()
            assert page.locator("#presentation-planner").is_visible()
            assert page.locator("#presentation-planner .presentation-only:visible").count() == 0
            assert page.locator("#presentation-planner .planner-template").is_visible()
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
