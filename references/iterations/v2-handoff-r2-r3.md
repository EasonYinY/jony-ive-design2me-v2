---
reference_id: REF-HANDOFF-R2-R3
title: Round 2 → Round 3 交接口令
category: handoff
used_when:
  - Round 3 启动
  - 新窗口/代理接力
called_by:
  - iteration-workflow.md
  - 5-round-iteration-plan-v2.md
depends_on:
  - NONE
outputs:
  - handoff_command
---

# Handoff: Round 2 → Round 3

> **日期**: 2026-06-21
> **技能版本**: 当前版本（已升级）
> **上轮产品**: 户外壁灯
> **下轮产品**: 户外庭院灯（景观照明）

---

## 上轮关键发现

### 艾维评分
| 方向 | 形态 | 评分 | 等级 |
|------|------|------|------|
| D1 | 水滴 | 80/90 | 🎉 艾维级 |
| **D2** | **贝壳** | **83/90** | **🎉 艾维级** |
| D3 | 折纸 | 74/90 | 准艾维级 |

### 核心发现
1. **文化杂交加分**: 贝壳（文化杂交）83/90 vs 水滴（纯自然）80/90，+3分
2. **材料对比重要性**: 双材料83/90 vs 单材料74/90，+9分
3. **自然形态持续优势**: 2/3方向达艾维级，验证.0有效

### 升级内容（当前版本→当前版本）
- 新增: `pitfall-027-single-material-trap.md`（单材料设计陷阱）
- 升级: `cultural-hybrid-design.md`（增加文化杂交实证）
- 升级: `hard-soft-contrast.md`（增加材料对比指南）
- 升级: `end-to-end-workflow.md`（STEP-10增加材料检查）
- 升级: `image-critique.md`（增加文化杂交+材料对比评分）

---

## 下轮启动指令

```
# Round 3 启动
加载技能 jony-ive-design2me-v2
执行5轮迭代计划 v2 Round 3
产品：户外庭院灯
切入角度：景观照明
核心挑战：氛围+光色+耐久
聚焦维度：氛围光+材料老化

# 关键约束
- 避免圆盘/圆柱/球形等俗套形态（Pitfall-026）
- 优先自然形态+文化杂交（cultural-hybrid-design.md）
- 至少2种材料，软硬对比（Pitfall-027）
- 不使用模块化（modular-design-scope.md）
- 目标评分: ≥80/90（艾维级）
```

---

## 已知问题

1. **Lovart模型**: `vertex/anon-bob` 可能timeout，fallback到 `vertex/nano-banana-2`
2. **图片查看**: 复制到桌面后用 `open` 命令打开
3. **技能版本**: 确保使用旧版（已升级）

---

## 文件索引

### Round 2 输出
- `references/iterations/v2-round-2/iteration-plan.md`
- `references/iterations/v2-round-2/design-output.md`（15步推理）
- `references/iterations/v2-round-2/image-analysis.md`（评审）
- `references/iterations/v2-round-2/upgrade-plan.md`（升级计划）

### 图片输出
- `~/lovart-out/v2-r2-d1/`（D1: Droplet）
- `~/lovart-out/v2-r2-d2/`（D2: Seashell）
- `~/lovart-out/v2-r2-d3/`（D3: Origami）

### 版本记录
- `references/changelogs/当前版本-changelog.md`

---

## 启动确认

启动Round 3前，请确认：
- [ ] 技能版本为旧版
- [ ] 已阅读 `pitfall-026-outdoor-light-form-cliche.md`
- [ ] 已阅读 `pitfall-027-single-material-trap.md`
- [ ] 已阅读 `cultural-hybrid-design.md`
- [ ] 已阅读 `modular-design-scope.md`
- [ ] 产品：户外庭院灯
- [ ] 目标：≥80/90（艾维级）

---

## 来源

- 技能: jony-ive-design2me-v2
- 迭代: Round 2
- 计划: 5-round-iteration-plan-v2.md
