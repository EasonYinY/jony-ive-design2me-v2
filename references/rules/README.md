---
reference_id: REF-RULE-INDEX
title: 硬编码规则与方法论索引
category: rules
used_when:
  - SKILL-AUDIT
  - DIRECTION-SELECTION
  - EVIDENCE-EVALUATION
called_by:
  - evidence-policy
  - direction-protocol
  - five-dimension-engine
depends_on:
  - REF-EVIDENCE-001
  - REF-DIRECTION-005
  - REF-FIVE-001
outputs:
  - rule_inventory
---

# 硬编码规则与方法论索引

> **用途**: 索引所有已记录的硬编码规则、方法论框架和决策机制。
> **更新规则**: 发现新规则或方法论 → 添加新文件；规则更新 → 标记版本；不删除历史记录。
> **目录结构**:

```
references/rules/
├── README.md                 # 本文件：总索引
├── evidence-evaluation.md    # 证据等级评估规则
├── direction-selection.md    # 方向筛选决策规则
├── quality-gate-rules.md     # 质量门判定规则
└── ...
```

## 已记录规则

| 规则 ID | 标题 | 适用范围 | 来源 | 状态 |
|---------|------|---------|------|------|
| rule-001 | 证据等级评估 | 所有步骤的证据判定 | REF-EVIDENCE-001 | 待创建 |
| rule-002 | 来源冲突处理 | 多来源冲突时的优先级 | REF-EVIDENCE-001 | 待创建 |
| rule-003 | 方向同质化检测 | 三个候选方向的本质差异判定 | REF-DIRECTION-005 | 待创建 |
| rule-004 | 质量门判定 | 8项审美质量门的通过/失败标准 | REF-QUALITY-001 | 待创建 |
| rule-005 | 禁止外推范围 | BND-001/BND-002/BND-003 的具体执行 | REF-EVIDENCE-001 | 待创建 |
| rule-006 | 五维卡强制填写 | 每个步骤的五维决策卡填写规范 | REF-FIVE-001 | 待创建 |
| rule-007 | 步骤字段完整性 | 10个步骤字段的强制展示规范 | REF-FIVE-001 | 待创建 |
| rule-008 | 摄影控制封闭枚举 | 摄影参数只允许使用预定义枚举值 | REF-PROMPT-001 | 待创建 |
| rule-009 | 提示词编译不等于出图授权 | 无明确指令时停止在提示词处 | REF-PROMPT-001 | 待创建 |

## 使用方式

1. **证据评估时**: 对照 evidence-evaluation.md 检查证据等级
2. **方向筛选时**: 对照 direction-selection.md 检查本质差异
3. **质量门审查时**: 对照 quality-gate-rules.md 检查通过标准
4. **新规则积累时**: 按 `rule-NNN-标题.md` 格式创建新文件

## 创建新规则模板

```markdown
---
reference_id: REF-RULE-NNN
title: Rule NNN - 标题
category: rules
used_when:
  - STEP-XX
called_by:
  - [workflow-name]
depends_on:
  - [dependency-ref]
outputs:
  - rule_definition
---

# Rule NNN - 标题

## 规则定义

[清晰描述规则内容]

## 适用范围

[描述规则适用的步骤/场景]

## 执行标准

[描述如何执行此规则]

## 违反后果

[描述违反此规则的后果]

## 验证方式

[描述如何确认规则已正确执行]

## 来源

- [引用相关 reference]
```
