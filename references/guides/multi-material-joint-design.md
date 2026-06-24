---
reference_id: REF-GUIDE-015-02
title: 多材料接缝设计指南
category: guides
used_when:
  - MATERIAL-SELECTION
called_by:
  - end-to-end-workflow
  - pitfall-026
depends_on:
  - REF-GUIDE-001
  - REF-CASE-026
outputs:
  - joint_design_spec
---

# 多材料接缝设计指南 (Multi-Material Joint Design)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 1 智能桌面台灯迭代 — 接缝处理不足导致评审扣分

---

## 艾维接缝处理原则

乔纳森·艾维的设计中，多材料接缝只有两种处理方式：

1. **完全隐藏** — 用户不应感知到材料的变化
2. **故意强调** — 接缝本身就是设计元素

不存在"中间状态"。模糊的接缝 = 设计失败。

---

## 提示词中的接缝描述规范

### 类型1: 隐藏式接缝

**关键词替换**:

| ❌ 避免 | ✅ 使用 |
|--------|--------|
| seamless transition | monolithic construction, no visible joint line |
| smooth transition | material gradient transition over 5mm |
| blended | continuous surface, material change invisible to naked eye |

**完整描述模板**:
```
[材料A] and [材料B] form monolithic construction.
Material transition zone: [宽度]mm gradient, no visible joint line.
Surface continuity: [描述，如"aluminum grain continues into granite crystal pattern"].
Manufacturing: [工艺，如"CNC pocket in granite, aluminum arm press-fit with 0.01mm tolerance"].
```

**示例**（光之桥 arm-base 过渡）:
```
Aluminum arm and granite base form monolithic construction.
Material transition zone: 8mm gradient, aluminum surface gradually reveals granite crystal pattern.
No visible joint line; arm appears to grow from stone.
Manufacturing: CNC pocket in granite, aluminum arm press-fit with 0.01mm tolerance,
epoxy filled, surface ground flush, hand-polished to match granite finish.
```

### 类型2: 强调式接缝

**关键词**:

| 关键词 | 效果 |
|--------|------|
| deliberate 0.5mm gap | 精确间隙，阴影强调边界 |
| shadow line accentuates material boundary | 阴影成为设计元素 |
| contrasting material junction | 材料对比本身就是焦点 |
| precision-machined reveal | 机加工显露，制造精度展示 |

**完整描述模板**:
```
[材料A] and [材料B] meet at deliberate [宽度]mm gap.
Gap function: [功能，如"thermal expansion joint"或"visual accent"].
Gap treatment: [处理，如"anodized black to absorb light"或"polished to reflect"].
Shadow behavior: [阴影描述，如"gap casts 0.3mm shadow line at 45° light"].
```

**示例**（光之柱 shade-column 过渡）:
```
Aluminum column and acrylic shade meet at deliberate 0.3mm gap.
Gap function: visual accent + thermal expansion.
Gap treatment: aluminum edge anodized black to absorb light, acrylic edge polished.
Shadow behavior: gap casts precise shadow line, emphasizing 12mm column diameter.
```

---

## 常见材料对的接缝策略

| 材料A | 材料B | 推荐策略 | 关键描述 |
|-------|-------|---------|---------|
| 铝 | 花岗岩 | 隐藏 | "press-fit + epoxy, surface ground flush" |
| 铝 | 玻璃 | 强调 | "0.2mm rubber gasket, black anodized frame" |
| 铝 | 亚克力 | 强调 | "0.3mm gap, precision-machined reveal" |
| 铝 | 织物 | 隐藏 | "fabric wrapped + adhesive, edge tucked into 1mm groove" |
| 钢 | 木材 | 强调 | "0.5mm reveal, steel edge polished, wood edge waxed" |
| 陶瓷 | 金属 | 隐藏 | "metal insert molded into ceramic, surface continuous" |

---

## 提示词自检清单

在 STEP-15 生成提示词后，检查：

```
[ ] 每个材料过渡都有明确的接缝策略（隐藏或强调）
[ ] 隐藏式接缝有具体制造工艺描述
[ ] 强调式接缝有具体尺寸和阴影描述
[ ] 无"seamless""smooth""blended"等抽象词
[ ] 接缝处理与功能一致（如热膨胀缝≠装饰缝）
```

---

## 关联

- 相关 Pitfall: 026（提示词→图片衰减）
- 相关指南: material-honesty-visualization.md
- 相关案例: Round 1 光之桥（granite-aluminum 接缝扣分）

---

## 来源

- Round 1 实证: references/iterations/round-1/image-analysis.md
- 艾维设计原则: 知识库【设计师-知识蒸馏/乔纳森·艾维-知识蒸馏】
- 日期: 2026-06-21
