# 脚本工具

<p align="center">
  <strong>HTML Presentation 脚本工具集</strong>
</p>

<p align="center">
  封面提取、封面应用、幻灯片截图三条命令，覆盖从模板到分镜素材的完整工作流。
</p>

---

## 这是什么？

本目录提供三个独立的 Python 脚本，分别负责封面管理、封面替换和幻灯片截图导出。三者可单独使用，也可串联成完整流水线：

1. 用 `extract_covers.py` 从各主题模板提取经典封面并维护索引。
2. 用 `apply_cover.py` 把某个封面应用到目标演示文稿的第一页。
3. 用 `screenshot_html_slides.py` 把最终 HTML 导出为 1920×1080 PNG 序列。

## 环境准备

所有脚本共用项目根目录的依赖：

```bash
pip install -r requirements.txt
playwright install chromium
```

`extract_covers.py` 和 `apply_cover.py` 仅依赖 Python 标准库，无需额外安装。`screenshot_html_slides.py` 依赖 Playwright，需要单独安装 Chromium。

## 路径解析

三个脚本均通过 `Path(__file__).resolve().parent.parent` 自动定位**项目根目录**（即 `scripts/` 的父目录），因此：

- 所有命令需在**项目根目录**下执行，路径参数（如 `themes/...`、`-o output.html`）均相对于项目根目录解析。
- 脚本内部访问 `themes/`、`index.html`、`themes/covers-index.json` 等项目文件时，不受脚本自身所在目录影响。
- `screenshot_html_slides.py` 省略 `html_path` 参数时，会在项目根目录下查找最新的 `.html` 文件作为默认输入。

## 目录结构

```
scripts/
├── README.md                  # 本文件
├── apply_cover.py             # 把封面 HTML 应用到演示文稿第一页
├── extract_covers.py          # 从主题模板提取经典封面并更新索引
└── screenshot_html_slides.py  # 截图导出 1920×1080 PNG 序列
```

---

## extract_covers.py

### 核心功能

从 `themes/` 下每个主题的 `template.html` 中提取第一页 slide，生成独立可预览的经典封面 `themes/{theme}/covers/classic.html`，同时扫描并登记已有的手动设计封面，统一写入 `themes/covers-index.json`，并把索引内联到项目根目录的 `index.html` 中。

脚本运行时会：

- 遍历 `themes/index.json` 中登记的所有主题。
- 提取每个主题模板的 `<head>` 样式和第一个 `.slide` 元素，组装成完整 HTML 文件。
- 自动为提取的 slide 添加 `active` 类，确保独立预览时可见。
- 注入一段隐藏导航控件的 CSS，避免独立预览时出现翻页按钮等干扰元素。
- 扫描各主题 `covers/` 目录下非 `classic.html` 的手动封面，按文件名匹配默认元数据。
- 更新 `themes/covers-index.json`，并把封面数据内联到 `index.html` 的 `<!-- cover-index-data -->` 标记处。

### 输入

无需命令行参数，脚本自动从项目目录结构中读取数据：

| 输入 | 来源 | 说明 |
|------|------|------|
| 主题列表 | `themes/index.json` | 脚本读取 `templates` 数组，逐个处理。 |
| 模板文件 | `themes/{slug}/template.html` | 提取第一页 slide 作为经典封面来源。 |
| 手动封面 | `themes/{slug}/covers/*.html` | 扫描并登记到索引，不覆盖已有文件。 |

### 输出

| 输出 | 路径 | 说明 |
|------|------|------|
| 经典封面 | `themes/{slug}/covers/classic.html` | 每个主题生成一个，可直接用浏览器打开预览。 |
| 封面索引 | `themes/covers-index.json` | 记录所有封面的 id、主题、文件路径、风格、适用场景等元数据。 |
| 内联索引 | `index.html` | 把封面数据写入 `window.__COVER_INDEX__`，支持 `file://` 直接预览。 |

### 使用方法

```bash
python scripts/extract_covers.py
```

运行后控制台会逐行输出处理结果：

```
[OK] blockframe/classic.html
[OK] blockframe-dark/classic.html
[OK] blue-professional/classic.html
[OK] purple-gold-presentation/classic.html
[OK] 已登记手动封面 purple-gold-presentation/tutorial
[OK] 已内联封面索引到 index.html
[OK] 已更新 themes/covers-index.json
```

### 手动封面元数据

脚本会为特定文件名的手动封面匹配默认元数据，未匹配的文件使用通用描述：

| 文件名 | 风格 | 适用场景 |
|--------|------|----------|
| `tutorial.html` | 教程风 | AI 教程、实战教学、零基础入门类视频封面 |
| `impact.html` | 冲击风 | 热点话题、争议观点、强情绪表达 |
| `minimal.html` | 极简风 | 干净、克制、专业感强的内容 |
| 其他 | 沿用文件名 | 自定义封面模板 |

### 注意事项

- 脚本不会覆盖已存在的手动设计封面，只生成和更新 `classic.html`。
- 索引中已有的条目会被保留并更新路径，防止目录结构变更后路径失效。
- 如果 `index.html` 中没有 `<!-- cover-index-data -->` 标记，内联步骤会被跳过，不影响索引文件本身。

---

## apply_cover.py

### 核心功能

把 `themes/{theme}/covers/` 下的某个封面 HTML 应用到目标演示文稿的第一页，替换原有首页内容。脚本会自动处理 CSS 作用域隔离和 slide 状态管理，避免封面样式污染目标演示文稿，同时确保封面成为唯一的 active slide。

### 输入参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `cover` | 位置参数 | 是 | 封面 HTML 文件路径，或 `themes/covers-index.json` 中的封面 id（格式：`主题名/封面名`）。 |
| `presentation` | 位置参数 | 是 | 目标演示文稿 HTML 文件路径。 |
| `-o, --output` | 选项 | 否 | 输出文件路径。默认在目标文件名后加 `.covered.html`。 |

### 输出

一个完整的 HTML 文件，第一页被替换为封面内容，其余页保持不变。封面被包裹在 `<div class="slide cover-slide active">` 中，样式经过作用域隔离处理。

### 使用方法

按文件路径指定封面：

```bash
python scripts/apply_cover.py \
    themes/purple-gold-presentation/covers/tutorial.html \
    themes/purple-gold-presentation/template.html \
    -o output.html
```

按索引 id 指定封面（从 `themes/covers-index.json` 查找）：

```bash
python scripts/apply_cover.py \
    purple-gold-presentation/tutorial \
    themes/purple-gold-presentation/template.html \
    -o output.html
```

省略 `-o` 时，输出文件自动命名为 `template.covered.html`：

```bash
python scripts/apply_cover.py \
    purple-gold-presentation/classic \
    themes/purple-gold-presentation/template.html
```

### 处理流程

1. 解析封面参数：优先按文件路径查找，匹配失败则从 `themes/covers-index.json` 按 id 查找。
2. 提取封面 `<body>` 内容，移除其中的 `<script>` 标签。
3. 提取封面所有 `<style>` 内容，为每条规则的选择器加上 `.cover-slide` 前缀，实现 CSS 作用域隔离。`@keyframes`、`@font-face` 等全局规则保持原样。
4. 把封面根元素的 `.slide` 类替换为 `.cover-root`，避免目标演示文稿的翻页 JS 误管理封面内部元素。
5. 用栈匹配算法定位目标演示文稿的第一个 `.slide` 元素，整体替换为封面内容。
6. 在 `</head>` 前注入隔离后的封面 CSS 和一段 active 覆盖样式，强制封面可见。
7. 清除所有 slide 的 `active` 类，只给封面 wrapper 及其内部 slide 添加 `active`，确保首次打开时显示封面。

### 注意事项

- 脚本会完整替换目标演示文稿的第一个 `.slide`，原首页内容不会保留。如需保留，请提前备份。
- CSS 作用域隔离能减少大多数样式冲突，但无法处理 `!important` 优先级极高的全局规则。如果封面显示异常，检查目标模板是否有覆盖性强的全局样式。
- 输出文件可直接用浏览器打开预览，翻页交互正常工作。

---

## screenshot_html_slides.py

### 核心功能

使用 Playwright 驱动 Chromium，把 HTML 演示文稿的每一页 slide 截取为 1920×1080 的 PNG 图片，输出可直接拖入剪辑软件的分镜素材序列。脚本会自动隐藏导航控件、禁用动画过渡，并支持多种截图裁剪模式。

### 输入参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `html_path` | 位置参数 | — | HTML 演示文稿路径。省略时自动查找项目根目录下最新的 `.html` 文件。 |
| `-o, --output-dir` | 选项 | `slides_out` | PNG 输出目录。 |
| `-s, --selector` | 选项 | `.slide` | slide 元素的 CSS 选择器。 |
| `-W, --viewport-width` | 选项 | `1920` | 视口宽度（像素）。 |
| `-H, --viewport-height` | 选项 | `1080` | 视口高度（像素）。 |
| `--prefix` | 选项 | `page` | 输出文件名前缀，最终格式为 `{prefix}_{序号}.png`。 |
| `--wait` | 选项 | `1000` | 页面加载后的初始等待时间（毫秒）。 |
| `--transition-wait` | 选项 | `650` | 切换 slide 后的等待时间（毫秒），用于等待过渡动画结束。 |
| `--device-scale` | 选项 | `2` | 设备像素比，数值越大截图越清晰，文件也越大。 |
| `--content-scale-preset` | 选项 | — | 内容缩放预设，可选 `1.0x` / `1.5x` / `1.6x`。 |
| `--content-scale` | 选项 | `0` | 自定义内容缩放比例，设为正数时覆盖预设。 |
| `--mode` | 选项 | `standard` | 截图模式，详见下表。 |
| `--hide-selectors` | 选项 | 内置列表 | 需要隐藏的 CSS 选择器列表，空格分隔。 |

### 截图模式

| 模式 | 说明 |
|------|------|
| `standard` | 保留完整 16:9 画布，直接截取整个视口。适合已经做好留白的模板。 |
| `balanced` | 围绕内容裁剪但保持 16:9 比例，自动添加 48px 水平 / 32px 垂直边距。 |
| `compact` | 紧贴内容裁剪，不强制 16:9，添加 24px 水平 / 20px 垂直边距。适合单页素材单独使用。 |
| `auto` | 自动判断：内容占比低于 62% 时用 `compact`，否则用 `balanced`。 |

### 输出

输出目录下的 PNG 序列，文件名格式为 `{prefix}_{序号}.png`，序号从 `01` 开始补零。默认输出 `slides_out/page_01.png`、`slides_out/page_02.png`...，分辨率 1920×1080，设备像素比 2 倍（实际像素 3840×2160）。

### 使用方法

基础导出：

```bash
python scripts/screenshot_html_slides.py \
    themes/purple-gold-presentation/template.html \
    -o slides_out
```

指定输出前缀和截图模式：

```bash
python scripts/screenshot_html_slides.py \
    themes/blockframe/template.html \
    -o slides_out \
    --prefix blockframe \
    --mode compact
```

调整等待时间和缩放：

```bash
python scripts/screenshot_html_slides.py \
    themes/blue-professional/template.html \
    -o slides_out \
    --wait 2000 \
    --transition-wait 800 \
    --content-scale 1.5
```

### 处理流程

1. 解析参数，确定 HTML 文件路径（省略时在项目根目录自动查找）。
2. 启动无头 Chromium，设置视口大小和设备像素比。
3. 加载 HTML，等待初始时间，注入隐藏控件 CSS 和禁用动画 CSS。
4. 遍历所有 `.slide` 元素，逐个激活并截图。
5. 根据 `--mode` 决定截取方式：`standard` 截全屏，`balanced` / `compact` 计算裁剪区域后截取，`auto` 按内容密度自动选择。
6. 关闭浏览器，输出 PNG 序列。

### 注意事项

- 项目模板已内置 `.content-wrapper { transform: scale(1.45) }` 放大内容，因此默认不额外缩放。手动设置 `--content-scale` 大于 1 时可能导致内容超出画布边缘。
- 交互式终端运行时会提示选择缩放预设，非交互环境（如 CI）默认使用 `1.0x`。
- 如果 slide 中使用了 `deck-stage` 自定义元素的 Shadow DOM 覆盖层，脚本会自动隐藏其 `.overlay`。
- 动画类 `.anim` 的元素会被强制设为 `opacity: 1`，确保截图时所有内容可见。

---

## 完整工作流示例

以下命令均在**项目根目录**下执行：

从模板到最终分镜素材的完整流程：

```bash
# 1. 提取所有主题的经典封面（首次运行或新增主题后执行）
python scripts/extract_covers.py

# 2. 把教程封面应用到紫金主题模板的第一页
python scripts/apply_cover.py \
    purple-gold-presentation/tutorial \
    themes/purple-gold-presentation/template.html \
    -o my-presentation.html

# 3. 导出 1920×1080 PNG 分镜序列
python scripts/screenshot_html_slides.py \
    my-presentation.html \
    -o slides_out \
    --mode standard
```

输出目录 `slides_out/` 下的 PNG 文件可直接拖入剪映、Premiere、DaVinci Resolve 等剪辑软件，按序号排列即为视频分镜顺序。
