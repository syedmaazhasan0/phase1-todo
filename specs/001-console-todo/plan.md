# Implementation Plan: Python Console-Based Todo Application

**Branch**: `001-console-todo` | **Date**: 2025-12-25 | **Spec**: [Link to spec.md](spec.md)
**Input**: Feature specification from `/specs/001-console-todo/spec.md`

## Summary

A console-based todo application written in pure Python that uses a plain text file (`tasks.txt`) for persistent task storage. The application provides a menu-driven interface for managing tasks with features organized in phases: Phase 1 (Core MVP), Phase 2 (Organization), and Phase 3 (Advanced). Key technical decisions favor simplicity and learnability while maintaining data integrity through validation and consistent file operations.

## Technical Context

**Language/Version**: Python 3.x (standard library only)
**Primary Dependencies**: None (standard library only)
**Storage**: Plain text file (`tasks.txt`) with pipe-separated values
**Testing**: Manual testing after each feature; automated tests optional for advanced users
**Target Platform**: Cross-platform (Windows, macOS, Linux terminals)
**Project Type**: Single project (console application)
**Performance Goals**: <5 second startup for 100 tasks; instant operations (<1s) for add/view/update/delete
**Constraints**: Python standard library only; no external libraries, GUI, or databases; single .txt file storage
**Scale/Scope**: Single user, local storage, typically <100 tasks

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Python-Only Implementation | PASS | Using only Python standard library (datetime, os, json/csv parsing) |
| II. Plain Text Persistence | PASS | Tasks stored in `tasks.txt` with pipe-separated format |
| III. Menu-Driven Interface | PASS | Numbered menu system with input validation |
| IV. Phase-Based Development | PASS | Following Phase 0 → Phase 1 → Phase 2 → Phase 3 progression |
| V. Input Validation | PASS | All inputs validated before processing |
| VI. Modular Simplicity | PASS | Functions with single responsibilities, YAGNI principle |

**Result**: All gates pass. No violations requiring justification.

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (technical decisions)
├── data-model.md        # Phase 1 output (entity definitions)
├── quickstart.md        # Phase 1 output (development guide)
├── contracts/           # Phase 1 output (CLI contracts)
│   └── cli-contracts.md
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
# Single project structure (console application)
main.py                 # Entry point and main application loop
tasks.txt               # Persistent task storage (auto-created)

# No tests/ directory - manual testing per constitution
```

**Structure Decision**: Simple single-file application structure at repository root. The `main.py` file contains all application logic with functions organized by feature. The `tasks.txt` file is created automatically if missing.

## Phase 0: Research Decisions

### Technical Approach

| Decision | Rationale | Alternatives Considered |
|----------|-----------|------------------------|
| Single main.py file | Simplicity for beginners; all code in one place | Module structure (rejected - adds complexity) |
| Pipe-separated format | Human-readable; easy to parse with split(); matches constitution | JSON (rejected - less human-readable), CSV (rejected - more complex parsing) |
| Simple list of dictionaries in memory | Python-native data structure; easy to manipulate | Custom class (rejected - more code), ORM (rejected - not allowed) |
| Full file rewrite on changes | Simpler implementation; no partial-write risks | Append-only (rejected - complicates updates), in-place edit (rejected - risky) |
| Sequential ID generation | Simple to implement; matches spec requirements | UUID (rejected - overkill), timestamp (rejected - not sequential) |

### Unknowns Resolved

| Unknown | Resolution |
|---------|------------|
| File locking for concurrent access | Not needed (single-user, constitution assumes no concurrent access) |
| Date validation approach | Use `datetime.strptime()` with YYYY-MM-DD format |
| Sorting implementation | Python's built-in `sorted()` with lambda key functions |
| Input loop for invalid choices | `while True` loop with try/except for non-integer input |

## Phase 1: Design

### File Format

**tasks.txt** (created automatically if missing):
```
ID | Title | Status | Priority | Category | DueDate
```
Example line: `1 | Complete Python assignment | Pending | Medium | Study | 2025-01-15`

**Parsing**: `line.split(" | ")` to extract fields
**Serialization**: `" | ".join([str(id), title, status, priority, category, due_date])`

### Data Model

```python
Task = {
    "id": int,
    "title": str,
    "status": str,           # "Pending" or "Complete"
    "priority": str,         # "High", "Medium", or "Low"
    "category": str,         # User-defined, may be empty
    "due_date": str          # YYYY-MM-DD format, may be empty
}
```

### CLI Interface (Console Menu)

```
=== TODO APPLICATION ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Search / Filter Tasks
7. Exit

Enter your choice: _
```

### Function Structure

| Function | Purpose | Phase |
|----------|---------|-------|
| `load_tasks()` | Read tasks from tasks.txt | 1 |
| `save_tasks(tasks)` | Write tasks to tasks.txt | 1 |
| `display_menu()` | Show main menu | 1 |
| `add_task(tasks)` | Add new task | 1 |
| `view_tasks(tasks)` | Display all tasks | 1 |
| `update_task(tasks)` | Update task title | 1 |
| `delete_task(tasks)` | Delete task by ID | 1 |
| `mark_complete(tasks)` | Mark task as complete | 1 |
| `set_priority()` | Set task priority | 2 |
| `set_category()` | Set task category | 2 |
| `search_tasks(tasks)` | Search by keyword | 2 |
| `filter_tasks(tasks)` | Filter by criteria | 2 |
| `sort_tasks(tasks)` | Sort tasks | 2 |
| `set_due_date()` | Set due date | 3 |
| `validate_date(date_str)` | Validate YYYY-MM-DD | 3 |

## Complexity Tracking

> No Constitution Check violations. All decisions align with simplicity principles.

## Next Steps

After `/sp.plan` completes:
1. Run `/sp.tasks` to generate task breakdown
2. Implement tasks in order (Phase 0 → Phase 1 → Phase 2 → Phase 3)
3. Test each feature before advancing to next phase
4. Verify data persistence after program restart
