---
reference_id: REF-GUIDE-019-03
title: 焦点强调可视化指南
category: guides
used_when:
  - PROMPT-COMPILATION
called_by:
  - prompt-engineering
  - focal-point-design
depends_on:
  - REF-PROMPT-001
  - REF-PROMPT-004
outputs:
  - focal_point_emphasis_method
---

# 焦点强调可视化指南

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 3 D2涟漪波纹中心凹陷在图片中不够明显，导致识别性扣分

---

## 概述

本指南解决提示词中"焦点特征"（如中心凹陷、关键纹理、标志性细节）在图片生成中被模型弱化或忽略的问题。

## 核心问题

当提示词包含多个特征时，模型倾向于渲染"整体印象"而非"精确焦点"。中心凹陷、关键纹理等细节常被平滑化。

## 焦点强调方法

### 方法1: 重复强调法

在提示词中重复关键特征2-3次，增加模型注意力权重。

```
❌ "中心凹陷定位"
✅ "中心凹陷定位，明显的中心凹陷，凹陷深度清晰可见"
```

### 方法2: 对比强调法

通过明暗/材质对比突出焦点。

```
❌ "中心凹陷"
✅ "中心凹陷，凹陷区域哑光，周围区域抛光，对比突出"
```

### 方法3: 尺度强调法

明确焦点的相对尺度，帮助模型理解重要性。

```
❌ "中心凹陷"
✅ "中心凹陷，占据表面40%面积，最显著特征"
```

### 方法4: 位置强调法

明确焦点的精确位置，避免模型随机放置。

```
❌ "中心凹陷"
✅ "正中心凹陷，几何中心点，精确居中"
```

## 检查清单

- [ ] 焦点特征在提示词中出现≥2次
- [ ] 焦点有明暗/材质对比
- [ ] 焦点的相对尺度已说明
- [ ] 焦点的精确位置已说明
- [ ] 焦点不是提示词中唯一的细节（避免过度强调）

## 示例

### 涟漪波纹充电器（修正后）

```
Studio photograph, LoveFrom 2030.
A wireless charger that doesn't look like any wireless charger.
Aluminum disc with concentric ripple waves, 
CENTER凹陷定位（占据表面40%，凹陷区域哑光，周围抛光，对比突出），
micro-blasted matte surface, continuous seamless waves.
Floats. Pure white background.
No logo, no text, no screws.
```

## 来源

- Round 3 失败分析：D2涟漪波纹中心凹陷不够明显，识别性扣分
- REF-GUIDE-008: 提示词工程方法
