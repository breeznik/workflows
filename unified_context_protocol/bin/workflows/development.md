# Universal Development Workflow (v3.0)

> **Policy**: Test-Driven, Context-Aware, Atomic Commits.
> **Triggers**: Feature, Bugfix, Refactor.

## 1. PRE-FLIGHT (Mandatory)
- **Check Locks**: If `context/active/` is locked by another task, ABORT.
- **Check Version**: If `bin/VERSION` has pending breaking changes, WARN.

## 2. MODES & POLICIES

### ✨ Feature
- **Rule**: Update `context/product/vision.md` FIRST if the feature isn't defined there.
- **TDD**: Write the "Expectation Test" before the Implementation code.

### 🐛 Bugfix
- **Rule**: NEVER fix without reproduction.
- **Step 1**: Create `repro_case.[py|js]`.
- **Step 2**: Verify it FAILS.
- **Step 3**: Fix code.
- **Step 4**: Verify it PASSES.

### ♻️ Refactor
- **Rule**: NO behavior changes.
- **Constraint**: Existing tests MUST pass without modification.

## 3. EXECUTION LOOP
1. **Plan**: Update `context/active/PLAN.md` with granular steps.
2. **Code**: Edit files.
3. **Verify**: Run tests/build.
4. **Loop**: If fail, read error -> fix -> retry.

## 4. FINALIZE (Definition of Done)
1. **Context Update**:
   - `context/tech.md`: Add new dependencies?
   - `context/map.md`: Add new files/components?
2. **Knowledge**:
   - `knowledge/learnings.md`: Did you learn a new pattern?
3. **Changelog**:
   - `CHANGELOG.md`: Apped `[Type] Description`.
4. **Commit**:
    - Run `bin/workflows/commit.md`.
