---
reference_id: REF-ITERATION-5_ROUND_25_AGENT_PLAN_V2.0
title: 5轮25代理迭代升级计划 · 当前版本 → 当前版本
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
# 5轮25代理迭代升级计划 · 当前版本 → 当前版本

> **日期**: 2026-06-21
> **技能**: jony-ive-design2me-v2
> **起始版本**: 当前版本
> **目标版本**: 当前版本
> **产品**: 旅行户外灯（Travel Outdoor Lantern）
> **迭代次数**: 5轮
> **代理数**: 25个（5轮 × 5代理/轮）
> **方案数**: 75个（5轮 × 5代理 × 3方向/代理）
> **技能升级**: 每轮结束后基于评审结果升级技能

---

## 迭代架构

### 核心原则

1. **独立性**: 每轮完全独立，不共享上下文
2. **技能升级**: 每轮结束后升级技能文件
3. **Handoff接力**: 每轮结束后生成Handoff口令，新代理/窗口启动下一轮
4. **显性过程**: 每一步推导都完整展示

### 代理分配

| 轮次 | 代理1 | 代理2 | 代理3 | 代理4 | 代理5 |
|------|-------|-------|-------|-------|-------|
| R1 | 旅行户外灯-自然形态 | 旅行户外灯-机械形态 | 旅行户外灯-文化杂交 | 旅行户外灯-极简形态 | 旅行户外灯-有机形态 |
| R2 | 使用R1升级技能 | 使用R1升级技能 | 使用R1升级技能 | 使用R1升级技能 | 使用R1升级技能 |
| R3 | 使用R2升级技能 | 使用R2升级技能 | 使用R2升级技能 | 使用R2升级技能 | 使用R2升级技能 |
| R4 | 使用R3升级技能 | 使用R3升级技能 | 使用R3升级技能 | 使用R3升级技能 | 使用R3升级技能 |
| R5 | 使用R4升级技能 | 使用R4升级技能 | 使用R4升级技能 | 使用R4升级技能 | 使用R4升级技能 |

---

## 每轮执行流程（5代理并行）

### Phase 1: 5代理并行设计推理（15个方案）

每个代理独立执行：

```
STEP 1: 加载 jony-ive-design2me-v2 技能
STEP 2: 执行 STEP-01 至 STEP-15 完整推理
STEP 3: 生成3个方向的完整提示词（中文+英文）
STEP 4: 将3个方向提示词写入文件
STEP 5: 返回3个方向提示词
```

**输出**: 5代理 × 3方向 = 15个方案（15个提示词对）

### Phase 2: 图片生成（3方向/代理 × 5代理 = 15张图并行）

使用 Lovart 技能，指定 `vertex/anon-bob` (Nano Banana Pro) 模型，1K分辨率：

```bash
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py chat \
  --prompt "[提示词]" \
  --prefer-models '{"IMAGE":["vertex/anon-bob"]}' \
  --download --output-dir ~/lovart-out/rN-aM-dD
```

**输出**: 15张图片（5代理 × 3方向）

### Phase 3: 图片评审与艾维评估（15个方案）

对每个方案进行8维度评审 + 艾维水平评估：

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

**参考知识库**: 设计师-知识蒸馏/乔纳森·艾维-知识蒸馏

**输出**: 15个方案的评分 + 优化建议

### Phase 4: 整合升级计划

整合5代理的优化建议，生成升级计划：

```
1. 分析15个方案的共性问题
2. 分析15个方案的个性问题
3. 确定技能升级优先级（流程缺陷 > 方法论缺失 > 表达优化）
4. 生成升级计划文档
5. 执行升级（修改技能文件）
```

**输出**: `references/iterations/round-N/upgrade-plan.md`

### Phase 5: Handoff口令生成

生成下一轮启动口令：

```
1. 记录本轮关键发现
2. 记录技能版本变更
3. 生成Handoff文档
```

**输出**: `references/iterations/handoff-rN-rN+1.md`

---

## 文件存放规范

### 迭代记录目录结构

```
references/iterations/
├── 5-round-25-agent-plan-旧版.md      # 本计划
├── round-1/
│   ├── iteration-plan.md              # R1计划
│   ├── agent-1-design.md              # 代理1设计输出
│   ├── agent-2-design.md
│   ├── agent-3-design.md
│   ├── agent-4-design.md
│   ├── agent-5-design.md
│   ├── image-analysis.md              # 15方案评审汇总
│   └── upgrade-plan.md                # R1升级执行记录
├── round-2/
│   ├── iteration-plan.md
│   ├── agent-1-design.md
│   ├── ...
│   ├── image-analysis.md
│   └── upgrade-plan.md
├── ...
├── round-5/
│   ├── iteration-plan.md
│   ├── agent-1-design.md
│   ├── ...
│   ├── image-analysis.md
│   └── upgrade-plan.md
├── handoff-r1-r2.md                   # R1→R2交接口令
├── handoff-r2-r3.md
├── handoff-r3-r4.md
├── handoff-r4-r5.md
└── final-summary.md                     # 5轮迭代总结
```

### 图片输出目录

```
~/lovart-out/
├── r1-a1-d1/                          # R1代理1方向1
├── r1-a1-d2/                          # R1代理1方向2
├── r1-a1-d3/                          # R1代理1方向3
├── r1-a2-d1/                          # R1代理2方向1
├── ...
└── r5-a5-d3/                          # R5代理5方向3
```

---

## 升级策略

### 升级类型优先级

| 优先级 | 类型 | 说明 |
|--------|------|------|
| 🔴 高 | 流程缺陷 | 影响设计质量的方法论缺失 |
| 🟡 中 | 方法论缺失 | 特定品类/场景的设计方法 |
| 🟢 低 | 表达优化 | 提示词、评审维度优化 |

### 升级文件类型

| 类型 | 存放位置 | 命名规范 |
|------|---------|---------|
| 指南 | `references/guides/` | `[topic].md` |
| Pitfall | `references/cases/` | `pitfall-NNN-[name].md` |
| 流程补丁 | `references/process/` | 修改现有文件 |
| 质量门补丁 | `references/quality/` | 修改现有文件 |
| 版本记录 | `references/changelogs/` | `vX.Y.Z-changelog.md` |

---

## 关键约束

1. **与 jony-ive-perspective 无关**: 本次升级只修改 jony-ive-design2me-v2，不触碰 jony-ive-perspective
2. **技能文件卫生**: 所有升级内容写入技能目录，不污染主文件
3. **版本记录**: 每轮升级必须记录 changelog
4. **Handoff**: 每轮结束必须生成 Handoff 口令
5. **显性过程**: 每一步推导都完整展示，不隐藏
6. **独立性**: 每轮完全独立，不共享上下文

---

## 预期成果

### 量化目标

| 指标 | 起始 | 目标 |
|------|------|------|
| 平均评分 | 77.9/90 | 82+/90 |
| 艾维级方向率 | 53.3% | 70%+ |
| 最高分 | 86/90 | 88+/90 |

### 技能升级

- 新增指南: 5-10个
- 新增Pitfall: 5-10个
- 版本演进: 当前版本 → 当前版本

---

## 执行状态

| 轮次 | 状态 | 开始时间 | 完成时间 | 技能版本 |
|------|------|---------|---------|---------|
| R1 | ⏳ 待执行 | - | - | 当前版本 |
| R2 | ⏳ 待执行 | - | - | 当前版本 |
| R3 | ⏳ 待执行 | - | - | 当前版本 |
| R4 | ⏳ 待执行 | - | - | 当前版本 |
| R5 | ⏳ 待执行 | - | - | 当前版本 |

---

**状态**: 计划已制定，准备执行R1
