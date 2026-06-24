---
reference_id: REF-CASES-NEW
title: 失败模式库 (Failure Patterns)
category: cases
used_when:
called_by:
  - all-workflows
  - image-generation
  - prompt-compilation
depends_on:
  - REF-GUIDE-008
  - REF-PROMPT-002
  - REF-QUALITY-002
outputs:
  - failure_pattern_knowledge
---

# 失败模式库 (Failure Patterns) — 泛用版 旧版

> **版本**: 2.0
> **日期**: 2026-06-21
> **触发**: 2轮迭代，6张图全部失败，用户评分1/10
> **性质**: 泛用性Bug，影响所有消费电子产品AI图像生成任务
> **适用范围**: 所有需要"突破传统+保留品类识别"的产品设计任务

---

## 概述

本文件记录 jony-ive-design2me-v2 技能在AI图像生成过程中发现的系统性失败模式。这些模式不是单次执行错误，而是**结构性设计缺陷**，影响所有需要"突破传统+保留品类识别"的产品设计任务。

**核心死结**:
```
说品类词 → 模型渲染默认品类原型（无突破）
不说品类词 → 模型不认识品类（不像目标产品）
说品类词 + 突破约束 → 模型忽略突破约束（仍是默认原型）
```

**泛用性原则**: 以下模式适用于任何消费电子产品（鼠标、咖啡机、耳机、手机、灯具、家具等），不限于特定品类。

---

## 模式1: 概念覆盖（Concept Override）

- **触发**: 提示词中出现品类词（mouse/phone/coffee maker/headphone/lamp/chair）
- **现象**: 模型渲染默认品类原型，忽略所有突破约束
- **根因**: 模型对品类词的训练强度远高于对突破约束的训练
- **修复**: 使用"品类锚定法"（方法14）——保留品类词但立即否定默认原型
- **泛用示例**:
  ```
  ❌ "A wireless mouse, LoveFrom 2030, extremely flat glass slab..."
     → 渲染默认鼠标（蛋形，塑料，无突破）
  
  ✅ "A mouse that doesn't look like any mouse. Paper-thin glass slab..."
     → 渲染突破形态（扁平板状，玻璃，有识别性）
  ```

---

## 模式2: 品类丢失（Category Loss）

- **触发**: 删除品类词以避免默认原型（如删除"mouse""coffee maker"）
- **现象**: 模型不认识产品，生成抽象物体（玻璃板/塔/鹅卵石/石头）
- **根因**: 模型需要品类词来建立产品认知框架
- **修复**: 必须保留品类词，但立即否定默认原型
- **泛用示例**:
  ```
  ❌ "Extremely flat rectangular slab, smoked glass, hairline metal..."
     → 像玻璃板/手机/平板，不像任何已知产品
  
  ✅ "A coffee maker that doesn't look like any coffee maker. Black stone slab..."
     → 像咖啡机，但突破传统
  ```

---

## 模式3: 数字忽略（Number Blindness）

- **触发**: 提示词包含数字（mm/°/ratio/比例/尺寸/角度）
- **现象**: 数字被完全忽略，渲染默认比例
- **根因**: 图像生成模型无法理解精确数字，只理解相对概念
- **修复**: 删除所有数字，使用比例形容词（"paper-thin""tower-like""slender"）
- **泛用示例**:
  ```
  ❌ "120mm long, 12mm thick, 10:1 aspect ratio, 45-degree angle"
     → 数字被忽略，渲染默认比例
  
  ✅ "Paper-thin, extremely flat, slender, leaning forward"
     → 模型理解相对比例
  ```

---

## 模式4: 材料简化（Material Simplification）

- **触发**: 材料描述复杂（多层/多种/工程词汇/化学名称）
- **现象**: 材料被渲染为塑料或默认材质
- **根因**: 模型对复杂材料描述的遵循度有限
- **修复**: 单一主材，感官词汇，强调表面处理
- **泛用示例**:
  ```
  ❌ "Smoked glass slab body with hairline-brushed titanium border and transparent glass base"
     → 渲染为塑料+金属漆
  
  ✅ "Smoked glass, hairline metal edge"
     → 玻璃+金属，材料诚实
  ```

---

## 模式5: 背景污染（Background Pollution）

- **触发**: 背景描述不够强烈或过于复杂
- **现象**: 背景出现环境元素（桌面/地面/阴影/反射/房间/天空）
- **根因**: 模型默认渲染环境场景
- **修复**: 使用强烈否定"pure white, no ground, no shadow, no environment"
- **泛用示例**:
  ```
  ❌ "White background"
     → 可能出现灰色渐变、地面阴影、环境反射
  
  ✅ "Pure white background, no ground, no shadow, no environment"
     → 纯白无环境
  ```

---

## 模式6: 细节抹除（Detail Erasure）

- **触发**: 细节描述>3个（LED/纹理/按钮/接口/螺丝/刻字）
- **现象**: 所有细节被忽略，产品表面光滑无特征
- **根因**: 模型对细节的渲染能力有限，优先保留大形态
- **修复**: 只保留1-2个核心细节，用形态暗示功能
- **泛用示例**:
  ```
  ❌ "Hairline LED slit, micro-bumps, hidden scroll wheel, copper accent line, magnetic haptic feedback, brand engraving"
     → 所有细节被忽略
  
  ✅ "No buttons visible, copper accent line"
     → 保留2个核心细节
  ```

---

## 模式7: 交互不可见（Interaction Invisible）

- **触发**: 提示词包含交互描述（click/scroll/touch zone/press/slide/rotate）
- **现象**: 交互被忽略，产品无操作界面
- **根因**: 模型无法渲染"功能"，只能渲染"形态"
- **修复**: 删除交互描述，用形态暗示功能（"no buttons visible"暗示触控）
- **泛用示例**:
  ```
  ❌ "Index finger touch zone, middle finger scroll zone, pressure-sensing click, thumb slide control"
     → 无操作界面，光滑表面
  
  ✅ "No buttons visible, seamless surface, single copper line"
     → 暗示触控操作
  ```

---

## 模式8: 文化概念丢失（Cultural Concept Loss）

- **触发**: 提示词包含文化杂交概念（"Cultural hybrid: X × Y""Inspired by Z"）
- **现象**: 文化概念被忽略或简化为装饰元素
- **根因**: 模型无文化杂交训练数据，无法表达抽象文化关系
- **修复**: 删除文化概念，保留视觉描述（"tower-like"代替"五重塔"）
- **泛用示例**:
  ```
  ❌ "Cultural hybrid: Japanese five-story pagoda × modern vertical mouse"
     → 概念被忽略
  
  ✅ "Tower-like, layered, slender"
     → 视觉描述可渲染
  ```

---

## 模式9: 人体工学不可见（Ergonomics Invisible）

- **触发**: 提示词包含人体工学描述（wrist/palm/hand/posture/grip/angle）
- **现象**: 人体工学被忽略，产品形态不符合人体
- **根因**: 模型无法渲染"人体关系"，只能渲染"物体形态"
- **修复**: 删除人体工学，在DesignIR中保留，不在提示词中表达
- **泛用示例**:
  ```
  ❌ "Palm hovers 20-30mm above body, wrist neutral posture, finger touch zone, ergonomic grip"
     → 人体工学被忽略
  
  ✅ （删除所有人体工学，用形态暗示："slender tower"暗示垂直握持）
  ```

---

## 模式10: 功能说明丢失（Function Description Loss）

- **触发**: 提示词包含功能说明（sensor/feedback/pressure/tilt/heat/brew/grind）
- **现象**: 功能被忽略，产品无功能特征
- **根因**: 模型无法渲染"功能"，只能渲染"外观"
- **修复**: 删除功能说明，用形态暗示功能
- **泛用示例**:
  ```
  ❌ "Pressure-sensing click, magnetic haptic feedback, optical tracking sensor, temperature control"
     → 功能不可见
  
  ✅ "Seamless surface, no visible buttons, small display window"
     → 暗示触控+隐藏功能
  ```

---

## 模式11: 功能性按键/操作描述的渲染失败（Functional Control Rendering Failure）

- **触发**: 提示词包含功能性按键、旋钮、开关、接口等操作元素的精确描述
- **现象**: 
  - 按键被渲染为装饰性凸起而非真实按钮
  - 旋钮被渲染为圆形纹理而非可旋转部件
  - 开关被渲染为线条而非拨动机构
  - 接口被渲染为凹陷而非真实插孔
- **根因**: 
  - 模型理解"按钮"概念但无法理解"按压反馈"
  - 模型理解"旋钮"概念但无法理解"旋转阻尼"
  - 模型缺乏对功能性操作细节的精细训练数据
- **修复**: 
  - **用形态暗示功能，不用功能描述形态**
  - "flush circular depression" 代替 "rotary knob with detents"
  - "slight raised line" 代替 "slide switch"
  - "small rectangular recess" 代替 "USB-C port"
  - **保留1-2个核心操作暗示，删除所有功能性描述**
- **泛用示例**:
  ```
  ❌ "Rotary knob with 24 detents, tactile feedback, aluminum construction, 30mm diameter"
     → 渲染为圆形纹理或装饰盘
  
  ✅ "Flush circular depression, subtle texture"
     → 暗示旋钮位置，不描述功能
  ```

---

## 模式12: 多部件装配关系渲染失败（Multi-Part Assembly Rendering Failure）

- **触发**: 提示词包含多个部件的装配关系（A connects to B, C slides over D）
- **现象**: 
  - 部件被渲染为单一整体
  - 装配间隙被忽略
  - 连接结构被简化为纹理
- **根因**: 模型擅长渲染单一物体，不擅长渲染装配关系
- **修复**: 
  - 描述为"单一形态"而非"多个部件"
  - 用"seamless""monolithic"暗示整体感
  - 如需表达分层，用"layered"而非"part A + part B"
- **泛用示例**:
  ```
  ❌ "Base connects to body via magnetic coupling, top cap rotates independently"
     → 渲染为单一物体或混乱结构
  
  ✅ "Layered monolithic form, subtle seam lines"
     → 暗示分层但整体感
  ```

---

## 模式13: 动态/使用状态渲染失败（Dynamic State Rendering Failure）

- **触发**: 提示词包含动态描述（tilt/rotate/flex/extend/fold/open/close）
- **现象**: 
  - 动态被忽略，渲染静态形态
  - 或渲染为破碎/错误结构
- **根因**: 模型只能渲染静态图像，无法表达动态
- **修复**: 
  - 删除所有动态描述
  - 用静态形态暗示动态能力（"hinge line"暗示可折叠）
  - 只渲染"静息状态"
- **泛用示例**:
  ```
  ❌ "Folding mechanism allows 180-degree rotation, compact when closed, extended when open"
     → 渲染为破碎结构或忽略动态
  
  ✅ "Slight hinge line, compact form"
     → 暗示可折叠，不描述动态
  ```

---

## 修复总结：品类锚定法（方法14）+ 功能暗示法（方法15）

### 核心原则

1. **保留品类词**（让模型知道"这是什么"）
2. **立即否定默认原型**（让模型知道"不要长这样"）
3. **极端突破形态**（让模型知道"要长这样"）
4. **删除所有不可渲染字段**（数字/交互/功能/文化/人体工学/动态）
5. **用形态暗示功能**（"no buttons visible"暗示触控，"flush depression"暗示旋钮）
6. **渲染静态静息状态**（不描述动态/使用状态）

### 三段式结构（基础版）

```
1. 品类锚定: "A [品类] that doesn't look like a [品类]"
2. 突破形态: "[极端形态词], [非传统材料], [识别性特征]"
3. 背景控制: "Floats. Pure white. No ground."
```

### 五段式结构（功能暗示版）

适用于需要保留功能性操作暗示的产品（咖啡机、音响、灯具等）：

```
1. 品类锚定: "A [品类] that doesn't look like a [品类]"
2. 突破形态: "[极端形态词], [非传统材料]"
3. 功能暗示: "[形态暗示1], [形态暗示2]"（如"no buttons visible, flush circular depression"）
4. 识别性特征: "[1-2个核心细节]"（如"copper accent line, subtle texture"）
5. 背景控制: "Floats. Pure white. No ground."
```

### 检查清单

- [ ] 包含品类词？
- [ ] 包含否定默认原型？
- [ ] 突破形态极端？
- [ ] 无数字？
- [ ] 无交互描述？
- [ ] 无功能说明？
- [ ] 无文化概念？
- [ ] 无人体工学？
- [ ] 无动态描述？
- [ ] 功能暗示用形态表达（非功能描述）？
- [ ] 多部件描述为单一形态？
- [ ] 背景纯净？

---

## 产品类型适配表

| 产品类型 | 品类词 | 突破形态示例 | 功能暗示示例 | 识别性特征 |
|----------|--------|-------------|-------------|-----------|
| 鼠标 | mouse | paper-thin glass slab | no buttons visible, flush surface | hairline metal edge |
| 咖啡机 | coffee maker | black stone slab | recessed cup well, brass drip | copper accent line |
| 耳机 | headphones | two carbon rings | no headband, tension lines | kevlar texture |
| 手机 | phone | tall narrow glass monolith | no visible camera, seamless back | ceramic white edge |
| 灯具 | lamp | floating circular disc | no visible switch, thin power line | warm glow edge |
| 椅子 | chair | single curved shell | no legs, cantilever base | matte black surface |
| 手表 | watch | thin rectangular face | no crown, seamless band | sapphire crystal edge |
| 音箱 | speaker | tall cylindrical tower | no visible drivers, fabric wrap | brass base ring |

---

## 来源

- Round 1 失败分析：用户评分 1/10，提示词过载
- Round 2 失败分析：用户评分 1/10，品类识别为零
- Round 3 验证：无线充电器设计，首次达到艾维级（D1=80, D3=82），品类锚定法有效
- 模型失效模式：Lovart Nano Banana Pro / Nano Banana 2 输出分析
- REF-GUIDE-008: 提示词工程方法（方法13+方法14）
- REF-GUIDE-015: 功能暗示法（方法15）
- REF-PROMPT-002: 中文提示词压缩规则
- REF-QUALITY-002: 图片评审合同
- 用户反馈：2026-06-21 "修复方案要具备广泛性，其他产品都能用"
