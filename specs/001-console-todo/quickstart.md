# Quickstart: Python Console-Based Todo Application

**Feature**: Python Console-Based Todo Application
**Date**: 2025-12-25
**Branch**: 001-console-todo

## Prerequisites

- Python 3.x installed
- Terminal or command prompt access
- Text editor (VS Code, Notepad, etc.)

## Project Structure

```
TODO-console/
├── main.py          # Application code
└── tasks.txt        # Created automatically (task storage)
```

## Running the Application

```bash
# From the TODO-console directory
python main.py
```

## Development Workflow

### Phase 0: Setup

1. Create `main.py` with basic structure
2. Test Python execution: `python main.py`
3. Verify no syntax errors

### Phase 1: Core Features

Implement in order:
1. `load_tasks()` - Read from tasks.txt
2. `save_tasks(tasks)` - Write to tasks.txt
3. `display_menu()` - Show options
4. `add_task(tasks)` - Create new task
5. `view_tasks(tasks)` - List all tasks
6. `update_task(tasks)` - Edit task title
7. `delete_task(tasks)` - Remove task
8. `mark_complete(tasks)` - Toggle status

### Phase 2: Organization

After Phase 1 works:
1. Add priority support (High/Medium/Low)
2. Add category support
3. Implement search by keyword
4. Implement filtering
5. Implement sorting

### Phase 3: Advanced (Optional)

After Phase 2 works:
1. Add due date support
2. Validate date format (YYYY-MM-DD)
3. Display overdue warnings

## Testing Checklist

After each phase:

### Phase 1 Testing
- [ ] Add task appears in list
- [ ] Task has unique ID
- [ ] Update changes title
- [ ] Delete removes task
- [ ] Mark complete changes status
- [ ] Data persists after restart
- [ ] Invalid menu choice shows error
- [ ] Empty title is rejected
- [ ] Invalid ID shows error

### Phase 2 Testing
- [ ] Priority can be set to High/Medium/Low
- [ ] Category is saved and displayed
- [ ] Search finds matching tasks
- [ ] Filter shows only matching tasks
- [ ] Sorting works correctly

### Phase 3 Testing
- [ ] Due date is saved
- [ ] Invalid date format is rejected
- [ ] Overdue tasks are highlighted

## Common Issues

### File Not Found
- `tasks.txt` is created automatically on first run
- If deleted, it will be recreated (empty)

### Permission Errors
- Ensure write permissions in project directory
- Check file is not open in another program

### Encoding Issues
- Use UTF-8 encoding for Python file
- `tasks.txt` uses system default encoding

## Code Quality Guidelines

From constitution:
1. Functions under 50 lines when possible
2. Clear variable and function names
3. Comments for non-obvious logic
4. No code duplication
5. Single responsibility per function

## Next Steps

1. Run `/sp.tasks` to get implementation tasks
2. Implement tasks one at a time
3. Test after each task
4. Commit after completing features
