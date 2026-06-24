---
reference_id: REF-DESIGN-003
title: CMF 系统
category: design
used_when:
  - STEP-09
  - STEP-12
  - STEP-14
  - STEP-15
called_by:
  - product-design
  - prompt-rewriting
  - image-critique
depends_on:
  - REF-EVIDENCE-001
  - REF-DESIGN-001
outputs:
  - cmf_system
---

# CMF 系统

每个方向在单一 `cmf_system` 中记录主材、辅材、颜色、成形与表面工艺、触感、清洁方式、老化路径和回收后果，并与 `materials`、`manufacturing` 和 `maintenance` 三个字段互相一致。材料必须承担结构、接触、密封、导热、耐磨或维护职责；不得只写“高级金属”或用灰黑配色替代方向差异。

三方向不得共享同一主材、主色和表面工艺组合。颜色必须给出明确范围或稳定物理参照，避免抽象形容词导致生成偏差。

## 旧版 感官材料优先（新增）

### 工程材料 vs 感官材料

| 工程材料（❌） | 感官材料（✅） | 说明 |
|---------------|---------------|------|
| "titanium alloy TC4" | "hairline-brushed titanium" | 删除工程前缀，添加表面处理 |
| "stainless steel 316L" | "polished steel" / "brushed steel" | 删除牌号，保留表面处理 |
| "polycarbonate PC" | "smoked glass" / "translucent amber" | 用感官描述替代材料学名 |
| "aluminum 6061" | "anodized aluminum" | 保留表面处理，删除牌号 |
| "carbon fiber reinforced polymer" | "matte carbon" / "carbon ring" | 简化材料名，添加形态 |

### 材料描述转换规则

1. **删除工程前缀**：alloy/grade/316L/6061/TC4/reinforced/polymer
2. **保留表面处理**：hairline-brushed/polished/matte/smoked/anodized
3. **添加形态词**：slab/dome/ring/shell/cylinder/bell
4. **添加空间关系**：suspended over/linked by/rests on/flush in
5. **检查感官可感知性**：材料名是否能在图片中被识别？

### 示例转换

```
❌ 工程材料："Titanium alloy TC4 disc body, 65mm diameter, 28mm thick"
✅ 感官材料："Hairline-brushed titanium disc, 65mm diameter, 28mm thick, micro-blasted dark space gray"

❌ 工程材料："Stainless steel 316L etched foil mesh"
✅ 感官材料："Polished steel foil mesh, micro-etched"

❌ 工程材料："Translucent amber PC elliptical handle"
✅ 感官材料："Smoked amber glass handle, high-gloss showing internal structure"
```

### 材料职责格式

材料描述必须使用"材料职责"格式，但**材料名称必须使用感官材料**：

```
材料名称（感官） | 结构职责 | 触感职责 | 制造方式 | 寿命 | 维护方式

例：
"hairline-brushed titanium" | 主机身壳体，承力+散热 | 微凉、发丝纹理 | CNC五轴加工 | 10年+ | 湿布擦拭
"polished steel" | 刀网，切割+皮肤接触 | 微凉、光滑 | 微蚀刻+电抛光 | 18个月 | 更换
"smoked amber glass" | 手柄壳体 | 温润、半透明 | 注塑成型 | 5年 | 湿布擦拭
```
