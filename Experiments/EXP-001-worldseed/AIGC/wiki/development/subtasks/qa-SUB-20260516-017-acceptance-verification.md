# SUB-20260516-017-acceptance-verification

## 状态

- status: completed
- source: TASK-20260516-007-acceptance-asset-replacement
- updated: 2026-05-16

## 角色

完整验收验证。

## 目标

验证正式验收资源替换后，工程仍能构建、数据引用完整、最小闭环可跑通，并给用户提供完整验收入口。

## 允许读取入口

- `tools/`
- `project.godot`
- `WorldSeed.csproj`
- `data/game_spec/ascension_forge.prototype.json`
- `Experiments/EXP-001-worldseed/AIGC/wiki/development/tasks/TASK-20260516-007-acceptance-asset-replacement.md`

## 允许修改范围

- 验证记录。
- 运行记录。
- 追溯记录。

## 禁止范围

- 不修改运行时代码。
- 不修改资源图像。

## 成功标准

1. 资源生成、数据验证、C# 构建、Godot 构建、headless 启动、smoke 和编码检查全部通过。
2. 验收运行命令明确。
3. 未验证或需要人工验收的视觉内容明确列出。

## 验证方式

- `python tools\generate_acceptance_assets.py`
- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`

## 验证结果

自动验证已通过；真实窗口视觉验收需要用户运行后确认。
