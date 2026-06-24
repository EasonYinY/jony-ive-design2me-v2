---
reference_id: REF-GUIDE-020-03
title: 悬浮间隙可视化指南
category: guides
used_when:
  - PROMPT-COMPILATION
called_by:
  - prompt-engineering
  - levitation-design
depends_on:
  - REF-PROMPT-001
  - REF-PROMPT-004
outputs:
  - levitation_visualization_method
---

# 悬浮间隙可视化指南

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 3 D1石盘悬浮2-3mm间隙在图片中不够明显

---

## 概述

本指南解决"悬浮"概念在图片生成中难以可视化的问题。2-3mm的微小间隙在图片中常被忽略或表达不清。

## 核心问题

- 微小间隙（2-3mm）在图片中难以辨识
- 模型倾向于将悬浮物体与地面/底座合并
- "levitates""floats"等词不足以确保间隙可视化

## 悬浮间隙可视化方法

### 方法1: 光影间隙法

通过间隙中的光影效果强调悬浮感。

```
❌ "levitates 2mm above base"
✅ "levitates above base, soft light glow in the gap, shadow beneath"
```

### 方法2: 材质对比法

通过上下材质对比强调分离感。

```
❌ "disc levitates above base"
✅ "warm stone disc clearly separated from cold metal base, distinct layers"
```

### 方法3: 视角强调法

通过特定视角展示间隙。

```
❌ "three-quarter view"
✅ "low angle view emphasizing the gap between disc and base"
```

### 方法4: 环境反射法

通过间隙中的环境反射强调空间感。

```
❌ "2mm gap"
✅ "gap reflects pure white background, creating bright line between layers"
```

## 检查清单

- [ ] 间隙有光影效果描述
- [ ] 上下材质有对比
- [ ] 视角有助于展示间隙
- [ ] 间隙有环境反射或发光描述
- [ ] 不使用精确数字（mm），使用感官描述

## 示例

### 石盘悬浮充电器（修正后）

```
Studio photograph, LoveFrom 2030.
A wireless charger that doesn't look like any wireless charger.
Travertine disc clearly separated from aluminum base,
soft light glow in the gap between layers,
warm stone texture against cold metal, distinct layers visible.
Floats. Pure white background.
No logo, no text, no screws.
```

## 来源

- Round 3 失败分析：D1石盘悬浮间隙不够明显
- REF-GUIDE-008: 提示词工程方法
