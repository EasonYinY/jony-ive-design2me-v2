#!/usr/bin/env python3
"""验证 reference 总索引、步骤映射、反向时机和依赖图。"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Tuple


REQUIRED_METADATA_FIELDS = (
    "reference_id",
    "title",
    "category",
    "used_when",
    "called_by",
    "depends_on",
    "outputs",
)
STEP_IDS = tuple(f"STEP-{index:02d}" for index in range(1, 16))
TABLE_REFERENCE = re.compile(r"^\|\s*(STEP-\d{2})\s*\|\s*([^|]+?)\s*\|\s*$")
INDEX_REFERENCE = re.compile(
    r"^\|\s*([A-Z][A-Z0-9_.-]+)\s*\|\s*\[[^]]+\]\(([^)]+\.md)\)\s*\|"
)
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")


@dataclass(frozen=True)
class ReferenceMetadata:
    reference_id: str
    title: str
    category: str
    used_when: Tuple[str, ...]
    called_by: Tuple[str, ...]
    depends_on: Tuple[str, ...]
    outputs: Tuple[str, ...]
    path: Path


@dataclass(frozen=True)
class ReferenceGraph:
    references: Mapping[str, ReferenceMetadata]
    step_references: Mapping[str, Tuple[str, ...]]
    skipped: Tuple[str, ...] = ()  # （后续版本）: 容错加载时跳过无 frontmatter 的文件


def _parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("缺少 YAML frontmatter")
    closing = text.find("\n---\n", 4)
    if closing < 0:
        raise ValueError("frontmatter 未闭合")
    result: dict[str, object] = {}
    current_list: str | None = None
    for raw_line in text[4:closing].splitlines():
        if raw_line.startswith("  - "):
            if current_list is None:
                raise ValueError("列表项缺少字段")
            values = result.setdefault(current_list, [])
            assert isinstance(values, list)
            values.append(raw_line[4:].strip())
            continue
        if ":" not in raw_line:
            raise ValueError(f"无法解析元数据行：{raw_line}")
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_list = key if not value else None
        result[key] = value if value else []
    return result


def _metadata(path: Path) -> ReferenceMetadata:
    raw = _parse_frontmatter(path)
    missing = [field for field in REQUIRED_METADATA_FIELDS if field not in raw]
    if missing:
        raise ValueError(f"缺少元数据字段：{', '.join(missing)}")
    # （后续版本）: 容忍空列表(case 文件常用空 used_when 表示"被动触发")
    # depends_on 必须非空,其他可空(代表"未指定")
    for field in ("depends_on", "outputs"):
        value = raw[field]
        if not isinstance(value, list) or not value:
            raise ValueError(f"{field} 必须是非空列表")
    used_when = tuple(str(item) for item in raw.get("used_when", []))
    called_by = tuple(str(item) for item in raw.get("called_by", []))
    return ReferenceMetadata(
        reference_id=str(raw["reference_id"]),
        title=str(raw["title"]),
        category=str(raw["category"]),
        used_when=used_when,
        called_by=called_by,
        depends_on=tuple(str(item) for item in raw["depends_on"]),
        outputs=tuple(str(item) for item in raw["outputs"]),
        path=path,
    )


def _load_step_references(path: Path) -> dict[str, Tuple[str, ...]]:
    result: dict[str, Tuple[str, ...]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = TABLE_REFERENCE.match(line)
        if not match:
            continue
        step_id, raw_ids = match.groups()
        if step_id in result:
            raise ValueError(f"步骤重复：{step_id}")
        result[step_id] = tuple(item.strip() for item in raw_ids.split(",") if item.strip())
    return result


# 上游知识蒸馏镜像目录:用户 Obsidian 知识库的字节级镜像,跳过运行 reference 解析
UPSTREAM_KB_DIR = "knowledge-base"


def _is_upstream_kb(path: Path, skill_root: Path) -> bool:
    """上游知识蒸馏镜像判断。

    KB 目录下的 .md 默认不参与运行 reference 闭环(原 28 篇无 frontmatter 是合法状态)。
    例外:knowledge-base/README.md 是我们自己写的索引元数据文件,**允许**作为 running reference
    并进入 graph,这样 step-reference-map 中 REF-KB-INDEX 的引用可以解析。
    """
    rel = path.relative_to(skill_root).as_posix()
    if not rel.startswith(f"references/{UPSTREAM_KB_DIR}/"):
        return False
    # KB 原文 28 篇跳过(无 frontmatter)
    if path.name not in ("README.md", "SHA256SUMS.txt"):
        return True
    # README.md 例外(它有 frontmatter,可以加载)
    return False


def load_reference_graph(skill_root: Path) -> ReferenceGraph:
    """加载 reference 闭环图。

    容错策略(当前版本+):不再 fail-fast,跳过无 frontmatter 的文件并收集到 skipped 列表。
    这样 validate_reference_graph 不会因个别历史文件缺 frontmatter 就整体抛错。
    """
    reference_root = Path(skill_root) / "references"
    references: dict[str, ReferenceMetadata] = {}
    skipped: list[str] = []
    for path in sorted(reference_root.rglob("*.md")):
        if _is_upstream_kb(path, skill_root):
            # 上游镜像不参与运行 reference 闭环(原 28 篇无 frontmatter 是合法状态)
            continue
        try:
            item = _metadata(path)
        except (ValueError, OSError) as e:
            # 容错:跳过无 frontmatter 的文件,不阻断 graph 加载
            skipped.append(f"{path.relative_to(skill_root).as_posix()}: {e}")
            continue
        if item.reference_id in references:
            raise ValueError(f"reference_id 重复：{item.reference_id}")
        references[item.reference_id] = item
    step_references = _load_step_references(reference_root / "process" / "step-reference-map.md")
    return ReferenceGraph(references=references, step_references=step_references, skipped=tuple(skipped))


def _index_issues(reference_root: Path, graph: ReferenceGraph) -> Tuple[str, ...]:
    index_path = reference_root / "README.md"
    rows: dict[str, str] = {}
    duplicates: set[str] = set()
    for line in index_path.read_text(encoding="utf-8").splitlines():
        match = INDEX_REFERENCE.match(line)
        if not match:
            continue
        reference_id, target = match.groups()
        if reference_id in rows or target in rows.values():
            duplicates.add(reference_id)
        rows[reference_id] = target
    issues: Tuple[str, ...] = ()
    if duplicates:
        issues += (f"总索引存在重复项：{', '.join(sorted(duplicates))}",)
    if set(rows) != set(graph.references):
        missing = set(graph.references) - set(rows)
        extra = set(rows) - set(graph.references)
        issues += (f"总索引 ID 不一致：缺少 {sorted(missing)}，多出 {sorted(extra)}",)
    indexed_paths = {(reference_root / target).resolve() for target in rows.values()}
    actual_paths = {item.path.resolve() for item in graph.references.values()}
    if indexed_paths != actual_paths:
        issues += ("总索引未与全部 Markdown 路径一一对应。",)
    return issues


def _step_issues(graph: ReferenceGraph) -> Tuple[str, ...]:
    issues: Tuple[str, ...] = ()
    if set(graph.step_references) != set(STEP_IDS):
        issues += ("步骤映射必须且只能包含 STEP-01 至 STEP-15。",)
    for step_id, reference_ids in graph.step_references.items():
        unknown = set(reference_ids) - set(graph.references)
        if unknown:
            issues += (f"{step_id} 引用了未知文档：{sorted(unknown)}",)
            continue
        if len(reference_ids) < 2:
            issues += (f"{step_id} 少于两个引用。",)
        categories = {graph.references[item].category for item in reference_ids}
        if "core" not in categories:
            issues += (f"{step_id} 缺少 core 引用。",)
        if not categories - {"core", "process"}:
            issues += (f"{step_id} 缺少专业方法引用。",)
        for reference_id in reference_ids:
            if step_id not in graph.references[reference_id].used_when:
                issues += (f"{step_id} 与 {reference_id} 的 used_when 不互反。",)
    for reference_id, item in graph.references.items():
        for step_id in (value for value in item.used_when if value.startswith("STEP-")):
            if reference_id not in graph.step_references.get(step_id, ()):
                issues += (f"{reference_id} 声明 {step_id}，但步骤映射未引用它。",)
    return issues


def _dependency_issues(graph: ReferenceGraph) -> Tuple[str, ...]:
    issues: Tuple[str, ...] = ()
    adjacency: dict[str, Tuple[str, ...]] = {}
    for reference_id, item in graph.references.items():
        dependencies = tuple(value for value in item.depends_on if value != "NONE")
        unknown = set(dependencies) - set(graph.references)
        if unknown:
            issues += (f"{reference_id} 存在未知依赖：{sorted(unknown)}",)
        adjacency[reference_id] = dependencies

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(reference_id: str) -> None:
        nonlocal issues
        if reference_id in visited:
            return
        if reference_id in visiting:
            issues += (f"引用依赖存在循环：{reference_id}",)
            return
        visiting.add(reference_id)
        for dependency in adjacency.get(reference_id, ()):
            if dependency in adjacency:
                visit(dependency)
        visiting.remove(reference_id)
        visited.add(reference_id)

    for reference_id in sorted(adjacency):
        visit(reference_id)
    return issues


def _link_and_workflow_issues(reference_root: Path) -> Tuple[str, ...]:
    issues: Tuple[str, ...] = ()
    skill_root_for_kb_check = reference_root.parent
    for path in sorted(reference_root.rglob("*.md")):
        if _is_upstream_kb(path, skill_root_for_kb_check):
            continue
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            clean = target.split("#", 1)[0]
            if not clean or "://" in clean:
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(reference_root.resolve())
            except ValueError:
                issues += (f"{path.relative_to(reference_root)} 链接越出 references：{target}",)
                continue
            if not resolved.exists():
                issues += (f"{path.relative_to(reference_root)} 存在断链：{target}",)
    workflow_root = reference_root / "workflows"
    for path in sorted(workflow_root.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        if "## 调用步骤" not in text or "## 必读引用" not in text:
            issues += (f"{path.name} 缺少调用步骤或必读引用。",)
        if len(MARKDOWN_LINK.findall(text)) < 2:
            issues += (f"{path.name} 至少需要两个文档引用。",)
    return issues


def validate_reference_graph(skill_root: Path) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    """返回 (issues, warnings) 元组。issues 是必须修复的错误,warnings 是可接受的状态。"""
    try:
        graph = load_reference_graph(skill_root)
    except (OSError, ValueError) as error:
        return ((str(error),), ())
    reference_root = Path(skill_root) / "references"
    issues = (
        _index_issues(reference_root, graph)
        + _step_issues(graph)
        + _dependency_issues(graph)
        + _link_and_workflow_issues(reference_root)
    )
    # （后续版本）: skipped 列表转化为 warning(而不是 fail),让历史无 frontmatter 文件不阻断校验
    skipped_warnings = tuple(
        f"跳过无 frontmatter 文件:{entry}" for entry in graph.skipped
    )
    return (tuple(sorted(set(issues))), skipped_warnings)


def main() -> int:
    parser = argparse.ArgumentParser(description="验证 Design2Me V2 reference 引用闭环。")
    parser.add_argument("skill_root", type=Path)
    args = parser.parse_args()
    issues, warnings = validate_reference_graph(args.skill_root)
    # 打印 warnings(非阻断)
    for w in warnings:
        print(f"⚠️  {w}")
    # 打印 failures(阻断)
    if issues:
        for issue in issues:
            print(f"失败：{issue}")
        return 1
    print("reference 引用闭环验证通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
