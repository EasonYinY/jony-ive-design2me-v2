---
reference_id: REF-DESIGN-003
title: CMF 系统
category: design
used_when:
  - STEP-09
  - STEP-12
  - STEP-14
  - STEP-15
called_by:
  - product-design
  - prompt-rewriting
  - image-critique
depends_on:
  - REF-EVIDENCE-001
  - REF-DESIGN-001
outputs:
  - cmf_system
---

# CMF 系统

每个方向在单一 `cmf_system` 中记录主材、辅材、颜色、成形与表面工艺、触感、清洁方式、老化路径和回收后果，并与 `materials`、`manufacturing` 和 `maintenance` 三个字段互相一致。材料必须承担结构、接触、密封、导热、耐磨或维护职责；不得只写“高级金属”或用灰黑配色替代方向差异。

三方向不得共享同一主材、主色和表面工艺组合。颜色必须给出明确范围或稳定物理参照，避免抽象形容词导致生成偏差。
