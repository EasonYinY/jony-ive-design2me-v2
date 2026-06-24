---
reference_id: REF-CASE-048-A
title: Pitfall 048-A - 代码块 text 标记泄漏到提示词
category: cases
supersedes_id_was: REF-CASE-048
disambiguation_note: 原 REF-CASE-048 与 pitfall-048-backup-skill-illusion.md 冲突(后者日期更早,留为权威)。本文件分配 -A 后缀。
category: cases
used_when:
  - STEP-15
  - PROMPT-OUTPUT
called_by:
  - prompt-compression
  - prompt-contract
depends_on:
  - REF-PROMPT-002
  - REF-PROMPT-004
outputs:
  - failure_pattern
  - fix_recipe
---

# Pitfall 048: Code Block `text` Marker Leaking into Prompt

> **日期**: 2026-06-24
> **触发**: 用户反馈"提示词的前面为什么会有个text 的单词？这个会严重影响出图质量"
> **严重级别**: HIGH — 直接影响 AI 图像生成质量

## 现象

当使用 Markdown 代码块（```）包裹提示词输出时，如果错误地使用了带语言标记的代码块（```text），`text` 这个词会被保留在提示词内容中，导致：

```
❌ 错误输出（text 泄漏）:
```text
Studio photograph, three-quarter view slightly above...
```
→ AI 实际接收: "text Studio photograph, three-quarter view slightly above..."
→ 结果: 可能生成与"文字""文本"相关的错误内容

✅ 正确输出（无标记）:
```
Studio photograph, three-quarter view slightly above...
```
→ AI 实际接收: "Studio photograph, three-quarter view slightly above..."
→ 结果: 正常执行摄影语法
```

## 根因

1. 代码块标记 ` ```text ` 中的 `text` 是 Markdown 语法高亮标识，不是内容的一部分
2. 但某些复制/粘贴场景或工具链可能将 `text` 一并复制到提示词中
3. 用户直接复制代码块内容时，如果不注意会包含 `text` 前缀

## 修复方法

### 输出端（技能侧）

STEP-15 输出提示词时：
- **禁止**使用 ` ```text ` 或 ` ```txt ` 等带语言标记的代码块
- **必须使用**无语言标记的纯代码块：` ``` `（三个反引号，无后缀）
- **禁止**使用 ` ```markdown ` 标记，原因同上（`markdown` 词会泄漏到提示词内容中）
- 或使用行内代码格式（不推荐，提示词较长时）

### 内部结构标签泄漏（2026-06-25 MRI 任务新发现）

**现象**：STEP-15 使用五段式物理空间协议（Layout Block 1-5）作为内部推理结构，但 `[Layout Block X: ...]` 标记被错误输出到最终提示词中。

**错误示例**：
```
❌ 错误输出（结构标签泄漏）:
[Layout Block 1: 视角与空间锚定]
Studio photograph, three-quarter view slightly above...

[Layout Block 2: 核心拓扑与交接关系]
A solid honed basalt slab...
```
→ 用户复制时包含 `[Layout Block X: ...]` 标记
→ AI 图像生成模型接收异常前缀

**修复**：
1. **内部推理阶段**可使用 `[Layout Block X: ...]` 作为思维框架
2. **最终输出阶段**必须删除所有 `[Layout Block X: ...]` 标记
3. 只保留五段式协议的**内容**，不保留标签
4. 每段之间用**空行**自然分隔，不用标签分隔

**正确示例**：
```
✅ 正确输出（无标签，纯内容）:
Studio photograph, three-quarter view slightly above, of a single next-generation dry-magnet 3T MRI scanner...

A solid honed basalt slab, 250cm long and 40cm thick...

G2 fillet edges around the aperture...

Integrated tactile surface nodes...

No text, no branding, no visible screws...
```

### 用户端（复制时）

如果看到提示词以 `text` 开头：
- 手动删除 `text` 前缀
- 确保提示词以 `Studio photograph` 或 `A` 或 `The` 等正常英文词开头

## 检查清单

- [ ] STEP-15 输出代码块是否使用了 ` ```text `？→ 改为 ` ``` `
- [ ] 提示词是否以 `text` 开头？→ 删除
- [ ] 提示词是否以 `markdown` 开头？→ 删除（` ```markdown ` 标记泄漏）
- [ ] 提示词是否包含 `[Layout Block X: ...]` 标记？→ 删除
- [ ] 提示词是否以正确的摄影语法开头？→ `Studio photograph` / `Product shot` / `A...`

## 来源

- 2026-06-24 下一代载人飞行器任务用户反馈
- REF-PROMPT-002: 中文提示词压缩规则
- REF-PROMPT-004: 摄影表达控制
