---
reference_id: PITFALL-059
title: 审计报告驱动升级时跳过调研直接 bump 版本号
category: cases
used_when:
  - 用户提交详细审计报告要求重构技能文件
  - audit 涉及 prompt-engineering.md / compile_prompt.py 实质性改动
called_by:
  - SKILL.md 升级规范
  - file-hygiene.md 铁律 8.6
depends_on:
  - REF-CASE-046
  - REF-CASE-053
outputs:
  - 升级决策记录
---

# Pitfall 059: 审计报告驱动升级时跳过调研直接 bump 版本号

> **版本**: 1.0
> **日期**: 2026-06-24
> **触发**: user 提交详细审计报告(结构层/输出层/模型适配层),要求重构上游技能文件

## 现象

用户提交审计报告，要求"完全补完，完全更新"技能文件。audit 涉及 prompt-engineering.md / compile_prompt.py 实质性改动。按 Pitfall 046 铁律，必须先做 `references/research/{model-name}-model-fit.md` 调研文档才能 bump。

但用户明确要求"更新skill"，与铁律 8.6"调研没完成前禁止 bump"冲突。

## 根因分析

1. **审计报告 ≠ 质量差反馈**：这是技能优化模式（路由规则 #2），不是"质量差"反馈（路由规则 #1）
2. **但实质性改动仍需调研**：audit 中涉及 prompt-engineering.md / compile_prompt.py 改动 → 仍属于"对 SKILL.md / prompt-engineering / cmf-system / product-level-prompt-revolution 的实质性改动"
3. **用户显式指令 > 内部一致性**：user 原话"是完全补完，完全更新" → 必须执行技能文件修改
4. **版本号硬规则不可违反**：铁律 8.6"调研没完成前禁止 bump SKILL.md frontmatter"

## 解决方案

**分阶段处理**：

1. **阶段 A（立即执行）**：按审计报告修改技能文件（end-to-end-workflow.md + prompt-engineering.md + compile_prompt.py）
2. **阶段 B（阻塞）**：不 bump 版本号，保持当前版本
3. **阶段 C（待补）**：完成 `references/research/nano-banana-pro-model-fit.md` 调研文档（≥5节 + 交叉≥3类来源）
4. **阶段 D（解锁）**：user 拍板"按建议改" → bump 版本号 → 运行 render-version.sh

## 关键协议

- **修改范围**：end-to-end-workflow.md + prompt-engineering.md + compile_prompt.py（audit 涉及的文件）
- **不修改**：SKILL.md frontmatter version 字段（铁律 8.6）
- **commit 信息**：明确标注"不 bump 版本号（调研未完成）"
- **待补清单**：nano-banana-pro-model-fit.md 调研文档

## 验证

- [ ] 技能文件已按审计报告修改？
- [ ] 版本号仍为原版本？
- [ ] commit 信息明确标注不 bump 原因？
- [ ] 待补调研文档已记录？

## 关联

- `references/cases/pitfall-046-upgrade-without-research.md`
- `references/file-hygiene.md` 铁律 8.6
- `references/cases/pitfall-053-dynamic-version-variable-pitfalls.md`
