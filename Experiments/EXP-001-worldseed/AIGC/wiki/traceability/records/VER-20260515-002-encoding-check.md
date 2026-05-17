# VER-20260515-002 编码检查

## 状态

- status: active
- source: 本轮命令验证
- updated: 2026-05-15

## 验证目标

确认项目文本文件可按 UTF-8 读取，未发现常见中文乱码，并确认通用 harness 未受影响。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 文本编码扫描 | `python tools\check_text_encoding.py` | 通过，扫描 258 个文本文件。 |
| UTF-8 读取工具 | `powershell -ExecutionPolicy Bypass -File tools\read_utf8.ps1 -Path WorldSeed.AIGC\wiki\rules\encoding.md -Raw` | 通过，中文内容正常输出。 |
| `THarness` 门控 | `python tools\oneharness.py gate` | 通过。 |
| `THarness` 单元测试 | `python -m unittest tools.test_oneharness` | 通过，8 个测试 OK。 |

## 局限

- 该检查只能发现解码失败和常见乱码标记，不能判断所有语义错误。

## 关联记录

- `CHG-20260515-004-encoding-guardrails`
