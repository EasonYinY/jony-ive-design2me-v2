---
reference_id: REF-PROMPT-002
title: 中文提示词压缩规则
category: prompt
used_when:
  - STEP-15
called_by:
  - product-design
  - prompt-rewriting
depends_on:
  - REF-PROMPT-001
  - REF-DESIGN-003
outputs:
  - production_prompt
---

# 中文提示词压缩规则

每个方向最终只输出一段中文提示词，长度为 90 至 160 个非空白 Unicode 字符。固定顺序为：产品身份与关系、结构形态、差异化 CMF、使用动作、摄影表达。

删除论证过程、风险、内部字段名、方向编号和重复修饰，不输出反向提示词。凡不能追溯到 DesignIR 或摄影控制的词句均删除。

确定性编译先去除字段名式前缀和重复空白，再按固定字符预算保留各字段的开头语义摘要；被压缩的短句仍必须在 `prompt_trace` 中保留完整原始值。摄影枚举转换为固定中文标签，不接受自由改写。
