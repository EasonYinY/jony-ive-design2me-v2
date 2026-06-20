---
reference_id: REF-FIVE-001
title: 五维推理引擎与显性步骤合同
category: core
used_when:
  - STEP-03
  - STEP-05
  - STEP-06
  - STEP-07
  - STEP-09
  - STEP-10
  - STEP-11
  - STEP-12
  - STEP-13
  - STEP-14
called_by:
  - product-design
  - ui-ux
  - service
  - organization
  - wearable
  - modular
depends_on:
  - REF-EVIDENCE-001
outputs:
  - five_dimension_card
---

# 五维推理引擎与显性步骤合同

## 用途

本文件将用户指定的《现代产品成功五维模型》转换为每个正式设计步骤的强制决策合同。该模型是本工程的治理框架，证据等级为 `G`；不得将其表述为 Jony Ive 或 LoveFrom 的公开理论。

## 五维决策卡

每个正式步骤都必须完整填写五个维度，不得缺省或用空值代替。

| 维度 | 强制问题 | 治理证据 |
|---|---|---|
| 核心理念 `vision_value` | 当前决策为谁解决什么本质问题，创造什么长期价值？ | `GOV-001` |
| 规则体系 `strategy_system` | 什么路径、标准和决策机制能使结论可重复、可调整？ | `GOV-002` |
| 工具基建 `tools_infrastructure` | 需要哪些稳定、可扩展、成本合理的技术、数据或工具支撑？ | `GOV-003` |
| 执行技巧 `execution_tactics` | 如何用小步验证、细节打磨和协作将判断落地？ | `GOV-004` |
| 环境时机 `environment_timing` | 哪些市场、政策、竞争、资源和投入时点构成客观约束？ | `GOV-005` |

每个维度必须记录四项内容：

1. `judgment`：当前判断，不得只复述维度定义。
2. `evidence`：一条或以上可追溯证据。
3. `risks`：一条或以上尚未消除的风险。
4. `status`：当前判断状态，不得留空。

## 证据引用合同

每条证据至少携带 `claim_id`、`claim_class`、`evidence_level` 和 `source_pointer`，并保留适用条件与禁止外推范围。类型和等级必须沿用 `evidence-policy.md` 与工程 `SOURCE_LEDGER.csv` 中的值。仅有本地结论而没有来源指针的内容，不得进入正向决策。

## 显性步骤的十字段合同

每个正式步骤都必须展示下列字段，不得自动压缩：

1. `input`：本步骤实际使用的输入。
2. `core_question`：本步骤唯一需解决的核心问题。
3. `five_dimension_judgment`：完整的五维决策卡。
4. `evidence`：支持本步骤候选与结论的可追溯证据。
5. `candidates`：被实际比较的候选项。
6. `rejection_reasons`：未采用候选项的具体否决理由。
7. `conclusion`：当前通过证据支持的结论。
8. `unconfirmed_items`：仍需验证的项目；如当前无项目，也必须显式记录“无”。
9. `status`：本步骤的当前状态。
10. `next_step`：下一个可执行动作。

## 运行约束

- 十个步骤字段和五个维度均为强制项。
- 证据不足时必须保留未确认项或阻断结论，不得用风格词填补。
- 五维卡是设计判断的治理内核，不是 Jony Ive 个人风格模板。
- 本合同不定义艾维模型、案例胶囊、三方向协议、Design IR 或提示词编译。
