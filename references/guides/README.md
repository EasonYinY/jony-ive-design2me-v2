---
reference_id: REF-GUIDE-INDEX
title: 扩展指南与深度参考索引
category: guides
used_when:
  - SKILL-SETUP
  - SKILL-UPDATE
  - DEEP-REFERENCE
called_by:
  - skill-reading-guide
  - file-hygiene-check
depends_on:
  - REF-PROCESS-004
  - REF-HYGIENE-001
outputs:
  - guide_inventory
---

# 扩展指南与深度参考索引

> **用途**: 索引所有扩展指南、深度参考文档和外部权威摘录。
> **更新规则**: 需要深度参考时 → 添加新文件；指南更新 → 标记版本；不删除历史记录。
> **目录结构**:

```
references/guides/
├── README.md                 # 本文件：总索引
├── [按需添加指南文件]
└── ...
```

## 已记录指南

| 指南 ID | 标题 | 用途 | 来源 | 状态 |
|---------|------|------|------|------|
| — | 暂无 | — | — | 占位 |

## 预期指南内容

以下指南可根据需要逐步添加：

| 指南 | 用途 | 建议内容 |
|------|------|---------|
| design-philosophy-deep-dive.md | 设计哲学深度解读 | Jony Ive 设计哲学的学术分析 |
| cross-case-analysis.md | 跨案例分析方法 | 如何从多个案例中提取可迁移方法 |
| evidence-collection-guide.md | 证据收集指南 | 如何收集和验证 S/A/B/C/D 级证据 |
| user-research-integration.md | 用户研究集成 | 如何将用户研究融入十五步流程 |
| manufacturing-constraints.md | 制造约束指南 | 常见制造约束及其设计影响 |
| material-selection-guide.md | 材料选择指南 | 材料性能、制造、触感、老化综合评估 |

## 使用方式

1. **需要深度参考时**: 查找对应指南文件
2. **新任务需要扩展知识时**: 按指南模板创建新文件
3. **指南更新时**: 保留历史版本，添加新版本

## 创建新指南模板

```markdown
---
reference_id: REF-GUIDE-NNN
title: [指南标题]
category: guides
used_when:
  - [步骤/场景]
called_by:
  - [workflow-name]
depends_on:
  - [dependency-ref]
outputs:
  - guide_content
---

# [指南标题]

## 概述

[描述指南的目的和范围]

## 详细内容

[指南的详细内容]

## 使用示例

[具体的使用示例]

## 注意事项

[使用时的注意事项]

## 相关参考

- [引用相关 reference]
```
