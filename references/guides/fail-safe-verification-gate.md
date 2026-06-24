---
reference_id: REF-GUIDE-FAILSAFE
title: 防御性决策树（Fail-Safe Verification Gate）
category: guides
used_when:
  - STEP-15
  - PROMPT-COMPILATION
  - FINAL-OUTPUT
called_by:
  - end-to-end-workflow
  - prompt-engineering
depends_on:
  - REF-GUIDE-008
  - REF-PROCESS-001
  - REF-GUIDE-SCALE-CMF
outputs:
  - fail_safe_result
  - corrected_prompt
---

# 防御性决策树（Fail-Safe Verification Gate）

> **版本**: 1.0
> **日期**: 2026-06-25
> **触发**: 用户审计报告（系统级重构审计）—— 缺乏自动化审计机制导致提示词漂移

---

## 概述

在最终输出提示词前，运行自动化审计分支逻辑，防止三类常见漂移：
1. **绝对化否定词漂移**：`No text/logo` 用于高精密设备，导致表面虚无
2. **材质尺度错配漂移**：桌面级材质用于大型设备，导致比例压缩
3. **原型丢失漂移**：品类锚定词缺失，导致不可识别

---

## 决策树规则

### 规则1：绝对化否定词拦截（Absolute Negation Interceptor）

**触发条件**：
```
IF (Prompt 包含 "No text" OR "No logo" OR "No status icons" OR "No warning labels" OR "No screws")
   AND (Brief.Category ∈ {医疗设备, 精密仪器, 重型机械, 工业设备, B端设备})
THEN 触发规则1
```

**执行动作**：
1. 强制删除该绝对化否定词
2. 重新调用【功能细节密度矩阵】
3. 补齐 `flush-integrated micro-typographic text indicators` 描述
4. 输出：Layer C 高秩序微观细节描述

**替换模板**：
```
All essential [operational nomenclature / warning labels / status interfaces / model indicators]
are flush-integrated into the [material surface] with zero relief,
strictly governed by a rigorous [typographic grid / engineering grid],
perfectly aligned to the [G2/G3 hairline parting lines],
executed in [ultra-muted low-contrast tones],
visible only upon physical proximity,
whispered rather than screamed.
```

**示例**：
- ❌ `No text, no logo, no status icons`
- ✅ `All essential operational nomenclature and micrometric warning labels are flush-integrated into the ceramic matrix with zero relief, strictly governed by a rigorous typographic grid, executed in ultra-muted low-contrast slate gray tones, whispered rather than screamed.`

---

### 规则2：材质尺度错配拦截（Material-Scale Mismatch Interceptor）

**触发条件**：
```
IF (Prompt 包含 "travertine" OR "obsidian" OR "walnut" OR "marble" OR "small slab" OR "micro hairline")
   AND (Brief.PhysicalScale.MaxDimension > 1.5m)
THEN 触发规则2
```

**执行动作**：
1. 强制拦截桌面级高端家居材质词
2. 重新调用【大型设备材料职责库】
3. 强制替换为建筑级/工业级材质：
   - `medical-grade non-porous ceramic matrices`
   - `precision bead-blasted performance alloys`
   - `monolithic architectonic enclosures`
   - `high-grade acoustic dampening composite panels`
   - `cryogenic hardened steel alloys`
4. 输出：Layer D 尺度材料职责描述

**替换示例**：
- ❌ `travertine base` → ✅ `monolithic architectonic base in high-density solid surface mineral polymer`
- ❌ `walnut accent` → ✅ `brushed bead-blasted titanium accent indicating care for the unseen`
- ❌ `small obsidian slab` → ✅ `precision bead-blasted performance alloy panel`

---

### 规则3：原型丢失拦截（Archetype Loss Interceptor）

**触发条件**：
```
IF (Prompt 缺少品类锚定词)
   OR (Prompt 缺少不可缩减三大特征描述)
   OR (Prompt 使用纯几何体替代品类词: "slab", "cube", "cylinder", "ring", "plate", "block")
THEN 触发规则3
```

**执行动作**：
1. 强制打断当前编译流程
2. 提取 Brief 中的原始物理拓扑名词
3. 将 [A][B][C] 原型结构作为第一主语强行插入 Layer A 与 Layer B
4. 重新编译提示词
5. 输出：修正后的 Layer A + Layer B

**修正示例**：
- ❌ `A solid basalt slab, 250cm long and 40cm thick, with a precise circular aperture recessed flush into its center`
- ✅ `A monolithic 3T MRI scanning enclosure, 250cm in length, featuring a 65cm cylindrical bore cavity defining its front orientation, surfaced in honed basalt for acoustic dampening, with a horizontal patient cradle track seamlessly intersecting the core`

---

## 执行时机与流程

```
STEP-15.10: 防御性决策树执行流程

1. 提示词编译完成（五段式重组后）
2. 运行规则1：绝对化否定词拦截
   - 若触发 → 修正 Layer C → 重新编译
3. 运行规则2：材质尺度错配拦截
   - 若触发 → 修正 Layer D → 重新编译
4. 运行规则3：原型丢失拦截
   - 若触发 → 修正 Layer A + Layer B → 重新编译
5. 全部规则通过 → 输出最终提示词
6. 任一规则触发后，必须重新运行全部三条规则，直至连续两次全部通过
```

---

## 与五段式权重重组的集成

| 五段式层级 | 防御性决策树应用 |
|-----------|--------------|
| Layer A (20%) | 规则3：原型丢失拦截 |
| Layer B (30%) | 规则3：原型丢失拦截 |
| Layer C (15%) | 规则1：绝对化否定词拦截 |
| Layer D (20%) | 规则2：材质尺度错配拦截 |
| Layer E (15%) | 规则1：否定词漂移检查 |

---

## 与行业原型锚定的关系

防御性决策树是 `archetype-verification.md` 的**自动化执行层**：
- `archetype-verification.md` 定义了"应该做什么"（规范）
- `fail-safe-verification-gate.md` 定义了"如果做错了如何自动修正"（自动化审计）

---

## 来源

- 审计报告：2026-06-25 系统级重构审计（防御性决策树）
- 核心病灶：提示词漂移导致生成结果不可识别
- 根因分析：缺乏自动化审计机制
- 升级触发：用户审计报告"三级单点测试防御性决策树"
