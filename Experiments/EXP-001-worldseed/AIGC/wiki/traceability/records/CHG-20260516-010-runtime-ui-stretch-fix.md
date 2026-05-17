# CHG-20260516-010-runtime-ui-stretch-fix

## 状态

- status: active
- source: 用户实机截图反馈
- updated: 2026-05-16

## 来源

- 用户反馈：运行后游戏画面没有铺满窗口，启动界面周围出现黑边。
- 关联问题：`WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md` 中 `DEV-008`

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| Godot 项目配置 | `project.godot` | 增加 `window/stretch/mode="canvas_items"` 和 `window/stretch/aspect="expand"`，让画面随窗口扩展，避免固定 1280x720 居中黑边。 |
| Godot UI 脚本 | `scripts/Main.gd` | 启动时和 viewport 尺寸变化时强制根 `Control` 铺满 viewport。 |
| 验证工具 | `tools/check_gdscript_sanity.py` | 增加 stretch 配置回归检查。 |
| 问题记录 | `WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md` | 记录并关闭本次窗口铺满反馈。 |

## 影响范围

- 运行窗口拉伸、最大化和编辑器嵌入运行时的画面铺满行为。
- 不改变玩法规则、数据结构或界面流程。

## 验证方式

- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-010-runtime-ui-stretch-fix-check` 验证。

## 是否晋升为项目事实

是。当前 Godot 运行窗口应使用 stretch 扩展画面，不应在窗口放大时露出黑边。
