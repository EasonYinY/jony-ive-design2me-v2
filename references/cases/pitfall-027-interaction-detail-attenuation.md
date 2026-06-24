---
reference_id: REF-CASE-027-02
title: Pitfall 027 — 交互细节衰减
version: 1.0
category: cases
used_when:
  - INTERACTION-DETAIL-VISUALIZATION
called_by:
  - interaction-detail-visualization-v2
  - end-to-end-workflow
depends_on:
  - REF-GUIDE-018
  - REF-GUIDE-019
outputs:
  - pitfall_warning
---

# Pitfall 027 — 交互细节衰减 (Interaction Detail Attenuation)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 2 便携式咖啡机迭代
> **严重程度**: 🔴 高

---

## 现象

设计阶段交互细节评分 8-9/10 → 图片评审交互细节评分 5-7/10，衰减 **1-2 分**。

三个方向具体衰减：
| 方向 | 设计评分 | 图片评分 | 衰减 | 主要衰减点 |
|------|---------|---------|------|-----------|
| D1 压力柱 | 8/10 | 5/10 | -3 | LED微光、按钮微凸 |
| D2 折叠泵压 | 8.5/10 | 6/10 | -2.5 | 铰链锁定、压力表指针 |
| D3 螺旋加压 | 8.5/10 | 6/10 | -2.5 | 旋钮凹槽、压力指示环 |

---

## 根因分析

### 根因1: 尺寸太小

AI 图像生成模型优先渲染大形态（主体轮廓），忽略微小细节（<1mm）。

| 交互元素 | 设计尺寸 | AI渲染阈值 | 结果 |
|---------|---------|-----------|------|
| LED环 | 0.2mm厚 | ~1mm | 被忽略 |
| 按钮凸台 | 0.3mm | ~1mm | 被平滑 |
| 纹理间距 | 0.4mm | ~0.8mm | 被平滑 |
| 凹陷深度 | 0.5mm | ~1.5mm | 被填平 |

### 根因2: 对比度太低

同材料微处理（如"拉丝不锈钢上的微凸按钮"）对比度不足，AI无法区分。

### 根因3: 位置不突出

侧面/边缘位置的交互元素在整体构图中不突出，被背景化。

### 根因4: 弱化词使用

"subtle""micro""fine"等词在提示词中弱化了交互元素的重要性。

---

## 解决方案

### 方案1: 尺寸放大法

交互元素尺寸在提示词中放大2-3倍：

| 元素 | 旧版 | 升级版 | 放大 |
|------|------|------|------|
| 按钮 | 8mm | 15mm | 2x |
| LED环 | 0.2mm | 1mm | 5x |
| 纹理 | 0.4mm间距 | 0.8mm间距 | 2x |
| 凹陷 | 0.5mm | 1.5mm | 3x |

### 方案2: 对比度强化法

使用不同材料创造强对比：

```
旧版: "stainless steel button on stainless steel body" → 对比度0
旧版: "polished brass button on brushed stainless steel body" → 对比度100%
```

### 方案3: 位置突出法

将交互元素放在视觉焦点位置：

```
旧版: "side button" → 边缘位置，不突出
旧版: "front face center button, breaking contour" → 焦点位置
```

### 方案4: 多线索叠加法

同时使用尺寸+对比+位置+表面处理+发光：

```
旧版: "15mm polished brass button, 1.0mm protrusion,
      centered on front face, breaking contour,
      surrounded by dark anodized ring,
      warm LED glow from translucent edge"
```

---

## 验证方法

在 STEP-15 后，运行以下自检：

```
[ ] 交互元素尺寸 ≥ 2x 实际设计尺寸
[ ] 交互元素与主体有强材料对比
[ ] 交互元素位置在视觉焦点
[ ] 交互元素有表面处理差异
[ ] 交互元素有发光/阴影/颜色线索
[ ] 无"subtle""micro""fine"等弱化词
```

---

## 关联

- 相关 Guide: interaction-detail-visualization-v2.md
- 相关 Guide: interaction-detail-visualization.md 
- 相关案例: Round 2 便携式咖啡机（衰减 1-2 分）

---

## 来源

- Round 2 实证: references/iterations/round-2/image-analysis.md
- 日期: 2026-06-21
