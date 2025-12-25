---
id: "001"
title: "Create TODO Console Constitution"
stage: "constitution"
date: "2025-12-25"
surface: "agent"
model: "claude-opus-4-5-20251101"
feature: "none"
branch: "master"
user: "Maaz Hassan"
command: "/sp.constitution"
labels: ["constitution","python","console","todo-app"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - ".specify/memory/constitution.md"
tests:
  - "null"
---

## Prompt

PYTHON CONSOLE TODO APPLICATION – REQUIREMENTS
==============================================

Project Overview
----------------
This project is a Console-based Todo Application built using ONLY Python.
The application runs in the terminal and stores all data in a plain text (.txt) file.
No GUI, no web framework, no database is allowed.

------------------------------------------------

Technology Constraints (STRICT)
-------------------------------
- Programming Language: Python ONLY
- Interface: Console / Terminal ONLY
- Storage: Plain text file (.txt)
- External libraries: NOT allowed
- Database, GUI, Web frameworks: NOT allowed

------------------------------------------------

Core Principles
---------------
1. Simple and readable Python code
2. Menu-driven console interaction
3. Persistent task storage using a .txt file
4. Proper input validation
5. Feature-based incremental development
6. No unnecessary complexity

------------------------------------------------

Data Storage Rules
------------------
- File name: tasks.txt
- Each task must be stored on ONE LINE
- Data fields separated using a pipe (|) symbol

Task Format:
ID | Title | Status | Priority | Category | DueDate

Example:
1 | Complete Python assignment | Pending | High | Study | 2025-01-15

------------------------------------------------

PHASE 1: BASIC FEATURES (MANDATORY)
----------------------------------
These features MUST be completed first.

1. Add Task
   - Input task title from user
   - Auto-generate unique task ID
   - Default status: Pending
   - Save task to t due date, or title

------------------------------------------------

PHASE 2: INTERMEDIATE FEATURES
------------------------------
Implemented only after Phase 1 is stable.

1. Task Priority
   - Values: High / Medium / Low

2. Category / Tag
   - Example: Work, Home, Study

3. Search Tasks
   - Search by keyword in task title

4. Filter Tasks
   - Filter by status, priority, or category

5. Sort Tasks
   - Sort by priority, text, or due date

------------------------------------------------

PHASE 3: ADVANCED FEATURES (OPTIONAL)
------------------------------------
1. Due Dates
   - Format: YYYY-MM-DD

2. Recurring Tasks
   - Daily or Weekly tasks
   - Automatically re-added after completion

3. Console Reminders
   - Show warning message for upcoming deadlines

------------------------------------------------

Console Menu Example
--------------------
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Search / Filter Tasks
7. Exit

------------------------------------------------

Validation Rules
----------------
- Task ID must exist before update or delete
- Empty task titles are not allowed
- Invalid menu input must be handled safely

------------------------------------------------

Success Criteria
----------------
- Application runs without errors
- Tasks persist after restarting program
- All operations are performed via console
- Code is modular and easy to understand

END OF DOCUMENT
==============================================

## Response snapshot

Created initial project constitution at `.specify/memory/constitution.md` with 6 core principles:
1. Python-Only Implementation - No external libraries or frameworks
2. Plain Text Persistence - Pipe-separated values in tasks.txt
3. Menu-Driven Interface - Numbered menu with input validation
4. Phase-Based Development - Implement Phase 1 first, then 2, then 3
5. Input Validation - Validate all user inputs
6. Modular Simplicity - YAGNI principle, single responsibilities

Added Technology Constraints section (Strict Boundaries, Data Format Specification)
Added Development Workflow section (Feature Implementation Order, Code Quality Standards, Testing Expectations)

## Outcome

- Impact: Established foundational project governance document
- Files: .specify/memory/constitution.md (created)
- Next prompts: /sp.spec to create feature specifications for Phase 1
- Reflection: Constitution provides clear guidance for the todo console project

## Evaluation notes (flywheel)

- Failure modes observed: "null"
- Graders run and results (PASS/FAIL): "N/A"
- Prompt variant (if applicable): "N/A"
- Next experiment (smallest change to try): "N/A"
