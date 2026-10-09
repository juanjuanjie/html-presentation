---
name: "html-presentation-video"
description: "将逐字稿生成简洁演讲 HTML，或将导演稿逐镜生成导演 HTML；沿用用户模板，单文件输出。"
---

# HTML Presentation · 视频友好规范

> 本规范基于 [Zara Zhang](https://github.com/zarazhangrui) 的 [frontend-slides](https://github.com/zarazhangrui/frontend-slides) 与 [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) 改编，针对视频演示场景做了调整。详见项目根目录 [`NOTICE.md`](./NOTICE.md)。

本规范用于指导生成适合 B 站讲解、知识分享、教程分镜的 HTML 幻灯片。

## 首先选择模式

- **演讲 HTML**：输入逐字稿，提炼观点，可合并段落并自由分页，以轻量动画、手动讲解为主。输出 `【演讲HTML】原稿标题.html`。
- **导演 HTML**：输入导演稿，严格一镜一页，不增加封面、不合并或遗漏镜头；逐镜保留口播原文及标点，实现指定动效。输出 `【导演HTML】原稿标题.html`。
- 用户要求导演 HTML 却只给逐字稿时，先请求导演稿，不默默替用户编排镜头。

生成前完整阅读 [两种生成模式](docs/generation-modes.md)，遵循其模式约束与验收要求。每次另存新 HTML，不修改输入。用户指定模板和配色优先；下文紫金配色、字号、缩放、组件只是默认模板示例，不可强行覆盖其他主题。导演模式的逐镜约束优先于下文的内容精简与轻量动画建议。

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
- 翻页复用所选模板的激活状态和交互；导演模式还必须执行每页的动效初始化与清理，不能只切换 class。

### 截图隐藏

截图脚本会自动隐藏以下元素，保证导出画面干净：

- `.controls`
- `.dots`
- `.hint`
- `.progress`

## 输出工作流

1. 读取用户指定的完整模板；未指定时使用 `templates/presentation.html`。
2. 按所选生成模式编写内容，另存为新文件。
3. 浏览器打开预览翻页节奏。
4. 如需静态图片，运行 `python scripts/screenshot_html_slides.py xxx.html -o slides_out`；PNG 不包含动态过程。
5. 将 PNG 序列导入剪辑软件。

## 禁止项

- 一页多个核心观点。
- 字号低于推荐最小值。
- 使用外部 CSS/JS/图片资源（Google Fonts 等模板主题可例外，但基础模板应保持内联）。
- 演讲模式避免复杂动画；导演模式允许稿件要求的动效，但必须可重播、可确定性定位。两种模式都避免无意义装饰。
- 低对比度文字。
