---
reference_id: REF-ITERATION-R2-ITERATION-PLAN
title: Round 2 迭代计划
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
# Round 2 迭代计划

> **轮次**: Round 2 / 5
> **技能版本**: jony-ive-design2me-v2
> **日期**: 2026-06-21
> **产品**: 便携式咖啡机 (Portable Espresso Machine)
> **品类**: 厨房电器
> **核心挑战**: 压力系统 + 便携性 + 形态融合

---

## 产品定义

### 产品名称
便携式咖啡机 · 压力雕塑

### 品类属性
- **大类**: 厨房电器
- **子类**: 便携式意式浓缩咖啡机
- **使用场景**: 户外、旅行、办公室桌面
- **用户画像**: 25-40岁咖啡爱好者、户外工作者、商务人士

### 核心功能
1. **主功能**: 15bar压力萃取意式浓缩咖啡
2. **次功能**: 便携收纳、快速加热、杯量可调
3. **智能功能**: 温度控制、萃取计时、低电量提醒

### 设计挑战
1. **压力系统融合**: 如何将15bar压力泵、水箱、萃取头融入整体形态
2. **便携性**: 体积<500ml水瓶，重量<800g，但功能完整
3. **热管理**: 加热模块散热，外壳不烫手
4. **操作直观**: 无需说明书即可使用

### 人体工学约束
- **握持尺寸**: 直径60-80mm，长度200-250mm
- **操作力**: 萃取按钮<5N，水箱盖开启<10N
- **热表面**: 外壳<45°C（萃取时）
- **重心**: 使用时不倾倒，握持平衡

### 禁止内容
- 不得模仿现有产品（如Wacaco Nanopresso、Staresso）
- 不得牺牲压力性能追求形态
- 不得使用纯装饰性元素

---

## 设计目标

1. **艾维级目标**: 达到80/90分（艾维级）
2. **便携性**: 可放入背包侧袋
3. **操作直觉**: 形态暗示操作方式
4. **热安全**: 外壳不烫手

---

##应用

本轮必须应用.0指南：

1. **Pitfall 026**: 提示词→图片衰减应对
   - 提示词长度≥400英文词
   - 抽象概念→具体视觉转换

2. **Guide 015**: 多材料接缝设计
   - 每个材料过渡明确接缝策略（隐藏或强调）
   - 具体制造工艺描述

3. **Guide 016**: 材料诚实可视化
   - 结构功能显性化
   - 触感特征可辨识
   - 制造痕迹合理

4. **Guide 017**: 文化杂交视觉化
   - 具体视觉元素（≥3个/文化）
   - 融合方式明确

5. **Guide 018**: 交互细节可视化
   - 接触点精确位置
   - 视觉+触觉线索
   - 尺寸具体（mm级别）

---

## 执行步骤

1. **STEP 1**: 执行15步推理（完整显性展示，应用旧版指南）
2. **STEP 2**: 生成3方向提示词（≥400词，具体视觉）
3. **STEP 3**: Lovart出图（3方向并行）
4. **STEP 4**: 图片分析 + 艾维评估
5. **STEP 5**: 生成升级计划
6. **STEP 6**: 执行技能升级
7. **STEP 7**: 生成Handoff口令

---

## 输出文件

- `references/iterations/round-2/iteration-plan.md` — 本文件
- `references/iterations/round-2/design-output.md` — 完整15步推理
- `references/iterations/round-2/image-analysis.md` — 图片分析+艾维评估
- `references/iterations/round-2/upgrade-plan.md` — 升级计划
- `~/lovart-out/r2-d{1,2,3}/` — 3方向图片
- `references/iterations/handoff-r2-r3.md` — R2→R3交接口令

---

## 来源

- 5轮迭代计划: `references/iterations/5-round-iteration-plan.md`
- 迭代工作流: `references/process/iteration-workflow.md`
- Handoff R1→R2: `references/iterations/handoff-r1-r2.md`
