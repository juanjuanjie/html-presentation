# 脚本工具

本目录保留与当前页面功能直接相关的 3 个脚本：幻灯片截图、配色预览生成和浏览器冒烟测试。

## 安装依赖

在项目根目录运行：

```bash
pip install -r requirements.txt
playwright install chromium
```

## screenshot_html_slides.py

把 HTML 演示逐页导出为 PNG：

```bash
python scripts/screenshot_html_slides.py themes/doodle-cream/template.html -o slides_out
```

常用参数：

| 参数 | 说明 | 默认值 |
|---|---|---|
| `-o, --output-dir` | 输出目录 | `slides_out` |
| `--prefix` | 文件名前缀 | `page` |
| `--mode` | `standard` / `balanced` / `compact` / `auto` | `standard` |
| `--device-scale` | 设备像素比 | `2` |
| `--content-scale` | 额外页面缩放 | `1.0` |
| `--wait` | 页面初始等待时间（毫秒） | `1000` |

脚本会隐藏模板自带的翻页控件，并按 16:9 画幅输出页面。

## generate_variant_previews.py

重新生成模板卡片使用的配色变体预览：

```bash
python scripts/generate_variant_previews.py
```

只更新一个预览：

```bash
python scripts/generate_variant_previews.py --only blue-professional.png
```

当前脚本维护 Professional 的奶油钴蓝预览与 BlockFrame 的复古纸感预览。

## test_generator.py

运行页面、模板选择与生成器冒烟测试：

```bash
python scripts/test_generator.py
```

测试覆盖演讲 / 导演模式、镜头编号校验、模板选择、页面导航与移动端布局。

## 模板约定

- 每页使用 `.slide` 元素。
- 当前页使用 `.active` class。
- 翻页逻辑只切换当前页，不应修改页面内容。
- 导演 HTML 严格一镜一页，镜头编号连续。
- 每镜口播放入 `.slide-subtitle`，用于字幕或后续时间轴匹配。
- 动效应可重播、可清理，并在截图时保持确定性。

完整设计规范见项目根目录的 [`SKILL.md`](../SKILL.md)。
