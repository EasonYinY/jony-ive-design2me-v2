---
reference_id: REF-CASE-027
title: Pitfall 027 - Lovart shell quoting failure with multi-line prompts
category: cases
used_when:
  - LOVART-INVOCATION
  - SHELL-EXECUTION
  - PROMPT-COMPILATION
called_by:
  - lovart-execution
  - image-critique
  - quality-gates
depends_on:
  - REF-GUIDE-010
  - references/cases/pitfall-024-lovart-quiet-success-timeout.md
outputs:
  - shell_pattern
  - failure_pattern
---

# Pitfall 027: Lovart 调用时 shell 嵌套引号失败(`exit=2` "unexpected EOF")

> **版本**: 1.0
> **日期**: 2026-06-23
> **触发**: Lovart 调用使用 bash `heredoc` (`cat <<'EOF' ... EOF`) + 双引号包 `--prompt` 时,外层 `bash` 因引号不匹配解析失败,`exit=2` 且 stdout 完全空,无 Status / Thread / image URL
> **严重级别**: MEDIUM — 完全可避免,但首次触发时难定位(因无错误信息,只看到 exit code)
> **前置**: 与 Pitfall 024(`Status: timeout` 但实际成功)同根于"stdout 兜底"需求

## 现象

```bash
# 失败模式 A:heredoc + 双引号冲突
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ... agent_skill.py chat \
  --prompt "$(cat <<'EOF'
... multi-line prompt with double quotes and apostrophes ...
EOF
)" \
  --prefer-models '{"IMAGE":["vertex/anon-bob"]}' \
  --download --output-dir ~/lovart-out/r1-d1

# 现象:
# - bash 解析错误: "unexpected EOF while looking for matching `''"
#                  "bash: syntax error: unexpected end of file"
# - exit code = 2
# - run.log 内容: 仅 "Saving session..." (无 Status, 无 Thread, 无 image URL)
# - 输出目录为空
```

**首次触发实证(2026-06-23)**:
- 飞行器 r1-d5 首次调用,`exit=2`,run.log 仅 5 行 session close
- 提示词含单引号(`LoveFrom's`) + 多行结构 + 双引号 `--prefer-models '{...}'`
- 根因:heredoc 内的单引号 `LoveFrom's` 与 heredoc 边界 `<<'EOF'` 冲突

## 根因分析

1. **Bash heredoc 边界冲突**: `<<'EOF'` 内的内容本应被原样保留,但提示词中混入的引号(单/双)与外层 shell 解析层产生隐式转义冲突
2. **嵌套引号复杂度**: `--prompt "$(cat <<'EOF' ...)"` 是 3 层引号嵌套(`""` + `''` + `EOF` 边界),任一层引号失配即触发语法错误
3. **错误信息延迟**: shell 报错时,heredoc 内的提示词可能尚未执行,导致错误位置不可见,只有 exit code

## 修复方法(强制标准模式)

### 模式 1:`/tmp/<file>.txt` + `cat` 读取(**强制默认**)

```bash
# 步骤 1: 用 write_file 把提示词写入 /tmp/<file>.txt
# (用 hermes write_file 工具,避免 shell 引号问题)

# 步骤 2: bash 调用时只做单层 shell 替换
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
PROMPT=$(cat /tmp/lovart-r1-d1-prompt.txt) && \
python3 ... agent_skill.py chat \
  --prompt "$PROMPT" \
  --prefer-models '{"IMAGE":["vertex/anon-bob"]}' \
  --download --output-dir ~/lovart-out/r1-d1 > ~/lovart-out/r1-d1/run.log 2>&1
```

**优势**:
- `cat /tmp/file` 不引号化,避免任何嵌套冲突
- `PROMPT=$(cat ...)` 把文件内容作为单层变量
- `--prompt "$PROMPT"` 仍是双引号但只包变量,无内容冲突

### 模式 2:heredoc 但限定为单层 `<<'EOF'` + 显式 `python3 -c`

仅当提示词不含任何单/双引号时可用(实际很少见):

```bash
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ... agent_skill.py chat \
  --prompt "$(cat <<'EOF'
clean prompt without quotes
EOF
)" \
  --prefer-models '{"IMAGE":["vertex/anon-bob"]}' \
  --download --output-dir ~/lovart-out/r1-d1
```

### 模式 3:`base64` 编码(极端场景)

提示词含 binary-like 字符或 shell 关键字时:

```bash
echo "$PROMPT_BASE64" | base64 -d | xargs -0 -I {} python3 ... agent_skill.py chat --prompt "{}"
```

不推荐,过复杂,优先用模式 1。

## 验证方式

每次 Lovart 调用后,执行以下检查:

```bash
# 1. exit code 应为 0
echo "exit=$?"

# 2. run.log 应包含至少以下任一关键词
grep -E "Status:|Thread:|\[image\]" ~/lovart-out/r1-dN/run.log || echo "FAIL: no Lovart output"

# 3. 如有 [image] URL,文件应存在
grep "\[image\]" ~/lovart-out/r1-dN/run.log | awk '{print $NF}' | xargs -I {} ls -la {}

# 4. 输出目录应至少 1 个 .png
ls ~/lovart-out/r1-dN/*.png || echo "FAIL: no PNG file"
```

## 关键经验:hermes `write_file` 是 Lovart 提示词的"零引号"传递

| 工具 | 引号冲突风险 | 推荐 |
|---|---|---|
| bash heredoc `<<'EOF'` | 高(heredoc 边界 + 内容引号) | ❌ |
| bash `echo "..."` | 中(单/双引号需转义) | ❌ |
| `write_file` + `cat /tmp/file` | 0(内容走文件系统) | ✅ 强制默认 |
| `python3 -c "..."` | 中(python 字符串转义) | ❌ |

**规则**: **任何 > 5 行的 Lovart 提示词,必须先 `write_file` 到 `/tmp/`,再用 `cat` 注入 shell 命令。**

## 与其他 Pitfall 关系

- **Pitfall 024(Lovart 静默超时成功)**: 互补。
  - 024: `exit=0` + `Status: timeout` + 实际成功(需要 grep stdout 兜底)
  - 027: `exit=2` + 完全空 stdout + 完全失败(需要重写 shell 命令)
- **Pitfall 025/026(品类反模式)**: 独立。027 是 shell 层面问题,025/026 是 prompt 内容问题
- **REF-GUIDE-010(Lovart 执行指南)**: 应更新其"执行命令模板"段,把"模式 1"作为默认推荐

## 来源

- 2026-06-23 飞行器 r1-d5 首次调用触发,`exit=2` + run.log 5 行 session close
- 同日 D2 首次也因类似原因 timeout(但实际有 image URL,属 024 而非 027)
- 同日 D5 用 write_file + cat 模式重跑,`Status: done` + PNG 成功下载
- 修复模式 1(`write_file` + `cat /tmp/file`)已验证 3 次成功(咖啡机任务,飞行器任务 D1/D2/D5)
