# 健康检查规则

## 状态

- status: active
- source: 项目适配层初始化
- updated: 2026-05-17

## 结论

实验二 wiki 健康检查只确认入口可达、来源明确、边界正确和低 token 检索成立。

## 最小检查

- `AIGC/wiki/INDEX.md` 存在。
- `INDEX.md` 只做路由，不复制正文。
- 可检索页面包含 `read_when` 或清晰入口说明。
- 项目事实有来源文件、验证记录或用户确认。
- 项目 wiki 没有写入通用 AIGC。
