<!--
  Sync Impact Report
  ===================
  Version change: N/A → 1.0.0 (initial creation)

  Modified principles: N/A (all new)
  Added sections: Technology Constraints, Development Workflow
  Removed sections: None
  Templates requiring updates: None detected (templates use placeholder tokens)

  Follow-up TODOs: None
-->

# TODO Console Constitution

## Core Principles

### I. Python-Only Implementation
All code MUST be written in Python. No external libraries, frameworks, databases, or
non-Python dependencies are permitted. The application runs exclusively in the console
or terminal environment.

**Rationale**: Ensures simplicity, portability, and ease of understanding for a
beginner-friendly todo application.

### II. Plain Text Persistence
All task data MUST be stored in a single `tasks.txt` file using pipe-separated values
(`|`) on a single line per task. Format: `ID | Title | Status | Priority | Category | DueDate`.

**Rationale**: Eliminates database complexity while ensuring human-readable, easily
editable data storage that persists across application restarts.

### III. Menu-Driven Interface
The application MUST present a numbered menu for all operations. Input validation
MUST handle invalid menu choices gracefully without crashing. Users interact solely
through console input.

**Rationale**: Provides intuitive, predictable navigation while ensuring the application
remains robust against unexpected user input.

### IV. Phase-Based Development
Features MUST be implemented incrementally: Phase 1 (Basic) first, then Phase 2
(Intermediate), then Phase 3 (Advanced). No Phase 2 or 3 features may be implemented
until Phase 1 is stable and tested.

**Rationale**: Ensures a working MVP is delivered before expanding scope, reducing
risk and maintaining focus.

### V. Input Validation
All user inputs MUST be validated before processing. Empty task titles are forbidden.
Task IDs MUST exist before update, delete, or mark-complete operations.

**Rationale**: Prevents data corruption and provides immediate user feedback on errors.

### VI. Modular Simplicity
Code MUST be modular with clear separation of concerns. Functions and classes SHOULD
have single responsibilities. Unnecessary complexity MUST be avoided (YAGNI principle).

**Rationale**: Keeps the codebase maintainable and understandable for learning purposes.

## Technology Constraints

### Strict Boundaries
- **Language**: Python 3.x ONLY
- **Interface**: Console/Terminal ONLY
- **Storage**: Plain text file (`tasks.txt`) ONLY
- **External Libraries**: NOT allowed
- **Database**: NOT allowed
- **GUI/Web Frameworks**: NOT allowed

### Data Format Specification
Each task occupies exactly one line in `tasks.txt`:
```
ID | Title | Status | Priority | Category | DueDate
```
Example: `1 | Complete Python assignment | Pending | High | Study | 2025-01-15`

All fields except DueDate are required. DueDate is optional for Phase 1.

## Development Workflow

### Feature Implementation Order
1. Complete Phase 1 (Add, View, Update, Delete, Mark Complete)
2. Stabilize and test Phase 1
3. Implement Phase 2 (Priority, Category, Search, Filter, Sort)
4. Implement Phase 3 (Due Dates, Recurring Tasks, Reminders) - optional

### Code Quality Standards
- Functions SHOULD be under 50 lines where possible
- Clear variable and function names REQUIRED
- Comments REQUIRED for non-obvious logic
- No code duplication (extract to functions)

### Testing Expectations
- Manual testing after each feature implementation
- Verify data persists after application restart
- Test edge cases (invalid IDs, empty inputs, duplicate entries)

## Governance

This constitution supersedes all other development practices for this project.
Amendments require:
1. Documentation of the proposed change
2. Review and approval
3. Update to the constitution version following semantic versioning

**Compliance**: All code changes SHOULD be reviewed against these principles before
committing. Complexity additions MUST be justified against the simplicity principle.

**Guidance**: Refer to `/specs/<feature>/quickstart.md` for runtime development guidance
and feature-specific instructions.

**Version**: 1.0.0 | **Ratified**: 2025-12-25 | **Last Amended**: 2025-12-25
