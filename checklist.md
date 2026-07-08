# html-studio 验收清单

page 与 deck 统一适用。带 **[deck]** 仅 deck 检查。

## 1. 协议
- 判定了 `mode`（page / deck）
- page：识别 `style_id`，`layout_id` 属于该风格
- deck：识别 `theme_id`，或按 mood/tone/scheme 匹配到默认 `purple-gold-presentation`
- deck：识别或补全 `slide_structure`
- 有 `content.title` 或等价标题
- 输出到用户指定目录（未指定落工作区）

## 2. 视觉（page 风格 / deck 主题）
- 使用对应 tokens；page 出现 `must_have`、未触发 `avoid`
- **[deck]** 忠于该主题：原生 deck 主题检查 `themes/<slug>/design.md`；page 风格适配主题检查 `references/styles.yaml` 的 tokens / must_have / avoid
- 未混入其它风格/主题的主元素（尤其 deck 不得串主题）

## 3. HTML
- 单文件、16:9、文本不溢出不重叠
- page：可离线打开，无外链字体/CDN
- **[deck]** 主题若用 Google Fonts 属允许；若需纯离线，改系统字体栈（见 export.offline）

## 4. Deck 引擎 [deck]
- Slide Engine（分页）、Controls（翻页+页码）、Progress、Dots、淡入动画 齐全
- 页序与所选 `slide_structure` 一致（结构不可乱）
- **单页单点**、字号≥推荐最小、左右留白够（视频安全边距）
- 已知修复到位：
  - `.slide.active` 的 `opacity/visibility/transform` 均带 `!important`
  - 翻页只用 `classList`，无 inline `element.style.xxx`（进度条 width 除外）
  - 仅系统字体栈或主题声明的 Google Fonts，无其它外部资源
- 导航 chrome 在可被截图脚本隐藏的选择器内（`.controls/.dots/.progress/.hint` 或 `.nav-controls/.slide-counter`）

## 5. PNG 导出 [deck·可选]
- `python screenshot_html_slides.py <deck>.html -o slides_out` 可跑通
- 导出画面已隐藏控件；分辨率 1920×1080；每页一帧

## 6. 主题保真铁律 [deck]（来自 AGENTS.md）
- **不替换字体**、**不改配色**、**不删装饰**、**不圆角化 BlockFrame 的直角**、**不混两个主题**
- 缺某种版式时，用该主题的设计系统「就地设计」，而非换主题或引入新视觉语言

## 7. 匹配等级
- **high**：主色/构图/关键识别元素准确，远看即认出；[deck] 引擎四件套齐、翻页正常、页序正确、忠于 design.md
- **medium**：主色与大体结构正确，1–2 个关键细节弱化
- **low**：风格难辨 / 串了风格 / 关键元素缺失；[deck] 翻页失效或页序错乱
