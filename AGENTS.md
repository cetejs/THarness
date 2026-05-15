# WorldSeed AI 开发入口

本文件是本仓库所有 AI 开发、文档、验证和架构讨论的强制入口。

## 必须读取

任何 AI 在处理本仓库任务前，必须先读取：

1. `WorldSeed.AIGC/INDEX.md`
2. `WorldSeed.AIGC/ADAPTER.md`
3. `WorldSeed.AIGC/wiki/INDEX.md`

需要通用工作流规则时，再按 `WorldSeed.AIGC/ADAPTER.md` 指向的 `THarness/AIGC` 入口读取。

## 编码要求

- 本仓库文本文件统一使用 UTF-8。
- PowerShell 读取中文文件时必须使用 `-Encoding UTF8`，并设置输出编码。
- 推荐使用 `tools/read_utf8.ps1` 读取中文文本，例如：

```powershell
powershell -ExecutionPolicy Bypass -File tools\read_utf8.ps1 -Path WorldSeed.AIGC\INDEX.md -Raw
```

- 交付前需要运行 `python tools\check_text_encoding.py`，确认没有非 UTF-8 或疑似乱码文本。

## 写入边界

- WorldSeed 项目事实、决策、开发任务、接口契约、运行记录和验证记录只能写入 `WorldSeed.AIGC/`。
- 通用 AIGC 工作流、通用规则、通用模板和通用架构知识只能写入 `THarness/AIGC/`。
- 临时过程、失败尝试和命令输出只能写入 `WorldSeed.AIGC/workflows/*/runs/`，不能写入正式 wiki 正文。
- 实验计划、实验输入、生成产物、日志和实验报告必须写入 `WorldSeed.Experiments/`。
- 实验稳定结论只有经过复核后，才能摘要写入 `WorldSeed.AIGC/wiki/experiments/` 或对应正式 wiki 页面。
- 正式新增文件、正式新增目录、正式新增设计结论和正式新增开发任务必须登记到 `WorldSeed.AIGC/wiki/traceability/records/`。
- 未确认内容只能写入 `WorldSeed.AIGC/wiki/open-questions.md`，不能写成已确认事实。

## 开发约束

- 没有项目 wiki 开发任务页，不进入代码实现。
- 没有接口契约，不做跨模块修改。
- 没有验证方式，不标记任务完成。
- 实验不能替代正式开发任务；实验结论不能自动晋升为项目事实。
- 没有 `CHG` 记录，不新增正式项目内容。
- 不允许使用未声明编码的读取或写入方式处理中文项目文档。
- 不允许从历史对话、个人记忆或全仓扫描直接开始开发。
- 所有输出、注释和项目文档默认使用简体中文。
