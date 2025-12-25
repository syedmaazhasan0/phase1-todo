# CLI Contracts: Python Console-Based Todo Application

**Feature**: Python Console-Based Todo Application
**Date**: 2025-12-25
**Branch**: 001-console-todo

## Main Menu

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

## Function Contracts

### 1. Add Task

**Input**:
```
--- ADD TASK ---
Enter task title: [user input]

Priority (1-High, 2-Medium, 3-Low) [2]: [1-3 or Enter]
Category (optional): [user input or Enter]
Due date (YYYY-MM-DD, optional): [date or Enter]
```

**Output (Success)**:
```
Task added successfully! ID: 1
```

**Output (Error - Empty Title)**:
```
Error: Task title cannot be empty.
```

**Validation**:
- Title must not be empty after stripping whitespace
- Priority defaults to Medium (2) if not specified
- Category defaults to empty if not specified
- Due date validated to YYYY-MM-DD format if provided

---

### 2. View Tasks

**Input**: None (selects from menu)

**Output**:
```
=== TASK LIST ===
ID | Title               | Status    | Priority | Category | Due Date
---------------------------------------------------------------
1  | Buy groceries       | Pending   | High     | Home     |
2  | Finish report       | Pending   | Medium   | Work     | 2025-01-15
3  | Call mom            | Complete  | Low      | Family   |

3 tasks found.
```

**Output (Empty)**:
```
No tasks found. Add a task to get started!
```

**Formatting**:
- Left-aligned columns
- Status shows [Complete] or [Pending]
- Truncate titles > 20 chars with "..."

---

### 3. Update Task

**Input**:
```
--- UPDATE TASK ---
Enter task ID to update: [user input]

Current title: Buy groceries
Enter new title: [user input or Enter to skip]
```

**Output (Success)**:
```
Task updated successfully!
```

**Output (Error - Invalid ID)**:
```
Error: Task with ID 999 not found.
```

**Output (Error - Empty Title)**:
```
Error: Task title cannot be empty.
```

**Validation**:
- Task ID must exist
- New title cannot be empty (if provided)
- Press Enter to skip updating a field

---

### 4. Delete Task

**Input**:
```
--- DELETE TASK ---
Enter task ID to delete: [user input]
```

**Output (Success)**:
```
Task deleted successfully!
```

**Output (Error - Invalid ID)**:
```
Error: Task with ID 999 not found.
```

**Output (Confirmation - Optional)**:
```
Are you sure you want to delete "Buy groceries"? (y/n): [user input]
```

---

### 5. Mark Task as Complete

**Input**:
```
--- MARK COMPLETE ---
Enter task ID to mark complete: [user input]
```

**Output (Success)**:
```
Task "Buy groceries" marked as complete!
```

**Output (Error - Invalid ID)**:
```
Error: Task with ID 999 not found.
```

**Output (Error - Already Complete)**:
```
Task "Buy groceries" is already complete.
```

**Validation**:
- Task ID must exist
- Task must be in "Pending" status

---

### 6. Search / Filter Tasks

**Input**:
```
--- SEARCH / FILTER ---
1. Search by keyword
2. Filter by status
3. Filter by priority
4. Filter by category
5. Sort tasks
6. Show all tasks

Enter choice: [user input]
```

**Search by Keyword**:
```
Enter keyword to search: [user input]
```

**Filter by Status**:
```
1. Pending
2. Complete
Enter status: [user input]
```

**Filter by Priority**:
```
1. High
2. Medium
3. Low
Enter priority: [user input]
```

**Sort Tasks**:
```
1. By ID
2. By Title
3. By Priority
4. By Due Date
Enter sort option: [user input]
```

**Output (Results)**:
```
=== SEARCH RESULTS ===
Found 2 task(s):
1  | Buy groceries       | Pending   | High     | Home     |
2  | Buy gifts           | Pending   | High     | Family   |
```

**Output (No Results)**:
```
No tasks found matching your criteria.
```

---

### 7. Exit

**Input**: None (selects from menu)

**Output**:
```
Goodbye! Your tasks have been saved.
```

---

## Error Messages

| Error | Message |
|-------|---------|
| Invalid menu choice | "Invalid choice. Please enter 1-7." |
| Non-numeric ID | "Please enter a valid number." |
| Task not found | "Error: Task with ID {id} not found." |
| Empty title | "Error: Task title cannot be empty." |
| Invalid date | "Error: Please enter date in YYYY-MM-DD format." |
| File read error | "Error: Could not read tasks file." |
| File write error | "Error: Could not save tasks." |

## Data File Format

**File**: `tasks.txt` (plain text, created automatically)

**Format**:
```
ID | Title | Status | Priority | Category | DueDate
```

**Example**:
```
1 | Buy groceries | Pending | High | Home |
2 | Finish report | Pending | Medium | Work | 2025-01-15
3 | Call mom | Complete | Low | Family |
```

**Parsing**: `line.split(" | ")` to extract 6 fields
**Serialization**: `" | ".join([...])` to create line
