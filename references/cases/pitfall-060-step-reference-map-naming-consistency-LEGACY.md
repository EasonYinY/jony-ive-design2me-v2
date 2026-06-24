---
reference_id: PITFALL-060-LEGACY
title: step-reference-map 与 pitfall 文件命名不一致（Naming Consistency Trap）
category: cases
used_when:
  - SKILL-UPGRADE
  - REFERENCE-VALIDATION
called_by:
  - verify-all.sh
  - validate_reference_graph.py
depends_on:
  - REF-PROCESS-002
outputs:
  - validation_fix_recipe
---

# Pitfall 060: step-reference-map 与 pitfall 文件命名不一致

## 触发条件

新增 pitfall 文件（如 `pitfall-055-scale-fact-disconnect.md`）后，`validate_reference_graph.py` 报错：
- "PITFALL-055 声明 STEP-04，但步骤映射未引用它"
- "STEP-12 与 PITFALL-055 的 used_when 不互反"

## 现象

1. pitfall 文件 frontmatter 使用 `reference_id: PITFALL-055`
2. step-reference-map.md 使用 `REF-CASE-055`
3. 验证器进行精确字符串匹配，导致双向一致性检查失败

## 根因

历史命名不一致：
- 旧 pitfall 文件（001-053）使用 `reference_id: PITFALL-XXX`
- 但 step-reference-map.md 中对应条目使用 `REF-CASE-XXX`
- 验证器期望两侧使用**完全相同的 ID 字符串**

## 修复方案

**统一使用 PITFALL-XXX 格式**（因为 pitfall 文件本身已用此格式）：

1. 在 step-reference-map.md 中，将所有 `REF-CASE-XXX` 替换为 `PITFALL-XXX`（仅针对 pitfall 类引用）
2. 确保 pitfall 文件的 `used_when` 与 step-reference-map 中的引用**双向互反**：
   - 若 pitfall-055 的 `used_when: [STEP-04, STEP-10]`
   - 则 step-reference-map 中 STEP-04 和 STEP-10 必须包含 `PITFALL-055`
   - 且其他步骤**不能**包含 `PITFALL-055`

## 检查清单

- [ ] 新增 pitfall 文件的 `reference_id` 与 step-reference-map 中的引用名称一致？
- [ ] `used_when` 与 step-reference-map 中的引用双向互反？
- [ ] pitfall 文件的 `called_by` 包含 `step-reference-map.md`？
- [ ] 运行 `validate_reference_graph.py .` 通过？

## 历史记录

- **2026-06-24**: 修复 PITFALL-055~059 的命名不一致问题，统一为 PITFALL-XXX 格式
