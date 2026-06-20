# Python TO-DO List Application

A feature-rich command-line TO-DO list app built in Python without the use of any frameworks or databases, just clean code and the standard library. Important for practicing file I/O, list/dict manipulation, sorting algorithms, and CLI design.

---

## Features

- ➕ **Add tasks** with text, priority, and an optional due date
- 👀 **View tasks** — see status, priority, and due date at a glance
- ✏️ **Edit tasks** — update text, priority, or due date anytime
- ✔️ **Mark tasks complete**
- 🗑️ **Delete tasks**
- 🔴🟡🟢 **Priority levels** — High / Medium / Low
- 📅 **Due dates** with format validation (`YYYY-MM-DD`)
- 🔍 **Search** tasks by keyword
- ↕️ **Sort** tasks by priority, due date, or completion status
- 🧹 **Clear completed** tasks in one click
- 💾 **Auto-saves** everything to `tasks.txt` — your list survives between runs

---

## Special Functions & Concepts Used

| Function / Concept | What it does |
|---|---|
| `load_tasks()` | Reads `tasks.txt` line by line and rebuilds the task list using `str.split("\|", 3)` |
| `save_tasks()` | Writes the current task list back to disk after every change |
| `get_task_index()` | Shared helper that safely validates user-entered task numbers (keeps code DRY) |
| `valid_date()` | Uses `datetime.strptime()` to validate `YYYY-MM-DD` input and catch bad formats |
| `choose_priority()` | Restricts priority input to a fixed set (High/Medium/Low) to avoid typos |
| `sort_tasks()` | Uses `list.sort(key=lambda ...)` with a priority-rank dictionary for custom ordering |
| `search_tasks()` | Uses a **list comprehension** to filter tasks by keyword |
| `clear_completed()` | Uses in-place list reassignment (`tasks[:] = [...]`) to remove finished tasks |

---

## 📚 Libraries Used

Built with **zero external dependencies** — just the Python standard library:

- [`os`](https://docs.python.org/3/library/os.html) — checks whether `tasks.txt` already exists
- [`datetime`](https://docs.python.org/3/library/datetime.html) — validates due dates against the `YYYY-MM-DD` format

> 💡 No `pip install` required — just clone and run.

---

## Requirements
- 🐍 Python 3.6 or higher

---

## 🖥️ Menu Overview

```
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
```

---

## 💾 How Tasks Are Stored

Tasks are saved in a plain text file called `tasks.txt`, created automatically in the same folder as the script.

**Format:** `done|priority|due_date|text`

- `done` → `1` for complete, `0` for incomplete
- `priority` → `High`, `Medium`, or `Low`
- `due_date` → optional, left blank if not set
- `text` → the task description


## Future Improvements

- 🔔 Due-date reminders shown on startup
- 📤 Export tasks to CSV
- 🏷️ Tags/categories for grouping tasks
- 🔁 Recurring tasks
- 🎨 Colored terminal output

