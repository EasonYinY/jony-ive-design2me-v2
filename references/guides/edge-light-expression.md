---
reference_id: REF-GUIDE-021-02
title: 边缘微光表达指南
category: guides
used_when:
  - PROMPT-COMPILATION
called_by:
  - prompt-engineering
  - edge-light-design
depends_on:
  - REF-PROMPT-001
  - REF-PROMPT-004
outputs:
  - edge_light_expression_method
---

# 边缘微光表达指南

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 3 D3单芯片片"subtle edge glow"表达成功但方法不稳定

---

## 概述

本指南记录"边缘微光"（edge glow）在提示词中的稳定表达方法，用于状态指示、技术暗示和视觉焦点。

## 核心问题

- "subtle edge glow"有时被模型忽略
- "edge glow"有时被渲染为过度发光（像霓虹灯）
- 微光的"subtle"程度难以控制

## 边缘微光表达方法

### 方法1: 材质+光结合法

将微光与材质描述结合，而非单独描述光。

```
❌ "edge glow"
✅ "edge emits soft warm light through translucent material"
```

### 方法2: 对比强调法

通过明暗对比突出微光。

```
❌ "subtle edge glow"
✅ "edge glows softly against dark body, warm amber light"
```

### 方法3: 技术暗示法

将微光与技术功能关联，增加模型理解。

```
❌ "edge glow"
✅ "edge indicator light, charging status glow, minimal LED"
```

### 方法4: 色彩限定法

明确微光的色彩，避免模型随机渲染。

```
❌ "edge glow"
✅ "warm white edge glow, 2700K color temperature"
```

## 检查清单

- [ ] 微光与材质或功能关联
- [ ] 微光有明暗对比描述
- [ ] 微光的技术功能已说明
- [ ] 微光的色彩已限定
- [ ] 微光不是唯一光源（避免过度发光）

## 示例

### 单芯片片充电器（修正后）

```
Studio photograph, LoveFrom 2030.
A wireless charger that doesn't look like any wireless charger.
Extremely thin aluminum disc, 
edge emits soft warm white light through translucent chamfer,
charging status indicator, minimal LED glow against dark body.
Floats. Pure white background.
No logo, no text, no screws.
```

## 来源

- Round 3 成功分析：D3单芯片片"subtle edge glow"表达成功
- REF-GUIDE-008: 提示词工程方法
