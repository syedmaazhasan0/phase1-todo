# Research: Python Console-Based Todo Application

**Feature**: Python Console-Based Todo Application
**Date**: 2025-12-25
**Branch**: 001-console-todo

## Technical Decisions

### 1. Project Structure

**Decision**: Single `main.py` file at repository root

**Rationale**:
- Simplicity for beginner Python learners
- All code in one place, easy to navigate
- No module imports complexity
- Matches constitution's "Modular Simplicity" principle

**Alternatives Considered**:
- Modular structure with `src/` directory (rejected - adds complexity for beginners)
- Multiple files for different features (rejected - unnecessary for <500 LOC project)

### 2. Data Persistence Format

**Decision**: Pipe-separated values in `tasks.txt`

**Format**: `ID | Title | Status | Priority | Category | DueDate`

**Rationale**:
- Human-readable format (can edit manually if needed)
- Easy to parse with `line.split(" | ")`
- Matches constitution requirement
- No external libraries needed

**Alternatives Considered**:
- JSON format (rejected - less human-readable, requires `json` module parsing)
- CSV format (rejected - more complex parsing, handling of commas in titles)
- SQLite database (rejected - not allowed by constitution)

### 3. In-Memory Data Structure

**Decision**: List of dictionaries

**Example**:
```python
tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "status": "Pending",
        "priority": "Medium",
        "category": "Home",
        "due_date": ""
    }
]
```

**Rationale**:
- Python-native data structure
- Easy to manipulate with built-in methods
- Natural serialization to pipe-separated format
- Intuitive for beginners

**Alternatives Considered**:
- Custom Task class (rejected - more code, less flexible)
- Named tuple (rejected - immutable, harder to update)
- ORM-style (rejected - not allowed, over-engineered)

### 4. File Write Strategy

**Decision**: Full file rewrite on any task modification

**Rationale**:
- Simpler implementation (no partial-write risks)
- Data integrity (complete file always valid)
- No file locking needed (single-user)
- Easy recovery if write fails

**Alternatives Considered**:
- Append-only (rejected - complicates updates and filtering)
- In-place edit (rejected - risk of partial writes corrupting file)
- Transaction log (rejected - over-engineered for this scope)

### 5. ID Generation

**Decision**: Sequential integer based on `max(task["id"]) + 1`

**Rationale**:
- Simple to implement
- Predictable and sequential
- Matches spec requirements

**Alternatives Considered**:
- UUID (rejected - overkill, less readable)
- Timestamp-based (rejected - not sequential, harder to parse)
- Auto-increment database style (rejected - no database)

### 6. Input Validation Strategy

**Decision**: `try/except` for numeric input, `while` loop for validation

**Rationale**:
- Python-native approach
- Clear error messages
- Graceful handling of invalid input

**Example**:
```python
while True:
    try:
        choice = int(input("Enter choice: "))
        if 1 <= choice <= 7:
            break
        print("Please enter 1-7")
    except ValueError:
        print("Please enter a number")
```

### 7. Date Validation (Phase 3)

**Decision**: Use `datetime.strptime()` with YYYY-MM-DD format

**Rationale**:
- Built-in Python module
- Validates both format and logical dates (e.g., Feb 30 rejected)
- Simple error handling

**Example**:
```python
from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
```

### 8. Sorting Implementation

**Decision**: Python's built-in `sorted()` with `key` parameter

**Rationale**:
- No external libraries
- Flexible sorting by any field
- Readable and Pythonic

**Example**:
```python
sorted_tasks = sorted(tasks, key=lambda x: x["priority"], reverse=True)
```

## Best Practices for Python Console Applications

### 1. Entry Point
```python
if __name__ == "__main__":
    main()
```

### 2. Clear Function Responsibilities
- Each function does one thing
- Functions return values or modify state, not both
- Use descriptive names (snake_case)

### 3. User-Friendly Output
- Clear prompts with examples
- Meaningful error messages
- Visual distinction for completed items (e.g., "[X]")

### 4. Code Organization
- Imports at top
- Constants before functions
- Helper functions after main functions
- Main execution at bottom

### 5. Handling Edge Cases
- Empty task list
- Missing or corrupted file
- Invalid user input
- Duplicate entries

## Resources

### Python Standard Library Modules Used
- `os` - File operations (`os.path.exists`, `os.remove`)
- `datetime` - Date parsing and validation
- `typing` - Type hints (optional, for clarity)

### No External Dependencies
Per constitution, no external libraries are used.
