---
reference_id: REF-GUIDE-022
title: 动态形态图片表达指南
version: 1.0
category: guides
used_when:
  - DYNAMIC-FORM-DESIGN
called_by:
  - end-to-end-workflow
  - product-design
depends_on:
  - REF-GUIDE-001
  - REF-CASE-026
outputs:
  - dynamic_form_visualization_spec
---

# 动态形态图片表达指南 (Dynamic Form Visualization)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 2 D2 折叠泵压、D3 螺旋加压 — 动态形态在静态图片中难以表达

---

## 问题定义

折叠、螺旋、展开等动态形态在静态图片中面临挑战：
- 折叠机构：只能展示一个状态（折叠或展开），无法展示动态
- 螺旋结构：旋转动态在静态图中不可见
- 展开机构：展开过程无法展示

**核心问题**: 如何在静态图片中暗示动态形态的变化和可能性？

---

## 解决方案

### 方案1: 多状态暗示法

在单一图片中暗示多个状态：

```
Method: 部分展开/部分折叠
Example: 折叠杠杆咖啡机
  - 杠杆展开至60°（非完全展开120°）
  - 暗示"正在展开"的动态过程
  - 铰链缝隙可见，暗示折叠可能性

Prompt: "Lever partially unfolded at 60° angle, hinge gap visible,
         suggesting dynamic folding capability, mechanical tension implied"
```

### 方案2: 动态线条法

使用线条暗示运动轨迹：

```
Method: 螺旋线/弧线暗示旋转
Example: 螺旋加压咖啡机
  - 螺旋线从底部到顶部
  - 暗示"旋转上升"的动态
  - 螺旋线光影变化暗示运动方向

Prompt: "Spiral lines ascending from base to top, light raking across spiral
         creating dynamic shadows, suggesting rotational motion"
```

### 方案3: 残影/轨迹法

使用轻微残影暗示运动：

```
Method: 运动轨迹的轻微暗示
Example: 旋转旋钮
  - 旋钮边缘轻微模糊（暗示旋转）
  - 或旋钮位置偏离中心（暗示可旋转）

Prompt: "Knob slightly rotated off-center, suggesting rotational capability,
         subtle motion blur on knob edge"
```

### 方案4: 多视角组合法

使用构图暗示多视角：

```
Method: 单一图片包含多个视角暗示
Example: 折叠机构
  - 主体正面展示折叠状态
  - 杠杆侧面展示展开角度
  - 铰链特写展示精密配合

Prompt: "Three-quarter view showing both folded body and partially unfolded lever,
         hinge detail visible, dynamic composition"
```

### 方案5: 光影动态法

使用光影变化暗示动态：

```
Method: 光影方向暗示运动方向
Example: 螺旋柱
  - 光从斜上方照射
  - 螺旋线阴影方向暗示旋转上升
  - 光影对比强调动态感

Prompt: "Light raking from upper left, spiral shadows creating dynamic pattern,
         suggesting upward rotational motion"
```

---

## 动态形态提示词模板

### 折叠机构

```
"Folding [product], [folded/extended] form, [angle]° hinge angle visible,
 [hinge material] precision hinge with [gap]mm gap, shadow line emphasizing fold,
 dynamic composition suggesting [folding/unfolding] motion,
 [secondary element] positioned to imply [state change]"
```

### 螺旋机构

```
"Spiral [product], [pitch]mm pitch spiral lines, [direction] ascending from base,
 light raking across spiral creating dynamic shadows, [node material] nodes at [interval],
 suggesting rotational [compression/extension] motion,
 [base material] weighted base providing stability"
```

### 旋转机构

```
"Rotating [product], [knob/dial] positioned at [angle]° off-center,
 suggesting rotational capability, [indicator] showing [position/state],
 dynamic composition with [element] implying motion,
 [material contrast] emphasizing rotational element"
```

---

## 自检清单

```
[ ] 动态形态有具体角度/位置暗示
[ ] 光影/阴影暗示运动方向
[ ] 构图包含动态元素（非完全静态）
[ ] 材料对比强调动态部件
[ ] 无"dynamic""motion"等抽象词，用具体视觉描述替代
```

---

## 来源

- Round 2 实证: D2折叠泵压、D3螺旋加压动态形态表达分析
- REF-GUIDE-001: 视觉张力比例指南
- REF-CASE-026: 提示词→图片衰减
- 日期: 2026-06-21
