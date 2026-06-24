---
reference_id: REF-ITERATION-R4-ITERATION-PLAN
title: Round 4 迭代计划
category: iteration
used_when:
  - SKILL-AUDIT
  - DOC-REFERENCE
  - ITERATION-MODE
called_by:
  - skill-router
  - iteration-workflow
depends_on:
  - REF-PROCESS-001
outputs:
  - reference_metadata
---
# Round 4 迭代计划

> **轮次**: Round 4 / 5
> **技能版本**: jony-ive-design2me-v2
> **日期**: 2026-06-21
> **产品**: 蓝牙音箱 (Bluetooth Speaker)
> **品类**: 音频设备
> **核心挑战**: 声学腔体 + 视觉张力 + 材料声学

---

## 产品定义

### 产品名称
蓝牙音箱 · 声波雕塑

### 品类属性
- **大类**: 音频设备
- **子类**: 便携式蓝牙音箱
- **使用场景**: 桌面、户外、旅行
- **用户画像**: 25-40岁音乐爱好者、设计师、户外工作者

### 核心功能
1. **主功能**: 蓝牙音频播放，360°声场
2. **次功能**: 防水、便携、长续航
3. **智能功能**: 语音助手、多设备连接、EQ调节

### 设计挑战
1. **声学腔体**: 扬声器需要空间，但便携需要小巧
2. **材料声学**: 材料选择影响音质（金属共振、织物透声）
3. **视觉张力**: 音箱形态需要识别性，但避免俗套
4. **防水与声学**: 防水密封与声学透射的矛盾

### 人体工学约束
- **尺寸**: 直径≤120mm，高度≤80mm（便携）
- **重量**: ≤500g
- **操作**: 按钮触感明确，盲操可行
- **握持**: 单手抓握，防滑

### 禁止内容
- 不得模仿Bose SoundLink、JBL Flip、Sonos Roam
- 不得牺牲音质追求形态
- 不得使用纯装饰性网罩

---

##应用

- Pitfall 026/027/028: 提示词衰减+超时+自然形态
- Guide 015-019: 接缝+材料诚实+文化杂交+交互+动态形态
- **Guide 020**: 静态图LED状态表达
- **Guide 021**: 透明材料表达

---

## 执行步骤

1. **STEP 1**: 执行15步推理
2. **STEP 2**: 生成3方向提示词
3. **STEP 3**: Lovart出图
4. **STEP 4**: 图片分析 + 艾维评估
5. **STEP 5**: 生成升级计划
6. **STEP 6**: 执行技能升级
7. **STEP 7**: 生成Handoff口令

---

## 输出文件

- `references/iterations/round-4/iteration-plan.md`
- `references/iterations/round-4/design-output.md`
- `references/iterations/round-4/image-analysis.md`
- `references/iterations/round-4/upgrade-plan.md`
- `~/lovart-out/r4-d{1,2,3}/`
- `references/iterations/handoff-r4-r5.md`

---

## 来源

- 5轮迭代计划
- Handoff R3→R4
