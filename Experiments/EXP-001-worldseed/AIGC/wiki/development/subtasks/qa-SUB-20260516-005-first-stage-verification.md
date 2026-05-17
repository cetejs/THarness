# SUB-20260516-005-first-stage-verification

## 状态

- status: draft
- source: TASK-20260516-001-game-data-runtime-prep
- updated: 2026-05-16

## 角色

验证设计。

## 目标

定义第一阶段进入实现后的验收方式，确保数据链路、UI 跳转、素材引用和最小可玩循环可以被检查。

## 允许读取入口

- `Experiments/EXP-001-worldseed/AIGC/wiki/design/game-data-blueprint-v0.1.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/design/playable-game-requirements.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/development/tasks/TASK-20260516-001-game-data-runtime-prep.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/development/contracts/CONTRACT-20260516-001-gamespec-runtime.md`

## 允许修改范围

后续进入开发后，仅允许修改验证计划、验收清单和验证记录。

## 范围

- 数据完整性检查。
- ID 引用检查。
- UI 跳转检查。
- 素材引用检查。
- 最小一局流程检查。
- 无效输入反馈检查。

## 禁止范围

- 不替代实际代码测试。
- 不把未运行的验证写成已通过。
- 不使用实验结果冒充正式验收。

## 验证方式

- 验收清单能覆盖主菜单到结算的完整链路。
- 每个失败条件都有可观察反馈。
- 验证结果必须写入追溯记录。
