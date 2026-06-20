---
reference_id: REF-DIRECTION-004
title: 六轴方向差异门
category: direction
used_when:
  - STEP-09
  - STEP-14
called_by:
  - product-design
  - ui-ux
  - service
  - organization
  - wearable
  - modular
depends_on:
  - REF-EVIDENCE-001
  - REF-DIRECTION-005
outputs:
  - direction_diversity_result
---

# 六轴方向差异门

输入必须是四至六个候选。先剔除存在物理、法规、制造、成本、寿命、环境或反俗套失败的候选，再对幸存候选执行差异组合。

三个方向必须在关系、结构和操作三个核心轴上分别唯一，并在材料、工艺、颜色、形态四个视觉轴中至少三个分别唯一。共享同一主材、主色和表面工艺组合视为 CMF 同质化；仅改变形态修饰不能通过。

确定性筛选按原候选顺序检查三元组，返回首个合格组合。幸存候选不足三个，或所有三元组都未通过时，结果必须为 `regeneration_required`，重新生成四至六个候选，不允许用弱方向补位。
