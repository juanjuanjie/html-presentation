#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_covers.py
从每个主题的 template.html 中提取第一页作为 classic 封面，
生成独立可预览的 themes/{theme}/covers/classic.html。

不会覆盖已存在的手动设计封面（非 classic 文件保留）。
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def safe_print(msg):
    """兼容 Windows GBK 控制台：无法编码的字符用 ? 替换。"""
    encoded = (msg + "\n").encode(sys.stdout.encoding, errors="replace")
    sys.stdout.buffer.write(encoded)


ROOT = Path(__file__).resolve().parent.parent
THEMES_DIR = ROOT / "themes"
INDEX_FILE = THEMES_DIR / "covers-index.json"


def theme_covers_dir(slug: str) -> Path:
    """每个主题下的 covers/ 目录。"""
    return THEMES_DIR / slug / "covers"

# 隐藏所有可能与封面无关的导航控件，确保独立预览干净
HIDE_CHROME = """
/* extracted-cover: hide navigation chrome that may leak from theme CSS */
.nav-controls, .slide-counter, .progress-bar, .dots, .controls,
.keyboard-hint, .nav-arrows, .nav-btn, .nav-dots {
  display: none !important;
}
"""

# 手动封面文件名 -> 默认元数据（可被 index.json 中已有条目覆盖）
STYLE_META = {
    "tutorial": {
        "name_suffix": "教程风封面",
        "style": "tutorial",
        "best_for": "AI 教程、实战教学、零基础入门类视频封面",
    },
    "impact": {
        "name_suffix": "冲击风封面",
        "style": "impact",
        "best_for": "热点话题、争议观点、强情绪表达",
    },
    "minimal": {
        "name_suffix": "极简封面",
        "style": "minimal",
        "best_for": "干净、克制、专业感强的内容",
    },
}


def extract_title_from_html(html: str) -> str:
    m = re.search(r"<title>([^<]*)</title>", html, re.IGNORECASE)
    return m.group(1).strip() if m else ""


def load_index():
    if INDEX_FILE.exists():
        return json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    return {"schema_version": 1, "covers": []}


def save_index(data):
    INDEX_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def embed_index_into_html(data: dict):
    """把封面索引内联到 index.html，让 file:// 直接打开时也能看到封面卡片。"""
    html_path = ROOT / "index.html"
    if not html_path.exists():
        safe_print(f"[!] 未找到 {html_path}，跳过内联")
        return
    html = html_path.read_text(encoding="utf-8")
    marker = "<!-- cover-index-data -->"
    if marker not in html:
        safe_print(f"[!] {html_path} 中未找到 {marker}，跳过内联")
        return

    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    script_block = f"""{marker}
  <script>
    window.__COVER_INDEX__ = {json_str};
  </script>"""

    # 替换 marker 到下一个 <script> 标签之间的内容，避免重复插入
    html = re.sub(
        rf"{re.escape(marker)}\s*<script[^>]*>.*?</script>",
        script_block,
        html,
        count=1,
        flags=re.DOTALL,
    )
    # 如果上面没有匹配到（首次运行），直接替换 marker
    if marker in html and "window.__COVER_INDEX__" not in html:
        html = html.replace(marker, script_block, 1)

    html_path.write_text(html, encoding="utf-8")
    safe_print(f"[OK] 已内联封面索引到 {html_path}")


def extract_head(html: str) -> str:
    """提取 <head> 内部内容，并去掉原 charset/viewport/title，避免独立 HTML 重复。"""
    m = re.search(r"<head[^>]*>([\s\S]*?)</head>", html, re.IGNORECASE)
    if not m:
        return ""
    inner = m.group(1)
    # 去掉原 <meta charset>、<meta viewport> 和 <title>，后续由 build_cover_html 提供统一标题
    inner = re.sub(r"<meta[^>]*charset[^>]*>\s*", "", inner, flags=re.IGNORECASE)
    inner = re.sub(r"<meta[^>]*viewport[^>]*>\s*", "", inner, flags=re.IGNORECASE)
    inner = re.sub(r"<title>[^<]*</title>\s*", "", inner, flags=re.IGNORECASE)
    return inner


def extract_first_slide(html: str) -> str:
    """提取第一个 class 中完整出现 'slide' 的元素（section 或 div），并确保 active。"""
    # 先定位开始标签
    m = re.search(
        r"<((?:section|div))[^>]*class=\"(?:[^\"]*\s)?slide(?:\s[^\"]*)?\"[^>]*>",
        html,
        re.IGNORECASE,
    )
    if not m:
        raise ValueError("未找到第一个 slide")

    tag = m.group(1).lower()
    start = m.start()
    depth = 1
    i = m.end()
    while i < len(html) and depth > 0:
        # 查找下一个同类型开始或结束标签
        next_open = re.search(
            rf"<{tag}(?:\s[^>]*)?>", html[i:], flags=re.IGNORECASE
        )
        next_close = re.search(
            rf"</{tag}\s*>", html[i:], flags=re.IGNORECASE
        )
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
                slide = html[start:end]
                break
            i = close_pos + len(next_close.group(0))

    # 确保 slide 有 active 类，方便独立预览
    if not re.search(r'class="[^"]*\bactive\b', slide):
        slide = re.sub(
            r'class="([^"]*)"',
            lambda mm: f'class="{mm.group(1).strip()} active"',
            slide,
            count=1,
        )
    return slide


def build_cover_html(head_inner: str, slide: str, title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
{head_inner}
  <style>
{HIDE_CHROME}
  </style>
</head>
<body>
{slide}
</body>
</html>
"""


def main():
    index = load_index()

    # 读取 themes/index.json 中的主题列表
    themes_index = json.loads((THEMES_DIR / "index.json").read_text(encoding="utf-8"))
    themes = themes_index.get("templates", [])

    existing_by_id = {c["id"]: c for c in index["covers"]}
    new_covers = []

    for theme in themes:
        slug = theme["slug"]
        name = theme.get("name", slug)
        template_path = THEMES_DIR / slug / "template.html"
        if not template_path.exists():
            safe_print(f"[!] 跳过 {slug}: 未找到 {template_path}")
            continue

        cover_dir = theme_covers_dir(slug)
        cover_dir.mkdir(parents=True, exist_ok=True)
        cover_file = cover_dir / "classic.html"

        html = template_path.read_text(encoding="utf-8")
        head_inner = extract_head(html)
        slide = extract_first_slide(html)
        cover_html = build_cover_html(head_inner, slide, f"{name} · 经典封面")
        cover_file.write_text(cover_html, encoding="utf-8")
        safe_print(f"[OK] {slug}/classic.html")

        cover_id = f"{slug}/classic"
        entry = {
            "id": cover_id,
            "theme": slug,
            "file": f"themes/{slug}/covers/classic.html",
            "name": f"{name} · 经典封面",
            "style": "classic",
            "preview": f"assets/previews/covers/{slug}_classic.png",
            "best_for": "保留主题原始风格的通用封面",
            "placeholders": ["title", "subtitle", "tagline", "meta"],
        }
        existing_by_id[cover_id] = entry
        new_covers.append(cover_id)

    # 发现并登记已有的非 classic 封面（手动设计）
    for theme in themes:
        slug = theme["slug"]
        name = theme.get("name", slug)
        cover_dir = theme_covers_dir(slug)
        if not cover_dir.exists():
            continue
        for cover_file in sorted(cover_dir.glob("*.html")):
            if cover_file.name == "classic.html":
                continue
            cover_id = f"{slug}/{cover_file.stem}"
            if cover_id in existing_by_id:
                # 更新路径，防止目录结构变更后索引里的路径失效
                existing_by_id[cover_id]["file"] = f"themes/{slug}/covers/{cover_file.name}"
                existing_by_id[cover_id]["preview"] = f"assets/previews/covers/{slug}_{cover_file.stem}.png"
                if cover_id not in new_covers:
                    new_covers.append(cover_id)
                continue

            cover_html = cover_file.read_text(encoding="utf-8")
            file_title = extract_title_from_html(cover_html)
            meta = STYLE_META.get(cover_file.stem, {
                "name_suffix": f"{cover_file.stem} 封面",
                "style": cover_file.stem,
                "best_for": "自定义封面模板",
            })
            display_name = file_title or f"{name} · {meta['name_suffix']}"
            entry = {
                "id": cover_id,
                "theme": slug,
                "file": f"themes/{slug}/covers/{cover_file.name}",
                "name": display_name,
                "style": meta["style"],
                "preview": f"assets/previews/covers/{slug}_{cover_file.stem}.png",
                "best_for": meta["best_for"],
                "placeholders": ["title", "subtitle", "tags", "category"],
            }
            existing_by_id[cover_id] = entry
            new_covers.append(cover_id)
            safe_print(f"[OK] 已登记手动封面 {cover_id}")

    index["covers"] = [existing_by_id[cid] for cid in new_covers]
    index["generated_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    save_index(index)
    embed_index_into_html(index)
    safe_print(f"[OK] 已更新 {INDEX_FILE}")


if __name__ == "__main__":
    main()
