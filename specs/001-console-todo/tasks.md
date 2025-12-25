---

description: "Task list template for feature implementation"
---

# Tasks: Python Console-Based Todo Application

**Input**: Design documents from `/specs/001-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/
**Tests**: Not requested - manual testing per constitution

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `main.py` at repository root
- All functions in single file for simplicity per constitution

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Initialize project structure and verify Python environment

- [x] T001 Create main.py with if __name__ == "__main__": main() entry point in main.py
- [x] T002 Create empty tasks.txt file in repository root
- [x] T003 Add shebang line and UTF-8 encoding comment at top of main.py
- [x] T004 Run `python main.py` to verify no syntax errors
- [x] T005 Add TODO comments section at top of main.py listing all planned functions

**Checkpoint**: Project structure verified, Python executes without errors

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 [P] Implement load_tasks() function in main.py to read tasks from tasks.txt
- [x] T007 [P] Implement save_tasks(tasks) function in main.py to write tasks to tasks.txt
- [x] T008 [P] Implement parse_task(line) helper function in main.py for file parsing
- [x] T009 [P] Implement format_task(task) helper function in main.py for file serialization
- [x] T010 [P] Implement validate_title(title) helper function in main.py
- [x] T011 [P] Implement get_next_id(tasks) helper function in main.py for sequential IDs
- [x] T012 Create main_loop() function skeleton with while True in main.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) MVP

**Goal**: Users can add new tasks with auto-generated IDs and view all tasks

**Independent Test**: Add 2-3 tasks and verify they appear correctly with IDs in task list

### Implementation for User Story 1

- [x] T013 [US1] Implement display_menu() function in main.py showing numbered options 1-7
- [x] T014 [US1] Implement add_task(tasks) function in main.py
- [x] T015 [US1] Connect menu option 1 to add_task() in main_loop() in main.py
- [x] T016 [US1] Implement view_tasks(tasks) function in main.py with formatted output
- [x] T017 [US1] Connect menu option 2 to view_tasks() in main_loop() in main.py
- [x] T018 [US1] Integrate load_tasks() at startup and save_tasks() before exit in main.py

**Checkpoint**: User Story 1 complete - can add and view tasks independently

---

## Phase 4: User Story 2 - Update and Delete Tasks (Priority: P1) MVP

**Goal**: Users can modify task titles and remove tasks by ID

**Independent Test**: Create tasks, update one, delete another, verify changes persist

### Implementation for User Story 2

- [x] T019 [US2] Implement update_task(tasks) function in main.py with ID validation
- [x] T020 [US2] Connect menu option 3 to update_task() in main_loop() in main.py
- [x] T021 [US2] Implement delete_task(tasks) function in main.py with ID validation
- [x] T022 [US2] Connect menu option 4 to delete_task() in main_loop() in main.py

**Checkpoint**: User Story 2 complete - can update and delete tasks independently

---

## Phase 5: User Story 3 - Mark Tasks as Complete (Priority: P1) MVP

**Goal**: Users can mark tasks as done and see completed status

**Independent Test**: Mark tasks complete and verify status changes and visual distinction

### Implementation for User Story 3

- [x] T023 [US3] Implement mark_complete(tasks) function in main.py with status validation
- [x] T024 [US3] Connect menu option 5 to mark_complete() in main_loop() in main.py
- [x] T025 [US3] Update view_tasks() to visually distinguish complete tasks in main.py

**Checkpoint**: User Story 3 complete - all P1 MVP features working

---

## Phase 6: User Story 4 - Task Priority and Categories (Priority: P2)

**Goal**: Users can assign priority levels and categories to organize tasks

**Independent Test**: Add tasks with different priorities and categories, verify they display correctly

### Implementation for User Story 4

- [x] T026 [US4] Add priority parameter to add_task() with High/Medium/Low options in main.py
- [x] T027 [US4] Add category parameter to add_task() in main.py
- [x] T028 [US4] Implement set_priority(tasks) function for updating priority in main.py
- [x] T029 [US4] Implement set_category(tasks) function for updating category in main.py
- [x] T030 [US4] Update update_task() to include priority and category editing in main.py
- [x] T031 [US4] Update view_tasks() to display priority and category columns in main.py

**Checkpoint**: User Story 4 complete - priority and category support working

---

## Phase 7: User Story 5 - Search and Filter Tasks (Priority: P2)

**Goal**: Users can search by keyword and filter by status/priority/category

**Independent Test**: Add 10+ tasks, search for keywords, filter by different criteria

### Implementation for User Story 5

- [x] T032 [US5] Implement search_tasks(tasks, keyword) function in main.py
- [x] T033 [US5] Implement filter_tasks(tasks, criteria_type, criteria_value) in main.py
- [x] T034 [US5] Implement sort_tasks(tasks, sort_by) function in main.py
- [x] T035 [US5] Create search_filter_menu() sub-menu function in main.py
- [x] T036 [US5] Connect menu option 6 to search_filter_menu() in main_loop() in main.py

**Checkpoint**: User Story 5 complete - search and filter working

---

## Phase 8: User Story 6 - Task Due Dates (Priority: P3)

**Goal**: Users can set due dates and system validates format

**Independent Test**: Add tasks with due dates, verify YYYY-MM-DD format validation

### Implementation for User Story 6

- [x] T037 [US6] Implement validate_date(date_str) function using datetime.strptime() in main.py
- [x] T038 [US6] Add due_date parameter to add_task() with validation in main.py
- [x] T039 [US6] Implement set_due_date(tasks) function in main.py
- [x] T040 [US6] Update update_task() to include due date editing in main.py
- [x] T041 [US6] Update view_tasks() to display due date column in main.py

**Checkpoint**: User Story 6 complete - due dates working

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T042 Connect menu option 7 to exit application with goodbye message in main.py
- [x] T043 Add input validation for menu choices (handle non-numeric input) in main.py
- [x] T044 Handle empty tasks.txt file gracefully (create if missing) in main.py
- [x] T045 Handle malformed lines in tasks.txt with warning messages in main.py
- [x] T046 Improve console output formatting (consistent column widths) in main.py
- [x] T047 Add confirmation prompt before deleting tasks in main.py
- [x] T048 Handle duplicate task IDs edge case in get_next_id() in main.py
- [x] T049 Handle very long task titles (truncate or wrap) in view_tasks() in main.py

**Checkpoint**: All features complete and polished

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-8)**: All depend on Foundational phase completion
  - User stories can proceed in parallel (if staffed)
  - Or sequentially in priority order (US1 → US2 → US3 → US4 → US5 → US6)
- **Polish (Phase 9)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Depends on US1 for testing
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - Depends on US1 for testing
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Can test with US1-3 tasks
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - Depends on US4 for filtering
- **User Story 6 (P3)**: Can start after Foundational (Phase 2) - Independent of other stories

### Within Each User Story

- Helper functions before main functions
- Core implementation before menu integration
- Story complete before moving to next priority
- Test after each story completion

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
Task: "Implement display_menu() function in main.py"
Task: "Implement add_task(tasks) function in main.py"
Task: "Implement view_tasks(tasks) function in main.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Add User Story 6 → Test independently → Deploy/Demo (optional)
8. Add Polish phase → Finalize

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Task Summary

| Phase | Description | Tasks | Status |
|-------|-------------|-------|--------|
| Phase 1 | Setup | 5 tasks | ✅ Complete |
| Phase 2 | Foundational | 7 tasks | ✅ Complete |
| Phase 3 | US1: Add and View Tasks (P1) | 6 tasks | ✅ Complete |
| Phase 4 | US2: Update and Delete Tasks (P1) | 4 tasks | ✅ Complete |
| Phase 5 | US3: Mark Complete (P1) | 3 tasks | ✅ Complete |
| Phase 6 | US4: Priority and Categories (P2) | 6 tasks | ✅ Complete |
| Phase 7 | US5: Search and Filter (P2) | 5 tasks | ✅ Complete |
| Phase 8 | US6: Due Dates (P3) | 5 tasks | ✅ Complete |
| Phase 9 | Polish | 8 tasks | ✅ Complete |
| **Total** | | **49 tasks** | **✅ ALL COMPLETE** |

### Parallel Execution Opportunities

- Phase 1: T001, T002, T003 can run in parallel
- Phase 2: T006, T007, T008, T009, T010, T011 can run in parallel
- User Stories: Each story's tasks can run in parallel within the story
