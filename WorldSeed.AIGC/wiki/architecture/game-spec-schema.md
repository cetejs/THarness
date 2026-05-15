# GameSpec Schema

## 状态

- status: draft
- source: 当前方案判断
- updated: 2026-05-15

## 结论

GameSpec 是 WorldSeed 从对话到 Godot 工程之间的中间表示。

## 初始分区

| 分区 | 用途 |
| --- | --- |
| `metadata` | 项目名、版本、目标平台和生成策略。 |
| `world` | 世界设定、场景列表和空间关系。 |
| `gameplay` | 核心循环、规则、胜负或推进条件。 |
| `ui` | 菜单、HUD、交互面板和状态展示。 |
| `stats` | 数值、公式、成长和可调参数。 |
| `audio` | 音效、音乐、音频事件和混音分组。 |
| `animation` | 动画状态、触发条件和过渡。 |
| `assets` | 资源清单、占位资源和生成资源引用。 |
| `validation` | 自动验证目标和手动验收项。 |

## 验证

第一版 schema 必须能校验有效输入和无效输入。

