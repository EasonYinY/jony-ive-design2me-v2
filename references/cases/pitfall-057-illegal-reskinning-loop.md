---
reference_id: PITFALL-057
title: 非线性重构的"作弊解"（Illegal Reskinning Loop）
category: cases
used_when:
  - STEP-06
  - STEP-07
  - STEP-09
called_by:
  - end-to-end-workflow.md
depends_on:
  - REF-PROCESS-001
outputs:
  - candidate_lineage_report
---

# Pitfall 057: Illegal Reskinning Loop

## 触发条件

STEP-07 否决候选后，为了凑满"三个独立方向"的交付合同，直接修改死地方案或临时编造新方案，跳过物理与法规验证。

## 现象

- STEP-06 生成候选 A/B/C（Monolithic Slab / Monocoque Tension Shell / Volumetric Subtraction）
- STEP-07 否决候选 C（体量减法，成本失败）
- STEP-09 为了凑齐三个方向，将已否决的候选 C 套上"磁悬浮分离体"的壳子强行复活
- 新方案 C 引入超导磁体、液氮补充等完全未经上游约束层检验的假设

## 根因

1. 破坏可审计决策链的严谨性
2. 通过否定一个方案，再毫无逻辑递进地"无中生有"新方案
3. 缺乏断路器自闭环（Circuit Breaker Self-Loop）

## 逻辑破产

候选 C 的否决是基于成本层（减材制造材料浪费 >40%）。新"磁悬浮分离体"方案虽然拓扑不同，但同样面临成本问题（超导磁体、液氮维护），且引入了全新的物理假设（磁悬浮在城市低空的安全性与法规），这些假设完全未在 STEP-07 中验证。

## 解决方案

在 STEP-07 注入断路器自闭环：

> 若 STEP-07/08 导致候选数量不足 3 个，**禁止就地修改死地方案或临时编造新方案**。工作流必须强制回退（Re-entry）至 STEP-06.1，修改基础排布变量，重新生成全新的候选集合，并完整重新跑一遍 STEP-07/08 约束级联。

## 检查清单

- [ ] 否决候选后是否回退 STEP-06.1 重新生成？
- [ ] 新候选是否完整跑过 STEP-07/08 约束级联？
- [ ] 是否存在"否决→复活"的基因突变？
- [ ] 所有三个方向的推导血统是否清白？
