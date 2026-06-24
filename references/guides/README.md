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
├── README.md                          # 本文件：总索引
├── visual-tension-proportion.md       # 视觉张力比例设计
├── identity-design.md                 # 识别性设计
├── ergonomic-fatigue-data.md          # 人体工学疲劳数据
├── lighting-design.md                 # 照明产品光路设计
├── prompt-seam-precision.md           # 提示词接缝精度强化
├── miniaturization-design.md          # 微型化产品设计
├── container-sealing-design.md        # 容器密封设计
├── temperature-visualization.md       # 温度可视化设计
├── ive-level-design.md                # 艾维级设计系统化方法
└── ...
```

## 已记录指南

| 指南 ID | 标题 | 用途 | 来源 | 版本 |
|---------|------|------|------|------|
| REF-GUIDE-001 | [视觉张力比例](visual-tension-proportion.md) | 功能比例确定后的视觉张力设计 | Round 1 实证 | 当前版本 |
| REF-GUIDE-002 | [识别性设计](identity-design.md) | 标志性形态与细节设计 | Round 1 实证 | 当前版本 |
| REF-GUIDE-003 | [人体工学疲劳数据](ergonomic-fatigue-data.md) | 人体工学疲劳量化数据 | Round 1 实证 | 当前版本 |
| REF-GUIDE-004 | [照明产品光路设计](lighting-design.md) | 照明产品光路设计方法 | Round 2 实证 | 当前版本 |
| REF-GUIDE-005 | [提示词接缝精度](prompt-seam-precision.md) | 提示词接缝精度强化 | Round 2 实证 | 当前版本 |
| REF-GUIDE-006 | [微型化产品设计](miniaturization-design.md) | 微型化产品特殊设计方法 | Round 3 实证 | 当前版本 |
| REF-GUIDE-007 | [艾维级设计方法](ive-level-design.md) | 艾维级设计系统化方法 | Round 5 突破 | 当前版本 |
| REF-GUIDE-008 | [提示词工程方法](prompt-engineering.md) | 从优秀提示词提炼的提示词工程方法 | 优秀提示词分析 | 旧版 |
| REF-GUIDE-009 | [文化杂交设计方法](cultural-hybrid-design.md) | 文化杂交设计方法 | 优秀提示词分析 | 旧版 |

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
  - NONE
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

## 来源

- 5轮迭代实证（R1-R5）
- REF-PROCESS-001: 四阶段十五步主流程
