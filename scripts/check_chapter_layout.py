"""Browser regression check for chapter and existing transition layouts."""
from pathlib import Path
import functools
import http.server
import threading
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[1]
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(root)))
threading.Thread(target=server.serve_forever,daemon=True).start()
try:
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='C:/Program Files/Google/Chrome/Application/chrome.exe')
        page = browser.new_page(viewport={'width':1920,'height':1080})
        page.route('https://fonts.googleapis.com/**',lambda route: route.abort())
        for template in (root/'themes').glob('*/template.html'):
            page.goto(f'http://127.0.0.1:{server.server_port}/themes/{template.parent.name}/template.html',wait_until='domcontentloaded')
            for _ in range(page.locator('.slide').count()-2):
                page.keyboard.press('ArrowRight')
                page.wait_for_timeout(100)
            page.wait_for_timeout(600)
            assert page.locator('.chapter-slide.active').count() == 1, template
            if template.parent.name.startswith(('doodle','blockframe')):
                assert page.locator('[data-transition-series]').count() > 0, template
            if template.parent.name.startswith('doodle-cream'):
                assert page.locator('.chapter-track').count() == 0
                assert page.locator('.chapter-number').inner_text() == '01'
                assert page.locator('.chapter-title .highlight').count() == 1
            else:
                assert page.locator('.chapter-track [aria-current="step"]').count() == 1
            if template.parent.name == 'doodle-cream-dark':
                assert page.locator('.chapter-number').evaluate('(el)=>getComputedStyle(el).color') == 'rgb(33, 27, 13)'
                page.screenshot(path=str(root/'assets/previews/chapter-layout-dark.png'))
            for width,height in [(1920,1080),(390,844)]:
                page.set_viewport_size({'width':width,'height':height})
                assert page.locator('.chapter-title,.chapter-description,.chapter-track').evaluate_all('(els)=>els.every(e=>{const r=e.getBoundingClientRect();return r.left>=0&&r.right<=innerWidth+1&&r.bottom<=innerHeight})'),template
            page.set_viewport_size({'width':1920,'height':1080})
            if template.parent.name == 'doodle-cream':
                page.screenshot(path=str(root/'assets/previews/chapter-layout.png'))
        page.goto(f'http://127.0.0.1:{server.server_port}/index.html',wait_until='domcontentloaded')
        page.locator('[data-page-link="templates"]').click()
        page.locator('[data-preview-page="chapter"]').click()
        page.wait_for_timeout(500)
        assert page.frame_locator('#preview-iframe').locator('.chapter-slide.active').count() == 1
        assert page.locator('[data-preview-page="transition"]').count() == 1
        browser.close()
        print('PASS: all six themes, chapter navigation, original transitions, desktop/mobile bounds')
finally:
    server.shutdown()
