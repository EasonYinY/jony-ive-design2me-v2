---
reference_id: REF-GUIDE-015-03
title: 优秀提示词词库
category: guides
used_when:
  - PROMPT-COMPILATION
  - PROMPT-REWRITING
called_by:
  - prompt-engineering
  - prompt-contract
  - prompt-compression
depends_on:
  - REF-GUIDE-008
  - REF-PROMPT-001
  - REF-PROMPT-002
outputs:
  - prompt_word_bank
---

# 优秀提示词词库

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 用户要求从优秀提示词中提取思维模式，适应所有产品设计

---

## 词库结构

本词库从9个优秀提示词（3个产品×3轮迭代）中提取高频词汇、句式结构和思维模式，供所有产品设计任务参考。

---

## 一、基础形态词库

### 1.1 核心体块

| 英文 | 中文 | 适用产品 | 变形方向 | 姿态词 |
|------|------|----------|----------|--------|
| **slab** | 板状 | 鼠标、咖啡机、灯具 | 弯曲、倾斜、挖空 | Floats |
| **block** | 块状 | 音箱、充电器、工具 | 倒角、分割、层叠 | rests on / Floats |
| **cylinder** | 圆柱 | 灯具、容器、笔 | 锥化、扭曲、挖空 | suspended / Floats |
| **dome** | 圆顶 | 鼠标、控制器、盖子 | 压扁、偏移、切割 | nestles / Floats |
| **wedge** | 楔形 | 支架、底座、工具 | 倾斜、弯曲、分割 | rests on |
| **disc** | 圆盘 | 旋钮、底座、托盘 | 凹陷、边缘处理 | Floats |
| **shell** | 壳状 | 耳机、容器、保护罩 | 包裹、镂空、分层 | nestles / Floats |
| **ring** | 环状 | 灯具、无人机、装饰 | 连接、悬挂、旋转 | suspended / Floats |

### 1.2 形态修饰词

| 英文 | 中文 | 含义 | 示例 |
|------|------|------|------|
| **solid** | 实心 | 无空心，厚重感 | solid aluminum slab |
| **hollow** | 空心 | 内部挖空，轻量化 | hollow cylinder |
| **tapered** | 锥化 | 一端宽一端窄 | front wider, rear tapered |
| **flared** | 外扩 | 边缘向外展开 | flared base |
| **recessed** | 凹陷 | 表面向内凹陷 | recessed circular cup well |
| **raised** | 凸起 | 表面向外凸起 | raised button |
| **flush** | 齐平 | 与表面齐平 | brass brew slit flush in glass |
| **suspended** | 悬浮 | 悬挂于上方 | suspended brass drip nozzle |

---

## 二、几何术语词库

### 2.1 连续性术语

| 术语 | 含义 | 适用场景 | 示例 |
|------|------|----------|------|
| **G2 continuous** | 曲率连续 | 曲面过渡，无视觉突变 | G2 fillet edges |
| **G1 continuous** | 切线连续 | 边缘过渡，无棱角 | G1 chamfer |
| **tangent** | 相切 | 曲线/曲面平滑连接 | sweeping tangent base |
| **fillet** | 圆角 | 内圆角过渡 | 8mm fillet radius |
| **chamfer** | 倒角 | 斜角过渡 | 45° chamfer |
| **blend** | 混接 | 曲面自然过渡 | G2 blend at anchor |
| **step** | 台阶 | 垂直落差 | vertical step between deck and sidewall |

### 2.2 精确数字模板

| 类型 | 模板 | 示例 |
|------|------|------|
| **厚度** | Xcm thick / Xmm thick | 6cm thick, 1.5cm at peak |
| **长度** | Xmm long / Xcm wide | 120mm long, 65mm wide |
| **角度** | X-degree forward lean | 6-degree forward lean |
| **曲率半径** | Xmm fillet radius | 8mm fillet radius |
| **公差** | Xmm L/R / Xmm凹陷 | 0.1mm L/R, 0.3mm凹陷 |
| **悬浮高度** | levitates Xmm above | levitates 2mm above glass pad |
| **比例** | X:Y ratio | 3:2 length-width ratio |

---

## 三、材料词库(本版本扩展)

### 3.1 主导材料 + 工艺组合(单材质策略 · ≥ 30 种工艺)

**工艺分类**(从 Nano Banana Pro 训练集先验角度覆盖,避免单一 brushed/polished/matte 陷阱):

#### 3.1.1 机械处理(7 种)

| 材料 | 工艺 | 基础形态 | 完整示例 |
|------|------|----------|----------|
| **aluminum** | hairline-brushed | slab / block | hairline-brushed aluminum slab |
| **aluminum** | **circular-brushed**(圆周拉丝) | disc / cylinder | circular-brushed aluminum disc |
| **aluminum** | **bead-blasted**(喷珠) | block | bead-blasted aluminum block |
| **aluminum** | **shot-peened**(喷丸) | block | shot-peened aluminum housing |
| **steel** | **mirror-polished**(镜面抛光) | slab | mirror-polished steel slab |
| **steel** | **honed-steel**(精磨) | block | honed-steel base |
| **titanium** | hairline-brushed | slab / disc | hairline-brushed titanium slab |

#### 3.1.2 化学处理(4 种)

| 材料 | 工艺 | 完整示例 |
|------|------|----------|
| **aluminum** | **anodized-II**(II 型硫酸阳极氧化) | anodized aluminum in deep space gray |
| **aluminum** | **anodized-III-hardcoat**(III 型硬质阳极氧化) | III-hardcoat anodized aluminum housing |
| **aluminum** | **micro-arc-oxidation**(微弧氧化,MAO) | micro-arc-oxidized aluminum ceramic shell |
| **titanium** | **blackened / patinated**(发黑 / 旧化) | patinated titanium slab with bronze undertones |

#### 3.1.3 涂层(8 种 · 解决"全是金属拉丝"问题)

| 材料 | 工艺 | 完整示例 |
|------|------|----------|
| **steel** | **PVD-titanium-nitride**(物理气相沉积氮化钛) | PVD titanium nitride coated steel ring |
| **steel** | **DLC-coating**(类金刚石碳涂层) | DLC-coated steel driver |
| **steel** | **ceramic-coated**(陶瓷涂层) | ceramic-coated steel shell |
| **steel** | **teflon-coated**(特氟龙涂层) | teflon-coated steel surface |
| **aluminum** | **powder-coated**(粉末喷涂) | powder-coated aluminum in matte black |
| **aluminum** | **enameled**(搪瓷涂层) | enameled aluminum in deep blue |
| **steel** | **cerakoted**(陶瓷涂料) | cerakoted steel in coyote tan |
| **steel** | **rubberized-coating**(橡胶化涂层) | rubberized-coated steel grip |

#### 3.1.4 表面图案(4 种)

| 材料 | 工艺 | 完整示例 |
|------|------|----------|
| **steel** | **guilloché**(机器雕刻花纹) | guilloché-engraved steel dial |
| **aluminum** | **laser-engraved**(激光雕刻) | laser-engraved aluminum logo plate |
| **steel** | **micro-etched**(微蚀刻) | micro-etched steel mesh |
| **aluminum** | **perforated**(冲孔) | perforated aluminum grille |

#### 3.1.5 镜面(3 种)

| 材料 | 工艺 | 完整示例 |
|------|------|----------|
| **steel** | **piano-black**(钢琴黑镜面) | piano-black polished steel slab |
| **steel** | **super-mirror**(超镜面) | super-mirror stainless surface |
| **obsidian** | **polished-obsidian**(抛光黑曜石) | polished obsidian dome |

#### 3.1.6 复合(4 种)

| 材料 | 工艺 | 完整示例 |
|------|------|----------|
| **composite** | **carbon-fiber-woven**(碳纤维编织) | carbon-fiber-woven slab |
| **composite** | **forged-carbon**(锻造碳) | forged-carbon irregular pattern |
| **composite** | **kevlar-woven**(凯夫拉编织) | kevlar-woven protective shell |
| **composite** | **aramid-laminate**(芳纶层压) | aramid-laminate structural shell |

#### 3.1.7 半透明(3 种)

| 材料 | 工艺 | 完整示例 |
|------|------|----------|
| **glass** | **smoked-glass**(烟熏玻璃) | smoked glass slab |
| **glass** | **frosted-glass**(磨砂玻璃) | frosted glass diffuser |
| **glass** | **backlit-translucent**(背光半透明) | backlit translucent resin panel |

#### 3.1.8 自然材料(3 种)

| 材料 | 工艺 | 完整示例 |
|------|------|----------|
| **stone** | **honed-stone**(精磨石材) | honed-stone base |
| **wood** | **dark-walnut**(深胡桃木) | dark walnut plinth |
| **leather** | **leather-burnished**(磨光皮革) | leather-burnished grip wrap |

#### 3.1.9 喷漆(4 种)

| 材料 | 工艺 | 完整示例 |
|------|------|----------|
| **aluminum** | **matte-painted**(哑光喷漆) | matte-painted aluminum in forest green |
| **aluminum** | **high-gloss-painted**(高光喷漆) | high-gloss piano-black painted aluminum |
| **steel** | **satin-painted**(缎面喷漆) | satin-painted steel surface |
| **plastic** | **rubberized-paint**(橡胶漆) | rubberized-paint grip surface |

### 3.2 工艺选择硬约束(本版本新增 · 防 pitfall-034/035 方向同质化)

**3 方向必须 3 种工艺互斥**,从以下 9 个子类别选:

```markdown
[方向 1 工艺] ∈ 机械处理 / 化学处理 / 涂层 / 表面图案 / 镜面 / 复合 / 半透明 / 自然 / 喷漆
[方向 2 工艺] ∈ 上述 9 子类别之一,但与方向 1 不同子类别
[方向 3 工艺] ∈ 上述 9 子类别之一,但与方向 1+2 都不同子类别
```

**示例**:

| 方向 | 工艺 | 子类别 |
|------|------|--------|
| D1 鹅卵石户外灯 | bead-blasted aluminum | 机械处理(喷珠) |
| D2 水滴露营灯 | anodized-III-hardcoat silicone | 化学处理(III 型硬质) |
| D3 禅石三模块 | forged-carbon + brass inlay | 复合 + 镶嵌 |

**禁止**:
- ❌ 3 方向都用 hairline-brushed(同质化,pittfall-034 实证)
- ❌ 工艺词自由发挥 → 默认走 brushed / polished / matte 三件套
- ❌ 跨子类别搭配("bead-blasted + mirror-polished + shot-peened" 全是机械处理类,不算互斥)

### 3.3 辅助材料(最多 1 种 · 不强制 LED 暖白)

| 材料 | 功能 | 位置 | 示例 |
|------|------|------|------|
| **brass** | 点缀/缝隙 | 缝隙/按钮/镶嵌 | brass brew slit(温润黄铜) |
| **copper** | 点缀/镶嵌 | 缝隙/边缘/接触点 | copper accent ring |
| **LED**(从 § 5 光感词库选) | 指示/氛围 | 缝隙/边缘/底部 | **cool-white 6500K dot indicator**(非 amber 默认) |
| **glass** | 透明/光学 | 顶部/窗口 | transparent glass window |
| **rubber** | 防滑/缓冲 | 底部/握持区 | rubber foot pad |
| **fabric** | 柔软/携带 | 织带/包裹 | woven carrying lanyard |
| **resin** | 半透明体光 | 内部/光源区 | translucent resin body glow |

---

## 四、颜色词库(本版本新增 · 解决"按键全是橙色"问题)

### 4.1 10 种主色名(3 方向必须 3 种互斥)

| 主色名 | 触发关键词 | 适用场景 | 视觉特征 |
|--------|------------|----------|----------|
| **深空灰** | space gray / graphite / charcoal | 高端工业 / 3C | 冷调中性,反光柔和 |
| **哑光黑** | matte black / piano black / obsidian | 极简 / 高端 | 强吸光,几乎无反射 |
| **月白** | porcelain white / off-white / bone | 极简 / 医疗 / 美妆 | 暖白调,反光均匀 |
| **暖砂金** | champagne gold / warm brass | 复古奢华 / 配饰 | 暖金属感,黄橙底色 |
| **玫瑰金** | rose gold / pink champagne | 美妆 / 配饰 | 粉橙金属感 |
| **陶土橙** | terracotta / clay / rust | 暖色系 / 室内 | 哑光红橙,自然质感 |
| **勃艮第** | burgundy / wine / oxblood | 复古 / 高端配饰 | 深红带紫调 |
| **雾绿** | sage / olive / forest | 自然系 / 户外 | 低饱和绿,哑光 |
| **哑光蓝** | navy / cobalt / ink blue | 冷色系 / 商务 | 深蓝,低反光 |
| **焦糖棕** | caramel / cognac / tobacco | 复古 / 木材配饰 | 暖棕,带红调 |

### 4.2 颜色选择硬约束(防 pitfall-034/035 同质化)

**3 方向必须 3 种主色互斥**:

```markdown
D1 主色 ≠ D2 主色 ≠ D3 主色
且三者必须从 10 种主色选,不允许"灰色""白色"等抽象描述
```

**示例**:

| 方向 | 主色 | 来源 |
|------|------|------|
| D1 鹅卵石户外灯 | 哑光黑 + 暖砂金点缀 | § 4.1 主色 #2 + #4 |
| D2 水滴露营灯 | 月白 + 玫瑰金点缀 | § 4.1 主色 #3 + #5 |
| D3 禅石三模块 | 焦糖棕 + 勃艮第点缀 | § 4.1 主色 #10 + #7 |

**禁止**:
- ❌ 3 方向都用"金属灰"(同质化)
- ❌ 颜色自由发挥 → 默认走黑色 + 暖白
- ❌ 抽象颜色名("高级灰""质感白")

---

## 五、光感词库(本版本新增 · 解决"灯光全是暖白"问题)

### 5.1 10 类光感(3 方向必须 3 种互斥)

| 类型 | 词汇 | 视觉特征 |
|------|------|----------|
| **点光** | pinhole LED / dot-matrix LED / single-pixel indicator | 小点光源,1-3mm |
| **线光** | hairline slit / optical-fiber strip / edge-lit groove | 细线光源,0.5-2mm 宽 |
| **面光** | diffused panel / frosted glow / area light | 均匀面光源 |
| **体光** | volumetric / internal glow / underlit core | 立体内部发光,光从物体内部透出 |
| **长虹玻璃** | fluted glass / reeded glass / linear-prism glass | 垂直条纹折射,光斑有方向性 |
| **衍射** | fresnel / rainbow-cast / dichroic | 折射分光,产生彩色光斑 |
| **漫反射** | bounced / soft-cast / wraparound | 柔和扩散,无明显光源 |
| **方向光** | edge-grazing / backlit / rim-lit / side-lit | 强调轮廓,光源来自特定方向 |
| **色温**(6 选 1) | cool-white 6500K / neutral-white 5000K / warm-white 3000K / amber 2700K / red-LED / blue-LED / green-LED | 显性色温,不是默认暖白 |
| **动态** | tri-color RGB / individually-addressable / pulsing / breathing | 动态变化,需配合时间维度 |

### 5.2 光感选择硬约束(防 pitfall-034/035 同质化)

**3 方向必须 3 种光感互斥**:

```markdown
D1 光感 ≠ D2 光感 ≠ D3 光感
且三者必须从 10 类光感选(类型 + 色温 + 动态)
```

**示例**:

| 方向 | 光感 | 来源 |
|------|------|------|
| D1 鹅卵石户外灯 | 线光 + cool-white 6500K | § 5.1 线光 + 色温 cool-white |
| D2 水滴露营灯 | 体光 + amber 2700K + breathing | § 5.1 体光 + 色温 amber + 动态 breathing |
| D3 禅石三模块 | 长虹玻璃 + neutral-white 5000K | § 5.1 长虹玻璃 + 色温 neutral |

**禁止**:
- ❌ 3 方向都用 "amber LED hairline"(同质化,导致暖白默认)
- ❌ "LED 灯"自由发挥 → 默认单点暖白
- ❌ 混合多个色温("暖白 + 冷白混光") → 模型默认走单一色温

---

## 四、姿态词库

| 姿态词 | 适用基础形态 | 含义 | 示例 |
|--------|-------------|------|------|
| **Floats** | slab, block, disc | 悬浮于画面中 | Floats. Neutral gradient. |
| **levitates Xmm** | slab, disc | 精确悬浮高度 | levitates 2mm above glass pad |
| **rests on** | block, wedge | 放置于底座 | rests on travertine base |
| **suspended** | cylinder, ring | 悬挂状态 | suspended by three kevlar lines |
| **nestles** | dome, shell | 半嵌入/半包裹 | nestles in palm |
| **perches** | block, wedge |  perched on edge | perches on marble edge |

---

## 五、负面约束词库

### 5.1 默认约束（3-5个）

| 约束 | 含义 | 适用产品 |
|------|------|----------|
| **No logo** | 无品牌标识 | 所有产品 |
| **No text** | 无文字信息 | 所有产品 |
| **No screws** | 无螺丝连接 | 大多数产品 |
| **No visible buttons** | 无可见按钮 | 鼠标、控制器 |
| **No glossy plastic** | 无光泽塑料 | 高端产品 |
| **No exposed blades** | 无暴露叶片 | 无人机、风扇 |
| **No seams** | 无接缝 | 无缝产品 |
| **No decorative grooves** | 无装饰凹槽 | 极简产品 |
| **No LED strips** | 无LED灯带 | 非灯具产品 |
| **No sharp edges** | 无锐边 | 手持产品 |

### 5.2 按基础形态分类

| 基础形态 | 默认约束 | 可选补充 |
|----------|----------|----------|
| **slab** | No logo, no text, no screws | no visible buttons, no glossy plastic |
| **block** | No logo, no text, no seams | no decorative grooves, no LED strips |
| **cylinder** | No logo, no text, no joints | no visible wiring, no mounting brackets |
| **dome** | No logo, no text, no flat surfaces | no sharp edges, no plastic |
| **ring** | No logo, no text, no exposed blades | no glossy plastic, no decorative elements |

---

## 六、高频句式模板

### 6.1 标准句式

```
Studio photograph, [镜头],
[产品类型]，LoveFrom 2030，post-Apple Jony Ive。
[基础形态]，[精确尺寸]，[变形规则]，[几何术语]。
[材料职责]，[表面处理]，[触感暗示]。
[高频接触点]，[功能暗示]。
[姿态词]。
[背景]。
[负面约束]。
```

### 6.2 优秀示例拆解

**示例1: 鼠标（单材质 slab）**
```
Studio photograph, three-quarter view slightly above,
一款无线鼠标，LoveFrom 2030，post-Apple Jony Ive。
Solid carbon fiber slab, 1.2cm at highest, six-degree forward lean,
G2 palm dome, sweeping tangent base, no parting line, matte black.
Floats. Neutral gradient.
No logo, no text, no buttons.
```

**拆解：**
- 基础形态：slab
- 精确尺寸：1.2cm at highest
- 变形规则：six-degree forward lean（人体工学）
- 几何术语：G2 palm dome, sweeping tangent base
- 单材质：matte carbon fiber
- 姿态：Floats
- 负面约束：3个

**示例2: 咖啡机（单材质+辅助材质）**
```
Studio photograph, three-quarter view slightly above,
一款单杯咖啡机，LoveFrom 2030，post-Apple Jony Ive。
Smoked glass slab suspended over a travertine base,
brass brew slit flush in glass, G2 fillet edges,
sweeping tangent into base, warm walnut beneath, amber LED hairline at slit.
Floats. Neutral gradient.
No logo, no text, no screws.
```

**拆解：**
- 基础形态：slab（主导）+ base（辅助）
- 精确尺寸：无显性数字，但"slab"暗示厚度
- 变形规则：suspended over（空间关系）
- 几何术语：G2 fillet edges, sweeping tangent
- 单材质主导：smoked glass（80%视觉）
- 辅助材质：travertine base, brass slit, walnut
- 姿态：Floats
- 负面约束：3个

---

## 七、思维模式提炼

### 7.1 单材质主导思维

```
不是：titanium + carbon fiber + glass + wood
而是：solid titanium slab（主导）+ brass accent（辅助，仅1种）

核心：视觉焦点 = 材料诚实 = 单材质可识别
```

### 7.2 基础形态锁定思维

```
不是："整体流线型，有机曲线"
而是："slab（基础）+ 前宽后窄（变形）+ 6°前倾（人体工学）+ G2 fillet（几何控制）"

核心：骨架（基础体块）→ 肌肉（变形规则）→ 皮肤（表面处理）
```

### 7.3 理性-有机转换思维

```
不是："随意曲线，自由曲面"
而是："从手掌握持曲线偏移3mm（人体工学）→ G2连续曲面（几何控制）→ 碳纤维可成型（材料约束）"

核心：每个曲面必须有来源、有依据、可解释
```

### 7.4 姿态锁定思维

```
不是："放在桌上"
而是："slab → Floats（悬浮）" 或 "block → rests on（放置但有底座）"

核心：姿态是基础形态的延伸，不是独立选择
```

### 7.5 负面约束精简思维

```
不是："No logo, no text, no screws, no buttons, no plastic, no rubber, no LED..."
而是："No logo, no text, no screws"（3个，与slab一致）

核心：约束是设计决策的否定，不是质量要求的否定
```

---

## 八、应用检查清单

### 8.1 提示词自检

- [ ] 是否先定义基础体块？
- [ ] 是否有精确尺寸（至少2个数字）？
- [ ] 是否使用几何术语（G2/G1/fillet/chamfer/tangent/step）？
- [ ] 变形是否有理性依据？
- [ ] 是否单材质主导（80%视觉面积）？
- [ ] 辅助材料是否≤1种？
- [ ] 是否有姿态锁定词？
- [ ] 负面约束是否3-5个？
- [ ] 是否包含显性焦点+隐性细节？
- [ ] 是否包含点睛之笔？

### 8.2 失败模式识别

| 失败模式 | 特征 | 修正 |
|----------|------|------|
| **有机失控** | 无基础体块，直接曲线 | 退回STEP-10，锁定基础形态 |
| **材质堆砌** | 3种以上材料并列 | 选择1种主导，删除其他 |
| **数字缺失** | 无精确数字 | 添加尺寸+角度/曲率 |
| **几何模糊** | 无G2/G1/fillet等术语 | 添加几何控制术语 |
| **姿态混乱** | 落地/放置/悬浮不一致 | 根据基础形态选择姿态词 |
| **约束过多** | >5个负面约束 | 精简到3-5个 |
| **约束过少** | <3个负面约束 | 添加与产品相关的约束 |

---

## 九、来源

- 优秀提示词分析：9个提示词（3产品×3轮迭代）
- REF-GUIDE-008: 提示词工程方法
- REF-DESIGN-002: 形态比例与部件层级
- REF-QUALITY-001: 审美收敛质量门
- 用户反馈 2026-06-21: mouse nextgen 失败诊断
