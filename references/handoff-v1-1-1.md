---
reference_id: REF-HANDOFF-V111
title: Handoff 口令 当前版本 → 当前版本
category: handoff
used_when:
  - NEW-SESSION
  - SKILL-CONTINUATION
called_by:
  - user-request
depends_on:
  - REF-CHANGELOG-007
outputs:
  - handoff_token
---

# Handoff 口令 当前版本 → 当前版本

## 快速启动检查

1. **读取文件卫生铁律**: `references/file-hygiene.md`（6条铁律）
2. **读取本次升级**: `references/changelogs/当前版本-changelog.md`
3. **读取新增规则**: 
   - `references/rules/rule-form-variety.md`（形态变化硬规则）
   - `references/rules/rule-cmf-contrast.md`（CMF软硬对比硬规则）
   - `references/rules/rule-interaction-nodes.md`（交互节点显性化硬规则）
   - `references/rules/rule-manufacturing-constraints.md`（制造工艺硬约束）
4. **读取新增Pitfall**:
   - `references/cases/pitfall-019-organic-curve.md`（曲面过于有机）
   - `references/cases/pitfall-020-liquid-metal-flat.md`（液态金属单一）
   - `references/cases/pitfall-021-hidden-interaction.md`（交互过度隐藏）
   - `references/cases/pitfall-022-no-manufacturing.md`（缺少制造工艺）

## 升级摘要

**版本**: 当前版本
**日期**: 2026-06-21
**触发**: 用户反馈电动剃须刀图片问题

### 4个核心问题修复

| 问题 | 新增规则 | 影响步骤 | 关键变更 |
|------|---------|---------|---------|
| 曲面过于有机，无亮眼曲线 | Rule 010 | STEP-10 | 强制≥3个控制点+1个视觉钩子+层次节奏 |
| 液态金属单一，无软硬对比 | Rule 011 | STEP-12 | 强制硬+柔对比，柔必须有规律，液态金属<50% |
| 缺少交互显性特征 | Rule 012 | STEP-11 | 强制≥1个显性交互特征，隐性显性设计 |
| 缺少制造工艺/分件 | Rule 013 | STEP-12/13 | 强制分件方式+加工工艺标注，禁止「一体成型」 |

### 提示词新增强制字段

- 分件线描述（如"seamless two-part construction"）
- 加工工艺描述（如"CNC-machined aluminum upper shell"）
- 显性交互特征描述（如"single micro-dimple for power"）
- 软硬对比描述（如"hard aluminum core wrapped in soft liquid metal coating"）

## 接续任务

如需重新生成电动剃须刀图片（应用旧版规则），请执行：
1. 重新运行十五步主流程（STEP-01至STEP-15）
2. 按新规则生成三个方向的DesignIR和提示词
3. 调用Lovart生成图片
4. 按8维度评审

## 来源

- `references/changelogs/当前版本-changelog.md`
