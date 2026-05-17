# SUB-20260516-011-screen-contracts-1080p

## 状态

- status: draft
- source: TASK-20260516-006-gameplay-ui-alignment-rework
- updated: 2026-05-16

## 角色

UI 合同设计。

## 目标

把 v0.3 的 13 个界面效果图转换成 `1920x1080` 运行时界面合同，明确每个界面的区域比例、控件、按钮、数据来源、状态、跳转和截图验收标准。

## 允许读取入口

- `Experiments/EXP-001-worldseed/AIGC/wiki/design/ui-screen-visual-spec-v0.3.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/design/gameplay-ui-alignment-v0.1.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/development/contracts/CONTRACT-20260516-003-screen-runtime-parity.md`
- `data/game_spec/ascension_forge.prototype.json`

## 允许修改范围

- UI 合同文档。
- 对应任务、运行记录、验证记录和追溯记录。

## 禁止范围

- 不改 C# 运行时代码。
- 不改 GameSpec 业务数据。
- 不新增未确认界面。

## 成功标准

1. 每个界面都有目标设计稿路径和目标运行分辨率。
2. 每个界面都有区域比例、按钮动作、跳转和状态说明。
3. 每个界面都有实机截图验收要求和允许偏差。

## 验证方式

- 检查 13 个界面合同是否完整。
- 检查每个合同是否引用目标设计图和运行时截图要求。
- `python tools\check_text_encoding.py --root .`
