# WorldSeed 项目适配配置

## 配置

```yaml
project_name: WorldSeed
project_root: D:\UnityDemo\WroldSeed
project_aigc_root: WorldSeed.AIGC
project_wiki_root: WorldSeed.AIGC/wiki
workflow_runs_root: WorldSeed.AIGC/workflows
general_harness_root: THarness/AIGC
active_workflow: project-wiki-maintenance
engine_target: Godot
created_at: 2026-05-15
```

## 调用规则

- 需要 WorldSeed 项目事实时，读取 `WorldSeed.AIGC/wiki/INDEX.md` 并按索引命中具体页面。
- 需要通用工作流规则时，读取 `THarness/AIGC/INDEX.md` 并按其工作流路由继续读取。
- 开发任务必须先写入 `WorldSeed.AIGC/wiki/development/tasks/`。
- 子任务必须写入 `WorldSeed.AIGC/wiki/development/subtasks/`。
- 跨模块接口必须写入 `WorldSeed.AIGC/wiki/development/contracts/`。
- 运行记录必须写入 `WorldSeed.AIGC/workflows/{workflow_id}/runs/`。

## 路径说明

当前仓库目录名是 `WroldSeed`，项目名是 `WorldSeed`。在实际路径中保留磁盘目录名，在项目文档中使用项目名。

