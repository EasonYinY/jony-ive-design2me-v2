---
reference_id: PITFALL-062
title: Lovart 生成超时恢复（Timeout Recovery）
category: cases
used_when:
  - IMAGE-GENERATION
  - LOVART-EXECUTION
called_by:
  - lovart-skill
depends_on:
  - REF-PROCESS-001
outputs:
  - timeout_recovery_procedure
---

# Pitfall 062: Lovart 生成超时恢复

> **日期**: 2026-06-25
> **触发**: MRI 任务 D-03 方向生成时，Lovart chat 命令在 180s 超时限制内未完成，返回 `final_status: timeout`
> **严重级别**: MEDIUM — 可恢复，但需手动处理

## 现象

```bash
# 后台运行 Lovart chat
python3 agent_skill.py chat --prompt "..." --download --output-dir ~/lovart-out/...

# 等待超时后输出
{
  "thread_id": "872cd3e8-5063-46b4-a39a-209be990ca39",
  "status": "running",
  "items": [],
  "final_status": "timeout",
  "project_id": "...",
  "downloaded": []
}
```

- 进程 exit_code = 0（不是失败）
- `final_status` = `timeout`（不是 `failed`）
- 无 artifacts 下载

## 根因

1. Lovart 后台生成仍在进行中（`status: running`）
2. 本地等待超时（180s 限制）不等于 Lovart 生成失败
3. 需要后续轮询获取结果

## 恢复步骤

### 步骤 1：轮询结果（result 命令）

```bash
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py \
  result --thread-id 872cd3e8-5063-46b4-a39a-209be990ca39 --json
```

- 每 30-60 秒轮询一次
- 直到 `status` 变为 `done` 且 `items` 包含 artifacts

### 步骤 2：手动下载图片

当 result 返回 artifacts URL 后：

```bash
curl -L --max-time 180 -o ~/lovart-out/<dir>/lovart_<hash>.png \
  "https://a.lovart.ai/artifacts/agent/<hash>.png"
```

- `--max-time 180`：大文件（4K 图片约 4MB）可能需要较长时间
- 检查文件大小：`ls -la` 确认非零

### 步骤 3：继续 Eagle 发布流程

下载完成后，按正常流程执行 `eagle_publish.sh publish-images`

## 检查清单

- [ ] thread_id 已记录？
- [ ] result 轮询显示 status=done？
- [ ] artifacts URL 已提取？
- [ ] curl 下载成功（文件大小 > 0）？
- [ ] 文件是有效 PNG（不是 HTML 错误页）？
- [ ] Eagle publish 已完成？

## 来源

- 2026-06-25 MRI 干磁体3T核磁共振扫描设备任务 D-03 方向
- Lovart skill v2.x 超时处理经验
