# GameAIGC AI 开发入口

本文件是本仓库所有 AI 开发、文档、验证和架构讨论的强制入口。

## 必须读取

任何 AI 在处理本仓库任务前，必须先读取：

1. `AIGC.Framework/INDEX.md`
2. `Experiments/INDEX.md`
3. `Experiments/EXP-001-worldseed/AIGC/INDEX.md`
4. `Experiments/EXP-001-worldseed/AIGC/ADAPTER.md`
5. `Experiments/EXP-001-worldseed/AIGC/wiki/INDEX.md`

只处理通用框架时，可以停在 `AIGC.Framework/`；只处理实验一项目事实时，必须进入实验一自己的 AIGC 适配层。

## 编码要求

- 本仓库文本文件统一使用 UTF-8。
- PowerShell 读取中文文件时必须使用 `-Encoding UTF8`，并设置输出编码。
- 推荐使用 `tools/read_utf8.ps1` 读取中文文本，例如：

```powershell
powershell -ExecutionPolicy Bypass -File tools\read_utf8.ps1 -Path AIGC.Framework\INDEX.md -Raw
```

- 交付前需要运行 `python tools\check_text_encoding.py`，确认没有非 UTF-8 或疑似乱码文本。

## 写入边界

- 通用游戏 AIGC 工作流、通用规则、通用模板、通用架构知识只能写入 `AIGC.Framework/`。
- 实验登记、实验入口和实验项目列表只能写入 `Experiments/`。
- 实验一项目事实、决策、开发任务、接口契约、运行记录和验证记录只能写入 `Experiments/EXP-001-worldseed/AIGC/`。
- 实验一 Godot 工程代码、数据、素材和项目专用工具只能写入 `Experiments/EXP-001-worldseed/project/`。
- 实验一输入材料写入 `Experiments/EXP-001-worldseed/inputs/`。
- 实验一生成产物、日志、截图和构建产物写入 `Experiments/EXP-001-worldseed/outputs/`。
- 实验一验证过程和报告写入 `Experiments/EXP-001-worldseed/validation/`。
- 实验一复盘候选经验写入 `Experiments/EXP-001-worldseed/retro/`。
- 实验稳定结论只有复核后，才能晋升到 `AIGC.Framework/` 或摘要写入实验一项目 wiki。
- 正式新增实验一项目内容必须登记到 `Experiments/EXP-001-worldseed/AIGC/wiki/traceability/records/`。
- 未确认内容只能写入对应实验项目的 `AIGC/wiki/open-questions.md` 或 `retro/framework-candidates.md`，不能写成已确认事实。

## 开发约束

- 没有实验项目 wiki 开发任务页，不进入代码实现。
- 没有接口契约，不做跨模块修改。
- 没有验证方式，不标记任务完成。
- 实验不能替代通用框架结论；实验结论不能自动晋升为通用规则。
- 没有 `CHG` 记录，不新增正式实验项目内容。
- 不允许使用未声明编码的读取或写入方式处理中文项目文档。
- 不允许从历史对话、个人记忆或全仓扫描直接开始开发。
- 所有输出、注释和项目文档默认使用简体中文。
