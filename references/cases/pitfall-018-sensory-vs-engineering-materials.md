---
reference_id: REF-CASE-018
title: Pitfall 018 - 工程材料替代感官材料
category: cases
used_when:
  - PROMPT-COMPILATION
called_by:
  - prompt-compression
  - image-critique
  - quality-gates
depends_on:
  - REF-PROMPT-002
  - REF-GUIDE-008
  - REF-DESIGN-003
outputs:
  - failure_pattern
---

# Pitfall 018 - 工程材料替代感官材料

## 触发条件

- 提示词中使用工程化材料名称（如 "titanium alloy TC4", "stainless steel 316L", "polycarbonate PC"）
- 缺少感官可感知的表面处理描述（如 "hairline-brushed", "polished", "smoked", "matte"）
- 缺少形态词（如 "slab", "dome", "ring", "shell"）
- 用户反馈"造型不够，质感和高级感不太对味"

## 失败表现

1. **图片质感偏冷硬**：AI 图像生成模型对工程材料词汇的渲染倾向于"工业零件"而非"高端产品"
2. **高级感缺失**："titanium alloy TC4" 渲染为普通金属，而 "hairline-brushed titanium" 渲染为精致纹理
3. **造型识别性弱**：缺少 "slab" "G2 fillet" "sweeping tangent" 等标志性形态词汇，导致造型趋于平庸
4. **品牌语境缺失**：缺少 "LoveFrom 2030, post-Apple Jony Ive" 锚定，AI 无法调用关联的高端工业设计风格

## 根因分析

| 层级 | 问题 | 说明 |
|------|------|------|
| 材料层 | 工程前缀冗余 | "alloy"/"grade"/"316L"/"6061"/"TC4" 等工程前缀对 AI 渲染无正向贡献 |
| 描述层 | 表面处理缺失 | 缺少 "hairline-brushed"/"polished"/"smoked"/"anodized" 等感官描述 |
| 形态层 | 形态词缺失 | 缺少 "slab"/"dome"/"ring" 等艾维标志性形态词汇 |
| 语境层 | 品牌锚定缺失 | 缺少 "LoveFrom 2030, post-Apple Jony Ive" 风格坐标 |
| 细节层 | 精致细节缺失 | 缺少 "amber LED hairline"/"single brass inlay dot"/"brew slit" 等点缀 |

## 修复方法

### 1. 材料转换规则

```
删除工程前缀 → 保留表面处理 → 添加形态词 → 添加空间关系

例：
"titanium alloy TC4 disc body" 
→ "titanium disc" 
→ "hairline-brushed titanium disc" 
→ "hairline-brushed titanium disc, 65mm diameter"
```

### 2. 感官材料对照表

| 工程材料（❌） | 感官材料（✅） |
|---------------|---------------|
| "titanium alloy TC4" | "hairline-brushed titanium" |
| "stainless steel 316L" | "polished steel" / "brushed steel" |
| "polycarbonate PC" | "smoked glass" / "translucent amber" |
| "aluminum 6061" | "anodized aluminum" |
| "carbon fiber reinforced polymer" | "matte carbon" / "carbon ring" |

### 3. 品牌语境锚定

必须在产品身份段包含：
```
"[产品类型], LoveFrom 2030, post-Apple Jony Ive"
```

### 4. 精致细节注入

每个方向至少包含一个精致细节：
- "amber LED hairline at slit"
- "single brass inlay dot"
- "single brass start point on right"
- "brass brew slit flush in glass"

### 5. 负面约束简化

从冗长具体 → 简洁通用：
```
❌ "no visible buttons, no LED glow, no plastic parts"
✅ "no logo, no text, no screws"
```

## 验证方式

1. 检查提示词是否包含 "LoveFrom 2030, post-Apple Jony Ive"
2. 检查材料名称是否包含工程前缀（alloy/grade/316L/6061/TC4）
3. 检查是否包含至少1个感官表面处理词（hairline-brushed/polished/smoked/matte）
4. 检查是否包含至少1个形态词（slab/dome/ring/shell）
5. 检查是否包含至少1个精致细节（amber LED/brass dot/brew slit）
6. 检查负面约束是否为 "no logo, no text, no screws" 结构

## 来源

- 用户反馈："造型不够，质感和高级感不太对味"（2026-06-21）
- 优秀提示词分析：9个提示词全部使用感官材料（"smoked glass slab", "polished obsidian slab", "matte carbon"）
- REF-PROMPT-002: 中文提示词压缩规则（新增感官材料强制字段）
- REF-GUIDE-008: 提示词工程方法（方法8: 感官材料优先法）
- REF-DESIGN-003: CMF 系统（感官材料转换规则）
