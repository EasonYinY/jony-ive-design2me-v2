---
reference_id: PITFALL-034
title: 方向同质化陷阱
category: cases
used_when:
  - 多代理并行设计
  - STEP-09六轴差异门检查
called_by:
  - end-to-end-workflow.md
  - iteration-workflow.md
depends_on:
  - REF-PROCESS-001
outputs:
  - direction_diversity_check
---

# Pitfall 034: 方向同质化陷阱

> **版本**: 3.0
> **日期**: 2026-06-24
> **触发**: 2026-06-24 下一代载人飞行器任务，3个方向全部使用"环"作为核心结构元素（D1双环围绕/D2张力悬吊/D3单环贯穿），用户反馈"为什么全都是环，希望能更有想法一点，不要全部用同一种元素"
> **严重级别**: 🔴 高
> **审计升级**: 2026-06-24 资深设计流程审计师提交结构性诊断报告，指出"结构家族"概念仍属低维几何分类，需升级为"拓扑去同质化断路器"（基于艾维大脑架构 v4.1 的物理叙事坐标）

---

## 问题描述

当多个候选/方向共享同一个核心结构元素时，导致**结构轴同质化**——六轴差异门在"结构"维度上无法通过，用户感知为"三个方向只是同一个想法的变体"。

**2026-06-24 载人飞行器实证（V1.0 失败）**:
- D1: 双环围绕弦月舱 → 核心结构：**环** (torus)
- D2: 张力悬吊水滴舱 → 核心结构：**环** (torus) ×2
- D3: 单环贯穿椭球舱 → 核心结构：**环** (torus)
- **结果**: 3个方向100%共享"环"结构元素，用户感知为"全都是环"

**V2.0 修复尝试（仍不充分）**:
- D1: 茧形舱（壳家族）→ 仍属"包裹型"几何，缺乏物理叙事深度
- D2: 折叠翼（翼家族）→ 仍触发生物形态俗套
- D3: 太阳能帆板（板家族）→ 仍依赖"外挂结构"表达功能
- **审计结论**: "结构家族"只是低维几何分类，未触及"形态从关系中自然浮现"的本质

---

## 同质化类型（V3.0 高维审计版）

### 类型1: 科幻陈词滥调同质化（Sci-fi Cliché Homogeneity）

**现象**: LLM自动检索概率场中最密集的科幻视觉意象（环、圈、格栅、阵列），而非从关系命题中自然推导形态
**根因**: 系统未让形态从"人与天空的关系"中自然浮现，而是将"Jony Ive风格"误解为"把科幻片里的飞船刷成苹果白"
**审计引用**: 艾维大脑架构 v4.1 方法1——"关系命题必须让形态自然浮现，而非抓取既有符号"

### 类型2: 低维几何分类同质化（Low-dim Geometry Homogeneity）

**现象**: "结构家族"（环/板/壳/杆/翼/场）只是几何形状的分类，未触及物理叙事本质
**根因**: 壳家族（茧形）vs 翼家族（折叠翼）vs 板家族（帆板）——三者仍可能共享"包裹/外挂/附加"的同一物理逻辑
**审计结论**: 需升级为"物理叙事坐标"——从"形态是什么"转向"形态如何承载关系"

### 类型3: 情绪词/时间词/风格抽象词污染（Semantic Noise Homogeneity）

**现象**: 提示词中出现"futuristic""sleek""cybernetic""sense of safety""spinning slowly"等词汇
**根因**: LLM缺乏真实工程架构感知，用抽象词替代物理描述
**模型后果**: Lovart Nano Banana Pro 无法理解时间状态动词和情绪词，转化为视觉噪声，导致结构性扭曲（Artifacts）

### 类型4: 材料贴图化同质化（Texture-map Homogeneity）

**现象**: 材料描述写成"white matte plastic shell""transparent glass window"——质感贴图而非材料职责
**根因**: 未理解艾维语境中"材料必须承担行为或物理转换"
**纠偏**: 必须描述材料的结构职责（如"smoked glass slab suspended over travertine base"）

---

## 高维解决方案：拓扑去同质化断路器（V3.0）

### 核心升级：从"结构家族"到"物理叙事坐标"

**审计师诊断**: 当Brief涉及复杂或具有未来感的产品时，AI必须强制进行【拓扑解耦】，禁止连续2个方案使用同一种核心几何形（如圆环、球体、阵列格栅）。

**必须从以下四个完全对立的物理叙事坐标中，强制选择3个互不交叉的架构**：

| 物理叙事坐标 | 艾维思想源头 | 映射至复杂产品的泛化隐喻 | 物理动词表达 |
|------------|------------|----------------------|------------|
| **Monolithic Slab（单体方碑）** | iPod玻璃镜面 / Mouse曜石单片 | 飞行器表现为一块悬浮的、无缝的几何体。没有外部机械外挂，动力与交互完全隐匿于不可见的底部接合线内。 | Floats, unbroken glass, flush intake slit, sweeping tangent |
| **Monocoque Tension Shell（张力外壳）** | Ferrari Luce进气秩序 / Moncler一体拉链 | 放弃任何外包结构。将飞行器视为由内部骨架向外撑起的张力皮肤，结构即外壳，利用极具张力的曲面弧度（G2连续）暗示空气动力学。 | Taut carbon skin, stretched membrane, bone-line crispness |
| **Volumetric Subtraction（负空间雕刻）** | Linn LP12-50铝块切削 / Christie's讲台内凹 | 飞行器是一个完美的正几何体，空间不是向外叠加结构，而是向内雕刻出供人类乘坐的"仪式感舱位"，露出极致打磨的内部构件。 | Carved travertine, hollowed oblate, recessed inner horizon |
| **Tensegrity（张力悬吊）** | （仅限极端悬浮需求） | 严禁实体环，改用极致纤细的拉索与纯粹的体块平衡。 | （慎用，需审计师批准） |

**硬性规则**: 三个方向必须来自**三个不同的物理叙事坐标**，禁止两个方向共享同一坐标。

---

## 五段式物理空间协议（V3.0 提示词模板）

**审计师强制要求**: 每个方案的英文Prompt必须严格遵循以下5段式物理空间布局，严禁任何情绪词、时间词与风格抽象词。

```markdown
[Layout Block 1: 视角与空间锚定]
Studio photograph, [视角，如 three-quarter view slightly above / eye-level dead-front view], of a single [产品中性核心词], LoveFrom 2030, post-Apple Jony Ive.

[Layout Block 2: 核心拓扑与材质职责 (Material Duty)]
[主要构件材质] slab/shell [物理动作，如 suspended over / flush integrated into] a [基座材质] base, [次要材质] [物理交接状态，如 flush in / recessed into].

[Layout Block 3: 极致几何与切线控制 (G2 Fillet & Tangent)]
G2 fillet edges, sweeping tangent into [交接面], [精确微观尺寸描述，如 0.5mm hairline seam / hairline amber LED slit].

[Layout Block 4: 消失设计与行为触点 (Vanishing & Tactile Node)]
[材质] tactile node [功能，如 for physical override] positioned at [精确位置]. Unseen elements perfectly aligned. Floats. Neutral gradient.

[Layout Block 5: 绝对排除项 (Negative Filter)]
No logo, no text, no visible screws, no visible joints, no redundant mechanical decoration, no sci-fi rings.
```

**禁止词滤网（绝对禁止进入Prompt）**:
- ❌ futuristic, sleek, cybernetic, sci-fi, high-tech
- ❌ Apple-like, minimalist design, Jony Ive style
- ❌ sense of safety, feeling of trust, emotional connection
- ❌ spinning slowly, gently hovering, gracefully flying
- ❌ white matte plastic shell, transparent glass window（材料贴图化）

---

## 检查清单（V3.0 审计增强版）

### STEP-06候选生成前检查

```
[ ] 是否列出四个物理叙事坐标（Monolithic Slab / Monocoque Shell / Subtraction / Tensegrity）？
[ ] 每个候选是否来自不同的物理叙事坐标？
[ ] 是否有候选依赖"环、圈、格栅、阵列"等科幻陈词滥调？（有 = 否决）
[ ] 形态是否从"人与产品的关系"中自然浮现？（而非抓取既有符号）
[ ] 是否考虑了"不被看见的部分"（底面接合线、铰链、进气口边缘倒角）？
```

### STEP-09六轴差异门检查

```
[ ] 关系维度是否不同？（信任/掌控/冒险）
[ ] 结构维度是否不同？（物理叙事坐标是否唯一）
[ ] 操作维度是否不同？
[ ] 材料维度是否不同？
[ ] 工艺维度是否不同？
[ ] 颜色维度是否不同？
[ ] 形态维度是否不同？
[ ] 文化维度是否不同？
[ ] 物理叙事坐标是否唯一？（V3.0核心检查）
```

### 提示词编译检查（STEP-15）

```
[ ] 是否遵循五段式物理空间协议？
[ ] 是否包含任何情绪词/时间词/风格抽象词？（有 = 删除）
[ ] 材料描述是否使用"Material Duty"格式（结构职责+触感职责+物理交接）？
[ ] 是否包含"不被看见的部分"的描述（底面接合线、隐藏进气口）？
[ ] 负面约束是否包含"no sci-fi rings"？
```

---

## 修复案例：2026-06-24 载人飞行器（V3.0 审计级修复）

**V1.0问题**: D1/D2/D3全部使用"环"结构
**V2.0问题**: "结构家族"只是低维几何分类，未触及物理叙事本质

**V3.0审计级修复方案**:

| 方向 | 物理叙事坐标 | 核心结构 | 材料职责 | 禁止元素 |
|------|------------|----------|----------|----------|
| D1 | **Monolithic Slab** | 抛光钛合金单体板，前宽后窄，弧面玻璃与外壳平齐 | 钛合金承载结构+玻璃视野职责 | 无可见引擎、无螺旋桨、无外挂 |
| D2 | **Monocoque Tension Shell** | 陶瓷化碳纤维一体成型流线外壳，微型平齐进气口 | 碳纤维张力皮肤+陶瓷隔热职责 | 无机翼、无套圈、无缆索 |
| D3 | **Volumetric Subtraction** | 精密喷砂铝合金扁椭球，前方负空间切削出乘员舱 | 铝块结构+编织物内衬触感职责 | 无外挂结构、无附加装饰 |

**修复后差异**:
- D1: 单体方碑——动力完全隐匿，靠无缝单片表达
- D2: 张力外壳——结构即皮肤，靠曲面张力表达
- D3: 负空间雕刻——向内切削，靠消失的体量表达

**三个方向物理叙事坐标互不相同，无共享，无科幻陈词滥调。**

---

## 相关引用

- REF-PROCESS-001: 四阶段十五步主流程
- REF-RULE-ORCH: 三方向差距编排框架
- REF-DIRECTION-004: 六轴/七轴差异门
- PITFALL-031: 准艾维级天花板突破
- PITFALL-032: 文化杂交显性化陷阱
- PITFALL-035: 惊喜时刻同质化
- **艾维大脑架构 v4.1**: 关系命题、材料职责、触觉节点、时间盟友

---

## 来源

- 技能: jony-ive-design2me-v2
- 迭代: Round 2（材料/操作同质化）
- 实证: 2026-06-24 下一代载人飞行器（结构同质化——3个方向全部使用环）
- **审计升级**: 2026-06-24 资深设计流程审计师提交结构性诊断报告，触发V3.0高维重构
