---
reference_id: REF-CASE-025
title: Pitfall 025 — 规则写在文档里但未在编译器/质量门中强制执行
category: cases
used_when:
  - skill-optimization
  - image-generation
  - rule-audit
called_by:
  - product-design
  - prompt-rewriting
  - image-critique
depends_on:
  - REF-PROMPT-004
  - REF-PROMPT-001
  - REF-QUALITY-001
  - REF-QUALITY-002
outputs:
  - enforcement_gap_analysis
  - fix_plan
---

# Pitfall 025 — 规则写在文档里但未在编译器/质量门中强制执行

> **版本**: 1.0.0
> **日期**: 2026-06-21
> **触发**: 用户反馈 D2/D3 图片出现手/人物，背景非纯白，单材质无工艺分界线

---

## 现象

`photography-controls.md` 旧版 明确写了：
> "禁止元素：辅助物品（手、工具、配件）、人物（全身、手、脸）"

但生成的图片中仍然出现了手/人物。

## 根因分析

**文档规则 ≠ 执行规则**。四层防线中，只有第一层（文档）存在，后三层缺失：

| 防线层级 | 职责 | 旧版 | |
|---------|------|----------|----------|
| **L1: 文档规则** | 告诉人"应该怎么做" | ✅ 有文字 | 强化零容忍措辞 |
| **L2: 编译器强制** | 提示词编译时自动注入约束 | ❌ 无 | `compile_prompt.py` 强制注入 |
| **L3: 质量门检查** | 编译后检查提示词是否包含约束 | ❌ 无 | `aesthetic-gate.md` 8维度检查 |
| **L4: 图片评审零容忍** | 生成后检查图片是否违规 | ❌ 无 | `image-critique.md` 零容忍前置 |

## 具体失败点

### 失败点 1：compile_prompt.py 未注入零容忍约束

旧版的 `negative_prompt` 只包含：
```python
"不得使用 Apple-like 外形、白色圆角金属套壳...不得用机位隐藏产品冲突。"
```

缺少：`No hand, no finger, no human, no person, only product; Pure white background.`

### 失败点 2：prompt-contract.md 未检查零容忍约束

旧版的负面约束检查只验证：
- 是否使用通用负面词 → 重新编译
- 负面约束与产品无关 → 重新编译
- 负面约束少于 3 个或多于 5 个 → 重新编译

缺少：是否包含 `No hand, no finger, no human, no person`

### 失败点 3：aesthetic-gate.md 未检查无手/人物

旧版的视觉语言一致性只有 7 维度：
- 悬浮感一致性
- 背景一致性
- 焦点一致性
- 摄影语法一致性
- 负面约束一致性
- 材料精确度
- 几何精确度

缺少：无手/人物零容忍检查

### 失败点 4：image-critique.md 未前置零容忍检查

旧版的"背景纯净"检查在 7 项必查之后，不是零容忍前置。

## 修复路径（旧版 已实施）

1. **compile_prompt.py**：`negative_prompt` 强制注入 `No hand...Pure white background.`
2. **prompt-contract.md**：负面约束检查新增"必须包含零容忍约束"
3. **aesthetic-gate.md**：视觉语言 7 维度 → 8 维度（+无手/人物零容忍）
4. **image-critique.md**：零容忍检查前置，先执行无手/人物/纯白背景/单一产品

## 通用教训

**任何新规则必须同时更新四层防线**：
- 文档规则（references/）
- 编译器强制（scripts/compile_prompt.py）
- 质量门检查（references/quality/）
- 图片评审零容忍（references/quality/image-critique.md）

只更新文档 = 规则不会被执行。

## 检查清单

添加新规则时，确认以下四项都已更新：
- [ ] 文档规则已更新（references/ 对应文件）
- [ ] 编译器已强制注入（scripts/compile_prompt.py）
- [ ] 质量门已添加检查项（references/quality/aesthetic-gate.md）
- [ ] 图片评审已前置零容忍（references/quality/image-critique.md）
