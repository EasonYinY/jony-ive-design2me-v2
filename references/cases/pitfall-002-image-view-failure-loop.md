---
reference_id: PITFALL-002
title: 图片查看失败循环（Image View Failure Loop）
category: cases
used_when:
  - IMAGE-REVIEW
  - POST-GENERATION
called_by:
  - lovart-execution
depends_on:
  - REF-PROCESS-003
outputs:
  - image_view_workaround
---

# Pitfall 002: 图片查看失败循环

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 用户要求"将图片贴出来然后进行评审"时，agent 反复尝试 browser_navigate 访问 file:// 路径失败

---

## 现象

1. Lovart 图片生成成功，文件保存到 `~/lovart-out/rN-dN/`
2. 用户要求查看图片
3. Agent 尝试 `browser_navigate("file:///Users/.../image.png")` → 失败（Chrome not found）
4. Agent 重复尝试相同命令 → 进入循环
5. Agent 尝试 `vision` 工具读取本地文件 → 可能失败或返回空结果
6. Agent 尝试 `delegate_task` + `vision` → 子 agent 也失败

## 根本原因

- **browser 工具**: 依赖 Chrome/Puppeteer/Playwright，当前 macOS 环境未安装
- **vision 工具**: 可能无法直接读取本地文件系统上的图片（`No LLM provider configured for task=vision`）
- **file:// 协议**: 现代浏览器安全策略限制本地文件访问
- **Lovart pending_confirmation**: 图片生成任务需要显式 `confirm` 才能执行，否则产生空白占位图（见 REF-GUIDE-010 §确认流程）

## 解决方案

### 推荐做法（macOS）

```bash
# 将图片复制到桌面并打开
cp ~/lovart-out/rN-dN/*.png ~/Desktop/
open ~/Desktop/*.png

# 或直接打开原文件
open ~/lovart-out/rN-dN/*.png
```

### 备选做法

```bash
# 用系统预览打开单张图片
open ~/lovart-out/rN-d1/lovart_xxxx.png
```

### 评审方式

无法直接查看图片时，基于以下信息进行评审：

1. **文件信息**: `ls -la` 查看分辨率、大小
2. **Lovart 生成日志**: 包含 AI 对生成结果的描述
3. **PIL 读取**: 用 Python 读取图片尺寸和基本属性
4. **用户反馈**: 请用户直接描述图片内容

### 空白/占位图检测（2026-06-24 飞行器任务实证）

当 `vision_analyze` 不可用时，用 Python 快速检测图片是否真正包含内容：

```python
from PIL import Image

for f in ['r1-d1.png', 'r1-d2.png', 'r1-d3.png']:
    img = Image.open(f)
    img_small = img.resize((50, 50))
    pixels = list(img_small.getdata())
    white_count = sum(1 for p in pixels if p[0] > 240 and p[1] > 240 and p[2] > 240)
    ratio = white_count / len(pixels)
    print(f'{f}: {ratio:.1%} white pixels')
    if ratio > 0.7:
        print(f'  ⚠️ WARNING: Likely blank/placeholder image!')
```

**判定标准**：
- > 70% 白色像素 → 极可能是空白占位图（Lovart `pending_confirmation` 未处理）
- 30-70% 白色像素 → 正常（纯白背景产品图）
- < 30% 白色像素 → 正常（有内容）

### vision_analyze 工具不可用的应对（2026-06-24 电动剃须刀任务实证）

**现象**: `vision_analyze` 返回错误 `No LLM provider configured for task=vision provider=auto`。

**应对流程**:
1. **不要重复尝试 vision_analyze**（已知会失败，进入同工具失败循环）
2. **立即切换到 `open` 命令**: `open ~/lovart-out/rN-dN/*.png` 在 macOS 上直接打开系统预览
3. **基于 Lovart 生成日志进行文本评审**: Lovart 返回的 assistant 描述包含对生成结果的详细说明，可作为评审依据
4. **请用户直接查看并反馈**: 图片已在用户桌面/预览中打开，用户可直接提供视觉反馈

**禁止**: 在 vision_analyze 失败后继续尝试 browser_navigate、delegate_task+vision 等其他工具路径——这些路径在相同环境下同样受限。

## 禁止做法

- ❌ 反复尝试 `browser_navigate("file://...")`（已知会失败）
- ❌ 反复尝试相同参数的 `vision` 调用（可能进入循环）
- ❌ 使用 `delegate_task` 将图片查看委托给子 agent（子 agent 同样受限）

## 相关文件

- `references/guides/lovart-execution.md`: Lovart 执行指南
- `references/quality/image-critique.md`: 图片评审流程

---
