---
reference_id: REF-QUALITY-004
title: 图片确定性质量门
category: quality
used_when:
  - STEP-02
  - STEP-07
  - STEP-09
  - STEP-13
  - STEP-14
  - STEP-15
called_by:
  - all-workflows
depends_on:
  - REF-EVIDENCE-001
  - REF-QUALITY-003
outputs:
  - quality_result
---

# 图片确定性质量门

## 输入与输出

质量门输入为不可变 `ImageCritique`，输出为不可变 `ImageQualityResult`。结果保留原始 `DesignIR` 与 `PromptBundle` 引用，并明确给出结果、修复层级、原因、必要动作和禁止动作。

## 三种结果

| 结果 | 修复层级 | 适用条件 |
|---|---|---|
| `PASS` | `NONE` | 未发现合同冲突 |
| `EXPRESSION_REPAIR` | `PROMPT_OR_RENDER` | 仅有操作、静息状态不可见、无依据文字标签、背景侵入或提示词格式错误等表达失败 |
| `RETURN_TO_PRODUCT_DERIVATION` | `DESIGN_IR` | 存在结构误读、材料伪造、方向同质化、Apple 外形套壳、形态先于关系、材料无职责、纯审美比例、颜色词替代高级感或功能未验证 |

## 决策顺序

1. 验证方向标识、`DesignIR` 和 `PromptBundle` 的追溯关系。
2. 检查所有失败码是否来自封闭失败库。
3. 只要存在产品冲突，整体结果立即退回产品推导。
4. 没有产品冲突但存在表达失败时，只允许修订提示词约束或重新渲染。
5. 没有失败时通过，不创建额外修复动作。

## 不可跨越的边界

- 摄影参数不得覆盖产品冲突。
- 表达修复不得修改 `DesignIR`，也不得增加、删除或重定义产品构件。
- 退回产品推导后必须重新检查关系、结构、操作和约束；不能用更换机位或风格词假装冲突消失。
- 混合失败按最高层级处理，不能用局部表达修复降低产品冲突等级。
