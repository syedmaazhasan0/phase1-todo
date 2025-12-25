# Data Model: Python Console-Based Todo Application

**Feature**: Python Console-Based Todo Application
**Date**: 2025-12-25
**Branch**: 001-console-todo

## Entity: Task

Represents a single todo item stored in the application.

### Attributes

| Field | Type | Required | Default | Validation |
|-------|------|----------|---------|------------|
| id | int | Yes | Auto-generated | Must be unique, sequential |
| title | str | Yes | N/A | Non-empty, max 200 chars |
| status | str | Yes | "Pending" | "Pending" or "Complete" |
| priority | str | Yes | "Medium" | "High", "Medium", or "Low" |
| category | str | No | "" | Alphanumeric, max 50 chars |
| due_date | str | No | "" | YYYY-MM-DD format |

### Data Structure (Python)

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    status: str = "Pending"
    priority: str = "Medium"
    category: str = ""
    due_date: str = ""
```

### Alternative (Dictionary - for simplicity)

```python
# For beginners, dictionary is preferred over dataclass
task = {
    "id": 1,
    "title": "Buy groceries",
    "status": "Pending",
    "priority": "Medium",
    "category": "Home",
    "due_date": ""
}
```

### State Transitions

```
[New Task] --add_task()--> Pending
    |
    |--> mark_complete() --> Complete
    |
    |--> update_task() --> (Updated title/category/priority)
    |
    |--> delete_task() --> [Deleted from list]
```

### Persistence Format

**File**: `tasks.txt` (plain text, one line per task)

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

### Parsing/Serialization

**Load from file**:
```python
def parse_task(line):
    parts = line.strip().split(" | ")
    return {
        "id": int(parts[0]),
        "title": parts[1],
        "status": parts[2],
        "priority": parts[3],
        "category": parts[4],
        "due_date": parts[5]
    }
```

**Save to file**:
```python
def format_task(task):
    return " | ".join([
        str(task["id"]),
        task["title"],
        task["status"],
        task["priority"],
        task["category"],
        task["due_date"]
    ])
```

### Validation Rules

1. **ID**: Must be unique; generated as `max(existing_ids) + 1` or `1` if empty
2. **Title**: Cannot be empty after stripping whitespace
3. **Status**: Must be exactly "Pending" or "Complete"
4. **Priority**: Must be exactly "High", "Medium", or "Low"
5. **Category**: Optional; trimmed to 50 chars max
6. **Due Date**: Optional; must match YYYY-MM-DD format if provided

### Edge Cases Handled

| Edge Case | Handling |
|-----------|----------|
| Empty tasks.txt | Return empty list, create file if needed |
| Malformed line | Skip line, log warning, continue |
| Duplicate ID | Should not occur with sequential generation |
| Missing fields | Treat as empty/default values |
| Extra fields | Ignore additional fields |
| Corrupted file | Show error, start with empty list |
