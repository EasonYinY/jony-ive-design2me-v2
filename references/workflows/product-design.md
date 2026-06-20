---
reference_id: REF-WORKFLOW-002
title: 产品设计工作流
category: workflows
used_when:
  - ROUTE-PRODUCT-DESIGN
called_by:
  - skill-router
depends_on:
  - REF-PROCESS-001
  - REF-DIRECTION-002
  - REF-DESIGN-001
outputs:
  - three_product_directions
---

# 产品设计工作流

## 调用步骤

执行 `STEP-01` 至 `STEP-15`，在用户可见输出中完整展示每一步。必须同时交付三个本质不同方向的完整 DesignIR、质量门结果和各自提示词，不能只展开或绘制首选方向。

默认在三段提示词交付后停止。只有用户在当前请求中明确要求“出图、绘制、生成图片或渲染”时才允许调用图像工具；“设计产品”本身不等于要求绘图。

若当前输入是用户对上一次结果的批评、纠正或建议，且未明确要求重跑项目，则停止本工作流，转入技能优化模式，不重新生成该产品方案。

## 必读引用

- [主流程](../process/end-to-end-workflow.md)
- [步骤引用映射](../process/step-reference-map.md)
- [六层约束](../direction/constraint-cascade.md)
- [DesignIR](../design/design-ir.md)
- [审美质量门](../quality/aesthetic-gate.md)

重点检查承力、尺寸与姿态、误操作、装配公差、失效、清洁和修理；不得用表面风格替代产品推导。
