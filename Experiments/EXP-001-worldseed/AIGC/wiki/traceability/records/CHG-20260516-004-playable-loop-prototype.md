# CHG-20260516-004-playable-loop-prototype

## 状态

- status: active
- source: 用户确认进入开发
- updated: 2026-05-16

## 来源

- 用户请求：基于已准备内容进行游戏开发，中途不介入，直到游戏可以玩。
- 关联需求：`TASK-20260516-001-game-data-runtime-prep`
- 关联决策：第一阶段范围为 1 角色、1 章、1 Boss 的完整链路。
- 关联实验：试制 UI 素材包作为第一阶段占位素材。
- 关联开发任务：`TASK-20260516-001-game-data-runtime-prep`

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| GameSpec 数据 | `data/game_spec/ascension_forge.prototype.json` | 提供第一阶段角色、卡牌、敌人、地图、奖励、UI 流程、素材引用和 UI 视觉布局参数。 |
| Godot 主场景 | `scenes/main.tscn` | 提供项目运行入口。 |
| Godot 脚本 | `scripts/GameSpecLoader.gd` | 读取并索引 GameSpec 数据。 |
| Godot 脚本 | `scripts/GameRuntime.gd` | 驱动局内状态、战斗、奖励、事件、商店和构筑。 |
| Godot 脚本 | `scripts/Main.gd` | 构建主菜单、角色选择、地图、战斗、奖励、构筑和结算 UI，并渲染占位美术素材与反馈闪烁。 |
| 素材 | `assets/` | 导入第一阶段可用占位 UI、卡框、图标、地图节点和状态图标。 |
| 验证工具 | `tools/validate_game_spec.py` | 验证 GameSpec 数据引用和素材引用。 |
| 验证工具 | `tools/smoke_playable_loop.py` | 验证第一阶段地图节点和奖励链路。 |
| 验证工具 | `tools/check_gdscript_sanity.py` | 检查 GDScript 主场景配置和已知编译风险模式。 |
| 项目配置 | `project.godot` | 设置主场景和 1280x720 视口。 |
| 说明文档 | `README.md` | 补充当前可玩原型运行方式和验证命令。 |
| 运行记录 | `WorldSeed.AIGC/workflows/development/runs/RUN-20260516-001-playable-loop-development.md` | 记录本轮开发目标和边界。 |
| 问题记录 | `WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md` | 记录开发中问题和处理。 |

## 影响范围

- 新增第一阶段 Godot 可玩原型。
- 主要界面已使用导入的 UI 面板、按钮纹理、卡框、资源图标、地图节点图标和状态图标。
- 不影响 THarness 通用工作流。
- 不实现联机、后期地图、自动生成器或完整多章节内容。

## 验证方式

- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_gdscript_sanity.py`
- `python tools\check_text_encoding.py --root .`
- 工程结构静态检查。

## 验证结果

已通过 `VER-20260516-004-playable-loop-prototype-check` 验证。

## 是否晋升为项目事实

是。第一阶段最小可玩闭环原型已落地。

## 后续事项

- 在具备 Godot 命令行环境后补充 headless 启动验证。
- 后续迭代可扩展更多角色、章节、卡牌和正式美术。
