🚀 tasktracker

A modular, pip-installable CLI task manager built with Python.

Manage tasks directly from your terminal with a clean command interface and layered architecture.

⚡ Installation
```bash
git clone https://github.com/your-username/tasktracker.git
cd tasktracker
pip install -e .
```

After installation:
``` bash

tasktracker --help
🖥 Usage
Add a task
tasktracker add "Learn backend architecture"
List tasks
tasktracker list
Update a task
tasktracker update 1 "Learn advanced Python design"
Change task status
tasktracker mark 1 done
```
Available statuses:
``` bash
todo

in-progress

done

Delete a task
tasktracker delete 1
```
✨ Features
``` bash
Add, update, and delete tasks

Task status management

Clean tabulated terminal output

JSON-based persistence

Modular layered architecture

src/ layout packaging

CLI entry point via pyproject.toml
```

🏗 Project Structure
```bash
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
```
🧠 Architecture
``` bash
The project follows a layered design:

CLI Layer → Argument parsing & routing

Operations Layer → Core business logic

Database Layer → JSON persistence

Style Layer → Output formatting

This separation improves maintainability, clarity, and future scalability.
```