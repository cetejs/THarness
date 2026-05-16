# TASK-20260516-007-acceptance-asset-replacement

## 状态

- status: completed
- source: 用户要求替换正式资源并进行完整验收
- updated: 2026-05-16

## 目标

替换第一阶段原型占位资源，接入符合 v0.3 中国风手绘卡牌修仙方向的正式验收资源包，并准备完整验收所需的资源、运行时和验证记录。

## 范围

允许修改：

- `assets/` 下当前被 GameSpec 引用的卡牌框、图标、地图节点、状态图标和 UI 面板按钮资源。
- 资源生成脚本和资源清单。
- 必要的 UI 资源加载逻辑，让正式资源在运行时可见。
- 资源相关任务、契约、运行记录、验证记录和追溯记录。

## 禁止范围

- 不修改战斗数值、卡牌效果、地图节点顺序或奖励池逻辑。
- 不扩展新角色、新章节或新卡牌内容量。
- 不切换引擎或运行语言。
- 不引入外部不可追溯资源。
- 不把商业最终美术质量写成已达成事实。

## 成功标准

1. `assets/` 中所有 GameSpec 引用资源被验收版资源替换。
2. 卡牌框、UI 面板和按钮资源在运行时可见。
3. 资源尺寸、路径和引用验证通过。
4. C# 构建、Godot .NET 构建、数据验证、smoke 和编码检查通过。
5. 形成完整验收运行记录和资源预览图。

## 验证方式

- `python tools\generate_acceptance_assets.py`
- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-020-acceptance-asset-replacement-check` 验证。

## 子任务

- `SUB-20260516-015-acceptance-asset-pack`
- `SUB-20260516-016-runtime-asset-visibility`
- `SUB-20260516-017-acceptance-verification`
