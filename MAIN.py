"Command-Line TO-DO List Application"

import os
from datetime import datetime

FILENAME = "tasks.txt"
PRIORITIES = {"1": "High", "2": "Medium", "3": "Low"}


def load_tasks():
    "Read tasks from file into a list of dicts."
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                line = line.rstrip("\n")
                if line:
                    parts = line.split("|", 3)
                    if len(parts) == 4:
                        done, priority, due, text = parts
                        tasks.append({
                            "done": done == "1",
                            "priority": priority,
                            "due": due,
                            "text": text,
                        })
    return tasks


def save_tasks(tasks):
    "Write all tasks back to the file."
    with open(FILENAME, "w") as f:
        for t in tasks:
            status = "1" if t["done"] else "0"
            f.write(f"{status}|{t['priority']}|{t['due']}|{t['text']}\n")


def valid_date(date_str):
    """Return True if date_str is empty or matches YYYY-MM-DD."""
    if date_str == "":
        return True
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def show_tasks(tasks, filtered=None):
    """Display tasks with index, status, priority, and due date.
    If 'filtered' is given, show that subset instead (search results)."""
    items = filtered if filtered is not None else tasks
    if not items:
        print("\nNo tasks to show.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(items, start=1):
        mark = "✔" if task["done"] else "✗"
        due = f" (due {task['due']})" if task["due"] else ""
        print(f"  {i}. [{mark}] ({task['priority']}) {task['text']}{due}")
    print()


def choose_priority():
    print("Priority: 1) High  2) Medium  3) Low")
    choice = input("Choose priority (default Medium): ").strip()
    return PRIORITIES.get(choice, "Medium")


def add_task(tasks):
    text = input("Enter new task: ").strip()
    if not text:
        print("Task cannot be empty.\n")
        return
    priority = choose_priority()
    due = input("Due date (YYYY-MM-DD, optional): ").strip()
    while not valid_date(due):
        print("Invalid date format.")
        due = input("Due date (YYYY-MM-DD, optional): ").strip()
    tasks.append({"done": False, "priority": priority, "due": due, "text": text})
    save_tasks(tasks)
    print("Task added!\n")


def get_task_index(tasks):
    """Helper: show tasks, ask for a number, return zero-based index or None."""
    show_tasks(tasks)
    if not tasks:
        return None
    try:
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            return num - 1
    except ValueError:
        pass
    print("Invalid task number.\n")
    return None


def complete_task(tasks):
    idx = get_task_index(tasks)
    if idx is not None:
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print("Task marked complete!\n")


def edit_task(tasks):
    idx = get_task_index(tasks)
    if idx is None:
        return
    task = tasks[idx]
    print(f"Editing: {task['text']}")
    new_text = input(f"New text (leave blank to keep '{task['text']}'): ").strip()
    if new_text:
        task["text"] = new_text
    change_priority = input("Change priority? (y/n): ").strip().lower()
    if change_priority == "y":
        task["priority"] = choose_priority()
    new_due = input(f"New due date (leave blank to keep '{task['due']}'): ").strip()
    if new_due != "" or input("Clear due date? (y/n): ").strip().lower() == "y":
        if valid_date(new_due):
            task["due"] = new_due
    save_tasks(tasks)
    print("Task updated!\n")


def delete_task(tasks):
    idx = get_task_index(tasks)
    if idx is not None:
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print(f"Deleted: {removed['text']}\n")


def clear_completed(tasks):
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t["done"]]
    save_tasks(tasks)
    removed = before - len(tasks)
    print(f"Removed {removed} completed task(s).\n")


def search_tasks(tasks):
    keyword = input("Search keyword: ").strip().lower()
    results = [t for t in tasks if keyword in t["text"].lower()]
    if results:
        show_tasks(tasks, filtered=results)
    else:
        print("No matching tasks found.\n")


def sort_tasks(tasks):
    print("Sort by: 1) Priority  2) Due date  3) Completion status")
    choice = input("Choose option: ").strip()
    priority_rank = {"High": 0, "Medium": 1, "Low": 2}

    if choice == "1":
        tasks.sort(key=lambda t: priority_rank.get(t["priority"], 3))
    elif choice == "2":
        # Tasks without a due date go to the end
        tasks.sort(key=lambda t: t["due"] if t["due"] else "9999-99-99")
    elif choice == "3":
        tasks.sort(key=lambda t: t["done"])
    else:
        print("Invalid option.\n")
        return
    save_tasks(tasks)
    print("Tasks sorted!\n")


def main():
    tasks = load_tasks()

    menu = """
========= TODO LIST =========
1. View tasks
2. Add task
3. Edit task
4. Mark task as complete
5. Delete task
6. Search tasks
7. Sort tasks
8. Clear completed tasks
9. Exit
==============================
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            search_tasks(tasks)
        elif choice == "7":
            sort_tasks(tasks)
        elif choice == "8":
            clear_completed(tasks)
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
