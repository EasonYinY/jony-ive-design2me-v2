---
reference_id: REF-CASE-020A
title: Pitfall 020 - 光路设计不可见
category: cases
used_when:
  - IMAGE-CRITIQUE
called_by:
  - lighting-design
  - image-critique
depends_on:
  - REF-DESIGN-003
  - REF-QUALITY-002
outputs:
  - failure_pattern
---

# Pitfall 020 - 光路设计不可见

## 触发条件

- 照明产品的光路设计在提示词中未充分表达
- 图片中光路不可见或表达不足
- 用户无法从图片中理解光路设计

## 失败表现

- 图片中光源不可见
- 反射器/扩散器设计不可见
- 光路效果不可见
- 照明产品看起来像非照明产品

## 根因分析

1. **提示词缺少光路关键词**: 未包含光源、反射器、扩散器描述
2. **CMF缺少光路材料**: 材料职责未包含光路职责
3. **图片评审缺少光路维度**: 未检查光路表达

## 修复方法

1. 在STEP-12使用照明产品专用材料职责格式
2. 在提示词中包含光路可见性关键词
3. 参考 `references/guides/lighting-design.md`

## 验证方式

- 图片中光源可见
- 反射器/扩散器设计可见
- 光路效果可见

## 来源

- REF-DESIGN-003: CMF系统
- REF-QUALITY-002: 图片评审
- Round 2 实证: 照明产品光路设计缺失
