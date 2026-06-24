---
reference_id: REF-CASE-028
title: Pitfall 028 — 自然形态表达不稳定
category: cases
used_when:
  - NATURAL-FORM-DESIGN
called_by:
  - end-to-end-workflow
  - prompt-engineering-guide
depends_on:
  - REF-GUIDE-001
outputs:
  - natural_form_warning
---

# Pitfall 028 — 自然形态表达不稳定 (Natural Form Instability)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 3 无线充电器迭代 — 鹅卵石形态有时被AI理解为"不规则石头"
> **严重程度**: 🟢 低

---

## 现象

提示词描述"扁平鹅卵石""自然曲线"时，AI有时生成：
- 过于随机的"石头"，缺乏设计感
- 过于规则的"椭圆"，失去自然感
- 材质错误（花岗岩而非陶瓷）

Round 3 方向A（静息石）成功，但自然形态的稳定性需要关注。

---

## 根因分析

### 根因1: AI对"自然"的理解偏向随机

AI将"natural"理解为"random/irregular"，而非"controlled organic"。

### 根因2: 缺乏"设计自然"的语义

提示词中缺少"designed""controlled""precision"等词修饰"natural"。

### 根因3: 材质描述不够精确

"鹅卵石"可能触发"river rock"（花岗岩）而非"ceramic pebble"（陶瓷）。

---

## 解决方案

### 策略1: 强调"受控的自然"

| ❌ 避免 | ✅ 使用 |
|--------|--------|
| natural stone | precision-crafted ceramic with organic form |
| irregular shape | controlled asymmetry, designed organic curve |
| random texture | hand-finished surface, intentional variation |
| pebble | ceramic sculpture, pebble-inspired |

### 策略2: 材质前置

将材质放在形态之前，避免AI先理解形态再选材质：

```
✅ "alumina ceramic pebble" — 材质明确
❌ "pebble made of ceramic" — 形态先触发
```

### 策略3: 添加"设计"修饰词

```
✅ "designer pebble" "sculptural form" "artisan-crafted"
✅ "precision organic" "controlled natural"
```

---

## 验证方法

```
[ ] 自然形态前有"designed""controlled""precision"修饰
[ ] 材质放在形态之前描述
[ ] 有"sculptural""artisan"等设计词
[ ] 无"random""irregular"等失控词
```

---

## 关联

- 相关案例: Round 3 静息石（成功但需稳定性）
- 日期: 2026-06-21
