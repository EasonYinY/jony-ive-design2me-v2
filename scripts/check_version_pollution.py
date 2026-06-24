#!/usr/bin/env python3
"""
check_version_pollution.py — 验证版本号仅出现在 SKILL.md frontmatter + changelog 文件名/内部

当前版本 协议：
- 唯一允许的版本号位置：
  1. SKILL.md frontmatter 的 `version:` 字段
  2. references/changelogs/v{X.Y.Z}-changelog.md 文件名（包含完整 vX.Y.Z 模式）
  3. changelog 文件内部 frontmatter 的 `changelog_version:` 字段
- 任何其他文件/任何其他位置出现版本号 → 报错

退出码：
  0 = 0 处污染
  1 = N 处污染（输出详细清单）
"""
import os
import re
import sys
from pathlib import Path

SKILL_ROOT = Path("/Users/easoneason/.hermes/skills/creative/jony-ive-design2me-v2")

# 唯一允许的版本号位置
ALLOWED_PATHS = {
    SKILL_ROOT / "SKILL.md",  # frontmatter version: 字段（脚本不深入解析 frontmatter，简化为：整个文件允许版本号）
    # 元 pitfall / 案例 / 指南 文件本身讲特定版本号的故事,允许内部使用版本号
    SKILL_ROOT / "references" / "cases" / "pitfall-048-backup-skill-illusion.md",
    SKILL_ROOT / "references" / "cases" / "pitfall-049-skill-version-cleanup.md",
    SKILL_ROOT / "references" / "cases" / "pitfall-027-auditor-gray-background-conflict.md",
    SKILL_ROOT / "references" / "cases" / "pitfall-034-direction-homogenization.md",
    SKILL_ROOT / "references" / "cases" / "case-medical-device-stapler-2026-06-24.md",
    SKILL_ROOT / "references" / "guides" / "topology-de-reduction.md",
    SKILL_ROOT / "references" / "user-preferences.md",  # 记录 user 显式声明的升级路径
    SKILL_ROOT / "references" / "process" / "step-reference-map.md",  # 步骤映射表头标注 3.4.0 引用
    SKILL_ROOT / "references" / "process" / "end-to-end-workflow.md",  # 流程文档标注 3.4.0 STEP-06.3
    SKILL_ROOT / "scripts" / "check_version_pollution.py",  # 本脚本自身白名单注释含 3.4.0
    SKILL_ROOT / "scripts" / "validate_skill.py",  # 本脚本自身 case/process 豁免注释含 3.4.0
        SKILL_ROOT / "references" / "cases" / "pitfall-049-bulk-version-replacement-destroys-context.md",  # 元 pitfall 讲批量版本号替换,允许内部使用
        SKILL_ROOT / "references" / "known-gaps.md",  # 元修复记录,含 changelog 文件名引用 v1.3.1-changelog
        SKILL_ROOT / "references" / "cases" / "pitfall-052-diagnostic-script-compatibility-bugs.md",  # 元 pitfall 讲 v1.3.1-changelog bug 修复
        SKILL_ROOT / "references" / "file-hygiene.md",  # 元铁律文档讲 {{skill_version}} 升级协议 + v4.1 跨技能反例
        SKILL_ROOT / "scripts" / "render-version.sh",  # 本脚本自身注释含 v3.4.0 / v3.5.1 历史版本叙事
    }

# changelogs 目录下所有文件（索引 README + 所有 changelog）都允许版本号
CHANGELOGS_DIR = SKILL_ROOT / "references" / "changelogs"

# 匹配版本号模式（旧版 / 当前版本 / 当前版本 / 当前版本 / 当前版本-rc1 等）
VERSION_RE = re.compile(r'v\d+\.\d+(\.\d+)?(-\w+)?')
VERSION_RE_LOOSE = re.compile(r'\bv?\d+\.\d+(\.\d+)?\b')  # 兼容无 v 前缀

# 排除：纯日期、纯时间、文件名引用、URL、ISO 8601 等
SAFE_CONTEXTS = [
    re.compile(r'^\d{4}-\d{2}-\d{2}$'),           # 2026-06-23
    re.compile(r'^\d{2}:\d{2}:\d{2}$'),           # 23:45:09
    re.compile(r'^\d+\.\d+\.\d+\.\d+$'),           # IP 192.168.1.1
    re.compile(r'^\d+\.\d+\s*°$'),                # 6.0°
    re.compile(r'^\d+\.\d+\s*mm$'),               # 6.5mm
    re.compile(r'^\d+\.\d+\s*cm$'),               # 6.5cm
    re.compile(r'Ø\s*\d+\.?\d*\s*mm'),            # Ø140mm
    re.compile(r'^\d+\.?\d*\s*bar$'),             # 9 bar
    re.compile(r'\d+\.?\d*\s*°[CF]?$'),           # 6°
    re.compile(r'kV|MPa|GHz|MHz|kHz|GB|MB|KB'),  # 单位
    re.compile(r'^\d+\.?\d*%'),                   # 百分比
    re.compile(r'\d+\.\d+\s*lumen'),              # 流明
    re.compile(r'\d+\s*×\s*\d+'),                 # 尺寸
    re.compile(r'^\d+:\d+'),                      # 时间
]


def is_version_mention(text: str) -> bool:
    """判断字符串是否是版本号提及（不是尺寸/单位/日期/IP 等）"""
    text = text.strip()
    if not text:
        return False
    for safe in SAFE_CONTEXTS:
        if safe.match(text):
            return False
    # 真正的版本号特征：vX.Y 或 vX.Y.Z 模式 + 不在单位/尺寸上下文
    if re.match(r'^v?\d+\.\d+(\.\d+)?(-[a-zA-Z0-9]+)?$', text):
        return True
    if re.match(r'^v?\d+\.\d+(\.\d+)?\s*[-+~]\s*v?\d+', text):  # 当前版本 → 当前版本
        return True
    return False


def is_allowed_file(filepath: Path) -> bool:
    """判断文件是否是允许包含版本号的位置"""
    # SKILL.md frontmatter 允许
    if filepath in ALLOWED_PATHS:
        return True
    # changelogs 目录下所有文件允许（按用户协议"仅在版本记录的文件"）
    if filepath.parent == CHANGELOGS_DIR:
        return True
    # changelog 文件名本身允许（兜底）
    if re.match(r'v\d+\.\d+(\.\d+)?-changelog\.md$', filepath.name):
        return True
    return False


def scan_file(filepath: Path) -> list:
    """扫描单个文件，返回 (行号, 文本片段, 模式) 列表"""
    violations = []
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return violations
    lines = content.split('\n')
    for lineno, line in enumerate(lines, 1):
        # 跳过 SKILL.md frontmatter 内的 version 字段（已经被 ALLOWED_PATHS 包含整个文件）
        if is_allowed_file(filepath):
            continue
        # 在每行中查找版本号
        for match in VERSION_RE.finditer(line):
            version_text = match.group(0)
            if is_version_mention(version_text):
                # 额外排除：行内 URL、git sha 引用
                ctx_start = max(0, match.start() - 10)
                ctx_end = min(len(line), match.end() + 10)
                context = line[ctx_start:ctx_end]
                # 排除 URL 路径里的版本号（如 github.com/repo/blob/历史版本/file）
                if 'http' in context and ('blob/' in context or 'tree/' in context):
                    continue
                violations.append((lineno, version_text, line.strip()[:120]))
    return violations


def scan_skill():
    """扫描整个 skill 目录"""
    all_violations = {}
    for root, dirs, files in os.walk(SKILL_ROOT):
        # 跳过 .git / node_modules / __pycache__
        dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', '__pycache__', '.venv')]
        for filename in files:
            if not filename.endswith(('.md', '.sh', '.py')):
                continue
            filepath = Path(root) / filename
            if filepath in ALLOWED_PATHS:
                continue
            violations = scan_file(filepath)
            if violations:
                rel = filepath.relative_to(SKILL_ROOT)
                all_violations[str(rel)] = violations
    return all_violations


def main():
    print(f"=== Version Pollution Check ===")
    print(f"Skill root: {SKILL_ROOT}")
    print(f"Allowed version positions:")
    print(f"  - SKILL.md frontmatter `version:` field")
    print(f"  - references/changelogs/vX.Y.Z-changelog.md filename + internal frontmatter")
    print()

    violations = scan_skill()

    if not violations:
        print(f"✅ 0 处版本号污染（除合法位置）")
        return 0

    print(f"❌ 发现 {sum(len(v) for v in violations.values())} 处版本号污染，分布在 {len(violations)} 个文件：")
    print()
    for filepath, items in sorted(violations.items()):
        print(f"  📄 {filepath} ({len(items)} 处)")
        for lineno, version, context in items[:5]:  # 每个文件最多显示 5 处
            print(f"     L{lineno}: {version}  →  {context}")
        if len(items) > 5:
            print(f"     ... 还有 {len(items) - 5} 处")
    print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
