---
reference_id: REF-GUIDE-010
title: Lovart 图片生成执行指南
category: guides
used_when:
  - IMAGE-GENERATION
called_by:
  - end-to-end-workflow
  - iteration-workflow
depends_on:
  - REF-PROMPT-004
  - REF-PROCESS-001
outputs:
  - lovart_execution_command
---

# Lovart 图片生成执行指南

> **版本**: 1.1
> **日期**: 2026-06-21(初始) · 2026-06-23(模式升级)
> **触发**: 用户明确要求"调用 Lovart nano banana pro 模型生成图片"

> **当前模式升级(2026-06-23)**: 新增"模式 1:write_file + cat"作为强制默认。原早期版本的 heredoc 模式在多行提示词 + 含单/双引号场景下触发 `exit=2`(详见 pitfall-027)。本指南从今起**禁止使用 heredoc**,统一走文件路径。

---

## 概述

本指南记录从 STEP-15 提示词到 Lovart 图片生成的标准执行流程，确保三个方向并行生成、统一输出规范。

> **⚠️ CRITICAL FIX (2026-06-24)**: Lovart `chat` 命令对高成本操作（如 image generation）默认进入 `pending_confirmation` 状态，需要显式 `confirm` 才能实际生成。直接 `background=true` 会静默失败，产生空白占位图。详见下方「确认流程」章节。

---

## 执行命令模板

### 模式 1(强制默认):`/tmp/<file>.txt` + `cat` 注入

```bash
# 步骤 1:用 hermes write_file 工具把提示词写入 /tmp/lovart-r1-dN-prompt.txt
# (此步骤在 hermes agent 端完成,文件内容零引号冲突)

# 步骤 2:bash 调用时只做单层 shell 替换
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
PROMPT=$(cat /tmp/lovart-r1-d1-prompt.txt) && \
python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py chat \
  --prompt "$PROMPT" \
  --prefer-models '{"IMAGE":["vertex/anon-bob"]}' \
  --download --output-dir ~/lovart-out/r1-d1
```

**优势**:
- 提示词内容走文件系统,零 shell 引号冲突
- 任何 > 5 行的多行提示词都安全
- 与 pitfall-027 修复模式一致(已验证 3+ 次成功)

**禁止**: 任何 > 5 行的提示词禁止使用 heredoc (`cat <<'EOF'`)。

### 模式 2(已废弃):heredoc 嵌入(仅适用于极短提示词)

```bash
# ⚠️ 当前版本起不再推荐,仅作历史记录
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py chat \
  --prompt "[提示词]" \
  --prefer-models '{"IMAGE":["vertex/anon-bob"]}' \
  --download --output-dir ~/lovart-out/[目录名]
```

### 参数说明

| 参数 | 值 | 说明 |
|------|-----|------|
| `--prefer-models` | `{"IMAGE":["vertex/anon-bob"]}` | Nano Banana Pro 模型（1K分辨率） |
| `--download` | - | 自动下载图片到本地 |
| `--output-dir` | `~/lovart-out/rN-dN` | 输出目录命名规范 |

### 目录命名规范

```
~/lovart-out/
├── r1-d1/          # Round 1, Direction 1
├── r1-d2/          # Round 1, Direction 2
├── r1-d3/          # Round 1, Direction 3
├── r2-d1/          # Round 2, Direction 1
└── ...
```

---

## 并行执行模式

### 三个方向同时生成

使用 `background=true` 并行启动三个任务：

```python
# 伪代码示例
for direction in [d1, d2, d3]:
    terminal(
        command=lovart_command(direction.prompt),
        background=True,
        notify_on_complete=True
    )
```

### 等待策略

1. 启动三个后台任务
2. 使用 `process(action="poll")` 检查进度
3. 使用 `process(action="wait")` 等待完成（timeout=120s）
4. 若超时，继续poll直到全部完成

---

## 输出验证

### 检查清单

- [ ] 每个方向生成2张图片（共6张）
- [ ] 图片分辨率符合1K标准（1024×1024 或 1280×720 或 2048×2048）
- [ ] 文件大小合理（通常 500KB-3MB）
- [ ] 文件名格式：`lovart_[hash].png`

### 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| 图片未生成 | Lovart API 超时 | 重新运行命令 |
| 分辨率不足 | 模型限制 | 确认使用 vertex/anon-bob |
| 文件损坏 | 下载中断 | 删除后重新下载 |
| **Status: pending_confirmation** | **需要用户确认高成本操作** | **使用 `confirm` 命令：`python3 agent_skill.py confirm --thread-id <THREAD_ID> --download --output-dir <DIR>`** |
| 图片空白/纯白 | 模型未实际生成，只返回占位符 | 检查文件平均RGB值，确认后重新生成 |
| **Status: pending_confirmation** | **需要用户确认高成本操作** | **使用 `confirm` 命令：`python3 agent_skill.py confirm --thread-id <THREAD_ID> --download --output-dir <DIR>`** |
| 图片空白/纯白 | 模型未实际生成，只返回占位符 | 检查文件平均RGB值，确认后重新生成 |
| **空白/占位图** | `pending_confirmation` 未处理 | 见下方「确认流程」 |

---

## 确认流程（CRITICAL — 2026-06-24 实证）

### 问题

Lovart `chat` 命令对 image generation 等高成本操作默认返回 `Status: pending_confirmation`，**不会立即生成图片**。如果直接 `background=true` + `notify_on_complete=true`，任务会静默"完成"，但目录中只产生空白占位图或旧文件。

### 正确流程

```bash
# Step 1: 启动 chat（获取 thread-id）
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py chat \
  --prompt "[提示词]" \
  --prefer-models '{"IMAGE":["vertex/anon-bob"]}' \
  --download --output-dir ~/lovart-out/r1-d1

# 输出示例：
# Status: pending_confirmation
# Thread: 6873a515-9808-4bbb-89a1-6680fa4d8ff0

# Step 2: 显式 confirm（必须）
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py confirm \
  --thread-id 6873a515-9808-4bbb-89a1-6680fa4d8ff0 \
  --download --output-dir ~/lovart-out/r1-d1

# 输出示例：
# Status: done
# [image] https://a.lovart.ai/artifacts/agent/xxx.png
# -> /Users/easoneason/lovart-out/r1-d1/lovart_xxx.png
```

### 并行生成修正流程

```bash
# 不要直接用 background=true！正确做法：

# 1. 前台启动三个 chat（快速获取 thread-id）
# 2. 对每个 thread-id 执行 confirm
# 3. confirm 可以并行后台执行

# 示例：
for thread_id in $THREAD1 $THREAD2 $THREAD3; do
  python3 .../agent_skill.py confirm \
    --thread-id $thread_id \
    --download --output-dir ~/lovart-out/rN-dN &
done
wait
```

### 验证：检测空白/占位图

如果怀疑图片未正确生成，用 Python 快速检测：

```python
from PIL import Image

for f in ['r1-d1.png', 'r1-d2.png', 'r1-d3.png']:
    img = Image.open(f)
    img_small = img.resize((50, 50))
    pixels = list(img_small.getdata())
    white_count = sum(1 for p in pixels if p[0] > 240 and p[1] > 240 and p[2] > 240)
    total = len(pixels)
    ratio = white_count / total
    print(f'{f}: {ratio:.1%} white pixels')
    if ratio > 0.7:
        print(f'  ⚠️ WARNING: Likely blank/placeholder image!')
```

**判定标准**：
- > 70% 白色像素 → 极可能是空白占位图，需重新 confirm
- 30-70% 白色像素 → 正常（纯白背景产品图）
- < 30% 白色像素 → 正常（有内容）

---

## 重复生成策略

### 场景

用户要求"每个方向生成2张图片"时，Lovart 单次调用通常只生成1张。需要多次调用同一提示词以生成多张图片。

### 执行方法

1. **第一次调用**: 使用 `background=true` + `notify_on_complete=true` 并行启动三个方向
2. **等待完成**: 使用 `process(action="wait", timeout=120)` 等待每个任务完成
3. **检查输出**: 用 `ls -la` 确认每个目录已有1张图片
4. **第二次调用**: 再次并行启动三个方向（相同提示词，相同输出目录），Lovart 会自动生成新文件（不同 hash）
5. **最终验证**: 每个目录应有2张图片，共6张

### 注意事项

- 不要删除第一次生成的图片，直接在同一目录运行第二次
- Lovart 会为每次调用生成不同 hash 的文件名，不会覆盖
- 若某方向第二次生成失败，该方向已有1张可用，记录为部分完成

### 输出目录最终状态

```
~/lovart-out/
├── r1-d1/
│   ├── lovart_[hash1].png   # 第1次生成
│   └── lovart_[hash2].png   # 第2次生成
├── r1-d2/
│   ├── lovart_[hash3].png   # 第1次生成
│   └── lovart_[hash4].png   # 第2次生成
└── r1-d3/
    ├── lovart_[hash5].png   # 第1次生成
    └── lovart_[hash6].png   # 第2次生成
```

---

### 超时处理与重试策略

### 问题

Lovart API 调用可能因网络或模型负载超时（120s timeout）。直接重试相同命令可能再次超时，形成重复失败循环。

### 解决方案

**第一次超时**：
- 改用 `background=true` + `notify_on_complete=true` 后台运行
- 使用 `process(action="poll")` 检查进度
- 等待后台进程自然完成（通常 200-300s）

**第二次超时**：
- 再次前台运行（timeout=120），通常此时 API 负载已降低
- 若仍超时，继续后台模式

**经验数据**：
- 2026-06-21 鼠标任务：D2 轨道导航方向连续2次前台超时，第3次后台成功
- 后台进程完成时间：~223s（3分43秒）
- 前台成功通常在 API 负载低时（<120s）

### 后台进程 timeout 后文件未下载的恢复（2026-06-24 电动剃须刀任务实证）

**现象**: `process(action="wait", timeout=180)` 返回 `Status: timeout`，但 `exit_code=0`。检查输出目录为空（`total 0`），说明图片生成可能已完成但下载失败。

**恢复流程**:
1. **检查目录**: `ls -la ~/lovart-out/rN-dN/` 确认是否为空
2. **使用 `result --thread-id` 重试下载**:
   ```bash
   source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
   python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py result \
     --thread-id <THREAD_ID> \
     --download --output-dir ~/lovart-out/rN-dN
   ```
3. **验证**: 检查目录是否已有文件，且 JSON 输出中 `downloaded` 数组非空

**关键发现**:
- `timeout` + `exit_code=0` ≠ 失败，只是下载未完成
- Thread ID 在 timeout 后仍然有效，可以用 `result` 命令恢复
- 不要重新运行 `chat`（会创建新 thread，浪费 credits）

### 禁止

- ❌ 连续3次以上相同命令前台重试（会进入重复失败循环）
- ❌ 删除已生成的图片后重试（浪费已生成结果）
- ❌ 同时运行多个相同方向的后台任务（可能导致目录混乱）
- ❌ timeout 后直接重新运行 `chat`（应先用 `result` 恢复）

---

## 后台进程 timeout 后旧图复用问题

### 问题

`process(action="wait", timeout=300)` 实际被 clamp 到 180s。当 Lovart 后台进程在 180s 内未完成时，process 返回 `timeout` 状态，但后台进程仍在运行。

此时检查输出目录会发现：
1. **旧图片存在**：目录中有之前会话生成的旧图片（不同 hash）
2. **新图片未生成**：当前进程的图片尚未完成
3. **误判风险**：容易将旧图片误认为当前轮次的生成结果

### 5轮迭代中的实证

| 轮次 | 现象 | 后果 |
|------|------|------|
| Round 3 | D1 timeout 1，但目录有旧图 | 误用旧图进行评审 |
| Round 4 | D1/D2 timeout 1，D3 done 1 | 部分旧图混入 |
| Round 5 | 全部 timeout，但目录有旧图 | 可能误用旧图 |

### 解决方案

**1. 区分新旧图片**

```bash
# 按时间排序，只取最新的图片
ls -lt ~/lovart-out/rN-dN/*.png | head -1
```

**2. 验证图片与提示词匹配**

检查 Lovart 返回的 JSON 日志（`/tmp/rN-dN.json`）中的 `final_status` 和 `downloaded` 字段：

```bash
cat /tmp/rN-dN.json | python3 -c "import sys,json; d=json.load(sys.stdin); print('status:', d.get('final_status')); print('downloaded:', len(d.get('downloaded',[])))"
```

- `done 1` = 当前进程成功生成1张新图片
- `timeout 1` = 进程超时，但可能已完成1张（旧图或新图）
- `timeout 0` = 进程超时，未生成任何图片

**3. 清理旧图片策略**

在多轮迭代中，每轮开始前清理旧图片：

```bash
# 保留最新2张，删除其余
ls -t ~/lovart-out/rN-dN/*.png | tail -n +3 | xargs rm -f
```

**4. 使用 JSON 状态验证**

不要仅依赖 `ls` 判断生成状态，必须检查 JSON 日志：

```bash
# 检查所有方向的 JSON 状态
for i in 1 2 3; do
  echo "R5-D$i:"
  cat /tmp/r5-d$i.json 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(' ', d.get('final_status'), len(d.get('downloaded',[])))" 2>/dev/null || echo "  no json"
done
```

### 禁止

- ❌ 仅通过 `ls` 判断生成成功（可能看到旧图）
- ❌ 不检查 JSON 日志直接进行图片评审
- ❌ 将旧轮次的图片用于当前轮次的评审

### 推荐做法

1. 每轮开始前创建新目录（即使目录已存在，旧图会被新图覆盖或共存）
2. 使用 `mkdir -p` 确保目录存在
3. 生成后按时间排序取最新图片
4. 评审前验证 JSON 日志确认是当前进程的生成结果

---

## 与迭代工作流的集成

### 迭代模式中的图片生成

在迭代工作流（REF-PROCESS-005）中，图片生成是 Phase 1 的 STEP 3：

```
Phase 1: 单轮执行
  STEP 1: 创建迭代计划
  STEP 2: 执行15步推理
  → STEP 3: Lovart出图（3方向并行）
  STEP 4: Vision分析+艾维评估
  STEP 5: 生成升级计划
  STEP 6: 执行升级
  STEP 7: 生成Handoff口令
```

---

## 来源

- 2026-06-21 电动剃须刀设计任务：成功生成6张图片（3方向×2张）
- Lovart 技能文档：`~/.hermes/skills/lovart/`
- REF-PROCESS-005: 迭代工作流
