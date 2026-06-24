---
reference_id: REF-CASE-017
title: Pitfall 017 - 提示词未用代码块
category: cases
used_when:
called_by:
  - product-design
  - quality-gates
  - failure-library
depends_on:
  - REF-PROCESS-001
  - REF-QUALITY-003
outputs:
  - failure_pattern
---

# Pitfall 017 - 提示词未用代码块

## 触发条件

1. 最终提示词未使用代码块显示（如使用普通文本、引用格式、列表格式）
2. 未额外输出英文提示词（仅输出中文提示词）
3. 输出格式不符合用户要求的6组代码块（3中文+3英文）
4. 提示词与其他内容混排，无法直接复制使用

## 失败表现

- 提示词以普通文本输出，用户无法直接复制到AI绘图工具
- 缺少英文提示词，用户需要自行翻译
- 提示词与DesignIR、质量门结果混排，提取困难
- 格式不统一，不同方向提示词格式不一致

## 根因分析

### 直接原因
STEP-15输出格式未标准化：
- 提示词输出格式未在流程中明确规定
- 多语言输出要求未在流程中体现

### 深层原因
流程缺少"输出格式"强制规范：
- 默认输出仅为中文提示词
- 未考虑用户可能需要直接复制提示词到AI绘图工具

## 修复方法

### STEP-15强制输出格式
必须输出6组代码块：

```markdown
## D1 [方向名称]

### 中文提示词
```
[中文提示词内容]
```

### English Prompt
```
[English prompt content]
```

## D2 [方向名称]

### 中文提示词
```
[中文提示词内容]
```

### English Prompt
```
[English prompt content]
```

## D3 [方向名称]

### 中文提示词
```
[中文提示词内容]
```

### English Prompt
```
[English prompt content]
```
```

### 代码块规范
1. 每个提示词独立代码块
2. 代码块语言标记为`text`或`prompt`
3. 中文提示词在前，英文提示词在后
4. 方向标识（D1/D2/D3）清晰标注

### 禁止事项
- ❌ 提示词以普通文本输出（无代码块）
- ❌ 仅输出中文提示词（无英文）
- ❌ 提示词与DesignIR混排
- ❌ 不同方向格式不一致

## 验证方式

1. 检查是否输出6组代码块（3中文+3英文）
2. 检查每个提示词是否在独立代码块中
3. 检查方向标识是否清晰
4. 检查提示词是否可直接复制使用

## 来源

- REF-PROCESS-001 STEP-15
- REF-QUALITY-003 failure-library `prompt_not_in_codeblock`
- 实证：2026-06-21用户明确要求"6组代码块设计提示词，3个英文，3个中文"
