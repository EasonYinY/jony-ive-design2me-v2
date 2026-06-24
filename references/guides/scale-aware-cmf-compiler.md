---
reference_id: REF-GUIDE-SCALE-CMF
title: 尺度自适应 CMF 与摄影编译算法
category: guides
used_when:
  - STEP-15
  - PROMPT-COMPILATION
  - CMF-SELECTION
called_by:
  - prompt-engineering
  - end-to-end-workflow
depends_on:
  - REF-GUIDE-008
  - REF-PROCESS-001
outputs:
  - scale_aware_cmf
  - photographic_compiler
---

# 尺度自适应 CMF 与摄影编译算法（Scale-Aware CMF & Photographic Compiler）

> **版本**: 1.0
> **日期**: 2026-06-25
> **触发**: 用户审计报告（系统级重构审计）—— 微观材质词导致模型反向压缩产品主体比例

---

## 概述

系统必须根据 Brief 输入的产品物理外形尺寸（定义大、中、小三档物理尺度），动态调用完全不同阶数的 CMF 语料与摄影透视控制语料。防止微观桌面级材质词导致模型反向压缩产品主体比例，造成"手办感"或"首饰感"。

---

## 三档物理尺度定义

| 档位 | 尺寸范围 | 典型品类 | 摄影语料 | CMF 语料 |
|------|---------|---------|---------|---------|
| **小型** | < 30cm | 鼠标、耳机、手表、咖啡机 | `Studio photograph, three-quarter view, macro detail shot` | 桌面级材质：`walnut`, `travertine`, `obsidian`, `brushed brass` |
| **中型** | 30cm - 1.5m | 显示器、打印机、医疗推车 | `Studio photograph, three-quarter view, medium shot` | 设备级材质：`bead-blasted aluminum`, `matte composite`, `tempered glass` |
| **大型** | > 1.5m | MRI、CT、无人机、汽车 | `Architectural-grade studio composition, medium-long shot with orthogonal precision, grand volumetric presence` | 建筑级/工业级材质：`monolithic architectonic enclosures`, `precision bead-blasted performance alloys`, `structural architectural basalt anchors` |

---

## 大型设备（> 1.5m）编译规则

### 禁止词

严禁使用任何带有微观桌面摆件、手办、首饰倾向的材质描述：

- ❌ `travertine base`
- ❌ `small obsidian slab`
- ❌ `micro hairline slit`
- ❌ `walnut accent`
- ❌ `marble inlay`
- ❌ `pocket-sized`
- ❌ `miniature`
- ❌ `tiny`

### 替代材料职责语料

```
Monolithic architectonic enclosures
Precision bead-blasted performance alloys
Structural architectural basalt anchors
High-grade acoustic dampening composite panels
Pristine medical-grade non-porous ceramic matrices
Cryogenic hardened steel alloys
High-density solid surface mineral polymer
```

### 摄影语料升阶

```
Architectural-grade studio composition
Medium-long shot with orthogonal precision
Grand volumetric presence
Cinematic subtle diffuse environmental light
Soft volumetric wrapping highlights revealing the monumental scale
Monumental scale industrial product photography
```

---

## 中型设备（30cm - 1.5m）编译规则

### 摄影语料

```
Studio photograph, three-quarter view, medium shot
Balanced environmental lighting
Clear volumetric definition
Professional product photography
```

### CMF 语料

```
Bead-blasted aluminum
Matte engineering composite
Tempered glass panel
Precision-machined stainless steel accent
Soft-touch silicone
Brushed titanium
```

---

## 小型设备（< 30cm）编译规则

### 摄影语料

```
Studio photograph, three-quarter view, macro detail shot
Intimate lighting revealing micro-textures
Shallow depth of field
Close-up product photography
```

### CMF 语料

```
Walnut
Travertine
Obsidian
Brushed brass
Micro hairline slit
Hand-polished resin
Leather accent
```

---

## 自动化尺度判定流程

```
STEP-1: 读取 Brief 物理尺寸（长×宽×高）
STEP-2: 取最大维度作为尺度判定依据
STEP-3: 判定档位：
  IF max_dimension < 30cm → 小型档
  IF 30cm <= max_dimension <= 1.5m → 中型档
  IF max_dimension > 1.5m → 大型档
STEP-4: 根据档位调用对应摄影语料库和 CMF 语料库
STEP-5: 在提示词编译时强制替换禁用词
STEP-6: 运行防御性决策树（方法29）验证
```

---

## 尺度-材质-摄影联动匹配表

| 产品 | 尺寸 | 档位 | 摄影语料 | 主材质 | 辅助材质 |
|------|------|------|---------|--------|----------|
| 无线鼠标 | 12cm | 小型 | Studio photograph, macro detail shot | Walnut | Brushed brass |
| 咖啡机 | 35cm | 中型 | Studio photograph, medium shot | Bead-blasted aluminum | Tempered glass |
| MRI 扫描仪 | 250cm | 大型 | Architectural-grade studio composition | Medical-grade ceramic | Performance alloys |
| 无人机 | 80cm | 中型 | Studio photograph, medium shot | Carbon fiber composite | Precision-machined titanium |
| 纯电汽车 | 480cm | 大型 | Architectural-grade studio composition | Structural aluminum | Acoustic composite panels |

---

## 与五段式权重重组的关系

| 五段式层级 | 尺度自适应应用 |
|-----------|--------------|
| Layer A (20%) | 直接调用对应档位的摄影语料 |
| Layer B (30%) | 不可缩减特征尺寸需与档位匹配 |
| Layer C (15%) | 微观细节密度与档位反比（大型设备细节更稀疏） |
| Layer D (20%) | 直接调用对应档位的 CMF 语料 |
| Layer E (15%) | 光影强度与档位正比（大型设备需要更强烈的光影定义） |

---

## 来源

- 审计报告：2026-06-25 系统级重构审计（尺度自适应 CMF 与摄影编译算法）
- 核心病灶：微观材质词导致模型反向压缩产品主体比例
- 根因分析：缺乏尺度-材质-摄影的联动匹配机制
- 升级触发：用户审计报告"尺度自适应 CMF 与摄影编译算法"
