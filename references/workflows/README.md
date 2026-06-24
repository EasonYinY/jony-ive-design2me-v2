---
reference_id: REF-WORKFLOW-001
title: 专项工作流索引
category: workflows
used_when:
  - STEP-01
called_by:
  - skill-router
depends_on:
  - REF-PROCESS-001
outputs:
  - selected_workflow
---

# 专项工作流索引

|| 启动条件 | 工作流 |
|---|---|
| 实体产品设计或重设计 | [产品设计](product-design.md) |
| II 类手持电动手术器械(吻合器/电刀/超声刀/缝合器/骨钻) | [医疗器械](medical-device.md) |
| 改写图像或视频提示词 | [提示词改写](prompt-rewriting.md) |
| 评审图片、草图或渲染 | [图片评审](image-critique.md) |
| 询问设计理念与方法 | [设计理念](design-philosophy.md) |
| 数字界面与体验 | [UI/UX](ui-ux.md) |
| 跨触点服务 | [服务](service.md) |
| 团队、治理与能力建设 | [组织](organization.md) |
| 长时身体接触产品 | [穿戴](wearable.md) |
| 可替换、升级或重组系统 | [模块化](modular.md) |

混合任务选择对最终交付负责的主工作流，其余工作流仅作为补充检查，不重复建立权威结论。**医疗器械工作流是产品设计工作流的子集**:brief 含"医疗/手术/器械/II 类/无菌/灭菌"等关键词或任务对象明确为手持电动手术器械时,医疗器械工作流优先(法规不可让步)。
