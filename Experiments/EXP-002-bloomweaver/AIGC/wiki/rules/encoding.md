# 编码规则

## 状态

- status: active
- source: 仓库入口规则
- updated: 2026-05-17

## 结论

实验二中文文本文件统一使用 UTF-8。

## 内容

- PowerShell 读取中文文件时必须设置 UTF-8 输出编码。
- 推荐使用仓库根目录 `tools/read_utf8.ps1` 读取中文文档。
- 交付前运行 `python tools/check_text_encoding.py`。
