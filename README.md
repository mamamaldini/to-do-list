# 📝 Python TODO List

A simple command-line TODO list application written in Python. Tasks are stored in a local text file, so your list persists between runs — no database or external dependencies required.

This repo includes two versions:

- **`todo_list.py`** — A basic version with core features (add, view, complete, delete).
- **`todo_list_advanced.py`** — An enhanced version with priorities, due dates, editing, searching, and sorting.

## Features

### Basic (`todo_list.py`)
- Add a task
- View all tasks
- Mark a task as complete
- Delete a task
- Tasks saved automatically to `tasks.txt`

### Advanced (`todo_list_advanced.py`)
Everything in the basic version, plus:
- **Priorities** — tag tasks as High, Medium, or Low
- **Due dates** — optional date in `YYYY-MM-DD` format
- **Edit tasks** — update text, priority, or due date
- **Search** — find tasks by keyword
- **Sort** — by priority, due date, or completion status
- **Clear completed** — remove all finished tasks in one step

## Requirements

- Python 3.6 or higher
- No external libraries — uses only the Python standard library (`os`, `datetime`)

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/python-todo-list.git
cd python-todo-list
```

## Usage

Run the basic version:

```bash
python todo_list.py
```

Run the advanced version:

```bash
python todo_list_advanced.py
```

You'll see a menu like this:

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

Enter the number corresponding to the action you want, and follow the prompts.

## How Tasks Are Stored

Tasks are saved in a plain text file called `tasks.txt`, created automatically in the same folder as the script.

- **Basic version format:** `done|text`
- **Advanced version format:** `done|priority|due_date|text`

Example (advanced):

```
0|High|2026-07-01|Finish project report
1|Medium||Buy groceries
```

> ⚠️ The two versions use different file formats. Avoid running both versions against the same `tasks.txt` file in the same folder, as it will cause read errors.

## Project Structure

```
python-todo-list/
├── todo_list.py            # Basic CLI TODO app
├── todo_list_advanced.py   # Advanced CLI TODO app with extra features
├── tasks.txt                # Auto-generated task storage (created on first run)
└── README.md
```

## Possible Future Improvements

- Categories/tags for tasks
- Due-date reminders shown on startup
- Export tasks to CSV
- A graphical interface using `tkinter`
- Recurring tasks

## License

This project is open source and available under the [MIT License](LICENSE).
