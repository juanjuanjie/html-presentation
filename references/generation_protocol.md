# 生成协议（调用层）

> 把一次生成请求固定为：`mode + style_id + 结构 + content`。
> 结构：page 用 `layout_id`，deck 用 `slide_structure`。执行流程见根目录 `SKILL.md`。

## 处理顺序

1. 归一自然语言 → 标准 ID（`aliases.yaml`）。
2. 校验 `content`；page 校验 `style_id`，deck 校验 `theme_id`（缺→按 themes_index.json 匹配，兜底 `purple-gold-presentation`）。
3. 判定 `mode`（page / deck）。
4. 取风格 tokens / must_have / avoid / prompt_template（`styles.yaml`）。
5. 取结构 regions / pages（page 布局在 `styles.yaml`，deck 结构在 `slide_structures.yaml`）。
6. 按内容映射优先级把 `content` 落位。
7. 生成单文件 HTML（16:9 / 离线 / 无外链）。
8. 查 must_have 是否齐、avoid 是否触发（`checklist.md`）。
9. 输出 + match report。

## page 内容映射优先级

- **MFLEX**（`weekly_report_2x2` / `weekly_report_lr`）：标题栏 → 四象限或左右双栏 → 底部波浪 → 页码/元信息。
- **暗金**（`dark_gold_three_col`）：中心标题副标题 → 三栏主题 → 底部元信息。
- **Raw Paper**（`raw_paper_storyboard`）：左侧大标题 → 右侧纸张与拼贴块 → 标签区。
- **V2a**（`social_cover_v2a`）：左大标题 → 右白面板 → 层叠色块 → 三段信息。
- **V2b**（`social_dashboard_v2b`）：顶部标题栏 → 指标卡 → 进度区 → 动态列表 → 底部信息栏。
- **Aurora**（`aurora_cover` / `aurora_mix_panel`）：左标题区 → 右玻璃面板 → 光晕层叠卡片。

## deck 内容映射

- 按所选 `slide_structure` 的 `pages` 顺序逐页填 `content.pages[i]`；未显式给出时，从 `content.source_material` 拆成各页 `content_outline`。
- 每页要点 ≤ 5；页序不可乱。

## 输出约束

- 必须：单文件可离线打开、无外部字体/CDN、16:9、风格与 `style_id` 一致、结构与所选 layout/structure 一致。
- 默认：缺 `layout_id` 用 `default_layouts[0]`；缺 `slide_structure` 用 `defaults.structure`；缺字段用中性占位且告知用户。
- 禁止：擅自换风格、把风格做成固定单页模板、把内容强塞进错误结构。
