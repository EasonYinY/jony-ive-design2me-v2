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
   - **STEP-04.5 [NEW · 2026-06-24 {{skill_version}}] 空间包络硬验证（Spatial Package Validation Matrix）**：在 STEP-04 尾部强制增加体积与包络估算。任何形态生成前的尺寸必须通过 `[净尺寸需求 + 结构厚度容差 + 安全防护边界 = 最终输出数值]` 的显性算式硬校验。载具类公差 ±10%，电子设备 ±0.5mm。未通过校验的尺寸必须标注 `UNVALIDATED` 并回退重新推导。详见 `references/cases/pitfall-055-scale-fact-disconnect.md`。
5. `STEP-05` 提炼必须解决的核心矛盾。新增反形态预设检查：关系模式必须描述"动作"而非"形态"；若直接对应已知产品形态（如指环=智能戒指、半球=美容仪、轨道=工业设备），退回 STEP-04 重新推导。**KB 反向链接**: `references/knowledge-base/02-设计方法论/01-核心16法.md` §4-§6(核心矛盾提炼 / 材料职责 / 时间检查的具体方法)。
   - **STEP-05.5 [NEW · 2026-06-24 {{skill_version}}] 语义洗涤器（Semantic Sanitizer）**：禁止以下两类词汇进入形态推导：① 意识形态/艺术流派名词（如：侘寂、赛博朋克、孟菲斯、极简主义）；② 情感暗示词（如：手工感、温暖感、陌生感、充满信任）。所有形态表达必须通过几何曲率（G2/G3 Continuity）、部件交接（Recessed/Flush/Suspended）和材料物理特性（Tensile/Compressive/Translucent）进行高维泛化重写。详见 `references/cases/pitfall-056-semantic-mimicry.md`。
   - **STEP-05.7 [NEW · 2026-06-24 {{skill_version}}] 行业原型锚定门（Archetype Verification Gate）**：在核心矛盾提炼后、候选生成前，强制注入行业原型拓扑保护协议。详见 `references/guides/archetype-verification.md`。当 Brief 属于"重型设备/复杂系统/精密工具/医疗仪器"类目时，必须显式定义该类目的【不可缩减三大形态特征】（Irreducible Archetype Features），确保后续形态分化不会切断与品类原型的语义联系。检查项：
     - **拓扑完备性**：该产品品类在人类集体潜意识中的"第一特征"是什么？（如：MRI 的扫描舱口、相机的镜头突起、飞行器的推进器轴线）。该特征在形态分化后是否依然占据视觉主体（Volume Weight > 40%）？
     - **尺度错觉防御**：形态描述词是否会引发扩散模型在微观（桌面级）与宏观（建筑级）之间的尺度漂移？必须通过 `[净尺寸需求 + 结构厚度容差 + 安全防护边界 = 最终输出数值]` 的显性算式硬校验。
     - **功能 Legibility**：提示词第一段是否明确描述了定义该产品核心功能的关键宏观大部件与轴向？是否包含至少一个"功能暗示词"（如 patient cradle, scanning bore, control panel）确保 Lovart 模型识别正确品类？
     - **禁止纯几何替代**：严禁用纯几何体（slab, cube, cylinder, ring）完全替代行业原型词。几何体只能作为形态修饰，不能作为语义主语。例如：❌ "A solid basalt slab" → ✅ "A monolithic MRI scanning enclosure with a 65cm bore cavity, surfaced in honed basalt"。

## 方向筛选

6. `STEP-06` 生成四至六个候选，**不预设必须保留**。流程修订（旧版 · 2026-06-23 咖啡机任务）：
   - **STEP-06.0 [NEW · 必触发] 功能区拆解**：brief 落地后立即列 4-7 个功能区，每个写明位置+边界+接口+可见性。**触发条件**：功能数 ≥ 3 → 必做；功能数 ≥ 5 → 必做且每区必须独立选基础体块。详见 `references/guides/functional-zoning.md`。
   - **STEP-06.1 [改] 候选生成**：5 个候选 = 5 种**功能区排布方案**（不是 5 种基础体块）。
   - **STEP-06.2 [NEW] 基础体块分配**：选定的功能区排布下，每个功能区独立选基础体块。
   - **STEP-06.3 [NEW · 2026-06-24 {{skill_version}}] 拓扑去同质化断路器**：在候选生成前，**必须列出四个物理叙事坐标（Monolithic Slab / Monocoque Tension Shell / Volumetric Subtraction / Tensegrity）**，并确保每个候选来自**不同的物理叙事坐标**。禁止两个候选共享同一坐标。禁止依赖"环、圈、格栅、阵列"等科幻陈词滥调。形态必须从"人与产品的关系"中自然浮现，而非抓取既有符号。必须考虑"不被看见的部分"（底面接合线、铰链、进气口边缘倒角）。详见 `references/cases/pitfall-034-direction-homogenization.md` {{skill_version}}。
   - 功能验证：每个候选必须回答"该形态能完成核心功能吗？""关键构件的可及性（清洁/更换/维修）如何？""静息状态（存放/充电/维护）合理吗？""功能区视觉上是否被表达（≥ 3 段视觉信号）？"任一答案为否，否决该候选。**KB 反向链接**: `references/knowledge-base/附录V-跨领域迁移指南.md`(跨领域迁移模式 + transfer 协议,可作为 STEP-06 候选生成的扩展灵感)。
7. `STEP-07` 依次检查物理、法规、制造、成本、寿命和审美约束。
   - **STEP-07.5 [NEW · 2026-06-24 {{skill_version}}] 断路器自闭环（Circuit Breaker Self-Loop）**：若在 STEP-07/08 中否决候选导致剩余候选不足 3 个，**禁止就地修改死地方案或临时编造新方案**。工作流必须强制回退（Re-entry）至 STEP-06.1，修改基础排布变量，重新生成全新的候选集合，并完整重新跑一遍 STEP-07/08 约束级联。详见 `references/cases/pitfall-057-illegal-reskinning-loop.md`。
8. `STEP-08` 检查品类俗套、旧失败和无依据形态模仿。**KB 反向链接**: `references/knowledge-base/02-设计方法论/03-误用风险清单.md`(完整误用风险清单)+ `references/knowledge-base/03-产品案例库/02-辅助案例.md`(7 个辅助案例)+ `references/knowledge-base/03-产品案例库/03-背景案例.md`(4 个背景案例)+ `references/knowledge-base/附录X-反例与边界案例库.md`(反例与边界案例库,展示反例识别模式)。
   - **STEP-08.5 [NEW · 2026-06-24 {{skill_version}}] 品类动态排除词（Category Dynamic Exclusion）**：根据 brief 品类自动绑定动态排除词。例如：飞行器 brief → 自动将 `sci-fi wings, glowing thrusters, aerodynamic decals, transparent dome, cybernetic rings` 写入绝对排除项；消费电子 brief → 自动将 `glossy plastic, LED strips, decorative grooves` 写入排除项。详见 `references/cases/pitfall-058-category-dynamic-exclusion.md`。
9. `STEP-09` 用六轴差异门筛选三个可继续方向；不足三个时重新生成。**KB 反向链接**: `references/knowledge-base/03-产品案例库/03-深化案例判断逻辑.md`(决策树: 候选 → 通过/退回的判断路径,Step-09 差异门的判断依据)。

## 方向展开

10. `STEP-10` 推导形态、比例和部件层级。新增强制字段：每个关键尺寸必须标注来源（人体测量/工程约束/功能需求/制造工艺）；禁止纯审美比例（如"黄金比例""视觉平衡"）。**新增视觉张力比例设计**：在功能比例确定后，必须通过极端比例、不对称比例、层次比例或动态比例创造视觉张力和识别性。参考 `references/guides/visual-tension-proportion.md`。**新增文化杂交检查**：至少一个方向包含文化杂交元素（历史对象×现代功能、地域材料×全球功能、生物形态×科技功能）。参考 `references/guides/cultural-hybrid-design.md`。
11. `STEP-11` 推导人体工学、动作、反馈和恢复路径。**新增高频接触点设计**：每个方向必须定义至少2个主要接触点（精确位置、材料、触感反馈）和每个高频操作的交互节点（位置、手势、反馈）。参考 `references/guides/prompt-engineering.md` 方法5。
12. `STEP-12` 推导 CMF、制造、老化、清洁和维护。新增"材料职责"强制格式：材料名称 | 结构职责 | 触感职责 | 制造方式 | 寿命 | 维护方式。禁止使用纯颜色词（如"深岩灰""香槟金"）替代材料职责说明。
    - **STEP-12.5 [NEW · 2026-06-24 {{skill_version}}] 多材质职责链解耦（Material Duty Chain Decoupling）**：严禁将产品作为单一材质块统一描述。必须强制拆解为三个相互依存的材质层级，并遵循 `[材料名称] + [微观加工工艺] + [承担的物理/交互职责] + [时间沉淀表现]` 的标准公式：
      1. **主构型壳体材质（Primary Structural Base）**：承担大体量气动/物理防护职责，要求耐磨、内敛、高度漫反射质感。必须指定具体工业精加工工艺（如 honed / bead-blasted / satin / mirror-polished）。
      2. **交互与触觉接触材质（Tactile Interaction Interface）**：人手、舱门、按键接触区域，必须选用导热率让人安心、触觉反馈清晰、能留下好看老化痕迹的亲肤/高精材料（如氟橡胶、冷感陶瓷、阳极氧化铝）。
      3. **功能性能量/流体转换材质（Functional Energy/Fluid Transition）**：出风口、排风口、喷射器、接口区域，由于承受高温、高频流体或信号传输，必须显式指定具备强理化特征的工业材质（如耐高温特种陶瓷、钨钛合金、光学级微晶玻璃）。
      详见 `references/guides/prompt-engineering.md` 方法21。
    - **STEP-12.6 [NEW · 2026-06-24 {{skill_version}}] 功能性孔口与秩序收束协议（Aperture & Order Integration）**：按键、交互口、出风口、排风口必须被物理几何秩序死死收束。必须显式指定其"边界消解方式"：
      - **缝隙隐匿法（Slot-Invisibility）**：排风口与交互口必须"齐平嵌入"（Flush）在两种材质交界的 G2 连续缝隙内，或极细的线性能量阵列（Linear Array），绝不破坏整体秩序。
      - **微观倒角强化法（Diamond-Cut Hardening）**：每一个机械按键、接口边缘，必须强制指定"0.5mm 钻石切边"或"CNC 铣削凹槽"，利用高亮边缘（Specularity Highlight）在 Lovart 模型中逼出极度真实的精密工业感。
      详见 `references/guides/prompt-engineering.md` 方法22。
13. `STEP-13` 形成三个完整且可追溯的 DesignIR。**新增字段**：`primary_contact_points`（主要接触点）、`interaction_nodes`（交互节点）、`cultural_hybrid`（文化杂交，可选）。
14. `STEP-14` 通过审美质量门并证据化排序。**新增识别性设计检查**：在八项质量门基础上，增加识别性设计检查（标志性形态、标志性细节、材料对比、比例记忆）。参考 `references/guides/identity-design.md`。识别性评分需 ≥ 8/10。**新增视觉语言一致性检查**：三个方向的提示词必须共享同一视觉语言基础（悬浮感、背景、焦点、摄影语法、负面约束、材料精确度、几何精确度）。参考 `references/guides/prompt-engineering.md`。

## 表达与评审

15. `STEP-15` 为三个完整方向分别生成追溯记录和压缩提示词。默认在三段提示词交付后停止；只有用户在当前请求中明确要求出图时，才进入图片生成与评审循环。**KB 反向链接（仅供提示词写作参考,严禁直接复制进 PromptBundle 破坏 prompt-contract 字符边界）**: `references/knowledge-base/02-设计方法论/02-Prompt协议.md`(关系命题/材料职责/触觉节点/时间检查的完整 Prompt 协议)+ `references/knowledge-base/07-视觉语料库/01-图像提示词库.md`(12 个产品的完整图像提示词语料,提供句式/词汇参考)+ `references/knowledge-base/08-优秀提示词搜集/02-进阶指南.md`(Prompt 进阶方法)+ `references/knowledge-base/08-优秀提示词搜集/03-实战模板.md`(8 个实战模板)+ `references/knowledge-base/附录Y-AI生成应用指南.md`(AI 生成应用与边界提示)。
    - **STEP-15.5 [NEW · 2026-06-24 {{skill_version}}] 五维工业级提示词架构（5-Stage Industrial Prompt Schema）**：提示词必须放弃散文式叙述，强行切换为以下五维结构。注意：内部推理可使用 `[Layout Block X: ...]` 作为思维框架，但**最终输出必须删除所有 `[Layout Block X: ...]` 标记**，只保留内容，用空行分隔段落。详见 `references/cases/pitfall-048-code-block-text-marker-leak.md`。
      1. **阶段一：功能原型与轴向主量体（Functional Archetype & Axis）**：开篇第一句必须由"相机设置 + 明确的产品原型词（Archetype）"组成。用几何语言和物理方位词，明确界定"主驾驶/操作区"和"动力/功能输出源"，确立视觉重心与方向感。**注意：此处的"原型词"是物理功能原型（如 manned flight vessel / espresso machine），不是品牌语境词。品牌语境必须移至阶段四处理。** 泛化公式：`Studio photograph of a [明确产品原型], featuring a highly visible [核心功能组件] defining its front orientation...`
      2. **阶段二：多材质职责链与对撞纹理（CMF Interlocking & Micro-Textures）**：严格禁止单一材质。必须采用"自然纹理"与"科技精密纹理"的交织对撞。使用 Lovart 模型最敏感的机械加工术语（CNC 微铣削、激光蚀刻渐变、注浆成型）来"逼出"细节。泛化公式：`Primary body made of [自然/哑光材质 + 微观纹理], directly interlocking with a secondary [精密金属/科技材质] accented by [微观科技纹理]...`
      3. **阶段三：3D 立体光学结构（Volumetric Lighting Structures）**：严禁使用 `flat LED light` 等平面词汇。必须引入"光学介质"与"实体结构"。将光线描述为被包裹在"三维光导管（3D light-pipe）"、"石英折射棱镜（refractive quartz prism）"或"带微幅槽线的立体腔体"内部的物理实体。泛化公式：`A recessed 3D linear light-guide tube, encased inside a micro-grooved frosted crystal channel, emitting a controlled, volumetric soft amber architectural glow...`
      4. **阶段四：设计谱系控制与反文字污染（Debranded Lineage Control）**：将具体品牌词 `LoveFrom 2030` 替换为抽象作画风格描述语，并加入严厉物理去品牌化指令。泛化公式：`...reflecting the pure minimalist design lineage of Jony Ive's aesthetic philosophy, strictly debranded, absolute zero alphanumeric text, no printed logos, seamless pristine surfaces.`
      5. **阶段五：地面锚定与硬表面环境闭塞（Grounding & Hard-Surface AO）**：通过具体物理悬浮高度/接触缝隙与地面材质，强迫模型计算出精密高亮边界与浓重环境光闭塞（AO）阴影。
      详见 `references/guides/prompt-engineering.md` 方法23。
    - **STEP-15.6 [NEW · 2026-06-24 {{skill_version}}] 反纯粹抽象与功能 Legible 质量门**：在提示词编译阶段强制追加以下校验：
      1. **拦截品牌词污染**：禁止直接向 Prompt 输出 "LoveFrom"、"Apple" 或任何具体年份数字。必须编译为：`reflecting the pure minimalist design lineage of Jony Ive's aesthetic philosophy, strictly debranded, absolute zero alphanumeric text`。
      2. **材质丰富度对撞要求**：每个方案的 CMF 表达必须至少包含 1 种天然/珩磨纹理（如 honed basalt, water-honed grain）与 1 种微观机械科技纹理（如 laser-etched gradient micro-grooves, micro-knurled patterns）在几何边界处的机械交叠。
      3. **禁止平面发光层**：全面废除 "LED line"、"glowing strip" 等词汇。必须强制编译为 3D 立体光学结构，指定具体物理容纳腔体与光学折射介质（如: recessed 3D linear light-guide tube encased inside a micro-grooved frosted quartz channel）。
      4. **原型 Legibility 校验**：提示词第一段必须明确描述定义该产品核心功能的关键宏观大部件与轴向（如飞行器的全景舱门与推进矢量轴），确保 Lovart 模型第一眼生成正确的物理功能原型。
      详见 `references/cases/pitfall-060-debranding-and-legibility.md`。
    - **STEP-15.7 [NEW · 2026-06-24 {{skill_version}}] 高秩序工业细节加载协议（High-Order Industrial Detail Loading Protocol）**：针对复杂工业系统（医疗设备、精密仪器、重型机械），禁止产品表面"绝对虚无"。必须引入三级细节加载，将"克制"重新定义为"复杂被秩序收束"，而非"空白"。详见 `references/guides/prompt-engineering.md` 方法24-26。三级细节：
      1. **认知状态指示层（Cognitive State UI）**：人机交互界面必须以"与材料表面完全平齐的、无缝集成的、微观排印的控制矩阵"形式融入产品。措辞：`Flush-integrated micro-typographic control zones embedded seamlessly into the surface. High-density micro-perforated dynamic display flush with the outer skin, exhibiting no decorative ornament when dormant.`
      2. **法律与工程信任标签（Regulatory & Engineering Veracity）**：微型、激光雕刻、极高排印秩序的刻度线、警告图标、设备型号铭牌。措辞：`Sub-millimeter laser-etched scale markings, warning typography, and functional indicators aligned to a strict engineering grid, maintaining absolute typographic restraint.`
      3. **制造工艺接口（Manufacturing Interface Detail）**：极其克制的零间隙接缝（0.3mm flush seams）、功能性丝印、盲用触觉定位点。措辞：`0.3mm tight engineering gaps, flawless structural split-lines serving as functional division of materials, precise parting lines showing uncompromising manufacturing rigor.`
      4. **禁止绝对虚无**：提示词中必须包含至少一个上述三级细节层，不得只写 "no text, no logo" 后留空。
    - **STEP-15.9 [NEW · 2026-06-25 {{skill_version}}] 五段式权重重组架构（Five-Layer Weighted Prompt Architecture）**：STEP-15 的输出结构必须严格重组为五大独立层级，按以下权重比例组织词组：
      - **Layer A: 摄影环境与体量尺度控制 (Weight: 20%)** — 严禁在大件设备上使用小品级 studio 词汇。根据产品物理尺度动态选择摄影语料：
        - 小型器物（< 30cm）：`Studio photograph, three-quarter view, macro detail shot`
        - 中型设备（30cm - 1.5m）：`Studio photograph, three-quarter view, medium shot`
        - 大型设备（> 1.5m）：`Architectural-grade studio composition, medium-long shot with orthogonal precision, grand volumetric presence`
      - **Layer B: 拓扑原型与主几何秩序 (Weight: 30%)** — 锁死品类基本功能拓扑，维持物种视觉主体体量权重（Volume Weight > 40%）。必须包含：品类锚定词 + 不可缩减三大特征 + 主几何关系描述。
      - **Layer C: 高秩序微观细节与丝印系统 (Weight: 15%)** — 规定丝印、按键、UI 在材料拓扑内的网格化存在状态。必须包含至少一个三级细节层（方法24-26）。
      - **Layer D: 尺度材料职责与时间老化 (Weight: 20%)** — 基于 [material] for [specific function] 语法的三问闭环描述。必须区分：结构材料（刚性/屏蔽/承载）+ 交互材料（触觉/情感）+ 隐蔽接口材料（ unseen / aging）。
      - **Layer E: 光影控制与复杂性负向排除 (Weight: 15%)** — 排除不受控的装饰噪音。禁止一刀切否定词（no text/no logo），改用"高秩序收束"描述（如 `whispered rather than screamed`）。
      详见 `references/guides/prompt-engineering.md` 方法27（五段式权重重组）。
    - **STEP-15.10 [NEW · 2026-06-25 {{skill_version}}] 防御性决策树（Fail-Safe Verification Gate）**：在最终输出提示词前，必须运行以下自动化审计分支逻辑：
      - **规则1**：IF (Prompt 包含 "No text" OR "No logo") AND (Brief 属于高精密/医疗/工业品类) → 强制删除该绝对化否定词，重新调用【功能细节密度矩阵】，补齐 `flush-integrated micro-typographic text indicators` 描述。
      - **规则2**：IF (Prompt 包含 "travertine" OR "obsidian" OR "walnut" OR "marble") AND (Brief 物理尺度 > 1.5m) → 强制拦截桌面级高端家居材质词，重新调用【大型设备材料职责库】，强制替换为 `medical-grade non-porous ceramic matrices` 或 `precision bead-blasted performance alloys`。
      - **规则3**：IF (Prompt 缺少品类原型结构描述) → 强制打断，提取 Brief 中的原始物理拓扑名词，将 [A][B][C] 原型结构作为第一主语强行插入 Layer A 与 Layer B 中。
      详见 `references/guides/fail-safe-verification-gate.md`。
    - **STEP-15.8 [NEW · 2026-06-24 {{skill_version}}] 材料职责诚实性校验（Material Responsibility Honesty Check）**：禁止将建筑/家具材料（travertine, walnut, marble）用于重型精密医疗设备的外壳。材料必须承担功能职责，不能仅表达"高级感"。重型设备外壳必须使用工程复合材料、高刚性合金或医用级高分子，并指定具体工业精加工工艺。例如：❌ "travertine base" → ✅ "bead-blasted matte engineering composite enclosure, 40mm wall thickness, providing electromagnetic shielding and structural rigidity"。详见 `references/cases/pitfall-061-material-responsibility-violation.md`。

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
- **视觉等效洗涤（Visual Equivalent Wash）**：STEP-12 材料职责矩阵中的工程账本数据（寿命、制造方式、维护方式）**禁止直接注入提示词**。必须通过视觉等效编译转化为光学物理表征（IOR/Roughness/Anisotropy/Micro-texture）。详见 `references/guides/prompt-engineering.md` 方法17。
- **尺度缩放滤网（Scale Zoom Filter）**：宏观体量产品（载具/家具）自动抑制微观尺寸（<1mm），泛化为对比级视觉信号（hairline shadow line / high-contrast alignment split）。详见 `references/guides/prompt-engineering.md` 方法18。
- **语义洗涤器（Semantic Sanitizer）**：提示词编译阶段强制过滤意识形态/艺术流派名词和情感暗示词。详见 `references/cases/pitfall-056-semantic-mimicry.md`。
- **品类动态排除词（Category Dynamic Exclusion）**：根据 brief 品类自动绑定动态排除词，写入 Layout Block 5。详见 `references/cases/pitfall-058-category-dynamic-exclusion.md`。
- **原型锚定与拓扑保护（Archetype Anchor & Topological Protection）**：复杂工业系统必须在提示词第一段保留品类原型词（如 MRI scanner / espresso machine / drone），禁止用纯几何体（slab/cube/cylinder）完全替代。详见 `references/guides/archetype-verification.md`。
- **高秩序工业细节加载（High-Order Industrial Detail Loading）**：复杂工业系统必须在提示词中包含至少一个三级细节层（认知状态UI / 工程信任标签 / 制造工艺接口），禁止产品表面"绝对虚无"。详见 `references/guides/prompt-engineering.md` 方法24（认知状态UI层）、方法25（工程信任标签层）、方法26（制造工艺接口层）。
- **材料职责诚实性（Material Responsibility Honesty）**：重型设备必须使用工程复合材料/高刚性合金/医用级高分子，禁止用建筑/家具材料（travertine/walnut/marble）。详见 `references/cases/pitfall-061-material-responsibility-violation.md`。
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
Studio photograph, [精确视角，如 three-quarter view slightly above / eye-level dead-front view], of a single [产品中性核心词], [设计谱系描述，如 reflecting the pure minimalist design lineage of Jony Ive's aesthetic philosophy], shot on 35mm lens, pristine gallery lighting.

[Layout Block 2: 核心拓扑与交接关系 (Visualized Intersect)]
A solid [构件A材质] slab [物理交接动作，强制使用：recessed flush into / hovering exactly 10mm above with visual airgap / piercing through] a [构件B材质] base. Material transition controlled by absolute geometric alignment.

[Layout Block 3: 极致几何与切线控制 (Micro-Geometry)]
G2 fillet edges, sweeping tangent into surfaces, [微观物理交接线，强制使用：0.3mm crisp hairline split-line / zero-tolerance sealed joint / continuous unbroken perimeter shadow].

[Layout Block 4: 消失设计与行为触点 (Vanishing Element)]
Integrated tactile surface node for human interface, flush with the main body, perfectly vanishing when not in use. Light interaction defines the forms. Shadow reveals the negative spaces. Neutral uniform gradient background.

[Layout Block 5: 绝对排除项 (Negative Filter)]
No text, no branding, no visible screws, no status icons, no cybernetic patterns, no sci-fi mechanical ribbing, no background props, no ground reflections, no decorative lines.
```

**V3.0 升级说明（2026-06-24 {{skill_version}}）**：
- Block 2 材质职责 → 核心拓扑与交接关系（Visualized Intersect），强制使用物理交接动作词（recessed flush into / hovering exactly 10mm above with visual airgap / piercing through）
- Block 3 精确微观尺寸 → 微观物理交接线（强制使用 hairline split-line / zero-tolerance sealed joint / continuous unbroken perimeter shadow），避免宏观体量与微观尺寸语义冲突
- Block 4 Floats → 消失设计与行为触点（Vanishing Element），用"Light interaction defines the forms"替代"Floats"，避免水面漂浮次生幻觉
- Block 5 新增 `no cybernetic patterns, no sci-fi mechanical ribbing, no background props, no ground reflections, no decorative lines`

**禁止词滤网（绝对禁止进入Prompt）**：
- ❌ futuristic, sleek, cybernetic, sci-fi, high-tech
- ❌ Apple-like, minimalist design, Jony Ive style
- ❌ sense of safety, feeling of trust, emotional connection
- ❌ spinning slowly, gently hovering, gracefully flying
- ❌ white matte plastic shell, transparent glass window（材料贴图化）
- ❌ 意识形态/艺术流派名词（侘寂、赛博朋克、孟菲斯、极简主义）
- ❌ 情感暗示词（手工感、温暖感、陌生感、充满信任）

**材料职责强制格式**：材料名称 | 结构职责 | 触感职责 | 制造方式 | 寿命 | 维护方式

**新增"不被看见的部分"强制描述**：底面接合线、铰链、进气口边缘倒角、隐藏接口等必须在Layout Block 2或Block 4中描述。

材料描述必须使用"材料职责"格式：材料名称 | 结构职责 | 触感职责 | 制造方式 | 寿命 | 维护方式。

- **视觉等效编译强制要求**：compile_prompt.py 在编译时自动执行视觉等效洗涤（方法17）和尺度缩放滤网（方法18），将材料职责转化为光学物理表征，删除工程噪音词。
- **多材质职责链解耦（Material Duty Chain Decoupling）**：严禁单一材质统领全身。必须强制遵守"三元材质重叠律"：① 主壳体材质必须指定具体工业精加工工艺；② 接口与交互组件必须指定至少2个具体机械部件并说明装配关系；③ 流体转换组件必须指定与主壳体对比的次级功能材质并明确几何秩序收束方式。详见 `references/guides/prompt-engineering.md` 方法21。
- **功能性孔口与秩序收束（Aperture & Order Integration）**：按键、交互口、出风口、排风口必须被物理几何秩序收束。缝隙隐匿法（Flush 嵌入 G2 连续缝隙）+ 微观倒角强化法（0.5mm 钻石切边 / CNC 铣削凹槽）。详见 `references/guides/prompt-engineering.md` 方法22。
- **CMF 丰富度与组件真实性质量门**：提示词必须包含 ≥3 种相交材质，每种材质指定具体加工工艺词汇（如 bead-blasted / CNC-milled / diamond-cut）。若未满足，系统拒绝输出并重写。

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
