---
reference_id: REF-CASE-026-B
title: Pitfall 026-B - Flying vehicle prompt anti-patterns in Nano Banana Pro
category: cases
supersedes_id_was: REF-CASE-026
disambiguation_note: 原 REF-CASE-026 与 pitfall-026-prompt-to-image-attenuation.md / pitfall-026-flat-design-no-functional-zoning.md 三重冲突,本文件分配 -B 后缀。官方权威 REF-CASE-026 = 提示词→图片衰减(由 README.md 登记)。
used_when:
  - PROMPT-COMPILATION
  - FLYING-VEHICLE
  - VTOL
  - AERIAL-MOBILITY
called_by:
  - prompt-contract
  - image-critique
  - quality-gates
depends_on:
  - REF-PROMPT-002
  - REF-PROMPT-005
  - references/guides/prompt-engineering.md
outputs:
  - prompt_recipe
  - failure_pattern
---

# Pitfall 026: 飞行载人器具品类的提示词反模式(Nano Banana Pro 实证)

> **版本**: 1.0
> **日期**: 2026-06-23
> **触发**: 下一代 1 人 VTOL 飞行载人器具 3 张图任务中,D1 触发 Nano Banana Pro 的"飞行器品类默认联想"——把 DesignIR 明确要求的"双环围绕等大弦月舱"压缩为"装饰性小弦月舱 + 工业风车"
> **严重级别**: HIGH for `form_first_collapse` / `proportion_violation` / `identity_loss`
> **前置**: pitfall-025(咖啡机)同构,本 pitfall 是其在飞行器品类的扩展

## 现象

即便提示词已包含完整 DesignIR(`crescent cabin 2400mm long x 1100mm wide x 950mm high` + `two rings 2400mm diameter` + 显式比例标注),Nano Banana Pro 仍触发以下品类默认联想:

| 触发场景 | 模型主动行为 | 失败码 | 实证 |
|---|---|---|---|
| D1 双环 + 等大弦月舱 | 弦月舱被严重压缩成小装饰件,实际渲染舱体长度远小于 2400mm 环径 | `proportion_violation` + `identity_loss` | flying-vehicle-r1-d1/lovart_4570cbd9b124.png |
| D1 16 片变距扇叶 | 环内扇叶被渲染为复古风车/工业吊扇形态,叶片数变密,失去"飞行器升力系统"识别 | `form_first_collapse` | flying-vehicle-r1-d1/lovart_4570cbd9b124.png |
| D2 张力场环 + 椭球舱(虚构) | ✅ 渲染表现优秀,识别度+材料语言均到位 | (no trigger) | flying-vehicle-r1-d2/lovart_6dd2bbb280f1.png |
| D5 上下双碳环 + 张力线 | ✅ 渲染表现优秀,凯夫拉编织线 + G2 节点 + OLED 触屏全部呈现 | (no trigger) | flying-vehicle-r1-d5/lovart_9b9d31987a76.png |

**关键观察**: 3 个方向中,只有 D1(双环围绕主体舱)触发反模式,D2(虚构力场环在舱下方)/D5(双环通过张力线悬吊舱)均未触发。**结构对位是根因**——Nano Banana Pro 不擅长"两个等大主体互为主从"的对位几何。

## 根因分析

1. **Nano Banana Pro 对"双环围绕主体"的几何对位有强默认**: 当提示词含 `two rings + central cabin` 结构时,模型倾向把"rings"作为主体框架、`cabin` 作为被包覆的内部小元素,忽略 `crescent cabin 2400mm = rings 2400mm` 的等大关系
2. **环内扇叶的默认形态**: 16 片变距扇叶被读为"风车/吊扇"原型,失去"飞行器升力系统"的工业语言
3. **复合比例表述衰减**: 即便写 `cabin 2400mm x 1100mm x 950mm`,模型对 `2400mm vs 2400mm` 等大关系的保持能力弱
4. **D2/D5 不触发的反向证据**: D2 的"场环在舱体下方"是垂直分离几何,D5 的"双环通过张力线悬吊舱"是几何连接 + 力学悬吊,均不触发"对位压缩"

## 修复方法(Round 2 推荐 prompt 模板)

### 模板 A:等大双环围绕主体类(D1 类)

在结构描述中**强化主体身份 + 反向锚定**:

```text
# 原版(弱):
"Two rings front/rear, 2400mm diameter, central crescent cabin
2400mm long x 1100mm wide x 950mm high"

# Round 2 强化版(强):
"The crescent cabin is the PRIMARY subject with EQUAL 2400mm dimension
to the rings — NOT smaller, NOT a decorative element between the rings.
Crescent cabin 2400mm long x 1100mm wide x 950mm high is the
PASSENGER COCKPIT, not a window or accent piece.
The two rings (2400mm diameter each) are LIFT SYSTEMS that
surround and support the cabin — they are NOT the main body.
COMPOSITION: cabin occupies ~40% of frame, rings occupy ~30% each."
```

**关键修复点**:
1. 显式声明 "PRIMARY subject"
2. 显式否定 "NOT smaller, NOT a decorative element"
3. 角色反转:"rings are LIFT SYSTEMS that surround the cabin" 而非"cabin between rings"
4. 显式 COMPOSITION 比例(40% / 30% / 30%)防止模型自动压缩

### 模板 B:环内扇叶类(风扇/吊扇反模式)

针对 16 片变距扇叶的"风车"反模式,补强工艺语言:

```text
# 在扇叶描述中加否定锚定:
"16 variable-pitch forged titanium blades, INDUSTRIAL LIFT FAN
geometry — NOT a windmill, NOT a ceiling fan, NOT a turbine
propeller, NOT a steampunk rotor.
Blades have AERODYNAMIC sweep with 15-degree pitch variation,
hairline metal finish, machined leading edge."
```

**关键修复点**:
1. 显式列出反模式原型(`windmill / ceiling fan / turbine / steampunk`)
2. 补强工艺细节(`15-degree pitch variation / hairline metal finish / machined leading edge`)
3. 用"INDUSTRIAL LIFT FAN"作为正面锚定

### 模板 C:对位几何失效预防(通用)

**Lovart 通用反比例衰减规则**(适用任何 `A + B + C` 复合几何):

```text
# 在结构描述后追加:
"GEOMETRIC HIERARCHY:
- [A] is the [role 1], [dimension 1] — OCCUPIES [X]% OF FRAME
- [B] is the [role 2], [dimension 2] — OCCUPIES [Y]% OF FRAME
- [C] is the [role 3], [dimension 3] — OCCUPIES [Z]% OF FRAME
Do NOT auto-shrink or auto-enlarge any element."
```

## 关键经验:身份反转语言(Inverted Identity Language)

D1 失败的根因是 Nano Banana Pro 用了错误的"主体/装饰"分配。Round 2 提示词需要**显式反转这种分配**,通过:

| 写法 | 效果 |
|---|---|
| ❌ "two rings with central cabin" | 模型读为"rings 是主体,cabin 是中心点缀" |
| ✅ "crescent cabin (PRIMARY) with two supporting lift rings" | 模型读为"cabin 是主体,rings 是支撑" |
| ❌ "blades inside the ring" | 模型读为"风车叶片" |
| ✅ "INDUSTRIAL LIFT FAN blades — NOT a windmill" | 模型读为"工业升力风扇" |

## 验证方式

每张图生成后 vision_analyze 问 4 个 yes/no:

- Q1: 主体舱体是否被严重压缩(目测 < 环直径 50%)?(是 = 触发 D1 反模式)
- Q2: 环内扇叶是否呈现"风车/吊扇/复古"形态?(是 = 触发扇叶反模式)
- Q3: 核心识别特征(如 D1 的"等大双环围绕弦月舱")是否视觉可识别?(否 = 触发 `identity_loss`)
- Q4: COMPOSITION 比例是否平衡(主体 30-50% 画面占比)?

任一为"是/否触发" → 退回编译,应用本 pitfall 修复模板。

## 与其他 Pitfall 关系

- **Pitfall 025(咖啡机)**: 同构 pitfall。025 是家电品类反模式,026 是飞行器品类反模式。两者共享"interior state clause" + "INVERTED IDENTITY"修复策略
- **Pitfall 024(Lovart 静默成功)**: 独立。本 pitfall 是渲染成功但内容偏差,024 是渲染超时但实际成功
- **Pitfall 016(背景侵入)**: 互补。016 关注外部场景,026 关注内部几何对位
- **REF-QUALITY-003 `form_first_collapse`**: 026 的 D1 是该码的具体子类型
- **REF-QUALITY-003 `proportion_violation`**: 026 是该码的首个独立 pitfall 案例

## 来源

- 2026-06-23 下一代 1 人 VTOL 飞行载人器具 3 张图实证
  - D1 触发(弦月舱被压小 + 扇叶变风车),得分 60/80
  - D2 未触发(虚构场环+琥珀 LED 渲染优秀),得分 71/80
  - D5 未触发(双环+张力线+OLED 渲染优秀),得分 71/80
- 与 Pitfall 025 同日触发,证实 Nano Banana Pro 对"主体-包覆"复合几何存在系统性弱点
- 修复策略"INVERTED IDENTITY LANGUAGE"经 D5 渲染结果反向验证(上环 2800mm vs 下环 1800mm 1.55:1 主从比例精确呈现)
