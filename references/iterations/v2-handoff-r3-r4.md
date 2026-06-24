---
reference_id: REF-HANDOFF-R3-R4
title: Round 3 → Round 4 交接口令
category: handoff
used_when:
  - Round 4 启动
  - 新窗口/代理接力
called_by:
  - iteration-workflow.md
  - 5-round-iteration-plan-v2.md
depends_on:
  - NONE
outputs:
  - handoff_command
---

# Handoff: Round 3 → Round 4

> **日期**: 2026-06-21
> **技能版本**: 当前版本（已升级）
> **上轮产品**: 户外庭院灯
> **下轮产品**: 户外头灯（穿戴照明）

---

## 上轮关键发现

### 艾维评分
| 方向 | 形态 | 评分 | 等级 |
|------|------|------|------|
| D1 | 禅石 | 76/90 | 准艾维级 |
| **D2** | **蘑菇** | **85/90** | **🎉 艾维级** |
| D3 | 竹节 | 80/90 | 🎉 艾维级 |

### 核心发现
1. **最高分突破85/90**: 蘑菇文化杂交+三材料+氛围光
2. **纯自然形态天花板76/90**: 禅石纯自然形态，缺少文化杂交
3. **氛围光设计成功**: 蘑菇帽状扩散，竹节分段发光
4. **文化杂交持续有效**: 2/3方向达艾维级

### 升级内容（当前版本→当前版本）
- 新增: `ambient-lighting-design.md`（氛围光设计方法）
- 新增: `pitfall-028-pure-natural-form-ceiling.md`（纯自然形态天花板）
- 升级: `cultural-hybrid-design.md`（增加纯自然形态实证）
- 升级: `end-to-end-workflow.md`（STEP-03增加文化杂交检查）
- 升级: `image-critique.md`（增加氛围光+文化杂交评分）

---

## 下轮启动指令

```
# Round 4 启动
加载技能 jony-ive-design2me-v2
执行5轮迭代计划 v2 Round 4
产品：户外头灯
切入角度：穿戴照明
核心挑战：人体工学+重量+光路
聚焦维度：人体工学+轻量化

# 关键约束
- 避免圆盘/圆柱/球形等俗套形态（Pitfall-026）
- 优先自然形态+文化杂交（Pitfall-028）
- 至少2种材料，软硬对比（Pitfall-027）
- 不使用模块化（modular-design-scope.md）
- 考虑氛围光设计（ambient-lighting-design.md）
- 目标评分: ≥80/90（艾维级）
```

---

## 已知问题

1. **Lovart模型**: `vertex/anon-bob` 可能timeout，fallback到 `vertex/nano-banana-2`
2. **图片查看**: 复制到桌面后用 `open` 命令打开
3. **技能版本**: 确保使用旧版（已升级）

---

## 文件索引

### Round 3 输出
- `references/iterations/v2-round-3/iteration-plan.md`
- `references/iterations/v2-round-3/design-output.md`（15步推理）
- `references/iterations/v2-round-3/image-analysis.md`（评审）
- `references/iterations/v2-round-3/upgrade-plan.md`（升级计划）

### 图片输出
- `~/lovart-out/v2-r3-d1/`（D1: Zen Stone）
- `~/lovart-out/v2-r3-d2/`（D2: Mushroom）
- `~/lovart-out/v2-r3-d3/`（D3: Bamboo）

### 版本记录
- `references/changelogs/当前版本-changelog.md`

---

## 启动确认

启动Round 4前，请确认：
- [ ] 技能版本为旧版
- [ ] 已阅读 `pitfall-026-outdoor-light-form-cliche.md`
- [ ] 已阅读 `pitfall-027-single-material-trap.md`
- [ ] 已阅读 `pitfall-028-pure-natural-form-ceiling.md`
- [ ] 已阅读 `cultural-hybrid-design.md`
- [ ] 已阅读 `ambient-lighting-design.md`
- [ ] 产品：户外头灯
- [ ] 目标：≥80/90（艾维级）

---

## 来源

- 技能: jony-ive-design2me-v2
- 迭代: Round 3
- 计划: 5-round-iteration-plan-v2.md
