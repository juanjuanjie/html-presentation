# 优化合并说明

## 一、合并了哪两个 skill

| | Skill A | Skill B |
|---|---|---|
| 名称 | html-style-protocol | html-presentation（juanjuanjie，基于 Zara Zhang，MIT）|
| 定位 | 单页风格化 HTML | 视频友好多页幻灯片 |
| 视觉 | 6 套离线中式**页风格** | 4 套视频友好**deck 主题** |
| 输入 | `style_id + layout_id + content` | 主题 + 页序 + 内容 |
| 特色 | must_have/avoid 护栏、离线、别名归一、验收清单 | 真实幻灯片引擎、PNG 分镜导出、按 mood/tone 选主题、design.md 设计系统 |

## 二、各取的精华

**取自 A：** 6 套有辨识度的中式视觉风格及其 tokens / must_have / avoid 护栏；`风格×版式×内容` 的清晰协议；自然语言别名归一；离线单文件铁律；验收清单机制。

**取自 B：** 真实、已修复两个已知 Bug 的幻灯片引擎（`presentation.html`，20+ 组件）；4 套设计系统级 deck 主题（每套一份 `design.md`）；**PNG 1920×1080 分镜导出管线**（原 A 没有的能力）；「先问 occasion+mood → 按 tone 选主题 → 忠于 design.md 生成、缺版式就地设计」的工作流；视频友好三原则（单页单点、字号够大、左右留白）。

## 三、统一架构（风格 × 结构 × 执行）

```
执行层  page 单页渲染  |  deck: presentation.html 引擎 + screenshot 导出
结构层  page: layout_id（页内区域）      deck: slide_structure（多页页序）
风格层  page: styles.yaml 6 风格         deck: themes/*.design.md 4 主题
```

一个 `mode` 开关分流：`page`（Skill A 世界）/ `deck`（Skill B 世界），共用别名表与验收清单。

## 四、做的优化 / 取舍

1. **消除重复**：6 风格库合并为唯一事实源 `references/styles.yaml`；deck 主题各自一份 `design.md`。
2. **退休占位、改用真身**：上一版我临时注册的 `midnight_purple` 由真实主题 `purple-gold-presentation` 取代（后者正是 `presentation.html` 基底引擎的原生外观）。
3. **并入导出能力**：把 B 的 `screenshot_html_slides.py` 纳入并写进 schema/USAGE，deck 可直接出视频分镜帧。
4. **用真实文件替换重建**：deck 引擎与 `blue-professional` 主题用仓库真身；其余 3 主题以其 `design.md` 完整设计系统承载（这也正是原仓库「先读 design.md 再生成」的用法）。
5. **统一离线策略**：page 强离线、无外链字体；deck 主题允许 Google Fonts（否则丢失 Space Grotesk 等签名字体），并提供 `export.offline` 一键回退系统字体栈。
6. **统一引擎模型**：采用仓库实际发布的 `.deck` 视口模型（vw/vh/clamp）；`viewport-base.css` 的 1920×1080 固定舞台模型作为替代方案保留在 `references/frontend-slides/`。导出时截图脚本把视口设为 1920×1080，`.deck` 模型即像素级出图，无需强制固定舞台。
7. **保真护栏上升为规则**：把 B 的「不换字体/不改配色/不删装饰/不混主题/缺版式就地设计」写进 `checklist.md` 与 `AGENTS.md`。
8. **合规**：`NOTICE.md` / `LICENSE` 同时致谢 juanjuanjie 与 Zara Zhang，并标注 A 的来源；沿用 MIT。

## 五、已知限制

- HTML 真身：`presentation.html`（≈purple-gold 引擎）与 `blue-professional.html`；`blockframe`/`blockframe-dark`/`purple-gold` 的整页 HTML 未随上传送达。
- design.md 完整度：`blue-professional.design.md` 为完整版（设计令牌 frontmatter + 长篇正文）；其余 3 个含**完整设计令牌**（配色/字体/间距/组件/装饰/layout_rules/don't）但缺上游那段扩展正文。设计令牌已足以忠实为 deck 套用主题；按原仓库工作流「读 design.md 再构建」即可。
- 主题 `template.json` 中部分 tagline/best_for 字段在上游存在编码损坏（显示为 `????`）；本 skill 以 `design.md` / `preview.md` 的完整中文为准。
- 复杂视觉细节（暗金颗粒、极光流动、粗野硬阴影）是「尽量接近参考」，非像素级复刻。
