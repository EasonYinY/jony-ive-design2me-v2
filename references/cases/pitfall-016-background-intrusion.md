---
reference_id: REF-CASE-016
title: Pitfall 016 - 背景侵入
category: cases
used_when:
called_by:
  - product-design
  - quality-gates
  - failure-library
  - image-critique
depends_on:
  - REF-QUALITY-002
  - REF-QUALITY-003
outputs:
  - failure_pattern
---

# Pitfall 016 - 背景侵入

## 触发条件

1. 图片中出现背景、环境、辅助物品、场景、人物、手、脸等除产品外的元素
2. 提示词中包含环境描述（如"浴室台面""镜前反射""阳光照射的房间"）
3. 产品未置于纯白背景中
4. 提示词聚焦分散（包含场景、氛围、情境描述而非产品造型）

## 失败表现

- 图片中出现浴室、台面、镜子、手、脸等环境元素
- 产品被场景淹没，无法聚焦产品本体
- 提示词中大量词汇用于描述环境而非产品（如"sunlit room with north-facing windows"）
- 产品识别性降低（环境元素分散注意力）

## 根因分析

### 直接原因
提示词未严格限制为"纯产品造型"：
- 使用了摄影模板（如"photographed in a sunlit room"）而非"product hero shot on pure white background"
- 提示词包含环境光、反射环境、背景描述

### 深层原因
混淆了"产品摄影"与"产品造型"：
- 产品摄影需要环境来展示产品使用情境
- 产品造型只需要展示产品本身，环境是干扰

## 修复方法

### 提示词强制规则
1. **背景**：必须为纯白（`pure white background` / `seamless white` / `255 white`）
2. **环境**：禁止任何环境元素（`no environment` / `no context` / `no scene`）
3. **辅助物**：禁止任何辅助物品（`no props` / `no accessories` / `no hands` / `no face`）
4. **聚焦**：100%聚焦产品造型（`product only` / `hero shot` / `centered composition`）

### 摄影参数调整
- ❌ "Shot on Hasselblad H6D-100c, 100mm macro, f/8, **sunlit room with north-facing windows**"
- ✅ "Shot on Hasselblad H6D-100c, 100mm macro, f/8, **pure white background, studio softbox 45°, no environment, no props, product only**"

### 禁止词汇清单
- 环境类：room, bathroom, kitchen, office, studio, outdoor, indoor, scene, setting
- 辅助物类：hand, finger, face, person, human, model, hand model, lifestyle
- 氛围类：lifestyle, natural light, ambient, cozy, warm atmosphere
- 反射环境类：reflected color from white stone counter, gradient backdrop

## 验证方式

1. 检查提示词是否包含纯白背景声明
2. 检查提示词是否包含环境/辅助物/人物禁止声明
3. 检查图片是否仅包含产品本体（无背景/环境/辅助物）
4. 检查提示词中产品造型词汇占比是否 > 80%

## 来源

- REF-QUALITY-002 image-critique "背景纯净"
- REF-QUALITY-003 failure-library `background_intrusion`
- 实证：2026-06-21剃须器设计（D3轨道式生成描述包含"浴室台面场景，镜前反射"）
