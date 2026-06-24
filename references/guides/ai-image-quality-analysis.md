---
reference_id: REF-GUIDE-AI-QUALITY-ANALYSIS
title: AI生成图片质量分析方法
category: guides
used_when:
  - 图片评审
  - AI生成质量评估
  - 突破AI天花板
called_by:
  - image-critique.md
  - pitfall-030-ai-product-ceiling.md
depends_on:
  - REF-GUIDE-PRODUCT-PROMPT
outputs:
  - image_quality_analysis
---

# AI生成图片质量分析方法

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: 用户要求"重新用模型识别图片"，发现vision工具无法使用
> **目标**: 提供不依赖vision工具的本地图片质量分析方法

---

## 问题背景

当需要分析AI生成图片质量时，可能遇到以下工具限制：
- **vision工具**: 可能因API认证失败无法使用
- **browser工具**: 可能因Chrome未安装无法使用
- **直接查看**: 需要复制到桌面后用系统查看器打开

**解决方案**: 使用Python+PIL进行本地图片质量分析

---

## 本地图片分析方法

### 方法1: 基础信息分析（Python+PIL）

```python
from PIL import Image
import os

# 读取图片
img_path = '/path/to/image.png'
img = Image.open(img_path)

# 基础信息
print(f"图片尺寸: {img.size[0]} x {img.size[1]} pixels")
print(f"图片格式: {img.format}")
print(f"图片模式: {img.mode}")
print(f"文件大小: {os.path.getsize(img_path) / 1024:.1f} KB")
print(f"宽高比: {img.size[0] / img.size[1]:.2f}")
```

### 方法2: 颜色分布分析

```python
# 获取像素数据
pixels = list(img.getdata())
width, height = img.size

# 计算平均颜色
r_sum = sum(p[0] for p in pixels)
g_sum = sum(p[1] for p in pixels)
b_sum = sum(p[2] for p in pixels)
total_pixels = len(pixels)

avg_r = r_sum / total_pixels
avg_g = g_sum / total_pixels
avg_b = b_sum / total_pixels

print(f"平均颜色 (RGB): {avg_r:.1f}, {avg_g:.1f}, {avg_b:.1f}")

# 判断背景
if avg_r > 200 and avg_g > 200 and avg_b > 200:
    print("背景: 浅色/白色背景 ✓")
else:
    print("背景: 深色背景")
```

### 方法3: 亮度分析

```python
# 计算亮度
brightness = [(p[0] + p[1] + p[2]) / 3 for p in pixels]
avg_brightness = sum(brightness) / len(brightness)
min_brightness = min(brightness)
max_brightness = max(brightness)

# 计算标准差
variance = sum((b - avg_brightness) ** 2 for b in brightness) / len(brightness)
std_brightness = variance ** 0.5

print(f"平均亮度: {avg_brightness:.1f}")
print(f"亮度范围: {min_brightness:.1f} - {max_brightness:.1f}")
print(f"亮度标准差: {std_brightness:.1f}")
```

### 方法4: 边缘清晰度分析（简化版）

```python
# 计算相邻像素差异
edge_scores = []
for y in range(0, height-1, 10):  # 每隔10行采样
    for x in range(0, width-1, 10):  # 每隔10列采样
        idx = y * width + x
        idx_right = y * width + (x + 1)
        idx_down = (y + 1) * width + x
        
        # 水平差异
        r_diff_h = abs(pixels[idx][0] - pixels[idx_right][0])
        g_diff_h = abs(pixels[idx][1] - pixels[idx_right][1])
        b_diff_h = abs(pixels[idx][2] - pixels[idx_right][2])
        
        # 垂直差异
        r_diff_v = abs(pixels[idx][0] - pixels[idx_down][0])
        g_diff_v = abs(pixels[idx][1] - pixels[idx_down][1])
        b_diff_v = abs(pixels[idx][2] - pixels[idx_down][2])
        
        edge_score = max(r_diff_h + g_diff_h + b_diff_h, 
                        r_diff_v + g_diff_v + b_diff_v)
        edge_scores.append(edge_score)

avg_edge = sum(edge_scores) / len(edge_scores)
max_edge = max(edge_scores)

print(f"边缘强度平均: {avg_edge:.2f}")
print(f"边缘强度最大: {max_edge:.2f}")
```

### 方法5: 综合质量评估

```python
# 综合评估
print("\n=== 图片质量评估 ===")

if img.size[0] >= 1024 and img.size[1] >= 1024:
    print("✓ 分辨率: 高分辨率 (>=1024px)")
else:
    print("✗ 分辨率: 低分辨率 (<1024px)")

if avg_edge > 10:
    print("✓ 边缘清晰度: 清晰")
else:
    print("✗ 边缘清晰度: 模糊")

if std_brightness > 30:
    print("✓ 对比度: 良好")
else:
    print("✗ 对比度: 低")
```

---

## 图片查看方法

### 方法1: 复制到桌面查看

```bash
cp ~/lovart-out/rN-dN/*.png ~/Desktop/
open ~/Desktop/*.png
```

### 方法2: 直接打开（macOS）

```bash
open ~/lovart-out/rN-dN/*.png
```

### 方法3: 生成缩略图对比

```python
from PIL import Image
import glob

# 生成缩略图对比
files = glob.glob('~/lovart-out/rN-dN/*.png')
for f in files:
    img = Image.open(f)
    thumb = img.thumbnail((256, 256))
    img.save(f.replace('.png', '_thumb.png'))
```

---

## 评审标准对照

### 边缘清晰度评估

| 边缘强度平均值 | 评估 | 说明 |
|--------------|------|------|
| > 15 | 非常清晰 | 产品级精度 |
| 10-15 | 清晰 | 可接受 |
| 5-10 | 模糊 | 概念级 |
| < 5 | 非常模糊 | 需要重新生成 |

### 对比度评估

| 亮度标准差 | 评估 | 说明 |
|-----------|------|------|
| > 60 | 高对比度 | 质感强烈 |
| 40-60 | 良好对比度 | 可接受 |
| 20-40 | 低对比度 | 质感平淡 |
| < 20 | 非常低对比度 | 需要重新生成 |

---

## 与vision工具的对比

| 能力 | vision工具 | 本地Python分析 |
|------|-----------|-------------|
| 材料质感识别 | ✅ 强 | ❌ 无法识别 |
| 功能细节识别 | ✅ 强 | ❌ 无法识别 |
| 形态分析 | ✅ 强 | ⚠️ 基础分析 |
| 边缘清晰度 | ⚠️ 一般 | ✅ 量化分析 |
| 对比度 | ⚠️ 一般 | ✅ 量化分析 |
| 分辨率 | ❌ 不报告 | ✅ 精确报告 |
| 颜色分布 | ⚠️ 一般 | ✅ 精确分析 |
| 可用性 | ❌ 可能失败 | ✅ 始终可用 |

**结论**: 本地Python分析是vision工具的可靠备选，尤其在vision不可用时。

---

## 检查清单

### 分析前

```
[ ] 图片是否已下载到本地？
[ ] Python和PIL是否可用？
[ ] 是否已准备好评审标准？
```

### 分析中

```
[ ] 是否分析了分辨率？
[ ] 是否分析了边缘清晰度？
[ ] 是否分析了对比度？
[ ] 是否分析了颜色分布？
[ ] 是否查看了图片（复制到桌面）？
```

### 分析后

```
[ ] 是否记录了量化数据？
[ ] 是否进行了人工视觉评审？
[ ] 是否对比了艾维设计标准？
[ ] 是否提供了改进建议？
```

---

## 来源

- 技能: jony-ive-design2me-v2
- 触发: 用户要求"重新用模型识别图片"
- 问题: vision工具API认证失败，browser工具Chrome未安装
- 解决: 使用Python+PIL进行本地图片质量分析
