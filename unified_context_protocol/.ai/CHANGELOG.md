# UCP Release Notes

> What changed in each version of the Unified Context Protocol.

---

## v1.1.0 (2025-12-22)

### Added
- **Context Budget System**: P0/P1/P2/P3 priority tiers with token budgets
- **Knowledge Management**: `learnings.md`, `boundaries.md`
- **User Preferences**: `user-prefs.md` for coding style memory
- **Dependencies**: `dependencies.md` for external APIs
- **Priority Loading**: `PRIORITY.md` with loading rules
- **Upgrade System**: `VERSION` file + `upgrade.md` workflow
- **Export System**: `export.md` workflow for knowledge migration
- **Self-Identification**: Agents detect themselves and ask user if unsure

### Changed
- `boot.md`: Added tiered loading and context budget
- `maintenance.md`: Added auto-triggers and size auditing
- `.ai/README.md`: Updated structure with all new files
- Knowledge templates: Added tags for searchability
- All workflows: Reference `learnings.md` in session end

### Fixed
- Consistent session end protocol across all workflows
- Clear [TEMPLATE] markers on template files

---

## v1.0.0 (2025-12-22)

### Initial Release
- Core protocol structure
- 8 agent adapters
- Basic workflows (audit, feature, bugfix, refactor, handoff, maintenance)
- Context system (MASTER.md, tech.md, changelog.md)
- Knowledge system (patterns.md, gotchas.md, decisions.md)
