---
reference_id: PITFALL-029-A
title: Pitfall 029-A - Lovart pending_confirmation silent failure
category: cases
supersedes_id_was: PITFALL-029
disambiguation_note: 原 PITFALL-029 与 pitfall-029-aerodynamic-trap.md 冲突,本文件分配 -A 后缀。官方权威 PITFALL-029 = 空气动力学陷阱(由 README.md 登记)。
category: cases
used_when:
  - LOVART-EXECUTION
  - IMAGE-GENERATION
called_by:
  - lovart-execution
depends_on:
  - REF-GUIDE-010
  - REF-CASE-002
outputs:
  - lovart_confirmation_workflow
---

# Pitfall 029: Lovart pending_confirmation 静默失败

> **版本**: 1.0
> **日期**: 2026-06-24
> **触发**: 飞行器任务 — Lovart `chat` 命令返回 `pending_confirmation`，agent 误以为成功，用户看到空白图
> **严重级别**: 🔴 BLOCKER

---

## 现象

1. Agent 执行 `lovart chat --prompt ... --download --output-dir ...`
2. 命令返回 `Status: pending_confirmation` + `Thread: xxx`
3. Agent 误以为任务完成，文件已下载
4. 目录中出现文件（可能是旧文件或空白占位图）
5. 用户反馈"完全没有看到正确的图像"
6. 文件像素分析显示 > 70% 白色像素（空白占位图）

---

## 根本原因

Lovart CLI 对高成本操作（image generation）默认需要用户确认。`chat` 命令启动任务后进入 `pending_confirmation` 状态，**不会实际执行生成**，直到显式调用 `confirm --thread-id xxx`。

`background=true` + `notify_on_complete=true` 会捕获到 `exited` 状态，但退出原因是任务"完成"了 pending_confirmation 阶段，而非实际生成完成。

---

## 正确流程

### 单方向生成

```bash
# Step 1: 启动 chat（获取 thread-id）
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py chat \
  --prompt "[提示词]" \
  --prefer-models '{"IMAGE":["vertex/anon-bob"]}' \
  --download --output-dir ~/lovart-out/r1-d1

# 输出：
# Status: pending_confirmation
# Thread: 6873a515-9808-4bbb-89a1-6680fa4d8ff0

# Step 2: 显式 confirm（必须）
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py confirm \
  --thread-id 6873a515-9808-4bbb-89a1-6680fa4d8ff0 \
  --download --output-dir ~/lovart-out/r1-d1

# 输出：
# Status: done
# [image] https://a.lovart.ai/artifacts/agent/xxx.png
# -> /Users/easoneason/lovart-out/r1-d1/lovart_xxx.png
```

### 多方向并行生成

```bash
# 不要直接用 background=true 并行 chat！
# 正确做法：

# 1. 前台启动三个 chat（快速获取 thread-id）
# 2. 对每个 thread-id 执行 confirm
# 3. confirm 可以并行后台执行

# 示例脚本
THREAD_IDS=()
for i in 1 2 3; do
  output=$(python3 .../agent_skill.py chat ... 2>&1)
  thread_id=$(echo "$output" | grep "Thread:" | awk '{print $2}')
  THREAD_IDS+=($thread_id)
done

for thread_id in "${THREAD_IDS[@]}"; do
  python3 .../agent_skill.py confirm \
    --thread-id $thread_id \
    --download --output-dir ~/lovart-out/r1-dN &
done
wait
```

---

## 检测方法

### 文件存在 ≠ 生成成功

```bash
# 错误：只看文件是否存在
ls ~/lovart-out/r1-d1/*.png  # 文件存在，但可能是空白图

# 正确：检查文件内容
python3 -c "
from PIL import Image
img = Image.open('~/lovart-out/r1-d1/lovart_xxx.png')
img_small = img.resize((50, 50))
pixels = list(img_small.getdata())
white_count = sum(1 for p in pixels if p[0] > 240 and p[1] > 240 and p[2] > 240)
ratio = white_count / len(pixels)
print(f'White pixel ratio: {ratio:.1%}')
if ratio > 0.7:
    print('⚠️ LIKELY BLANK PLACEHOLDER!')
"
```

### 判定标准

| 白色像素比例 | 结论 | 行动 |
|-------------|------|------|
| > 70% | 空白占位图 | 重新执行 confirm |
| 30-70% | 正常（纯白背景产品图） | 通过 |
| < 30% | 正常（有内容） | 通过 |

---

## 禁止

- ❌ 看到 `Status: pending_confirmation` 就假设任务完成
- ❌ 只用 `ls` 检查文件存在就报告"生成成功"
- ❌ 用 `background=true` 并行启动 chat 而不处理 confirm
- ❌ 忽略 Lovart 返回的 `Thread:` ID

---

## 验证清单

- [ ] `chat` 输出包含 `Thread:` ID（已记录）
- [ ] `confirm` 输出包含 `Status: done`（非 `pending_confirmation`）
- [ ] 图片文件白色像素比例 < 70%
- [ ] 图片分辨率符合预期（2048×2048 或 1024×1024）

---

## 相关文件

- `references/guides/lovart-execution.md`: Lovart 执行指南（确认流程章节）
- `references/cases/pitfall-002-image-view-failure-loop.md`: 图片查看失败循环（同源问题）
