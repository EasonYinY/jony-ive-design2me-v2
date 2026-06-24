---
reference_id: PITFALL-060
title: 反纯粹抽象与功能 Legible 质量门（Debranding & Functional Legibility）
category: cases
used_when:
  - STEP-15
  - PROMPT-COMPILATION
called_by:
  - end-to-end-workflow.md (STEP-15.6)
  - prompt-engineering.md 方法23
  - compile_prompt.py
depends_on:
  - REF-GUIDE-008
  - REF-PROMPT-004
outputs:
  - prompt_quality_gate_result
  - debranding_compliance_report
---

# Pitfall 060: 反纯粹抽象与功能 Legible 质量门

## 触发条件

提示词编译阶段检测到以下任一问题：
1. 品牌词污染（"LoveFrom 2030"、"Apple"、具体年份数字）
2. 材质单调（单一材质统领全身，无自然/科技纹理对撞）
3. 平面发光层（"LED line"、"glowing strip" 等平面词汇）
4. 功能原型不可辨识（第一眼无法判断产品核心功能）

## 现象

- 提示词中出现 "LoveFrom 2030" → Lovart 文本编码器将其具象化为印刷字符/Logo
- 材质描述仅 "metal and glass" → 模型生成单调无细节的伪极简表面
- "LED strip on the side" → 生成扁平的、无结构深度的发光面
- "a futuristic vehicle" → 模型无法确定功能原型，生成模糊的科幻概念图

## 根因

1. **品牌词污染**：Lovart 模型的文本编码器（Text Encoder）极易将具体品牌词直接具象化为印刷字符
2. **材质单调**：缺乏自然纹理（如岩石微粒）与科技纹理（如激光微雕、渐变微孔）的对撞
3. **LED 扁平化**：缺乏 3D 结构（如光导管、折射棱镜）以及细腻的导光纹理
4. **功能原型 legibility 不足**：缺乏对核心功能组件（驾驶舱、推进轴向）的一眼识别度

## 修复方案

### 1. 拦截品牌词污染

**禁止**：
- ❌ "LoveFrom 2030"
- ❌ "Apple"
- ❌ 任何具体年份数字（如 2030、2024）
- ❌ "Jony Ive style"（风格模仿，非谱系描述）

**必须替换为**：
- ✅ "reflecting the pure minimalist design lineage of Jony Ive's aesthetic philosophy"
- ✅ "strictly debranded, absolute zero alphanumeric text, no printed logos"
- ✅ "seamless pristine surfaces"

### 2. 材质丰富度对撞要求

每个方案的 CMF 表达必须至少包含：
- **1 种天然/珩磨纹理**：honed basalt, water-honed grain, natural volcanic micro-texture
- **1 种微观机械科技纹理**：laser-etched gradient micro-grooves, micro-knurled patterns, CNC-milled precision ridges
- **几何边界处的机械交叠**：两种纹理必须在 G2 连续缝隙内交接，用 "interlocking with"、"structually bounded by" 描述

### 3. 禁止平面发光层

**全面废除**：
- ❌ "LED line"
- ❌ "glowing strip"
- ❌ "light bar"
- ❌ "illuminated edge"

**必须编译为 3D 立体光学结构**：
- ✅ "recessed 3D linear light-guide tube, encased inside a micro-grooved frosted quartz channel"
- ✅ "volumetric frosted polycarbonate light-prism housed inside a mechanical aluminum cage"
- ✅ "multi-layered refractive quartz tube emitting an intense, volumetric architectural glow"

### 4. 原型 Legibility 校验

提示词第一段必须明确描述：
- **核心功能组件**：飞行器的全景舱门、推进矢量轴；咖啡机的酿造组、蒸汽棒
- **物理方位词**：front orientation, rear propulsion core, dorsal spine
- **功能暗示**：piloting function, brew operation, magnetic levitation

## 检查清单

- [ ] 提示词中无 "LoveFrom"/"Apple"/年份数字？
- [ ] 有 "design lineage" + "strictly debranded" 指令？
- [ ] CMF 包含 ≥1 种天然纹理 + ≥1 种科技纹理？
- [ ] 无 "LED line"/"glowing strip" 等平面发光词汇？
- [ ] 有 3D 光导管/折射棱镜/立体腔体描述？
- [ ] 第一段明确描述核心功能组件与轴向？
- [ ] 第一眼能辨识产品功能原型？

## 相关参考

- `references/guides/prompt-engineering.md` 方法23（五维工业级提示词架构）
- `references/process/end-to-end-workflow.md` STEP-15.6
- `references/cases/pitfall-058-category-dynamic-exclusion.md`（品类动态排除词）
