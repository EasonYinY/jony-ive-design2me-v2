---
reference_id: REF-CASE-026
title: Pitfall 026 — 提示词→图片衰减
category: cases
used_when:
  - IMAGE-GENERATION
called_by:
  - prompt-engineering-guide
  - iteration-workflow
depends_on:
  - REF-GUIDE-001
outputs:
  - pitfall_warning
---

# Pitfall 026 — 提示词→图片衰减 (Prompt-to-Image Attenuation)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 1 智能桌面台灯迭代
> **严重程度**: 🔴 高

---

## 现象

设计阶段评分 8.7/10 → 图片评审 7.75/10，衰减 **0.95 分**。

三个方向平均衰减 0.77 分，主要衰减点：
- 材料质感表达（-0.5 至 -1.0）
- 接缝处理（-0.5 至 -1.0）
- 交互细节可视化（-0.5 至 -1.0）

---

## 根因分析

### 根因1: 抽象概念AI理解有限

提示词中的抽象概念 AI 无法直接转化为视觉：

| 抽象概念 | AI理解 | 实际效果 | 衰减 |
|---------|--------|---------|------|
| "seamless transition" | 字面无缝 | 可见 seam 或过度融合 | -0.5 |
| "micro-texture" | 模糊纹理 | 表面过于光滑或过于粗糙 | -0.3 |
| "cultural hybrid" | 风格混合 | 文化元素不可见或混乱 | -0.5 |
| "fabric soft-light layer" | 织物覆盖 | 织物不可见或被忽略 | -0.5 |
| "suspension" | 悬浮 | 支撑结构不清晰 | -0.3 |

### 根因2: 提示词信息密度不足

提示词平均 200-300 英文词，但图片包含的视觉信息远超文字描述能力。
关键视觉细节在压缩过程中丢失。

### 根因3: AI模型对工业设计语义的理解偏差

- "anodized aluminum" → AI 理解为"银色金属"，忽略微纹理
- "granite base" → AI 理解为"斑点石头"，忽略配重功能暗示
- "fabric diffuser" → AI 理解为"黑色覆盖"，忽略透光功能

---

## 解决方案

### 策略1: 抽象概念→具体视觉转换

所有抽象概念必须替换为具体视觉描述：

| ❌ 抽象表达 | ✅ 具体视觉 |
|-----------|-----------|
| seamless transition | monolithic construction, no visible joint line, material gradient transition 5mm |
| micro-texture | fine longitudinal grain, 0.2mm pitch, brushed finish visible at 30° angle |
| cultural hybrid | moss-textured base surface + stone-group arrangement + light raking across |
| fabric soft-light layer | 2mm thick fabric diffuser, 85% light transmission, visible weave pattern |
| suspension | transparent acrylic rod 8mm diameter, 150mm length, minimal visible support |

### 策略2: 信息密度增强

- 提示词长度从 200-300 词增至 400-500 词
- 每个材料必须包含：名称 + 结构职责 + 触感描述 + 制造痕迹 + 视觉特征
- 每个接缝必须包含：位置 + 处理方式 + 视觉结果 + 尺寸

### 策略3: 分层提示词结构

```
Layer 1: 形态定义（50词）— 不可协商
Layer 2: 材料精确描述（150词）— 结构+触感+制造+视觉
Layer 3: 接缝处理（50词）— 每个过渡的具体视觉
Layer 4: 交互细节（50词）— 接触点位置+视觉线索
Layer 5: 文化元素（50词）— 具体视觉符号
Layer 6: 摄影语法（50词）— 视角+光+背景
Layer 7: 负面约束（30词）— 禁止元素
```

### 策略4: 验证循环

1. 生成提示词后，自检："如果我是AI，看到这个提示词会生成什么？"
2. 识别提示词中的抽象概念，逐一替换
3. 生成图片后，对比提示词与图片，记录衰减点
4. 下一轮迭代中针对性增强

---

## 验证方法

在 STEP-15 后，运行以下自检：

```
[ ] 提示词中无抽象概念（seamless, micro, subtle, elegant, graceful）
[ ] 每个材料有≥3个视觉特征描述
[ ] 每个接缝有具体尺寸和处理方式
[ ] 文化元素有具体视觉符号
[ ] 交互细节有位置和视觉线索
[ ] 提示词长度≥400英文词
```

---

## 关联

- 相关 Pitfall: 002（图片查看失败循环）
- 相关指南: prompt-engineering.md, multi-material-joint-design.md
- 相关案例: Round 1 智能桌面台灯（衰减 0.77 分）

---

## 来源

- Round 1 实证: references/iterations/round-1/image-analysis.md
- 日期: 2026-06-21
