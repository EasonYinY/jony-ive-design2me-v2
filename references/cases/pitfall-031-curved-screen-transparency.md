---
reference_id: REF-CASE-031
title: Pitfall 031 — 曲面屏幕透明度
category: cases
used_when:
  - SCREEN-DESIGN
  - CURVED-SURFACE
called_by:
  - end-to-end-workflow
  - pitfall-026
depends_on:
  - REF-GUIDE-021
outputs:
  - curved_screen_warning
---

# Pitfall 031 — 曲面屏幕透明度 (Curved Screen Transparency)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 5 智能手表迭代 — 曲面蓝宝石屏幕在AI生成中偏白
> **严重程度**: 🟡 中

---

## 现象

曲面蓝宝石/玻璃屏幕在AI生成中常偏白或不透明：
- 曲面屏幕看起来像白色塑料而非透明玻璃
- 屏幕下的内容（时间显示）不可见
- 折射效果缺失

Round 5 方向B（水滴表）的曲面蓝宝石屏幕有表达但透明度不足。

---

## 根因分析

### 根因1: AI对"曲面+透明"的理解偏差

AI将"curved"和"transparent"分开理解，无法同时处理两个属性。

### 根因2: 缺少折射描述

未描述光线穿过曲面屏幕的折射效果。

### 根因3: 缺少屏幕下内容描述

未描述屏幕下可见的内容（时间显示、传感器）。

---

## 解决方案

### 策略1: 使用强透明词

```
✅ "optically clear curved sapphire""transparent curved glass"
✅ "crystal clear curved surface""invisible curved screen"
```

### 策略2: 描述折射效果

```
✅ "light bends through curved surface""refraction visible at edges"
✅ "background distorts through curved glass"
```

### 策略3: 描述屏幕下内容

```
✅ "time display visible beneath curved surface"
✅ "subtle glow visible through transparent screen"
✅ "display elements visible under glass"
```

---

## 验证方法

```
[ ] 使用"optically clear""crystal clear"等强透明词
[ ] 描述折射效果
[ ] 描述屏幕下可见内容
[ ] 评审中检查屏幕透明度
```

---

## 关联

- 相关 Guide: 021（透明材料表达）
- 相关案例: Round 5 水滴表（曲面屏幕透明度）

---

## 来源

- Round 5 实证: references/iterations/round-5/image-analysis.md
- 日期: 2026-06-21
