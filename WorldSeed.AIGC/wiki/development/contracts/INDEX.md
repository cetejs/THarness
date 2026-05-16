# 接口契约索引

| 契约 | 状态 | 说明 |
| --- | --- | --- |
| `CONTRACT-20260516-001-gamespec-runtime.md` | draft | GameSpec 数据层到 Godot 运行时的交接契约。 |
| `CONTRACT-20260516-002-csharp-runtime-entry.md` | active | Godot .NET/C# 运行时入口契约。 |
| `CONTRACT-20260516-003-screen-runtime-parity.md` | active | v0.3 设计稿到 1920x1080 运行时界面的对齐契约。 |
| `CONTRACT-20260516-004-acceptance-assets.md` | active | 第一阶段正式验收资源包到 Godot 运行时的资源契约。 |

## 规则

- 生成器、GameSpec、Godot 运行时、资产管线和验证器之间必须通过契约交接。
- 契约必须包含输入、输出、错误处理、验证方式和禁止事项。
