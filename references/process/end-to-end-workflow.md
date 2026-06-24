---
reference_id: REF-PROCESS-001
title: 四阶段十五步主流程
category: process
used_when:
  - STEP-01
  - STEP-06
  - STEP-09
  - STEP-15
called_by:
  - all-workflows
depends_on:
  - REF-EVIDENCE-001
  - REF-FIVE-001
outputs:
  - workflow_state
---

# 四阶段十五步主流程

## Brief 解析

1. `STEP-01` 分类任务与交付目标。**KB 反向链接**: `references/knowledge-base/02-设计方法论/04-不可生成项.md`(明确 AI 无法生成的边界,定义伦理与人类判断领域,避免将任务类别错配到生成能力外)。
2. `STEP-02` 区分事实、推断、假设、未知项和禁止内容。**KB 反向链接**: `references/knowledge-base/00-大脑架构总览.md`(五维联动: 核心理念/规则体系/工具基建/执行技巧/环境时机)+ `references/knowledge-base/05-价值观哲学/02-五维联动.md`(五维映射详述)+ `references/knowledge-base/01-认知框架/01-世界观与信念.md`(7 个核心信念,可作为 Brief 解析的事实锚点)。
3. `STEP-03` 用行为与关系重写 brief。**新增用户明确要求显性化**：若用户提出明确风格/感觉要求（如"科技感""简洁风""复古感"），必须在该步骤显性拆解为可执行的设计方向定义（形态特征、材料选择、工艺表达、视觉语言、触感暗示、交互反馈），不得简单带过或仅作为标签粘贴。参考 `references/guides/user-requirement-disassembly.md`。**KB 反向链接**: `references/knowledge-base/03-产品案例库/01-核心案例CPSO.md`(5 个 CPSO 格式案例: Airbnb / Moncler / Balmuda / Linn / Terra Carta,展示完整 Brief → 关系命题重写)+ `references/knowledge-base/03-产品案例库/03-深化案例判断逻辑.md`(决策树 + 常见误区 + 反推验证,Step-03 判断的核心参考)。
4. `STEP-04` 建立可测量的物理与人体事实。新增强制字段：①使用时的身体部位及关键尺寸范围（基于人体测量数据）；②接触方式（握持/佩戴/贴靠/滑动）；③典型动作轨迹；④最优接触角度/力度（如有公开研究）。**KB 反向链接**: `references/knowledge-base/02-设计方法论/01-核心16法.md` §1-§3(关系命题编写 / 触觉节点 / 人体事实的 16 法具体方法,可作为 STEP-04 字段模板的源头参考)。
5. `STEP-05` 提炼必须解决的核心矛盾。新增反形态预设检查：关系模式必须描述"动作"而非"形态"；若直接对应已知产品形态（如指环=智能戒指、半球=美容仪、轨道=工业设备），退回 STEP-04 重新推导。**KB 反向链接**: `references/knowledge-base/02-设计方法论/01-核心16法.md` §4-§6(核心矛盾提炼 / 材料职责 / 时间检查的具体方法)。

## 方向筛选

6. `STEP-06` 生成四至六个候选，**不预设必须保留**。流程修订（旧版 · 2026-06-23 咖啡机任务）：
   - **STEP-06.0 [NEW · 必触发] 功能区拆解**：brief 落地后立即列 4-7 个功能区，每个写明位置+边界+接口+可见性。**触发条件**：功能数 ≥ 3 → 必做；功能数 ≥ 5 → 必做且每区必须独立选基础体块。详见 `references/guides/functional-zoning.md`。
   - **STEP-06.1 [改] 候选生成**：5 个候选 = 5 种**功能区排布方案**（不是 5 种基础体块）。
   - **STEP-06.2 [NEW] 基础体块分配**：选定的功能区排布下，每个功能区独立选基础体块。
   - **STEP-06.3 [NEW · 2026-06-24 v3.0] 拓扑去同质化断路器**：在候选生成前，**必须列出四个物理叙事坐标（Monolithic Slab / Monocoque Tension Shell / Volumetric Subtraction / Tensegrity）**，并确保每个候选来自**不同的物理叙事坐标**。禁止两个候选共享同一坐标。禁止依赖"环、圈、格栅、阵列"等科幻陈词滥调。形态必须从"人与产品的关系"中自然浮现，而非抓取既有符号。必须考虑"不被看见的部分"（底面接合线、铰链、进气口边缘倒角）。详见 `references/cases/pitfall-034-direction-homogenization.md` v3.0。
   - 功能验证：每个候选必须回答"该形态能完成核心功能吗？""关键构件的可及性（清洁/更换/维修）如何？""静息状态（存放/充电/维护）合理吗？""功能区视觉上是否被表达（≥ 3 段视觉信号）？"任一答案为否，否决该候选。**KB 反向链接**: `references/knowledge-base/附录V-跨领域迁移指南.md`(跨领域迁移模式 + transfer 协议,可作为 STEP-06 候选生成的扩展灵感)。
7. `STEP-07` 依次检查物理、法规、制造、成本、寿命和审美约束。
8. `STEP-08` 检查品类俗套、旧失败和无依据形态模仿。**KB 反向链接**: `references/knowledge-base/02-设计方法论/03-误用风险清单.md`(完整误用风险清单)+ `references/knowledge-base/03-产品案例库/02-辅助案例.md`(7 个辅助案例)+ `references/knowledge-base/03-产品案例库/03-背景案例.md`(4 个背景案例)+ `references/knowledge-base/附录X-反例与边界案例库.md`(反例与边界案例库,展示反例识别模式)。
9. `STEP-09` 用六轴差异门筛选三个可继续方向；不足三个时重新生成。**KB 反向链接**: `references/knowledge-base/03-产品案例库/03-深化案例判断逻辑.md`(决策树: 候选 → 通过/退回的判断路径,Step-09 差异门的判断依据)。

## 方向展开

10. `STEP-10` 推导形态、比例和部件层级。新增强制字段：每个关键尺寸必须标注来源（人体测量/工程约束/功能需求/制造工艺）；禁止纯审美比例（如"黄金比例""视觉平衡"）。**新增视觉张力比例设计**：在功能比例确定后，必须通过极端比例、不对称比例、层次比例或动态比例创造视觉张力和识别性。参考 `references/guides/visual-tension-proportion.md`。**新增文化杂交检查**：至少一个方向包含文化杂交元素（历史对象×现代功能、地域材料×全球功能、生物形态×科技功能）。参考 `references/guides/cultural-hybrid-design.md`。
11. `STEP-11` 推导人体工学、动作、反馈和恢复路径。**新增高频接触点设计**：每个方向必须定义至少2个主要接触点（精确位置、材料、触感反馈）和每个高频操作的交互节点（位置、手势、反馈）。参考 `references/guides/prompt-engineering.md` 方法5。
12. `STEP-12` 推导 CMF、制造、老化、清洁和维护。新增"材料职责"强制格式：材料名称 | 结构职责 | 触感职责 | 制造方式 | 寿命 | 维护方式。禁止使用纯颜色词（如"深岩灰""香槟金"）替代材料职责说明。
13. `STEP-13` 形成三个完整且可追溯的 DesignIR。**新增字段**：`primary_contact_points`（主要接触点）、`interaction_nodes`（交互节点）、`cultural_hybrid`（文化杂交，可选）。
14. `STEP-14` 通过审美质量门并证据化排序。**新增识别性设计检查**：在八项质量门基础上，增加识别性设计检查（标志性形态、标志性细节、材料对比、比例记忆）。参考 `references/guides/identity-design.md`。识别性评分需 ≥ 8/10。**新增视觉语言一致性检查**：三个方向的提示词必须共享同一视觉语言基础（悬浮感、背景、焦点、摄影语法、负面约束、材料精确度、几何精确度）。参考 `references/guides/prompt-engineering.md`。

## 表达与评审

15. `STEP-15` 为三个完整方向分别生成追溯记录和压缩提示词。默认在三段提示词交付后停止；只有用户在当前请求中明确要求出图时，才进入图片生成与评审循环。**KB 反向链接（仅供提示词写作参考,严禁直接复制进 PromptBundle 破坏 prompt-contract 字符边界）**: `references/knowledge-base/02-设计方法论/02-Prompt协议.md`(关系命题/材料职责/触觉节点/时间检查的完整 Prompt 协议)+ `references/knowledge-base/07-视觉语料库/01-图像提示词库.md`(12 个产品的完整图像提示词语料,提供句式/词汇参考)+ `references/knowledge-base/08-优秀提示词搜集/02-进阶指南.md`(Prompt 进阶方法)+ `references/knowledge-base/08-优秀提示词搜集/03-实战模板.md`(8 个实战模板)+ `references/knowledge-base/附录Y-AI生成应用指南.md`(AI 生成应用与边界提示)。

**新增提示词输出要求**：
- 最终提示词必须使用代码块显示；额外输出英文提示词（共 6 组代码块：3 中文 + 3 英文）
- **中文提示词强制规则**：所有提示词必须以中文为主体，英文仅作为补充（品牌名、材料名、工艺名可保留英文）
- **语义完整优先**：不强制限制字符数，以语义完整为优先
- **强制保留字段**：精确数字（≥2个）、悬浮感（Floats/levitates）、高频接触点（≥1个）、负面约束（3-5个具体否定）
- **材料精确描述**：材料名称 + 结构状态 + 触感描述（如"smoked glass slab suspended over travertine base"）
- **几何精确注入**：至少2个精确数字（尺寸/角度/曲率/公差，如"6cm thick", "G2 fillet edges"）
- **悬浮感统一**：所有提示词共享"Floats"或等效悬浮描述
- **负面约束具体化**：每个否定对应已否决特征（如"No logo, no text, no screws"）
- **高频接触点精确**：材料 + 精确位置 + 结构状态 + 功能暗示（如"brass brew slit flush in glass"）
- **视觉语言一致性**：三个方向共享同一摄影语法（Studio photograph, three-quarter view slightly above... Floats. Neutral gradient.）
- **单一焦点**：只描述产品，禁止背景/环境/人物/辅助物品
- **纯白背景**：neutral gradient 或 pure white
- **层次描述法**：必须按"大造型→部件关系→CMF→细节特征→画面整体"5层顺序描述
- **轻重缓急与点睛之笔**：每个方向必须有1-2个显性焦点、2-3个隐性细节、1个惊喜/暖心时刻
- 参考 `references/guides/prompt-engineering.md` 方法13（简化法）、方法14（品类锚定法）和方法15（功能暗示法）
- 参考 `references/guides/method15-functional-hint.md` 功能暗示详细指南
- 参考 `references/cases/failure-patterns.md` 避免13个失败模式（品类锚定法）和方法15（功能暗示法）
- 参考 `references/guides/method15-functional-hint.md` 功能暗示详细指南
- 参考 `references/cases/failure-patterns.md` 避免13个失败模式
- 参考 `references/guides/prompt-engineering.md` 方法13（简化法）、方法14（品类锚定法）和方法15（功能暗示法）
- 参考 `references/guides/method15-functional-hint.md` 功能暗示详细指南
- 参考 `references/cases/failure-patterns.md` 避免13个失败模式

**V3.0 审计增强 · 五段式物理空间协议（2026-06-24）**：

每个方案的英文Prompt必须严格遵循以下5段式物理空间布局，严禁任何情绪词、时间词与风格抽象词：

```markdown
[Layout Block 1: 视角与空间锚定]
Studio photograph, [视角，如 three-quarter view slightly above / eye-level dead-front view], of a single [产品中性核心词], LoveFrom 2030, post-Apple Jony Ive.

[Layout Block 2: 核心拓扑与材质职责 (Material Duty)]
[主要构件材质] slab/shell [物理动作，如 suspended over / flush integrated into] a [基座材质] base, [次要材质] [物理交接状态，如 flush in / recessed into].

[Layout Block 3: 极致几何与切线控制 (G2 Fillet & Tangent)]
G2 fillet edges, sweeping tangent into [交接面], [精确微观尺寸描述，如 0.5mm hairline seam / hairline amber LED slit].

[Layout Block 4: 消失设计与行为触点 (Vanishing & Tactile Node)]
[材质] tactile node [功能，如 for physical override] positioned at [精确位置]. Unseen elements perfectly aligned. Floats. Neutral gradient.

[Layout Block 5: 绝对排除项 (Negative Filter)]
No logo, no text, no visible screws, no visible joints, no redundant mechanical decoration, no sci-fi rings.
```

**禁止词滤网（绝对禁止进入Prompt）**：
- ❌ futuristic, sleek, cybernetic, sci-fi, high-tech
- ❌ Apple-like, minimalist design, Jony Ive style
- ❌ sense of safety, feeling of trust, emotional connection
- ❌ spinning slowly, gently hovering, gracefully flying
- ❌ white matte plastic shell, transparent glass window（材料贴图化）

**材料职责强制格式**：材料名称 | 结构职责 | 触感职责 | 制造方式 | 寿命 | 维护方式

**新增"不被看见的部分"强制描述**：底面接合线、铰链、进气口边缘倒角、隐藏接口等必须在Layout Block 2或Block 4中描述。

材料描述必须使用"材料职责"格式：材料名称 | 结构职责 | 触感职责 | 制造方式 | 寿命 | 维护方式。

## 执行模式约定

### 自主执行模式（默认）

用户调用本技能时，**默认进入自主执行模式**：

- 从 STEP-01 到 STEP-15 **一次性连续执行**，不在中间步骤暂停请求用户确认
- 不输出"请确认是否继续"、"是否需要我执行下一步"等中断性提示
- 若执行过程中遇到未确认项，记录为 `unconfirmed_items` 并继续推进，不在该步骤阻塞
- 完整十五步记录和三个方向的提示词必须在**同一交付中完整出现**

**用户明确说"停"、"等一下"、"先别继续"时**，才切换为交互模式，等待用户指令后再继续。

### 为什么需要自主执行

本技能的设计流程是**可审计的决策链**，不是需要逐项授权的菜单。每一步的判断、证据、候选比较和否决理由都已完整展示，用户可以在最终交付后一次性审阅。中途暂停会：

1. 打断设计思维的连续性
2. 增加不必要的交互成本
3. 违背用户"分析→计划→全部执行"的工作偏好

## 默认终止与重跑边界

- "设计、方案、视觉、提示词、效果"只授权文本设计流程，不授权绘图。
- 未出现"出图、绘制、生成图片、渲染"等直接指令时，禁止调用绘图或图像生成工具。
- 用户在一次结果之后提出问题、批评、纠正或建议，默认视为对技能行为的反馈。除非用户明确要求重做、重跑、重新执行或继续该设计，否则只优化技能，不重新执行原项目。
- 十五步用户可见记录和三个方向的提示词必须在同一交付中完整出现；不得以"已写入文件"或仅给首选方向替代。

每步的强制引用以 [步骤引用映射](step-reference-map.md) 为唯一权威来源；用户可见字段以 [推理输出合同](reasoning-output.md) 为准。
