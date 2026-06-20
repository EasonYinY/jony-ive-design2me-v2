---
reference_id: REF-CASE-001
title: 可运行案例胶囊
category: core
used_when:
  - STEP-03
  - STEP-08
  - STEP-14
called_by:
  - product-design
  - design-philosophy
depends_on:
  - REF-EVIDENCE-001
  - REF-IVE-001
outputs:
  - case_method_anchors
---

# 可运行案例胶囊

## 用途与边界

案例胶囊用于证明方法如何在特定条件中成立，不是形态、材料、尺寸、品牌符号或提示词模板。运行时只能迁移“如何判断”，不能复制“案例做成了什么样”。

## FCT-001 Sailing Lantern

- 证据类型：`FACT`。
- 证据等级：`S`，BALMUDA 官方项目页。
- 来源指针：https://www.balmuda.com/lovefrom-balmuda/ ；source-index.md 中 SL-S-002
- 已确认事实：官方页确认可维护、拆解、修理与回收，以及单旋钮的亮度和色温控制。
- 可迁移方法：将环境边界、操作反馈和维护路径一同写入产品命题。
- 适用条件：仅用于 Sailing Lantern 案例事实和方法抽取
- 反例：把“航海”降格为造型或复古意象，不核对环境和维护条件。
- 禁止外推：不得将其材料指标控制方式或限量策略复制到新产品

## FCT-002 Linn LP12-50

- 证据类型：`FACT`。
- 证据等级：`S`，Linn 官方产品页。
- 来源指针：https://www.linn.co.uk/us/turntables/lp12-50 ；source-index.md 中 LP-S-001
- 已确认事实：官方页确认 LoveFrom 合作、250 台限量以及特定构件和材料。
- 可迁移方法：对成熟产品先识别高频接触点和系统约束，再决定是否需要改变整体架构。
- 适用条件：仅用于 LP12-50 案例事实和长期产品更新方法
- 反例：为了显示新鲜而否定经验证的产品架构，或把限量本身当成设计质量。
- 禁止外推：不得把限量或铝制构件写成 Ive 通用处方

## FCT-003 Terra Carta Seal

- 证据类型：`FACT`。
- 证据等级：`S`，Sustainable Markets Initiative 官方材料。
- 来源指针：https://www.sustainable-markets.org/news/19-companies-awarded-the-terra-carta-seal-in-recognition-of-their-commitment-to-creating-a-sustainable-future/ ；source-index.md 中 TC-S-003
- 已确认事实：官方材料确认 Ive / LoveFrom 的设计参与以及多种自然元素。
- 可迁移方法：复杂语义可以通过层级、边界、排版和使用规则被收束，而不是一律删除。
- 适用条件：仅用于 Terra Carta Seal 事实与公共图形系统分析
- 反例：只以纹样密度或装饰精细度评价公共图形，忽略授予、承诺与识别功能。
- 禁止外推：不得复制 oak leaves fern magnolia honeybees 等具体图形

## FCT-004 OpenAI / io 合作边界

- 证据类型：`FACT`。
- 证据等级：`S`，OpenAI 官方公告。
- 来源指针：https://openai.com/sam-and-jony/ ；source-index.md 中 OI-S-001
- 已确认事实：官方公告只确认 io 团队与 OpenAI 的关系，以及 LoveFrom 保持独立并承担设计与创意责任。
- 可迁移方法：把合作关系、责任分工和信息缺失本身作为设计边界。
- 适用条件：仅用于合作事实和未发布产品边界
- 反例：从人物照片、合作用语、媒体泄露或所谓“反屏幕”立场推导产品。
- 禁止外推：不得推断任何外观尺寸材料交互屏幕或佩戴方式
- 停止条件：无公开产品证据时停止；不生成产品 Design IR 或正向形态提示。

## FCT-005 Airbnb 与 LoveFrom

- 证据类型：`FACT`。
- 证据等级：`S`，Airbnb 官方公告。
- 来源指针：https://news.airbnb.com/designing-the-future-of-airbnb/ ；source-index.md 中 AF-S-001
- 已确认事实：官方公告确认合作范围包括产品、服务和 Airbnb 内部设计团队的发展。
- 可迁移方法：在服务与组织设计中，交付物可以包括决策方式、团队能力和持续运作机制。
- 适用条件：用于服务和组织设计案例
- 反例：把组织合作简化为界面改版，或将合作方团队的成果全部归因于 LoveFrom。
- 禁止外推：不得把后续 Airbnb 的具体产品变化默认归因于 LoveFrom

## FCT-006 LoveFrom, Moncler

- 证据类型：`FACT`。
- 证据等级：`S`，Moncler 官方页。
- 来源指针：https://www.moncler.com/en-us/stories/lovefrom-moncler-collection ；source-index.md 中 MON-S-001
- 已确认事实：官方页确认三种 shell 与 central Moncore 构成模块化穿着系统。
- 可迁移方法：在身体与场景会变化的任务中，可先分离稳定主体与可变接口层，再检验连接与反馈。
- 适用条件：仅用于 Moncler 案例的身体与接口关系
- 反例：未定义身体动作、连接安全和场景变化，就为了可换外观强行模块化。
- 禁止外推：不得将 shell-core 具体结构复制到其他穿戴或硬件品类

## FCT-007 Coronation Emblem

- 证据类型：`FACT`。
- 证据等级：`S`，The Royal Family 官方使用规范。
- 来源指针：https://www.royal.uk/sites/default/files/documents/2023-05/coronation_2023_emblem_usage_guidelines_0-2.pdf ；source-index.md 中 CE-S-002
- 已确认事实：官方使用规范包含尺度、留白、色彩和禁止变形规则。
- 可迁移方法：将图形和它被正确使用的系统规则视为同一份设计产物。
- 适用条件：用于公共图形系统规范方法
- 反例：标志单独看成立，但在小尺寸、数字、商品或共存场景中因无规则而失真。
- 禁止外推：不得复制皇室符号色彩或具体构图

# 待核验队列

下列内容仅保留为证据回查线索，不得作为正向案例规则：

- `AUD-001`至 `AUD-008`、`AUD-023`至 `AUD-026`：旧产品案例和修正链，尚未通过公开证据逐条核验。
- `AUD-032`：旧真实案例摘要，原有等级不继承，只能回到公开来源重新确认。
