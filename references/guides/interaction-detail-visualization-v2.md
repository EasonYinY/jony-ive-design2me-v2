---
reference_id: REF-GUIDE-019-04
title: 交互细节可视化增强 v2
version: 2.0
category: guides
used_when:
  - INTERACTION-DETAIL-VISUALIZATION
called_by:
  - interaction-detail-visualization
  - pitfall-027
depends_on:
  - REF-GUIDE-018
  - REF-CASE-027
outputs:
  - interaction_detail_历史版本_spec
---

# 交互细节可视化增强 v2 (Interaction Detail Visualization v2)

> **版本**: 2.0
> **日期**: 2026-06-21
> **触发**: Round 2 便携式咖啡机 — 交互细节衰减 0.5-0.8 分
> **升级**: 从 旧版的"精确位置+视觉+触觉+尺寸"增强为"高对比度+大尺寸+强位置+多线索"

---

## 旧版 问题

Round 2 发现：
- LED微光（3000K）在图片中不可见
- 压力指示环颜色渐变被忽略
- 按钮微凸边缘（0.3mm）在图片中不可辨识
- 触觉纹理（0.4mm间距）被AI平滑处理

**核心问题**: 交互细节尺寸太小、对比度太低、位置不够突出，AI生成时优先渲染大形态，忽略微小交互。

---

## 旧版 增强策略

### 策略1: 尺寸放大法

| 交互元素 | 旧版 尺寸 | 旧版 尺寸 | 放大倍数 | 效果 |
|---------|----------|----------|---------|------|
| 按钮 | 8mm | 12-15mm | 1.5-2x | 从不可见→可见 |
| LED环 | 0.2mm厚 | 1-2mm厚 | 5-10x | 从忽略→可辨识 |
| 纹理间距 | 0.3-0.4mm | 0.8-1.0mm | 2-3x | 从平滑→有纹理 |
| 凹陷深度 | 0.5mm | 1.5-2mm | 3-4x | 从平面→有层次 |
| 凸台高度 | 0.3mm | 1.0mm | 3x | 从忽略→可见 |

**规则**: 交互元素尺寸在提示词中放大2-3倍，确保AI渲染时可见。

### 策略2: 对比度强化法

| 对比类型 | 旧版 | 升级版 | 效果 |
|---------|------|------|------|
| 材料对比 | 同材料微处理 | 不同材料强对比 | 从模糊→清晰 |
| 颜色对比 | 同色系 | 互补色/冷暖对比 | 从融合→分离 |
| 表面处理对比 | 同为拉丝 | 镜面vs拉丝 | 从单调→层次 |
| 光泽对比 | 同为哑光 | 高光vs哑光 | 从平面→立体 |

**示例**:
```
旧版: "8mm stainless steel button, brushed finish, 0.3mm raised edge"
→ AI渲染: 按钮与主体融合，不可见

旧版: "15mm polished brass button, mirror finish, 1.0mm protrusion,
      contrasting with brushed stainless steel body"
→ AI渲染: 黄铜按钮在不锈钢主体上清晰可见
```

### 策略3: 位置突出法

| 位置策略 | 旧版 | 升级版 | 效果 |
|---------|------|------|------|
| 中心位置 | 侧面偏置 | 正面中心或黄金分割点 | 从边缘→焦点 |
| 非对称 | 对称分布 | 非对称强调 | 从平淡→动态 |
| 打破轮廓 | 沿轮廓线 | 打破轮廓线 | 从连续→中断 |

**示例**:
```
旧版: "side button, 80mm from top"
→ AI渲染: 按钮融入侧面，不突出

旧版: "front face center, 15mm brass button breaks the cylindrical contour,
      creating a focal point"
→ AI渲染: 按钮成为视觉焦点
```

### 策略4: 多线索叠加法

旧版 单一线索 → 旧版 多线索叠加：

```
旧版（单线索）:
"8mm button with 0.3mm raised edge"

旧版（多线索）:
"15mm polished brass button, mirror finish, 1.0mm protrusion,
 breaking cylindrical contour, centered on front face,
 surrounded by 2mm dark anodized ring for contrast,
 subtle warm LED glow (3000K) from 1mm translucent edge"
```

**线索叠加公式**:
```
[大尺寸] + [强材料对比] + [突出位置] + [表面处理差异] + [发光/阴影] + [打破轮廓]
```

---

## 旧版 提示词模板

### 按钮/开关模板

```
[尺寸放大] + [材料对比] + [位置突出] + [表面处理差异] + [发光/阴影]

例：
"15mm polished brass button, mirror finish, 1.0mm protrusion from body,
 centered on front face, breaking the cylindrical contour,
 surrounded by 2mm dark anodized aluminum ring for contrast,
 subtle warm LED glow (3000K) from 1mm translucent silicone edge when active"
```

### 纹理/防滑模板

```
[间距放大] + [深度放大] + [方向对比] + [材料对比]

例：
"0.8mm pitch longitudinal knurl pattern, 0.3mm depth, tactile grip visible,
 perpendicular to body grain direction, polished peaks against matte valleys,
 copper-colored knurl against stainless steel body"
```

### 指示/反馈模板

```
[尺寸放大] + [颜色对比] + [位置突出] + [渐变/变化]

例：
"2mm wide LED indicator ring, color gradient from green (low) to yellow (medium) to red (high),
 embedded in top surface, 1mm below surface, glow visible through translucent acrylic,
 color change proportional to pressure level"
```

---

## 旧版 自检清单

在 STEP-15 生成提示词后，检查交互细节：

```
[ ] 交互元素尺寸 ≥ 2x 旧版 标准
[ ] 交互元素与主体有强材料对比（不同材料）
[ ] 交互元素位置突出（中心/黄金分割/打破轮廓）
[ ] 交互元素有表面处理差异（镜面vs拉丝/抛光vs哑光）
[ ] 交互元素有发光/阴影/颜色变化线索
[ ] 使用多线索叠加（≥3个线索）
[ ] 无"micro""subtle""fine"等弱化词
```

---

## 与 旧版 对比

| 维度 | 旧版 | 升级版 | 效果 |
|------|------|------|------|
| 尺寸 | 精确但小 | 放大2-3倍 | 从不可见→可见 |
| 对比度 | 同材料微处理 | 不同材料强对比 | 从模糊→清晰 |
| 位置 | 精确但边缘 | 突出位置 | 从边缘→焦点 |
| 线索数 | 1-2个 | 3-5个叠加 | 从单一→丰富 |
| 弱化词 | 允许"subtle" | 禁止所有弱化词 | 从弱化→强调 |
| 衰减 | 0.5-0.8分 | 目标≤0.3分 | 显著改善 |

---

## 来源

- Round 2 实证: 便携式咖啡机交互细节衰减分析
- REF-GUIDE-018: 交互细节可视化
- REF-CASE-027: Pitfall 027 — 交互细节衰减
- 日期: 2026-06-21
