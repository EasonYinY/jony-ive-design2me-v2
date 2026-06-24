---
name: jony-ive-design2me-v2
description: 以证据驱动的十五步产品设计工作流，逐步显式交付可审计判断、三个本质不同的完整方向、DesignIR、审美质量门和可追溯中文绘画提示词，并默认在提示词处停止、不生成图片。适用于工业设计、图片评审、提示词改写、设计理念、UI/UX、服务、组织、穿戴、模块化任务，以及用户基于结果提出意见后要求继续优化本技能的场景；不进行人物扮演或表面风格模仿。
version: 2.9.0
author: EasonYinY
license: MIT
metadata:
  hermes:
    tags: [design, product-design, jony-ive, workflow, creative]
    related_skills: [jony-ive-perspective]
---

# Jony Ive Design2Me V2

本技能把可验证的方法证据、五维治理、方向筛选、产品定义与视觉表达组成可回查流程。运行知识为技能内置稳定快照，不依赖外部知识库路径。

> **本版本升级要点(2026-06-23)**:`references/changelogs/v2.9.0-changelog.md`。**模型适配优先协议** —— 提示词结构对齐 Google Cloud 官方公式(Subject + Action + Location + Composition + Style,Camera/Lighting 在末尾);数字精度 ≤ 2 个 ≥ 1mm 粗数字,0 个 < 1mm 精度;工艺词库 ≥ 30 种 + 颜色/光感词库新增 + 3 方向互斥硬约束。事实底座见 `references/research/nano-banana-model-fit.md`(8 个权威源跨平台交叉)。升级纪律见 `references/cases/pitfall-046-upgrade-without-model-capability-research.md` + `references/cases/pitfall-047-prompt-method-chain-internal-contradiction.md`。

> **上游知识蒸馏库（v4.2 · 2026-06-22 镜像,737.5 KB · 28 篇 + 索引 + sha256 校验）**：用户 Obsidian 知识库中《乔纳森·艾维-知识蒸馏》28 篇文档已**字节级镜像**到 `references/knowledge-base/`,完整保留原文,不含任何删减、简化、改写。**当需要深度背景、教学输出、长文写作、5 维联动案例、CPSO 完整案例、协作模板、能力图谱、视觉语料、附录级反例/AI/学习路径**时,读本目录对应分类的原文。**不要把本目录直接喂给 STEP-15 提示词编译**(会破坏 prompt-contract 字符边界)。完整索引见 `references/knowledge-base/README.md`,字节校验见 `SHA256SUMS.txt`。同步命令与 0 删除原则见索引 §4-§5。
>
> **外部镜像通用方法论**:任何"同步/镜像/导入"外部知识库任务必须完成三阶段(镜像 A → 接入 B → 验证 C),B 阶段 6 个必做动作见 `references/guides/external-knowledge-mirror-integration.md`。失败模式:
> - `references/cases/pitfall-040-content-added-not-integrated.md` — 内容镜像未接入引用闭环(v2.6.0 触发:只完成 A,未完成 B,被 user 反问两次后 v2.6.1 补齐)
> - `references/cases/pitfall-041-audit-rigidity-false-positive.md` — 验证脚本僵化报"计划外 reference"(audit_references.py 的 REQUIRED_REFERENCES 固定 37 个,v2.0.0+ 新增的 guides/rules/cases/changelogs 全部被误报)
> - `references/cases/pitfall-042-graph-bypass-via-index-table.md` — KB 不进 graph 但通过索引表实现闭环(fail-fast + 0 改写 + forbidden-text 三重约束下的 graph bypass 模式)
- `references/cases/pitfall-043-skillopt-cannot-break-lovart-visual-blackbox.md` — **2026-06-23 实测**: SkillOpt 训练不能突破 Lovart 视觉权重分配黑盒, 9 张 baseline 图里 A/B 视觉互换 ≥ 4 张, 0.1mm 精度全丢, 印证 pitfall-039 4-5/10 AI 天花板; 改 SKILL.md ≠ 让 Lovart 听 prompt, 应走"对照实验 + 真人评审"
> 
> 文件卫生铁律 7(0 字节改写外部镜像)见 `references/file-hygiene.md`。

## 启动顺序

1. 阅读 [reference 总索引](references/README.md)，确认任务所需文档。
2. 阅读 [四阶段十五步主流程](references/process/end-to-end-workflow.md)。
3. 在 [专项工作流索引](references/workflows/README.md) 中选择唯一主路由。
4. 按 [步骤引用映射](references/process/step-reference-map.md) 为每一步加载多个引用。
5. 按 [用户可见推理输出合同](references/process/reasoning-output.md) 展示完整判断链。
6. **（可选但推荐）当需要深度背景、教学输出、长文写作、5维联动案例、完整 CPSO 案例、协作模板、能力图谱、视觉语料、附录级反例/AI/学习路径时，按 [上游知识蒸馏库索引](references/knowledge-base/README.md) 加载 KB 原文。KB 是 28 篇原文 + 元数据表 + SHA256 校验,完整保留用户原始文字,不参与 STEP-15 提示词编译。**

> **执行前必读（防 Pitfall 001）**：`references/process/reasoning-output.md` 和 `references/guides/prompt-engineering.md` 必须在执行前完整阅读，不得只浏览摘要。执行时必须严格展示每一步的完整 WorkflowStepRecord（输入、核心问题、五维判断、引用证据、候选、否决理由、结论、未确认项、状态、下一步），不得压缩或省略。详见 `references/cases/pitfall-001-output-contract-violation.md`。

> **执行连续性（防 Pitfall 003）**：十五步主流程必须**一次性连续执行完成**，不得在中途（如STEP-05后）停下来询问用户"是否继续"。用户说"直接到最后""继续执行""不要停"时，必须连续输出STEP-01至STEP-15的完整内容。详见 `references/cases/pitfall-003-mid-process-stop.md`。

> **用户设计方法论（高优先级）**：当用户说"按我的方法"或传授设计方法论时，优先使用 `references/guides/user-design-methodology.md` 中的5层设计推导顺序（大造型→部件关系→CMF→细节→画面整体）和"轻重缓急、点睛之笔"原则。

> **自然形态艾维级模式（v1.5.0+）**：基于5轮迭代实证，自然形态（鹅卵石、水滴、禅石）比机械形态更容易达到艾维级。当设计目标是达到艾维级时，优先参考 `references/guides/natural-form-ive-level-pattern.md` 选择自然原型+精密骨架+文化杂交的模式。
>
> **艾维级设计系统化方法（v2.0.0+）**：基于5轮迭代（R1-R5）的完整实证，形成艾维级设计六要素方法论：自然形态（基础）+ 文化杂交（+4~9分）+ 材料对比（+3~8分）+ 人体工学（底线）+ 氛围光设计（+2~4分）+ 比例张力（+2~4分）。详细方法见 `references/guides/ive-level-systematic-method.md`。
>
> **户外灯品类设计综合指南（v2.0.0+）**：5轮迭代覆盖5个户外灯子类型（露营灯/壁灯/庭院灯/头灯/路灯），形成品类特定设计要点。详见 `references/guides/outdoor-lighting-comprehensive.md`。

> **技能边界明确（v1.6.0+）**：本技能（jony-ive-design2me-v2）与 jony-ive-perspective 是**两个独立的技能**，升级时不得混淆。用户明确说"该升级和【jony-ive-perspective】没有任何关系"时，必须严格区分：
> - 本技能：15步推理工作流，默认在提示词处停止，不生成图片
> - jony-ive-perspective：设计评审与图片生成，默认生成图片
> - 升级内容写入本技能目录，不写入 jony-ive-perspective 目录

> **当用户要求"完整阅读"本技能时**：按 [技能完整阅读指南](references/process/skill-reading-guide.md) 执行，确保遍历全部 29 个 reference 文件、6 个验证脚本，并运行引用闭环检查。

## 迭代执行模式（多轮升级）
> **迭代执行模式（多轮升级）**
>
> 当用户要求执行多轮迭代（如"执行5轮""迭代升级"）时，按 [迭代工作流](references/process/iteration-workflow.md) 执行：
> 1. 每轮独立运行，不共享上下文
> 2. 每轮完成后升级技能文件
> 3. 每轮结束后生成 Handoff 口令
> 4. 新窗口/代理通过 Handoff 口令启动下一轮
> 5. 所有迭代记录存放在 `references/iterations/round-N/`
>
> **5轮迭代实证（v2.0.0）**：已完成5轮完整迭代（v1.6.0→v2.0.0），覆盖户外灯5个子类型。迭代记录见 `references/iterations/v2-final-summary.md`，Handoff口令见 `references/iterations/v2-handoff-r*-r*.md`。
>
> **迭代模式中的 subagent 使用约束（v1.6.0+）**：
> **迭代模式中的 subagent 使用约束（v1.6.0+）**：
> - 后台 `delegate_task` 子代理在迭代模式中**不可靠**——多次观测到子代理 timeout、未生成文件、max_iterations 退出前未 commit
> - **v2.2.0+ 新增发现**：当并行启动5个 `delegate_task` 时，频繁触发 HTTP 429（Too Many Requests）限流，导致子代理批量失败
> - **推荐做法**：主会话直接执行每轮迭代，不使用 `delegate_task` 后台子代理；若必须并行，采用串行或最多2个并行
> - 若必须使用子代理，必须在 prompt 中明确"commit after EACH task"硬约束，并切分更小的任务单元
> - 子代理失败后，主会话必须接管并手工完成剩余步骤

> **迭代模式与单次模式的区别**：迭代模式在 STEP-15 后自动进入图片生成、评审、升级流程；单次模式在 STEP-15 停止，等待用户明确出图指令。

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

> **🚨 强制三步链（防 Pitfall 044 — 2026-06-23 咖啡机任务实证）**：
> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 用户明确要求"调用 Lovart nano banana pro 模型生成图片"

---

## 概述

本指南记录从 STEP-15 提示词到 Lovart 图片生成的标准执行流程，确保三个方向并行生成、统一输出规范。

---

## 执行命令模板

### 基础命令结构

```bash
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py chat \
  --prompt "[提示词]" \
  --prefer-models '{"IMAGE":["vertex/anon-bob"]}' \
  --download --output-dir ~/lovart-out/[目录名]
```

**第二步：立即 publish 到 Eagle（每方向一次，必跑）**：

```bash
bash ~/.hermes/skills/lovart/scripts/eagle_publish.sh publish-images \
  --file ~/lovart-out/<brief>-r<N>-d<N>/lovart_<hash>.png \
  --brief <slug> --version V<N>.0 \
  --direction "D<N>-<name>" --model vertex/anon-bob \
  --prompt "<完整 prompt 原文>"
```

**第三步：项目结束 publish-doc（必跑）**：

```bash
bash ~/.hermes/skills/lovart/scripts/eagle_publish.sh publish-doc \
  --brief <slug> --version V<N>.0 \
  --chat-log /tmp/<brief>-chat.md \
  --reasoning /tmp/<brief>-reasoning.md \
  --prompts-dir /tmp/<brief>-prompts/
```

> **跨技能钩子**：本技能的"出图 → Eagle"完整流程依赖 `lovart` skill（v2.x+），
> 任何 Lovart 出图任务前必须先 `skill_view(name="lovart")` 加载 v2.0+ 协议
> （含 `eagle-integration.md` 集成合同与 3 个新 pitfall 017/018/019）。
> 漏加载会导致：只下载到桌面不推送 / 用户追问后才补做 / SKILL.md 与
> 实际行为漂移。详见 `references/cases/pitfall-044-eagle-publish-not-automatic.md`。

**图片查看与评审（防 Pitfall 002）**：

- 当前 Hermes 环境可能无法直接渲染图片文件（browser 工具依赖 Chrome，vision 工具可能无法直接读取本地文件）
- **推荐做法**：将图片复制到用户桌面后用系统默认查看器打开：`cp ~/lovart-out/rN-dN/*.png ~/Desktop/ && open ~/Desktop/*.png`
- **备选做法**：用 `open` 命令直接在 macOS 预览中打开：`open ~/lovart-out/rN-dN/*.png`
- **禁止**：反复尝试 browser_navigate 访问 file:// 路径（会失败并进入循环）
- 图片评审应基于文件信息（分辨率、大小、Lovart 生成日志中的描述）进行，而非依赖 vision 工具直接读取
- 详见 `references/cases/pitfall-002-image-view-failure-loop.md`

_test_marker_

## 技能升级规范

所有升级内容必须写入技能目录：

- **新增指南**: `references/guides/[name].md`
- **新增 Pitfall**: `references/cases/pitfall-NNN-[name].md`
- **迭代记录**: `references/iterations/round-N/`
- **版本记录**: `references/changelogs/vX.Y.Z-changelog.md`
- **Handoff 口令**: `references/iterations/handoff-rN-rN+1.md`

详细方法、合同和流程只存在于 `references/` 对应目录；本文件不复制正文。

| **升级顺序铁律（防 Pitfall 025）**：当用户对已有结果提出批评、要求优化时，**先修改技能文件，再重新执行流程**。用户说"先修改技能文件"时，必须：
> 1. 分析反馈 → 确定技能文件修改点
> 2. 修改技能文件（guides/cases/rules/quality）
> 3. 运行验证脚本确保无错误
> 4. 重新执行 STEP-01 至 STEP-15
> 5. 不得跳过步骤 1-3 直接重新生成
>
> 详见 `references/cases/pitfall-025-upgrade-before-rerun.md`。
>
> **升级前必做调研（防 Pitfall 046,2026-06-23 NEW）**：任何对 SKILL.md / prompt-engineering / cmf-system / product-level-prompt-revolution 的实质性改动前,必须先有 `references/research/{model-name}-model-fit.md` 调研文档(≥ 5 节 + 交叉 ≥ 3 类来源 + user 拍板)。**调研没完成前禁止 bump SKILL.md frontmatter**。详见 `references/cases/pitfall-046-upgrade-without-model-capability-research.md`。
>
> **升级前必查内部矛盾（防 Pitfall 047,2026-06-23 NEW）**：任何改 prompt-engineering.md 之前,必须跑方法链审计:列出方法 1-15,标出冲突对(塞数字 vs 删数字 / 摄影前 vs 后 / 中文 vs 英文),给出解决方案 + 写进 changelog。**禁止静默保留矛盾**。详见 `references/cases/pitfall-047-prompt-method-chain-internal-contradiction.md`。
>
> **v2.0.0 新增 Pitfall 与指南索引**：
> - `references/cases/pitfall-026-outdoor-light-form-cliche.md` - 户外灯品类形态俗套避坑
> - `references/cases/pitfall-027-single-material-trap.md` - 单材料设计陷阱
> - `references/cases/pitfall-028-pure-natural-form-ceiling.md` - 纯自然形态天花板
> - `references/cases/pitfall-029-lovart-pending-confirmation.md` - Lovart pending_confirmation 静默失败
> - `references/cases/pitfall-029-aerodynamic-trap.md` - 空气动力学陷阱
> - `references/guides/modular-design-scope.md` - 模块化设计适用场景限定
> - `references/guides/ambient-lighting-design.md` - 氛围光设计方法
> - `references/guides/wearable-ergonomics.md` - 穿戴设备人体工学设计
> - `references/guides/seashell-form-pattern.md` - 贝壳形态应用指南
> - `references/guides/ive-level-systematic-method.md` - 艾维级设计系统化方法
> - `references/guides/outdoor-lighting-comprehensive.md` - 户外灯品类设计综合指南
>
> **v2.1.0 Round 1升级（5轮25代理迭代）**：
> 基于15个方案评审结果（平均75.4/90），新增3个Pitfall和3个Guide：
> - `references/cases/pitfall-031-quasi-ive-ceiling.md` — 准艾维级天花板突破（79分瓶颈）
> - `references/cases/pitfall-032-cultural-hybrid-explicit-trap.md` — 文化杂交显性化陷阱
> - `references/cases/pitfall-033-complex-structure-precision-loss.md` — 复杂结构制造精度损失
> - `references/guides/resting-state-design-checklist.md` — 静息状态设计检查清单
> - `references/guides/material-contrast-visualization.md` — 材料对比可视化策略
> - `references/guides/function-recognition-enhancement.md` — 功能识别性强化方法
> - 迭代记录：`references/iterations/round-1/upgrade-plan.md`
> - Handoff口令：`references/iterations/handoff-r1-r2.md`
>
> **v2.2.0 产品级提示词革命（用户反馈驱动）**：
> 当用户反馈"设计太飘逸、质感不顶级、缺少细节"时，必须执行产品级提示词革命：
> - 删除所有抽象形容词（"温润""精致""优雅"），替换为工程参数（尺寸、Ra值、R值、壁厚）
> - 强制包含精确尺寸（≥3个，精确到0.1mm）、壁厚、圆角、表面粗糙度
> - 强制包含功能细节（≥5个：接口、指示灯、按键、散热、固定、防水）
> - 强制包含制造精度（≥2处：CNC刀纹、阳极氧化膜厚、拉丝纹理）
> - 强制包含材料牌号（6061-T6铝合金、SUS304不锈钢等）
> - 强制包含重量感描述（重心、配重、密度）
> - 详见 `references/guides/product-level-prompt-revolution.md` 和 `references/guides/ive-precision-manufacturing.md`
>
> **v2.3.0 真实评审标准与AI天花板识别（用户反馈驱动）**：
> 当用户反馈"评分降一半"或要求严格真实评审时：
> - **不要字面理解**：用户要求的是更严格的评审标准，不是数学计算
> - **使用真实标准**：诚实报告AI生成的真实水平（当前约4-5/10），不虚高
> - **识别AI天花板**：当前AI（Lovart Nano Banana Pro）无法达到产品级精度
>   - 材料质感：塑料感，无法真实表达金属/玻璃冷峻感
>   - 制造精度：模糊纹理，无法表达CNC刀纹、0.1mm间隙
>   - 功能细节：完全缺失，USB-C、指示灯、散热孔不可见
>   - 边缘清晰度：7.92/100，边缘模糊
> - **提供突破方案**：
>   - 短期：使用更高质量模型（Midjourney v6/DALL-E 3）
>   - 中期：使用ControlNet精确控制形态和细节
>   - 长期：结合3D渲染（Blender+KeyShot）达到产品级
> - **分阶段评分预期**：概念级（4-5/10）→ 细节级（6-7/10）→ 精确级（7-8/10）→ 产品级（8-9/10）
> - 详见 `references/cases/pitfall-039-real-evaluation-standard.md` 和 `references/guides/ai-ceiling-breaking.md`
>
> **v2.3.0 图片质量本地分析方法（工具限制应对）**：
> 当vision工具或browser工具不可用时：
> - 使用Python+PIL进行本地图片质量分析（分辨率、边缘清晰度、对比度、颜色分布）
> - 将图片复制到桌面后用系统查看器打开：`cp ~/lovart-out/rN-dN/*.png ~/Desktop/ && open ~/Desktop/*.png`
> - 禁止反复尝试失败的工具路径（browser file://、vision API）
> - 详见 `references/guides/ai-image-quality-analysis.md` 和 `references/cases/pitfall-002-image-view-failure-loop.md`
>
> **v2.2.0 精密制造细节规范**：
> - `references/guides/ive-precision-manufacturing.md` - 艾维级精密制造细节规范（几何精确度、制造精度、功能细节、材料质感、接缝秩序、静息状态）
>
> **技能名称歧义处理（实践发现）**：
> 当技能目录存在多个备份版本（如 `-BACKUP-v1.1.0-20260621-134945`）时，`skill_view` 会拒绝猜测并要求显式路径。
> - **解决方法**：使用完整分类路径 `creative/jony-ive-design2me-v2` 而非仅技能名
> - **预防措施**：定期清理备份目录，保持技能名称唯一性
> - **详见**：`references/cases/pitfall-030-skill-name-ambiguity.md`
>
> **Agent 差异化执行模式（v2.2.0+ 实践验证）**：
> 在多 Agent 并行执行时，每个 Agent 应有明确的差异化焦点：
> - **Agent 1**：自然形态 + 材料对比方向（鹅卵石/水滴/蘑菇等纯自然形态探索）
> - **Agent 2**：人体工学 + 功能创新方向（穿戴/便携/交互创新）
> - **Agent 3**：文化杂交 + 识别性方向（历史/地域/生物文化杂交）
> - 每个 Agent 在 STEP-06 候选生成时优先探索其焦点方向，但最终仍需通过六轴差异门筛选
> - 实践验证：Agent 3 文化杂交方向在户外灯品类达到预测 90/90 艾维级评分
> - **详见**：`references/guides/agent-differentiation-pattern.md`
>
> **v2.2.0 Round 2升级（5轮25代理迭代续）**：
> 基于Round 2评审发现方向同质化问题，新增2个Pitfall和2个Guide：
> - `references/cases/pitfall-034-direction-homogenization.md` — 方向同质化陷阱（5代理设计高度相似）
> - `references/cases/pitfall-035-surprise-homogenization.md` — 惊喜时刻同质化
> - `references/guides/operation-diversity-guide.md` — 操作维度多样化指南（触摸/旋转/滑动/按压/握持）
> - `references/guides/material-diversity-guide.md` — 材料维度多样化指南（5类材料差异化分配）
> - 迭代记录：`references/iterations/round-2/upgrade-plan.md`
> - Handoff口令：`references/iterations/handoff-r2-r3.md`
>
> **v2.3.0 Round 3升级（操作/材料/工艺差异化验证）**：
> 验证v2.2.0差异化策略有效，5代理使用5种不同操作/材料/工艺，预测评分提升至80-84/90：
> - `references/cases/pitfall-036-operation-ergonomics-mismatch.md` — 操作人体工学不匹配
> - `references/guides/process-diversity-guide.md` — 工艺维度多样化指南
> - 迭代记录：`references/iterations/round-3/`
>
> **v2.4.0 Round 4升级（情感连接突破85分）**：
> 首次突破85分天花板，发现情感连接是关键因素：
> - `references/cases/pitfall-037-score-ceiling-breakthrough.md` — 评分天花板突破
> - `references/guides/emotional-connection-guide.md` — 情感连接设计指南
> - 迭代记录：`references/iterations/round-4/`
>
> **v2.5.0 Round 5升级（故事化设计达到87分）**：
> 最终轮达到87/90，形成完整四维差异化（操作/材料/工艺/情感）：
> - `references/cases/pitfall-038-emotional-connection-missing.md` — 情感连接缺失
> - `references/guides/storytelling-design-guide.md` — 故事化设计指南
> - 迭代记录：`references/iterations/round-5/`
> - 最终总结：`references/iterations/5-round-25-agent-final-summary.md`
