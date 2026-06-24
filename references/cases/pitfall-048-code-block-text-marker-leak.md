---
reference_id: REF-CASE-048
title: Pitfall 048 - Code Block `text` Marker Leaking into Prompt
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
- 或使用行内代码格式（不推荐，提示词较长时）

### 用户端（复制时）

如果看到提示词以 `text` 开头：
- 手动删除 `text` 前缀
- 确保提示词以 `Studio photograph` 或 `A` 或 `The` 等正常英文词开头

## 检查清单

- [ ] STEP-15 输出代码块是否使用了 ` ```text `？→ 改为 ` ``` `
- [ ] 提示词是否以 `text` 开头？→ 删除
- [ ] 提示词是否以正确的摄影语法开头？→ `Studio photograph` / `Product shot` / `A...`

## 来源

- 2026-06-24 下一代载人飞行器任务用户反馈
- REF-PROMPT-002: 中文提示词压缩规则
- REF-PROMPT-004: 摄影表达控制
