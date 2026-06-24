---
reference_id: REF-USER-PREFS
title: User Preferences & Workflow Conventions
category: references
used_when:
  - SKILL-MAINTENANCE
  - VERSION-UPGRADE
  - USER-INTERACTION
called_by:
  - skill-router
  - version-manager
depends_on:
  - NONE
outputs:
  - user_preference_log
---

# User Preferences & Workflow Conventions

> **Date**: 2026-06-24
> **Trigger**: User explicitly said "升级" (upgrade) to trigger version bump without confirmation

## 1. Version Upgrade Command

### User Preference
- When user says **"升级技能版本"** → Immediately execute version upgrade workflow
- When user says **"升级"** → Same immediate execution, no additional confirmation needed
- **Do NOT ask**: "您确认要升级吗?" or "升级到哪个版本?"
- **Directly execute**: minor bump (e.g., 3.2.0 → 3.3.0 → 3.4.0)

### Workflow
1. Update SKILL.md frontmatter `version:`
2. Create `references/changelogs/vX.Y.Z-changelog.md`
3. Update document routing table in SKILL.md
4. Run validation script `scripts/check_version_consistency.py`
5. Report completion

## 2. Audit Feedback Processing

### User Preference
- User acts as **senior design process auditor** providing detailed system-level audit reports
- Audit feedback should be processed via **Pitfall 026 protocol**: classify → evaluate → absorb → no rerun
- **Honest反查** (honest self-check) is required: agree to absorb / reject / partially absorb
- All new protocols go to `references/` directory, never pollute SKILL.md

## 3. File Hygiene

### User Preference (2026-06-24 explicit)
- "资料说明类的应该放到对应的文档下,而不是什么文件都往 SKILL.md 里塞"
- SKILL.md = pure execution contract, not encyclopedia
- All detailed content goes to `references/` with 1-line pointers in SKILL.md

## 4. Source

- User explicit statements in 2026-06-24 session
- jony-ive-design2me-v2 v3.2.0 → v3.3.0 → v3.4.0 upgrade process
