---
reference_id: REF-PROMPT-003
title: 提示词逐句追溯
category: prompt
used_when:
  - STEP-15
called_by:
  - product-design
  - prompt-rewriting
  - image-critique
depends_on:
  - REF-PROMPT-001
  - REF-DESIGN-001
outputs:
  - prompt_trace
---

# 提示词逐句追溯

最终提示词按语义短句拆分，每个短句记录来源字段与原始内容。允许来源仅限 DesignIR 字段和封闭摄影控制；一个短句可以合并多个字段，但不能创造新结构、材料、动作或设计意图。

追溯记录用于校验，不与最终生产提示词混排。

`form_proportion`、`cmf_system`、`resting_state` 与封闭摄影控制是必需追溯项。校验时不只检查字段名，还必须将追溯中的完整原始值与同方向 `DesignIR` 逐项比对。
