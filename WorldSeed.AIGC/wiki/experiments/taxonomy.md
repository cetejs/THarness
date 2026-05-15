# 实验类型

## 状态

- status: active
- source: 当前项目适配层规划
- updated: 2026-05-15

## 类型

| 类型 | 用途 | 典型验证 |
| --- | --- | --- |
| `gamespec` | 验证对话到 GameSpec 的结构化表达 | schema 校验、无效输入测试 |
| `godot-runtime` | 验证 Godot 工程、场景、脚本和导出链路 | headless 加载、主场景 smoke test |
| `gameplay` | 验证玩法循环、数值和交互反馈 | 输入模拟、状态断言、试玩记录 |
| `ui` | 验证 UI 生成、布局、状态和交互 | 截图、节点检查、输入反馈 |
| `asset-pipeline` | 验证图像、音频、动画资源生成和导入 | manifest、资源缺失检查 |
| `validation` | 验证自动测试、截图和报告链路 | 命令可复现、报告完整性 |
| `export` | 验证 Godot 导出和可分发包 | 导出命令、产物启动检查 |

## 规则

实验只能选择一个主类型。跨类型实验必须拆分，或明确主类型和辅助类型。

