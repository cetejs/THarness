# BloomWeaver Wiki 页面格式

项目 wiki 页面默认使用以下结构。

```md
# 页面标题

## 状态

- status: draft / active / deprecated
- source: 用户确认 / 运行记录 / 代码扫描 / 外部资料
- updated: YYYY-MM-DD

## 结论

明确、可检索的当前结论。

## 内容

正文。

## 验证

说明该页面结论如何验证，或为什么当前无法验证。
```

## 规则

- 未确认内容必须标注为待确认，或写入 `open-questions.md`。
- 页面只保存稳定事实、约束和索引，不保存长命令输出。
- 开发任务、子任务和接口契约必须落在 `development/` 对应目录。
- 每个页面只承担一个清晰职责。
