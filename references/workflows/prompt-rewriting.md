---
reference_id: REF-WORKFLOW-003
title: 提示词改写工作流
category: workflows
used_when:
  - ROUTE-PROMPT-REWRITING
called_by:
  - skill-router
depends_on:
  - REF-PROCESS-001
  - REF-PROMPT-001
outputs:
  - rewritten_prompt_bundle
---

# 提示词改写工作流

## 调用步骤

执行 `STEP-01` 至 `STEP-05` 重建上游定义，再执行 `STEP-10` 至 `STEP-15`；缺失的产品事实标为未知，不凭提示词补写。

## 必读引用

- [证据政策](../core/evidence-policy.md)
- [DesignIR](../design/design-ir.md)
- [提示词合同](../prompt/prompt-contract.md)
- [压缩规则](../prompt/prompt-compression.md)
- [追溯合同](../prompt/prompt-trace.md)

最终每个方向只输出一段 90 至 160 个非空白字符的中文提示词，不输出反向提示词。
