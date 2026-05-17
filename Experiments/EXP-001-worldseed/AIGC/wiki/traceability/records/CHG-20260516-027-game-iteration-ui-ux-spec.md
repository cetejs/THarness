# CHG-20260516-027-game-iteration-ui-ux-spec

## 状态

- status: active
- source: 用户要求继续完善工作流并补充开发经验
- updated: 2026-05-16

## 来源

本次来源于 WorldSeed UI 开发复盘：只有玩法策划、界面名称或效果图时，仍不足以直接进入 UI 工程实现。UI 开发还需要目标视口、缩放策略、布局合同、组件规范、hitbox、素材边界和验收标准。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 通用工作流 | `THarness/AIGC/workflows/game-iteration/WORKFLOW.md` | 增加 UI/UX 可开发规格阶段和完成标准。 |
| 通用规则 | `THarness/AIGC/workflows/game-iteration/rules/ui-ux-development-spec.md` | 新增 UI/UX 可开发规格规则。 |
| 通用规则 | `THarness/AIGC/workflows/game-iteration/rules/INDEX.md` | 登记新增规则并更新组合读取规则。 |
| 通用规则 | `THarness/AIGC/workflows/game-iteration/rules/playable-loop-ui.md` | 明确界面拆分不等于 UI 工程规格。 |
| 通用规则 | `THarness/AIGC/workflows/game-iteration/rules/development-gate.md` | 将 UI/UX 可开发规格纳入进入 UI 或完整游戏实现的门控。 |
| 通用模板 | `THarness/AIGC/workflows/game-iteration/templates/ui-ux-development-spec.md` | 新增 UI/UX 可开发规格模板。 |
| 通用模板 | `THarness/AIGC/workflows/game-iteration/templates/` | 更新模板索引、最小可玩循环模板和开发门控模板。 |
| 能力索引 | `THarness/AIGC/capabilities/` | 将系统版本升级到 `2.6.0`，并登记 game-iteration 的 UI/UX 可开发规格能力。 |
| 自检 | `THarness/tools/test_oneharness.py` | 增加 game-iteration UI/UX 可开发规格路由回归检查。 |

## 影响范围

- 影响后续游戏想法从策划进入 UI 或完整游戏开发前的准备门控。
- 不修改 WorldSeed 游戏运行时代码、玩法数据或素材。
- 不把 WorldSeed 具体界面、数值、资源路径或截图写入 THarness。

## 验证方式

- `python THarness\tools\test_oneharness.py`
- `python tools\check_text_encoding.py --root .`
- `git diff --check`

## 验证结果

已通过 `VER-20260516-028-game-iteration-ui-ux-spec-check` 验证。

## 是否晋升为项目事实

是。WorldSeed 后续 UI 验收或 UI 重做前，应先确认 UI/UX 可开发规格是否完整，不能只凭玩法策划案或单张效果图进入实现。
