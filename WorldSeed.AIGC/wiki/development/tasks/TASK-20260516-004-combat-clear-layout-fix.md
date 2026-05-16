# TASK-20260516-004-combat-clear-layout-fix

## 状态

- status: completed
- source: 用户提供 `[WorldSeed/UI]` 运行日志
- updated: 2026-05-16

## 目标

修复斗法界面多次刷新后 `content` 高度持续累积，导致界面下方被裁切的问题。

## 范围

- 修复 C# UI 清屏逻辑。
- 增加清屏节点数量日志。
- 更新静态回归检查。
- 补充问题记录、运行记录和追溯记录。

## 禁止范围

- 不改变玩法规则。
- 不改变 GameSpec 业务数据。
- 不新增界面或素材。

## 成功标准

1. 清屏时旧 UI 节点立即从父容器移除。
2. 同一帧重建斗法界面时旧节点不再参与布局计算。
3. 布局日志保留清屏节点数量。
4. 构建、结构、数据、闭环和编码验证通过。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
