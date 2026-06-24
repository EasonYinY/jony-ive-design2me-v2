---
reference_id: REF-CASE-025-02
title: Pitfall 025 - 跳过技能升级直接重跑
category: cases
used_when:
  - SKILL-UPGRADE
called_by:
  - skill-upgrade
  - iteration-workflow
depends_on:
  - REF-PROCESS-005
  - REF-HYGIENE-001
outputs:
  - failure_pattern
---

# Pitfall 025 - 跳过技能升级直接重跑

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 用户反馈 mouse nextgen "先修改技能文件"，明确要求技能升级优先于重新执行
> **严重级别**: HIGH

---

## 触发条件

1. 用户对已有设计结果提出批评、要求优化
2. 用户明确说"先修改技能文件""升级技能""优化方法"
3. Agent 跳过技能文件修改，直接重新生成新方案
4. 结果：新方案重复旧错误，用户再次不满意

---

## 失败表现

- Agent 听到"重新设计"立即执行 STEP-01 至 STEP-15
- 新方案与旧方案有相同缺陷（如基础形态缺失、有机失控）
- 用户再次评分 1-2 分
- 浪费计算资源和时间

---

## 根因分析

### 根因1: 技能文件未升级（80%责任）

- 旧技能文件缺少关键方法（如基础形态锁定、几何精确注入）
- 直接重跑 = 用同样错误的方法再做一遍
- 结果必然相同

### 根因2: 验证脚本未运行（15%责任）

- 修改后未运行 `validate_skill.py` 和 `validate_reference_graph.py`
- 引用图不一致、索引缺失未被发现
- 导致运行时 reference 加载失败

### 根因3: 用户反馈未结构化分析（5%责任）

- 未将用户批评转化为具体的技能文件修改点
- 未确定是方法错误、流程缺失还是执行偏差

---

## 修复方法

### 正确顺序（用户说"先修改技能文件"时）

```
1. 分析用户反馈 → 确定缺陷类型（方法/流程/执行）
2. 确定修改点 → 哪些 reference 文件需要升级
3. 修改技能文件 → 按 file-hygiene.md 规范
4. 运行验证脚本 → validate_skill.py + validate_reference_graph.py
5. 修复验证错误 → 索引、引用图、步骤映射
6. 重新执行 STEP-01 至 STEP-15 → 使用升级后的方法
7. 交付新方案 → 基于新技能文件生成
```

### 修改点决策树

| 用户反馈 | 修改文件 | 修改类型 |
|---------|---------|---------|
| "有机造型无规则" | `references/guides/prompt-engineering.md` | 新增基础形态锁定法 |
| "无基础形态构成" | `references/design/form-proportion.md` | 新增理性-有机转换规则 |
| "像学生作品" | `references/quality/aesthetic-gate.md` | 新增艾维级评分自检 |
| "多材质堆砌" | `references/guides/prompt-engineering.md` | 新增单材质主导策略 |
| "缺少精确数字" | `references/guides/prompt-engineering.md` | 新增几何精确注入法 |
| "无姿态控制" | `references/guides/prompt-engineering.md` | 新增姿态锁定词库 |

---

## 验证方式

检查清单：
- [ ] 是否先分析了用户反馈的缺陷类型？
- [ ] 是否确定了具体的技能文件修改点？
- [ ] 是否修改了技能文件（不是只修改了输出）？
- [ ] 是否运行了 `validate_skill.py`？
- [ ] 是否运行了 `validate_reference_graph.py`？
- [ ] 是否修复了所有验证错误？
- [ ] 是否重新执行了完整流程？
- [ ] 新方案是否避免了旧缺陷？

---

## 来源

- 用户 2026-06-21 反馈：mouse nextgen "先修改技能文件"
- 实际执行：跳过技能升级直接重跑 → 再次失败
- 正确执行：先升级技能文件 → 再重跑 → 成功
