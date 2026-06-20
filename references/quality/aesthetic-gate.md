---
reference_id: REF-QUALITY-001
title: 审美收敛质量门
category: quality
used_when:
  - STEP-08
  - STEP-09
  - STEP-10
  - STEP-11
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
  - aesthetic_quality_result
---

# 审美收敛质量门

分别检查产品识别性、比例张力、部件层级、材料诚实、触觉精度、接缝秩序、静息状态和十年耐久。八项必须各有一条 `AestheticCriterionAssessment`，不得缺失或重复。

每项判断必须包含具体结论、`design_ir.<field>` 或 `image.<evidence>` 证据指针和通过状态，不使用“不够高级”之类无对照结论。只要一项失败，结果即为 `RETURN_TO_DIRECTION_DEVELOPMENT`；八项全部通过才返回 `PASS`，摄影和提示词不能覆盖失败。

本质量门是工程治理规则，不冒充 Jony Ive 的公开理论，也不允许用人物风格锚点替代具体判断。
