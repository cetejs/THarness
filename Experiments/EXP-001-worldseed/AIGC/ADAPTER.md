# EXP-001-worldseed 项目适配配置

## 配置

```yaml
project_name: WorldSeed
experiment_id: EXP-001-worldseed
repository_root: D:\UnityDemo\WroldSeed
experiment_root: Experiments/EXP-001-worldseed
project_root: Experiments/EXP-001-worldseed/project
project_aigc_root: Experiments/EXP-001-worldseed/AIGC
project_wiki_root: Experiments/EXP-001-worldseed/AIGC/wiki
workflow_runs_root: Experiments/EXP-001-worldseed/AIGC/workflows
general_harness_root: AIGC.Framework
active_workflow: project-wiki-maintenance
engine_target: Godot
created_at: 2026-05-15
```

## 调用规则

- 需要 WorldSeed 项目事实时，读取 `Experiments/EXP-001-worldseed/AIGC/wiki/INDEX.md` 并按索引命中具体页面。
- 需要通用工作流规则时，读取 `AIGC.Framework/INDEX.md` 并按其工作流路由继续读取。
- 开发任务必须先写入 `Experiments/EXP-001-worldseed/AIGC/wiki/development/tasks/`。
- 子任务必须写入 `Experiments/EXP-001-worldseed/AIGC/wiki/development/subtasks/`。
- 跨模块接口必须写入 `Experiments/EXP-001-worldseed/AIGC/wiki/development/contracts/`。
- 运行记录必须写入 `Experiments/EXP-001-worldseed/AIGC/workflows/{workflow_id}/runs/`。

## 路径说明

当前仓库目录名是 `WroldSeed`，实验名是 `EXP-001-worldseed`，项目名是 `WorldSeed`。Godot 工程位于实验目录的 `project/` 下。
