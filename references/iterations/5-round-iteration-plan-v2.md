---
reference_id: REF-ITERATION-5_ROUND_ITERATION_PLAN_V2
title: 5轮迭代升级计划 · 当前版本 → 当前版本
category: iteration
used_when:
  - SKILL-AUDIT
  - DOC-REFERENCE
  - ITERATION-MODE
  - 5-ROUND-PLAN
called_by:
  - skill-router
  - iteration-workflow
depends_on:
  - REF-PROCESS-001
outputs:
  - reference_metadata
---
# 5轮迭代升级计划 · 当前版本 → 当前版本

> **技能**: jony-ive-design2me-v2
> **起始版本**: 当前版本
> **目标版本**: 当前版本
> **日期**: 2026-06-21
> **产品**: 户外灯（固定品类，5轮迭代同一产品类型以深度优化）
> **目标**: 通过5轮独立迭代，每轮完整推理→Lovart出图→评审→升级技能，最终达到稳定艾维级设计水平（≥80/90）

---

## 总体架构

```
┌─────────────────────────────────────────────────────────────────┐
│              5轮迭代升级总架构 · 当前版本 → 当前版本                 │
├─────────────────────────────────────────────────────────────────┤
│  Round 1 → Round 2 → Round 3 → Round 4 → Round 5                │
│    ↑         ↑         ↑         ↑         ↑                     │
│  当前版本   当前版本   当前版本   当前版本   当前版本                    │
│                                                                  │
│  产品: 户外灯（固定品类，深度优化）                                │
│  每轮独立运行，不共享上下文                                       │
│  每轮结束后升级技能，生成Handoff口令                              │
│  新窗口/代理通过Handoff口令启动下一轮                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 每轮标准流程（7步闭环）

### STEP 1: 创建迭代计划
- 产品固定为户外灯，但每轮从不同角度切入
- 写入 `references/iterations/v2-round-N/iteration-plan.md`
- 包含：产品名称、核心功能、设计挑战、本轮聚焦维度

### STEP 2: 执行15步推理（完整显性展示）
- 按 `references/process/end-to-end-workflow.md` 执行
- 从 STEP-01 到 STEP-15 一次性连续输出
- 每步显示完整 WorkflowStepRecord
- 写入 `references/iterations/v2-round-N/design-output.md`

### STEP 3: Lovart出图（3方向并行）
- 使用 `vertex/anon-bob` (Nano Banana Pro) 模型，1K分辨率
- 纯白背景，高细节工业设计渲染风格
- 3个方向同时生成
- 输出至 `~/lovart-out/v2-rN-d{1,2,3}/`
- 写入生成日志

### STEP 4: Vision分析 + 艾维水平评估
- 基于图片文件信息和生成日志进行8维度评审
- 参考知识库：设计师-知识蒸馏/乔纳森·艾维-知识蒸馏
- 评分：形态比例/材料质感/接缝秩序/人体工学/识别性/静息状态/背景纯净度/艾维对比
- 写入 `references/iterations/v2-round-N/image-analysis.md`

### STEP 5: 生成升级计划
- 分析评审结果，确定技能文件修改点
- 按优先级排序：🔴流程缺陷 > 🟡方法论缺失 > 🟢表达优化 > 🔵评审增强
- 写入 `references/iterations/v2-round-N/upgrade-plan.md`

### STEP 6: 执行升级
- 新增/修改 `references/` 下的文件
- 更新版本记录 `references/changelogs/vX.Y.Z-changelog.md`
- 运行验证脚本确保无错误
- 写入升级执行记录

### STEP 7: 生成Handoff口令
- 写入 `references/iterations/v2-handoff-rN-rN+1.md`
- 包含：上轮关键发现、技能版本、下轮启动指令、已知问题

---

## 5轮产品计划（户外灯，每轮不同切入角度）

| 轮次 | 产品 | 切入角度 | 核心挑战 | 聚焦维度 |
|------|------|---------|---------|---------|
| R1 | 户外露营灯 | 便携照明 | 防水+光路+便携 | 光路设计+防水结构 |
| R2 | 户外壁灯 | 固定照明 | 安装+光扩散+耐候 | 安装方式+材料耐候 |
| R3 | 户外庭院灯 | 景观照明 | 氛围+光色+耐久 | 氛围光+材料老化 |
| R4 | 户外头灯 | 穿戴照明 | 人体工学+重量+光路 | 人体工学+轻量化 |
| R5 | 户外路灯 | 公共照明 | 高度+光覆盖+维护 | 比例张力+维护友好 |

> **固定品类策略**: 5轮同一品类（户外灯），从不同子类型切入，深度优化该品类的设计方法论

---

## 技能升级路径（预期）

| 轮次 | 版本 | 预期升级内容 |
|------|------|-------------|
| R1 | 当前版本 | 光路设计方法论、防水结构表达 |
| R2 | 当前版本 | 固定安装方式、耐候材料CMF |
| R3 | 当前版本 | 氛围光设计、景观照明美学 |
| R4 | 当前版本 | 穿戴人体工学、轻量化结构 |
| R5 | 当前版本 | 公共照明比例、维护友好设计 |

---

## 文件存放规范

### 迭代记录目录结构
```
references/iterations/
├── 5-round-iteration-plan-v2.md      # 本文件（总计划）
├── v2-round-1/
│   ├── iteration-plan.md             # R1计划
│   ├── design-output.md              # R1完整15步推理
│   ├── image-analysis.md             # R1图片分析+艾维评估
│   └── upgrade-plan.md               # R1升级执行记录
├── v2-round-2/
│   ├── iteration-plan.md
│   ├── design-output.md
│   ├── image-analysis.md
│   └── upgrade-plan.md
├── ...
├── v2-round-5/
│   ├── iteration-plan.md
│   ├── design-output.md
│   ├── image-analysis.md
│   └── upgrade-plan.md
├── v2-handoff-r1-r2.md              # R1→R2交接口令
├── v2-handoff-r2-r3.md
├── v2-handoff-r3-r4.md
├── v2-handoff-r4-r5.md
└── v2-final-summary.md              # 5轮迭代总结
```

### 图片输出目录
```
~/lovart-out/
├── v2-r1-d1/lovart_*.png            # R1方向1
├── v2-r1-d2/lovart_*.png            # R1方向2
├── v2-r1-d3/lovart_*.png            # R1方向3
├── v2-r2-d1/lovart_*.png
├── ...
└── v2-r5-d3/lovart_*.png            # R5方向3
```

---

## 艾维水平评估标准（8维度）

| 维度 | 权重 | 说明 |
|------|------|------|
| 形态比例与体量感 | 15% | 比例关系、体量感、视觉张力 |
| 材料质感与CMF | 15% | 材料诚实、质感表达 |
| 接缝秩序与制造精度 | 15% | 接缝精密、制造感 |
| 人体工学合理性 | 15% | 尺寸、角度、力度 |
| 识别性与品牌特征 | 15% | 独特性、记忆点 |
| 静息状态表达 | 15% | 静息形态、收纳友好 |
| 背景纯净度 | 5% | 纯白背景、无干扰 |
| 与艾维设计对比 | 5% | 艾维核心16法对照 |

### 评分等级
| 等级 | 分数 | 描述 |
|------|------|------|
| 艾维级 | 80-90/90 | LoveFrom水平，可量产 |
| 准艾维级 | 65-79/90 | 接近，需优化 |
| 普通级 | 50-64/90 | 工业设计水平 |
| 未达标 | <50/90 | 未达标准 |

---

## 关键约束

1. **独立性**: 每轮完全独立，不共享上下文
2. **显性展示**: 每步推导必须完整展示，不得压缩
3. **技能升级**: 每轮结束后必须升级技能文件
4. **Handoff**: 每轮结束必须生成Handoff口令
5. **文件卫生**: 所有内容写入对应目录，不污染主文件
6. **Token效率**: 每轮独立运行，不浪费Token
7. **固定品类**: 5轮均为户外灯，从不同子类型切入

---

## 启动指令

```
# Round 1 启动
加载技能 jony-ive-design2me-v2
执行5轮迭代计划 v2 Round 1
产品：户外露营灯
切入角度：便携照明
核心挑战：防水+光路+便携
```

---

## 来源

- 技能: jony-ive-design2me-v2
- 迭代工作流: references/process/iteration-workflow.md
- 日期: 2026-06-21
