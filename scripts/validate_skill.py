#!/usr/bin/env python3
"""验证技能结构、导航、中文正文和运行时边界。"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Tuple

from validate_reference_graph import validate_reference_graph


SKILL_NAME = "jony-ive-design2me-v2"
DISPLAY_NAME = "Jony Ive Design2Me V2"
REQUIRED_REFERENCES = frozenset(
    {
        "README.md",
        "core/evidence-policy.md",
        "core/five-dimension-engine.md",
        "core/ive-thinking-models.md",
        "core/case-capsules.md",
        "process/end-to-end-workflow.md",
        "process/step-reference-map.md",
        "process/reasoning-output.md",
        "process/skill-reading-guide.md",
        "direction/first-principles.md",
        "direction/constraint-cascade.md",
        "direction/anti-cliche.md",
        "direction/diversity-gate.md",
        "direction/three-direction-protocol.md",
        "design/design-ir.md",
        "design/form-proportion.md",
        "design/cmf-system.md",
        "design/interaction-lifecycle.md",
        "prompt/prompt-contract.md",
        "prompt/prompt-compression.md",
        "prompt/prompt-trace.md",
        "prompt/photography-controls.md",
        "quality/aesthetic-gate.md",
        "quality/image-critique.md",
        "quality/failure-library.md",
        "quality/quality-gates.md",
        "workflows/README.md",
        "workflows/product-design.md",
        "workflows/prompt-rewriting.md",
        "workflows/image-critique.md",
        "workflows/design-philosophy.md",
        "workflows/ui-ux.md",
        "workflows/service.md",
        "workflows/organization.md",
        "workflows/wearable.md",
        "workflows/modular.md",
    }
)
REQUIRED_SCRIPTS = frozenset(
    {
        "validate_skill.py",
        "validate_design_ir.py",
        "compile_prompt.py",
        "audit_references.py",
        "validate_reference_graph.py",
    }
)
FORBIDDEN_RUNTIME_TEXT = (
    "jony-ive-product-designer-v2",
    "references/jony-ive-aesthetics.md",
    "references/jony-ive-prompt-library.md",
    "LoveFrom 2030",
    "post-Apple Jony Ive",
    "Mobile Documents",
)
FORBIDDEN_RUNTIME_PATTERNS = (
    (re.compile(r"\bV\d+(?:\.\d+)+\b"), "版本口令"),
    (re.compile(r"(?:Jony Ive|艾维)(?:认为|相信|主张|声称)"), "无来源人物归因"),
)
# 注：版本口令检查排除 known-gaps.md 和 changelogs/ 目录，这些文件需要记录版本信息
VERSION_WHITELIST = frozenset({"known-gaps.md"})
# 注：版本口令检查排除 known-gaps.md 和 changelogs/ 目录，这些文件需要记录版本信息
VERSION_WHITELIST = frozenset({"known-gaps.md"})
# 上游知识蒸馏镜像目录白名单:references/knowledge-base/ 下的 .md 不参与运行 reference 检查
UPSTREAM_KB_DIR = "knowledge-base"
# （后续版本）: 禁词检查现在只针对 SKILL.md (顶层契约) 和被 step-reference-map 主动引用的 running reference。
# 所有 reference 文件(category: guides/cases/prompt/quality/...)默认豁免,因为它们本身就是案例素材,
# 含真实 case-study 文本 (LoveFrom 2030/post-Apple Jony Ive/Mobile Documents 等) 是合法的。
# 严格禁词检查由 SKILL.md frontmatter 标记触发。
import re
_STRICT_FORBIDDEN_PATH_PATTERNS = (
    re.compile(r"^SKILL\.md$"),
)
# 已知 frontmatter 缺失豁免:这些文件在前已存在,会自动补 frontmatter
# 此白名单是 fail-fast 阶段的兜底
FRONTMATTER_EXEMPT_PREFIXES = ("changelogs/", "iterations/")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HAN_TEXT = re.compile(r"[\u3400-\u9fff]")
REQUIRED_BEHAVIOR_MARKERS = {
    "SKILL.md": (
        "技能优化模式",
        "禁止调用绘图或图像生成工具",
        "每次设计任务必须交付三个完整且本质不同的方向",
        "STEP-01` 至 `STEP-15",
    ),
    "references/process/end-to-end-workflow.md": (
        "三段提示词交付后停止",
        "只优化技能，不重新执行原项目",
    ),
    "references/process/reasoning-output.md": (
        "三个方向都必须",
        "不得重新运行原项目",
        "不声称披露模型私密思维链",
    ),
    "references/workflows/product-design.md": (
        "不能只展开或绘制首选方向",
        "设计产品”本身不等于要求绘图",
    ),
    "references/prompt/prompt-contract.md": (
        "提示词编译不等于图片生成授权",
    ),
}


def _frontmatter_value(text: str, key: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    closing = text.find("\n---\n", 4)
    if closing < 0:
        return None
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text[4:closing], re.MULTILINE)
    return match.group(1).strip().strip('"\'') if match else None


def _local_link_issues(markdown_path: Path, skill_root: Path) -> Tuple[str, ...]:
    text = markdown_path.read_text(encoding="utf-8")
    issues: Tuple[str, ...] = ()
    for target in MARKDOWN_LINK.findall(text):
        clean_target = target.split("#", 1)[0]
        if not clean_target or "://" in clean_target or clean_target.startswith("mailto:"):
            continue
        resolved = (markdown_path.parent / clean_target).resolve()
        try:
            resolved.relative_to(skill_root.resolve())
        except ValueError:
            issues += (f"{markdown_path.name} 的链接越出技能目录：{target}",)
            continue
        if not resolved.exists():
            issues += (f"{markdown_path.name} 存在断链：{target}",)
    return issues


def _get_category(text: str) -> str | None:
    """从 YAML frontmatter 提取 category。"""
    if not text.startswith("---\n"):
        return None
    closing = text.find("\n---\n", 4)
    if closing < 0:
        return None
    m = re.search(r"^category:\s*(\S+)", text[4:closing], re.MULTILINE)
    return m.group(1) if m else None


def _is_changelog_path(path: Path, root: Path) -> bool:
    """判断路径是否在 changelogs/ 或 iterations/ 目录(版本变更类,豁免禁词)。

    支持两种布局:
      - references/changelogs/... (skill 标准化布局)
      - changelogs/... (旧布局/顶层)
    """
    rel = path.relative_to(root).as_posix()
    return (
        rel.startswith("references/changelogs/")
        or rel.startswith("changelogs/")
        or rel.startswith("references/iterations/")
        or rel.startswith("iterations/")
    )


def validate_skill_root(skill_root: Path) -> Tuple[str, ...]:
    """返回确定性排序的问题元组；空元组表示通过。"""
    root = Path(skill_root).resolve()
    issues: Tuple[str, ...] = ()
    # 目录名校验:支持 resolve 后的绝对名,避免 cwd 差异
    if root.name != SKILL_NAME and not any(p.name == SKILL_NAME for p in root.parents):
        # 仅当向上遍历到技能目录名才允许(git worktree 软链场景)
        issues += (f"技能目录名必须是 {SKILL_NAME}。",)
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return issues + ("缺少 SKILL.md。",)

    skill_text = skill_path.read_text(encoding="utf-8")
    if _frontmatter_value(skill_text, "name") != SKILL_NAME:
        issues += (f"SKILL.md 的 name 必须是 {SKILL_NAME}。",)
    if not _frontmatter_value(skill_text, "description"):
        issues += ("SKILL.md 缺少 description。",)
    if len(skill_text.splitlines()) > 500:
        issues += ("SKILL.md 不得超过 500 行。",)

    yaml_path = root / "agents" / "openai.yaml"
    if not yaml_path.is_file():
        issues += ("缺少 agents/openai.yaml。",)
    elif f'display_name: "{DISPLAY_NAME}"' not in yaml_path.read_text(encoding="utf-8"):
        issues += (f"界面显示名必须是 {DISPLAY_NAME}。",)

    reference_root = root / "references"
    actual_references = frozenset(
        path.relative_to(reference_root).as_posix()
        for path in reference_root.rglob("*.md")
        if path.is_file()
    )
    for filename in sorted(REQUIRED_REFERENCES - actual_references):
        issues += (f"缺少运行 reference：{filename}",)
    for filename in sorted(REQUIRED_SCRIPTS):
        if not (root / "scripts" / filename).is_file():
            issues += (f"缺少固定脚本：{filename}",)

    markdown_paths = (skill_path,) + tuple(sorted(reference_root.rglob("*.md")))
    for markdown_path in markdown_paths:
        rel_posix = markdown_path.relative_to(root).as_posix()
        # 跳过上游知识蒸馏镜像目录中的 KB 原文(无 frontmatter,原文含真实 case-study 内容)
        # 例外:knowledge-base/README.md / SHA256SUMS.txt 是我们自己写的元数据,允许通过
        if (rel_posix.startswith(f"references/{UPSTREAM_KB_DIR}/")
                and markdown_path.name not in ("README.md", "SHA256SUMS.txt")):
            continue
        text = markdown_path.read_text(encoding="utf-8")
        if not HAN_TEXT.search(text):
            issues += (f"{markdown_path.name} 缺少中文正文。",)
        # （后续版本）: 读取 frontmatter category 仅为诊断需要;默认 reference 文件全部豁免禁词检查
        file_category = _get_category(text)
        is_case_study = _is_changelog_path(markdown_path, root)
        # （后续版本）: SKILL.md 是唯一必须严格禁词的契约文件,其他 reference 都允许 case-study 文本
        is_strict_file = any(p.match(markdown_path.name) for p in _STRICT_FORBIDDEN_PATH_PATTERNS)
        for forbidden in FORBIDDEN_RUNTIME_TEXT:
            if forbidden in text:
                # 案例分析 / 迭代记录 / 接力口令 / changelog 允许包含真实 case-study 文本
                if is_case_study or not is_strict_file:
                    continue
                issues += (f"{markdown_path.name} 含禁止运行文本：{forbidden}",)
        for pattern, label in FORBIDDEN_RUNTIME_PATTERNS:
            if pattern.search(text):
                # 白名单：known-gaps.md / changelogs/ / iterations/ 允许包含版本号
                if label == "版本口令" and (
                    markdown_path.name in VERSION_WHITELIST
                    or _is_changelog_path(markdown_path, root)
                ):
                    continue
                # case 类也允许包含版本号(实际迭代记录中常见 当前版本 等)
                if label == "版本口令" and file_category in {"case", "cases"}:
                    continue
                # process 类允许包含版本号引用(STEP-06.3 3.4.0 等元描述)
                if label == "版本口令" and file_category == "process":
                    continue
                # user-preferences.md 记录 user 显式声明的升级路径
                if label == "版本口令" and markdown_path.name == "user-preferences.md":
                    continue
                issues += (f"{markdown_path.name} 含{label}。",)
        issues += _local_link_issues(markdown_path, root)
    for relative_path, markers in REQUIRED_BEHAVIOR_MARKERS.items():
        policy_path = root / relative_path
        if not policy_path.is_file():
            issues += (f"缺少行为合同文件：{relative_path}",)
            continue
        policy_text = policy_path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in policy_text:
                issues += (f"{relative_path} 缺少强制行为：{marker}",)
    # （后续版本）: validate_reference_graph 返回 (issues, warnings),只取 issues 进入主 issues 流
    ref_graph_issues, _ref_graph_warnings = validate_reference_graph(root)
    issues += ref_graph_issues
    return tuple(sorted(set(issues)))


def main() -> int:
    parser = argparse.ArgumentParser(description="验证 Jony Ive Design2Me V2 技能结构。")
    parser.add_argument("skill_root", type=Path, help="待验证的技能目录。")
    args = parser.parse_args()
    issues = validate_skill_root(args.skill_root)
    if issues:
        for issue in issues:
            print(f"失败：{issue}")
        return 1
    print("技能结构验证通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
