# SUB-20260516-016-runtime-asset-visibility

## 状态

- status: completed
- source: TASK-20260516-007-acceptance-asset-replacement
- updated: 2026-05-16

## 角色

Godot .NET UI 资源接入。

## 目标

让正式验收资源在运行时可见，至少覆盖卡牌框、面板和按钮三类玩家高频看到的 UI 资源。

## 允许读取入口

- `scripts/Main.cs`
- `data/game_spec/ascension_forge.prototype.json`
- `assets/`
- `WorldSeed.AIGC/wiki/development/contracts/CONTRACT-20260516-004-acceptance-assets.md`

## 允许修改范围

- `scripts/Main.cs`
- 必要的 `ui_visual` 或 `assets` 配置字段。
- 对应运行记录、验证记录和追溯记录。

## 禁止范围

- 不改变界面跳转。
- 不改变玩法规则。
- 不在 UI 代码中硬编码资源路径。
- 不新增 C# 业务类。

## 成功标准

1. 面板优先使用 `assets.ui.panel` 纹理。
2. 按钮优先使用 `assets.ui.button_*` 纹理。
3. 纹理缺失时保留现有平面样式回退。
4. C# 构建通过。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-020-acceptance-asset-replacement-check` 验证。
