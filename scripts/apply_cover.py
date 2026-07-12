#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_cover.py
把 themes/{theme}/covers/ 下的某个封面 HTML 应用到目标演示文稿的第一页。

用法示例：
    python apply_cover.py themes/purple-gold-presentation/covers/tutorial.html \
                          themes/purple-gold-presentation/template.html \
                          -o output.html

也可以按 id 选择封面（从 themes/covers-index.json 查找）：
    python apply_cover.py purple-gold-presentation/tutorial \
                          themes/purple-gold-presentation/template.html \
                          -o output.html
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_FILE = ROOT / "themes" / "covers-index.json"


def safe_print(msg):
    """兼容 Windows GBK 控制台。"""
    encoded = (msg + "\n").encode(sys.stdout.encoding, errors="replace")
    sys.stdout.buffer.write(encoded)


def load_index():
    if INDEX_FILE.exists():
        return json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    return {"covers": []}


def resolve_cover_path(cover_arg: str) -> Path:
    """参数可能是文件路径，也可能是 index.json 中的 id。"""
    p = Path(cover_arg)
    if p.exists() and p.suffix == ".html":
        return p

    index = load_index()
    for c in index.get("covers", []):
        if c["id"] == cover_arg:
            return ROOT / c["file"]

    raise FileNotFoundError(f"找不到封面: {cover_arg}")


def extract_body_content(html: str) -> str:
    """提取 <body> 内部所有内容（不含 <script>）。"""
    m = re.search(r"<body[^>]*>([\s\S]*?)</body>", html, re.IGNORECASE)
    if not m:
        raise ValueError("封面 HTML 缺少 <body>")
    body = m.group(1)
    body = re.sub(r"<script[\s\S]*?</script>", "", body, flags=re.IGNORECASE)
    return body.strip()


def prepare_cover_body(body: str) -> str:
    """
    把封面根元素上的 .slide 类移除，换成 .cover-root，避免目标演示文稿的
    slide 导航 JS 把它当作普通 slide 管理（比如去掉 active）。
    """
    # 匹配 body 中的第一个标签
    m = re.match(
        r"(\s*)<((?:section|div))\b([^>]*class=\"([^\"]*)\")?([^>]*)>([\s\S]*)",
        body,
        flags=re.IGNORECASE,
    )
    if not m:
        return body
    before, tag, class_attr, cls, rest, after = m.groups()
    if cls and "slide" in cls.split():
        new_cls = " ".join(
            [c for c in cls.split() if c != "slide"] + ["cover-root"]
        ).strip()
        # 重建 class 属性（保留原有顺序中的非 slide 类）
        if class_attr:
            new_open = f'<{tag}{class_attr.replace(cls, new_cls)}{rest}>'
        else:
            new_open = f'<{tag} class="{new_cls}"{rest}>'
        return before + new_open + after
    return body


def extract_styles(html: str) -> str:
    """提取所有 <style> 标签内容。"""
    return "\n\n".join(re.findall(r"<style[^>]*>([\s\S]*?)</style>", html, flags=re.IGNORECASE))


def scope_css(css: str, scope: str = ".cover-slide") -> str:
    """
    将普通规则的 selector 前缀加上 scope，减少与目标演示文稿的样式冲突。
    @media / @supports 内部规则同样处理；@keyframes / @font-face 保持全局。
    """
    css = re.sub(r"/\*[\s\S]*?\*/", "", css)  # 去掉注释
    blocks = []
    depth = 0
    buf = []

    for ch in css:
        buf.append(ch)
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                blocks.append("".join(buf).strip())
                buf = []
    if buf:
        blocks.append("".join(buf).strip())

    out = []
    for block in blocks:
        if not block:
            continue
        head, _, body = block.partition("{")
        head = head.strip()
        body = body.rstrip("}").strip()

        if not head:
            continue

        if head.startswith("@"):
            atrule = head.lower()
            if atrule.startswith("@media") or atrule.startswith("@supports"):
                inner = scope_css(body, scope)
                out.append(f"{head} {{\n{inner}\n}}")
            else:
                # @keyframes, @font-face, @import 等保持原样
                out.append(block)
            continue

        selectors = [s.strip() for s in head.split(",") if s.strip()]
        scoped_selectors = []
        for sel in selectors:
            low = sel.lower()
            if low == ":root":
                scoped_selectors.append(scope)
            elif low in ("html", "body"):
                scoped_selectors.append(scope)
            elif low == "*":
                scoped_selectors.append(f"{scope} *")
            else:
                scoped_selectors.append(f"{scope} {sel}")
        out.append(f"{', '.join(scoped_selectors)} {{\n{body}\n}}")

    return "\n\n".join(out)


def ensure_single_active(pres_html: str) -> str:
    """确保封面 wrapper 及其内部 slide 均带 active，其他 slide 不带 active。"""
    # 1. 先把所有 slide 类元素的 active 去掉
    pres_html = re.sub(
        r'class="([^"]*)\bactive\b([^"]*)"',
        lambda m: f'class="{m.group(1).strip()}{m.group(2).strip()}"'.replace("  ", " "),
        pres_html,
    )

    # 2. 给封面 wrapper 加 active
    wrapper_match = re.search(r'<(div|section)[^>]*class="([^"]*\bcover-slide\b[^"]*)"', pres_html, flags=re.IGNORECASE)
    if wrapper_match:
        cls = wrapper_match.group(2).strip()
        if "slide" not in cls.split():
            cls = "slide " + cls
        if "active" not in cls.split():
            cls += " active"
        pres_html = pres_html[:wrapper_match.start()] + f'<{wrapper_match.group(1)} class="{cls.strip()}"' + pres_html[wrapper_match.end():]

    # 3. 给封面内部所有 .slide 元素也加 active，确保 extracted classic 封面可见
    def activate_inner_slides(html):
        pattern = re.compile(r'(<(div|section)[^>]*class="([^"]*\bslide\b[^"]*)"[^>]*>)', re.IGNORECASE)
        def repl(m):
            inner_cls = m.group(3).strip()
            if "active" in inner_cls.split():
                return m.group(0)
            return f'<{m.group(2)} class="{inner_cls} active"' + m.group(0)[m.group(0).index('>'):]
        return pattern.sub(repl, html)

    # 只在第一个 cover-slide 内部生效：拆出封面 wrapper 段落，处理内部，再拼回
    cover_start = re.search(r'<(div|section)[^>]*class="[^"]*\bcover-slide\b[^"]*"[^>]*>', pres_html, flags=re.IGNORECASE)
    if cover_start:
        # 找到匹配的闭合标签（简单栈匹配）
        tag = cover_start.group(1).lower()
        i = cover_start.end()
        depth = 1
        cover_end_pos = None
        while i < len(pres_html) and depth > 0:
            next_open = re.search(rf'<{tag}(?:\s[^>]*)?>', pres_html[i:], flags=re.IGNORECASE)
            next_close = re.search(rf'</{tag}\s*>', pres_html[i:], flags=re.IGNORECASE)
            open_pos = next_open.start() + i if next_open else None
            close_pos = next_close.start() + i if next_close else None
            if close_pos is None:
                break
            if open_pos is not None and open_pos < close_pos:
                depth += 1
                i = open_pos + len(next_open.group(0))
            else:
                depth -= 1
                if depth == 0:
                    cover_end_pos = close_pos + len(next_close.group(0))
                    break
                i = close_pos + len(next_close.group(0))
        if cover_end_pos:
            cover_html = pres_html[cover_start.start():cover_end_pos]
            cover_html = activate_inner_slides(cover_html)
            pres_html = pres_html[:cover_start.start()] + cover_html + pres_html[cover_end_pos:]

    return pres_html


def apply_cover(cover_path: Path, presentation_path: Path, output_path: Path = None) -> str:
    cover_html = cover_path.read_text(encoding="utf-8")
    pres_html = presentation_path.read_text(encoding="utf-8")

    body_content = extract_body_content(cover_html)
    cover_css = scope_css(extract_styles(cover_html))

    # 预处理封面内容：去掉内部根元素的 .slide，避免与目标 deck JS 冲突
    body_content = prepare_cover_body(body_content)

    # 把封面内容包进 .slide.cover-slide.active
    new_slide = f'<div class="slide cover-slide active">\n{body_content}\n</div>\n'

    # 替换目标中第一个 slide（使用栈匹配，避免被内部 </div> 截断）
    start_match = re.search(
        r'<((?:section|div))[^>]*class="(?:[^"]*\s)?slide(?:\s[^"]*)?"[^>]*>',
        pres_html,
        flags=re.IGNORECASE,
    )
    if not start_match:
        raise ValueError("目标演示文稿未找到 slide")

    tag = start_match.group(1).lower()
    start = start_match.start()
    i = start_match.end()
    depth = 1
    end = None
    while i < len(pres_html) and depth > 0:
        next_open = re.search(rf'<{tag}(?:\s[^>]*)?>', pres_html[i:], flags=re.IGNORECASE)
        next_close = re.search(rf'</{tag}\s*>', pres_html[i:], flags=re.IGNORECASE)
        open_pos = next_open.start() + i if next_open else None
        close_pos = next_close.start() + i if next_close else None
        if close_pos is None:
            raise ValueError(f"未找到 {tag} 的闭合标签")
        if open_pos is not None and open_pos < close_pos:
            depth += 1
            i = open_pos + len(next_open.group(0))
        else:
            depth -= 1
            if depth == 0:
                end = close_pos + len(next_close.group(0))
                break
            i = close_pos + len(next_close.group(0))
    if end is None:
        raise ValueError("未找到 slide 结束位置")

    pres_html = pres_html[:start] + new_slide + pres_html[end:]

    # 注入 scoped CSS，并追加 active 覆盖，避免 .cover-slide .slide 压住 .slide.active
    active_override = """
.cover-slide > .cover-root,
.cover-slide > .cover-slide {
  width: 100% !important;
  height: 100% !important;
  opacity: 1 !important;
  pointer-events: all !important;
  transform: translateX(0) !important;
  position: relative !important;
}
.cover-slide .slide.active,
.cover-slide .cover-slide.active {
  opacity: 1 !important;
  pointer-events: all !important;
  transform: translateX(0) !important;
  z-index: 10 !important;
}
/* 强制恢复紫金主题封面中的强调色，避免被父级 h1 颜色覆盖 */
.cover-slide .cover-purple { color: var(--primary) !important; }
.cover-slide .cover-yellow { color: var(--accent-gold) !important; }
.cover-slide .cover-gray { color: var(--text-muted) !important; }
"""
    css_block = f"<style>\n/* cover styles from {cover_path.name} */\n{cover_css}\n{active_override}</style>\n</head>"
    pres_html = re.sub(r"</head>", css_block, pres_html, count=1, flags=re.IGNORECASE)

    # 确保只有第一个 slide active
    pres_html = ensure_single_active(pres_html)

    if output_path:
        output_path = Path(output_path)
        output_path.write_text(pres_html, encoding="utf-8")
        safe_print(f"[OK] 已保存 {output_path}")
    return pres_html


def main():
    parser = argparse.ArgumentParser(description="把封面模板应用到演示文稿第一页")
    parser.add_argument("cover", help="封面 HTML 路径或 index.json 中的 id")
    parser.add_argument("presentation", help="目标演示文稿 HTML 路径")
    parser.add_argument("-o", "--output", help="输出文件路径（默认覆盖原文件名加 .covered.html）")
    args = parser.parse_args()

    cover_path = resolve_cover_path(args.cover)
    presentation_path = Path(args.presentation)
    output_path = args.output
    if not output_path:
        output_path = presentation_path.with_suffix(".covered" + presentation_path.suffix)

    apply_cover(cover_path, presentation_path, output_path)


if __name__ == "__main__":
    main()
