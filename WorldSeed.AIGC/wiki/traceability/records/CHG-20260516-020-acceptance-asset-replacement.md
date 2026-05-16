# CHG-20260516-020-acceptance-asset-replacement

## 状态

- status: active
- source: 用户要求替换正式资源并进行完整验收
- updated: 2026-05-16

## 来源

用户确认当前流程测试基本没有问题，要求替换正式资源并进行完整验收。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 设计结论 | `WorldSeed.AIGC/wiki/design/asset-acceptance-pack-v0.1.md` | 定义第一阶段正式验收资源包。 |
| 开发任务 | `WorldSeed.AIGC/wiki/development/tasks/TASK-20260516-007-acceptance-asset-replacement.md` | 建立资源替换任务边界。 |
| 接口契约 | `WorldSeed.AIGC/wiki/development/contracts/CONTRACT-20260516-004-acceptance-assets.md` | 定义资源到运行时的交接契约。 |
| 资源 | `assets/` | 替换卡框、图标、节点、状态、UI 面板和按钮。 |
| 工具 | `tools/generate_acceptance_assets.py` | 资源包可重复生成。 |
| 运行时 | `scripts/Main.cs` | 让面板和按钮优先使用 GameSpec 中的 UI 纹理资源。 |
| 运行记录 | `WorldSeed.AIGC/workflows/development/runs/RUN-20260516-009-acceptance-asset-replacement.md` | 记录处理和验证结果。 |

## 影响范围

- 影响运行时可见 UI 资源。
- 不改变战斗数值、卡牌效果、地图顺序、奖励池逻辑或语言运行时。

## 验证方式

- `python tools\generate_acceptance_assets.py`
- `dotnet build WorldSeed.csproj`
- 资源尺寸检查。
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_gdscript_sanity.py`
- Godot .NET console 构建和 headless 启动。
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-020-acceptance-asset-replacement-check` 验证。

## 是否晋升为项目事实

是。当前第一阶段原型已接入正式验收资源包，后续完整验收应以该资源包为基础。
