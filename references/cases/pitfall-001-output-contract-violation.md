---
reference_id: REF-CASE-PITFALL-001
title: Pitfall 001 - 输出合同违反
category: cases
used_when:
  - OUTPUT-VALIDATION
called_by:
  - skill-execution
  - quality-gate
depends_on:
  - REF-PROCESS-003
  - REF-PROCESS-001
outputs:
  - pitfall_lesson
---

# Pitfall 001: 输出合同违反

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 用户反馈"没有按照要求输出内容"
> **严重级别**: BLOCKER

---

## 现象

执行 jony-ive-design2me-v2 技能时，虽然读取了所有参考文件，但输出时：
1. 压缩了 WorkflowStepRecord，没有展示每一步的完整字段（输入、核心问题、五维判断、引用证据、候选、否决理由、结论、未确认项、状态、下一步）
2. 提示词没有使用感官材料优先法（方法8）和品牌语境锚定法（方法9）
3. 材料职责格式不完整，使用了工程材料名而非感官材料名
4. 没有包含文化杂交元素
5. 没有应用视觉张力比例

## 根因

1. **技能文件读取后没有严格执行**：读取了 `reasoning-output.md` 和 `end-to-end-workflow.md`，但输出时为了"简洁"而压缩了步骤
2. **提示词工程方法没有内化为执行习惯**：虽然读取了 `prompt-engineering.md`，但输出时仍使用了旧习惯（工程材料名、无品牌语境）
3. **视觉张力比例和文化杂交检查被遗漏**：没有按 `visual-tension-proportion.md` 和 `cultural-hybrid-design.md` 执行

## 修复

1. **严格执行输出合同**：每一步必须展示完整的 WorkflowStepRecord，不得压缩
2. **提示词工程检查清单**：输出前必须运行 `prompt-engineering.md` 的综合检查清单
3. **视觉张力比例检查**：STEP-10 后必须运行 `visual-tension-proportion.md` 的检查清单
4. **文化杂交检查**：STEP-06 后必须确认至少一个方向包含文化杂交元素

## 预防

在 SKILL.md 启动顺序中增加：
> **执行前必读**：`references/process/reasoning-output.md` 和 `references/guides/prompt-engineering.md` 必须在执行前完整阅读，不得只浏览摘要。

## 验证

未来执行时，检查：
- [ ] 每一步是否包含完整的 10 个 WorkflowStepRecord 字段
- [ ] 提示词是否使用感官材料优先法（方法8）
- [ ] 提示词是否包含品牌语境锚定（方法9）
- [ ] 材料职责是否使用强制格式
- [ ] 是否包含文化杂交元素
- [ ] 是否应用视觉张力比例
