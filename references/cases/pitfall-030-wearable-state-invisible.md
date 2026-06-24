---
reference_id: REF-CASE-030
title: Pitfall 030 — 佩戴状态不可见
category: cases
used_when:
  - PRODUCT-SELECTION
  - WEARABLE-DESIGN
called_by:
  - end-to-end-workflow
  - iteration-workflow
depends_on:
  - REF-CASE-029
outputs:
  - wearable_state_warning
---

# Pitfall 030 — 佩戴状态不可见 (Wearable State Invisible)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 5 智能手表迭代 — 佩戴状态在静态图中不可见
> **严重程度**: 🟡 中

---

## 现象

手表、耳机、眼镜等可穿戴产品的佩戴状态在静态图中不可见：
- 表体与手腕的贴合关系无法展示
- 表带缠绕手腕的形态无法展示
- 传感器与皮肤的接触无法展示

Round 5 方向A（时间环）和C（折叠带）因佩戴状态不可见，评分受影响。

---

## 根因分析

### 根因1: 静态图无法展示动态关系

静态图展示的是产品本身，而非产品与人体的关系。

### 根因2: AI对"佩戴"的理解偏差

AI可能将"on wrist"理解为"放在手腕旁边"而非"贴合手腕"。

### 根因3: 人体模型缺失

提示词中未包含人体模型/手腕模型作为参考。

---

## 解决方案

### 策略1: 提示词中描述佩戴状态

```
✅ "worn on wrist""conforms to wrist curve""wraps around wrist"
✅ "flush with skin""sits flat on wrist"
```

### 策略2: 使用人体模型参考

```
✅ "on mannequin wrist""wrist model reference"
✅ "human wrist 170mm circumference"
```

### 策略3: 接受静态图限制

在评审中备注：
```
⚠️ 佩戴状态需实物验证
⚠️ 人体工学评分基于设计意图，非图片验证
```

---

## 验证方法

```
[ ] 提示词包含佩戴状态描述
[ ] 有人体模型参考（可选）
[ ] 评审备注"佩戴状态需实物验证"
```

---

## 关联

- 相关 Pitfall: 029（复杂产品衰减）
- 相关案例: Round 5 智能手表（佩戴状态不可见）

---

## 来源

- Round 5 实证: references/iterations/round-5/image-analysis.md
- 日期: 2026-06-21
