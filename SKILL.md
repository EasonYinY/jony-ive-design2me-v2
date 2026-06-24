---
name: jony-ive-design2me-v2
description: 以证据驱动的十五步产品设计工作流，逐步显式交付可审计判断、三个本质不同的完整方向、DesignIR、审美质量门和可追溯中文绘画提示词，并默认在提示词处停止、不生成图片。适用于工业设计、图片评审、提示词改写、设计理念、UI/UX、服务、组织、穿戴、模块化任务，以及用户基于结果提出意见后要求继续优化本技能的场景；不进行人物扮演或表面风格模仿。
version: 3.5.2
author: EasonYinY
license: MIT
metadata:
  hermes:
    tags: [design, product-design, jony-ive, workflow, creative]
    related_skills: [jony-ive-perspective]
---

# Jony Ive Design2Me V2

本技能把可验证的方法证据、五维治理、方向筛选、产品定义与视觉表达组成可回查流程。运行知识为技能内置稳定快照，不依赖外部知识库路径。

> **版本号动态变量协议（{{skill_version}}+）**:本技能所有版本号字面仅出现在 2 个位置 — `SKILL.md` frontmatter `version:` 字段(唯一 SSOT)+ `references/changelogs/vX.Y.Z-changelog.md` 文件名与历史内容。`references/` 与 `scripts/` 其它位置一律用占位符 `{{skill_version}}`,由 `scripts/render-version.sh` 从 SKILL.md 提取真实版本号批量渲染。bump 版本只需 ① 改 SKILL.md frontmatter ② 跑 render-version.sh ③ 完成 — **不再手动改任何 references/ 里的版本号字面**。
>
> **升级历史**: 见 `references/changelogs/`(每个版本独立文件,0 删除)。  
> **外部知识库镜像**: 见 `references/knowledge-base/README.md` + `SHA256SUMS.txt`。  
> **文件卫生铁律**: `references/file-hygiene.md`(SKILL.md 严禁 9 类内容)。  
> **本版本关键变更与触发原因**: 最新 `references/changelogs/*.md`。
> **动态变量协议铁律**: `references/file-hygiene.md` § 8.6 + `references/cases/pitfall-053-dynamic-version-variable-pitfalls.md`(占位符永不渲染 + v 前缀陷阱 + bash 3.2 兼容)。

## 启动顺序

1. 阅读 [reference 总索引](references/README.md)，确认任务所需文档。
2. 阅读 [四阶段十五步主流程](references/process/end-to-end-workflow.md)。
3. 在 [专项工作流索引](references/workflows/README.md) 中选择唯一主路由。
4. 按 [步骤引用映射](references/process/step-reference-map.md) 为每一步加载多个引用。
5. 按 [用户可见推理输出合同](references/process/reasoning-output.md) 展示完整判断链。
6. **（可选但推荐）当需要深度背景、教学输出、长文写作、5维联动案例、完整 CPSO 案例、协作模板、能力图谱、视觉语料、附录级反例/AI/学习路径时，按 [上游知识蒸馏库索引](references/knowledge-base/README.md) 加载 KB 原文。KB 是 28 篇原文 + 元数据表 + SHA256 校验,完整保留用户原始文字,不参与 STEP-15 提示词编译。**

> **执行前必读（防 Pitfall 001）**：`references/process/reasoning-output.md` 和 `references/guides/prompt-engineering.md` 必须在执行前完整阅读，不得只浏览摘要。执行时必须严格展示每一步的完整 WorkflowStepRecord。详见 `references/cases/pitfall-001-output-contract-violation.md`。

> **执行连续性（防 Pitfall 003）**：十五步主流程必须**一次性连续执行完成**，不得在中途停下来询问用户"是否继续"。详见 `references/cases/pitfall-003-mid-process-stop.md`。

> **技能边界（{{skill_version}}+）**：本技能与 `jony-ive-perspective` 是**两个独立的技能**。本技能 = 15 步推理工作流，默认在提示词处停止；jony-ive-perspective = 设计评审与图片生成，默认生成图片。升级内容写入本技能目录，不写入 jony-ive-perspective 目录。

> **当用户要求"完整阅读"本技能时**：按 `references/process/skill-reading-guide.md` 执行，遍历全部 reference 文件、验证脚本，并运行引用闭环检查。

## 迭代执行模式（多轮升级）

> 当用户要求执行多轮迭代时，按 `references/process/iteration-workflow.md` 执行：每轮独立运行、完成后升级技能文件、生成 Handoff 口令、新窗口通过口令启动下一轮。所有迭代记录存放在 `references/iterations/round-N/`。

> **迭代模式中的 subagent 使用约束（{{skill_version}}+）**：`delegate_task` 子代理在迭代模式中**不可靠**。推荐主会话直接执行每轮迭代，不用后台子代理；若必须并行，串行或最多 2 个并行；若必须用子代理，prompt 必须显式 "commit after EACH task" 硬约束。详见 `references/cases/pitfall-032-subagent-unreliable-in-iteration.md`。

> **迭代模式 vs 单次模式**：迭代模式在 STEP-15 后自动进入图片生成、评审、升级；单次模式在 STEP-15 停止，等待用户明确出图指令。

## 请求路由优先级

1. 用户提出新的设计任务时，执行十五步主流程。
2. 用户对已有结果提出问题、批评、纠正或建议，但没有明确要求“重做、重跑、重新执行、继续该设计”时，进入**技能优化模式**：只分析反馈、修改本技能及其验证，不重新运行原项目，不生成新的项目方案或图片。
3. 只有用户在当前请求中明确使用“出图、绘制、生成图片、渲染”等直接指令时，才允许调用绘图或图像生成工具。仅说“设计、方案、视觉、提示词、效果”不构成出图授权。
| 4. 路由有歧义时，停在技能优化或文本交付，不自行扩大为项目重跑或图片生成。

> **🚨 用户对出图质量批评时（防 Pitfall 019）**：禁止编造评分、禁止文字评审替代真图对比、禁止跳过真出图就升级 SKILL.md。必须跑 prompt A vs B 同模型对比 → 复制桌面 → vision_analyze 真视觉评审 → 仅描述事实差异，不打分。详见 `references/cases/pitfall-019-prompt-output-empirical-validation.md`。

## 不可跨越的边界

- 事实、推断、假设、未知项和禁止内容必须分区。
- 用户可见输出必须按 `STEP-01` 至 `STEP-15` 顺序逐步给出全部可审计决策依据、中间结论、候选与否决理由，直到三个方向各自的最终提示词；不得只给摘要、首选方向、文件链接或隐藏标签。这里交付的是结构化决策记录，不声称披露模型私密思维链。
- 每次设计任务必须交付三个完整且本质不同的方向；三个方向必须独立推导，并分别在关系、结构和操作上唯一。不得只展开首选项；不足三个通过质量门时重新生成候选，不得弱项补位。
- 摄影与提示词只表达已完成的 DesignIR，不能反向创造产品定义。
- 默认交付终点是三个方向各自的可追溯提示词。没有当前请求中的明确出图指令时，禁止调用绘图或图像生成工具，也不得自动进入图片评审循环。
- 不得使用 Jony Ive、LoveFrom、Apple-like、白色、圆角、金属或极简词替代设计推导。

## 图片生成与评审（迭代模式）

> **强制三步链**（出图 → Eagle publish → doc publish）详见 `references/guides/lovart-execution.md`。

> **跨技能钩子**：本技能的"出图 → Eagle"完整流程依赖 `lovart` skill（v2.x+），任何 Lovart 出图任务前必须先 `skill_view(name="lovart")` 加载协议。详见 `references/cases/pitfall-044-eagle-publish-not-automatic.md`。

> **图片查看与评审（防 Pitfall 002）**：当前 Hermes 环境可能无法直接渲染图片文件。推荐做法是将图片复制到桌面后用系统默认查看器打开。详见 `references/cases/pitfall-002-image-view-failure-loop.md`。

## 技能升级规范

> 所有升级内容写入技能目录。新增指南 / Pitfall / 迭代记录 / 版本记录 / Handoff 口令 全部落 `references/` 子目录(规范见 `references/file-hygiene.md`)。版本历史只写 `references/changelogs/`,**不写回 SKILL.md**。

> **升级顺序铁律（防 Pitfall 025）**：用户对已有结果提出批评、要求优化时,**先修改技能文件,再重新执行流程**。详见 `references/cases/pitfall-025-upgrade-before-rerun.md`。

> **用户反馈处理优先级（2026-06-24）**：用户批评"三个方向太相似"时,优先修改技能文件(主要交付物),重新生成当前方案仅在用户明确要求"重做"时执行。

> **升级前必做调研（防 Pitfall 046,2026-06-23）**：任何对 SKILL.md / prompt-engineering / cmf-system / product-level-prompt-revolution 的实质性改动前,必须先有 `references/research/{model-name}-model-fit.md` 调研文档(≥ 5 节 + 交叉 ≥ 3 类来源 + user 拍板)。**调研没完成前禁止 bump SKILL.md frontmatter**。

> **升级前必查内部矛盾（防 Pitfall 047,2026-06-23）**：任何改 prompt-engineering.md 之前,必须跑方法链审计,标出冲突对,给出解决方案 + 写进 changelog。**禁止静默保留矛盾**。

> **本技能升级索引**：所有版本升级的历史与触发原因 → `references/changelogs/`。所有 pitfall 与指南 → `references/cases/` + `references/guides/`。

> **升级后版本号统一协议（铁律 8,2026-06-24 NEW）**：user 显式说"全部统一一个版本号"时,按 `references/file-hygiene.md` 铁律 8.1 批量替换 + 跳过 changelogs/knowledge-base。详见 `references/cases/pitfall-049-bulk-version-replacement-destroys-context.md` 防破坏模式。

> **升级后备份清理协议（铁律 8.2,2026-06-24 NEW）**：user 显式说"所有备份都删除"时,删 `.bak-*` + `*-BACKUP-*` 副本目录,保留 git 历史。

> **诊断脚本兼容性自检（2026-06-24 NEW）**：写新 shell 脚本 / 改 frontmatter 解析 / 加白名单前,跑 `references/cases/pitfall-052-diagnostic-script-compatibility-bugs.md` 检测三件套(bash 3.2 兼容 / category 单复数 / changelog 路径前缀)。

> **本技能与 jony-ive-perspective 无关（user 2026-06-24 显式声明）**：本技能升级、版本号、内容变更不跨技能影响 jony-ive-perspective(V4.x 系列,独立)。本技能是 V3.x 系列。

详细方法、合同和流程只存在于 `references/` 对应目录；本文件不复制正文。
