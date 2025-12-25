#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Console-Based Todo Application with User Authentication

A simple todo list manager using plain text storage.
Features:
- User authentication with separate data files
- Add, view, update, delete tasks
- Mark tasks as complete
- Priority and description support
- Search and filter capabilities
- Due date tracking
"""

import os
from datetime import datetime, date

USERS_FILE = "users.txt"
TASKS_FILE_PREFIX = "todos_"

# =============================================================================
# ANSI Color Codes for Clean, Formal Output
# =============================================================================

class Colors:
    """ANSI escape codes for terminal colors."""
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # Primary colors - clean and formal
    WHITE = "\033[37m"
    BLACK = "\033[30m"

    # Accent colors
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    BLUE = "\033[34m"

    # Light/bright versions for better visibility
    LIGHT_WHITE = "\033[97m"
    LIGHT_CYAN = "\033[96m"
    LIGHT_GREEN = "\033[92m"
    LIGHT_RED = "\033[91m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_MAGENTA = "\033[95m"


def colored(text, color):
    """Apply color to text."""
    return f"{color}{text}{Colors.RESET}"


def print_header(text):
    """Print a colored header."""
    print(f"\n{Colors.BOLD}{Colors.LIGHT_CYAN}{text}{Colors.RESET}")


def print_success(text):
    """Print success message in green."""
    print(colored(text, Colors.GREEN))


def print_error(text):
    """Print error message in red."""
    print(colored(text, Colors.RED))


def print_info(text):
    """Print info message in blue."""
    print(colored(text, Colors.BLUE))


def print_bold(text):
    """Print bold text."""
    print(colored(text, Colors.BOLD))


def get_today():
    """Get today's date from system."""
    return date.today()


def calculate_time_remaining(due_date_str):
    """Calculate time remaining until due date."""
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        today = get_today()

        if due_date == today:
            return "Due today!"

        days_remaining = (due_date - today).days

        if days_remaining < 0:
            return f"Overdue by {-days_remaining} day(s)"
        elif days_remaining == 1:
            return "Due tomorrow"
        elif days_remaining < 7:
            return f"Due in {days_remaining} days"
        elif days_remaining < 30:
            weeks = days_remaining // 7
            return f"Due in {weeks} week(s)"
        else:
            months = days_remaining // 30
            return f"Due in {months} month(s)"
    except ValueError:
        return ""


# =============================================================================
# USER AUTHENTICATION
# =============================================================================

def load_users():
    """Load users from users.txt file.
    Returns a dictionary: {username: password} (lowercase keys for case-insensitive lookup)"""
    users = {}
    if not os.path.exists(USERS_FILE):
        return users

    with open(USERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(" | ")
                if len(parts) >= 2:
                    # Store with lowercase key for case-insensitive lookup
                    users[parts[0].lower()] = (parts[0], parts[1])  # Store (original_name, password)
    return users


def save_users(users_dict):
    """Save users to users.txt file."""
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        for key, value in users_dict.items():
            original_name, password = value
            f.write(f"{original_name} | {password}\n")


def get_user_tasks_file(username):
    """Get the todo file path for a specific user."""
    # Use lowercase for filename to ensure consistency
    return f"{TASKS_FILE_PREFIX}{username.lower()}.txt"


def login():
    """Handle user login/registration.
    Returns (username, tasks_file) on success, or None on failure."""
    print_header("=== USER LOGIN ===")

    users = load_users()

    username_input = input(f"  {colored('Enter username:', Colors.LIGHT_CYAN)} ").strip()

    if not username_input:
        print_error("  Username cannot be empty.")
        return None

    username_lower = username_input.lower()

    if username_lower in users:
        # Existing user - verify password
        original_name, stored_password = users[username_lower]
        password = input(f"  {colored('Enter password:', Colors.LIGHT_CYAN)} ").strip()

        if stored_password == password:
            print_success(f"  Welcome back, {original_name}!")
            tasks_file = get_user_tasks_file(original_name)
            print_info(f"  Loading your todos from {tasks_file}")
            return (original_name, tasks_file)
        else:
            print_error("  Incorrect password!")
            return None
    else:
        # New user - create account
        print_info(f"  New user detected. Creating account for '{username_input}'.")

        password = input(f"  {colored('Create a password:', Colors.LIGHT_CYAN)} ").strip()

        if not password:
            print_error("  Password cannot be empty.")
            return None

        # Confirm password
        confirm_password = input(f"  {colored('Confirm password:', Colors.LIGHT_CYAN)} ").strip()

        if password != confirm_password:
            print_error("  Passwords do not match!")
            return None

        # Save new user (store original name with lowercase key)
        users[username_lower] = (username_input, password)
        save_users(users)

        # Create user's todo file (use lowercase for filename)
        tasks_file = get_user_tasks_file(username_input)
        open(tasks_file, "a", encoding="utf-8").close()

        print_success(f"  Account created successfully!")
        print_success(f"  Welcome, {username_input}! Your todo file has been created.")
        return (username_input, tasks_file)


# =============================================================================
# PHASE 2: FOUNDATIONAL - File I/O and Helper Functions
# =============================================================================

def load_tasks(tasks_file):
    """Read tasks from user's tasks file.
    Returns a list of task dictionaries."""
    tasks = []
    if not os.path.exists(tasks_file):
        return tasks

    with open(tasks_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                task = parse_task(line)
                if task:
                    tasks.append(task)
    return tasks


def save_tasks(tasks, tasks_file):
    """Write all tasks to user's tasks file."""
    with open(tasks_file, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(format_task(task) + "\n")


def parse_task(line):
    """Parse a single line from tasks file into a task dictionary.
    Format: ID | Title | Status | Priority | Description | DueDate | CreatedAt"""
    parts = line.split(" | ")
    if len(parts) < 7:
        return None

    try:
        return {
            "id": int(parts[0]),
            "title": parts[1],
            "status": parts[2],
            "priority": parts[3],
            "description": parts[4],
            "due_date": parts[5],
            "created_at": parts[6] if len(parts) > 6 else ""
        }
    except (ValueError, IndexError):
        return None


def format_task(task):
    """Format a task dictionary into a line for tasks file."""
    return " | ".join([
        str(task["id"]),
        task["title"],
        task["status"],
        task["priority"],
        task.get("description", ""),
        task["due_date"],
        task.get("created_at", "")
    ])


def validate_title(title):
    """Validate that task title is not empty."""
    return bool(title.strip())


def validate_due_date(due_date_str):
    """Validate that due date is not in the past."""
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        today = get_today()
        if due_date < today:
            return False, f"Date cannot be in the past. Please select a date from {today} onwards."
        return True, ""
    except ValueError:
        return False, "Invalid date format. Please use YYYY-MM-DD (e.g., 2025-12-31)"


def get_next_id(tasks):
    """Get the next sequential ID for a new task."""
    if not tasks:
        return 1
    max_id = max(task["id"] for task in tasks)
    return max_id + 1


# =============================================================================
# PHASE 3: USER STORY 1 - Add and View Tasks
# =============================================================================

def display_menu():
    """Display the main menu with clean colors."""
    print_header("=== TODO APPLICATION ===")
    print(f"  {colored('1.', Colors.LIGHT_CYAN)} {colored('Add Task', Colors.WHITE)}")
    print(f"  {colored('2.', Colors.LIGHT_CYAN)} {colored('View Tasks', Colors.WHITE)}")
    print(f"  {colored('3.', Colors.LIGHT_CYAN)} {colored('Update Task', Colors.WHITE)}")
    print(f"  {colored('4.', Colors.LIGHT_CYAN)} {colored('Delete Task', Colors.WHITE)}")
    print(f"  {colored('5.', Colors.LIGHT_CYAN)} {colored('Mark Task as Complete', Colors.WHITE)}")
    print(f"  {colored('6.', Colors.LIGHT_CYAN)} {colored('Search / Filter Tasks', Colors.WHITE)}")
    print(f"  {colored('7.', Colors.LIGHT_CYAN)} {colored('Exit', Colors.LIGHT_RED)}")
    print()


def add_task(tasks, tasks_file):
    """Add a new task with date input."""
    print_header("--- ADD TASK ---")

    title = input(f"  {colored('Enter task title:', Colors.LIGHT_CYAN)} ").strip()
    if not validate_title(title):
        print_error("  Error: Task title cannot be empty.")
        return

    # Priority selection with clean colors
    print(f"  {colored('Priority:', Colors.LIGHT_CYAN)}")
    print(f"    {colored('1.', Colors.LIGHT_CYAN)} {colored('High', Colors.LIGHT_RED)}   - Urgent tasks")
    print(f"    {colored('2.', Colors.LIGHT_CYAN)} {colored('Medium', Colors.WHITE)} - Normal priority")
    print(f"    {colored('3.', Colors.LIGHT_CYAN)} {colored('Low', Colors.LIGHT_GREEN)}  - When you can")

    priority_choice = input(f"  {colored('Select (1-3):', Colors.LIGHT_CYAN)} ").strip()
    priority_map = {"1": "High", "2": "Medium", "3": "Low"}
    priority = priority_map.get(priority_choice, "Medium")

    # Description input
    description = input(f"  {colored('Description (optional):', Colors.LIGHT_CYAN)} ").strip()

    # Due date input with validation
    while True:
        due_date = input(f"  {colored('Due date (YYYY-MM-DD) or press Enter:', Colors.LIGHT_CYAN)} ").strip()
        if not due_date:
            break
        is_valid, message = validate_due_date(due_date)
        if is_valid:
            # Calculate and show time remaining
            time_remaining = calculate_time_remaining(due_date)
            print_info(f"  Time remaining: {time_remaining}")
            break
        else:
            print_error(f"  {message}")

    # Created date (auto-generated)
    created_at = datetime.now().strftime("%Y-%m-%d")

    task = {
        "id": get_next_id(tasks),
        "title": title,
        "status": "Pending",
        "priority": priority,
        "description": description,
        "due_date": due_date,
        "created_at": created_at
    }

    tasks.append(task)
    save_tasks(tasks, tasks_file)

    # Success message with clean colors
    task_id = task["id"]
    print_success(f"  Task added successfully! {colored(f'ID: {task_id}', Colors.LIGHT_CYAN)}")

    # Show task summary with clean colors
    priority_color_map = {
        "High": Colors.LIGHT_RED,
        "Medium": Colors.WHITE,
        "Low": Colors.LIGHT_GREEN
    }
    print_bold(f"  Summary:")
    print(f"    {colored('Title:', Colors.LIGHT_CYAN)} {colored(task['title'], Colors.WHITE)}")
    print(f"    {colored('Priority:', Colors.LIGHT_CYAN)} {colored(task['priority'], priority_color_map.get(task['priority'], Colors.WHITE))}")
    print(f"    {colored('Description:', Colors.LIGHT_CYAN)} {colored(task['description'] if task['description'] else 'None', Colors.WHITE)}")
    if task['due_date']:
        print(f"    {colored('Due Date:', Colors.LIGHT_CYAN)} {colored(task['due_date'], Colors.LIGHT_BLUE)} ({calculate_time_remaining(task['due_date'])})")
    else:
        print(f"    {colored('Due Date:', Colors.LIGHT_CYAN)} {colored('None', Colors.WHITE)}")


def view_tasks(tasks):
    """Display all tasks with clean colors - full title and description on separate lines."""
    if not tasks:
        print_info("  No tasks found. Add a task to get started!")
        return

    print_header("=== TASK LIST ===")

    for task in tasks:
        # Clean status colors with checkmark for complete
        if task["status"] == "Complete":
            status = colored("[COMPLETE] ", Colors.LIGHT_GREEN) + colored("✔", Colors.LIGHT_GREEN)
        else:
            status = colored("[PENDING]", Colors.WHITE)

        # Clean due date display with time remaining
        due_date = task["due_date"]
        time_info = ""
        if due_date:
            try:
                due = datetime.strptime(due_date, "%Y-%m-%d").date()
                today = get_today()
                if due < today:
                    due_date = colored(due_date, Colors.LIGHT_RED)
                    time_info = colored(f"(Overdue)", Colors.LIGHT_RED)
                elif due == today:
                    due_date = colored(due_date, Colors.LIGHT_GREEN)
                    time_info = colored(f"(Due today!)", Colors.LIGHT_GREEN)
                else:
                    days_left = (due - today).days
                    if days_left <= 3:
                        due_date = colored(due_date, Colors.LIGHT_RED)
                    elif days_left <= 7:
                        due_date = colored(due_date, Colors.WHITE)
                    else:
                        due_date = colored(due_date, Colors.LIGHT_BLUE)
                    time_info = colored(f"({days_left} days)", Colors.WHITE)
            except ValueError:
                time_info = ""

        # Status color for title
        if task["status"] == "Complete":
            title_color = Colors.LIGHT_GREEN
        else:
            title_color = Colors.WHITE

        # Display ID, Due Date, Status on first line
        task_id = task["id"]
        row1 = f"  {colored(f'ID: {task_id}', Colors.LIGHT_CYAN)} | "
        row1 += f"{colored('Due:', Colors.LIGHT_BLUE)} {due_date} {time_info} | "
        row1 += f"{status}"
        print(row1)

        # Display full title on second line
        print(f"  {colored('Title:', Colors.LIGHT_CYAN)} {colored(task['title'], title_color)}")

        # Display full description on third line
        desc = task.get("description", "")
        if desc:
            print(f"  {colored('Desc:', Colors.LIGHT_CYAN)} {colored(desc, Colors.LIGHT_CYAN)}")
        else:
            print(f"  {colored('Desc:', Colors.LIGHT_CYAN)} {colored('---', Colors.WHITE)}")

        # Separator between tasks
        print(f"  {'-' * 60}")

    print(f"\n  {colored(f'{len(tasks)} task(s) found.', Colors.WHITE)}")


# =============================================================================
# PHASE 4: USER STORY 2 - Update and Delete Tasks
# =============================================================================

def update_task(tasks, tasks_file):
    """Update an existing task's title and description."""
    if not tasks:
        print_info("  No tasks to update.")
        return

    try:
        task_id = int(input(f"  {colored('Enter task ID to update:', Colors.LIGHT_CYAN)} "))
    except ValueError:
        print_error("  Please enter a valid number.")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print_error(f"  Error: Task with ID {task_id} not found.")
        return

    # Show current task details
    print(f"  {colored('Current title:', Colors.WHITE)} {colored(task['title'], Colors.LIGHT_CYAN)}")
    current_desc = task.get('description', '')
    print(f"  {colored('Current description:', Colors.WHITE)} {colored(current_desc if current_desc else 'None', Colors.LIGHT_CYAN)}")

    # Update title
    new_title = input(f"  {colored('Enter new title (or press Enter to keep current):', Colors.LIGHT_CYAN)} ").strip()

    if new_title:
        if not validate_title(new_title):
            print_error("  Error: Task title cannot be empty.")
            return
        task["title"] = new_title

    # Update description
    new_description = input(f"  {colored('Enter new description (or press Enter to keep current):', Colors.LIGHT_CYAN)} ").strip()
    if new_description:
        task["description"] = new_description

    if new_title or new_description:
        save_tasks(tasks, tasks_file)
        print_success("  Task updated successfully!")
    else:
        print_info("  No changes made.")


def delete_task(tasks, tasks_file):
    """Delete a task by ID."""
    if not tasks:
        print_info("  No tasks to delete.")
        return

    try:
        task_id = int(input(f"  {colored('Enter task ID to delete:', Colors.LIGHT_CYAN)} "))
    except ValueError:
        print_error("  Please enter a valid number.")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print_error(f"  Error: Task with ID {task_id} not found.")
        return

    # Clean confirmation
    task_title = task["title"]
    confirm_prompt = colored('Are you sure you want to delete', Colors.LIGHT_CYAN)
    confirm_prompt += colored(f'"{task_title}"', Colors.LIGHT_RED)
    confirm_prompt += colored('? (y/n):', Colors.LIGHT_CYAN)
    confirm = input(f"  {confirm_prompt} ").lower()
    if confirm != "y":
        print_info("  Delete cancelled.")
        return

    # Delete task by modifying list in place
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            del tasks[i]
            break
    save_tasks(tasks, tasks_file)
    print_success("  Task deleted successfully!")


# =============================================================================
# PHASE 5: USER STORY 3 - Mark Complete
# =============================================================================

def mark_complete(tasks, tasks_file):
    """Mark a task as complete."""
    if not tasks:
        print_info("  No tasks to mark as complete.")
        return

    try:
        task_id = int(input(f"  {colored('Enter task ID to mark complete:', Colors.LIGHT_CYAN)} "))
    except ValueError:
        print_error("  Please enter a valid number.")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print_error(f"  Error: Task with ID {task_id} not found.")
        return

    task_title = task["title"]
    if task["status"] == "Complete":
        print_info(f'  Task "{task_title}" is already complete!')
        return

    task["status"] = "Complete"
    save_tasks(tasks, tasks_file)

    # Clean celebration message with checkmark
    print_success(f"  Task completed! ✔")
    completed_msg = colored(f'"{task_title}"', Colors.LIGHT_GREEN)
    completed_msg += colored(' has been marked as complete!', Colors.LIGHT_GREEN)
    print(f"  {completed_msg}")


# =============================================================================
# PHASE 6: USER STORY 4 - Priority and Categories
# =============================================================================

def set_priority(tasks, tasks_file):
    """Set priority for a task."""
    if not tasks:
        print_info("  No tasks available.")
        return

    try:
        task_id = int(input(f"  {colored('Enter task ID:', Colors.LIGHT_CYAN)} "))
    except ValueError:
        print_error("  Please enter a valid number.")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print_error(f"  Error: Task with ID {task_id} not found.")
        return

    print(f"  {colored('Current priority:', Colors.WHITE)} {colored(task['priority'], Colors.WHITE)}")
    print(f"  {colored('Select new priority:', Colors.LIGHT_CYAN)}")
    print(f"    {colored('1.', Colors.LIGHT_CYAN)} {colored('High', Colors.LIGHT_RED)}")
    print(f"    {colored('2.', Colors.LIGHT_CYAN)} {colored('Medium', Colors.WHITE)}")
    print(f"    {colored('3.', Colors.LIGHT_CYAN)} {colored('Low', Colors.LIGHT_GREEN)}")

    choice = input(f"  {colored('Select (1-3):', Colors.LIGHT_CYAN)} ").strip()
    priority_map = {"1": "High", "2": "Medium", "3": "Low"}
    priority = priority_map.get(choice, "Medium")

    task["priority"] = priority
    save_tasks(tasks, tasks_file)
    print_success(f"  Priority set to {colored(priority, Colors.LIGHT_CYAN)}!")


def set_description(tasks, tasks_file):
    """Set description for a task."""
    if not tasks:
        print_info("  No tasks available.")
        return

    try:
        task_id = int(input(f"  {colored('Enter task ID:', Colors.LIGHT_CYAN)} "))
    except ValueError:
        print_error("  Please enter a valid number.")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print_error(f"  Error: Task with ID {task_id} not found.")
        return

    current_desc = task.get('description', '')
    print(f"  {colored('Current description:', Colors.WHITE)} {colored(current_desc if current_desc else 'None', Colors.LIGHT_CYAN)}")
    description = input(f"  {colored('Enter description (or press Enter for no description):', Colors.LIGHT_CYAN)} ").strip()
    task["description"] = description
    save_tasks(tasks, tasks_file)
    print_success(f"  Description set to {colored(description if description else 'None', Colors.LIGHT_CYAN)}!")


# =============================================================================
# PHASE 7: USER STORY 5 - Search and Filter
# =============================================================================

def search_tasks(tasks, keyword):
    """Search tasks by keyword in title."""
    keyword = keyword.lower()
    results = [t for t in tasks if keyword in t["title"].lower()]
    return results


def filter_tasks(tasks, criteria_type, criteria_value):
    """Filter tasks by criteria."""
    if criteria_type == "status":
        return [t for t in tasks if t["status"] == criteria_value]
    elif criteria_type == "priority":
        return [t for t in tasks if t["priority"] == criteria_value]
    elif criteria_type == "description":
        return [t for t in tasks if criteria_value in t.get("description", "")]
    return []


def sort_tasks(tasks, sort_by):
    """Sort tasks by specified criteria."""
    if sort_by == "id":
        return sorted(tasks, key=lambda x: x["id"])
    elif sort_by == "title":
        return sorted(tasks, key=lambda x: x["title"].lower())
    elif sort_by == "priority":
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        return sorted(tasks, key=lambda x: priority_order.get(x["priority"], 4))
    elif sort_by == "due_date":
        return sorted(tasks, key=lambda x: x["due_date"] or "z" * 20)
    elif sort_by == "created":
        return sorted(tasks, key=lambda x: x.get("created_at", "") or "z" * 20)
    return tasks


def search_filter_menu(tasks, tasks_file):
    """Sub-menu for search and filter operations."""
    while True:
        print_header("=== SEARCH / FILTER ===")
        print(f"  {colored('1.', Colors.LIGHT_CYAN)} {colored('Search by keyword', Colors.WHITE)}")
        print(f"  {colored('2.', Colors.LIGHT_CYAN)} {colored('Filter by status', Colors.WHITE)}")
        print(f"  {colored('3.', Colors.LIGHT_CYAN)} {colored('Filter by priority', Colors.WHITE)}")
        print(f"  {colored('4.', Colors.LIGHT_CYAN)} {colored('Filter by description', Colors.WHITE)}")
        print(f"  {colored('5.', Colors.LIGHT_CYAN)} {colored('Sort tasks', Colors.WHITE)}")
        print(f"  {colored('6.', Colors.LIGHT_CYAN)} {colored('Show all tasks', Colors.WHITE)}")
        print(f"  {colored('7.', Colors.LIGHT_CYAN)} {colored('Back to main menu', Colors.LIGHT_RED)}")

        choice = input(f"\n  {colored('Enter choice:', Colors.LIGHT_CYAN)} ").strip()

        if choice == "1":
            keyword = input(f"  {colored('Enter keyword to search:', Colors.LIGHT_CYAN)} ").strip()
            results = search_tasks(tasks, keyword)
            if results:
                print(f"\n  {colored(f'Found {len(results)} task(s):', Colors.LIGHT_GREEN)}")
                for task in results:
                    if task["status"] == "Complete":
                        print(f"    {colored(str(task['id']), Colors.LIGHT_CYAN)}. {colored(task['title'], Colors.LIGHT_GREEN)} {colored('[COMPLETE] ✔', Colors.LIGHT_GREEN)}")
                    else:
                        print(f"    {colored(str(task['id']), Colors.LIGHT_CYAN)}. {colored(task['title'], Colors.WHITE)} {colored('[PENDING]', Colors.WHITE)}")
            else:
                print_info("  No tasks found matching your criteria.")
        elif choice == "2":
            print(f"  {colored('1.', Colors.LIGHT_CYAN)} {colored('Pending', Colors.WHITE)}")
            print(f"  {colored('2.', Colors.LIGHT_CYAN)} {colored('Complete', Colors.LIGHT_GREEN)}")
            status_choice = input(f"  {colored('Enter status:', Colors.LIGHT_CYAN)} ").strip()
            status = "Complete" if status_choice == "2" else "Pending"
            results = filter_tasks(tasks, "status", status)
            print(f"\n  {colored(f'{len(results)} task(s) with status', Colors.WHITE)} {colored(status, Colors.LIGHT_CYAN)}:")
            for task in results:
                print(f"    {colored(str(task['id']), Colors.LIGHT_CYAN)}. {colored(task['title'], Colors.WHITE)}")
        elif choice == "3":
            print(f"  {colored('1.', Colors.LIGHT_CYAN)} {colored('High', Colors.LIGHT_RED)}")
            print(f"  {colored('2.', Colors.LIGHT_CYAN)} {colored('Medium', Colors.WHITE)}")
            print(f"  {colored('3.', Colors.LIGHT_CYAN)} {colored('Low', Colors.LIGHT_GREEN)}")
            pri_choice = input(f"  {colored('Enter priority:', Colors.LIGHT_CYAN)} ").strip()
            priority_map = {"1": "High", "2": "Medium", "3": "Low"}
            priority = priority_map.get(pri_choice)
            if priority:
                results = filter_tasks(tasks, "priority", priority)
                print(f"\n  {colored(f'{len(results)} task(s) with priority', Colors.WHITE)} {colored(priority, Colors.LIGHT_CYAN)}:")
                for task in results:
                    print(f"    {colored(str(task['id']), Colors.LIGHT_CYAN)}. {colored(task['title'], Colors.WHITE)}")
        elif choice == "4":
            description = input(f"  {colored('Enter description keyword:', Colors.LIGHT_CYAN)} ").strip()
            results = filter_tasks(tasks, "description", description)
            print(f"\n  {colored(f'{len(results)} task(s) with description containing', Colors.WHITE)} {colored(description, Colors.LIGHT_CYAN)}:")
            for task in results:
                print(f"    {colored(str(task['id']), Colors.LIGHT_CYAN)}. {colored(task['title'], Colors.WHITE)}")
        elif choice == "5":
            print(f"  {colored('Sort by:', Colors.LIGHT_CYAN)}")
            print(f"    {colored('1.', Colors.LIGHT_CYAN)} {colored('ID', Colors.WHITE)}")
            print(f"    {colored('2.', Colors.LIGHT_CYAN)} {colored('Title', Colors.WHITE)}")
            print(f"    {colored('3.', Colors.LIGHT_CYAN)} {colored('Priority', Colors.WHITE)}")
            print(f"    {colored('4.', Colors.LIGHT_CYAN)} {colored('Due Date', Colors.WHITE)}")
            print(f"    {colored('5.', Colors.LIGHT_CYAN)} {colored('Created Date', Colors.WHITE)}")
            sort_choice = input(f"  {colored('Enter choice:', Colors.LIGHT_CYAN)} ").strip()
            sort_map = {"1": "id", "2": "title", "3": "priority", "4": "due_date", "5": "created"}
            sort_by = sort_map.get(sort_choice)
            if sort_by:
                results = sort_tasks(tasks, sort_by)
                print(f"\n  {colored(f'Tasks sorted by {sort_by}:', Colors.LIGHT_CYAN)}")
                for task in results:
                    priority_color = {"High": Colors.LIGHT_RED, "Medium": Colors.WHITE, "Low": Colors.LIGHT_GREEN}
                    print(f"    {colored(str(task['id']), Colors.LIGHT_CYAN)}. {colored(task['title'], Colors.WHITE)} [{colored(task['priority'], priority_color.get(task['priority'], Colors.WHITE))}]")
        elif choice == "6":
            view_tasks(tasks)
        elif choice == "7":
            break
        else:
            print_error("  Invalid choice. Please enter 1-7.")


# =============================================================================
# PHASE 8: USER STORY 6 - Due Dates
# =============================================================================

def validate_date(date_str):
    """Validate date is in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def set_due_date(tasks, tasks_file):
    """Set due date for a task."""
    if not tasks:
        print_info("  No tasks available.")
        return

    try:
        task_id = int(input(f"  {colored('Enter task ID:', Colors.LIGHT_CYAN)} "))
    except ValueError:
        print_error("  Please enter a valid number.")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print_error(f"  Error: Task with ID {task_id} not found.")
        return

    print(f"  {colored('Current due date:', Colors.WHITE)} {colored(task['due_date'] if task['due_date'] else 'None', Colors.LIGHT_BLUE)}")

    while True:
        due_date = input(f"  {colored('Enter due date (YYYY-MM-DD) or press Enter:', Colors.LIGHT_CYAN)} ").strip()
        if not due_date:
            break
        is_valid, message = validate_due_date(due_date)
        if is_valid:
            time_remaining = calculate_time_remaining(due_date)
            print_info(f"  Time remaining: {time_remaining}")
            break
        else:
            print_error(f"  {message}")

    task["due_date"] = due_date
    save_tasks(tasks, tasks_file)

    if due_date:
        print_success(f"  Due date set to {colored(due_date, Colors.LIGHT_BLUE)}!")
    else:
        print_info("  Due date cleared.")


# =============================================================================
# PHASE 9: POLISH - Main Loop and Error Handling
# =============================================================================

def main_loop(username, tasks_file):
    """Main application loop for authenticated user."""
    tasks = load_tasks(tasks_file)

    # Welcome message
    print_header("=== WELCOME TO TODO APP ===")
    print(f"  {colored(f'Hello, {username}!', Colors.LIGHT_CYAN)}")
    print(f"  {colored(f'You have {len(tasks)} task(s).', Colors.WHITE)}")
    print()

    while True:
        display_menu()
        choice = input(f"  {colored('Enter your choice:', Colors.LIGHT_CYAN)} ").strip()

        if choice == "1":
            add_task(tasks, tasks_file)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks, tasks_file)
        elif choice == "4":
            delete_task(tasks, tasks_file)
        elif choice == "5":
            mark_complete(tasks, tasks_file)
        elif choice == "6":
            search_filter_menu(tasks, tasks_file)
        elif choice == "7":
            # Save before exit
            save_tasks(tasks, tasks_file)
            print(f"\n  {colored('Goodbye,', Colors.LIGHT_CYAN)} {colored(username, Colors.WHITE)} {colored('!', Colors.LIGHT_CYAN)}")
            print(f"  {colored('Your todos have been saved.', Colors.WHITE)}")
            print(f"  {colored('See you next time!', Colors.LIGHT_CYAN)}")
            break
        else:
            print_error("  Invalid choice. Please enter 1-7.")


def main():
    """Main entry point."""
    # First, authenticate user
    result = login()
    if result is None:
        print_error("  Authentication failed. Exiting.")
        return

    username, tasks_file = result
    # Then run the main application loop
    main_loop(username, tasks_file)


if __name__ == "__main__":
    main()
