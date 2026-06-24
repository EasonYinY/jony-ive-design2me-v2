---
reference_id: REF-PROMPT-001
title: PromptBundle 编译合同
category: prompt
used_when:
  - STEP-15
called_by:
  - product-design
  - prompt-rewriting
  - image-critique
depends_on:
  - REF-DESIGN-001
  - REF-EVIDENCE-001
outputs:
  - prompt_bundle
---

# PromptBundle 编译器与摄影控制合同

## 用途

`PromptBundle` 是一个 `IR_READY` 方向的视觉表达包。编译器只把 `DesignIR` 中已经确认的关系、结构、操作、人体工学、材料、制造、交互、维护和识别特征重新组织为提示词，不参与产品设计。

## 启动条件

- 输入必须是恰好三个不可变的 `DirectionBundle`。
- 三个方向都必须处于 `IR_READY`，且通过关系、结构和操作方式差异门。
- 每个 `DesignIR` 字段必须完整，方向标识必须一致。
- 任一条件不满足时立即拒绝编译，不得用摄影语言补全产品定义。
- 编译器必须为三个 `IR_READY` 方向分别返回完整提示词包；排序不构成省略另外两个方向的理由。
- 提示词编译不等于图片生成授权。没有用户在当前请求中的明确出图指令时，完成三个提示词包后立即停止。

## PromptBundle 完整合同

| 字段 | 用途 | 内容边界 |
|---|---|---|
| `direction_id` | 保持方向追溯 | 必须与输入方向完全一致 |
| `design_prompt` | 产品整体设计主提示 | 只表达既有关系、结构、操作、人体工学、材料和识别特征 |
| `detail_prompt` | 结构与工艺细节提示 | 只表达既有结构、材料、制造和维护路径 |
| `use_context_prompt` | 真实使用情境提示 | 只表达既有关系、动作、姿态、交互和反馈 |
| `negative_prompt` | 抑制已知越界与生成错误 | 不得反向成为新的正向产品处方 |
| `photography_controls` | 控制表达可见度 | 仅使用封闭枚举，不接收自由形态描述 |
| `production_prompt` | 最终生产提示词 | 语义完整优先，按固定语义顺序表达，必须包含精确数字、悬浮感、高频接触点 |
| `prompt_trace` | 逐句追溯 | 每个语义短句只引用 DesignIR 或封闭摄影控制 |

### 当前版本 强制字段

| 字段 | 用途 | 内容边界 |
|---|---|---|
| `material_precision` | 材料精确描述 | 必须包含材料名称 + 结构状态 + 触感描述，如 "smoked glass slab suspended over travertine base" |
| `geometric_specs` | 几何规格 | 必须包含至少 2 个精确数字（尺寸/角度/公差/曲率），如 "6cm thick", "G2 fillet edges" |
| `floating_state` | 悬浮状态 | 必须描述产品与环境的空间关系，如 "Floats", "levitates 2mm above glass pad" |
| `negative_constraints` | 负面约束 | 必须包含 3-5 个具体产品相关的否定描述，如 "No logo, no text, no screws" |
| `primary_contact` | 高频接触点 | 必须包含至少 1 个高频接触点的精确描述，如 "brass brew slit flush in glass" |

###强制字段（感官材料+品牌语境）

| 字段 | 用途 | 内容边界 |
|---|---|---|
| `brand_context` | 品牌语境锚定 | 必须包含 "LoveFrom 2030, post-Apple Jony Ive" |
| `sensory_material` | 感官材料优先 | 必须使用感官可感知材料（"hairline-brushed titanium"）而非工程材料（"titanium alloy TC4"） |
| `form_vocabulary` | 形态词汇 | 必须包含至少 1 个艾维标志性形态词（slab/G2 fillet/sweeping tangent/hairline） |
| `detail_precision` | 精致细节 | 必须包含至少 1 个精致细节（amber LED hairline / single brass inlay dot / brew slit） |

所有字段均为非空；提示词包与摄影控制均为不可变对象。编译器每次返回新对象，不修改 `DirectionBundle` 或 `DesignIR`。

## 摄影控制

摄影控制只允许选择以下表达参数：

- 镜头：整体、三分之四侧视、侧视、细节或使用状态。
- 构图：单一产品、正投影、细节或使用序列。
- 光线：中性柔光、方向性掠射光或漫射日光。
- 背景：纯白、中性灰或已经由输入确认的情境。
- 景深：深景深、中等景深或仅用于细节的浅景深。
- 可见目标：只能引用 `DesignIR` 的既有字段。

使用封闭枚举的原因是阻止“增加把手”“改变模块边界”等产品创造语言伪装成摄影参数。镜头、构图、光线、背景和景深若与 `DesignIR` 冲突，以 `DesignIR` 为准并拒绝越界参数。

## 确定性编译顺序

1. 检查三个输入方向的类型、数量和唯一标识。
2. 检查三个状态都为 `IR_READY`。
3. 重新检查每个 `DesignIR` 的完整字段，并确保 `form_proportion`、`cmf_system` 与 `resting_state` 进入编译与追溯。
4. 运行三方向关系、结构和操作方式差异门。
5. 使用同一组封闭摄影控制分别编译三个完整提示词包。
6. 保留 D1、D2、D3 的输入顺序和方向标识。

## 拒绝条件

- 方向不是三个、方向标识重复或本质差异门失败。
- 任一方向不是 `IR_READY`，或 `DesignIR` 字段缺失。
- 摄影控制值不在允许集合中。
- 可见目标不是 `DesignIR` 字段。
- 摄影、光线、背景、景深或反向提示试图创造、删除、隐藏或改写产品定义。

## 负面约束规则

`negative_prompt` 必须基于本产品的具体特征生成，不得使用通用负面词。

### 规则

- 每个负面约束必须对应一个 `DesignIR` 中的「已否决候选」或「已排除特征」
- 负面约束必须具体、可执行，不说 "no bad quality"，说 "no logo, no text, no screws"
- 负面约束数量：3-5 个，过少则约束不足，过多则稀释焦点
- 负面约束必须与产品类型强相关：咖啡机的 "no screws" 合理，无人机的 "no exposed blades" 合理

### 优秀示例

```
"No logo, no text, no screws"
← 对应：产品追求无缝外观，已排除螺丝连接（DesignIR.manufacturing 否决）

"No visible buttons, single brass inlay dot"
← 对应：已选择压电表面，排除机械按钮（DesignIR.interaction 否决）

"No glossy plastic, no exposed blades"
← 对应：已选择碳纤维，排除塑料；已选择涵道风扇，排除暴露叶片（DesignIR.cmf_system 否决）
```

### 否决条件

- 使用通用负面词（"no bad quality", "no blur", "no distortion"）→ 重新编译
- 负面约束与产品无关 → 重新编译
- 负面约束少于 3 个或多于 5 个 → 重新编译
- 负面约束与 DesignIR 已否决项无对应 → 重新编译

本合同采用 `SOURCE_LEDGER.csv` 中 `VIS-001` 至 `VIS-004` 的条件性表达规则，以及 `BND-002`、`BND-003` 的禁止外推规则。这些内容只控制 Design IR 之后的表达，不作为 Jony Ive 的公开理论或新的产品证据。`MTH-012` 仍处于待核验状态，不进入正向运行知识。
