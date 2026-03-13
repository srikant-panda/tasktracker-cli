import unittest
from datetime import date
from uuid import UUID

from pydantic import ValidationError

from src.model import TaskModel


class TestTaskModel(unittest.TestCase):
    def test_model_defaults(self):
        task = TaskModel(description="Write tests")
        self.assertIsInstance(task.id, UUID)
        self.assertEqual(task.status, "todo")
        self.assertEqual(task.created_at, date.today())

    def test_model_rejects_invalid_status(self):
        with self.assertRaises(ValidationError):
            TaskModel(description="Bad status", status="blocked")

    def test_model_dump_json_serializes_uuid_and_date(self):
        task = TaskModel(description="Serialize")
        dumped = task.model_dump(mode="json")
        self.assertIsInstance(dumped["id"], str)
        self.assertIsInstance(dumped["created_at"], str)
        self.assertEqual(dumped["status"], "todo")


if __name__ == "__main__":
    unittest.main()