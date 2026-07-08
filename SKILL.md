---
name: "html-presentation-video"
description: "生成适合视频演示的 HTML 幻灯片：大字号、低密度、左右留白、高对比、单文件输出。"
---

# HTML Presentation · 视频友好规范

> 本规范基于 [Zara Zhang](https://github.com/zarazhangrui) 的 [frontend-slides](https://github.com/zarazhangrui/frontend-slides) 与 [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) 改编，针对视频演示场景做了调整。详见项目根目录 [`NOTICE.md`](./NOTICE.md)。

本规范用于指导生成适合 B 站讲解、知识分享、教程分镜的 HTML 幻灯片。

## 分层原则：结构 × 风格

本 Skill 采用分层模型：

- **结构层**：决定页序、每页信息结构、演讲逻辑。
- **风格层**：决定颜色、字体、背景、组件质感、装饰语法。
- **执行层**：决定 HTML 幻灯片引擎、翻页、进度条、页码和动画。

核心原则：

```text
风格是风格，结构是结构。
可以替换风格，但结构不变。
```

优先把用户请求整理成：

```yaml
task: html_presentation
source_material: "原始材料或主题"
slide_structure: compact_report_6
style_id: video_dark_default
output:
  format: html
  offline_only: true
```

其中：

- `source_material`：原始材料、会议纪要、技术文档、汇报主题。
- `slide_structure`：页面结构，读取 [`slide_structures.yaml`](./slide_structures.yaml)，可使用 `enterprise_report_12`、`compact_report_6`、`storyboard`。
- `style_id`：视觉风格；未指定时使用本文件的默认黑紫视频友好风，也可选择仓库内 `themes/` 中的主题。

详细组合协议见 [`docs/structure-style-protocol.md`](./docs/structure-style-protocol.md)。

## 默认视觉风格

- **背景**：深黑 `#08090d`，封面页可单独使用 `#070609`。
- **主色（标题/结构）**：紫色 `#c8a8ff`。
- **强调色（关键词/结论）**：黄色 `#ffc402`。
- **正文**：暖白 `#f6f2e8`、灰白 `#c4c0b6`、中性灰 `#8a8580`。
- **禁用**：青色、粉色、绿色、红色、多彩霓虹、彩虹渐变、渐变文字、大面积发光。
- **卡片圆角**：`14px`（大）、`10px`（中）。

## 核心原则：视频友好

### 1. 单页单点

每页 slide 只传达**一个核心信息**。标题就是结论，正文只留必要支撑。

❌ 错误：一页放 5 个要点 + 2 张图 + 1 个表格。  
✅ 正确：一页 1 个标题 + 1 段说明 + 1 组视觉支撑。

### 2. 字号更大

| 元素 | 尺寸 | 说明 |
|------|------|------|
| 封面 h1 | `clamp(42px, 5.5vw, 78px)` | 占画面主导地位 |
| 内容 h2 | `clamp(34px, 4vw, 56px)` | 每页结论 |
| 卡片 h3 | `clamp(20px, 2.2vw, 28px)` | 次级标题 |
| 正文 | `clamp(17px, 1.7vw, 23px)` | 最小不小于 17px |
| 小字 | `clamp(14px, 1.3vw, 17px)` | 仅用于辅助说明 |

### 3. 左右大留白

```css
.slide {
  padding: 6vh 10vw;  /* 左右约 190px @1920px */
}
```

留出安全边距，避免被 B 站字幕、进度条、UP 主头像、点赞按钮遮挡。

### 4. 主体放大

```css
.content-wrapper {
  max-width: 1000px;
  transform: scale(1.45);
  transform-origin: center center;
}
```

核心内容在 1920×1080 画布上占据主要视觉区域，但不要超出安全边距。

### 5. 高对比

- 背景保持极暗，文字保持极亮。
- 紫色用于结构和标题，黄色用于强调和结论。
- 避免半透明文字与背景对比不足。

### 6. 少装饰

- 不添加噪点纹理（视频压缩后易产生脏点）。
- 不使用大面积发光、玻璃拟态、复杂渐变。
- 不使用 emoji 作为主要内容图标（可接受少量装饰）。

## 标题规则

- **封面页**：主标题可用紫色 + 黄色 + 灰白灵活搭配，可带删除线表示旧概念。
- **普通内容页**：`h2` 必须保持纯紫色，标题下方保留短紫色 divider。
- **正文关键词/数据**：使用黄色 `.accent` 或 `.accent-text` 强调。

## 删除线规则

`.strikethrough` 用于表示被否定的旧概念。通过伪元素 `::after` 实现，颜色与文字一致，线条微微倾斜。

## 流程步骤规则

- 步骤编号使用 `01`、`02`、`03` 两位数字。
- 编号放在圆形边框内，文字为白色。
- 流程箭头用淡紫色，不抢标题。
- 每个步骤包含：编号、短标题、一句话说明。

## 布局组件

### 内容居中

```css
.slide {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
```

### 封面左对齐

```css
.cover-layout {
  align-items: flex-start;
  justify-content: center;
  padding-left: 14vw;
  text-align: left;
}
```

### 卡片网格

```html
<div class="card-grid cols-2">
  <div class="card">...</div>
  <div class="card">...</div>
</div>
```

- 视频场景推荐 `cols-2` 或 `cols-3`，避免超过 3 列。
- 每卡片只放 1 个标题 + 1 段文字。

### 双栏对比

```html
<div class="vs-row">
  <div class="vs-col left-col">...</div>
  <div class="vs-col right-col">...</div>
</div>
```

左侧为旧方式/弱方案，右侧为新方式/强方案，使用紫色边框突出右侧。

### 列表

```html
<ul class="bullet-list">
  <li>要点一</li>
  <li>要点二</li>
</ul>
```

列表整体居中，文字左对齐。每行只写一句话，行高 `1.85`。

## Slide Engine 技术规范

### HTML 结构

```html
<section class="slide">
  <div class="content-wrapper">
    <div class="anim slide-label">标签</div>
    <h2 class="anim">标题</h2>
    <div class="anim divider"></div>
    <p class="anim body-text">正文</p>
  </div>
</section>
```

### 动画

- 每页元素添加 `.anim` class，激活时自动触发 `fadeUp` 动画。
- 最多 7 级延迟，避免过多元素同时出现。

### 翻页

- 键盘：← → / Home / End / 空格。
- 点击：底部控制栏。
- 触摸：左右滑动。
- 翻页只操作 `.active` / `.exit-up` class，不使用 inline style。

### 截图隐藏

截图脚本会自动隐藏以下元素，保证导出画面干净：

- `.controls`
- `.dots`
- `.hint`
- `.progress`

## 输出工作流

1. 读取或确认 `slide_structure`，优先使用 `slide_structures.yaml`。
2. 从 `source_material` 提炼 `content_outline`。
3. 将 `content_outline` 映射到所选结构的 `pages[].regions`。
4. 确定视觉风格：默认黑紫视频友好风，或仓库 `themes/` 中的主题。
5. 复制 `templates/presentation.html`，保留 Slide Engine、Controls、Progress Bar、Dots。
6. 按"单页单点"原则编写内容。
7. 只替换视觉 tokens 和组件质感，不改变页序结构。
8. 浏览器打开预览翻页节奏。
9. 运行 `python screenshot_html_slides.py xxx.html -o slides_out`。
10. 将 PNG 序列导入剪辑软件。

## 结构选项

机读页序定义在 [`slide_structures.yaml`](./slide_structures.yaml)：

| slide_structure | 用途 |
|---|---|
| `enterprise_report_12` | 企业完整汇报 / 项目汇报 / 课题汇报 |
| `compact_report_6` | 精简汇报 / 快速讲解 |
| `storyboard` | 视频分镜 / 内容展示 |

当用户要求“从材料生成 PPT 大纲和讲稿”或“企业课题汇报”时，优先使用 `enterprise_report_12`；内容不足时可降级到 `compact_report_6`。

## 风格替换规则

当用户指定风格或主题时：

1. 保持 `slide_structure` 页序不变。
2. 保持 Slide Engine 不变。
3. 保持 Controls / Progress Bar / Dots / screenshot hiding 不变。
4. 只替换背景、主色、字体气质、卡片/面板质感、装饰元素和强调色。
5. 生成后检查结构和风格是否同时成立。

## 禁止项

- 一页多个核心观点。
- 字号低于推荐最小值。
- 使用外部 CSS/JS/图片资源（Google Fonts 等模板主题可例外，但基础模板应保持内联）。
- 复杂动画、大量装饰元素。
- 低对比度文字。
