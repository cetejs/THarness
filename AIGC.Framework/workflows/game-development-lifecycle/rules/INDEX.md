# 游戏开发生命周期规则索引

默认只读本索引。按命中条件读取具体规则。

| 文件 | read_when |
| --- | --- |
| `intake.md` | 需要判断本轮处于策划、准备、开发、排查、验证或复盘哪个阶段。 |
| `stage-gates.md` | 需要决定是否允许进入下一阶段，或判断当前准备是否足够。 |
| `vertical-slice.md` | 需要从完整游戏目标收敛到最小可玩垂直切片。 |
| `ui-visual-runtime.md` | 需要把界面效果图、素材和运行时 UI 落地，并处理窗口缩放、布局和截图校准。 |
| `debug-observability.md` | 需要处理反复出现的运行时问题，要求先加日志、复现和观测点。 |
| `verification-and-retro.md` | 需要完成交付前验证、失败记录、复盘和通用知识沉淀。 |

## 组合读取规则

| 用户请求 | 必读文件 |
| --- | --- |
| 总结或建立完整游戏开发流程 | 本索引全部规则 |
| 判断是否能开发 | `intake.md` + `stage-gates.md` |
| 从策划进入实现 | `stage-gates.md` + `vertical-slice.md` |
| 修 UI 和视觉差异 | `ui-visual-runtime.md` + `debug-observability.md` |
| 修反复出现的漏洞 | `debug-observability.md` + `verification-and-retro.md` |
| 开发结束交付 | `verification-and-retro.md` |
