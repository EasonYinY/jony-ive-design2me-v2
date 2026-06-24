---
reference_id: PITFALL-061
title: 品牌语境与物理原型词混用（Brand Context & Physical Archetype Mixing）
category: cases
used_when:
  - STEP-15
  - PROMPT-COMPILATION
called_by:
  - end-to-end-workflow.md (STEP-15.5 阶段一 + 阶段四)
  - step-reference-map.md (STEP-15)
  - prompt-engineering.md 方法23
depends_on:
  - REF-GUIDE-008
  - PITFALL-060
outputs:
  - brand_context_separation_report
---

# Pitfall 061: Brand Context & Physical Archetype Mixing

## 触发条件

在提示词阶段一（功能原型与轴向）中混入品牌语境词（如 "LoveFrom 2030"），导致 Lovart 文本编码器将品牌词具象化为印刷字符/Logo，污染生成图像。

## 现象

- 提示词："Studio photograph of a manned flight vessel, LoveFrom 2030..."
- 生成结果：机身上出现 "LoveFrom" 或 "2030" 的印刷文字/Logo
- 根因：Lovart 文本编码器对具体品牌词高度敏感，易将其具象化为可见字符

## 修复方案

### 物理原型词（阶段一）

**只描述物理功能原型**，绝不包含品牌/年份/设计师名字：

```
✅ "Studio photograph of a manned aerodynamic flight vessel, featuring a prominent panoramic water-drop glass cockpit..."
❌ "Studio photograph of a manned flight vessel, LoveFrom 2030..."
```

### 品牌语境（阶段四）

**移至阶段四**，用抽象谱系描述替代具体品牌词：

```
✅ "reflecting the pure minimalist design lineage of Jony Ive's aesthetic philosophy, strictly debranded, absolute zero alphanumeric text"
❌ "LoveFrom 2030, post-Apple Jony Ive"
```

## 检查清单

- [ ] 阶段一提示词中无 "LoveFrom"/"Apple"/年份数字/设计师名字？
- [ ] 阶段一只有物理功能原型词（manned flight vessel / espresso machine）？
- [ ] 品牌语境已移至阶段四？
- [ ] 阶段四使用 "design lineage" + "strictly debranded" 替代具体品牌？

## 相关参考

- `references/guides/prompt-engineering.md` 方法23（五维工业级提示词架构）
- `references/cases/pitfall-060-debranding-and-legibility.md`（反纯粹抽象质量门）
