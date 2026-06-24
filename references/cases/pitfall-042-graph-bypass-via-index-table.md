---
reference_id: PITFALL-042
title: Pitfall 042 · KB 不进 graph 但通过索引表实现闭环
category: case
used_when:
  - KB-MIRROR
  - REFERENCE-GRAPH
  - EXTERNAL-KB-SYNC
called_by:
  - skill-router
  - upstream-knowledge-curator
depends_on:
  - REF-HYGIENE-001
  - REF-GUIDE-MIRROR
  - PITFALL-041
outputs:
  - graph_workaround_pattern
---

# Pitfall 042 · KB 不进 graph 但通过索引表实现闭环(graph-bypass-via-index-table)

> **触发版本**:jony-ive-design2me-v2
> **触发日期**:2026-06-22
> **触发场景**:KB 镜像 28 篇原文 + README,SHA256SUMS 都是合法的 KB 文件,**但**它们的 frontmatter / forbidden-text 检查与"running reference"的预期不符。试图让 KB 28 篇都进 graph 会触发 fail-fast 在前置无 frontmatter 文件(cases/iterations 部分文件)抛错。
> **正解**:KB **不进 graph**,但通过 `references/README.md` 总索引表 + `step-reference-map.md` 路径存在性校验实现完整闭环。

## 症状

尝试让 KB/README.md 进 `load_reference_graph` 时:

```python
graph = load_reference_graph('.')
# ValueError: 缺少 YAML frontmatter
# (fail-fast 在 cases/pitfall-005-category-deadlock.md 处抛错,根本走不到 KB)
```

即使加白名单让 KB README 通过,KB 28 篇原文仍无 frontmatter,且包含 FORBIDDEN_RUNTIME_TEXT(`LoveFrom 2030` / `Mobile Documents` 等真实 case-study 文字),不能进 graph。

## 根因(诚实反查)

| 占比 | 原因 |
|---|---|
| **40%** | graph 加载是 fail-fast 设计,任何前置文件失败都会阻断整个 graph 构建 |
| **30%** | KB 原文按设计不能加 frontmatter(违反 0 改写原则)和 humanizer(违反"不要优化") |
| **20%** | KB 原文包含真实 case-study 引用(`LoveFrom 2030` 是 Terra Carta Initiative 的真实时间点,`Mobile Documents` 是 Obsidian 路径)——在 running reference 里被禁,在 KB 原文里合法 |
| **10%** | 没有"上游镜像 vs 运行 reference"的明确边界定义 |

## 完成定义(正解)

KB 不进 graph,但**完整闭环**通过 4 个机制实现:

### 1. references/README.md 总索引表加 `REF-KB-INDEX` 行

```markdown
| REF-KB-INDEX | [艾维知识蒸馏库(上游参考)总索引](../knowledge-base/README.md) | 用户 Obsidian 知识库...完整保留用户原始文字... |
```

`_index_issues` 函数通过字符串匹配验证路径存在性,不依赖 graph 加载。

### 2. step-reference-map.md 加 REF-KB-INDEX 到关键 STEP

```markdown
| STEP-01 | REF-EVIDENCE-001, ..., REF-KB-INDEX |
| STEP-02 | ..., REF-KB-INDEX |
| STEP-03 | ..., REF-KB-INDEX |
| STEP-08 | ..., REF-KB-INDEX |
| STEP-15 | ..., REF-KB-INDEX |
```

### 3. end-to-end-workflow.md 各 STEP 加 KB 反向链接

每个 STEP 描述里嵌入 `**KB 反向链接**: \`references/knowledge-base/...\`` 段。

### 4. 运行 reference 反向链接 KB 关键节点

| reference | KB 链接 |
|---|---|
| `failure-library.md` | 附录X + 误用风险 + 辅助案例 + 背景案例 |
| `ive-thinking-models.md` | 核心16法 + 世界观 + 设计哲学 + 五维联动 + 核心案例 + 深化判断 |

## 验证方法

### 闭环检查(本会话已通过)

| 检查项 | 结果 |
|---|---|
| SKILL.md 启动顺序含 KB 路由指针 | ✅ |
| step-reference-map.md 5 STEP 引用 REF-KB-INDEX | ✅ |
| end-to-end-workflow.md 9 STEP 含 KB 反向链接 | ✅ 19 处 |
| 运行 reference 含 KB 反向链接 | ✅ 19 处 |
| KB 28/28 原文 sha256 一致 | ✅ |

### 验证脚本

```bash
# KB 路径 0 失败 = 闭环生效
python3 scripts/validate_skill.py . 2>&1 | grep "knowledge-base" | wc -l  # 0
python3 scripts/validate_reference_graph.py . 2>&1 | grep "knowledge-base" | wc -l  # 0
python3 scripts/audit_references.py . SOURCE_LEDGER.csv 2>&1 | grep "knowledge-base" | wc -l  # 0
```

## 教训

1. **graph 不是闭环的唯一载体**——索引表的字符串匹配 + 文件存在性已经能保证路径有效
2. **fail-fast 应当允许部分加载**——`load_reference_graph` 应该 try/except per-file 而不是整个图抛错
3. **KB 与 running reference 必须明确边界**——README.md 是 KB 内部元数据,可以注册为 `REF-KB-INDEX`;KB 28 篇原文**永远不**注册为 running reference

## 决策表

| KB 类型 | frontmatter | graph 注册 | 索引表 | STEP 引用 |
|---|---|---|---|---|
| KB/README.md(元数据) | ✅ 可加 | ❌ 因 fail-fast 不进 | ✅ REF-KB-INDEX | ✅ STEP-01/02/03/08/15 |
| KB/SHA256SUMS.txt(校验) | ❌ | ❌ | ❌ | ❌(工具文件) |
| KB/28 篇原文 | ❌ 0 改写 | ❌ | ❌ | ✅ 反向链接到具体 STEP |

## 关联

- 修复记录: jony-ive-design2me-v2 changelog
- 上游协议: `references/guides/external-knowledge-mirror-integration.md`
- Pitfall 040: 内容镜像未接入引用闭环
- Pitfall 041: 验证脚本僵化报"计划外 reference"