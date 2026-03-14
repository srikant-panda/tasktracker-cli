# tasktracker-cli

A terminal task manager built with Python and packaged as a CLI app.

## Features

- Add, list, update, mark, and delete tasks
- Status tracking: todo, in-progress, done
- JSON storage on disk
- Table output in terminal
- Unit test coverage for parser, model, database, and operations

## Installation

```bash
git clone https://github.com/srikant-panda/tasktracker-cli.git
cd tasktracker-cli
pip install -e .
```
## Project Structure

```text
tasktracker-cli/
├── __init__.py
├── main.py
├── pyproject.toml
├── README.md
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── database.py
│   ├── model.py
│   ├── operations.py
│   ├── style.py
│   └── storage/
│       └── task.json
└── tests/
	├── test_cli.py
	├── test_database.py
	├── test_model.py
	└── test_operations.py
```


## CLI Usage

After installation, run:

```bash
tasktracker --help
```

Add tasks:

```bash
tasktracker add "Learn backend architecture"
```

List tasks:

```bash
tasktracker list
tasktracker list todo
tasktracker list in-progress
tasktracker list done
```

Update a task:

```bash
tasktracker update <task-id> "Updated description"
```

Mark task status:

```bash
tasktracker mark-in-progress <task-id>
tasktracker mark-done <task-id>
tasktracker mark-todo <task-id>
```

Delete a task:

```bash
tasktracker delete <task-id>
tasktracker delete \*
```

## Storage

Tasks are stored in:

```text
src/storage/task.json
```

## Running Tests

```bash
python -m unittest discover -s tests -v
```

