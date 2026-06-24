---
reference_id: REF-ITERATION-R3-ITERATION-PLAN
title: Round 3 迭代计划
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
# Round 3 迭代计划

> **轮次**: Round 3 / 5
> **技能版本**: jony-ive-design2me-v2
> **日期**: 2026-06-21
> **产品**: 无线充电器 (Wireless Charger)
> **品类**: 消费电子
> **核心挑战**: 线圈隐藏 + 表面质感 + 静息状态

---

## 产品定义

### 产品名称
无线充电器 · 静息圆盘

### 品类属性
- **大类**: 消费电子配件
- **子类**: Qi标准无线充电器
- **使用场景**: 桌面、床头、办公室
- **用户画像**: 25-40岁智能手机用户

### 核心功能
1. **主功能**: Qi标准15W无线充电
2. **次功能**: 充电状态指示、防滑、散热
3. **智能功能**: 异物检测、温度保护、充电优化

### 设计挑战
1. **线圈隐藏**: 充电线圈必须隐藏，但散热需要开口
2. **表面质感**: 手机放置面需要特定触感（防滑+不伤屏幕）
3. **静息状态**: 不充电时作为桌面静物的美学价值
4. **状态指示**: 充电状态的视觉反馈（不打扰睡眠）

### 人体工学约束
- **放置尺寸**: 直径≥80mm（覆盖手机）
- **厚度**: ≤15mm（桌面不突兀）
- **重量**: ≥200g（手机放置不移位）
- **倾斜**: 0°（水平放置）

### 禁止内容
- 不得模仿Apple MagSafe、Samsung Pad、小米充电器
- 不得使用LED跑马灯等装饰性元素
- 不得牺牲散热追求薄度

---

##应用

本轮应用所有前期+.0指南：
1. Pitfall 026/027: 提示词衰减+超时应对
2. Guide 015: 多材料接缝设计
3. Guide 016: 材料诚实可视化
4. Guide 017: 文化杂交视觉化
5. Guide 018: 交互细节可视化
6. **Guide 019**: 动态形态表达（状态指示器）

---

## 执行步骤

1. **STEP 1**: 执行15步推理（完整显性展示）
2. **STEP 2**: 生成3方向提示词（300-450词，控制长度）
3. **STEP 3**: Lovart出图（3方向并行，timeout fallback）
4. **STEP 4**: 图片分析 + 艾维评估
5. **STEP 5**: 生成升级计划
6. **STEP 6**: 执行技能升级
7. **STEP 7**: 生成Handoff口令

---

## 输出文件

- `references/iterations/round-3/iteration-plan.md` — 本文件
- `references/iterations/round-3/design-output.md` — 完整15步推理
- `references/iterations/round-3/image-analysis.md` — 图片分析+艾维评估
- `references/iterations/round-3/upgrade-plan.md` — 升级计划
- `~/lovart-out/r3-d{1,2,3}/` — 3方向图片
- `references/iterations/handoff-r3-r4.md` — R3→R4交接口令

---

## 来源

- 5轮迭代计划: `references/iterations/5-round-iteration-plan.md`
- 迭代工作流: `references/process/iteration-workflow.md`
- Handoff R2→R3: `references/iterations/handoff-r2-r3.md`
