---
reference_id: REF-GUIDE-015
title: 方法15 - 功能暗示法
category: guides
used_when:
  - PROMPT-COMPILATION
  - STEP-15
called_by:
  - prompt-contract
  - prompt-compression
  - prompt-trace
depends_on:
  - REF-PROMPT-001
  - REF-PROMPT-002
  - REF-PROMPT-004
  - REF-DESIGN-001
outputs:
  - prompt_engineering_method
---

# 方法15: 功能暗示法

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 用户反馈"功能性的按键、功能性的操作的交互功能的描述，一定要细节细腻"
> **适用范围**: 所有需要保留功能性操作暗示的消费电子产品

---

## 原理

AI图像生成模型无法渲染"功能"（按压反馈、旋转阻尼、触控响应），但可以渲染"形态"（凸起、凹陷、线条、纹理）。**用形态暗示功能，不用功能描述形态**。

## 核心规则

1. **删除所有功能描述**：rotary knob / slide switch / press button / touch zone
2. **保留形态暗示**：flush circular depression / slight raised line / small rectangular recess
3. **限制数量**：每个产品最多2-3个功能暗示
4. **用材料/纹理强化暗示**：brass ring around depression / matte texture on line

## 功能暗示对照表

| 功能元素 | ❌ 删除（功能描述） | ✅ 保留（形态暗示） |
|----------|---------------------|---------------------|
| 旋钮 | rotary knob with detents | flush circular depression, subtle texture |
| 开关 | slide switch, toggle | slight raised line, matte finish |
| 按键 | press button, tactile feedback | small rectangular recess, flush surface |
| 接口 | USB-C port, charging hole | small rectangular recess, no visible pins |
| 滚轮 | scroll wheel, rubber grip | cylindrical groove, hairline texture |
| 显示屏 | OLED display, touch screen | black rectangular plane, glossy surface |
| 扬声器 | speaker grille, audio driver | perforated circular area, fabric texture |
| 指示灯 | LED indicator, status light | small circular dot, warm glow |
| 摄像头 | camera lens, sensor array | small circular depression, glass surface |
| 天线 | antenna line, signal strip | thin metallic line, hairline finish |

## 产品类型功能暗示示例

**鼠标**:
```
❌ "Left click button, right click button, scroll wheel, DPI switch"
✅ "No buttons visible, flush surface, slight cylindrical groove"
```

**咖啡机**:
```
❌ "Brew button, steam knob, cup warmer, water level indicator"
✅ "Small circular depression, brass ring, slight rectangular recess"
```

**耳机**:
```
❌ "Volume rocker, play/pause button, noise cancel switch, charging port"
✅ "Slight raised line, small circular dot, thin rectangular recess"
```

**手机**:
```
❌ "Power button, volume buttons, camera lens, charging port"
✅ "Thin metallic line, small circular depression, flush rectangular recess"
```

**灯具**:
```
❌ "Dimmer switch, color temperature button, power cord, hanging chain"
✅ "Small circular depression, thin power line, subtle mounting point"
```

## 检查清单

- [ ] 删除所有功能描述（rotary/slide/press/touch/scroll）？
- [ ] 用形态暗示替代（flush depression/raised line/recess/groove）？
- [ ] 功能暗示 ≤ 3 个？
- [ ] 用材料/纹理强化暗示？
- [ ] 不描述动态/使用状态？

## 与历史版本的关键差异

| 维度 | 历史版（品类锚定法） | 旧版（功能暗示法） |
|------|-------------------|-------------------|
| 功能描述 | 全部删除 | 删除功能描述，保留形态暗示 |
| 按键/旋钮 | 不出现 | 用flush depression/raised line暗示 |
| 适用产品 | 极简产品（无操作界面） | 功能性产品（有操作界面） |
| 细节程度 | 极简 | 细节细腻（形态层面） |

## 来源

- Round 1 失败分析：用户评分 1/10，提示词过载
- Round 2 失败分析：用户评分 1/10，品类识别为零
- Round 3 验证：无线充电器设计，首次达到艾维级（D1=80, D3=82），品类锚定法有效
- 模型失效模式：Lovart Nano Banana Pro / Nano Banana 2 输出分析
- REF-PROMPT-002: 中文提示词压缩规则
- REF-QUALITY-002: 图片评审合同
- 用户反馈：2026-06-21 "功能性的按键、功能性的操作的交互功能的描述，一定要细节细腻"
