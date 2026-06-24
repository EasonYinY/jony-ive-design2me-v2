---
reference_id: REF-GUIDE-023-02
title: 可穿戴产品人体工学指南
category: guides
used_when:
  - WEARABLE-DESIGN
called_by:
  - end-to-end-workflow
  - pitfall-030
depends_on:
  - REF-GUIDE-001
  - REF-GUIDE-018
outputs:
  - wearable_ergonomics_checklist
---

# 可穿戴产品人体工学指南 (Wearable Ergonomics Guide)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 5 智能手表迭代 — 佩戴舒适度需要系统化指导

---

## 概述

可穿戴产品（手表、耳机、眼镜、手环）的人体工学设计需要特别关注与人体的贴合关系。本指南提供系统化的设计参数和验证方法。

---

## 1. 手腕贴合

### 表体背面弧度

| 参数 | 数值 | 说明 |
|------|------|------|
| 曲率半径 | 30-50mm | 匹配手腕平均曲率 |
| 贴合面积 | ≥60% | 表体背面与手腕接触面积 |
| 边缘过渡 | 2mm圆角 | 避免边缘压迫 |

### 表体位置

- **中心位置**: 手腕骨突（ulna styloid）内侧10mm
- **倾斜角度**: 表体平面与手腕平面平行，±5°
- **高度**: 表体底面与手腕皮肤间隙≤1mm

---

## 2. 重量分布

### 重心位置

- **理想位置**: 表体几何中心
- **偏移限制**: ≤5mm（避免重心偏外导致翻转）

### 重量分配

| 部件 | 占比 | 说明 |
|------|------|------|
| 表体 | 60-70% | 主体重量集中 |
| 表带 | 30-40% | 均匀分布 |

---

## 3. 表带设计

### 无表带扣方案

| 方案 | 原理 | 适用 |
|------|------|------|
| 磁吸 | 磁铁吸附 | 金属表带 |
| 弹性 | 硅胶/织物弹性 | 运动手表 |
| 折叠 | 铰链折叠固定 | 时尚手表 |
| 卡扣 | 弹簧卡扣 | 通用 |

### 表带宽度

- **标准**: 18-22mm
- **宽表带**: 24-26mm（运动、户外）
- **窄表带**: 16-18mm（时尚、女性）

---

## 4. 传感器位置

### 最佳位置

- **心率**: 手腕内侧，桡动脉上方
- **血氧**: 手指/耳垂（手表不可行）
- **体温**: 手腕内侧，皮肤接触面

### 传感器窗口

- **尺寸**: 5-10mm直径
- **材质**: 蓝宝石/陶瓷（耐磨+透光）
- **凸起**: ≤0.5mm（避免压迫皮肤）

---

## 5. 验证方法

```
[ ] 表体背面曲率30-50mm
[ ] 贴合面积≥60%
[ ] 重心偏移≤5mm
[ ] 表带宽度18-22mm
[ ] 传感器窗口≤0.5mm凸起
[ ] 边缘过渡2mm圆角
[ ] 重量≤50g（手表）
```

---

## 6. 提示词表达

```
✅ "conforms to wrist curve""wrist-hugging back"
✅ "balanced weight distribution""center of gravity at geometric center"
✅ "sensor window flush with skin""0.3mm protrusion"
✅ "18mm band width""articulated links conform to wrist"
```

---

## 关联

- 相关 Pitfall: 030（佩戴状态不可见）
- 相关案例: Round 5 智能手表（水滴表贴合设计）

---

## 来源

- Round 5 实证: references/iterations/round-5/design-output.md
- 日期: 2026-06-21
