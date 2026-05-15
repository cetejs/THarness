# CHG-20260515-004 编码读取和检查机制

## 状态

- status: active
- source: 用户反馈
- updated: 2026-05-15

## 来源

- 用户请求：阅读过程中容易出现编码错误，需要修复这类问题。
- 关联需求：无
- 关联决策：无
- 关联实验：无
- 关联开发任务：无

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 配置 | `.editorconfig` | 约束编辑器默认使用 UTF-8。 |
| 配置 | `.gitattributes` | 约束 Git 文本归一化和常见二进制文件。 |
| 工具 | `tools/read_utf8.ps1` | 提供 PowerShell 稳定读取 UTF-8 中文文本的入口。 |
| 工具 | `tools/check_text_encoding.py` | 扫描非 UTF-8 文本和常见中文乱码标记。 |
| 文档 | `WorldSeed.AIGC/wiki/rules/encoding.md` | 建立项目编码规则。 |

## 影响范围

- 后续 AI 和人工读取中文文档时有统一命令。
- 后续交付前可运行编码检查，避免乱码进入仓库。
- 项目验证流程新增编码检查。

## 验证方式

- 运行 `python tools\check_text_encoding.py`。
- 使用 `tools/read_utf8.ps1` 读取中文入口文档。
- 运行 `THarness` 门控和单元测试。

## 验证结果

见 `VER-20260515-002-encoding-check.md`。

## 是否晋升为项目事实

是。编码规则是当前项目正式开发约束。

## 后续事项

- 后续可将编码检查接入自动门控脚本。

