---
reference_id: REF-GUIDE-019-02
title: 动态形态表达指南
category: guides
used_when:
  - DYNAMIC-FORM-DESIGN
called_by:
  - end-to-end-workflow
  - pitfall-027
depends_on:
  - REF-GUIDE-001
  - REF-CASE-027
outputs:
  - dynamic_form_spec
---

# 动态形态表达指南 (Dynamic Form Expression)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 2 便携式咖啡机迭代 — 杠杆折叠状态暗示不足

---

## 问题定义

多状态产品（折叠/展开/旋转）在图片生成时：

- 主图通常只展示一个状态
- 其他状态的特征不可见
- 用户无法从单图理解产品的完整功能

**核心问题**: 如何在单图中暗示产品的多状态特性？

---

## 动态形态表达策略

### 策略1: 状态指示器

在形态中嵌入"状态指示器"，暗示其他状态：

| 状态变化 | 指示器类型 | 示例 |
|---------|-----------|------|
| 折叠/展开 | 折叠线、铰链、间隙 | "3mm protrusion indicating folded state" |
| 旋转 | 刻度、索引、锁定槽 | "5 indexed positions visible on cap edge" |
| 伸缩 |  telescoping lines、重叠段 | "2mm overlap line indicating extended position" |
| 开合 | 铰链、磁吸点、凹槽 | "0.5mm gap when closed, magnetic closure visible" |

### 策略2: 最识别性状态优先

选择最具识别性的状态作为主图：

| 产品类型 | 最识别性状态 | 原因 |
|---------|-------------|------|
| 折叠手机 | 展开状态 | 展示完整屏幕 |
| 折叠工具 | 展开状态 | 展示功能 |
| 旋转盖容器 | 旋转中状态 | 展示动态 |
| 伸缩灯具 | 最长状态 | 展示范围 |

### 策略3: 辅助状态暗示

在主图中通过细节暗示其他状态：

```
主图: 杠杆展开状态（最识别性）
辅助暗示: 
  - 铰链处有折叠痕迹
  - 主体侧面有收纳凹槽
  - 杠杆末端有磁吸点（暗示折叠后固定位置）
```

### 策略4: 多图策略（如果允许）

如果平台支持多图，生成2张：

```
图1: 主状态（展开/使用状态）
图2: 次状态（折叠/收纳状态）
```

---

## 提示词模板

### 单图动态形态提示词

```
[主体形态描述，最识别性状态]
[状态指示器1]: [具体描述]
[状态指示器2]: [具体描述]
[状态变化暗示]: [具体描述]
```

### 示例: 杠杆压咖啡机（修正版）

```
Body: 6061-T6 aluminum, 65mm diameter, 180mm height, anodized gunmetal gray.
Lever: carbon fiber, 120mm length, 8mm thickness, EXTENDED STATE (most recognizable).
State indicators:
  - Hinge: stainless steel, 0.5mm gap, polished edge, FOLD MARK visible on body
  - Body side: 2mm recessed groove where lever nests when folded
  - Lever tip: magnetic dot, indicates attachment point when folded
  - Folded state hint: 3mm protrusion from body silhouette
Interaction: unfold 120° until click, press 30N, fold back after use.
```

---

## 常见动态形态问题

| 问题 | 示例 | 修正 |
|------|------|------|
| 状态不可区分 | 折叠/展开看起来一样 | 添加状态指示器（间隙、痕迹、凹槽） |
| 只展示收纳状态 | 折叠手机只展示折叠 | 优先展示展开状态 |
| 动态感过强 | 旋转形态看起来"正在转" | 冻结在最具识别性的角度 |
| 多状态混淆 | 用户不知道产品如何变化 | 添加"before/after"暗示 |

---

## 提示词自检清单

```
[ ] 产品是否有多个状态？
[ ] 最识别性状态是否作为主图？
[ ] 是否有≥2个状态指示器？
[ ] 状态变化是否在提示词中描述？
[ ] 其他状态是否有视觉暗示？
```

---

## 关联

- 相关 Pitfall: 027（复杂提示词超时）
- 相关指南: prompt-engineering.md, interaction-detail-visualization.md
- 相关案例: Round 2 杠杆压咖啡机（折叠状态暗示不足）

---

## 来源

- Round 2 实证: references/iterations/round-2/image-analysis.md
- 日期: 2026-06-21
