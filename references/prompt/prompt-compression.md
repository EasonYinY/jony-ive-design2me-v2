---
reference_id: REF-PROMPT-002
title: 中文提示词压缩规则
category: prompt
used_when:
  - STEP-15
called_by:
  - product-design
  - prompt-rewriting
depends_on:
  - REF-PROMPT-001
  - REF-DESIGN-003
outputs:
  - production_prompt
---

# 中文提示词压缩规则

> **版本**: 1.1
> **日期**: 2026-06-21
> **触发**: 优秀提示词分析发现精确性优于简洁性

---

## 核心原则：语义完整优先于字符限制

每个方向最终输出一段中文提示词，**以语义完整为优先，不强制限制字符数**。但必须满足以下强制要求：

### 强制保留字段（不得删除）

| 字段 | 要求 | 示例 |
|---|---|---|
| `material_precision` | 材料精确名称 + 结构状态 + 触感描述 | "smoked glass slab suspended over travertine base" |
| `geometric_specs` | 至少 2 个精确数字（尺寸/角度/公差/曲率） | "6cm thick", "G2 fillet edges", "5-degree forward lean" |
| `floating_state` | 产品与环境的关系（悬浮/放置/倚靠） | "Floats", "levitates 2mm above glass pad" |
| `negative_constraints` | 3-5 个具体产品相关的否定描述 | "No logo, no text, no screws" |
| `primary_contact` | 至少 1 个高频接触点的精确描述 | "brass brew slit flush in glass", "single brass start point on right" |
| `photography_controls` | 摄影控制（镜头/构图/光线/背景） | "Studio photograph, three-quarter view slightly above" |

###强制字段

| 字段 | 要求 | 示例 |
|---|---|---|
| `brand_context` | 品牌语境锚定 | "LoveFrom 2030, post-Apple Jony Ive" |
| `sensory_material` | 感官材料优先（非工程材料） | "hairline-brushed titanium" 而非 "titanium alloy TC4" |
| `form_vocabulary` | 艾维标志性形态词汇 | "slab", "G2 fillet", "sweeping tangent", "hairline" |
| `detail_precision` | 精致细节（LED/缝隙/点缀） | "amber LED hairline at slit", "single brass inlay dot" |
| `base_form` | 基础形态锁定 | "solid carbon fiber slab", "vertical cylindrical core" |
| `deformation_rule` | 变形规则 | "前宽后窄（手掌支撑）", "6°前倾（手腕自然角度）" |
| `geometric_terms` | 几何术语 | "G2 fillet edges", "sweeping tangent base" |

### 固定语义顺序

1. **摄影语法**：Studio photograph, three-quarter view slightly above
2. **产品身份与品牌语境**：产品类型 + LoveFrom 2030, post-Apple Jony Ive
3. **结构形态**：感官材料 + 几何规格 + 结构状态 + 形态词汇
4. **精致细节**：hairline/LED/缝隙/点缀
5. **高频接触点**：核心交互节点的精确位置与材料
6. **使用动作**：关键操作 + 状态切换
7. **悬浮状态**：产品与环境的空间关系
8. **负面约束**：具体否定的产品特征
9. **背景**：neutral gradient / pure white

### 删除规则

- 删除论证过程、风险、内部字段名、方向编号
- 删除重复修饰和纯审美形容词（如"优雅""高级"）
- 删除不能追溯到 DesignIR 或摄影控制的词句
- **不得删除**任何数字、工程术语（G2、fillet、slab、radius 等）
- **不得删除**品牌语境锚定（LoveFrom 2030, post-Apple Jony Ive）
- **不得删除**感官材料描述

### 确定性编译顺序

1. 检查 `brand_context`：是否包含 "LoveFrom 2030, post-Apple Jony Ive"？
2. 检查 `sensory_material`：是否使用感官材料而非工程材料？
3. 检查 `form_vocabulary`：是否包含 slab/G2 fillet/sweeping tangent/hairline？
4. 检查 `material_precision`：材料名称是否精确？是否包含结构状态？
5. 检查 `geometric_specs`：是否包含至少 2 个精确数字？
6. 检查 `detail_precision`：是否包含精致细节（LED/缝隙/点缀）？
7. 检查 `floating_state`：是否描述了产品与环境的空间关系？
8. 检查 `negative_constraints`：是否包含 3-5 个具体否定？
9. 检查 `primary_contact`：是否包含至少 1 个高频接触点？
10. 按固定语义顺序排列所有短句
11. 去除字段名式前缀和重复空白
12. 保留 `prompt_trace` 完整原始值

### 优秀提示词特征清单

编译完成后，检查是否具备以下特征：

- [ ] 品牌语境：包含 "LoveFrom 2030, post-Apple Jony Ive"
- [ ] 感官材料：不说"高级金属"，说"hairline-brushed titanium slab"
- [ ] 形态词汇：包含 slab/G2 fillet/sweeping tangent/hairline 至少1个
- [ ] 精致细节：包含 amber LED hairline / single brass inlay dot / brew slit 等
- [ ] 几何精确：包含至少 2 个数字（mm/°/G2/radius）
- [ ] 悬浮感：包含"Floats"或等效描述
- [ ] 负面具体：不说"no bad quality"，说"no logo, no text, no screws"
- [ ] 接触点精确：不说"按钮"，说"single brass start point on right"
- [ ] 单一焦点：只描述产品，无环境/人物/辅助物品
- [ ] 工程术语：使用 G2、fillet、slab、tangent、flush 等精确术语

### 与历史版本的关键差异

| 维度 | 旧版 | 升级版 |
|------|------|------|
| 字符限制 | 90-160 强制 | 语义完整优先，不强制限制 |
| 数字保留 | 可选删除 | 强制保留 |
| 材料描述 | 可简化 | 必须精确（名称+结构+触感） |
| 悬浮感 | 无要求 | 强制要求 |
| 负面约束 | 通用 | 具体产品相关 |
| 接触点 | 无要求 | 强制要求 |
| **品牌语境** | **无** | **强制要求** |
| **感官材料** | **无要求** | **强制要求** |
| **形态词汇** | **无要求** | **强制要求** |
| **精致细节** | **无要求** | **强制要求** |

---

## 来源

- 优秀提示词分析：9 个提示词的材料精确度、几何精确度、悬浮感、负面约束特征
- REF-PROMPT-001: PromptBundle 编译合同
- REF-DESIGN-001: DesignIR 完整合同
- REF-PROMPT-004: 摄影表达控制
- REF-GUIDE-008: 提示词工程方法（感官材料优先法+品牌语境锚定法）
