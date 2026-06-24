---
reference_id: PITFALL-058
title: 品类动态排除词缺失（Category Dynamic Exclusion Missing）
category: cases
used_when:
  - STEP-08
  - STEP-15
called_by:
  - end-to-end-workflow.md
  - prompt-engineering.md
depends_on:
  - REF-PROCESS-001
outputs:
  - exclusion_list
---

# Pitfall 058: Category Dynamic Exclusion Missing

## 触发条件

绝对排除词（Negative Filter）为静态列表，未与 brief 品类绑定，导致品类特定陈词滥调（如飞行器的 sci-fi wings、透明穹顶）进入提示词。

## 现象

- 五段式协议 Block 5 使用通用排除项：`No logo, no text, no visible screws`
- 但飞行器品类特有的污染词未自动排除：`sci-fi wings, glowing thrusters, aerodynamic decals, transparent dome, cybernetic rings`
- 模型生成结果出现科幻陈词滥调

## 根因

1. 禁止词滤网为静态全局列表
2. 未根据 brief 品类动态扩展排除项
3. 品类特定污染词未被识别

## 解决方案

在 STEP-08 注入品类动态排除词：

| 品类 | 动态排除词 |
|------|-----------|
| 飞行器 | `sci-fi wings, glowing thrusters, aerodynamic decals, transparent dome, cybernetic rings, UFO silhouette` |
| 消费电子 | `glossy plastic, LED strips, decorative grooves, tech-grid pattern, circuit board aesthetic` |
| 家具 | `rustic texture, farmhouse style, ornate carving, vintage distressing` |
| 穿戴设备 | `sporty silicone, fitness tracker aesthetic, neon accents, rubberized coating` |
| 医疗设备 | `clinical white, hospital aesthetic, sterile plastic, institutional look, warning labels, visible tubing, adjustment knobs, medical cross symbols, blue accent strips` |
| 大型医疗设备（MRI/CT/放疗） | `clinical white, hospital aesthetic, sterile plastic, institutional look, warning labels, visible tubing, adjustment knobs, medical cross symbols, blue accent strips, glossy plastic shell, exposed cabling, industrial grating, dangling cables, fluorescent tube lighting, beige plastic panels, rubber bumpers, caution tape yellow` |

## 检查清单

- [ ] brief 品类已识别？
- [ ] 品类特定排除词已自动写入 Block 5？
- [ ] 排除词是否覆盖该品类最常见的 5-7 个陈词滥调？
- [ ] 最终提示词中无品类特定污染词？
