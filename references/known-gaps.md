---
reference_id: REF-GAPS-001
title: 已知缺失与待修复项
category: meta
used_when:
  - SKILL-AUDIT
  - SKILL-UPDATE
  - SKILL-SETUP
called_by:
  - skill-router
  - file-hygiene-check
depends_on:
  - REF-INDEX-001
  - REF-HYGIENE-001
outputs:
  - gap_inventory
---

# 已知缺失与待修复项

> **用途**: 当对 jony-ive-design2me-v2 进行审计、升级或修复时，先读取此文件确认当前已知的结构性问题。
> **更新规则**: 发现新问题 → 添加到此文件；修复完成 → 标记为 ✅ 并记录修复版本；不删除历史记录。

## 当前状态概览

| 优先级 | 类别 | 问题 | 状态 |
|---|---|---|---|
| 🔴 高 | 缺失文件 | SOURCE_LEDGER.csv | 待修复 |
| 🔴 高 | 缺失文件 | source-index.md | 待修复 |
| 🔴 高 | 外部依赖 | 01-核心研究/ 目录引用 | 待修复 |
| 🟡 中 | 缺失目录 | references/cases/ | 待创建 |
| 🟡 中 | 缺失目录 | references/rules/ | 待创建 |
| 🟡 中 | 缺失目录 | references/guides/ | 待创建 |
| 🟢 低 | 方法论 | 无 SECI 模型显式引用 | 可选增强 |
| 🟢 低 | 方法论 | 无 DSF 5层方向筛选 | 可选增强 |

## 🔴 高优先级：缺失文件

### SOURCE_LEDGER.csv

**影响范围**: evidence-policy.md, five-dimension-engine.md, failure-library.md, prompt-contract.md
**影响描述**: evidence-policy.md 规定"具体候选知识及状态以工程根目录的 SOURCE_LEDGER.csv 为准"
**建议修复**: 创建最小 CSV 文件，包含 claim_id, status, target_reference 等字段
**阻塞性**: 是 — audit_references.py 依赖此文件运行

### source-index.md

**影响范围**: ive-thinking-models.md (10 次), case-capsules.md (7 次)
**影响描述**: 来源指针引用 source-index.md 中的条目 ID（如 AF-S-001, MON-S-001 等）
**建议修复**: 创建来源索引，映射外部来源到本地引用
**阻塞性**: 是 — 方法快照和案例胶囊的来源追溯不完整

### 01-核心研究/ 目录

**影响范围**: ive-thinking-models.md (10 处引用)
**影响描述**: 技能承诺"运行知识为技能内置稳定快照，不依赖外部知识库路径"
**建议修复**: 将外部目录内容内嵌到 skill 的 references/ 中，或替换为本地引用
**阻塞性**: 是 — 违反自包含承诺

## 🟡 中优先级：缺失目录

### references/cases/

**用途**: 存放 pitfall 案例、失败模式、实证记录
**参考**: jony-ive-perspective V4.x 积累了 23+ pitfalls
**建议**: 创建目录并添加 README.md 索引

### references/rules/

**用途**: 存放硬编码规则、方法论框架、决策机制
**参考**: jony-ive-perspective V4.17 的 DSF 5层方向筛选框架
**建议**: 创建目录并添加 README.md 索引

### references/guides/

**用途**: 存放扩展指南、深度参考、外部权威摘录
**建议**: 创建目录并添加 README.md 索引

## 🟢 低优先级：可选增强

### SECI 模型引用

**背景**: 蒸馏skill 核心框架（社会化→外在化→组合化→内在化）
**当前状态**: 五维引擎(REF-FIVE-001) 有类似结构但无 SECI 显式引用
**建议**: 在 five-dimension-engine.md 中添加 SECI 映射说明

### DSF 5层方向筛选

**背景**: jony-ive-perspective V4.17 核心创新（第一性锚点→约束级联→反俗套扫描→六轴差异→先验失败扫描）
**当前状态**: design2me-v2 有方向筛选但无系统化方法论框架
**建议**: 考虑在 direction/ 目录下添加 DSF 参考文档

## 修复追踪

| 修复日期 | 修复版本 | 修复内容 | 验证方式 |
|---|---|---|---|
| 2026-06-21 | 当前版本 | 创建 SOURCE_LEDGER.csv | audit_references.py 通过 |
| 2026-06-21 | 当前版本 | 创建 source-index.md | 所有引用可解析 |
| 2026-06-21 | 当前版本 | 创建 references/core/design-methodology.md | validate_reference_graph.py 通过 |
| 2026-06-21 | 当前版本 | 修复 ive-thinking-models.md 中 10 处 01-核心研究/ 引用 | 全部指向本地文件 |
| 2026-06-21 | 当前版本 | 创建 references/cases/ 目录 + README.md | 目录存在，索引完整 |
| 2026-06-21 | 当前版本 | 创建 references/rules/ 目录 + README.md | 目录存在，索引完整 |
| 2026-06-21 | 当前版本 | 创建 references/guides/ 目录 + README.md | 目录存在，索引完整 |
| 2026-06-21 | 当前版本 | 修复 validate_skill.py 版本口令误报 | validate_skill.py 通过 |
| 2026-06-22 | 当前版本 | 创建 `references/knowledge-base/` 镜像目录(28 篇用户 Obsidian 知识库《乔纳森·艾维-知识蒸馏》旧版 · 737.2 KB · 28/28 sha256 字节级一致) | shasum 比对通过;validate_skill.py + validate_reference_graph.py 对 KB 路径 0 失败 |
| 2026-06-22 | 当前版本 | 加 `UPSTREAM_KB_DIR` 白名单到 validate_skill.py + validate_reference_graph.py,跳过 KB 目录的运行 reference 检查 | 验证脚本对 KB 0 失败,预存在 35 个失败项与 当前版本 baseline 一致 |
| 2026-06-22 | 当前版本 | file-hygiene.md 加第 7 条铁律:用户原文 0 简化原则(上游 KB 镜像协议) | 文档化,下次同步可直接套用 |
| 2026-06-22 | 当前版本 | SKILL.md 加 1-line 路由块指向 KB README + version 2.5.0→2.6.0 | 不污染 SKILL.md,只加指针 |
| 2026-06-24 | 当前版本 | 修复 6 个 README 断链 guides (audit-feedback-2026-06-24 + 5 个协议 stub) | README 索引验证通过 |
| 2026-06-24 | 当前版本 | 修复 6 处 reference_id frontmatter 冲突(REF-CASE-026/027/030/048/REF-GUIDE-013 -A/-B 后缀) | validate_reference_graph.py 0 duplicate |
| 2026-06-24 | 当前版本 | 删除 SOURCE_LEDGER.csv 中 3 行 phantom 登记 (BND-002/003/MTH-005 → cases/README.md) | audit_references.py 通过 |
| 2026-06-24 | 当前版本 | SKILL.md 瘦身 297 行 → 87 行(-71%),升级史全部移至 changelogs/ | 文件卫生铁律 3 落地 |
| 2026-06-24 | 当前版本 | check_version_pollution.py 45 处污染清零 + 8 个元文件加 ALLOWED_PATHS 白名单 | 0 处污染 |
| 2026-06-24 | 当前版本 | 创建 `scripts/verify-all.sh` 一键跑 4 个验证脚本(bash 3.2 兼容版) | verify-all.sh 输出 4 项 exit code 汇总 |
| 2026-06-24 | 当前版本 | 修复 _is_changelog_path 不识别 references/changelogs/ 前缀 bug | v1.3.1-changelog.md 不再被误报 |
| 2026-06-24 | 当前版本 | audit_references.py + validate_skill.py + check_version_pollution.py 版本号豁免语义统一 | 三脚本对 case/process/user-prefs 元文件一致豁免 |
| 2026-06-24 | 当前版本 | 新增 pitfall-049 (批量版本号替换破坏上下文) + pitfall-050 (空目录误判) + pitfall-051 (bash 3.2 兼容) | 三类新陷阱已记录,下次同类修复时不再重蹈 |

## 修复后状态概览

| 优先级 | 类别 | 问题 | 状态 |
|---|---|---|---|
| 🔴 高 | 缺失文件 | SOURCE_LEDGER.csv | ✅ 已修复 |
| 🔴 高 | 缺失文件 | source-index.md | ✅ 已修复 |
| 🔴 高 | 外部依赖 | 01-核心研究/ 目录引用 | ✅ 已修复 |
| 🟡 中 | 缺失目录 | references/cases/ | ✅ 已创建 |
| 🟡 中 | 缺失目录 | references/rules/ | ✅ 已创建 |
| 🟡 中 | 缺失目录 | references/guides/ | ✅ 已创建 |
| 🟢 低 | 方法论 | 无 SECI 模型显式引用 | 可选增强 |
| 🟢 低 | 方法论 | 无 DSF 5层方向筛选 | 可选增强 |
