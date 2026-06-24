---
reference_id: REF-CASE-049
title: Pitfall 049 - Skill Backup Version Clutter
category: cases
used_when:
  - SKILL-MANAGEMENT
  - SKILL-UPGRADE
called_by:
  - skill-hygiene
  - file-hygiene
depends_on:
  - REF-HYGIENE-001
outputs:
  - cleanup_protocol
  - user_preference
---

# Pitfall 049: Skill Backup Version Clutter

> **日期**: 2026-06-24
> **触发**: 用户明确指示"只有一个最新版本，其他版本全删除"
> **严重级别**: MEDIUM — 影响技能加载和版本管理

## 现象

技能目录中存在多个备份版本：

```
~/.hermes/skills/creative/
├── jony-ive-design2me-v2
├── jony-ive-design2me-v2-BACKUP-v1.1.0-20260621-134945
├── jony-ive-design2me-v2-BACKUP-v1.1.0-20260621-134945-BACKUP-v1.1.1-20260621-150429
└── jony-ive-design2me-v2-BACKUP-v1.1.x-20260624-110000-before-mouse-archetype-prior-upgrade
```

## 问题

1. `skill_view` 加载时可能选择错误版本（BACKUP 而非最新）
2. 用户混淆：不清楚哪个是"当前使用"的版本
3. 磁盘空间浪费
4. 版本号混乱：BACKUP 目录名中包含旧版本号，与 SKILL.md 中的实际版本不一致

## 用户明确立场

> "只有一个最新版本，其他版本全删除"

- ❌ 不要保留多个备份版本
- ❌ 不要创建带 BACKUP 后缀的目录
- ✅ 只保留一个最新版本目录
- ✅ 版本历史通过 git 管理（如果技能目录是 git 仓库）
- ✅ 版本变更记录写入 `references/changelogs/`

## 清理协议

### 立即执行（当用户明确要求时）

```bash
# 1. 确认最新版本目录
ls -la ~/.hermes/skills/creative/ | grep jony-ive-design2me-v2

# 2. 删除所有 BACKUP 目录
rm -rf ~/.hermes/skills/creative/jony-ive-design2me-v2-BACKUP-*

# 3. 验证只剩一个
ls -la ~/.hermes/skills/creative/ | grep jony-ive-design2me-v2
# 期望输出: 只有 jony-ive-design2me-v2 一行
```

### 预防措施

1. **升级时直接覆盖**：修改 SKILL.md 和 references/ 文件，不创建新目录
2. **使用 git 管理版本**：如果技能目录是 git 仓库，通过 git log 查看历史
3. **changelog 记录变更**：所有版本历史写入 `references/changelogs/vX.Y.Z-changelog.md`
4. **避免手动复制备份**：不要手动 `cp -r skill skill-BACKUP-xxx`

## 检查清单

- [ ] 技能目录下是否只有一个版本？（无 BACKUP/OLD/backup 等后缀）
- [ ] SKILL.md frontmatter 中的 version 是否与目录名一致？
- [ ] 版本历史是否已写入 changelog 文件？

## 来源

- 2026-06-24 用户明确指示"只有一个最新版本，其他版本全删除"
- REF-HYGIENE-001: 文件卫生铁律与增量更新规范
