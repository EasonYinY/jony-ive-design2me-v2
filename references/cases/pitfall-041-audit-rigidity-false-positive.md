---
reference_id: PITFALL-041
title: Pitfall 041 · 验证脚本僵化报"计划外 reference"
category: case
used_when:
  - KB-MIRROR
  - SKILL-AUDIT
  - EXTERNAL-KB-SYNC
called_by:
  - skill-router
  - upstream-knowledge-curator
depends_on:
  - REF-HYGIENE-001
  - REF-GUIDE-MIRROR
outputs:
  - audit_whitelist_failure_mode
---

# Pitfall 041 · 验证脚本僵化报"计划外 reference"(audit-rigidity-false-positive)

> **触发版本**:jony-ive-design2me-旧版→ 当前版本
> **触发日期**:2026-06-22
> **触发场景**:镜像外部知识库到 `references/<mirror-dir>/` 后,跑 `scripts/audit_references.py` 报 209 个"存在计划外运行 reference"失败
> **症状**:3 个验证脚本都通过 KB 白名单解决了,但**脚本本身的僵化逻辑**(REQUIRED_REFERENCES 固定 37 个)才是根因

## 症状

执行"外部知识库镜像"任务后,完成 A 阶段(字节级复制)和 B 阶段(运行 reference 接入)后,跑验证脚本:

```
$ python3 scripts/audit_references.py . SOURCE_LEDGER.csv
失败:存在计划外运行 reference:guides/external-knowledge-mirror-integration.md
失败:存在计划外运行 reference:changelogs/当前版本-changelog.md
失败:存在计划外运行 reference:changelogs/当前版本-changelog.md
... (209 个全部是 （后续版本） 新增的 guides/rules/cases/changelogs)
```

## 根因(诚实反查)

| 占比 | 原因 |
|---|---|
| **50%** | audit_references.py 的逻辑:`actual_names != REQUIRED_REFERENCES` → 任何 （后续版本） 新增的 reference 都被报"计划外"。REQUIRED_REFERENCES 仍是 v1.x 时代定义的 37 个固定文件 |
| **25%** | validate_skill.py 的 FORBIDDEN_RUNTIME_TEXT/FORBIDDEN_RUNTIME_PATTERNS 扫描**所有** references/*.md,KB 原文(含 `LoveFrom 2030`、`V4.x` 等 case-study 真实内容)触发误报 |
| **15%** | validate_reference_graph.py 的 fail-fast 设计:第一个无 frontmatter 的文件就抛错,无法"部分加载" |
| **10%** | 没有统一的"上游镜像目录白名单"机制,每个脚本各自重复实现 |

## 完成定义(正解)

镜像接入到**运行 reference 闭环**后,验证脚本必须满足:

| 脚本 | 目标 |
|---|---|
| `validate_skill.py` | KB 路径 0 失败(其他预先失败不变) |
| `validate_reference_graph.py` | KB 路径 0 失败(fail-fast 不抛错) |
| `audit_references.py` | KB 路径 0 失败 + 镜像接入工具(mirror guide)0 失败 + 版本变更记录(changelogs/)0 失败 |

## 修复方法(白名单补丁)

### 1. validate_skill.py 加 KB 白名单常量

```python
# 上游知识蒸馏镜像目录白名单:references/knowledge-base/ 下的 .md 不参与运行 reference 检查
UPSTREAM_KB_DIR = "knowledge-base"
```

并在 markdown 扫描循环里 skip:

```python
rel_posix = markdown_path.relative_to(root).as_posix()
if rel_posix.startswith(f"references/{UPSTREAM_KB_DIR}/"):
    continue
```

### 2. validate_reference_graph.py 加共享判断函数

```python
def _is_upstream_kb(path: Path, skill_root: Path) -> bool:
    return path.relative_to(skill_root).as_posix().startswith(f"references/{UPSTREAM_KB_DIR}/")
```

在 `load_reference_graph` 和 `_link_and_workflow_issues` 两处调用。

### 3. audit_references.py 同时加 KB 白名单 + 工具白名单

```python
from validate_skill import (UPSTREAM_KB_DIR, _local_link_issues, ...)
from validate_reference_graph import _is_upstream_kb

# KB 目录跳过
reference_paths = tuple(p for p in reference_paths if not _is_upstream_kb(p, skill_root))

# changelogs/ + mirror guide 是工具类文件,不参与"业务 reference 集合"校验
_AUDIT_EXEMPT_PATHS = frozenset({
    "changelogs/",
    "guides/external-knowledge-mirror-integration.md",
})
```

## 教训

1. **不要等"先有 script bug 后修"**——每次镜像任务前先 patch 3 个脚本加 KB 白名单常量
2. **REQUIRED_REFERENCES 应当可扩展**——当前版本+ 大量新增 guides/rules/cases 后,该字段应当改为读取 references/README.md 总索引表动态生成
3. **白名单常量集中在 validate_skill.py 导出**——避免每个脚本各写一份 `_is_upstream_kb`

## 关联

- 修复记录: jony-ive-design2me-v2 changelog
- 上游协议: `references/guides/external-knowledge-mirror-integration.md`(阶段 C 验证)
- Pitfall 040: 内容镜像未接入引用闭环(B 阶段缺失)
- Pitfall 042: KB 不进 graph 的正确解法(本会话 当前版本 的特殊处理)