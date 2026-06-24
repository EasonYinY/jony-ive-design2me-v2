---
reference_id: REF-GUIDE-ARCHETYPE
title: 行业原型锚定验证
category: guides
used_when:
  - STEP-05.7
  - STEP-15
  - PROMPT-COMPILATION
called_by:
  - end-to-end-workflow
  - archetype-verification-gate
depends_on:
  - REF-PROCESS-001
  - REF-DESIGN-001
outputs:
  - archetype_features
  - topological_protection
---

# 行业原型锚定验证（Archetype Verification）

> **版本**: 1.0
> **日期**: 2026-06-24
> **触发**: 用户审计报告（联影医疗MRI设计）—— 产品无法识别为医疗设备，被误判为建筑/家具

---

## 概述

当 Brief 属于"重型设备/复杂系统/精密工具/医疗仪器"类目时，必须在设计流程中强制注入"行业原型拓扑保护协议"。该协议确保形态分化不会切断与品类原型的语义联系，防止扩散模型（如 Lovart Nano Banana Pro）将产品误判为其他品类。

---

## 核心问题

**为什么需要原型锚定？**

扩散模型在生成图像时，首先通过提示词中的"品类锚定词"（如 MRI scanner / espresso machine / drone）在训练集中定位正确的语义簇。如果提示词中缺乏这些锚定词，或被纯几何体（slab/cube/cylinder）完全替代，模型将：

1. 无法找到正确的语义簇
2. 退而求其次，调用相近但错误的品类（如将"石板"关联到建筑/家具）
3. 生成"无法识别为何物"的结果

---

## 不可缩减三大形态特征（Irreducible Archetype Features）

每个复杂工业品类都有三个在人类集体潜意识中不可缩减的形态特征。这些特征必须在任何形态分化后依然占据视觉主体（Volume Weight > 40%）。

### 示例：核磁共振（MRI）

| 特征 | 描述 | 视觉权重 | 禁止行为 |
|------|------|----------|----------|
| **扫描舱体（Bore Cavity）** | 65cm 圆形孔径，患者躺入的通道 | > 40% | 禁止将孔径缩小为"缝隙"或"凹槽" |
| **检查床与轨道（Patient Cradle Track）** | 承载患者滑入/滑出的机械系统 | > 20% | 禁止省略检查床或将其简化为"平面" |
| **整体屏蔽外壳（Monolithic Enclosure）** | 包裹超导磁体的整体结构 | > 30% | 禁止将外壳拆解为"分离的板"或"环" |

### 示例：飞行器（Drone/UAV）

| 特征 | 描述 | 视觉权重 | 禁止行为 |
|------|------|----------|----------|
| **动力臂拓扑（Propulsion Arm Topology）** | 推进器/旋翼的安装臂结构 | > 40% | 禁止将动力臂简化为"圆盘"或"球体" |
| **中央机身核心（Central Fuselage Core）** | 承载电池/控制系统的中央体 | > 30% | 禁止将机身分散为"分离模块" |
| **光学传感器舱（Optical Sensor Pod）** | 摄像头/雷达的安装舱 | > 20% | 禁止将传感器隐藏或简化为"平面" |

### 示例：咖啡机（Espresso Machine）

| 特征 | 描述 | 视觉权重 | 禁止行为 |
|------|------|----------|----------|
| **冲泡组（Brew Group）** | 咖啡萃取的核心机械单元 | > 40% | 禁止将冲泡组简化为"按钮"或"灯" |
| **蒸汽棒/奶泡系统（Steam Wand）** | 打奶泡的蒸汽输出管 | > 20% | 禁止省略蒸汽棒 |
| **水箱/豆仓（Water Tank/Bean Hopper）** | 供给系统 | > 30% | 禁止将供给系统隐藏为"内部结构" |

---

## 拓扑完备性检查（Topological Completeness Check）

### 检查项

1. **第一特征识别**：该产品品类在人类集体潜意识中的"第一特征"是什么？
   - 问：如果遮住产品名称，仅凭轮廓，人们能认出这是什么吗？
   - 标准：第一特征必须在轮廓中可识别

2. **视觉权重验证**：该特征在形态分化后是否依然占据视觉主体（Volume Weight > 40%）？
   - 计算：特征体积 / 产品总体积 > 40%
   - 若 < 40%，退回 STEP-06 重新推导

3. **功能暗示词（Functional Hint Words）**：提示词中是否包含至少一个功能暗示词？
   - 示例：MRI → "patient cradle", "scanning bore", "superconducting magnet"
   - 示例：Drone → "propulsion arm", "rotor hub", "aerial sensor"
   - 示例：Coffee Machine → "brew group", "steam wand", "portafilter"

---

## 尺度错觉防御（Scale Illusion Defense）

### 问题

形态描述词可能引发扩散模型在微观（桌面级）与宏观（建筑级）之间的尺度漂移。

### 防御规则

1. **显性尺寸链**：任何形态描述必须包含至少一个显性尺寸（如 "65cm bore", "250cm length"）
2. **人体参照**：必须包含人体尺度参照（如 "patient lies within", "operator stands beside"）
3. **禁止微观词**：禁止在宏观产品上使用微观尺度词（如 "tiny", "miniature", "pocket-sized"）
4. **禁止建筑词**：禁止在工业产品上使用建筑尺度词（如 "monumental", "architectural scale", "building-sized"）

### 校验公式

```
[净尺寸需求] + [结构厚度容差] + [安全防护边界] = [最终输出数值]

示例（MRI）：
- 净尺寸需求：65cm 孔径（患者肩部宽度）
- 结构厚度容差：40mm 壁厚（磁体屏蔽 + 结构刚性）
- 安全防护边界：15mm 间隙（热膨胀 + 维护空间）
- 最终输出：65cm + 40mm × 2 + 15mm × 2 = 75cm 外径
```

---

## 功能 Legibility 校验（Functional Legibility Check）

### 规则

提示词第一段必须明确描述定义该产品核心功能的关键宏观大部件与轴向。

### 正确示例

```
Studio photograph of a next-generation dry-magnet 3T MRI scanner, 
featuring a highly visible 65cm scanning bore cavity defining its front orientation, 
with a patient cradle track extending from the front...
```

### 错误示例

```
Studio photograph of a solid basalt slab, 250cm long and 40cm thick, 
with a precise circular aperture recessed flush into its center...
```
- ❌ 问题：缺少品类锚定词（MRI scanner），纯几何体（slab）替代了产品原型

---

## 禁止纯几何替代（No Pure Geometry Substitution）

### 规则

严禁用纯几何体（slab, cube, cylinder, ring）完全替代行业原型词。几何体只能作为形态修饰，不能作为语义主语。

### 转换表

| ❌ 错误（纯几何替代） | ✅ 正确（原型锚定 + 几何修饰） |
|----------------------|------------------------------|
| A solid basalt slab | A monolithic MRI scanning enclosure with a 65cm bore cavity, surfaced in honed basalt |
| A cylindrical ring | A dry-magnet MRI scanner with a cylindrical bore housing, wrapped in bead-blasted aluminum |
| Two parallel plates | A split-configuration MRI scanner with upper and lower magnetic shroud plates |
| A glass cube | A compact espresso machine with a glass-enclosed brew chamber |

---

## 在 15 步流程中的注入点

### 注入点 1：STEP-05.7（核心矛盾提炼后）

在核心矛盾提炼后、候选生成前，强制运行原型锚定门：

1. 列出该品类的【不可缩减三大形态特征】
2. 验证每个特征的视觉权重（> 40% / > 20% / > 30%）
3. 定义功能暗示词（至少 3 个）
4. 计算尺度校验公式

### 注入点 2：STEP-15（提示词编译）

在提示词编译阶段，强制追加原型 Legibility 校验：

1. 提示词第一段是否包含品类锚定词？（如 MRI scanner / espresso machine）
2. 是否描述了关键宏观大部件与轴向？
3. 是否包含至少一个功能暗示词？
4. 是否避免了纯几何替代？

---

## 与其他方法的关系

| 方法/文档 | 关系 |
|-----------|------|
| `end-to-end-workflow.md` STEP-05.7 | 本指南是 STEP-05.7 的详细展开 |
| `end-to-end-workflow.md` STEP-15.6 | 原型 Legibility 校验是 STEP-15.6 的子项 |
| `prompt-engineering.md` 方法14（品类锚定法） | 本指南是方法14的工业系统增强版 |
| `prompt-engineering.md` 方法24-26 | 三级细节加载是原型锚定后的细节增强 |
| `design-ir.md` `archetype_features` | 本指南定义了 `archetype_features` 字段的填写规范 |
| `pitfall-060-debranding-and-legibility.md` | 本指南是 pitfall-060 的预防性措施 |
| `pitfall-061-material-responsibility-violation.md` | 本指南与 pitfall-061 共同构成材料诚实性约束 |

---

## 来源

- 审计报告：2026-06-24 联影医疗MRI设计审计（用户提交）
- 核心病灶：产品无法识别为医疗设备，被误判为建筑/家具
- 根因分析：缺乏行业原型锚定，纯几何替代切断了品类语义联系
- 艾维案例：Moncler合作款（保留马灯提手）、Linn LP12（保留方形底座与圆盘）
- 升级触发：用户反馈"完全看不出是何物"
