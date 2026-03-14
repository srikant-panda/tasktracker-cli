import unittest
from copy import deepcopy
from uuid import UUID
from unittest.mock import patch

from src import operations


class FakeTaskDatabase:
    store = []

    def __init__(self):
        self.tasks = self.__class__.store

    def reload(self):
        self.tasks = self.__class__.store
        return self.tasks

    def save(self):
        self.__class__.store = self.tasks

    def save_And_reload(self):
        self.save()
        return self.reload()


class TestOperations(unittest.TestCase):
    def setUp(self):
        self.patcher = patch("src.operations.TD", FakeTaskDatabase)
        self.patcher.start()
        FakeTaskDatabase.store = [
            {"id": "id-1", "description": "first", "status": "todo", "created_at": "2026-03-14"},
            {"id": "id-2", "description": "second", "status": "in-progress", "created_at": "2026-03-14"},
            {"id": "id-3", "description": "third", "status": "done", "created_at": "2026-03-14"},
        ]

    def tearDown(self):
        self.patcher.stop()

    def test_add_task_creates_and_persists_tasks(self):
        initial_count = len(FakeTaskDatabase.store)
        added = operations.add_task("new a")

        self.assertEqual(len(FakeTaskDatabase.store), initial_count + 1)
        self.assertEqual(FakeTaskDatabase.store[-1]["description"], "new a")
        self.assertEqual(FakeTaskDatabase.store[-1]["status"], "todo")
        self.assertIsInstance(added["id"], UUID)

    def test_list_tasks_filters_by_status(self):
        todo_tasks = operations.list_tasks("todo")
        in_progress_tasks = operations.list_tasks("in-progress")
        done_tasks = operations.list_tasks("done")
        all_tasks = operations.list_tasks("all")

        self.assertEqual(len(todo_tasks), 1)
        self.assertEqual(todo_tasks[0]["id"], "id-1")
        self.assertEqual(len(in_progress_tasks), 1)
        self.assertEqual(in_progress_tasks[0]["id"], "id-2")
        self.assertEqual(len(done_tasks), 1)
        self.assertEqual(done_tasks[0]["id"], "id-3")
        self.assertEqual(len(all_tasks), 3)

    def test_update_task_updates_existing(self):
        updated = operations.update_task("id-2", "changed")
        self.assertIsNotNone(updated)
        self.assertEqual(updated["description"], "changed")

    def test_update_task_returns_none_for_missing_id(self):
        before = deepcopy(FakeTaskDatabase.store)
        updated = operations.update_task("missing", "changed")
        self.assertIsNone(updated)
        self.assertEqual(FakeTaskDatabase.store, before)

    def test_delete_task_removes_matching_item(self):
        remaining = operations.delete_task("id-2")
        self.assertEqual(len(remaining), 2)
        remaining_ids = [item["id"] for item in remaining]
        self.assertNotIn("id-2", remaining_ids)

    def test_mark_task_updates_status(self):
        changed = operations.mark_task("id-1", "in-progress")
        self.assertTrue(changed)
        updated = [item for item in FakeTaskDatabase.store if item["id"] == "id-1"][0]
        self.assertEqual(updated["status"], "in-progress")

    def test_mark_task_returns_false_when_same_status(self):
        changed = operations.mark_task("id-3", "done")
        self.assertFalse(changed)

    def test_mark_task_returns_none_when_missing(self):
        changed = operations.mark_task("missing", "done")
        self.assertIsNone(changed)


if __name__ == "__main__":
    unittest.main()