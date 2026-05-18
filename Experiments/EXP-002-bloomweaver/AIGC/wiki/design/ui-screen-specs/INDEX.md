# UI 单界面开发规格案索引

## 状态

- status: active
- source: 用户确认的 UI 开发策划输出要求
- updated: 2026-05-17

## 结论

本目录保存单个界面的完整 UI 开发规格案。这里的文档用于交给程序施工和 QA 验收，不替代 `migration-gdd/screens/` 中的玩法流程策划案。

## 内容

| 文件 | read_when |
| --- | --- |
| `main-menu-ui-spec.md` | 需要按主界面效果图实现、评审或验收主界面 UI 时读取。 |

## 验证

新增或修改本目录文档后，需要更新 `../INDEX.md` 和 `../../traceability/records/INDEX.md`，并运行 `python tools/check_text_encoding.py`。
