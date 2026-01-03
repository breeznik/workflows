# UCP Release Notes

> What changed in each version of the Unified Context Protocol.

---

## v3.2.0 (2026-01-03)

### Added
- **Command Palette Menu**: Boot protocol and task completion now trigger a standardized Command Palette menu for easier navigation.
- **Startup Team Pack**: New `@corepackai/startup-team` pack added, featuring a generic Agentic Board (Strategy & Personas) and UCP dependency.
- **Pack Dependencies**: `pack.config.json` support for defining pack dependencies (e.g. Startup Team depends on UCP).

### Changed
- **Boot Protocol**: Updated `boot.md` to enforce menu display on boot and post-task.
- **Template Fixes**: Synced `boot.md` fixes to the public template.


### Added
- **Smart Kernel v3.1**: Replaced verbose menu with high-speed execution logic
- **Auto-Maintenance**: Agents now auto-fix broken locks (>1h), stale context (>48h), and missing context (TBD)
- **Breaking Version Auto-Upgrade**: Agents auto-run `upgrade.md` if `breaking` field is set
- **Prune Empty Sections**: `audit.md` now removes inapplicable template sections
- **Learning TTL**: Learnings older than 30 days without pattern promotion are archived
- **`/reset` Command**: Clear working context and start fresh session

### Changed
- `boot.md` reduced from ~130 lines to ~65 lines (50% token savings)
- `development.md` streamlined to policy-only format
- `sync.md` now requires Proof of Work (test/visual confirmation) before marking tasks complete

---

## v2.2.0 (2026-01-02)

### Added
- **Smart Suggestions**: Agent now analyzes context and suggests the most relevant next action
  - Priority-based logic table for intelligent recommendations
  - Example suggestions for common scenarios (empty project, pending tasks, etc.)

### Fixed
- **Menu Formatting**: Resolved line collapsing issue when agents render the boot menu
  - Changed code block to explicit `text` type for consistent rendering
  - Added box drawing characters for visual structure
  - Fixed inconsistent indentation (2-space → 3-space)
  - Aligned double-digit menu items (10-13) properly
  - Replaced `---` separators with `═══` to avoid markdown interpretation

### Changed
- `boot.md`: Added `💡 SUGGESTED NEXT:` section with context-aware recommendations
- Menu now includes `[Enter number or command]` prompt for clarity

---

## v2.1.0 (2025-12-31)

### Fixed
- **Template Size Violations**: Trimmed all P0/P1 templates to comply with size limits
  - `MASTER.md`: 792B → ~280B (P0 ≤500B)
  - `tech.md`: 968B → ~400B (P1 ≤1KB)
  - `user-prefs.md`: 1873B → ~500B (P1 ≤1KB)
  - `PRIORITY.md`: 1802B → ~750B (still P0, more concise)

### Added
- **Mandatory Boot Checklist**: Added `[!CAUTION]` checklist to `boot.md` that agents MUST complete
- **Pre-Flight Validation**: Added ASSERT statements to `bin/workflows/boot.md`
- **Size Warnings**: Added `[!WARNING]` alerts to `PRIORITY.md` for size enforcement
- **Sync Reminder**: Added `[!IMPORTANT]` to remind agents to run sync at session end
- **Agent Greeting Menu**: Agents now present users with 13-option categorized menu after boot

### Changed
- `boot.md`: Rewritten — 4.8KB → 2.8KB (42% smaller), added 14-item menu + loop
- `PRIORITY.md`: Trimmed and added enforcement alerts
- All templates now clearly marked `[TEMPLATE]`

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
