# 游戏迭代工作流规则索引

默认只读本索引。按命中条件读取具体规则。

| 文件 | read_when |
| --- | --- |
| `intake.md` | 需要判断游戏迭代输入、边界、写入位置和是否允许进入落文档或开发。 |
| `playable-loop-ui.md` | 需要把游戏想法拆成最小可玩循环、玩家界面、按钮、反馈和跳转。 |
| `ui-ux-development-spec.md` | 需要把玩法策划和界面拆分补成可直接指导 UI 开发的规格、组件规范和验收合同。 |
| `data-blueprint.md` | 需要补齐完整游戏数据模块、字段、引用关系、规模、数值基准和验收标准。 |
| `development-gate.md` | 需要判断是否满足进入开发，或需要补主任务、契约、子任务和验证计划。 |

## 组合读取规则

| 用户请求 | 必读文件 |
| --- | --- |
| 判断当前准备是否够 | `intake.md` + `development-gate.md` |
| 输出最小可玩循环 | `intake.md` + `playable-loop-ui.md` |
| 判断 UI 是否可开发 | `intake.md` + `playable-loop-ui.md` + `ui-ux-development-spec.md` |
| 输出数据蓝图 | `intake.md` + `data-blueprint.md` |
| 准备进入开发 | `intake.md` + `playable-loop-ui.md` + `ui-ux-development-spec.md` + `data-blueprint.md` + `development-gate.md` |
| 完整游戏迭代流程 | 本索引全部规则 |
