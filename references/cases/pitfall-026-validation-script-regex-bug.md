---
reference_id: REF-CASE-026-02
title: Pitfall 026 - 验证脚本正则表达式不匹配 PITFALL ID
category: cases
used_when:
  - SKILL-UPGRADE
  - VALIDATION
called_by:
  - skill-upgrade
  - validation
depends_on:
  - REF-HYGIENE-001
  - REF-CASE-025
outputs:
  - failure_pattern
---

# Pitfall 026 - 验证脚本正则表达式不匹配 PITFALL ID

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 新增 pitfall-024-form-first-failure.md 后运行 validate_skill.py 报错
> **严重级别**: MEDIUM

---

## 触发条件

1. 新增或修改 PITFALL-xxx 类型的 reference 文件
2. 运行 `validate_skill.py` 或 `validate_reference_graph.py`
3. 脚本报错："总索引 ID 不一致：缺少 ['PITFALL-002', 'PITFALL-003', ...]"
4. 错误原因：INDEX_REFERENCE 正则表达式只匹配 `REF-[A-Z0-9-]+`，不匹配 `PITFALL-\d+`

---

## 失败表现

- 验证脚本报告 60+ 个错误
- 所有错误指向 "步骤映射未引用" 或 "总索引 ID 不一致"
- 实际文件和索引都存在，但正则表达式过滤掉了 PITFALL ID

---

## 根因分析

### 根因: 正则表达式范围过窄（100%责任）

`validate_reference_graph.py` 第 24-25 行：
```python
INDEX_REFERENCE = re.compile(
    r"^\|\s*(REF-[A-Z0-9-]+)\s*\|\s*\[[^]]+\]\(([^)]+\.md)\)\s*\|"
)
```

问题：只捕获 `REF-...` 格式的 ID，不捕获 `PITFALL-...` 格式。

---

## 修复方法

### 立即修复

修改 `scripts/validate_reference_graph.py` 第 24-25 行：

```python
# 旧代码（错误）
INDEX_REFERENCE = re.compile(
    r"^\|\s*(REF-[A-Z0-9-]+)\s*\|\s*\[[^]]+\]\(([^)]+\.md)\)\s*\|"
)

# 新代码（正确）
INDEX_REFERENCE = re.compile(
    r"^\|\s*(REF-[A-Z0-9-]+|PITFALL-\d+)\s*\|\s*\[[^]]+\]\(([^)]+\.md)\)\s*\|"
)
```

### 验证

修复后重新运行：
```bash
python3 scripts/validate_skill.py /path/to/skill
python3 scripts/validate_reference_graph.py /path/to/skill
```

---

## 预防方法

1. **新增 PITFALL 时**：同时检查 `validate_reference_graph.py` 的 INDEX_REFERENCE 正则是否匹配
2. **运行验证前**：确认所有 ID 格式（REF-xxx 或 PITFALL-xxx）都被正则覆盖
3. **测试用例**：新增 PITFALL 后，验证脚本应该通过，而不是报 60+ 个错误

---

## 验证方式

检查清单：
- [ ] 新增 PITFALL 后运行验证脚本
- [ ] 验证脚本是否报告 "总索引 ID 不一致"？
- [ ] 如果是，检查 INDEX_REFERENCE 正则是否包含 `PITFALL-\d+`
- [ ] 修复正则后重新运行验证
- [ ] 确认所有验证通过

---

## 来源

- 2026-06-21 技能升级 session
- 新增 pitfall-024-form-first-failure.md 后验证失败
- 根因：validate_reference_graph.py INDEX_REFERENCE 正则不匹配 PITFALL ID
