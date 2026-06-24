---
reference_id: REF-GUIDE-008
title: 提示词工程方法
category: guides
used_when:
  - PROMPT-COMPILATION
  - STEP-15
called_by:
  - prompt-contract
  - prompt-compression
  - prompt-trace
depends_on:
  - REF-PROMPT-001
  - REF-PROMPT-002
  - REF-PROMPT-004
  - REF-DESIGN-001
outputs:
  - prompt_engineering_method
---

# 提示词工程方法

> **版本**: 1.2
> **日期**: 2026-06-21
> **触发**: 用户反馈"提示词必须是中文"+"设计要有轻重缓急和点睛之笔"+"从大造型到部件关系到CMF到细节的层次控制"

---

## 概述

本指南从9个优秀提示词（3个产品×3轮迭代）中提炼提示词工程方法，将「精确性」作为提示词质量的核心指标，而非「简洁性」。

> **旧版 关键升级**：基于用户反馈（2026-06-21 mouse nextgen 失败），新增：
> 1. **基础形态锁定法**：必须先定义基础体块（slab/block/cylinder/dome），再写变形规则
> 2. **单材质主导策略**：每个方向只选1种主导材料，厚度精确到小数点后1位
> 3. **几何术语精确注入**：强制使用G2/G1连续、fillet、chamfer、tangent、step等术语
> 4. **姿态锁定词库**：每个方向必须有姿态词（Floats/levitates/resting flat/suspended）
> 5. **负面约束精简**：只保留3-5个最关键的负面约束，避免稀释焦点
>
> **【已记录】**：基于用户反馈，新增：
> 1. **中文提示词强制规则**：所有提示词必须以中文为主体，英文仅作为补充
> 2. **大造型→部件关系→CMF→细节层次法**：控制设计从宏观到微观的描述顺序
> 3. **轻重缓急与点睛之笔法**：避免寡淡或混乱，创造设计焦点和惊喜时刻
> 4. **用户要求显性化拆解法**：将用户模糊的风格要求拆解为可执行的设计方向定义
>
> **【已记录】**：增加「方法8: 感官材料优先法」和「方法9: 品牌语境锚定法」。

---

## 方法8: 感官材料优先法

### 原理

材料描述的核心不是工程精确性（"titanium alloy TC4"），而是感官可感知性（"smoked glass slab"）。AI图像生成模型对感官词汇的渲染质量远高于工程词汇。

### 感官材料 vs 工程材料

| 维度 | 工程材料（❌） | 感官材料（✅） | 效果差异 |
|------|---------------|---------------|----------|
| 金属 | "titanium alloy TC4" | "hairline-brushed titanium slab" | 后者有纹理+形态+工艺 |
| 玻璃 | "borosilicate glass" | "smoked glass slab" | 后者有颜色+透明度+形态 |
| 石材 | "calcium carbonate travertine" | "travertine base" | 后者简洁+可感知 |
| 碳纤维 | "carbon fiber reinforced polymer" | "matte carbon" | 后者有表面处理+简洁 |
| 塑料 | "polycarbonate" | "smoked-glass jellyfish bell" | 后者用形态替代材料名 |

### 转换规则

1. **删除工程前缀**："titanium alloy TC4" → "titanium"
2. **添加表面处理**："titanium" → "hairline-brushed titanium"
3. **添加形态词**："hairline-brushed titanium" → "hairline-brushed titanium slab"
4. **添加感官形容词**："slab" → "slab suspended over..."（创造空间关系）

### 优秀提示词材料分析

```
=== COFFEE ===
"smoked glass slab suspended over a travertine base"
→ 无工程材料名，全感官描述
→ "smoked"=颜色+透明度，"slab"=形态，"suspended over"=空间关系
→ "travertine"=材料名本身即感官（洞石纹理可感知）

=== MOUSE ===
"polished obsidian slab, front wider, rear tapered"
→ "polished"=表面处理，"obsidian"=材料+颜色（黑色火山玻璃）
→ "slab"=形态，"front wider, rear tapered"=动态比例
→ 无"titanium alloy""carbon fiber"等工程词汇

=== DRONE ===
"Two carbon rings linked by three kevlar tension lines"
→ "carbon"=简洁材料名，"rings"=形态
→ "kevlar tension lines"=材料+结构状态（张力线）
→ "matte carbon"=表面处理
```

### 应用步骤

1. 从 DesignIR.materials 提取材料
2. **删除工程化前缀**（alloy/grade/reinforced/polymer）
3. **选择感官可感知的材料名**（obsidian > titanium alloy, travertine > limestone）
4. **添加表面处理**（hairline-brushed/polished/matte/smoked）
5. **添加形态词**（slab/dome/ring/shell/bell）
6. **添加空间关系**（suspended over/linked by/rests on）
7. 检查：是否可感知？是否有纹理？是否有形态？

---

## 方法9: 品牌语境锚定法

### 原理

优秀提示词使用 "LoveFrom 2030, post-Apple Jony Ive" 作为品牌语境锚定，这不是人物模仿，而是建立设计语境的精确坐标。AI模型对该语境有稳定的视觉风格关联。

### 锚定结构

```
[产品类型], [设计工作室] [年份], [设计语境].

例：
"single-cup coffee maker, LoveFrom 2030, post-Apple Jony Ive"
"wireless mouse, LoveFrom 2030, post-Apple Jony Ive"
"camera drone, LoveFrom 2030, post-Apple Jony Ive"
```

### 锚定作用

| 作用 | 说明 |
|------|------|
| 风格坐标 | 建立"极简+精确材料+诚实结构"的视觉预期 |
| 时间坐标 | "2030"设定未来语境，允许科幻元素 |
| 文化坐标 | "post-Apple"暗示超越消费电子的语境 |
| 质量坐标 | 关联高端工业设计渲染质量 |

### 应用规则(本版本 更新)

1. 必须包含在 Subject 段(第 1 段,跟随产品类型):
   - 旧版:第 2-3 句
   - 新版:**第 1 段内,跟随产品类型一起出现**
2. 不得替换为其他设计师/品牌(保持方法一致性)
3. 不得添加人物模仿词("style of""inspired by")
4. **摄影语法(Studio photograph / three-point softbox)与品牌语境锚分开** —— 摄影锚移到第 5 段(Style 段),品牌语境锚保留在 Subject 段
5. 与方法 7「固定语法结构法」第 1 段配合使用

### 对比示例

```咖啡机示例(本版本对齐后):
一款单杯咖啡机,LoveFrom 2030,post-Apple Jony Ive。悬浮于台面,准备冲泡一杯浓缩咖啡。
整体板状造型,...

Studio photograph, 50mm at f/1.8, three-point softbox, three-quarter view slightly above.
```

旧版(摄影锚 + 品牌锚都放第 1 句,违反本版本规则):

```咖啡机示例(旧版,已废弃):
Studio photograph, three-quarter view slightly above, of a single-cup coffee maker, LoveFrom 2030, post-Apple Jony Ive.
```

---

---

## 方法1: 单材质主导 + 材料精确描述法

### 原理

每个方向只选**1种主导材料**，其他材料最多1种辅助。材料描述必须包含三个维度：名称精确、结构状态、触感暗示。

**【已记录】**：从优秀提示词分析发现，高评分提示词均使用**单材质 slab 策略**：
- `Solid aluminum slab, 5cm thick`
- `Solid carbon fiber slab, 1.2cm at highest`
- `Hairline-brushed titanium slab 1.5cm at peak`

多材质堆砌会导致视觉混乱、缺乏焦点、像学生作品。

### 单材质主导策略

| 策略 | 说明 | 示例 |
|------|------|------|
| **主导材料** | 承担 80% 以上视觉面积 | `solid aluminum slab` |
| **辅助材料** | 最多 1 种,承担特定功能 | `brass brew slit`(仅缝隙) |
| **禁止** | 3 种以上材料并列 | ❌ `titanium + carbon fiber + glass + wood` |

### 结构模板

```
[主导材料] + [基础形态] + [可选粗尺寸]

例:
- "smoked glass slab suspended over travertine base"
  → 主导:smoked glass slab(80% 视觉面积)
  → 辅助:travertine base(底座功能)
  → 尺寸:可选,粗尺寸 6cm thick(不是 6.0mm 精确)

- "hairline-brushed titanium slab 1.5cm at peak"
  → 主导:hairline-brushed titanium slab
  → 尺寸:1.5cm at peak(≥ 1mm 粗数字 OK)
  → 辅助:无(纯单材质)
```

### 禁止表达

| ❌ 错误 | ✅ 正确 |
|---------|---------|
| "高级金属" | "hairline-brushed titanium slab" |
| "奢华玻璃" | "smoked glass slab" |
| "优质塑料" | "matte carbon fiber" |
| "深岩灰" | "anodized aluminum" |
| "titanium + carbon + glass composite" | "solid titanium slab" |

### 应用步骤

1. 从 DesignIR.materials 提取所有候选材料
2. **选择1种主导材料**（视觉面积最大、结构职责最重）
3. **删除其他材料**或降级为辅助（最多1种）
4. 添加基础形态词（slab/block/cylinder/dome/wedge）
5. 添加表面处理（hairline-brushed/polished/matte/smoked）
6. 添加精确尺寸（Xcm thick, Xmm at peak，精确到小数点后1位）
7. 检查：是否单材质主导？是否包含基础形态？是否包含触感暗示？

---

## 方法2: 基础形态锁定 + 几何精确注入法

### 原理

**升级**：优秀提示词不是从"有机曲线"开始，而是先定义**基础体块**，再写**变形规则**。几何精确数字不是装饰，而是基础形态的控制参数。

**失败教训**：mouse nextgen 失败的核心原因——直接从"未来感"生成有机曲线，无基础形态，导致"乱七八糟的有机"。

### 基础形态词库

| 基础形态 | 适用产品 | 变形方向 |
|----------|----------|----------|
| **slab**（板状） | 鼠标、咖啡机、灯具 | 弯曲、倾斜、挖空 |
| **block**（块状） | 音箱、充电器、工具 | 倒角、分割、层叠 |
| **cylinder**（圆柱） | 灯具、容器、笔 | 锥化、扭曲、挖空 |
| **dome**（圆顶） | 鼠标、控制器、盖子 | 压扁、偏移、切割 |
| **wedge**（楔形） | 支架、底座、工具 | 倾斜、弯曲、分割 |
| **disc**（圆盘） | 旋钮、底座、托盘 | 凹陷、边缘处理 |

### 基础形态锁定步骤

```
Step 1: 选择基础形态
  → 从词库中选择1个最符合产品功能的基础体块
  → 例：鼠标 → slab（手掌平放）

Step 2: 定义精确尺寸
  → 长×宽×高，精确到小数点后1位
  → 例：120mm × 65mm × 35mm

Step 3: 定义变形规则
  → 从人体工学/功能/美学出发，定义如何变形
  → 例：前宽后窄（手掌支撑），6°前倾（手腕自然角度）
  → 变形必须有数学/物理依据，不能随意

Step 4: 定义几何术语
  → 使用G2/G1连续、fillet、chamfer、tangent、step等术语
  → 例：G2 fillet edges, sweeping tangent base

Step 5: 验证
  → 是否从基础体块出发？
  → 变形是否有理性依据？
  → 是否包含至少2个精确数字？
```

### 数字类型与几何术语

| 类型 | 示例 | 来源 | 几何术语 |
|------|------|------|----------|
| 尺寸 | "6cm thick", "1.5cm at peak" | DesignIR.form_proportion | slab, block, cylinder |
| 角度 | "5-degree forward lean", "six-degree forward lean" | DesignIR.ergonomics | forward lean, backward tilt |
| 曲率 | "G2 fillet edges", "G2 dome over palm" | DesignIR.form_proportion | G2 fillet, G1 chamfer, tangent |
| 公差 | "0.1mm L/R", "0.3mm凹陷" | DesignIR.manufacturing | flush, recessed, raised |
| 距离 | "levitates 2mm above glass pad" | DesignIR.resting_state | levitates, suspended, floats |
| 比例 | "1.2cm at highest" | DesignIR.form_proportion | at peak, at base, at center |

### 注入规则

1. **先定义基础形态**（slab/block/cylinder/dome），再提取数字
2. 数字必须服务于**形态控制**，而非装饰
3. 必须包含至少1个**几何术语**（G2/G1/fillet/chamfer/tangent/step）
4. 必须包含至少2个**精确数字**（尺寸+角度/曲率）
5. 变形规则必须有**理性依据**（人体工学/功能/物理）

### 示例对比

```
❌ 旧版写法（无基础形态，直接有机）：
"整体流线型，有机曲线，未来感造型"

✅ 旧版写法（基础形态+变形规则）：
"Solid carbon fiber slab, 120mm × 65mm × 35mm,
前宽后窄（手掌支撑），6°前倾（手腕自然角度），
G2 fillet edges, sweeping tangent base"

❌ "一个厚玻璃板"
✅ "Single black slate slab 6cm thick, 120mm diameter,
G2 dome over palm, 8mm fillet radius"

❌ "鼠标有前倾角度"
✅ "Solid carbon fiber slab, 1.2cm at highest, six-degree forward lean,
G2 palm dome, sweeping tangent base"
```

---

## 方法3: 姿态锁定词库

### 原理

所有产品提示词必须有**姿态锁定词**，这是LoveFrom的标志性视觉特征。姿态不是装饰，而是基础形态的延伸。

**【已记录】**：姿态词必须**与基础形态一致**，不能随意选择。

### 姿态词库

| 姿态词 | 适用基础形态 | 含义 | 适用产品 |
|--------|-------------|------|----------|
| **Floats** | slab, block, disc | 悬浮于画面中，无可见支撑 | 大多数产品（默认） |
| **levitates Xmm** | slab, disc | 精确悬浮高度 | 需要强调悬浮技术的产品 |
| **rests on** | block, wedge | 放置于底座/表面 | 必须有物理接触的产品 |
| **suspended** | cylinder, dome | 悬挂状态 | 吊灯、悬挂式产品 |
| **nestles** | dome | 半嵌入/半包裹 | 鼠标、控制器 |

### 姿态锁定规则

1. **根据基础形态选择姿态词**
   - slab → Floats（默认）
   - block → rests on 或 Floats
   - cylinder → suspended 或 Floats
   - dome → nestles 或 Floats

2. **姿态词必须出现在提示词末尾**，作为视觉句号

3. **不得使用"放在桌上""置于地面"等落地描述**

4. **即使产品需要放置，也要通过构图创造悬浮感**

### 示例

```
基础形态: slab → 姿态: Floats
"Studio photograph... of a wireless mouse... Floats. Neutral gradient."

基础形态: slab → 姿态: levitates
"Studio photograph... of a wireless mouse... levitates 2mm above glass pad."

基础形态: block → 姿态: rests on
"Studio photograph... of a coffee maker... rests on travertine base."
```

---

## 方法4: 负面约束精简法

### 原理

负面约束不是「不要坏质量」，而是「不要这些具体特征」——每个否定都对应一个已否决的设计决策。

**【已记录】**：负面约束必须**精简到3-5项**，过多会稀释焦点，过少则约束不足。必须**与基础形态一致**。

### 负面约束精简规则

| 基础形态 | 默认负面约束 | 可选补充 |
|----------|-------------|----------|
| **slab** | No logo, no text, no screws | no visible buttons, no glossy plastic |
| **block** | No logo, no text, no seams | no decorative grooves, no LED strips |
| **cylinder** | No logo, no text, no joints | no visible wiring, no mounting brackets |
| **dome** | No logo, no text, no flat surfaces | no sharp edges, no plastic |

### 数量规则

- **最少3个，最多5个**
- 必须与产品类型强相关
- 必须与基础形态一致
- 每个否定对应一个已否决特征

### 优秀示例

```
咖啡机（slab）:
"No logo, no text, no screws"
← 已否决：品牌标识、文字信息、螺丝连接

鼠标（slab）:
"No logo, no text, no buttons"
← 已否决：品牌标识、文字信息、机械按钮

无人机（ring）:
"No logo, no glossy plastic, no exposed blades"
← 已否决：品牌标识、塑料材料、暴露叶片
```

### 禁止

❌ 过多约束（>5个）：`No logo, no text, no screws, no buttons, no plastic, no rubber, no LED, no screen...`
❌ 过少约束（<3个）：`No logo`
❌ 与产品无关：`No wheels`（对于鼠标）
❌ 抽象约束：`No bad quality`, `No cheap look`

---

## 方法5: 高频接触点精确法

### 原理

将MTH-006「用触觉节点承载确认与信任」和MTH-008「让高频小构件承载核心命题」落实到提示词中。

### 结构模板

```
[材料] + [精确位置] + [结构状态] + [功能暗示]

例：
- "brass brew slit flush in glass"
  → 材料：brass
  → 位置：brew slit（酿造缝隙）
  → 结构：flush in glass（与玻璃齐平）
  → 功能：brew（酿造功能暗示）

- "single brass start point on right"
  → 材料：brass
  → 位置：on right（右侧）
  → 结构：single start point（单一启动点）
  → 功能：start（启动功能暗示）

- "hairline OLED slot off-center forward"
  → 材料：OLED
  → 位置：off-center forward（前偏中心）
  → 结构：hairline slot（发丝缝隙）
  → 功能：显示/交互功能暗示
```

### 应用步骤

1. 从 DesignIR.interaction_nodes 提取高频操作
2. 确定每个操作的具体位置（左/右/前/后/上/下/中心/偏置）
3. 确定接触点的材料（通常与主材不同，形成对比）
4. 描述结构状态（flush/raised/recessed/flush-mounted）
5. 检查：是否精确？是否可定位？是否与功能相关？

---

## 方法6: 文化杂交注入法

### 原理

将文化/历史/地域元素作为方向差异化的核心维度，而非表面装饰。

### 类型

| 类型 | 结构 | 示例 |
|------|------|------|
| 历史对象×现代功能 | [历史对象] + [现代功能] | "三足石砚,东亚文房 × 西方萃取" |
| 地域材料×全球功能 | [地域材料] + [全球功能] | "Italian travertine base × coffee maker" |
| 生物形态×科技功能 | [生物形态] + [科技功能] | "jellyfish bell × camera drone" |

### 应用规则

1. 文化元素必须影响结构或交互，不能只是装饰
2. 文化来源必须可识别（用户能感知到）
3. 文化杂交必须与功能一致
4. 在提示词中自然嵌入，不强行标注

### 示例

```
❌ "一个带有中国风格的咖啡机"
✅ "Single black slate slab 6cm thick, recessed circular cup well, suspended brass drip nozzle with G2 arm joint"
（三足石砚的"石"+"圆形凹槽"+"悬挂"结构）
```

---

## 方法10: 中文提示词强制规则

### 原理

所有提示词必须以**中文为主体**，英文仅作为补充（品牌名、材料名、工艺名可保留英文）。这是为了确保AI图像生成模型正确理解中文语境下的设计描述。

### 规则

1. **主体描述用中文**：造型、形态、轮廓、关系、感觉等用中文
2. **专业术语可中英混用**：材料名（hairline-brushed titanium）、工艺名（CNC）、品牌名（LoveFrom）保留英文
3. **数字和尺寸用中文+阿拉伯数字**："150毫米长"、"42毫米直径"
4. **负面约束用中文**："无logo、无文字、无螺丝"
5. **摄影语法用英文**："Studio photograph, three-quarter view slightly above"保留（AI模型对此有稳定理解）

### 转换示例

```
❌ 旧版写法（全英文）：
"Studio photograph, three-quarter view slightly above, of an electric shaver, LoveFrom 2030, post-Apple Jony Ive. Hairline-brushed aluminum handle, 150mm long, 42mm diameter..."

✅ 旧版写法（中文主体）：
"Studio photograph, three-quarter view slightly above,
一款次世代电动剃须刀，LoveFrom 2030，post-Apple Jony Ive。
拉丝铝一体成型手柄，150毫米长，42毫米直径，微喷砂表面处理。
刀头与手柄间2毫米磁悬浮间隙，钕磁体缓冲，35毫米直径刀头模块，镍镀层镜面处理。
侧面触控条激活，拇指滑动触发磁吸微震+LED微光。
冷滑精准的触感反馈， effortless precision control。
无logo、无文字、无螺丝、无塑料、无橡胶。
Floats. Neutral gradient. Pure white background."
```

---

## 方法11: 大造型→部件关系→CMF→细节层次法

### 原理

设计描述必须从宏观到微观，先抓住大造型大感觉，再逐步细化到部件关系、CMF、细节特征。避免一上来就描述细节导致整体失控。

### 描述层次

```
第1层：大造型/大感觉/大风格
  → 整体轮廓、体量感、风格定位

第2层：部件造型与轮廓关系
  → 部件之间的连接方式：穿插/倒角/咬合/组合/连接/桥接
  → 部件之间的比例关系、节奏感

第3层：部件CMF
  → 每个部件的材料、颜色、表面处理
  → 材料之间的对比和呼应

第4层：特殊细节特征
  → 网格、纹理、刻度、灯光
  → 点睛之笔：小点、小凸点、小凹点、丝印图标

第5层：画面整体感觉
  → 灯光、背景、环境（当前统一纯白）
```

### 部件关系类型

| 关系类型 | 描述 | 示例 |
|----------|------|------|
| 穿插 | 一部件穿过另一部件 | 金属杆穿插玻璃主体 |
| 倒角 | 边缘倒角过渡 | G2圆角过渡 |
| 咬合 | 一部件咬入另一部件 | 卡扣咬合结构 |
| 组合 | 多个部件组合成整体 | 模块化组合 |
| 连接 | 部件之间通过连接件连接 | 铰链连接 |
| 桥接 | 一部件桥接两个部件 | 金属桥接片 |

### 应用示例

```
=== 第1层：大造型 ===
整体修长悬浮感，流线型轮廓，未来科技风格

=== 第2层：部件关系 ===
手柄主体与刀头模块通过磁悬浮间隙桥接，
刀头偏置15度，与手柄形成非对称动态比例

=== 第3层：部件CMF ===
手柄：拉丝铝，微喷砂，深空灰
刀头：镍镀层，镜面，银白色
间隙：磁体场，无直接接触

=== 第4层：细节特征 ===
侧面触控条：发丝级LED指示灯
刀头网面：精密蚀刻网格，0.1毫米间隙
底部：微型品牌刻字（点睛之笔）

=== 第5层：画面整体 ===
Floats. Neutral gradient. Pure white background.
```

---

## 方法12: 轻重缓急与点睛之笔法

### 原理

设计不能太寡淡（无亮点），也不能太乱太复杂（找不到重点）。要有轻有重，有显性有隐性，有主有次，有疏有密。

### 设计焦点原则

| 类型 | 特征 | 设计手法 |
|------|------|----------|
| **显性焦点** | 第一眼看到的 | 大比例差异、强烈材质对比、特殊形态 |
| **隐性细节** | 第二眼发现的 | 精致刻度、微凹点、隐藏式灯光 |
| **惊喜时刻** | 使用时发现的 | 触觉反馈、声音反馈、动态变化 |
| **暖心时刻** | 长期使用后感受到的 | 老化美感、维护便利性、情感连接 |

### 点睛之笔类型

1. **品牌标识**：微型logo、丝印图标、精致刻度
2. **触觉细节**：小凸点、小凹点、纹理变化
3. **灯光设计**：发丝级LED、渐变灯光、隐藏式灯光
4. **特殊材质**：局部金属镶嵌、透明窗口、磁性吸附
5. **特殊工艺**：激光蚀刻、微喷砂、阳极氧化渐变

### 应用规则

- 每个方向必须有**1-2个显性焦点**
- 每个方向必须有**2-3个隐性细节**
- 每个方向必须有**1个惊喜时刻或暖心时刻**
- 点睛之笔不能过多（≤3个），否则会混乱

### 示例

```
显性焦点：2毫米磁悬浮间隙（视觉奇观）
隐性细节：手柄底部微型品牌刻字、侧面发丝级LED
惊喜时刻：拇指滑动触控条时，磁吸微震+LED渐亮
暖心时刻：长期使用后，铝表面形成个人化的微划痕纹理
```

---

## 方法7: 固定语法结构法(本版本对齐 Google Cloud 官方公式)

### 原理

所有提示词共享同一语法结构,形成视觉语言一致性。**本版本(2026-06-23)对齐 Google Cloud Ultimate Prompting Guide 官方公式**:`Subject + Action + Location + Composition + Style`,Camera/Lighting 在第 5 段(末尾)而非第 1 段。理由:Nano Banana Pro 是 reasoning 模型,优先理解主体本身再理解摄影语境;摄影参数放第一句违反 Google 官方"Describe the scene, don't just list keywords"原则。

### 固定结构(对齐官方公式,中文主体)

```
[第1段 · Subject + Action + Location] —— 产品是什么(具体感官描述),在做什么,在哪
[第2段 · Composition] —— 构图、部件关系
[第3段 · 部件 CMF] —— 每个部件的材料 + 工艺(从 prompt-word-bank § 3 选,3 方向互斥)
[第4段 · 细节特征] —— 网格、纹理、刻度、灯光(从 prompt-word-bank § 5 选)
[第5段 · Style + 摄影语法 + Camera/Lighting] —— Studio photograph, three-quarter view, 50mm at f/1.8, three-point softbox, ...
[背景与负面约束]
```

### 对比示例(主体)

```coffee 机示例(对齐后):
一款单杯咖啡机,LoveFrom 2030,post-Apple Jony Ive。悬浮于台面,准备冲泡一杯浓缩咖啡。
整体板状造型,烟熏玻璃板悬浮于洞石底座之上,
玻璃与洞石通过 G2 圆角倒角过渡,黄铜酿造缝隙与玻璃齐平,
玻璃板:烟熏透明,微磨砂,主导材料
洞石底座:天然纹理,温暖触感,辅助材料
黄铜缝隙:发丝级精度,点状 LED 微光(非 amber 默认)
底部:微型品牌刻字(点睛之笔)

Studio photograph, 50mm at f/1.8, three-point softbox setup, three-quarter view slightly above. Neutral gradient background. Pure white.
无 logo、无文字、无螺丝。
```

```鼠标示例(对齐后):
一款无线鼠标,LoveFrom 2030,post-Apple Jony Ive。静置于桌面,等待操作。
流线型板状,前宽后窄,
抛光黑曜石板(主导材料,非默认 brushed metal),
压电表面无可见按钮,单一黄铜镶嵌点作为点睛之笔,
底部无缝切线,午夜黑。
底部微型呼吸灯指示(冷白 5000K,非暖白 3000K 默认)。

Studio photograph, 85mm macro lens, f/2.0, soft diffused light, three-quarter view from front. Pure white background.
无 logo、无文字、无按钮。
```

### 关键改动(对比旧版)

| 维度 | 旧版(方法 7 早期版本 ~ 上一版 file-hygiene) | 新版(本版本) |
|------|------------------------|-------------------|
| 摄影参数位置 | 第 1 段(Studio photograph, ... 开头) | 第 5 段(Style 段末尾) |
| 品牌语境位置 | 产品身份段第 1 句 | 第 1 段(Subject 主体内,跟随产品类型) |
| 数字精度 | ≥ 2 个精确数字(含 < 1mm) | ≤ 2 个 ≥ 1mm 粗数字,0 个 < 1mm |
| 长度 | 100+ 词(产品级革命路线) | 40-80 words sweet spot(ppl.studio 1000+ 张实测) |
| 工艺选择 | 默认 brushed/polished/matte | 从 prompt-word-bank § 3 选 ≥ 30 种,3 方向互斥 |
| 颜色选择 | 默认橙色/暖白(无词库) | 从 prompt-word-bank § 4 选,3 方向互斥 |
| 光感选择 | 默认 amber LED 暖白 | 从 prompt-word-bank § 5 选,3 方向互斥 |

### 应用规则

1. **第 1 段必须是 Subject + Action + Location**(产品是什么 + 在做什么 + 在哪)
2. **第 5 段才放摄影语法 + Camera/Lighting**(Studio photograph, 镜头,光位)
3. 数字精度只允许 ≤ 2 个 ≥ 1mm 粗数字(尺寸/比例/厚度),0 个 < 1mm
4. 长度 40-80 words sweet spot(过短 < 40 = under-specifying,过长 > 100 = 互相矛盾)
5. 工艺/颜色/光感词必须从 prompt-word-bank § 3/§ 4/§ 5 选,3 方向互斥
6. 中文为主体,英文仅保留材料名/工艺名/品牌名/Lovart 摄影语法(Studio photograph/three-point softbox)

---

```
## 提示词工程检查清单

### 材料精确度
- [ ] 主材名称精确（不说"金属"，说"hairline-brushed titanium"）
- [ ] 结构状态明确（slab/dome/ring/shell）
- [ ] 触感暗示存在（brushed/polished/matte/smoked）

### 几何精确度
- [ ] 至少2个精确数字（尺寸/角度/曲率/公差）
- [ ] 数字自然嵌入描述
- [ ] 数字服务于形态理解

### 悬浮感
- [ ] 包含"Floats"或等效描述
- [ ] 不落地、不放置于桌面
- [ ] 作为视觉句号出现在末尾

### 负面约束
- [ ] 3-5个具体否定
- [ ] 每个否定对应已否决特征
- [ ] 与产品类型强相关

### 高频接触点
- [ ] 至少1个精确描述
- [ ] 包含材料+位置+结构+功能
- [ ] 可定位、可感知

### 文化杂交（可选）
- [ ] 文化元素影响结构或交互
- [ ] 文化来源可识别
- [ ] 与功能一致

### 语法一致性
- [ ] 使用固定语法结构
- [ ] 摄影描述统一
- [ ] 三个方向语法一致
```

---

## 方法13: 提示词简化法

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 1 用户评分 1/10，提示词过载导致模型失效

### 原理

AI 图像生成模型对复杂提示词的遵循度有限。当提示词包含 50+ words、20+ 约束时，模型优先渲染核心概念（如 "mouse"），忽略大部分精细约束。

### 失效模式

| 模式 | 现象 | 触发条件 |
|------|------|----------|
| 概念覆盖 | 渲染默认品类原型 | 提示词中出现品类词（mouse/phone/coffee maker） |
| 数字忽略 | 忽略所有数字约束 | 提示词中包含 >2 个数字 |
| 材料简化 | 复杂材料渲染为塑料 | 材料描述 >2 层结构 |
| 背景污染 | 背景出现环境元素 | 背景描述不够强烈 |
| 细节抹除 | 精细细节被忽略 | 细节描述 >3 个 |

### 简化规则

1. **词数限制**: 30-50 words
2. **约束限制**: 5-7 个核心约束
3. **删除所有**:
   - 数字（mm/°/ratio/比例）
   - 交互描述（finger/touch/click/scroll zone）
   - 人体工学（wrist/palm/hand/posture）
   - 功能说明（sensor/feedback/pressure/tilt）
   - 文化概念直译（Cultural hybrid/history/regional）
   - 多层结构（layer A + layer B + layer C）
4. **保留**:
   - 品牌语境（LoveFrom 2030）
   - 核心形态（1-2 个形态词）
   - 主材（1 个感官材料）
   - 悬浮感（Floats/levitates）
   - 背景（pure white/no ground/no shadow）
   - 精简负面约束（3 个）

### 转换示例

```
❌ 过载提示词（120+ words）:
"Studio photograph... a next-generation wireless mouse, LoveFrom 2030...
Floating slab form, extreme flat proportion, 120mm long, 12mm thick, 10:1 aspect ratio.
Smoked glass slab body suspended over transparent glass base, hidden magnetic connection, 2mm levitation gap.
Metal border hairline-brushed titanium... Index finger touch zone... Middle finger scroll zone...
Palm hovers 20-30mm above body... Pressure-sensing click... Hairline LED slit...
Cultural hybrid: magnetic levitation tech × traditional paperweight..."

✅ 简化提示词（30 words）:
"Studio photograph, three-quarter view slightly above, LoveFrom 2030, post-Apple Jony Ive.
Extremely flat rectangular slab, paper-thin profile, smoked glass surface, hairline metal border.
Floats. Pure white background, no ground, no shadow.
No logo, no text, no visible screws."
```

### 检查清单

- [ ] 提示词 < 50 words?
- [ ] 约束 < 10 个?
- [ ] 无数字（mm/°/ratio）?
- [ ] 无交互描述（finger/touch/click）?
- [ ] 无人体工学（wrist/palm/hand）?
- [ ] 无功能说明（sensor/feedback/pressure）?
- [ ] 无文化概念直译（Cultural hybrid/history）?
- [ ] 核心形态清晰（1-2 个词）?
- [ ] 主材单一（1 个感官材料）?
- [ ] 悬浮感明确（Floats/levitates）?
- [ ] 背景纯净（pure white/no ground）?
- [ ] 负面约束精简（3 个）?

### 与历史版本的关键差异

| 维度 | 旧版 | 历史版（新增） |
|------|------|-------------|
| 词数限制 | 无限制，语义完整优先 | 30-50 words |
| 数字保留 | 强制保留 ≥2 个 | 删除所有数字 |
| 交互描述 | 强制保留高频接触点 | 删除所有交互 |
| 文化杂交 | 自然嵌入 | 删除概念，保留视觉描述 |
| 功能说明 | 可保留 | 删除所有功能 |

---

## 方法14: 品类锚定法

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 2 简化提示词导致品类识别为零，发现核心死结

### 核心死结

```
说"mouse" → 模型渲染默认鼠标原型（无突破）
不说"mouse" → 模型不认识品类（不像鼠标）
说"mouse" + 突破约束 → 模型忽略突破约束（仍是默认原型）
```

### 原理

模型必须认识品类，但品类词会导致默认原型。解决方法是**保留品类词但立即否定默认原型**，让模型知道"这是什么"但"不要长这样"。

### 三段式结构

```
1. 品类锚定: "A [品类] that doesn't look like a [品类]"
2. 突破形态: "[极端形态词], [非传统材料], [识别性特征]"
3. 背景控制: "Floats. Pure white. No ground."
```

### 示例

**鼠标**:
```
"A mouse that doesn't look like any mouse you've seen.
Paper-thin glass slab, floating, no buttons visible.
Floats. Pure white background."
```

**咖啡机**:
```
"A coffee maker that doesn't look like any coffee maker.
Black stone slab, recessed cup well, brass drip nozzle.
Floats. Pure white background."
```

**耳机**:
```
"Headphones that don't look like any headphones.
Two carbon rings, kevlar tension lines, no headband.
Floats. Pure white background."
```

### 规则

1. **必须保留品类词**（mouse/phone/coffee maker/headphones）
2. **必须立即否定默认原型**（"doesn't look like" / "unlike any"）
3. **突破形态必须极端**（"paper-thin" "tower-like" "pebble-shaped" "ring-shaped"）
4. **形态描述不得超过10个词**
5. **不得使用数字**（mm/°/ratio）
6. **不得描述交互/功能**

### 检查清单

- [ ] 包含品类词？
- [ ] 包含否定默认原型？
- [ ] 突破形态极端？
- [ ] 无数字？
- [ ] 无交互？
- [ ] 无功能？
- [ ] 背景纯净？

### 与历史版本的关键差异

| 维度 | 历史版（简化法） | 旧版（品类锚定法） |
|------|---------------|-------------------|
| 品类词 | 删除 | **保留并否定** |
| 核心问题 | 提示词过载 | 品类识别 vs 形态突破的死结 |
| 适用场景 | 抽象物体/无品类 | **消费电子产品/有品类** |
| 失败率 | 100%（品类丢失） | 预计 <30% |

---

## 方法15: 功能暗示法

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 用户反馈"功能性的按键、功能性的操作的交互功能的描述，一定要细节细腻"
> **适用范围**: 所有需要保留功能性操作暗示的消费电子产品
> **验证**: Round 3 无线充电器设计，首次达到艾维级（D1=80, D3=82），品类锚定法有效

### 原理

AI图像生成模型无法渲染"功能"（按压反馈、旋转阻尼、触控响应），但可以渲染"形态"（凸起、凹陷、线条、纹理）。**用形态暗示功能，不用功能描述形态**。

### 核心规则

1. **删除所有功能描述**：rotary knob / slide switch / press button / touch zone
2. **保留形态暗示**：flush circular depression / slight raised line / small rectangular recess
3. **限制数量**：每个产品最多2-3个功能暗示
4. **用材料/纹理强化暗示**：brass ring around depression / matte texture on line

### 功能暗示对照表

| 功能元素 | ❌ 删除（功能描述） | ✅ 保留（形态暗示） |
|----------|---------------------|---------------------|
| 旋钮 | rotary knob with detents | flush circular depression, subtle texture |
| 开关 | slide switch, toggle | slight raised line, matte finish |
| 按键 | press button, tactile feedback | small rectangular recess, flush surface |
| 接口 | USB-C port, charging hole | small rectangular recess, no visible pins |
| 滚轮 | scroll wheel, rubber grip | cylindrical groove, hairline texture |
| 显示屏 | OLED display, touch screen | black rectangular plane, glossy surface |
| 扬声器 | speaker grille, audio driver | perforated circular area, fabric texture |
| 指示灯 | LED indicator, status light | small circular dot, warm glow |
| 摄像头 | camera lens, sensor array | small circular depression, glass surface |
| 天线 | antenna line, signal strip | thin metallic line, hairline finish |

### 产品类型功能暗示示例

**鼠标**:
```
❌ "Left click button, right click button, scroll wheel, DPI switch"
✅ "No buttons visible, flush surface, slight cylindrical groove"
```

**咖啡机**:
```
❌ "Brew button, steam knob, cup warmer, water level indicator"
✅ "Small circular depression, brass ring, slight rectangular recess"
```

**耳机**:
```
❌ "Volume rocker, play/pause button, noise cancel switch, charging port"
✅ "Slight raised line, small circular dot, thin rectangular recess"
```

**手机**:
```
❌ "Power button, volume buttons, camera lens, charging port"
✅ "Thin metallic line, small circular depression, flush rectangular recess"
```

**灯具**:
```
❌ "Dimmer switch, color temperature button, power cord, hanging chain"
✅ "Small circular depression, thin power line, subtle mounting point"
```

### 检查清单

- [ ] 删除所有功能描述（rotary/slide/press/touch/scroll）？
- [ ] 用形态暗示替代（flush depression/raised line/recess/groove）？
- [ ] 功能暗示 ≤ 3 个？
- [ ] 用材料/纹理强化暗示？
- [ ] 不描述动态/使用状态？

### 与历史版本的关键差异

| 维度 | 历史版(品类锚定法) | 旧版(功能暗示法) |
|------|-------------------|-------------------|
| 功能描述 | 全部删除 | 删除功能描述,保留形态暗示 |
| 按键/旋钮 | 不出现 | 用 flush depression/raised line 暗示 |
| 适用产品 | 极简产品(无操作界面) | 功能性产品(有操作界面) |
| 细节程度 | 极简 | 细节细腻(形态层面) |

---

## 方法16: 模型适配优先决策树(本版本新增 · 2026-06-23)

### 原理

方法 1-15 是历史累积的提示词构造规则,但**它们没有回答一个根本问题:目标模型是谁**。Lovart Nano Banana Pro / Midjourney v6 / DALL-E 3 / Flux 1.0 Pro / GPT Image 1.5 各有不同的遵循度和训练集先验。同一条 prompt 在不同模型下渲染差异巨大(见 pitfall-043)。

**本版本新增方法 16**,在跑 STEP-15 编译提示词之前,必须先做模型适配决策。

### 决策树

```
Q1: 目标模型是 Lovart Nano Banana Pro / 2 还是其他?
├─ Lovart Nano Banana Pro / 2 → 走"链路 B(精简+品类锚定)" + 启用方法 13/14/15 + 跳过方法 1/2 的 < 1mm 数字
└─ 其他模型(Midjourney v6 / DALL-E 3 / Flux 1.0 Pro / GPT Image 1.5)→ 走"链路 A(产品级)" + 启用方法 1/2 + 可用更精确数字

Q2: 提示词长度?(ppl.studio 1000+ 张实测 sweet spot)
├─ 40-80 words → 标准 ✅
├─ < 40 words → under-specifying,补充感官细节
└─ > 100 words → 互相矛盾,精简

Q3: 数字精度?
├─ ≤ 2 个 ≥ 1mm 粗数字(尺寸/比例/厚度)→ ✅
├─ 0 个 < 1mm 数字 → ✅(Nano Banana Pro 100% 丢 < 1mm,pittfall-039/043 实证)
└─ > 2 个数字或含 < 1mm → 违反硬约束,删减

Q4: 摄影参数位置?
├─ 第 5 段(Style 段)→ ✅(Google Cloud 官方公式)
├─ 第 1 段 → 违反官方公式,挪到第 5 段
└─ 散落多处 → 集中在第 5 段

Q5: 工艺/颜色/光感是否从 prompt-word-bank § 3/§ 4/§ 5 选?
├─ 是 + 3 方向互斥 → ✅
├─ 是 + 3 方向同质化 → 违反 pitfall-034/035 方向同质化,重新分配
└─ 否(自由发挥)→ 警告:大概率走训练集默认(brushed/amber LED/暖白)

Q6: 用户是否拍板?(防 pitfall-046)
├─ 用户已明确回复"按建议改"→ ✅ 可以 bump SKILL.md
└─ 用户还没拍板 → STOP,先回到调研/对比阶段
```

### 模型路由速查表

| 模型 | 提示词策略 | 数字精度 | 摄影锚位置 | 词库使用 |
|------|----------|---------|----------|---------|
| Lovart Nano Banana Pro / 2 | 链路 B(精简 + 品类锚定) | ≤ 2 个 ≥ 1mm | 第 5 段 | 强制使用 prompt-word-bank § 3/§ 4/§ 5 |
| Midjourney v6 | 链路 A(产品级) | ≤ 3 个 ≥ 1mm | 第 1 段或第 5 段皆可 | 可自由发挥 |
| DALL-E 3 | 链路 A | ≤ 2 个 ≥ 1mm | 第 1 段 | 可自由发挥 |
| Flux 1.0 Pro | 链路 A | ≤ 2 个 ≥ 1mm | 第 1 段或第 5 段皆可 | 可自由发挥 |
| GPT Image 1.5 | 链路 A | ≤ 2 个 ≥ 1mm | 第 1 段 | 可自由发挥 |

**当前默认模型**:Lovart Nano Banana Pro(本 skill 跟 Lovart skill 集成),走链路 B 强制使用词库。

### 关键洞察

- **Nano Banana Pro = Gemini 3 Pro Image,带 Think Mode 推理**。给"意图"比给"参数"更有效
- **Pro 100% 丢 < 1mm 数字是官方明示下限**,不是 bug,改 SKILL.md 没用
- **Pro 已知 10-20% 概率完全忽略 prompt**(Google 官方论坛 bug),SKILL.md 改不了
- **Pro 训练集先验**:消费电子金属默认 brushed / 按键 LED 默认 amber / 灯光默认暖白 → 工艺/颜色/光感词库强制使用是绕开训练集先验的唯一手段

### 应用规则

1. 跑 STEP-15 前先走 Q1-Q6 决策树
2. Lovart Nano Banana Pro 是当前默认模型(绑 Lovart skill),走链路 B
3. 词库 § 3/§ 4/§ 5 强制使用,3 方向互斥
4. 决策结果写进 STEP-15 的 WorkflowStepRecord 输入段

### 与其他方法的关系

| 方法 | 与方法 16 的关系 |
|------|-----------------|
| 方法 1/2/7/9 | 链路 A(产品级),适用于非 Lovart 模型或 Pro 不读时备用 |
| 方法 13/14/15 | 链路 B(精简+品类锚定),默认与 Lovart Pro 配套 |
| 方法 7(本版本 改写)| 是链路 B 的具体结构模板 |
| 方法 9(本版本 改写)| 是链路 B 的品牌语境锚处理 |
| 方法 11「5 层层次法」| 与方法 7 的结构对齐(Subject+Action+Location+Composition+Style) |
| 新增方法 16 | **决策框架**,先选模型再选链路再选具体方法 |

---

## 来源

- Round 1 失败分析：用户评分 1/10，提示词过载
- Round 2 失败分析：用户评分 1/10，品类识别为零
- Round 3 验证：无线充电器设计，首次达到艾维级（D1=80, D3=82），品类锚定法有效
- 模型失效模式：Lovart Nano Banana Pro / Nano Banana 2 输出分析
- REF-PROMPT-002: 中文提示词压缩规则
- REF-QUALITY-002: 图片评审合同
- 用户反馈：2026-06-21 "功能性的按键、功能性的操作的交互功能的描述，一定要细节细腻"
