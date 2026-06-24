---
reference_id: REF-ITERATION-R4-UPGRADE-PLAN
title: Round 4 升级计划
category: iteration
used_when:
  - SKILL-AUDIT
  - DOC-REFERENCE
  - ITERATION-MODE
called_by:
  - skill-router
  - iteration-workflow
depends_on:
  - REF-PROCESS-001
outputs:
  - reference_metadata
---
# Round 4 升级计划

> **轮次**: Round 4 / 5
> **产品**: 蓝牙音箱
> **日期**: 2026-06-21
> **技能版本**: jony-ive-design2me-旧版→ 当前版本

---

## 评审结果分析

### 核心问题

| 问题 | 影响 | 优先级 |
|------|------|--------|
| 复杂产品衰减增大 | 蓝牙音箱比充电器衰减大 | 🔴 高 |
| 织物/碳纤维质感表达不清 | 材料诚实受影响 | 🟡 中 |
| 动态形态折叠状态不可见 | 产品功能不完整 | 🟡 中 |
| timeout问题 | 复杂提示词导致 | 🟡 中 |

### 成功因素
- 陶瓷材料质感表达优秀（方向B最高分）
- 自然材料（陶瓷、釉面）AI理解准确

---

## 升级策略

### 升级1: 新增 Pitfall — 复杂产品衰减增大 (🔴 高)

**文件**: `references/cases/pitfall-029-complex-product-attenuation.md`

**内容**:
- 现象: 复杂产品（音箱、咖啡机）比简单产品（充电器、灯具）衰减更大
- 根因: 复杂产品需要描述更多部件、材料、交互
- 解决: 
  - 复杂产品优先使用自然材料（陶瓷、木材）
  - 减少机械结构描述，增加材料质感描述
  - 接受复杂产品的衰减，在评审中调整预期

### 升级2: 新增指南 — 织物/碳纤维质感精确表达 (🟡 中)

**文件**: `references/guides/textile-carbon-fiber-expression.md`

**内容**:
- 织物: 必须描述编织方式、线径、密度
- 碳纤维: 必须描述编织 pattern、层数、表面处理
- 示例: "carbon fiber 2×2 twill weave, 0.2mm thread, matte finish"

### 升级3: 升级动态形态表达指南 (🟡 中)

**文件**: `references/guides/dynamic-form-expression.md` (patch)

**内容**:
- 新增"折叠状态指示器"章节
- 要求折叠产品必须展示2个状态指示器

---

## 版本记录

**当前版本 Changelog**:
- 新增 Pitfall 029: 复杂产品衰减增大
- 新增指南: 织物/碳纤维质感精确表达
- 升级 Guide 019: 动态形态表达（新增折叠状态指示器）

---

## 来源

- 评审结果: references/iterations/round-4/image-analysis.md
- 日期: 2026-06-21
