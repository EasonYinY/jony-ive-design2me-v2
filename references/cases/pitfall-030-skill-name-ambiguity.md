---
reference_id: PITFALL-030-02
title: 技能名称歧义处理
category: cases
used_when:
  - 技能加载失败
  - 多版本技能冲突
  - skill_view 拒绝猜测
called_by:
  - skill_view
  - skill_manage
depends_on:
  - REF-PROCESS-001
outputs:
  - skill_name_resolution
---

# Pitfall 030: 技能名称歧义处理

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 执行 `skill_view(name="jony-ive-design2me-v2")` 时返回 "Ambiguous skill name" 错误
> **严重级别**: 🟡 中

---

## 问题描述

当技能目录存在多个备份版本（如 `-BACKUP-当前版本-20260621-134945`）时，`skill_view` 会拒绝猜测并要求显式路径。

### 错误示例

```
skill_view(name="jony-ive-design2me-v2")

# 返回错误:
Ambiguous skill name 'jony-ive-design2me-v2': 3 skills match across your local skills dir and external_dirs.
Refusing to guess — load one explicitly by its categorized path.

matches:
- /Users/easoneason/.hermes/skills/creative/jony-ive-design2me-v2-BACKUP-当前版本-20260621-134945-BACKUP-当前版本-20260621-150429/SKILL.md
- /Users/easoneason/.hermes/skills/creative/jony-ive-design2me-v2-BACKUP-当前版本-20260621-134945/SKILL.md
- /Users/easoneason/.hermes/skills/creative/jony-ive-design2me-v2/SKILL.md
```

---

## 根因分析

1. **备份版本累积**: 技能升级过程中自动生成的备份目录未清理
2. **名称匹配**: 所有备份名称包含原始技能名，导致模糊匹配
3. **拒绝猜测**: Hermes 设计为拒绝猜测，要求显式路径

---

## 解决方法

### 方法1: 使用完整分类路径（推荐）

```python
# ✅ 正确
skill_view(name="creative/jony-ive-design2me-v2")

# ❌ 错误
skill_view(name="jony-ive-design2me-v2")
```

### 方法2: 清理备份目录

```bash
# 删除旧备份
rm -rf ~/.hermes/skills/creative/jony-ive-design2me-v2-BACKUP-*

# 验证清理结果
ls ~/.hermes/skills/creative/ | grep jony-ive-design2me-v2
```

### 方法3: 使用 skill_view 的 file_path 参数

```python
# 直接读取特定文件
skill_view(name="creative/jony-ive-design2me-v2", file_path="references/process/end-to-end-workflow.md")
```

---

## 预防措施

1. **定期清理**: 每轮迭代结束后清理旧备份
2. **版本管理**: 使用 git 管理技能版本，而非文件系统备份
3. **命名规范**: 避免在技能名中使用连字符和版本号混合

---

## 检查清单

```
[ ] 技能名称是否唯一？
[ ] 是否存在备份目录冲突？
[ ] 是否使用完整分类路径？
[ ] 是否需要清理旧备份？
```

---

## 来源

- 技能: jony-ive-design2me-v2
- 触发: 2026-06-21 执行 skill_view 时
- 解决: 使用完整分类路径 `creative/jony-ive-design2me-v2`
