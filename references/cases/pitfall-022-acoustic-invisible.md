---
reference_id: REF-PITFALL-022
title: Pitfall 022 — 声学功能不可见
category: cases
used_when:
  - IMAGE-CRITIQUE
  - ACOUSTIC-DESIGN
called_by:
  - acoustic-visualization
depends_on:
  - REF-QUALITY-002
outputs:
  - pitfall_warning
---

# Pitfall 022 — 声学功能不可见

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 4 蓝牙音箱评审发现网罩、倒相孔、被动辐射器在图片中不够显性

---

## 现象

音频设备图片中，声学功能（扬声器网罩、倒相孔、被动辐射器）不可见或不够显性，导致产品看起来像"哑巴盒子"。

---

## 根因

1. 提示词仅使用功能描述（"acoustic mesh"），未转化为视觉元素
2. 模型对抽象声学概念理解有限，优先渲染形态
3. 网罩纹理过于细微，在1K分辨率下不可见

---

## 解决

使用声学功能视觉化公式：

```
[声学功能] = [视觉元素] + [材料暗示] + [结构暗示]
```

### 示例

```
❌ "acoustic mesh top"
✅ "micro-perforated aluminum mesh, 0.5mm precision holes, 
    etched pattern visible, acoustic transparency implied"
```

---

## 检查清单

- [ ] 网罩是否有具体孔径描述？
- [ ] 被动辐射器是否有视觉焦点？
- [ ] 倒相孔是否有结构暗示？
- [ ] 声学功能是否可辨识？

---

## 来源

- Round 4 蓝牙音箱评审
- REF-GUIDE-019: 声学功能视觉化指南
