# CHG-20260516-024-card-face-visual-upgrade

## 状态

- status: active
- type: change
- date: 2026-05-16
- source: 用户反馈当前卡面普通，并要求先总结问题到工作流再开始修改

## 背景

当前卡牌框虽然已经接入运行时，但卡牌身份主要靠边框颜色表达，卡面层级偏平，黑色信息块也容易被理解为占位。需要提升卡牌作为核心可收集对象的视觉识别度。

## 变更

| 范围 | 文件 | 说明 |
| --- | --- | --- |
| 通用工作流 | `THarness/AIGC/workflows/game-development-lifecycle/WORKFLOW.md` | 补充占位视觉、截图加真实输入、导入缓存原则。 |
| 通用工作流 | `THarness/AIGC/workflows/game-development-lifecycle/rules/ui-visual-runtime.md` | 补充占位 UI、核心卡面语义、截图和交互验收规则。 |
| 通用工作流 | `THarness/AIGC/workflows/game-development-lifecycle/rules/verification-and-retro.md` | 补充交互验证层级和复盘触发项。 |
| 资源生成 | `tools/generate_acceptance_assets.py` | 重做五套卡框，加入类型化主体纹样和更清晰卡面分区。 |
| UI 运行时 | `scripts/Main.cs` | 增加规则题签和卡面字体缩放。 |
| 验证脚本 | `tools/check_gdscript_sanity.py` | 增加卡面视觉结构回归检查。 |
| 设计记录 | `WorldSeed.AIGC/wiki/design/asset-acceptance-pack-v0.1.md` | 更新卡面验收风格要求。 |
| 运行记录 | `WorldSeed.AIGC/workflows/development/runs/RUN-20260516-014-card-face-visual-upgrade.md` | 记录工作流沉淀、卡面根因、修复和 Godot MCP 实测。 |

## 影响

- 攻击、护体、法诀、符箓、劫咒卡框具有不同主体纹样。
- 卡面去掉大面积黑色信息块，改为宣纸规则区。
- 卡面中部显示规则题签，不再重复卡名。
- 小卡字体随卡面缩放，降低标题和类型裁剪风险。

## 验证

已通过 `VER-20260516-025-card-face-visual-upgrade-check` 验证。
