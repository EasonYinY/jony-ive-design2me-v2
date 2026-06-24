---
reference_id: REF-CASE-032
title: Pitfall 032 — 迭代模式中 Subagent 不可靠
category: cases
used_when:
  - ITERATION-MODE
  - MULTI-ROUND-EXECUTION
called_by:
  - iteration-workflow
  - end-to-end-workflow
depends_on:
  - REF-PROCESS-005
outputs:
  - subagent_warning
---

# Pitfall 032 — 迭代模式中 Subagent 不可靠 (Subagent Unreliable in Iteration Mode)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 5轮迭代中多次使用 `delegate_task` 后台子代理失败
> **严重程度**: 🔴 高

---

## 现象

在5轮迭代执行中，尝试使用 `delegate_task` 后台子代理执行 Round 2-4 的迭代任务，结果：

| 轮次 | 子代理状态 | 结果 |
|------|----------|------|
| Round 2 | 后台启动 | timeout，未生成文件 |
| Round 3 | 后台启动 | timeout，未生成文件 |
| Round 4 | 后台启动 | timeout，未生成文件 |

最终主会话不得不手工接管，重新执行所有步骤。

---

## 根因分析

### 根因1: Subagent 的 max_iterations 限制

子代理有 tool 调用次数限制（max_iterations），复杂迭代任务（15步推理 + 文件写入 + Lovart 调用）容易超出限制，导致子代理在完成任务前退出。

### 根因2: 文件写入不同步

子代理写入的文件可能因 max_iterations 退出而未 flush 到磁盘，主会话看不到子代理的产出。

### 根因3: 上下文隔离

子代理没有主会话的上下文（如 Lovart 凭证、已创建的目录），需要重新初始化。

### 根因4: Timeout 与后台进程混淆

子代理的 timeout 与 Lovart 后台进程的 timeout 叠加，导致双重失败。

---

## 解决方案

### 策略1: 主会话直接执行（推荐）

**不要在迭代模式中使用 `delegate_task` 后台子代理。**

主会话直接执行每轮迭代：
1. 15步推理 → 写入文件
2. Lovart 出图 → 后台进程（仅 Lovart 用后台，推理部分不用）
3. 评审 → 写入文件
4. 升级 → 写入文件

### 策略2: 若必须使用子代理，切分更小任务

将一轮迭代切分为多个子代理任务：
- 任务A: 15步推理 → 写入 design-output.md
- 任务B: Lovart 出图（仅命令执行）
- 任务C: 评审 + 升级

每个任务必须在 prompt 中明确：
```
"commit after EACH file write. Not after all tasks."
"write file immediately after generation, do not wait for other tasks."
```

### 策略3: 子代理失败后主会话接管

当子代理失败时：
1. 不要重试子代理
2. 主会话直接接管，手工执行剩余步骤
3. 检查子代理可能已部分完成的文件

---

## 验证方法

```
[ ] 迭代模式中未使用 delegate_task 后台子代理
[ ] 若使用子代理，任务已切分为最小单元
[ ] 子代理 prompt 包含 "commit after EACH task" 硬约束
[ ] 子代理失败后主会话立即接管
```

---

## 5轮迭代中的实证

| 尝试 | 方法 | 结果 |
|------|------|------|
| 第1次 | 3个并行子代理（Round 2-4） | 全部 timeout，无文件 |
| 第2次 | 主会话直接执行 | 成功完成 Round 1-5 |

**结论**: 迭代模式中，主会话直接执行是唯一可靠方式。

---

## 关联

- 相关 Pitfall: 027（复杂提示词超时）
- 相关 Pitfall: 029（复杂产品衰减）
- 相关指南: Lovart 执行指南（references/guides/lovart-execution.md）

---

## 来源

- 5轮迭代实证: references/iterations/round-{1-5}/
- 日期: 2026-06-21
