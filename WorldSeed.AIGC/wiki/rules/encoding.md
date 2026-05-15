# 编码规则

## 状态

- status: active
- source: 用户反馈和当前编码修复
- updated: 2026-05-15

## 结论

本仓库文本文件统一使用 UTF-8。读取中文文件时必须显式指定 UTF-8，避免 Windows PowerShell 默认编码导致乱码。

## 读取规则

PowerShell 推荐使用：

```powershell
powershell -ExecutionPolicy Bypass -File tools\read_utf8.ps1 -Path WorldSeed.AIGC\INDEX.md -Raw
```

直接读取时必须使用：

```powershell
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
Get-Content -Raw -Encoding UTF8 <path>
```

## 写入规则

- Python 写入文本必须显式使用 `encoding="utf-8"` 或 `encoding="utf-8-sig"`。
- PowerShell 写入中文文本必须显式使用 UTF-8。
- 禁止用未声明编码的脚本批量改写中文文档。

## 检查命令

```powershell
python tools\check_text_encoding.py
```

## 验证

编码检查通过，且未发现常见中文乱码标记。

