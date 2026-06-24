---
reference_id: REF-WORKFLOW-MEDICAL-DEVICE
title: 医疗器械工作流(II 类手持电动)
category: workflows
used_when:
  - ROUTE-MEDICAL-DEVICE
  - ROUTE-REGULATED-PRODUCT
called_by:
  - skill-router
depends_on:
  - REF-WORKFLOW-002
  - REF-DIRECTION-002
  - REF-DESIGN-001
  - REF-GUIDE-MEDICAL-DEVICE
  - REF-CASE-MEDICAL-STAPLER-2026-06-24
outputs:
  - three_medical_device_directions
---

# 医疗器械工作流(II 类手持电动)

## 调用步骤

执行 `STEP-01` 至 `STEP-15`,在用户可见输出中完整展示每一步。必须同时交付三个本质不同方向的完整 DesignIR、质量门结果和各自提示词,不能只展开或绘制首选方向。

**强制前置**:必读 `references/guides/medical-device-design.md`(7 项硬事实 + 矛盾三角 + 法规清单 + 文化杂交 × 医疗场景),这是本工作流的领域知识底座。

默认在三段提示词交付后停止。只有用户在当前请求中明确要求"出图、绘制、生成图片或渲染"时才允许调用图像工具;"设计医疗器械"本身不等于要求绘图。

若当前输入是用户对上一次结果的批评、纠正或建议,且未明确要求重跑项目,则停止本工作流,转入技能优化模式,不重新生成该器械方案。

## 必读引用

- [主流程](../process/end-to-end-workflow.md)
- [产品设计工作流](product-design.md)
- [步骤引用映射](../process/step-reference-map.md)
- [医疗器械硬约束指南](../guides/medical-device-design.md)
- [案例 027 电动吻合器](../cases/case-medical-device-stapler-2026-06-24.md)
- [六层约束](../direction/constraint-cascade.md)
- [DesignIR](../design/design-ir.md)
- [审美质量门](../quality/aesthetic-gate.md)
- [法规清单](../guides/medical-device-design.md#法规清单ii-类手术器械step-07-必查)

## 重点检查(医疗器械专属)

除产品设计通用检查外,医疗器械方向必须额外验证:

1. **法规清单**:ISO 13485 / IEC 60601-1 / ISO 17665 / FDA 21 CFR 878.4750 / ISO 14971 全部命中
2. **灭菌兼容**:任何部件必须耐 134°C × 4min × 2000 次高压蒸汽(塑料件需特别标注)
3. **生物相容**:直接/间接接触患者材料必须 ISO 10993-1 评估
4. **重量限制**:≤ 400g 防止 8h 腕部疲劳指数 > 30
5. **无液体内部**:FDA 21 CFR 888 强制,排除液压/水冷
6. **风险管理**:ISO 14971 风险分析 + 控制 + 残余风险评估三段
7. **文化杂交 × 医疗**:参考 `REF-GUIDE-009` §类型 1(历史对象 × 现代功能),医疗场景里非装饰性杂交

## 启动条件

- 用户 brief 包含"医疗/手术/器械/II 类/无菌/灭菌"等关键词
- 或任务对象明确为手持电动手术器械(吻合器/电刀/超声刀/缝合器/骨钻等)
- 混合任务(如"医疗 + 服务"或"医疗 + UI")选择医疗器械工作流作为主路由

## 与产品设计工作流的关系

医疗器械工作流是产品设计工作流的子集,继承其所有步骤和约束,叠加医疗领域硬约束。两个工作流的关系:

- **主路由冲突时**:医疗器械优先(法规不可让步,不可被外观"美"覆盖)
- **混合任务**:医疗器械作主路由,UI/UX 作补充检查
