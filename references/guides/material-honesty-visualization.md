---
reference_id: REF-GUIDE-016
title: 材料诚实可视化指南
category: guides
used_when:
  - CMF-DESIGN
called_by:
  - end-to-end-workflow
  - pitfall-026
  - multi-material-joint-design
depends_on:
  - REF-GUIDE-001
  - REF-CASE-026
outputs:
  - material_honesty_spec
---

# 材料诚实可视化指南 (Material Honesty Visualization)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 1 智能桌面台灯迭代 — granite 装饰性使用违背材料诚实原则

---

## 艾维材料诚实三原则

1. **结构诚实**: 材料在图中承担的结构功能必须可见
2. **触感诚实**: 材料的表面质感必须可辨识
3. **制造诚实**: 制造工艺的痕迹必须合理

违背任一原则 = 设计失败。

---

## 材料诚实的3层表达

### Layer 1: 结构诚实

材料在图中的结构功能必须显性化：

| 材料 | 结构功能 | 提示词中必须包含 |
|------|---------|----------------|
| 花岗岩 | 配重 | "base weight 2.5kg, center of gravity 30mm above table" |
| 铝 | 散热 | "heat sink fins integrated into arm surface, 0.5mm pitch" |
| 玻璃 | 光扩散 | "diffuser plate, 85% transmission, uniform light output" |
| 织物 | 柔光 | "2mm fabric diffuser layer, 85% light transmission, visible weave" |
| 钢 | 结构 | "load-bearing frame, 2mm wall thickness, welded joints" |

**反例**（Round 1 光之桥）:
- ❌ "granite base" → AI 理解为装饰性石头
- ✅ "polished granite base, 180×120×30mm, weight 2.5kg, low center of gravity for stability" → 结构功能显性

### Layer 2: 触感诚实

材料的表面质感必须可辨识：

| 材料 | 触感特征 | 提示词中必须包含 |
|------|---------|----------------|
| 阳极氧化铝 | 冷、微纹理 | "anodized aluminum, fine longitudinal grain, 0.2mm pitch, cool to touch" |
| 抛光花岗岩 | 冷、光滑、重 | "polished granite, mirror-smooth, cold heavy, natural crystal pattern visible" |
| 磨砂亚克力 | 温润、轻 | "frosted acrylic, satin-smooth, warm light diffusion, feather-light" |
| 织物 | 温暖、柔软 | "woven fabric, 0.5mm thread, soft tactile, warm under light" |
| 玻璃 | 光滑、硬 | "tempered glass, optically smooth, hard, cool" |

**反例**（Round 1 光之柱）:
- ❌ "micro-textured surface" → AI 生成模糊纹理
- ✅ "micro-knurl pattern, 0.5mm pitch, 0.1mm depth, tactile grip visible at 30° angle" → 精确可辨识

### Layer 3: 制造诚实

制造工艺的痕迹必须合理：

| 工艺 | 视觉痕迹 | 提示词中必须包含 |
|------|---------|----------------|
| CNC | 刀痕、倒角 | "CNC machined, 0.1mm tool marks visible, G2 fillet edges" |
| 挤压 | 挤压纹 | "aluminum extrusion, longitudinal grain, die line visible" |
| 注塑 | 分模线 | "injection molded, 0.1mm parting line, gate mark at hidden location" |
| 冲压 | 折弯线 | "stamped and bent, 0.2mm bend radius, sharp fold line" |
| 焊接 | 焊缝 | "TIG welded, 2mm bead, ground flush, heat tint visible" |
| 抛光 | 镜面 | "hand-polished, mirror finish, 0.1μm Ra" |

**反例**（Round 1 光之翼）:
- ❌ "anodized black aluminum" → 无制造痕迹
- ✅ "stamped and bent aluminum, 0.2mm bend radius, anodized black, die line visible on edge" → 制造诚实

---

## 常见材料诚实违背

| 违背类型 | 示例 | 修正 |
|---------|------|------|
| 装饰性使用 | granite 用于美观而非配重 | 明确说明重量和重心位置 |
| 质感伪装 | "metal-like plastic" | 禁止 — 材料必须诚实 |
| 制造痕迹隐藏 | 注塑件无分模线 | 说明分模线位置和处理方式 |
| 功能不可见 | fabric diffuser 不可见 | 说明透光率和可见纹理 |
| 触感误导 | "warm metal" | 金属是冷的，暖触感来自表面处理而非材料本身 |

---

## 提示词自检清单

在 STEP-15 生成提示词后，检查每个材料：

```
[ ] 结构功能在提示词中明确说明
[ ] 触感特征有≥3个可辨识描述
[ ] 制造痕迹有具体视觉描述
[ ] 无"metal-like""wood-effect"等伪装词
[ ] 无纯装饰性使用（无结构/触感/制造功能）
```

---

## 关联

- 相关 Pitfall: 026（提示词→图片衰减）
- 相关指南: multi-material-joint-design.md, prompt-engineering.md
- 相关案例: Round 1 光之桥（granite 装饰性扣分）

---

## 来源

- Round 1 实证: references/iterations/round-1/image-analysis.md
- 艾维材料诚实原则: 知识库【设计师-知识蒸馏/乔纳森·艾维-知识蒸馏】
- 日期: 2026-06-21
