---
reference_id: REF-GUIDE-019
title: 声学功能视觉化指南
category: guides
used_when:
  - ACOUSTIC-DESIGN
called_by:
  - prompt-engineering
  - audio-device-design
depends_on:
  - REF-PROMPT-004
  - REF-DESIGN-001
outputs:
  - acoustic_visualization_method
---

# 声学功能视觉化指南

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 4 蓝牙音箱评审发现声学功能（网罩、倒相孔、被动辐射器）在图片中不够显性

---

## 概述

声学功能（扬声器、网罩、倒相孔、被动辐射器）必须在提示词中显性化为视觉元素，否则在图片中不可见。

---

## 视觉化公式

```
[声学功能] = [视觉元素] + [材料暗示] + [结构暗示]
```

---

## 常见声学功能视觉化

### 1. 扬声器网罩

| 功能 | 视觉元素 | 材料暗示 | 结构暗示 |
|------|----------|----------|----------|
| 声学透声 | 微孔阵列 | 金属/织物 | 精密蚀刻 |
| 防尘保护 | 细密网格 | 不锈钢 | 冲压成型 |
| 美观装饰 | 同心圆纹理 | 铝合金 | CNC加工 |

**提示词模板**:
```
"micro-perforated metal mesh, 0.5mm holes, precision etched, visible acoustic transparency"
```

### 2. 被动辐射器

| 功能 | 视觉元素 | 材料暗示 | 结构暗示 |
|------|----------|----------|----------|
| 低频增强 | 对称振动膜 | 橡胶/硅胶 | 悬挂边缘 |
| 视觉平衡 | 圆形/椭圆形 | 金属配重 | 精密配平 |

**提示词模板**:
```
"symmetrical bass radiator, visible vibration membrane, rubber surround, metal weight"
```

### 3. 倒相孔

| 功能 | 视觉元素 | 材料暗示 | 结构暗示 |
|------|----------|----------|----------|
| 低频增强 | 圆形/长条形开口 | 金属内衬 | 精密孔径 |
| 气流管理 | 内部通道暗示 | 光滑内壁 | 无锐角 |

**提示词模板**:
```
"tuned bass port, circular opening, internal channel visible, smooth inner wall"
```

### 4. 分频设计

| 功能 | 视觉元素 | 材料暗示 | 结构暗示 |
|------|----------|----------|----------|
| 高低音分离 | 上下分区 | 不同网罩 | 精密分界 |
| 声场定位 | 指向性设计 | 金属号角 | 精密角度 |

**提示词模板**:
```
"two-way speaker system, tweeter upper, woofer lower, distinct mesh patterns"
```

---

## 应用步骤

1. 从 DesignIR 提取所有声学功能
2. 为每个功能选择视觉元素
3. 添加材料暗示（表面处理、颜色）
4. 添加结构暗示（制造工艺、精度）
5. 检查：是否可感知？是否可辨识？

---

## 示例

### 蓝牙音箱（Round 4）

```
❌ 原提示词（声学功能不够显性）:
"micro-perforated metal mesh top"

✅ 改进提示词（声学功能视觉化）:
"micro-perforated aluminum mesh, 0.5mm precision holes, acoustic transparency visible, 
 etched pattern, sound waves implied"
```

---

## 来源

- Round 4 蓝牙音箱评审
- 声学工程原理
- REF-PROMPT-004: 提示词工程方法
