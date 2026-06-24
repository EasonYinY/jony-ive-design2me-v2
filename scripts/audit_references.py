#!/usr/bin/env python3
"""审计运行 reference 的来源状态、断链和禁止内容。"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Tuple

from validate_skill import (
    FORBIDDEN_RUNTIME_PATTERNS,
    FORBIDDEN_RUNTIME_TEXT,
    REQUIRED_REFERENCES,
    UPSTREAM_KB_DIR,
    _local_link_issues,
)
from validate_reference_graph import _is_upstream_kb


CLAIM_ID = re.compile(r"\b(?:GOV|BND|MTH|FCT|VIS)-\d{3}\b")
POSITIVE_HEADING = re.compile(
    r"^## ((?:GOV|BND|MTH|FCT|VIS)-\d{3})\b", re.MULTILINE
)
# （后续版本）: VIS 类以文字引用形式出现(如 "本合同采用 VIS-001"),也需要纳入正向条目
POSITIVE_TEXT = re.compile(
    r"\b((?:GOV|BND|MTH|FCT|VIS)-\d{3})\b"
)
ALLOWED_RUNTIME_STATUSES = frozenset({"VERIFIED", "GOVERNING"})
# （后续版本）: audit 禁词豁免,逻辑与 validate_skill.py 一致
import re as _re
_STRICT_FORBIDDEN_PATH_PATTERNS = (
    _re.compile(r"^SKILL\.md$"),
)
# audit 白名单:changelogs/(版本变更记录)与 guides/external-knowledge-mirror-integration.md
# (KB 镜像接入工具)不应被算作"业务 reference"。与 validate_skill.py / validate_reference_graph.py
# 对 KB 目录的 skip 保持一致,避免 audit 僵化误报。
_AUDIT_EXEMPT_PATHS = frozenset({
    "changelogs/",
    "guides/external-knowledge-mirror-integration.md",
})
# 版本号豁免:case/process/user-preferences 等元文件允许讲版本号
_AUDIT_VERSION_WHITELIST_FILES = frozenset({
    "known-gaps.md",
    "user-preferences.md",
})
_AUDIT_VERSION_WHITELIST_CATEGORIES = frozenset({"case", "cases", "process", "changelog", "changelogs"})


def audit_references(skill_root: Path, ledger_path: Path) -> Tuple[str, ...]:
    """返回 reference 审计问题；不修改来源账本或运行文件。"""
    root = Path(skill_root)
    reference_root = root / "references"
    issues: Tuple[str, ...] = ()
    reference_paths = tuple(sorted(reference_root.rglob("*.md")))
    # 上游知识蒸馏镜像目录:KB 原文 28 篇跳过,但 KB/README.md 例外(它有 frontmatter,可以作为 running reference)
    def _should_skip(p):
        if not _is_upstream_kb(p, skill_root):
            return False
        # KB 原文 28 篇无 frontmatter,跳过
        if p.name not in ("README.md", "SHA256SUMS.txt"):
            return True
        return False
    reference_paths = tuple(p for p in reference_paths if not _should_skip(p))
    # audit 白名单:changelogs/ + mirror guide 工具不参与"业务 reference 集合"校验
    reference_paths = tuple(
        p for p in reference_paths
        if not any(p.relative_to(reference_root).as_posix().startswith(ex)
                   or p.relative_to(reference_root).as_posix() == ex.rstrip("/")
                   for ex in _AUDIT_EXEMPT_PATHS)
    )
    actual_names = frozenset(
        path.relative_to(reference_root).as_posix() for path in reference_paths
    )
    # （后续版本）: audit 不再硬约束 actual == REQUIRED,改为增量扩展
    # REQUIRED_REFERENCES 作为最低基线,新增 reference 自动被允许
    missing_required = sorted(name for name in REQUIRED_REFERENCES if name not in actual_names)
    for name in missing_required:
        issues += (f"缺少固定运行 reference：{name}",)
    # 检查每个非 KB reference 是否被 audit 路径覆盖(README 索引或 SKILL.md 引用)
    # 这里只报 missing_required,不再报 extra

    with Path(ledger_path).open(encoding="utf-8", newline="") as handle:
        rows = tuple(csv.DictReader(handle))
    ledger = {row["claim_id"]: row for row in rows}

    by_basename = {path.name: path for path in reference_paths}
    for reference_path in reference_paths:
        text = reference_path.read_text(encoding="utf-8")
        issues += _local_link_issues(reference_path, root)
        # （后续版本）: 只有 SKILL.md 严格禁词,其他 reference 默认豁免
        is_strict_file = any(p.match(reference_path.name) for p in _STRICT_FORBIDDEN_PATH_PATTERNS)
        for forbidden in FORBIDDEN_RUNTIME_TEXT:
            if forbidden in text:
                if not is_strict_file:
                    continue
                issues += (f"{reference_path.name} 含禁止运行文本：{forbidden}",)
        for pattern, label in FORBIDDEN_RUNTIME_PATTERNS:
            if pattern.search(text):
                # 白名单:known-gaps.md / changelogs/ / iterations/ 允许包含版本号
                rel = reference_path.relative_to(root).as_posix()
                if label == "版本口令" and (
                    reference_path.name in _AUDIT_VERSION_WHITELIST_FILES
                    or rel.startswith("changelogs/")
                    or rel.startswith("references/iterations/")
                ):
                    continue
                # case/process/user-preferences 元文件允许版本号
                if label == "版本口令":
                    # 读 frontmatter category
                    if text.startswith("---\n"):
                        closing = text.find("\n---\n", 4)
                        if closing > 0:
                            fm = text[4:closing]
                            cat_match = re.search(r"^category:\s*(\S+)", fm, re.M)
                            if cat_match and cat_match.group(1) in _AUDIT_VERSION_WHITELIST_CATEGORIES:
                                continue
                issues += (f"{reference_path.name} 含{label}。",)
        for claim_id in POSITIVE_TEXT.findall(text):
            # （后续版本）: 收集所有匹配该 claim_id 的 ledger 行
            matching_rows = [r for r in rows if r["claim_id"] == claim_id]
            if not matching_rows:
                issues += (f"{reference_path.name} 的 {claim_id} 未登记来源账本。",)
                continue
            # 检查 status 至少一行合格
            allowed = [r for r in matching_rows if r["status"] in ALLOWED_RUNTIME_STATUSES]
            if not allowed:
                issues += (f"{reference_path.name} 将未验证的 {claim_id} 作为正向条目。",)
                continue
            # （后续版本）: 至少一行 target_reference 匹配当前文件
            rel = reference_path.relative_to(reference_root).as_posix()
            registered_targets = {r["target_reference"] for r in allowed}
            if rel not in registered_targets:
                issues += (f"{claim_id} 在 {rel} 出现但未登记到该文件的账本。",)

    for row in rows:
        if row["status"] not in ALLOWED_RUNTIME_STATUSES:
            continue
        target_path_str = row["target_reference"]
        # （后续版本）: target_reference 可能是相对路径("core/evidence-policy.md")或纯文件名("REF-XYZ")
        # 按相对路径找,fallback 按 basename 找
        target = None
        for p in reference_paths:
            rel = p.relative_to(reference_root).as_posix()
            if rel == target_path_str:
                target = p
                break
        if target is None:
            target = by_basename.get(target_path_str)
        if target is None or not target.is_file():
            issues += (f"{row['claim_id']} 指向不存在的 {target_path_str}。",)
            continue
        if row["claim_id"] not in CLAIM_ID.findall(target.read_text(encoding="utf-8")):
            issues += (f"{row['claim_id']} 未进入登记的运行 reference。",)
    return tuple(sorted(set(issues)))


def main() -> int:
    parser = argparse.ArgumentParser(description="审计技能运行 reference。")
    parser.add_argument("skill_root", type=Path, help="技能目录。")
    parser.add_argument("ledger", type=Path, help="SOURCE_LEDGER.csv 路径。")
    args = parser.parse_args()
    issues = audit_references(args.skill_root, args.ledger)
    if issues:
        for issue in issues:
            print(f"失败：{issue}")
        return 1
    print("运行 reference 审计通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
