# SUB-20260516-013-runtime-rule-parity

## 状态

- status: draft
- source: TASK-20260516-006-gameplay-ui-alignment-rework
- updated: 2026-05-16

## 角色

玩法系统实现。

## 目标

修正当前运行时中与第一阶段玩法目标不一致的规则表达，使奖励、符箓嵌入、重复卡槽位、装备、天赋和状态效果能通过数据驱动闭合。

## 允许读取入口

- `scripts/GameRuntime.cs`
- `scripts/GameSpecLoader.cs`
- `data/game_spec/ascension_forge.prototype.json`
- `Experiments/EXP-001-worldseed/AIGC/wiki/design/game-data-blueprint-v0.1.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/design/gameplay-ui-alignment-v0.1.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/development/contracts/CONTRACT-20260516-001-gamespec-runtime.md`

## 允许修改范围

- `scripts/GameRuntime.cs`
- `scripts/GameSpecLoader.cs`
- `data/game_spec/ascension_forge.prototype.json`
- 玩法验证脚本。
- 对应运行记录、验证记录和追溯记录。

## 禁止范围

- 不做最终数值平衡。
- 不新增完整章节或多角色内容量。
- 不把装备、天赋、状态效果直接写成 UI 文案。
- 不在一个 C# 脚本文件中新增多个业务类。

## 成功标准

1. 奖励池能按规则生成三选一候选。
2. 符箓嵌入由玩家选择目标法门和槽位。
3. 重复卡有独立实例或等效可区分槽位状态。
4. 装备、天赋和状态效果至少覆盖当前样例数据中已出现的效果类型。
5. 无效选择有明确反馈。

## 验证方式

- `dotnet build WorldSeed.csproj`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- 针对奖励三选一、符箓嵌入、重复卡槽位、装备/天赋/状态效果的回归检查。
