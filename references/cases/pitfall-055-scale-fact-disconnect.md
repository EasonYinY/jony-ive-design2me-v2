---
reference_id: PITFALL-055
title: 尺度与物理事实的"名实分离"（Scale-Fact Disconnect）
category: cases
used_when:
  - STEP-04
  - STEP-10
called_by:
  - end-to-end-workflow.md (STEP-04.5)
  - prompt-engineering.md
depends_on:
  - REF-PROCESS-001
outputs:
  - spatial_validation_result
---

# Pitfall 055: Scale-Fact Disconnect

## 触发条件

STEP-04 严谨收集了人体测量学数据，但 STEP-10 形态推导时这些数据未作为硬性数学边界约束布局，导致推导出的物理尺寸在工程上失效。

## 现象

- STEP-04 输出坐姿眼高 92.5cm、大腿长 52.0cm、半躺姿 20-30°
- STEP-10 产出飞行器尺寸 2.2m × 1.8m × 1.0m，声称容纳 2 人
- 工程证伪：半躺姿 20-30° 下，单人人体包络纵向投影已达 1.4-1.6m，加上推进器间距、碰撞缓冲区、电池盒体积，2.2m 总长甚至无法合法容纳单人

## 根因

1. 缺乏"尺度校验锚（Dimension Anchor Lock）"
2. 形态生成与物理事实之间没有硬校验公式
3. AI 为满足"注入精确数字"的硬约束，编造未经结构依据的绝对综合尺寸

## 解决方案

在 STEP-04 尾部强制增加【空间包络硬验证（Spatial Package Validation Matrix）】：

```
V_min = ΣV_human × 2.5 + V_powertrain + V_clearance
```

形态生成的任何尺寸必须通过此公式的逻辑硬校验，禁止产生逻辑断层。

## 检查清单

- [ ] 每个核心尺寸拆解为 `[净尺寸 + 结构厚度 + 安全边界 = 最终尺寸]`？
- [ ] 载具类公差是否在 ±10% 内？
- [ ] 电子设备公差是否在 ±0.5mm 内？
- [ ] 未通过校验的尺寸是否标注 `UNVALIDATED`？
