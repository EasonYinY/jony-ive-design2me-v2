---
reference_id: REF-GUIDE-005
title: 提示词接缝精度强化指南
category: guides
used_when:
  - PROMPT-COMPILATION
called_by:
  - prompt-contract
  - image-critique
depends_on:
  - REF-PROMPT-001
  - REF-PROMPT-002
outputs:
  - prompt_seam_precision_guidelines
---

# 提示词接缝精度强化指南

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 2 发现接缝秩序评分偏低（7/10）

---

## 接缝精度关键词

### 通用接缝精度关键词

| 关键词 | 效果 | 适用场景 |
|--------|------|---------|
| precision fit | 精密配合 | 通用 |
| tight tolerance | 紧密公差 | 高精度 |
| seamless joint | 无缝连接 | 外观要求高 |
| micro-gap | 微间隙 | 精密机械 |
| flush surface | 齐平表面 | 外观要求高 |

### 特定接缝类型关键词

| 接缝类型 | 关键词 | 效果 |
|---------|--------|------|
| 螺纹 | precision thread, tight pitch | 螺纹精密 |
| 铰链 | precision hinge, tight pivot | 铰链精密 |
| 磁吸 | precision magnetic fit | 磁吸精密 |
| 卡扣 | precision snap fit | 卡扣精密 |
| 焊接 | seamless weld, flush joint | 焊接无缝 |

---

## 提示词模板

```
[产品描述], precision fit between [部件A] and [部件B], 
tight tolerance [数值]mm, seamless joint, flush surface,
[材料描述], pure white background, product photography
```

---

## 应用示例

### 折叠臂台灯
```
...precision hinge joint, tight pivot tolerance 0.1mm, 
seamless connection between arm and head...
```

### 螺旋升降台灯
```
...precision thread fit, tight pitch tolerance 0.05mm, 
seamless connection between column and head...
```

---

## 验证方式

- 图片中接缝是否精密
- 接缝是否无缝
- 表面是否齐平

---

## 来源

- Round 2 实证: 接缝秩序评分7/10，需提升
- REF-PROMPT-001: 提示词合同
