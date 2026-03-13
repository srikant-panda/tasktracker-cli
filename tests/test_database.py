import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.database import Task_database


class TestTaskDatabase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_path = Path(self.temp_dir.name)
        (self.base_path / "storage").mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _build_db(self):
        with patch("src.database.os.path.dirname", return_value=str(self.base_path)):
            return Task_database()

    def test_init_creates_task_file_with_empty_list(self):
        db = self._build_db()
        self.assertEqual(db.tasks, [])
        self.assertTrue((self.base_path / "storage" / "task.json").exists())

    def test_save_and_reload_roundtrip(self):
        db = self._build_db()
        db.tasks.append({"id": "1", "description": "task", "status": "todo", "created_at": "2026-03-14"})
        db.save()
        db.tasks = []
        reloaded = db.reload()
        self.assertEqual(len(reloaded), 1)
        self.assertEqual(reloaded[0]["description"], "task")

    def test_corrupted_json_resets_and_creates_backup(self):
        task_file = self.base_path / "storage" / "task.json"
        task_file.write_text("{bad json", encoding="utf-8")

        db = self._build_db()

        self.assertEqual(db.tasks, [])
        self.assertTrue((self.base_path / "storage" / "task.json.bak").exists())
        with task_file.open("r", encoding="utf-8") as handle:
            self.assertEqual(json.load(handle), [])


if __name__ == "__main__":
    unittest.main()