---
reference_id: REF-INDEX-001
title: Reference 总索引
category: index
used_when:
  - ROUTING
called_by:
  - skill-router
depends_on:
  - NONE
outputs:
  - reference_inventory
---

# Reference 总索引

本表登记 `references/` 下全部 Markdown 文档。步骤与引用的权威关系见 [十五步引用映射](process/step-reference-map.md)，专项入口见 [工作流索引](workflows/README.md)。

| ID | 文档 | 用途 |
|---|---|---|
| REF-INDEX-001 | [Reference 总索引](README.md) | category=index | used_when=ROUTING |
| REF-HYGIENE-001 | [文件卫生铁律与增量更新规范](file-hygiene.md) | category=meta | used_when=SKILL-UPDATE,SKILL-REFACTOR,FILE-HYGIENECHECK |
| REF-HANDOFF-001 | [新窗口快速接力口令](handoff-quick-prompt.md) | category=meta | used_when=NEW-SESSION,TASK-HANDOFF,SKILL-RESUME |
| REF-GAPS-001 | [已知缺失与待修复项](known-gaps.md) | category=meta | used_when=SKILL-AUDIT,SKILL-UPDATE,SKILL-SETUP |
| REF-CHANGELOG-001 | [Changelog 索引与版本历史](changelogs/README.md) | category=changelogs | used_when=VERSION-HISTORY,SKILL-UPGRADE-PLANNING |
| REF-CASE-INDEX | [Pitfall 与案例索引](cases/README.md) | category=cases | used_when=SKILL-AUDIT,FAILURE-ANALYSIS,QUALITY-REVIEW |
| REF-RULE-INDEX | [硬编码规则与方法论索引](rules/README.md) | category=rules | used_when=SKILL-AUDIT,DIRECTION-SELECTION,EVIDENCE-EVALUATION |
| REF-GUIDE-INDEX | [扩展指南与深度参考索引](guides/README.md) | category=guides | used_when=SKILL-SETUP,SKILL-UPDATE,DEEP-REFERENCE |
| REF-KB-INDEX | [艾维知识蒸馏库（上游参考）总索引](knowledge-base/README.md) | used_when=KB-BROWSE,KB-EXTEND,KB-VERSION-CHECK |
| REF-GUIDE-MIRROR | [外部知识库镜像与引用闭环集成指南](guides/external-knowledge-mirror-integration.md) | category=guide | used_when=KB-MIRROR,EXTERNAL-KB-SYNC,UPSTREAM-DISTILL |
| PITFALL-040 | [Pitfall 040 · 内容镜像未接入引用闭环](cases/pitfall-040-content-added-not-integrated.md) | category=case | used_when=KB-MIRROR,EXTERNAL-KB-SYNC,SKILL-UPDATE |
| PITFALL-041 | [Pitfall 041 · 验证脚本僵化报"计划外 reference"](cases/pitfall-041-audit-rigidity-false-positive.md) | category=case | used_when=KB-MIRROR,SKILL-AUDIT,EXTERNAL-KB-SYNC |
| PITFALL-042 | [Pitfall 042 · KB 不进 graph 但通过索引表实现闭环](cases/pitfall-042-graph-bypass-via-index-table.md) | category=case | used_when=KB-MIRROR,REFERENCE-GRAPH,EXTERNAL-KB-SYNC |
| PITFALL-002 | [图片查看失败循环（Image View Failure Loop）](cases/pitfall-002-image-view-failure-loop.md) | category=cases | used_when=IMAGE-REVIEW,POST-GENERATION |
| PITFALL-003 | [中途停止执行](cases/pitfall-003-mid-process-stop.md) | category=cases |
| PITFALL-005 | [Pitfall 005: 品类锚定死结 (Category Deadlock)](cases/pitfall-005-category-deadlock.md) | category=case | used_when=SKILL-AUDIT,DOC-REFERENCE,RISK-AUDIT |
| PITFALL-024 | [Pitfall 024 - 形态推导中违反人体工学约束](cases/pitfall-024-ergonomics-violation-in-form-derivation.md) | category=cases |
| PITFALL-026 | [户外灯品类形态俗套避坑](cases/pitfall-026-outdoor-light-form-cliche.md) | category=cases | used_when=户外灯设计,品类形态检查 |
| PITFALL-027 | [单材料设计陷阱](cases/pitfall-027-single-material-trap.md) | category=cases | used_when=CMF设计,材料选择 |
| PITFALL-028 | [纯自然形态天花板](cases/pitfall-028-pure-natural-form-ceiling.md) | category=cases | used_when=文化杂交设计,形态选择 |
| PITFALL-029 | [空气动力学陷阱](cases/pitfall-029-aerodynamic-trap.md) | category=cases | used_when=穿戴设备设计,形态选择 |
| PITFALL-030 | [AI生成产品级精度天花板](cases/pitfall-030-ai-product-ceiling.md) | category=cases | used_when=图片生成,艾维级设计目标,质感提升 |
| PITFALL-030-02 | [技能名称歧义处理](cases/pitfall-030-skill-name-ambiguity.md) | category=cases | used_when=技能加载失败,多版本技能冲突,skill_view 拒绝猜测 |
| PITFALL-031 | [准艾维级天花板突破](cases/pitfall-031-quasi-ive-ceiling.md) | category=cases | used_when=艾维级目标设计 |
| PITFALL-032 | [文化杂交显性化陷阱](cases/pitfall-032-cultural-hybrid-explicit-trap.md) | category=cases | used_when=文化杂交设计 |
| PITFALL-033 | [复杂结构制造精度损失](cases/pitfall-033-complex-structure-precision-loss.md) | category=cases | used_when=结构复杂度评估 |
| PITFALL-034 | [方向同质化陷阱](cases/pitfall-034-direction-homogenization.md) | category=cases | used_when=多代理并行设计 |
| PITFALL-035 | [惊喜时刻同质化](cases/pitfall-035-surprise-homogenization.md) | category=cases |
| PITFALL-039 | [评审标准虚高陷阱](cases/pitfall-039-real-evaluation-standard.md) | category=cases | used_when=图片评审,艾维级设计目标,用户要求严格评审 |
| REF-IVE-001 | [艾维认知与方法稳定快照](core/ive-thinking-models.md) | category=core | used_when=STEP-03,STEP-05,STEP-08 |
| REF-EVIDENCE-001 | [证据政策与禁止外推合同](core/evidence-policy.md) | category=core | used_when=STEP-01,STEP-02,STEP-03 |
| REF-FIVE-001 | [五维推理引擎与显性步骤合同](core/five-dimension-engine.md) | category=core | used_when=STEP-03,STEP-05,STEP-06 |
| REF-CORE-002 | [设计方法论本地快照](core/design-methodology.md) | category=core | used_when=STEP-03,STEP-05,STEP-08 |
| REF-CASE-001 | [可运行案例胶囊](core/case-capsules.md) | category=core | used_when=STEP-03,STEP-08,STEP-14 |
| REF-CASE-011 | [Pitfall 011 - 形态先于关系](cases/pitfall-011-form-before-relation.md) | category=cases |
| REF-CASE-012 | [Pitfall 012 - 材料无职责](cases/pitfall-012-material-without-duty.md) | category=cases |
| REF-CASE-013 | [Pitfall 013 - 纯审美比例](cases/pitfall-013-aesthetic-ratio-only.md) | category=cases |
| REF-CASE-014 | [Pitfall 014 - 颜色词替代高级感](cases/pitfall-014-color-as-premium.md) | category=cases |
| REF-CASE-015 | [Pitfall 015 - 功能未验证](cases/pitfall-015-function-not-verified.md) | category=cases |
| REF-CASE-016 | [Pitfall 016 - 背景侵入](cases/pitfall-016-background-intrusion.md) | category=cases |
| REF-CASE-017 | [Pitfall 017 - 提示词未用代码块](cases/pitfall-017-prompt-not-in-codeblock.md) | category=cases |
| REF-CASE-018 | [Pitfall 018 - 工程材料替代感官材料](cases/pitfall-018-sensory-vs-engineering-materials.md) | category=cases | used_when=PROMPT-COMPILATION |
| REF-CASE-018A | [Pitfall 018 - 视觉张力缺失](cases/pitfall-018-visual-tension.md) | category=cases | used_when=AESTHETIC-GATE |
| REF-CASE-019 | [Pitfall 019 - 曲面过于有机无细节](cases/pitfall-019-organic-curve.md) | category=cases | used_when=IMAGE-CRITIQUE |
| REF-CASE-019-02 | [Pitfall 019 - 提示词质量反馈必须用真实视觉对比验证，禁止编造评分](cases/pitfall-019-prompt-output-empirical-validation.md) | category=cases | used_when=USER-FEEDBACK-ON-PROMPT-QUALITY,PROMPT-REVISION-DECISION,SKILL-UPGRADE-FROM-OUTPUT |
| REF-CASE-019A | [Pitfall 019 - 识别性不足](cases/pitfall-019-identity-weak.md) | category=cases | used_when=AESTHETIC-GATE |
| REF-CASE-020 | [Pitfall 020 - 液态金属造型单一](cases/pitfall-020-liquid-metal-flat.md) | category=cases | used_when=IMAGE-CRITIQUE |
| REF-CASE-020A | [Pitfall 020 - 光路设计不可见](cases/pitfall-020-light-path.md) | category=cases | used_when=IMAGE-CRITIQUE |
| REF-CASE-021 | [Pitfall 021 - 技能升级时验证脚本过度拦截](cases/pitfall-021-reference-graph-upgrade-friction.md) | category=cases | used_when=skill-upgrade,reference-graph-maintenance |
| REF-CASE-022 | [Pitfall 022 - 缺少制造工艺考虑](cases/pitfall-022-no-manufacturing.md) | category=cases | used_when=IMAGE-CRITIQUE |
| REF-CASE-023 | [Pitfall 023 - 隐藏交互节点导致操作不可见](cases/pitfall-021-hidden-interaction.md) | category=cases | used_when=IMAGE-CRITIQUE,STEP-11 |
| REF-CASE-024 | [Pitfall 024 - 基础形态缺失导致有机失控](cases/pitfall-024-form-first-failure.md) | category=cases | used_when=STEP-10,STEP-14 |
| REF-CASE-025 | [Pitfall 025 — 规则写在文档里但未在编译器/质量门中强制执行](cases/pitfall-025-rule-enforcement-gap.md) | category=cases | used_when=skill-optimization,image-generation,rule-audit |
| REF-CASE-025-02 | [Pitfall 025 - 跳过技能升级直接重跑](cases/pitfall-025-upgrade-before-rerun.md) | category=cases | used_when=SKILL-UPGRADE |
| REF-CASE-026 | [Pitfall 026 — 提示词→图片衰减](cases/pitfall-026-prompt-to-image-attenuation.md) | category=cases | used_when=IMAGE-GENERATION |
| REF-CASE-026-02 | [Pitfall 026 - 验证脚本正则表达式不匹配 PITFALL ID](cases/pitfall-026-validation-script-regex-bug.md) | category=cases | used_when=SKILL-UPGRADE,VALIDATION |
| REF-CASE-027 | [Pitfall 027 — 复杂提示词超时](cases/pitfall-027-complex-prompt-timeout.md) | category=cases | used_when=IMAGE-GENERATION |
| REF-CASE-027-02 | [Pitfall 027 — 交互细节衰减](cases/pitfall-027-interaction-detail-attenuation.md) | category=cases | used_when=INTERACTION-DETAIL-VISUALIZATION |
| REF-CASE-028 | [Pitfall 028 — 自然形态表达不稳定](cases/pitfall-028-natural-form-instability.md) | category=cases | used_when=NATURAL-FORM-DESIGN |
| REF-CASE-029 | [Pitfall 029 — 复杂产品衰减增大](cases/pitfall-029-complex-product-attenuation.md) | category=cases | used_when=PRODUCT-SELECTION,EXPECTATION-SETTING |
| REF-CASE-030 | [Pitfall 030 — 佩戴状态不可见](cases/pitfall-030-wearable-state-invisible.md) | category=cases | used_when=PRODUCT-SELECTION,WEARABLE-DESIGN |
| REF-CASE-031 | [Pitfall 031 — 曲面屏幕透明度](cases/pitfall-031-curved-screen-transparency.md) | category=cases | used_when=SCREEN-DESIGN,CURVED-SURFACE |
| REF-CASE-032 | [Pitfall 032 — 迭代模式中 Subagent 不可靠](cases/pitfall-032-subagent-unreliable-in-iteration.md) | category=cases | used_when=ITERATION-MODE,MULTI-ROUND-EXECUTION |
| REF-CASE-PITFALL-001 | [Pitfall 001 - 输出合同违反](cases/pitfall-001-output-contract-violation.md) | category=cases | used_when=OUTPUT-VALIDATION |
| REF-CASES-NEW | [失败模式库 (Failure Patterns)](cases/failure-patterns.md) | category=cases |
| REF-PROCESS-001 | [四阶段十五步主流程](process/end-to-end-workflow.md) | category=process | used_when=STEP-01,STEP-06,STEP-09 |
| REF-PROCESS-002 | [十五步引用映射](process/step-reference-map.md) | category=process | used_when=ROUTING |
| REF-PROCESS-003 | [用户可见推理输出合同](process/reasoning-output.md) | category=process | used_when=STEP-02,STEP-03,STEP-04 |
| REF-PROCESS-004 | [技能完整阅读指南与验证路径](process/skill-reading-guide.md) | category=process | used_when=SKILL-READING,SKILL-REVIEW,STEP-01 |
| REF-PROCESS-005 | [迭代工作流（多轮升级模式）](process/iteration-workflow.md) | category=process | used_when=ITERATION-MODE,MULTI-ROUND-UPGRADE |
| REF-DIRECTION-001 | [第一性物理与人体锚点](direction/first-principles.md) | category=direction | used_when=STEP-03,STEP-04,STEP-05 |
| REF-DIRECTION-002 | [六层约束级联](direction/constraint-cascade.md) | category=direction | used_when=STEP-05,STEP-06,STEP-07 |
| REF-DIRECTION-003 | [反俗套与既往失败扫描](direction/anti-cliche.md) | category=direction | used_when=STEP-08,STEP-14 |
| REF-DIRECTION-004 | [六轴方向差异门](direction/diversity-gate.md) | category=direction | used_when=STEP-09,STEP-14 |
| REF-DIRECTION-005 | [三方向隔离协议](direction/three-direction-protocol.md) | category=direction | used_when=STEP-06,STEP-09,STEP-13 |
| REF-DESIGN-001 | [Design IR 完整合同](design/design-ir.md) | category=design | used_when=STEP-10,STEP-11,STEP-12 |
| REF-DESIGN-002 | [形态比例与部件层级](design/form-proportion.md) | category=design | used_when=STEP-10,STEP-14 |
| REF-DESIGN-003 | [CMF 系统](design/cmf-system.md) | category=design | used_when=STEP-09,STEP-12,STEP-14 |
| REF-DESIGN-004 | [交互与生命周期](design/interaction-lifecycle.md) | category=design | used_when=STEP-11,STEP-12,STEP-13 |
| REF-PROMPT-001 | [PromptBundle 编译合同](prompt/prompt-contract.md) | category=prompt | used_when=STEP-15 |
| REF-PROMPT-002 | [中文提示词压缩规则](prompt/prompt-compression.md) | category=prompt | used_when=STEP-15 |
| REF-PROMPT-003 | [提示词逐句追溯](prompt/prompt-trace.md) | category=prompt | used_when=STEP-15 |
| REF-PROMPT-004 | [摄影表达控制](prompt/photography-controls.md) | category=prompt | used_when=STEP-15 |
| REF-QUALITY-001 | [审美收敛质量门](quality/aesthetic-gate.md) | category=quality | used_when=STEP-08,STEP-09,STEP-10 |
| REF-QUALITY-002 | [图片评审合同](quality/image-critique.md) | category=quality | used_when=STEP-15 |
| REF-QUALITY-003 | [图片失败库](quality/failure-library.md) | category=quality | used_when=STEP-08,STEP-14,STEP-15 |
| REF-QUALITY-004 | [图片确定性质量门](quality/quality-gates.md) | category=quality | used_when=STEP-02,STEP-07,STEP-09 |
| REF-WORKFLOW-001 | [专项工作流索引](workflows/README.md) | category=workflows | used_when=STEP-01 |
| REF-WORKFLOW-002 | [产品设计工作流](workflows/product-design.md) | category=workflows | used_when=ROUTE-PRODUCT-DESIGN |
| REF-WORKFLOW-003 | [提示词改写工作流](workflows/prompt-rewriting.md) | category=workflows | used_when=ROUTE-PROMPT-REWRITING |
| REF-WORKFLOW-004 | [图片评审工作流](workflows/image-critique.md) | category=workflows | used_when=ROUTE-IMAGE-CRITIQUE |
| REF-WORKFLOW-005 | [设计理念工作流](workflows/design-philosophy.md) | category=workflows | used_when=ROUTE-DESIGN-PHILOSOPHY |
| REF-WORKFLOW-006 | [UI UX 工作流](workflows/ui-ux.md) | category=workflows | used_when=ROUTE-UI-UX |
| REF-WORKFLOW-007 | [服务工作流](workflows/service.md) | category=workflows | used_when=ROUTE-SERVICE |
| REF-WORKFLOW-008 | [组织工作流](workflows/organization.md) | category=workflows | used_when=ROUTE-ORGANIZATION |
| REF-WORKFLOW-009 | [穿戴工作流](workflows/wearable.md) | category=workflows | used_when=ROUTE-WEARABLE |
| REF-WORKFLOW-010 | [模块化工作流](workflows/modular.md) | category=workflows | used_when=ROUTE-MODULAR |
| REF-GUIDE-001 | [视觉张力比例指南](guides/visual-tension-proportion.md) | category=guides | used_when=AESTHETIC-GATE |
| REF-GUIDE-002 | [识别性设计指南](guides/identity-design.md) | category=guides | used_when=AESTHETIC-GATE |
| REF-GUIDE-003 | [人体工学疲劳数据参考](guides/ergonomic-fatigue-data.md) | category=guides | used_when=INTERACTION-LIFECYCLE |
| REF-GUIDE-004 | [照明产品光路设计指南](guides/lighting-design.md) | category=guides | used_when=LIGHTING-PRODUCT |
| REF-GUIDE-005 | [提示词接缝精度强化指南](guides/prompt-seam-precision.md) | category=guides | used_when=PROMPT-COMPILATION |
| REF-GUIDE-006 | [微型化产品设计指南](guides/miniaturization-design.md) | category=guides | used_when=MINIATURIZATION-PRODUCT |
| REF-GUIDE-007 | [艾维级设计系统化方法](guides/ive-level-design.md) | category=guides | used_when=AESTHETIC-GATE |
| REF-GUIDE-008 | [提示词工程方法](guides/prompt-engineering.md) | category=guides | used_when=PROMPT-COMPILATION,STEP-15 |
| REF-GUIDE-009 | [文化杂交设计方法](guides/cultural-hybrid-design.md) | category=guides |
| REF-GUIDE-009A | [用户要求显性化拆解方法](guides/user-requirement-disassembly.md) | category=guides | used_when=BRIEF-ANALYSIS |
| **REF-GUIDE-CMS** | **[品类隐喻剥离与纯粹动作解耦协议](guides/category-metaphor-stripping.md)** | **category=guides · 强品类 brief 强制剥离"手柄/扳机"等部件名词 · 2026-06-24 审计师反馈** |
| **REF-GUIDE-MLCL** | **[多层级复合体块锁定与异质材质职责链](guides/multi-level-composite-locking.md)** | **category=guides · 精密/多轴设备三阶层次(宏观+关节+精密端) · 2026-06-24 审计师反馈** |
| **REF-GUIDE-CSM** | **[品类反偏见语境清洗机制](guides/context-sanitation-matrix.md)** | **category=guides · 8 品类通用反偏见矩阵 + 9 段编译位置 · 2026-06-24 审计师反馈** |
| **REF-GUIDE-TDR** | **[几何降维归原协议](guides/topology-de-reduction.md)** | **category=guides · 强制从拓扑几何体出发,禁止已知产品形态 · 2026-06-24 审计师反馈** |
| **REF-GUIDE-CSP** | **[工艺色谱协议](guides/craft-spectrum-palette.md)** | **category=guides · 颜色 4 元素(基础色+表面工艺+反射+触觉) · 2026-06-24 审计师反馈** |
| **REF-GUIDE-AUDIT-24** | **[审计师反馈处理记录 2026-06-24](guides/audit-feedback-2026-06-24-prompt-architecture.md)** | **category=guides · Pitfall 026 处理协议 + 5 个新协议 + 诚实反查审计师灰背景错误 · 2026-06-24 审计师反馈** |
| REF-GUIDE-010 | [Lovart 图片生成执行指南](guides/lovart-execution.md) | category=guides | used_when=IMAGE-GENERATION |
| REF-GUIDE-010A | [用户设计方法论](guides/user-design-methodology.md) | category=guides |
| REF-GUIDE-011 | [曲面设计规则 — 亮眼曲线与明确细节](guides/curve-design-rules.md) | category=guides | used_when=AESTHETIC-GATE |
| REF-GUIDE-012 | [软硬对比设计规则 — 柔的规律性](guides/hard-soft-contrast.md) | category=guides | used_when=AESTHETIC-GATE |
| REF-GUIDE-013 | [交互显性化设计规则 — 隐性显性](guides/interaction-visibility.md) | category=guides | used_when=AESTHETIC-GATE |
| REF-GUIDE-014 | [制造可行性设计规则 — 分件与工艺](guides/manufacturing-feasibility.md) | category=guides | used_when=AESTHETIC-GATE |
| REF-GUIDE-015 | [方法15 - 功能暗示法](guides/method15-functional-hint.md) | category=guides | used_when=PROMPT-COMPILATION,STEP-15 |
| REF-GUIDE-015-02 | [多材料接缝设计指南](guides/multi-material-joint-design.md) | category=guides | used_when=MATERIAL-SELECTION |
| REF-GUIDE-015-03 | [优秀提示词词库](guides/prompt-word-bank.md) | category=guides | used_when=PROMPT-COMPILATION,PROMPT-REWRITING |
| REF-GUIDE-016 | [材料诚实可视化指南](guides/material-honesty-visualization.md) | category=guides | used_when=CMF-DESIGN |
| REF-GUIDE-017 | [文化杂交视觉化指南](guides/cultural-hybrid-visualization.md) | category=guides | used_when=CULTURAL-DESIGN |
| REF-GUIDE-018 | [交互细节可视化指南](guides/interaction-detail-visualization.md) | category=guides | used_when=INTERACTION-DESIGN |
| REF-GUIDE-019 | [声学功能视觉化指南](guides/acoustic-visualization.md) | category=guides | used_when=ACOUSTIC-DESIGN |
| REF-GUIDE-019-02 | [动态形态表达指南](guides/dynamic-form-expression.md) | category=guides | used_when=DYNAMIC-FORM-DESIGN |
| REF-GUIDE-019-03 | [焦点强调可视化指南](guides/focal-point-emphasis.md) | category=guides | used_when=PROMPT-COMPILATION |
| REF-GUIDE-019-04 | [交互细节可视化增强 v2](guides/interaction-detail-visualization-v2.md) | category=guides | used_when=INTERACTION-DETAIL-VISUALIZATION |
| REF-GUIDE-020 | [音频设备设计指南](guides/audio-device-design.md) | category=guides | used_when=ACOUSTIC-DESIGN |
| REF-GUIDE-020-02 | [识别性设计增强 v2](guides/identity-design-v2.md) | category=guides | used_when=IDENTITY-DESIGN |
| REF-GUIDE-020-03 | [悬浮间隙可视化指南](guides/levitation-visualization.md) | category=guides | used_when=PROMPT-COMPILATION |
| REF-GUIDE-021 | [咖啡机品类交互设计指南](guides/coffee-machine-interaction.md) | category=guides | used_when=COFFEE-MACHINE-DESIGN |
| REF-GUIDE-021-02 | [边缘微光表达指南](guides/edge-light-expression.md) | category=guides | used_when=PROMPT-COMPILATION |
| REF-GUIDE-022 | [动态形态图片表达指南](guides/dynamic-form-visualization.md) | category=guides | used_when=DYNAMIC-FORM-DESIGN |
| REF-GUIDE-023 | [自然形态艾维级设计模式](guides/natural-form-ive-level-pattern.md) | category=guides | used_when=FORM-GENERATION |
| REF-GUIDE-023-02 | [可穿戴产品人体工学指南](guides/wearable-ergonomics-guide.md) | category=guides | used_when=WEARABLE-DESIGN |
| REF-GUIDE-AGENT-DIFF | [Agent 差异化执行模式](guides/agent-differentiation-pattern.md) | category=guides | used_when=多 Agent 并行执行,5轮25代理迭代计划 |
| REF-GUIDE-AI-CEILING-BREAKING | [突破AI产品级精度天花板](guides/ai-ceiling-breaking.md) | category=guides | used_when=AI生成不足,产品级精度目标,艾维级设计目标 |
| REF-GUIDE-AI-QUALITY-ANALYSIS | [AI生成图片质量分析方法](guides/ai-image-quality-analysis.md) | category=guides | used_when=图片评审,AI生成质量评估,突破AI天花板 |
| REF-GUIDE-CONCEPT | [概念来源库](guides/concept-source-library.md) | category=guides |
| REF-GUIDE-FUNCTION-RECOGNITION | [功能识别性强化方法](guides/function-recognition-enhancement.md) | category=guides | used_when=极简形态设计 |
| REF-GUIDE-IVE-PRECISION | [艾维级精密制造细节规范](guides/ive-precision-manufacturing.md) | category=guides | used_when=提示词生成,艾维级设计目标,质感提升 |
| REF-GUIDE-IVE-SYSTEMATIC | [艾维级设计系统化方法](guides/ive-level-systematic-method.md) | category=guides | used_when=艾维级设计目标,设计方法论,评分预测 |
| REF-GUIDE-MATERIAL-DIVERSITY | [材料维度多样化指南](guides/material-diversity-guide.md) | category=guides | used_when=多代理并行设计 |
| REF-GUIDE-MATERIAL-VISUALIZATION | [材料对比可视化策略](guides/material-contrast-visualization.md) | category=guides | used_when=提示词生成 |
| REF-GUIDE-MODULAR | [模块化设计适用场景限定](guides/modular-design-scope.md) | category=guides | used_when=模块化设计决策,产品架构选择 |
| REF-GUIDE-OPERATION-DIVERSITY | [操作维度多样化指南](guides/operation-diversity-guide.md) | category=guides | used_when=多代理并行设计 |
| REF-GUIDE-OUTDOOR | [户外灯品类设计综合指南](guides/outdoor-lighting-comprehensive.md) | category=guides | used_when=户外灯设计,品类特定设计,照明产品设计 |
| REF-GUIDE-PRODUCT-PROMPT | [产品级提示词革命](guides/product-level-prompt-revolution.md) | category=guides | used_when=提示词生成,艾维级设计目标,质感提升 |
| REF-GUIDE-RESTING-STATE | [静息状态设计检查清单](guides/resting-state-design-checklist.md) | category=guides | used_when=艾维级目标设计 |
| REF-RULE-010 | [Rule 010 - 形态变化硬规则](rules/rule-form-variety.md) | category=rules | used_when=AESTHETIC-GATE |
| REF-RULE-011 | [Rule 011 - CMF 软硬对比硬规则](rules/rule-cmf-contrast.md) | category=rules | used_when=AESTHETIC-GATE |
| REF-RULE-012 | [Rule 012 - 交互节点显性化硬规则](rules/rule-interaction-nodes.md) | category=rules | used_when=AESTHETIC-GATE |
| REF-RULE-013 | [Rule 013 - 制造工艺硬约束](rules/rule-manufacturing-constraints.md) | category=rules | used_when=AESTHETIC-GATE |
| REF-RULE-ORCH | [三方向差距编排框架](rules/three-direction-orchestration.md) | category=rules |
| REF-RULE-TECH | [技术克制原则](rules/tech-restraint.md) | category=rules |
| REF-ITERATION-5_ROUND_25_AGENT_FINAL_SUMMARY | [5轮25代理迭代升级总结 · jony-ive-design2me-v2](iterations/5-round-25-agent-final-summary.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-5-ROUND-25-AGENT-PLAN | [5轮25代理迭代升级计划 · ](iterations/5-round-25-agent-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-5_ROUND_ITERATION_PLAN | [5轮迭代升级计划 · 完整说明](iterations/5-round-iteration-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-5_ROUND_ITERATION_PLAN_V2 | [5轮迭代升级计划 · ](iterations/5-round-iteration-plan-v2.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-FINAL | [5轮迭代最终总结](iterations/final-summary.md) | category=iterations | used_when=SKILL-REVIEW,VERSION-ASSESSMENT |
| REF-ITERATION-HANDOFF_R3_R4 | [Handoff 口令 · Round 3 → Round 4](iterations/handoff-r3-r4.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-IMAGE_ANALYSIS | [Round 1 图片分析 + 艾维水平评估](iterations/v2-round-1/image-analysis.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-IMAGE_ANALYSIS-02 | [Round 2 图片分析 + 艾维水平评估](iterations/v2-round-2/image-analysis.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-IMAGE_ANALYSIS-03 | [Round 3 图片分析 + 艾维水平评估](iterations/v2-round-3/image-analysis.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-IMAGE_ANALYSIS-04 | [Round 4 图片分析 + 艾维水平评估](iterations/v2-round-4/image-analysis.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-IMAGE_ANALYSIS-05 | [Round 5 图片分析 + 艾维水平评估](iterations/v2-round-5/image-analysis.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-IMAGE_ANALYSIS_V2 | [Round 1 V2 精密制造版评审 · 严格标准](iterations/v2-round-1/image-analysis-v2.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-IMAGE_ANALYSIS_V3 | [Round 1 V3 产品级版评审 · 严格标准](iterations/v2-round-1/image-analysis-v3.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-ITERATION_PLAN | [Round 1 迭代计划](iterations/v2-round-1/iteration-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-ITERATION_PLAN-02 | [Round 2 迭代计划](iterations/v2-round-2/iteration-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-ITERATION_PLAN-03 | [Round 3 迭代计划](iterations/v2-round-3/iteration-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-AGENT-1-DESIGN | [旅行户外灯 — 15步完整推理记录 (Round 1, Agent 1)](iterations/round-1/agent-1-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-AGENT-2-DESIGN | [旅行户外灯设计 — 完整15步推理记录](iterations/round-1/agent-2-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-AGENT-4-DESIGN | [Agent 4: 旅行户外灯（Travel Outdoor Lantern）15步完整推理记录](iterations/round-1/agent-4-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-AGENT-5-DESIGN | [旅行户外灯设计 — 完整15步推理记录](iterations/round-1/agent-5-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-AGENT3-OUTPUT | [Round 1 Agent 3 · 旅行户外灯 · 完整15步推理输出](iterations/round-1/agent-3-design.md) | category=iterations | used_when=ROUND-1-AGENT3-REVIEW |
| REF-ITERATION-R1-ALL-PROMPTS-FOR-GENERATION | [Round 1 - All Prompts for Image Generation](iterations/round-1/all-prompts-for-generation.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-IMAGE-ANALYSIS | [Round 1 图片分析 + 艾维水平评估](iterations/round-1/image-analysis.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-IMAGE-ANALYSIS-BATCH-1 | [Round 1 图片分析 + 艾维水平评估 (Batch 1)](iterations/round-1/image-analysis-batch-1.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-IMAGE-ANALYSIS-BATCH-2 | [Round 1 图片分析 + 艾维水平评估 (Batch 2)](iterations/round-1/image-analysis-batch-2.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-IMAGE-ANALYSIS-BATCH-3 | [Round 1 图片分析 + 艾维水平评估 (Batch 3)](iterations/round-1/image-analysis-batch-3.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-ITERATION-PLAN | [Round 1 迭代计划](iterations/round-1/iteration-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R1-OUTPUT | [Round 1 完整15步推理输出](iterations/round-1/design-output.md) | category=iterations | used_when=ROUND-1-REVIEW |
| REF-ITERATION-R2-AGENT-1-DESIGN | [旅行户外灯 — 15步完整推理记录 (Round 2, Agent 1)](iterations/round-2/agent-1-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R2-AGENT-2-DESIGN | [Round 2 - Agent 2 设计方案 · 旅行户外灯](iterations/round-2/agent-2-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R2-AGENT-3-DESIGN | [Round 2 - Agent 3 设计方案 · 旅行户外灯](iterations/round-2/agent-3-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R2-AGENT-4-DESIGN | [Round 2 - Agent 4 设计方案 · 旅行户外灯](iterations/round-2/agent-4-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R2-AGENT-5-DESIGN | [Round 2 - Agent 5 设计方案 · 旅行户外灯](iterations/round-2/agent-5-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R2-ANALYSIS | [Round 2 图片分析与艾维水平评估（便携式咖啡机）](iterations/round-2/image-analysis.md) | category=iterations | used_when=ROUND-2-REVIEW |
| REF-ITERATION-R2-ITERATION-PLAN | [Round 2 迭代计划](iterations/round-2/iteration-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R2-OUTPUT | [Round 2 完整15步推理输出（便携式咖啡机）](iterations/round-2/design-output.md) | category=iterations | used_when=ROUND-2-REVIEW |
| REF-ITERATION-R2-UPGRADE-PLAN | [Round 2 升级计划 · ](iterations/round-2/upgrade-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R3-AGENT-1-DESIGN | [Round 3 - Agent 1 设计方案 · 旅行户外灯](iterations/round-3/agent-1-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R3-AGENT-2-DESIGN | [Round 3 - Agent 2 设计方案 · 旅行户外灯](iterations/round-3/agent-2-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R3-AGENT-3-DESIGN | [Round 3 - Agent 3 设计方案 · 旅行户外灯](iterations/round-3/agent-3-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R3-AGENT-4-DESIGN | [Round 3 - Agent 4 设计方案 · 旅行户外灯](iterations/round-3/agent-4-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R3-AGENT-5-DESIGN | [Round 3 - Agent 5 设计方案 · 旅行户外灯](iterations/round-3/agent-5-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R3-DESIGN-OUTPUT | [Round 3 设计输出 · 无线充电器](iterations/round-3/design-output.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R3-IMAGE-ANALYSIS | [Round 3 图片分析 + 艾维水平评估](iterations/round-3/image-analysis.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R3-ITERATION-PLAN | [Round 3 迭代计划](iterations/round-3/iteration-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R3-UPGRADE-PLAN | [Round 3 升级计划](iterations/round-3/upgrade-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R4-AGENT-ALL-DESIGN | [Round 4 - Agent 1-5 设计方案 · 旅行户外灯](iterations/round-4/agent-all-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R4-DESIGN-OUTPUT | [Round 4 设计输出 · 蓝牙音箱](iterations/round-4/design-output.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R4-IMAGE-ANALYSIS | [Round 4 图片分析 + 艾维水平评估](iterations/round-4/image-analysis.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R4-ITERATION-PLAN | [Round 4 迭代计划](iterations/round-4/iteration-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R4-UPGRADE-PLAN | [Round 4 升级计划](iterations/round-4/upgrade-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R5-AGENT-ALL-DESIGN | [Round 5 - Agent 1-5 设计方案 · 旅行户外灯](iterations/round-5/agent-all-design.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R5-DESIGN-OUTPUT | [Round 5 设计输出 · 智能手表](iterations/round-5/design-output.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R5-IMAGE-ANALYSIS | [Round 5 图片分析 + 艾维水平评估](iterations/round-5/image-analysis.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R5-ITERATION-PLAN | [Round 5 迭代计划](iterations/round-5/iteration-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-R5-UPGRADE-PLAN | [Round 5 升级计划 + 最终总结](iterations/round-5/upgrade-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-UPGRADE_PLAN | [Round 1 升级计划](iterations/v2-round-1/upgrade-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-UPGRADE_PLAN-02 | [Round 2 升级计划](iterations/v2-round-2/upgrade-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-UPGRADE_PLAN-03 | [Round 3 升级计划](iterations/v2-round-3/upgrade-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-UPGRADE_PLAN-04 | [Round 4 升级计划](iterations/v2-round-4/upgrade-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-UPGRADE_PLAN-05 | [Round 5 升级计划（最终升级）](iterations/v2-round-5/upgrade-plan.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-V2_FINAL_SUMMARY | [5轮迭代最终总结 · ](iterations/v2-final-summary.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-ITERATION-V2_HANDOFF_R5_R6 | [Handoff 口令: (Round 6)](iterations/v2-handoff-r5-r6.md) | category=iteration | used_when=SKILL-AUDIT,DOC-REFERENCE,ITERATION-MODE |
| REF-CHANGELOG-002 | [历史初始发布变更记录](changelogs/latest-changelog.md) | category=changelogs | used_when=VERSION-HISTORY,SKILL-AUDIT |
| REF-CHANGELOG-003 | [历史变更记录](changelogs/latest-changelog.md) | category=changelogs | used_when=VERSION-HISTORY,SKILL-UPGRADE-PLANNING |
| REF-CHANGELOG-004 | [历史变更记录](changelogs/latest-changelog.md) | category=changelogs | used_when=VERSION-HISTORY,SKILL-UPGRADE-PLANNING |
| REF-CHANGELOG-005 | [历史变更记录](changelogs/latest-changelog.md) | category=changelogs | used_when=VERSION-HISTORY,SKILL-UPGRADE-PLANNING |
| REF-CHANGELOG-006 | [历史变更记录](changelogs/latest-changelog.md) | category=changelogs | used_when=VERSION-UPGRADE,SKILL-AUDIT |
| REF-CHANGELOG-007 | [历史变更记录](changelogs/latest-changelog.md) | category=changelogs | used_when=SKILL-UPDATE,VERSION-HISTORY |
| REF-CHANGELOG-010 | [历史变更记录](changelogs/latest-changelog.md) | category=changelogs | used_when=版本升级,技能审计 |
| REF-CHANGELOG-011 | [历史变更记录](changelogs/latest-changelog.md) | category=changelogs | used_when=版本升级,技能审计 |
| REF-CHANGELOG-012 | [历史变更记录](changelogs/latest-changelog.md) | category=changelogs | used_when=版本升级,技能审计 |
| REF-CHANGELOG-013 | [历史变更记录](changelogs/latest-changelog.md) | category=changelogs | used_when=版本升级,技能审计 |
| REF-CHANGELOG-014 | [历史变更记录（最终版本）](changelogs/latest-changelog.md) | category=changelogs | used_when=版本升级,技能审计,最终评估 |
| REF-CHANGELOG-015 | [历史变更记录（Round 1升级）](changelogs/latest-changelog.md) | category=changelogs | used_when=版本升级,技能审计,Round 2准备 |
| REF-CHANGELOG-015-02-RELEASE | [历史变更记录（AI天花板突破）](changelogs/latest-changelog.md) | category=changelogs | used_when=版本升级,技能审计,AI能力评估 |
| REF-CHANGELOG-2-60-RELEASE | [上游知识蒸馏库镜像同步](changelogs/latest-changelog.md) | category=changelog | used_when=SKILL-AUDIT,DOC-REFERENCE,VERSION-HISTORY |
| REF-CHANGELOG-2-61-RELEASE | [KB 上游镜像完整引用闭环接入](changelogs/latest-changelog.md) | category=changelog | used_when=SKILL-AUDIT,DOC-REFERENCE,VERSION-HISTORY |
| REF-CHANGELOG-2-70-RELEASE | [完整闭环修复 + KB 接入 + humanizer 润色](changelogs/latest-changelog.md) | category=changelog | used_when=V270-CONTINUE |
| REF-HANDOFF-R1-R2 | [Round 1 → Round 2 Handoff 口令](iterations/handoff-r1-r2.md) | category=handoff | used_when=Round 2 启动,新窗口/代理接管 |
| REF-HANDOFF-R1-R2-02 | [Round 1 → Round 2 交接口令](iterations/v2-handoff-r1-r2.md) | category=handoff | used_when=Round 2 启动,新窗口/代理接力 |
| REF-HANDOFF-R2-R3 | [Round 2 → Round 3 交接口令](iterations/v2-handoff-r2-r3.md) | category=handoff | used_when=Round 3 启动,新窗口/代理接力 |
| REF-HANDOFF-R3-R4 | [Round 3 → Round 4 交接口令](iterations/v2-handoff-r3-r4.md) | category=handoff | used_when=Round 4 启动,新窗口/代理接力 |
| REF-HANDOFF-R4-R5 | [Handoff Round 4 → Round 5](iterations/handoff-r4-r5.md) | category=handoff | used_when=ROUND-5-START |
| REF-HANDOFF-R4-R5-02 | [Round 4 → Round 5 交接口令](iterations/v2-handoff-r4-r5.md) | category=handoff | used_when=Round 5 启动,新窗口/代理接力 |
| REF-HANDOFF-V1-1-1 | [Handoff 口令 ](handoff-v1-1-1.md) | category=handoff | used_when=NEW-SESSION,SKILL-CONTINUATION |
| REF-HANDOFF-V2-7-0 | [通关口令 · Humanizer 润色完成](handoff-humanizer-complete.md) | category=handoff | used_when=NEW-SESSION,SKILL-CONTINUATION,V270-CONTINUE |
| REF-PITFALL-022 | [Pitfall 022 — 声学功能不可见](cases/pitfall-022-acoustic-invisible.md) | category=cases | used_when=IMAGE-CRITIQUE,ACOUSTIC-DESIGN |
| REF-PITFALL-027 | [焦点特征丢失 (focal-point-loss)](cases/pitfall-027-focal-point-loss.md) | category=cases | used_when=IMAGE-REVIEW |
| REF-UPGRADE-PLAN-R1 | [Round 1 升级计划](iterations/round-1/upgrade-plan.md) | category=upgrade | used_when=Round 1 升级阶段,技能文件修改,Round 2 准备 |
