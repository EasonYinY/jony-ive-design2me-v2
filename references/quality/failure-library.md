---
reference_id: REF-QUALITY-003
title: 图片失败库
category: quality
used_when:
  - STEP-08
  - STEP-14
  - STEP-15
called_by:
  - product-design
  - image-critique
depends_on:
  - REF-EVIDENCE-001
outputs:
  - failure_findings
---

# 图片失败库

## 用途

失败库提供确定性分类，不提供正向造型处方。每项失败必须由可见现象与合同对照共同成立。

| 失败码 | 中文分类 | 判定信号 | 默认处理层级 |
|---|---|---|---|
| `structural_misread` | 结构误读 | 承力、连接、开合或模块边界与 `DesignIR` 冲突 | 退回产品推导 |
| `material_fabrication` | 材料伪造 | 图片用光效、纹理或无依据材质替换材料职责 | 退回产品推导 |
| `operation_invisible` | 操作不可见 | 已定义动作、顺序、状态或反馈未被图片表达 | 提示词或重渲染 |
| `direction_homogenization` | 方向同质化 | 三方向在关系、结构或操作上被生成成同一方案 | 退回产品推导 |
| `apple_shell` | Apple 外形套壳 | 以白色、圆角、金属或极简轮廓替代本方向逻辑 | 退回产品推导 |
| `unsupported_text_label` | 无依据文字标签 | 图片出现未由输入确认的品牌、规格、按钮或工艺文字 | 提示词或重渲染 |
| `resting_state_invisible` | 静息状态不可见 | 断电或停止使用时的构件位置、稳定性或状态可读性未被表达 | 提示词或重渲染 |
| `form_before_relation` | 形态先于关系 | 未先定义使用者动作就进入形态推导；关系模式直接对应已知产品形态 | 退回产品推导 |
| `material_without_duty` | 材料无职责 | 只写材料名称或颜色词，未说明结构/触感/制造/寿命/维护职责 | 退回产品推导 |
| `aesthetic_ratio_only` | 纯审美比例 | 比例数字无人体测量或工程约束依据，仅用"黄金比例""视觉平衡"等审美词 | 退回产品推导 |
| `color_as_premium` | 颜色词替代高级感 | 用"深岩灰""香槟金"等颜色词替代材料职责和工艺说明 | 退回产品推导 |
| `function_not_verified` | 功能未验证 | 形态无法完成核心功能，或关键构件（清洁/更换/维修）不可达 | 退回产品推导 |
| `background_intrusion` | 背景侵入 | 图片出现背景、环境、辅助物品、场景、人物、手、脸等除产品外的元素 | 提示词或重渲染 |
| `prompt_not_in_codeblock` | 提示词未用代码块 | 最终提示词未使用代码块显示，或未额外输出英文提示词 | 修订输出格式 |

## 证据边界

失败分类采用工程治理规则以及 `SOURCE_LEDGER.csv` 中 `BND-002`、`BND-003`、`VIS-003` 和 `AUD-009` 至 `AUD-022` 的待核验线索。待核验线索只用于发现可复现错误，不得被写成 Jony Ive 的公开理论。
