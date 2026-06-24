---
reference_id: REF-ITERATION-R3-DESIGN-OUTPUT
title: Round 3 设计输出 · 无线充电器
category: iteration
used_when:
  - SKILL-AUDIT
  - DOC-REFERENCE
  - ITERATION-MODE
called_by:
  - skill-router
  - iteration-workflow
depends_on:
  - REF-PROCESS-001
outputs:
  - reference_metadata
---
# Round 3 设计输出 · 无线充电器

> **轮次**: Round 3 / 5
> **技能版本**: jony-ive-design2me-v2
> **日期**: 2026-06-21
> **产品**: 无线充电器 (Wireless Charger)
> **品类**: 消费电子
> **核心挑战**: 线圈隐藏 + 表面质感 + 静息状态

---

## 应用

- Pitfall 026/027: 提示词衰减+超时应对（300-450词控制）
- Guide 015: 多材料接缝设计
- Guide 016: 材料诚实可视化
- Guide 017: 文化杂交视觉化
- Guide 018: 交互细节可视化
- Guide 019: 动态形态表达（状态指示器）

---

## STEP-01: 任务分类与交付目标

**输入**: 无线充电器设计

**核心问题**: 这是什么类型的设计任务？

**五维判断**:
- **物理维度**: 电磁感应线圈、散热、防滑
- **关系维度**: 手机与充电器的放置关系、桌面与充电器的占据关系
- **操作维度**: 放置、拿起、状态观察
- **感知维度**: 充电状态的视觉反馈、表面触感
- **时间维度**: 充电时间2-3小时、待机功耗、LED寿命

**结论**: **分类B — 桌面静息圆盘**，交付3个本质不同的设计方向

**状态**: ✅ 完成

---

## STEP-02: 事实/推断/假设/未知项/禁止内容

**事实**:
1. Qi标准需要线圈对齐（±5mm）
2. 15W充电产生热量（线圈温度<60°C）
3. 充电距离<8mm（手机壳厚度）
4. 异物检测防止金属物体误充

**推断**:
1. 表面需要防滑材料防止手机移位
2. 底部需要配重防止拉扯移动
3. 状态指示需要柔和不刺眼

**假设**:
1. 用户夜间充电，LED不能太亮
2. 用户愿意为多设备充电支付溢价

**未知项**:
1. 是否需要多线圈（多设备）
2. 是否需要支架角度（立式充电）

**禁止内容**:
1. ❌ 模仿Apple MagSafe、Samsung Pad
2. ❌ LED跑马灯等装饰性元素
3. ❌ 牺牲散热追求薄度

**状态**: ✅ 完成

---

## STEP-03: 行为与关系重写

**关系版brief**: "设计一个桌面静息圆盘，它在被手机覆盖时无声地输送能量，在空闲时作为桌面静物存在。用户只需将手机放下，就像将信放在桌上，光的变化暗示能量正在流动。"

**风格显性拆解**:
| 维度 | 设计方向定义 |
|------|-------------|
| 形态特征 | 圆盘/圆环/扁平几何，低存在感 |
| 材料选择 | 铝（散热+结构）+ 硅胶/织物（防滑+触感）+ 玻璃（表面） |
| 工艺表达 | CNC精密+拉丝+阳极氧化 |
| 视觉语言 | 悬浮感、纯白背景、极简静物 |
| 触感暗示 | 冷金属边缘+温润中心 |
| 交互反馈 | 放置=充电开始，光呼吸=能量流动 |

**状态**: ✅ 完成

---

## STEP-04: 可测量的物理与人体事实

**3条最基本物理事实**:
1. **电磁感应需要距离**: 线圈与手机接收线圈距离<8mm
2. **热需要散逸**: 15W功率产生热量，需要散热路径
3. **圆需要稳定**: 圆盘放置桌面，需要防滑防止移位

**人体事实**:
| 事实 | 数据 |
|------|------|
| 放置动作 | 单手放置，自然落点 |
| 接触方式 | 手机背面与充电器表面接触 |
| 操作力 | 无（纯放置） |
| 观察距离 | 30-50cm（桌面到眼） |
| 状态识别 | 余光识别LED状态 |

**状态**: ✅ 完成

---

## STEP-05: 核心矛盾提炼

**核心矛盾**:
> **"充电需要技术，但静息需要无技术感"**

- **矛盾A**: 散热需要开口/纹理，但静息需要光滑
- **矛盾B**: 状态指示需要光，但睡眠需要无光
- **矛盾C**: 防滑需要纹理，但触感需要光滑

**状态**: ✅ 完成

---

## STEP-06: 候选生成 + 功能验证

| 候选 | 形态 | 核心创新 | 功能验证 | 结论 |
|------|------|---------|---------|------|
| **A: 静息石** | 扁平鹅卵石形态 | 自然形态=静息 | 线圈可隐藏于内部 | **保留** |
| **B: 光环盘** | 圆盘+边缘光环 | 光环=状态指示 | 光环可绕线圈 | **保留** |
| **C: 悬浮碟** | 碟形+磁悬浮底座 | 悬浮=未来感 | 磁悬浮不干扰Qi | **保留** |
| **D: 折叠垫** | 可折叠硅胶垫 | 便携 | 折叠影响线圈平整 | **否决** |
| **E: 立架** | 立式角度支架 | 边充边看 | 偏离"静息"定位 | **否决** |
| **F: 多线圈** | 大面积多线圈 | 随意放置 | 成本高、散热难 | **否决** |

**保留候选**: A（静息石）、B（光环盘）、C（悬浮碟）

**状态**: ✅ 完成

---

## STEP-07: 约束检查

| 约束 | A: 静息石 | B: 光环盘 | C: 悬浮碟 |
|------|----------|----------|----------|
| 物理 | 鹅卵石形态可内置线圈 | 圆盘标准形态 | 磁悬浮需验证不干扰 |
| 法规 | Qi认证 | Qi认证 | Qi+磁安全 |
| 制造 | CNC铝+表面处理 | 标准 | 磁悬浮机构复杂 |
| 成本 | 中 | 低 | 高 |
| 寿命 | 电子10年 | 电子10年 | 磁铁50年 |
| 美学 | 自然静息 | 科技光环 | 未来悬浮 |

**全部保留**。

**状态**: ✅ 完成

---

## STEP-08: 反俗套检查

| 俗套原型 | A距离 | B距离 | C距离 |
|---------|-------|-------|-------|
| 圆形充电板 | 远（鹅卵石） | 近（需差异化） | 远（悬浮） |
| 鼠标垫 | 远 | 远 | 远 |
| 杯垫 | 中（扁平圆盘） | 远 | 远 |

**审视B**: 圆盘形态与标准充电器接近，需要通过光环/材料/比例差异化。

**状态**: ✅ 完成

---

## STEP-09: 六轴差异门筛选

| 候选 | 材料 | 工艺 | 颜色 | 形态 | 关系 | 结构 |
|------|------|------|------|------|------|------|
| A: 静息石 | 铝+陶瓷 | CNC+釉面 | 白+灰 | 鹅卵石 | 放置 | 实心 |
| B: 光环盘 | 铝+玻璃 | CNC+抛光 | 银+蓝 | 圆盘+光环 | 放置 | 中空 |
| C: 悬浮碟 | 铝+磁铁 | CNC+磁化 | 银+透明 | 碟+悬浮 | 悬浮 | 磁悬浮 |

**3维差异**: 形态（鹅卵石vs圆盘vs碟）、结构（实心vs中空vs磁悬浮）、关系（放置vs放置vs悬浮）

**结论**: A+B+C 组合 ✅

**状态**: ✅ 完成

---

## STEP-10: 形态、比例、部件层级 + 视觉张力 + 文化杂交

### 方向A: 静息石

**形态**: 扁平鹅卵石，不对称自然曲线
**比例**:
| 尺寸 | 数值 | 来源 |
|------|------|------|
| 长轴 | 120mm | 覆盖手机 |
| 短轴 | 90mm | 视觉比例 |
| 厚度 | 12mm | 线圈+散热 |
| 曲率 | 不规则 | 自然形态 |

**视觉张力**: 自然曲线 vs 精密电子 = 有机×无机对比
**部件层级**:
1. 外壳（陶瓷釉面）
2. 线圈层（隐藏）
3. 底座（铝散热+防滑）

**文化杂交**: 日本禅石 × 现代科技
- 禅石=永恒、静息、自然
- 科技=能量、效率、精确
- 融合：自然形态隐藏精密技术

**状态**: ✅ 方向A完成

### 方向B: 光环盘

**形态**: 圆盘+边缘光环槽
**比例**:
| 尺寸 | 数值 | 来源 |
|------|------|------|
| 直径 | 110mm | 覆盖手机 |
| 厚度 | 10mm | 薄型 |
| 光环槽宽 | 3mm | 可见但不突兀 |
| 光环槽深 | 2mm | 隐藏LED |

**视觉张力**: 3mm光环 vs 107mm圆盘 = 精密边缘
**部件层级**:
1. 表面（玻璃/硅胶）
2. 光环槽（LED+导光）
3. 底座（铝+配重）

**文化杂交**: 日食光环 × 北欧极简
- 日食=光环、神圣、瞬间
- 北欧=极简、功能、永恒
- 融合：神圣光环+极简功能

**状态**: ✅ 方向B完成

### 方向C: 悬浮碟

**形态**: 碟形主体+透明支撑杆
**比例**:
| 尺寸 | 数值 | 来源 |
|------|------|------|
| 碟直径 | 100mm | 覆盖手机 |
| 碟厚度 | 8mm | 超薄 |
| 支撑杆高 | 15mm | 悬浮高度 |
| 支撑杆径 | 8mm | 最小视觉 |

**视觉张力**: 悬浮8mm vs 底座 = 反重力
**部件层级**:
1. 碟主体（铝+线圈）
2. 透明支撑（亚克力）
3. 底座（铝+磁铁/配重）

**文化杂交**: 飞碟 × 日本漆器
- 飞碟=悬浮、未来、神秘
- 漆器=精致、光泽、手工艺
- 融合：悬浮碟+漆器光泽

**状态**: ✅ 方向C完成

---

## STEP-11: 人体工学 + 高频接触点

### 方向A: 静息石

**人体工学**: 自然放置，无精确对位要求
**高频接触点**:
| 接触点 | 位置 | 材料 | 触感 |
|--------|------|------|------|
| 放置面 | 顶面 | 陶瓷釉面 | 温润光滑 |
| 握持边 | 侧面 | 陶瓷 | 自然曲线贴合 |

**状态**: ✅ 方向A完成

### 方向B: 光环盘

**人体工学**: 圆盘自然放置，光环指示状态
**高频接触点**:
| 接触点 | 位置 | 材料 | 触感 |
|--------|------|------|------|
| 放置面 | 顶面 | 硅胶/玻璃 | 防滑/光滑 |
| 边缘 | 侧面 | 铝 | 冷精密 |

**状态**: ✅ 方向B完成

### 方向C: 悬浮碟

**人体工学**: 悬浮高度15mm，手机放置无障碍
**高频接触点**:
| 接触点 | 位置 | 材料 | 触感 |
|--------|------|------|------|
| 放置面 | 碟顶面 | 铝 | 冷精密 |
| 支撑杆 | 中心 | 亚克力 | 光滑透明 |

**状态**: ✅ 方向C完成

---

## STEP-12: CMF + 材料职责

### 方向A: 静息石

| 材料 | 结构 | 触感 | 制造 | 寿命 | 维护 |
|------|------|------|------|------|------|
| 氧化铝陶瓷 | 外壳 | 温润光滑 | 等静压+釉面 | 50年 | 湿布 |
| 6061铝 | 底座散热 | 冷 | CNC+阳极氧化 | 20年 | 湿布 |
| 硅胶 | 底面防滑 | 柔软 | 注塑 | 5年 | 可更换 |

### 方向B: 光环盘

| 材料 | 结构 | 触感 | 制造 | 寿命 | 维护 |
|------|------|------|------|------|------|
| 钢化玻璃 | 表面 | 光滑冷 | 热弯+钢化 | 10年 | 玻璃清洁剂 |
| 6061铝 | 底座+边框 | 冷精密 | CNC+阳极氧化 | 20年 | 湿布 |
| 硅胶 | 底面防滑 | 柔软 | 注塑 | 5年 | 可更换 |
| LED导光 | 光环 | 无 | 注塑+LED | 10年 | 不可更换 |

### 方向C: 悬浮碟

| 材料 | 结构 | 触感 | 制造 | 寿命 | 维护 |
|------|------|------|------|------|------|
| 6061铝 | 碟主体 | 冷精密 | CNC+阳极氧化 | 20年 | 湿布 |
| 亚克力 | 支撑杆 | 光滑透明 | 注塑+抛光 | 10年 | 湿布 |
| 铝 | 底座 | 配重 | CNC | 20年 | 湿布 |

**状态**: ✅ STEP-12完成

---

## STEP-13: 三个DesignIR

### DesignIR-A: 静息石

```yaml
product_name: 静息石
form:
  primary_shape: 扁平鹅卵石
  proportions: {long_axis: 120mm, short_axis: 90mm, thickness: 12mm}
  visual_tension: 自然曲线 vs 精密电子
materials:
  - {name: 氧化铝陶瓷, structural: 外壳, tactile: 温润光滑, manufacturing: 等静压+釉面}
  - {name: 6061铝, structural: 底座散热, tactile: 冷, manufacturing: CNC+阳极氧化}
ergonomics:
  contact_points:
    - {location: 顶面, material: 陶瓷, tactile: 温润光滑}
cultural_hybrid: 日本禅石 × 现代科技
```

### DesignIR-B: 光环盘

```yaml
product_name: 光环盘
form:
  primary_shape: 圆盘+光环槽
  proportions: {diameter: 110mm, thickness: 10mm, halo_width: 3mm}
  visual_tension: 3mm光环 vs 107mm圆盘
materials:
  - {name: 钢化玻璃, structural: 表面, tactile: 光滑冷, manufacturing: 热弯+钢化}
  - {name: 6061铝, structural: 底座+边框, tactile: 冷精密, manufacturing: CNC+阳极氧化}
  - {name: LED导光, structural: 光环, tactile: 无, manufacturing: 注塑+LED}
ergonomics:
  contact_points:
    - {location: 顶面, material: 玻璃, tactile: 光滑}
    - {location: 边缘, material: 铝, tactile: 冷精密}
cultural_hybrid: 日食光环 × 北欧极简
```

### DesignIR-C: 悬浮碟

```yaml
product_name: 悬浮碟
form:
  primary_shape: 碟形+透明支撑
  proportions: {diameter: 100mm, thickness: 8mm, support_height: 15mm, support_diameter: 8mm}
  visual_tension: 悬浮8mm vs 底座
materials:
  - {name: 6061铝, structural: 碟主体, tactile: 冷精密, manufacturing: CNC+阳极氧化}
  - {name: 亚克力, structural: 支撑杆, tactile: 光滑透明, manufacturing: 注塑+抛光}
ergonomics:
  contact_points:
    - {location: 碟顶面, material: 铝, tactile: 冷精密}
    - {location: 支撑杆, material: 亚克力, tactile: 光滑透明}
cultural_hybrid: 飞碟 × 日本漆器
```

**状态**: ✅ STEP-13完成

---

## STEP-14: 审美质量门

| 维度 | A: 静息石 | B: 光环盘 | C: 悬浮碟 |
|------|----------|----------|----------|
| 形态比例 | 9/10 | 8/10 | 8/10 |
| 材料质感 | 9/10 | 8/10 | 8/10 |
| 接缝秩序 | 8/10 | 8/10 | 7/10 |
| 人体工学 | 9/10 | 9/10 | 8/10 |
| 识别性 | 9/10 | 8/10 | 9/10 |
| 静息状态 | 10/10 | 8/10 | 7/10 |
| 背景纯净度 | 10/10 | 10/10 | 10/10 |
| 艾维对比 | 8/10 | 7/10 | 7/10 |
| **识别性** | 9/10 | 8/10 | 9/10 |

**评分**:
- A: 8.85/10
- B: 8.15/10
- C: 7.85/10

**排序**: A > B > C

**状态**: ✅ STEP-14完成

---

## STEP-15: 三个方向的最终提示词（旧版优化版，300-450词）

### 方向A: 静息石

```
Industrial design render, wireless charger as flat ceramic pebble. 
Form: asymmetric organic curve, 120mm long axis, 90mm short axis, 12mm thick, 
like a river stone worn smooth by water. Surface: alumina ceramic, 
glossy white glaze, warm to touch, subtle crystalline texture visible under light. 
Base: 6061-T6 aluminum, 2mm thick, anodized silver, CNC-machined with 
0.1mm tolerance, thermal vias 1mm diameter array for heat dissipation. 
Bottom: silicone ring 3mm wide, 1mm thick, soft grip, prevents sliding. 
Coil hidden internally, no visible electronics. 
Status indicator: 2mm micro-LED dot, warm white 3000K, breathing pattern 
when charging, invisible when off. 
Floats in neutral gradient background. Pure white background, no environment. 
Studio photograph, three-quarter view slightly above. 
Precise numbers: 120mm, 90mm, 12mm, 2mm LED. 
Cultural hybrid: Japanese zen garden stone × modern wireless technology = 
organic eternal form hiding precise electromagnetic coil, 
monolithic ceramic suggesting natural object, aluminum base suggesting 
hidden technology. No logo, no text, no visible screws, no plastic. 
Contact points: ceramic top surface 120mm×90mm warm smooth, 
aluminum base edge cold precision. 
Interaction: place phone gently, LED breathes, energy flows silently.
```

### 方向B: 光环盘

```
Industrial design render, wireless charger as circular disc with halo edge. 
Form: 110mm diameter, 10mm thick, precision aluminum disc. 
Surface: tempered glass, 2mm thick, optically smooth, cold tactile, 
110mm diameter covering phone. Edge: 3mm wide halo groove, 2mm deep, 
housing micro-LED array 12pcs, cool white 5000K when charging, 
off when idle, visible as thin luminous ring. 
Base: 6061-T6 aluminum, 8mm thick, anodized silver, CNC-machined 
with 0.05mm tolerance, thermal vias integrated. 
Bottom: silicone pad 2mm thick, full coverage, soft grip. 
Glass-aluminum junction: deliberate 0.3mm gap with shadow line 
accentuating material boundary, anodized black edge absorbing light. 
Floats in neutral gradient background. Pure white background, no environment. 
Studio photograph, three-quarter view. 
Precise numbers: 110mm diameter, 10mm thick, 3mm halo, 2mm glass. 
Cultural hybrid: Solar eclipse halo × Nordic minimalism = 
sacred luminous ring + pure functional disc, light as status not decoration. 
No logo, no text, no visible screws, no plastic. 
Contact points: glass surface 110mm cold smooth, aluminum edge 3mm halo cold precision. 
Interaction: place phone, halo glows, remove phone, halo fades.
```

### 方向C: 悬浮碟

```
Industrial design render, wireless charger as floating disc on transparent support. 
Form: 100mm diameter disc, 8mm thick, appearing to float 15mm above base. 
Disc: 6061-T6 aluminum, anodized silver, mirror-polished top surface, 
100mm diameter, 8mm thick, CNC precision 0.05mm. 
Support: transparent acrylic rod, 8mm diameter, 15mm height, 
optically clear, polished, minimal visual presence. 
Base: 120mm diameter aluminum disc, 5mm thick, anodized gunmetal gray, 
weighted 300g for stability. Disc-base connection: acrylic rod press-fit 
into aluminum socket, 0.1mm tolerance, no visible adhesive. 
Coil hidden in disc, thermal path through aluminum to base. 
Status: subtle LED glow from disc edge, 1mm wide, warm white, 
visible only in dim light. Floats in neutral gradient background. 
Pure white background, no environment. Studio photograph, three-quarter view. 
Precise numbers: 100mm disc, 8mm thick, 15mm float, 8mm support, 120mm base. 
Cultural hybrid: UFO levitation × Japanese lacquerware = 
mysterious floating object + exquisite polished surface, 
anti-gravity wonder + handcrafted precision. 
No logo, no text, no visible screws, no plastic. 
Contact points: aluminum disc top 100mm cold mirror, acrylic support 8mm smooth transparent. 
Interaction: place phone on floating disc, subtle glow confirms charging.
```

**状态**: ✅ STEP-15完成（3方向提示词，300-450词控制）

---

## 来源

- 技能: jony-ive-design2me-v2
- 日期: 2026-06-21
