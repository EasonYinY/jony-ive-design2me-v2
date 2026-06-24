---
reference_id: REF-CASE-PITFALL-027
title: Pitfall 027 - 审计师/外部建议与现有规则冲突时的诚实反查协议
category: cases
used_when:
  - PITFALL-026
  - SKILL-AUDIT
  - EXTERNAL-AI-FEEDBACK
called_by:
  - skill-optimizer
  - audit-handler
depends_on:
  - REF-CASE-PITFALL-026
  - REF-PROMPT-004
  - REF-QUALITY-001
outputs:
  - failure_pattern
  - conflict_resolution_protocol
---

# Pitfall 027 - 审计师/外部建议与现有规则冲突时的诚实反查协议

> **日期**: 2026-06-24
> **触发**: 资深审计师两轮反馈中,建议 "Suspended in a pure, seamless neutral studio grey (#D1D1D1 or #E5E5E5)" — 但这与本技能 v3.0.0 `REF-PROMPT-004 §3 纯白背景强制` + `REF-QUALITY-001 §视觉语言一致性` 直接冲突
> **严重级别**: 🟠 HIGH for SKILL-AUDIT 场景
> **强制范围**: 所有审计师/外部 AI 反馈处理流程(尤其在 Pitfall 026 协议下)

## 1. 规则定义

当外部审计师(资深用户、第三方 AI、行业专家)给出**看似专业、实则与本技能现有规则冲突**的建议时,禁止盲吸 / 盲拒。必须按 3 步协议处理:

1. **分类**:把建议分为 ① 完全吸收 ② 局部吸收 ③ 诚实反查 + 不照搬
2. **诚实反查**:把建议与现有规则(`REF-` 系列规则文件)逐条比对,记录冲突点
3. **决策**:有冲突的条款 → 不照搬,但记录"为何不照搬"到 `references/guides/audit-feedback-<date>.md` 留底

## 2. 触发判断清单

满足以下任一即触发本协议:

| 判断项 | 触发 |
|---|---|
| 外部建议含具体技术参数(颜色码、尺寸、镜号) | ✓ |
| 外部建议与本技能 v3.0.0+ 任意 `REF-` 文件存在潜在冲突 | ✓ |
| 外部建议由"听起来专业"权威发出(资深审计师 / 行业专家) | ✓ |
| 外部建议数量 ≥ 3 条(防止单点建议污染) | ✓ |

## 3. 实战案例:灰背景冲突

### 审计师建议原文
> "Suspended in a pure, seamless neutral studio grey (#D1D1D1 or #E5E5E5) non-reflective void."

### 现有规则(本技能 v3.0.0 强制)
- `REF-PROMPT-004 §3 纯白背景强制`:**所有提示词必须 `Pure white background`**,禁止 Neutral gradient,已废弃
- `REF-QUALITY-001 §视觉语言一致性`:纯白背景是 8 维度一致性硬要求
- `REF-CASE-016 background_intrusion`:**任何非纯白背景触发 FAIL**

### 冲突点
- 审计师建议 `#D1D1D1` 或 `#E5E5E5` 灰背景 = **直接触发 `background_intrusion` 失败码**
- 视觉语言一致性 8 维度中的"背景一致性"硬要求纯白

### 决策
**不照搬审计师灰背景建议,保留 v3.0.0 强制 pure white**。在 `audit-feedback-2026-06-24-prompt-architecture.md` 第 2.2 节明确记录"为何不照搬"。

## 4. 决策矩阵(诚实反查协议)

| 外部建议类型 | 处理 | 输出 |
|---|---|---|
| 与本技能现有 `REF-` 规则无冲突 + 提升普适性 | 完全吸收 | 写入 `references/guides/<name>.md` |
| 与现有规则部分冲突 + 冲突部分有合理依据 | 局部吸收 | 主体吸收,冲突部分用本技能规则替代 + 记录 |
| 与现有规则直接冲突(违反 `REF-` 强制字段) | 不照搬 | 记录到 `audit-feedback-<date>.md` 第 2.X 节"诚实反查"段 |
| 与现有规则无冲突但与本技能"默认"用户偏好冲突(用户红线) | 强制询问用户 | 不擅自 bump 版本号,等用户明确指令 |

## 5. 失败码(脚本可拒绝)

| 失败码 | 描述 | 严重性 |
|---|---|---|
| `auditor_suggestion_uncaught` | 外部建议未经诚实反查直接照搬 | 🟠 HIGH |
| `auditor_suggestion_uncatalogued` | 外部建议未记录到 `audit-feedback-*.md` 留底 | 🟡 MEDIUM |
| `auditor_suggestion_blindly_rejected` | 外部建议未做反查就盲拒 | 🟡 MEDIUM |

## 6. 与既有规则的关系

- **REF-CASE-PITFALL-026 第三方 AI 反馈处理(分类 → 评估 → 沉淀 → 不重跑)**:本 pitfall 是 Pitfall 026 在"建议 vs 现有规则冲突"子场景的细化
- **REF-PROMPT-004 摄影表达控制**:本 pitfall 的"灰背景冲突"案例的反查依据
- **REF-QUALITY-001 审美收敛质量门**:本 pitfall 的"视觉语言一致性"反查依据
- **REF-HYGIENE-001 文件卫生铁律**:本 pitfall 的"诚实反查记录" 必须写入 `references/`(不污染 SKILL.md)

## 7. 验证方式

```python
def check_auditor_suggestion_conflict(suggestion: str, current_rules: dict) -> list:
    """检查审计师建议与本技能现有规则的冲突点"""
    conflicts = []
    for rule_name, rule_text in current_rules.items():
        # 简化匹配:把审计师建议的关键词与每条 REF- 规则对比
        for keyword in rule_text.get("forbidden_keywords", []):
            if keyword in suggestion:
                conflicts.append(f"auditor_suggestion_uncaught: {rule_name} 含禁词 {keyword!r}")
    return conflicts
```

## 8. 来源

- 2026-06-24 医疗手术电动吻合器任务 R1 出图实战 + 资深审计师两轮反馈
- 审计师原文出处(本对话上下文,用户身份 = 资深设计流程审计师)
- REF-CASE-PITFALL-026: 第三方 AI 反馈处理
- REF-PROMPT-004 §3 纯白背景强制
- REF-QUALITY-001 §视觉语言一致性
- REF-CASE-016 background_intrusion
- REF-HYGIENE-001 文件卫生铁律
