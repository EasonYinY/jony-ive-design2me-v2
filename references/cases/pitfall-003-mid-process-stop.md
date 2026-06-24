---
reference_id: PITFALL-003
title: 中途停止执行
category: cases
used_when:
called_by:
  - skill-router
depends_on:
  - REF-PROCESS-003
outputs:
  - pitfall_warning
---

# Pitfall 003: 中途停止执行

## 现象

在STEP-01至STEP-15执行过程中，agent在STEP-05或中间步骤停下来，询问用户"是否继续"或"请确认"。用户反馈："为什么会停？直接到最后啊"

## 根因

1. Agent误解了"逐步交付"的含义，以为需要每步都等待用户确认
2. 未理解用户偏好：用户要求end-to-end自动化，0次mid-flow确认
3. 技能合同中的"逐步展示"被误读为"逐步等待"

## 触发条件

- 用户说"设计一个XX"时，agent执行几步后停下来
- 用户说"直接到最后""继续执行""不要停"时
- 用户反馈"没有按照要求输出内容"

## 正确做法

1. 十五步主流程必须**一次性连续执行完成**
2. "逐步展示"是指在同一输出中按顺序展示所有步骤，不是分多次输出
3. 用户未说"停"时，默认连续执行到STEP-15
4. 如果输出太长，可以在同一轮内分多个消息块发送，但不要在中间插入用户确认

## 错误做法

1. 执行到STEP-05后问"请确认是否继续"
2. 将15步拆分成多个轮次执行
3. 每步后等待用户反馈再进入下一步

## 相关规则

- `references/process/reasoning-output.md`: "完整流程必须恰好包含按顺序排列的 STEP-01 至 STEP-15"
- `references/process/end-to-end-workflow.md`: 默认在STEP-15停止
