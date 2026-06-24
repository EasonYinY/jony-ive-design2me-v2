---
reference_id: REF-HANDOFF-R4-R5-02
title: Round 4 → Round 5 交接口令
category: handoff
used_when:
  - Round 5 启动
  - 新窗口/代理接力
called_by:
  - iteration-workflow.md
  - 5-round-iteration-plan-v2.md
depends_on:
  - NONE
outputs:
  - handoff_command
---

# Handoff: Round 4 → Round 5

> **日期**: 2026-06-21
> **技能版本**: 当前版本（已升级）
> **上轮产品**: 户外头灯
> **下轮产品**: 户外路灯（公共照明）

---

## 上轮关键发现

### 艾维评分
| 方向 | 形态 | 评分 | 等级 |
|------|------|------|------|
| D1 | 水滴 | 76/90 | 准艾维级 |
| **D2** | **贝壳** | **84/90** | **🎉 艾维级** |
| D3 | 叶片 | 75/90 | 准艾维级 |

### 核心发现
1. **人体工学重要性**: 头灯品类人体工学权重更高
2. **贝壳持续优势**: R2贝壳83/90，R4贝壳84/90，持续艾维级
3. **空气动力学陷阱**: 叶片75/90，人体工学优先于空气动力学
4. **纯自然形态天花板验证**: 水滴76/90，验证Pitfall-028

### 升级内容（当前版本→当前版本）
- 新增: `wearable-ergonomics.md`（穿戴设备人体工学设计）
- 新增: `seashell-form-pattern.md`（贝壳形态应用指南）
- 新增: `pitfall-029-aerodynamic-trap.md`（空气动力学陷阱）
- 升级: `end-to-end-workflow.md`（STEP-04增加人体工学检查）
- 升级: `image-critique.md`（增加人体工学权重评分）

---

## 下轮启动指令

```
# Round 5 启动
加载技能 jony-ive-design2me-v2
执行5轮迭代计划 v2 Round 5
产品：户外路灯
切入角度：公共照明
核心挑战：高度+光覆盖+维护
聚焦维度：比例张力+维护友好

# 关键约束
- 避免圆盘/圆柱/球形等俗套形态（Pitfall-026）
- 优先自然形态+文化杂交（Pitfall-028）
- 至少2种材料，软硬对比（Pitfall-027）
- 不使用模块化（modular-design-scope.md）
- 考虑氛围光设计（ambient-lighting-design.md）
- 人体工学优先（Pitfall-029，若涉及穿戴）
- 目标评分: ≥80/90（艾维级）
```

---

## 已知问题

1. **Lovart模型**: `vertex/anon-bob` 可能timeout，fallback到 `vertex/nano-banana-2`
2. **图片查看**: 复制到桌面后用 `open` 命令打开
3. **技能版本**: 确保使用旧版（已升级）

---

## 文件索引

### Round 4 输出
- `references/iterations/v2-round-4/iteration-plan.md`
- `references/iterations/v2-round-4/design-output.md`（15步推理）
- `references/iterations/v2-round-4/image-analysis.md`（评审）
- `references/iterations/v2-round-4/upgrade-plan.md`（升级计划）

### 图片输出
- `~/lovart-out/v2-r4-d1/`（D1: Droplet）
- `~/lovart-out/v2-r4-d2/`（D2: Seashell）
- `~/lovart-out/v2-r4-d3/`（D3: Leaf）

### 版本记录
- `references/changelogs/当前版本-changelog.md`

---

## 启动确认

启动Round 5前，请确认：
- [ ] 技能版本为旧版
- [ ] 已阅读 `pitfall-026-outdoor-light-form-cliche.md`
- [ ] 已阅读 `pitfall-027-single-material-trap.md`
- [ ] 已阅读 `pitfall-028-pure-natural-form-ceiling.md`
- [ ] 已阅读 `pitfall-029-aerodynamic-trap.md`
- [ ] 已阅读 `cultural-hybrid-design.md`
- [ ] 已阅读 `ambient-lighting-design.md`
- [ ] 已阅读 `wearable-ergonomics.md`
- [ ] 已阅读 `seashell-form-pattern.md`
- [ ] 产品：户外路灯
- [ ] 目标：≥80/90（艾维级）

---

## 来源

- 技能: jony-ive-design2me-v2
- 迭代: Round 4
- 计划: 5-round-iteration-plan-v2.md
