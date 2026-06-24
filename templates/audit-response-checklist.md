---
title: 审计报告响应检查清单
description: 当用户提交审计报告并要求"更新skill"时的标准响应流程
---

# 审计报告响应检查清单

## 触发条件

用户提交详细审计报告 + 显式说"更新skill"

## 响应流程（严禁跳过）

```
STEP 1: 分析审计报告
  - 识别核心病灶（原型丢失/表面虚无/尺度错配/细节剥离等）
  - 识别根因（误读方法3/4/9？缺乏尺度自适应？缺乏自动化审计？）
  - 识别升级领域（结构层/输出层/模型适配层）

STEP 2: 更新技能文件（先升级，再重跑）
  - 修改 end-to-end-workflow.md（新增步骤或检查点）
  - 修改 prompt-engineering.md（新增方法）
  - 修改 aesthetic-gate.md（新增质量门检查项）
  - 修改 design-ir.md（新增字段）
  - 新增参考文档（如果需要）

STEP 3: 生成 changelog
  - 写入 references/changelogs/vX.Y.Z-changelog.md
  - 不 bump 版本号（除非用户拍板）

STEP 4: 运行验证
  - python3 scripts/check_version_pollution.py
  - python3 scripts/validate_skill.py .

STEP 5: 等待用户拍板
  - 用户说"按建议改" → 可以 bump 版本号
  - 用户说"重做" → 重新执行设计流程
  - 用户说"继续优化" → 进入技能优化模式

STEP 6: 重新执行（仅在用户明确要求时）
  - 加载更新后的技能
  - 重新运行十五步流程
  - 验证升级效果
```

## 常见审计类型与对应升级

| 审计类型 | 典型病灶 | 升级文件 | 新增方法/步骤 |
|---------|---------|---------|-------------|
| 原型丢失 | 产品不可识别 | archetype-verification.md | STEP-05.7 |
| 表面虚无 | No text/logo 过度 | prompt-engineering.md | 方法24-26 |
| 尺度错配 | 微观材质用于大型设备 | scale-aware-cmf-compiler.md | 方法28 |
| 提示词堆砌 | 缺乏层级权重 | prompt-engineering.md | 方法27 |
| 缺乏审计 | 漂移未被发现 | fail-safe-verification-gate.md | 方法29 |
| 材料不诚实 | travertine用于MRI | end-to-end-workflow.md | STEP-15.8 |

## 禁止行为

- ❌ 先重新运行流程，再升级技能文件（违反 Pitfall 025）
- ❌ 跳过验证脚本直接交付
- ❌ 未经用户拍板就 bump 版本号
- ❌ 只修改 SKILL.md 不修改 references/
- ❌ 不生成 changelog

## 来源

- 2026-06-24/25 MRI 审计案例：case-mri-audit-2026-06-25.md
- 铁律：references/file-hygiene.md
