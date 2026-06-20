---
reference_id: REF-WORKFLOW-004
title: 图片评审工作流
category: workflows
used_when:
  - ROUTE-IMAGE-CRITIQUE
called_by:
  - skill-router
depends_on:
  - REF-QUALITY-002
  - REF-QUALITY-004
outputs:
  - image_quality_decision
---

# 图片评审工作流

## 调用步骤

执行 `STEP-01`、`STEP-02`，重建缺失的 `STEP-13` 与 `STEP-15` 上游合同，再执行 `STEP-14` 和图片质量判断。

## 必读引用

- [DesignIR](../design/design-ir.md)
- [图片评审合同](../quality/image-critique.md)
- [失败库](../quality/failure-library.md)
- [审美质量门](../quality/aesthetic-gate.md)
- [质量门](../quality/quality-gates.md)

区分产品冲突与表达失败；产品冲突必须退回推导，不能靠换机位或光线修复。
