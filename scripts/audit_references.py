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
    _local_link_issues,
)


CLAIM_ID = re.compile(r"\b(?:GOV|BND|MTH|FCT)-\d{3}\b")
POSITIVE_HEADING = re.compile(
    r"^## ((?:GOV|BND|MTH|FCT)-\d{3})\b", re.MULTILINE
)
ALLOWED_RUNTIME_STATUSES = frozenset({"VERIFIED", "GOVERNING"})


def audit_references(skill_root: Path, ledger_path: Path) -> Tuple[str, ...]:
    """返回 reference 审计问题；不修改来源账本或运行文件。"""

    root = Path(skill_root)
    reference_root = root / "references"
    issues: Tuple[str, ...] = ()
    reference_paths = tuple(sorted(reference_root.rglob("*.md")))
    actual_names = frozenset(
        path.relative_to(reference_root).as_posix() for path in reference_paths
    )
    if actual_names != REQUIRED_REFERENCES:
        for name in sorted(REQUIRED_REFERENCES - actual_names):
            issues += (f"缺少固定运行 reference：{name}",)
        for name in sorted(actual_names - REQUIRED_REFERENCES):
            issues += (f"存在计划外运行 reference：{name}",)

    with Path(ledger_path).open(encoding="utf-8", newline="") as handle:
        rows = tuple(csv.DictReader(handle))
    ledger = {row["claim_id"]: row for row in rows}

    by_basename = {path.name: path for path in reference_paths}
    for reference_path in reference_paths:
        text = reference_path.read_text(encoding="utf-8")
        issues += _local_link_issues(reference_path, root)
        for forbidden in FORBIDDEN_RUNTIME_TEXT:
            if forbidden in text:
                issues += (f"{reference_path.name} 含禁止运行文本：{forbidden}",)
        for pattern, label in FORBIDDEN_RUNTIME_PATTERNS:
            if pattern.search(text):
                issues += (f"{reference_path.name} 含{label}。",)
        for claim_id in POSITIVE_HEADING.findall(text):
            row = ledger.get(claim_id)
            if row is None:
                issues += (f"{reference_path.name} 的 {claim_id} 未登记来源账本。",)
            elif row["status"] not in ALLOWED_RUNTIME_STATUSES:
                issues += (f"{reference_path.name} 将未验证的 {claim_id} 作为正向条目。",)
            elif row["target_reference"] != reference_path.name:
                issues += (f"{claim_id} 的目标 reference 与来源账本不一致。",)

    for row in rows:
        if row["status"] not in ALLOWED_RUNTIME_STATUSES:
            continue
        target = by_basename.get(row["target_reference"])
        if target is None or not target.is_file():
            issues += (f"{row['claim_id']} 指向不存在的 {row['target_reference']}。",)
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
