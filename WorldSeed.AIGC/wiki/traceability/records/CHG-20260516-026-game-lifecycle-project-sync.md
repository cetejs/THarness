# CHG-20260516-026-game-lifecycle-project-sync

## 状态

- status: active
- source: 用户要求继续完善工作流并补充本轮开发经验
- updated: 2026-05-16

## 来源

本次来源于对 WorldSeed 工作流执行状态的复盘：通用游戏开发生命周期工作流已经补强，但目标项目适配层中的当前工作流、状态页、构建运行入口、任务状态和运行记录索引可能没有同步更新。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 通用工作流 | `THarness/AIGC/workflows/game-development-lifecycle/WORKFLOW.md` | 增加项目侧执行同步阶段、原则和完成标准。 |
| 通用规则 | `THarness/AIGC/workflows/game-development-lifecycle/rules/stage-gates.md` | 增加项目侧执行同步门禁。 |
| 通用规则 | `THarness/AIGC/workflows/game-development-lifecycle/rules/verification-and-retro.md` | 增加项目侧同步检查要求。 |
| 通用模板 | `THarness/AIGC/workflows/game-development-lifecycle/templates/project-execution-sync-check.md` | 新增项目侧执行同步检查模板。 |
| 通用索引 | `THarness/AIGC/workflows/game-development-lifecycle/templates/INDEX.md` | 登记新增模板。 |
| 能力索引 | `THarness/AIGC/capabilities/` | 将系统版本升级到 `2.5.0`，并登记项目侧执行同步能力说明。 |
| 自检 | `THarness/tools/test_oneharness.py` | 增加项目侧同步门控字段回归检查。 |

## 影响范围

- 影响后续游戏项目交付和工作流升级后的收口检查。
- 不修改 WorldSeed 游戏运行时代码、玩法数据或素材。
- 不把 WorldSeed 当前具体路径、状态差异或验证命令写入 THarness 正文。

## 验证方式

- `python THarness\tools\test_oneharness.py`
- `python tools\check_text_encoding.py --root .`
- `git diff --check`

## 验证结果

已通过 `VER-20260516-027-game-lifecycle-project-sync-check` 验证。

## 是否晋升为项目事实

是。WorldSeed 后续执行完整界面验收或继续开发时，应先使用项目侧执行同步检查，确认项目入口、状态、验证入口、任务看板和追溯记录一致。
