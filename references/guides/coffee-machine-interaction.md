---
reference_id: REF-GUIDE-021
title: 咖啡机品类交互设计指南
version: {{skill_version}}
category: guides
used_when:
  - COFFEE-MACHINE-DESIGN
called_by:
  - end-to-end-workflow
  - product-design
depends_on:
  - REF-GUIDE-018
  - REF-GUIDE-019
outputs:
  - coffee_machine_interaction_spec
---

# 咖啡机品类交互设计指南 (Coffee Machine Interaction Design)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 2 便携式咖啡机 — 缺少咖啡机特殊交互设计方法

---

## 概述

咖啡机（尤其是意式浓缩机）有独特的交互需求：
- 压力建立可视化（9bar→15bar）
- 萃取进度感知（预浸泡→萃取→收尾）
- 温度控制（90-96°C精确控制）
- Crema观察（金黄色油脂层）
- 蒸汽/热水切换

本指南将咖啡机特殊交互从功能描述转化为具体视觉元素。

---

## 咖啡机特殊交互可视化

### 1. 压力可视化

**问题**: 用户需要知道压力是否达到15bar，但压力表在便携机上难以集成。

**解决方案**:

```
Visual: 压力指示环
Location: 主体顶部或侧面，环绕萃取头
Design: 2mm宽LED环，颜色渐变
  - Green (0-5bar): 低压，预浸泡阶段
  - Yellow (5-10bar): 中压，萃取建立
  - Orange (10-14bar): 高压，接近目标
  - Red (15bar): 目标压力，稳定萃取
Size: 2mm宽 × 42mm直径（环绕萃取头）
Visual cue: 颜色渐变，实时响应
```

**提示词示例**:
```
"2mm wide LED pressure indicator ring, 42mm diameter, surrounding extraction head,
 color gradient from green (low) to yellow (medium) to red (15bar target),
 embedded in top surface, glow visible through translucent acrylic,
 real-time pressure visualization"
```

### 2. 萃取进度可视化

**问题**: 用户需要知道萃取是否完成（25-30秒），但计时器增加复杂度。

**解决方案**:

```
Visual: 萃取进度条
Location: 主体侧面，垂直或弧形
Design: 细长LED条，分段点亮
  - 0-10s: 第一段亮（预浸泡）
  - 10-20s: 第二段亮（主萃取）
  - 20-30s: 第三段亮（收尾）
  - >30s: 闪烁提醒（过萃）
Size: 3mm宽 × 60mm长
Visual cue: 分段点亮，进度直观
```

### 3. 温度指示

**问题**: 水温需要90-96°C，但温度显示增加复杂度。

**解决方案**:

```
Visual: 温度色温环
Location: 水箱盖或主体顶部
Design: 小型LED点，色温变化
  - Blue (冷): <80°C
  - White (温): 80-90°C
  - Warm White (热): 90-96°C（萃取温度）
  - Red (过热): >96°C
Size: 3mm直径LED点
Visual cue: 色温变化，直观感知
```

### 4. Crema观察窗口

**问题**: 用户需要观察crema质量，但便携机通常封闭。

**解决方案**:

```
Visual: 透明萃取观察窗
Location: 萃取头侧面
Design: 小窗口，透明玻璃/亚克力
Size: 8mm宽 × 15mm高
Visual cue: 可观察咖啡流出和crema形成
Material: 透明钢化玻璃，与金属框架0.2mm间隙
```

### 5. 蒸汽/热水切换

**问题**: 部分咖啡机需要蒸汽打奶泡，但切换机构复杂。

**解决方案**:

```
Visual: 旋转切换环
Location: 萃取头下方
Design: 旋转环，两档位置
  - Position 1: 萃取（图标：咖啡杯）
  - Position 2: 蒸汽（图标：蒸汽线）
Size: 30mm直径 × 5mm厚
Visual cue: 图标+颜色区分（萃取=黑色，蒸汽=白色）
Tactile cue: 旋转到位"咔嗒"声
```

---

## 咖啡机交互提示词模板

### 完整咖啡机交互描述

```
Interaction system:
1. Pressure visualization: 2mm LED ring, 42mm diameter, color gradient green→yellow→red,
   real-time pressure indication, embedded in top surface
2. Extraction progress: 3mm × 60mm LED bar, side-mounted, segmented illumination,
   0-30s progression, over-extraction flash warning
3. Temperature indicator: 3mm LED dot, color temperature shift blue→white→warm→red,
   90-96°C optimal zone
4. Crema window: 8mm × 15mm transparent glass window, side-mounted,
   0.2mm gap from metal frame, observation of coffee flow and crema formation
5. Mode switch: 30mm diameter rotating ring, two-position, tactile "click" confirmation,
   icon + color differentiation
```

---

## 自检清单

```
[ ] 压力可视化有具体尺寸和颜色渐变
[ ] 萃取进度有分段和时间对应
[ ] 温度指示有色温变化和最优区间
[ ] Crema窗口有尺寸和位置
[ ] 模式切换有触觉确认
[ ] 所有交互与咖啡功能强相关
[ ] 无通用交互（如"按钮""开关"）替代咖啡专用交互
```

---

## 来源

- Round 2 实证: 便携式咖啡机交互设计缺失
- 意式浓缩咖啡工程: 9bar压力、90-96°C、25-30s萃取时间
- REF-GUIDE-018: 交互细节可视化
- REF-GUIDE-019: 交互细节可视化增强
- 日期: 2026-06-21
