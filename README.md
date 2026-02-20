🚀 TaskTracker – Python CLI Task Manager

A modular, pip-installable command-line task manager built with Python.

Designed with clean architecture principles and a src/ layout, this project demonstrates separation of concerns, structured layering, and JSON-based persistence.

📦 Installation

Clone and install in editable mode:

git clone https://github.com/your-username/tasktracker.git
cd tasktracker
sudo pip install -e .  #sudo for make this global and add to /usr/bin/

Now use it globally:

tasktracker add "Build scalable CLI apps"
🖥️ Usage
tasktracker add "Learn clean architecture"
tasktracker list
tasktracker update 1 "Learn advanced Python design"
tasktracker mark 1 done
tasktracker delete 1

Available statuses:

todo

in-progress

done

🏗️ Project Structure
tasktracker/
├── pyproject.toml
├── main.py
└── src/
    ├── cli.py
    ├── operations.py
    ├── database.py
    ├── style.py
    ├── task_entities_config.py
    └── storage/task.json

__pycache__ and *.egg-info are auto-generated and should be ignored.

🧠 Architecture

The project follows a layered structure:

CLI Layer → Argument parsing & command routing

Operations Layer → Core business logic

Database Layer → JSON persistence

Style Layer → Output formatting

This ensures:

Maintainability

Clear responsibility boundaries

Easier future testing

Scalability

💾 Storage

Tasks are stored in:

src/storage/task.json

Example:

{
  "id": 1,
  "description": "Learn Python",
  "status": "todo",
  "created_at": "2026-02-20 10:00:00"
}
🛠 Tech Stack

Python 3.10+

argparse

tabulate

JSON persistence

pyproject.toml packaging