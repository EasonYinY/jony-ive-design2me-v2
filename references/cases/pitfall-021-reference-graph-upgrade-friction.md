---
reference_id: REF-CASE-021
title: Pitfall 021 - 技能升级时验证脚本过度拦截
category: cases
used_when:
  - skill-upgrade
  - reference-graph-maintenance
called_by:
  - jony-ive-design2me-v2
depends_on:
  - REF-PROCESS-002
outputs:
  - upgrade_path
---

# Pitfall 021 - 技能升级时验证脚本过度拦截

## 现象

升级技能时运行 `validate_reference_graph.py` 或 `validate_skill.py`，脚本输出大量"失败"，但这些失败大多属于以下类别：

1. **Pitfall/Case 文件声明的 STEP 未被 step-reference-map 引用**
   - 例：`PITFALL-003 声明 STEP-01，但步骤映射未引用它`
   - 根因：Pitfall 文件是案例参考，不是活跃工作流步骤；它们的 `used_when` 标记的是"何时查阅"而非"被哪个步骤强制引用"

2. **Reference ID 重复**
   - 例：`reference_id 重复：REF-CASE-018`
   - 根因：历史版本迭代中新增文件时未检查现有 ID 池

3. **README 表格解析失败**
   - 例：`总索引 ID 不一致：缺少 [...]`
   - 根因：README.md 表格中某些行有额外 `|` 前缀（如 `|| REF-xxx` 而非 `| REF-xxx`），导致正则解析跳过这些行

4. **未知依赖**
   - 例：`REF-ITERATION-R1 存在未知依赖：['REF-LOVART-001']`
   - 根因：迭代记录文件依赖了外部技能（lovart）的引用，但验证脚本只检查本技能内部

## 影响

- 升级者被大量红色"失败"淹没，难以区分"真正需要修复的错误"和"历史遗留噪音"
- 修复过程变成打地鼠：修复一个 ID 重复，又暴露另一个；修复表格格式，又发现更多缺失条目
- 升级时间被验证脚本噪音显著拉长

## 修复路径（已验证）

### 针对 Reference ID 重复

1. 运行 `grep -r "REF-XXX-YYY" references/` 定位所有重复
2. 将重复 ID 的文件改为新 ID（如 REF-CASE-018 → REF-CASE-018b）
3. 同步更新 README.md 中的索引条目

### 针对 README 表格格式

1. 检查 README.md 中是否有 `||` 开头的行（应为 `|` 开头）
2. 用 write_file 重写整个 README.md 表格，确保每行严格格式：`| ID | 文档 | 用途 |`
3. 验证：用 Python 正则 `\|\s*(REF-[A-Z]+-\d+[a-z]?)\s*\|` 检查所有 ID 是否被正确捕获

### 针对 Step 映射缺失（Pitfall/Case 文件）

**判断**：如果文件是 `cases/pitfall-*.md` 或 `cases/case-*.md`，其 `used_when` 标记的是"查阅时机"，不应强制要求 step-reference-map 引用。

**处理**：
- 若该文件确实被某个工作流步骤主动引用（如 STEP-06 的"概念来源检查"引用 REF-GUIDE-CONCEPT），则添加到 step-reference-map
- 若该文件是被动参考材料（如 Pitfall 案例库），可考虑从文件的 frontmatter 中移除 `used_when` 的 STEP 声明，或接受验证脚本的警告

### 针对未知依赖（跨技能引用）

- 若依赖的是外部技能（如 REF-LOVART-001），在 depends_on 中使用完整引用格式，或在本技能内创建代理引用
- 或在验证脚本中增加跨技能引用白名单

## 预防措施

1. **新增文件时**：先用 `grep -r "reference_id" references/ | grep "目标ID"` 检查是否已存在
2. **修改 README.md 时**：用 Python 脚本验证表格格式，确保无 `||` 前缀行
3. **升级前**：先备份，再运行验证脚本记录基线错误数量；升级后只关注"新增错误"

## 经验

本次中，修复了 3 个 ID 重复和 1 个表格格式问题后，验证脚本仍输出 40+ 历史遗留错误。这些错误不影响技能功能，但会干扰升级者判断。建议未来版本：

- 将验证脚本分为"严格模式"（CI 用）和"宽松模式"（升级用）
- 或增加错误分类：ERROR（必须修复）vs WARNING（历史遗留）
