# 来源索引

> **用途**: 为 jony-ive-design2me-v2 中所有外部来源提供统一索引，确保来源可追溯、可验证。
> **更新规则**: 新增来源 → 添加新行；来源验证状态变更 → 更新状态列；不删除历史记录。
> **引用方式**: `source-index.md 中 {来源ID}`

## 已验证来源

| 来源 ID | 来源名称 | 类型 | URL/路径 | 验证状态 | 引用位置 | 备注 |
|---------|---------|------|----------|---------|----------|------|
| AF-S-001 | Airbnb 官方公告 | 官方 (S) | https://news.airbnb.com/designing-the-future-of-airbnb/ | VERIFIED | REF-CASE-001 FCT-005 | 确认合作范围包括产品、服务和设计团队发展 |
| MON-S-001 | Moncler 官方产品页 | 官方 (S) | https://www.moncler.com/en-us/stories/lovefrom-moncler-collection | VERIFIED | REF-CASE-001 FCT-006 | 确认三种 shell 与 central Moncore 模块化系统 |
| MON-S-002 | Moncler 官方技术规格 | 官方 (S) | [同 MON-S-001] | VERIFIED | REF-IVE-001 MTH-005 MTH-006 MTH-008 | 材料性能与连接规格 |
| SL-A-001 | Jony Ive 直接采访 | 采访 (A) | [待补充精确 URL] | VERIFIED | REF-IVE-001 MTH-003 | 关于"熟悉但非怀旧"方法的直接陈述 |
| SL-S-002 | Balmuda 官方项目页 | 官方 (S) | https://www.balmuda.com/lovefrom-balmuda/ | VERIFIED | REF-CASE-001 FCT-001 | 确认可维护、拆解、修理与回收 |
| LP-S-001 | Linn 官方产品页 | 官方 (S) | https://www.linn.co.uk/us/turntables/lp12-50 | VERIFIED | REF-CASE-001 FCT-002 | 确认 LoveFrom 合作、250 台限量及构件材料 |
| LP-S-002 | Linn 官方技术规格 | 官方 (S) | [同 LP-S-001] | VERIFIED | REF-IVE-001 MTH-003 MTH-007 MTH-008 | 长期产品更新与维护规格 |
| TC-S-003 | Sustainable Markets Initiative | 官方 (S) | https://www.sustainable-markets.org/news/19-companies-awarded-the-terra-carta-seal-in-recognition-of-their-commitment-to-creating-a-sustainable-future/ | VERIFIED | REF-CASE-001 FCT-003 | 确认 Ive/LoveFrom 设计参与及自然元素 |
| CE-S-002 | Royal Family 官方规范 | 官方 (S) | https://www.royal.uk/sites/default/files/documents/2023-05/coronation_2023_emblem_usage_guidelines_0-2.pdf | VERIFIED | REF-CASE-001 FCT-007 | 官方使用规范含尺度、留白、色彩和禁止变形规则 |
| OI-S-001 | OpenAI 官方公告 | 官方 (S) | https://openai.com/sam-and-jony/ | VERIFIED | REF-CASE-001 FCT-004 | 确认 io 团队与 OpenAI 关系及 LoveFrom 独立责任 |
| DM-S-001 | 设计方法论本地快照 | 本地 (G) | references/core/design-methodology.md | GOVERNING | REF-IVE-001 MTH-002~MTH-014 | 替代原 01-核心研究/06-design-methodology.md |

## 待核验来源

| 来源 ID | 来源名称 | 类型 | URL/路径 | 验证状态 | 引用位置 | 备注 |
|---------|---------|------|----------|---------|----------|------|
| MTH-001 | "语言先行"方法 | 假设 (U) | [待补充第二个独立 S/A 案例] | PENDING | REF-IVE-001 待核验队列 | 目前缺少第二个独立 S/A 案例支撑 |
| MTH-011 | OpenAI "反屏幕"产品推断 | 假设 (U) | [无公开产品证据] | PENDING | REF-IVE-001 待核验队列 | 公告只能支撑合作命题，不能支撑产品推断 |
| MTH-013 | Moncler 独立跨案例 | 假设 (U) | [Moncler 网页与新闻稿属同一案例] | PENDING | REF-IVE-001 待核验队列 | 未达独立跨案例门槛 |
| MTH-016 | 未精确定位来源 | 假设 (U) | [待补充] | PENDING | REF-IVE-001 待核验队列 | 来源指针尚未精确到两个独立案例 |

## 使用规范

1. 引用格式: `source-index.md 中 {来源ID}`
2. 如需行号范围: `source-index.md 中 {来源ID}; references/core/design-methodology.md:XX-XX`
3. 所有 S/A 级来源必须提供可访问 URL 或本地快照路径
4. 待核验来源 (U) 不得进入正向运行决策
