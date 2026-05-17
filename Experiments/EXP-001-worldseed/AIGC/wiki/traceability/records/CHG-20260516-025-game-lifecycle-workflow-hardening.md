# CHG-20260516-025-game-lifecycle-workflow-hardening

## 状态

- status: active
- source: 用户要求把通用工作流是否足够支撑开发的分析经验沉淀下去
- updated: 2026-05-16

## 来源

本次来源于对 WorldSeed 开发过程的复盘：截图正确但真实交互失败、素材替换需要导入缓存策略、界面合同需要明确 hitbox 和缩放验收、开发前门禁需要集中核对。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 通用工作流 | `THarness/AIGC/workflows/game-development-lifecycle/WORKFLOW.md` | 增加素材管线合同和开发前硬门禁阶段。 |
| 通用规则 | `THarness/AIGC/workflows/game-development-lifecycle/rules/stage-gates.md` | 增加开发前硬门禁清单。 |
| 通用规则 | `THarness/AIGC/workflows/game-development-lifecycle/rules/ui-visual-runtime.md` | 增加 hitbox、真实输入、素材管线合同和 UI 完成判定要求。 |
| 通用规则 | `THarness/AIGC/workflows/game-development-lifecycle/rules/verification-and-retro.md` | 增加真实输入和 hitbox 证据要求。 |
| 通用模板 | `THarness/AIGC/workflows/game-development-lifecycle/templates/development-readiness-checklist.md` | 新增开发前硬门禁模板。 |
| 通用模板 | `THarness/AIGC/workflows/game-development-lifecycle/templates/asset-pipeline-contract.md` | 新增素材管线合同模板。 |
| 通用模板 | `THarness/AIGC/workflows/game-development-lifecycle/templates/screen-contract.md` | 增加交互命中区、禁止遮挡区域和滚动策略字段。 |
| 通用模板 | `THarness/AIGC/workflows/game-development-lifecycle/templates/verification-retro.md` | 增加交互验证和关键控件证据字段。 |
| 能力索引 | `THarness/AIGC/capabilities/` | 将 `game-development-lifecycle` 登记为通用能力并升级版本记录到 `2.4.0`。 |
| 自检 | `THarness/tools/test_oneharness.py` | 增加工作流硬化字段回归检查。 |

## 影响范围

- 影响后续游戏项目进入开发、UI 落地、素材替换和交付验收的通用门控。
- 不修改 WorldSeed 游戏运行时代码、玩法数据或素材。
- 不把 WorldSeed 具体项目路径、截图或数值写入 THarness。

## 验证方式

- `python THarness\tools\test_oneharness.py`
- `python tools\check_text_encoding.py --root .`
- `git diff --check`

## 验证结果

已通过 `VER-20260516-026-game-lifecycle-workflow-hardening-check` 验证。

## 是否晋升为项目事实

是。WorldSeed 后续继续开发前，应使用加固后的通用游戏开发生命周期工作流进行准备检查和交付验收。
