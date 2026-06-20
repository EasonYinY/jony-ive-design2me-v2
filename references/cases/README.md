---
reference_id: REF-CASE-INDEX
title: Pitfall 与案例索引
category: cases
used_when:
  - SKILL-AUDIT
  - FAILURE-ANALYSIS
  - QUALITY-REVIEW
called_by:
  - failure-library
  - image-critique
  - quality-gates
depends_on:
  - REF-QUALITY-003
  - REF-QUALITY-002
outputs:
  - case_inventory
---

# Pitfall 与案例索引

> **用途**: 索引所有已记录的 pitfall 案例、失败模式和实证记录。
> **更新规则**: 发现新失败模式 → 添加新文件；修复完成 → 标记状态；不删除历史记录。
> **目录结构**:

```
references/cases/
├── README.md                 # 本文件：总索引
├── pitfall-001-apple-shell.md    # Apple-like 外形误用
├── pitfall-002-form-first.md     # 形态优先于关系
├── pitfall-003-direction-homogenization.md  # 方向同质化
└── ...
```

## 已记录 Pitfall

| Pitfall ID | 标题 | 触发条件 | 来源 | 状态 |
|-----------|------|---------|------|------|
| pitfall-001 | Apple-like 外形误用 | 将 BND-002 反向作为形态处方 | REF-QUALITY-003 | 待创建 |
| pitfall-002 | 形态优先于关系 | 未先定义使用者动作就进入形态推导 | REF-IVE-001 MTH-002 | 待创建 |
| pitfall-003 | 方向同质化 | 三个候选方向在关系/结构/操作维度本质相同 | REF-DIRECTION-005 | 待创建 |
| pitfall-004 | 操作不可见 | 图片未显示使用状态或交互反馈 | REF-QUALITY-002 | 待创建 |
| pitfall-005 | 静息状态缺失 | 未展示产品未使用时的物理状态 | REF-QUALITY-002 | 待创建 |
| pitfall-006 | 材料职责未说明 | 只写材料名称未说明性能/制造/维护职责 | REF-IVE-001 MTH-005 | 待创建 |
| pitfall-007 | 通用视觉知识反向决定产品 | 将摄影/渲染知识当作产品决策依据 | REF-EVIDENCE-001 BND-003 | 待创建 |
| pitfall-008 | 未确认项自动填补 | 用风格词或假设填补证据缺口 | REF-EVIDENCE-001 | 待创建 |
| pitfall-009 | 来源冲突静默删除 | 为得出单一结论而删除冲突证据 | REF-EVIDENCE-001 | 待创建 |
| pitfall-010 | 摄影参数创造产品 | 用镜头/构图语言新增/删除产品构件 | REF-PROMPT-001 | 待创建 |
| pitfall-011 | 形态先于关系 | 未先定义使用者动作就进入形态推导；关系模式直接对应已知产品形态 | REF-PROCESS-001 STEP-04/05 | 已记录(2026-06-21) |
| pitfall-012 | 材料无职责 | 只写材料名称或颜色词，未说明结构/触感/制造/寿命/维护职责 | REF-QUALITY-003 | 已记录(2026-06-21) |
| pitfall-013 | 纯审美比例 | 比例数字无人体测量或工程约束依据，仅用"黄金比例""视觉平衡"等审美词 | REF-PROCESS-001 STEP-10 | 已记录(2026-06-21) |
| pitfall-014 | 颜色词替代高级感 | 用"深岩灰""香槟金"等颜色词替代材料职责和工艺说明 | REF-QUALITY-003 | 已记录(2026-06-21) |
| pitfall-015 | 功能未验证 | 形态无法完成核心功能，或关键构件（清洁/更换/维修）不可达 | REF-PROCESS-001 STEP-06 | 已记录(2026-06-21) |
| pitfall-016 | 背景侵入 | 图片出现背景、环境、辅助物品、场景、人物、手、脸等除产品外的元素 | REF-QUALITY-002 | 已记录(2026-06-21) |
| pitfall-017 | 提示词未用代码块 | 最终提示词未使用代码块显示，或未额外输出英文提示词 | REF-PROCESS-001 STEP-15 | 已记录(2026-06-21) |

## 使用方式

1. **质量门审查时**: 对照 pitfall 列表检查当前输出
2. **失败分析时**: 查找匹配的 pitfall 记录根因
3. **新案例积累时**: 按 `pitfall-NNN-标题.md` 格式创建新文件

## 创建新 Pitfall 模板

```markdown
---
reference_id: REF-CASE-NNN
title: Pitfall NNN - 标题
category: cases
used_when:
  - STEP-XX
called_by:
  - quality-gates
  - image-critique
depends_on:
  - REF-QUALITY-003
outputs:
  - failure_pattern
---

# Pitfall NNN - 标题

## 触发条件

[描述什么情况下会触发此 pitfall]

## 失败表现

[描述输出中的具体错误表现]

## 根因分析

[分析为什么会发生]

## 修复方法

[描述如何避免或修复]

## 验证方式

[描述如何确认已修复]

## 来源

- [引用相关 reference 和步骤]
```
