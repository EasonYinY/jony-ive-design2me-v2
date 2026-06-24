---
reference_id: REF-GUIDE-018
title: 交互细节可视化指南
category: guides
used_when:
  - INTERACTION-DESIGN
called_by:
  - end-to-end-workflow
  - pitfall-026
depends_on:
  - REF-GUIDE-001
  - REF-CASE-026
outputs:
  - interaction_detail_spec
---

# 交互细节可视化指南 (Interaction Detail Visualization)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 1 智能桌面台灯迭代 — 交互细节（触摸区域、调光机制）在图中不可见

---

## 问题定义

人体工学和交互设计在 DesignIR 中详细定义，但图片生成时：

- "底座前端边缘触摸调光" → AI 生成平滑底座，无触摸区域标识
- "柱身微纹理开关" → AI 生成光滑柱身，无纹理区域
- "翼底面微光反馈" → AI 生成均匀发光，无反馈层次

**核心问题**: 交互细节必须在提示词中显性化为视觉元素，而非仅描述功能。

---

## 交互细节可视化公式

```
[交互功能] = [位置] + [视觉线索] + [触觉线索] + [尺寸]
```

---

## 高频接触点可视化

### 模板

```
Contact point: [名称]
Location: [精确位置，如"base front edge, 20mm from corner"]
Visual cue: [视觉标识，如"2mm raised ridge, brushed finish"]
Tactile cue: [触觉标识，如"0.5mm knurl, 0.2mm pitch"]
Size: [尺寸，如"30mm × 5mm active area"]
Function indicator: [功能暗示，如"subtle LED glow beneath when active"]
```

### 示例1: 底座触摸调光（光之桥修正版）

```
Contact point: Dimming control
Location: base front edge, 20mm from left corner, along 80mm arc
Visual cue: 2mm raised ridge, brushed aluminum perpendicular to base grain
Tactile cue: fine longitudinal knurl, 0.3mm pitch, 0.1mm depth
Size: 80mm × 3mm active area
Function indicator: subtle warm LED glow (3000K) beneath ridge when active,
  intensity proportional to brightness setting
```

### 示例2: 柱身触摸开关（光之柱修正版）

```
Contact point: On/off and dimming
Location: column lower third, 100mm from base, 360° around column
Visual cue: micro-knurl pattern, 0.5mm pitch, matte finish contrasting with polished column
Tactile cue: distinct texture change, tactile "click" zone at 12 o'clock position
Size: 30mm × 360° band
Function indicator: column emits soft white glow (4000K) through micro-knurl
  when touched, brightness follows finger position
```

### 示例3: 翼片固定角度（光之翼修正版）

```
Contact point: On/off
Location: base top surface, center of triangle, 20mm diameter circle
Visual cue: 1mm micro-concave depression, polished finish contrasting with matte base
Tactile cue: smooth center with subtle edge lip, finger naturally settles
Size: 20mm diameter
Function indicator: wing underside emits soft gradient glow from center to tip
  when on, dark when off
```

---

## 交互节点可视化

### 模板

```
Interaction node: [操作名称]
Trigger: [触发方式，如"touch""slide""rotate""press"]
Visual feedback: [视觉反馈，如"LED glow""color change""motion"]
Tactile feedback: [触觉反馈，如"vibration""click""resistance"]
Auditory feedback: [听觉反馈，如"silent""soft click""tone"]
Transition: [状态过渡描述，如"0.3s fade in""instant on"]
```

### 示例: 调光交互

```
Interaction node: Brightness adjustment
Trigger: finger slide along contact point
Visual feedback: real-time brightness change, LED glow intensity follows finger
Tactile feedback: subtle haptic pulse at 25%/50%/75%/100% positions
Auditory feedback: silent (no mechanical sound)
Transition: 0.1s real-time response, 0.5s smooth fade to target
```

---

## 常见交互可视化问题

| 问题 | 示例 | 修正 |
|------|------|------|
| 交互区域不可见 | "touch base to turn on" | "base top surface 20mm concave depression, polished" |
| 反馈层次缺失 | "LED glow when on" | "subtle warm LED (3000K) glow beneath contact point, intensity proportional to brightness" |
| 触觉线索模糊 | "micro-textured surface" | "micro-knurl 0.5mm pitch, 0.1mm depth, tactile at fingertip" |
| 位置不精确 | "column lower part" | "column lower third, 100mm from base, 30mm band" |
| 尺寸缺失 | "small button" | "8mm diameter, 1mm protrusion, flush when off" |

---

## 提示词自检清单

在 STEP-15 生成提示词后，检查交互细节：

```
[ ] 每个高频接触点有精确位置描述
[ ] 每个接触点有视觉线索（可见标识）
[ ] 每个接触点有触觉线索（纹理/尺寸）
[ ] 每个交互节点有反馈描述（视觉/触觉/听觉）
[ ] 无"touch area""control zone"等抽象位置词
[ ] 所有尺寸具体（mm级别）
```

---

## 关联

- 相关 Pitfall: 026（提示词→图片衰减）
- 相关指南: prompt-engineering.md, material-honesty-visualization.md
- 相关案例: Round 1 三个方向（交互细节均不可见）

---

## 来源

- Round 1 实证: references/iterations/round-1/image-analysis.md
- 交互设计可视化原则: 知识库【设计师-知识蒸馏/乔纳森·艾维-知识蒸馏】
- 日期: 2026-06-21
