---
reference_id: REF-CHANGELOG-001
title: Changelog 索引与版本历史
category: changelogs
used_when:
  - VERSION-HISTORY
  - SKILL-UPGRADE-PLANNING
called_by:
  - skill-router
  - file-hygiene-check
depends_on:
  - NONE
outputs:
  - version_history_index
---

# Changelog 索引与版本历史

本目录存放 `jony-ive-design2me-v2` 的全部版本升级记录。遵循 **0 删除原则**：所有历史内容保留，新版本只追加。

## 版本列表

| 版本 | 文件 | 日期 | 核心变更 |
|---|---|---|---|
| v1.0.0 | [v1.0.0-changelog.md](v1.0.0-changelog.md) | 2026-06-20 | 初始发布，十五步工作流，五维引擎，DesignIR，八项审美质量门 |

## 命名规则

- 文件：`v{X.Y}-changelog.md`（例如 `v1.0.0-changelog.md`）
- **不要**带 skill 名前缀
- 每个版本独立文件，不合并

## 何时查阅

- 需要了解某个版本的具体变更内容
- 需要追溯某个规则/文件的引入版本
- 需要规划升级路径
