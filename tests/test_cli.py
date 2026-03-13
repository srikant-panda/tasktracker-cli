import sys
import unittest
from unittest.mock import patch

from src.cli import parse_args


class TestCliParser(unittest.TestCase):
    def test_add_command_parses_description_tokens(self):
        with patch.object(sys, "argv", ["task", "add", "learn", "python"]):
            args = parse_args()
        self.assertEqual(args.command, "add")
        self.assertEqual(args.description, ["learn", "python"])

    def test_list_command_defaults_to_all(self):
        with patch.object(sys, "argv", ["task", "list"]):
            args = parse_args()
        self.assertEqual(args.command, "list")
        self.assertEqual(args.type, "all")

    def test_mark_in_progress_requires_id(self):
        with patch.object(sys, "argv", ["task", "mark-in-progress"]):
            with self.assertRaises(SystemExit):
                parse_args()

    def test_mark_commands_parse_id(self):
        with patch.object(sys, "argv", ["task", "mark-in-progress", "abc-uuid"]):
            args = parse_args()
        self.assertEqual(args.command, "mark-in-progress")
        self.assertEqual(args.id, "abc-uuid")

        with patch.object(sys, "argv", ["task", "mark-done", "abc-uuid"]):
            args = parse_args()
        self.assertEqual(args.command, "mark-done")
        self.assertEqual(args.id, "abc-uuid")

        with patch.object(sys, "argv", ["task", "mark-todo", "abc-uuid"]):
            args = parse_args()
        self.assertEqual(args.command, "mark-todo")
        self.assertEqual(args.id, "abc-uuid")

    def test_update_command_parses_id_and_description(self):
        with patch.object(sys, "argv", ["task", "update", "abc-uuid", "new text"]):
            args = parse_args()
        self.assertEqual(args.command, "update")
        self.assertEqual(args.id, "abc-uuid")
        self.assertEqual(args.description, "new text")

    def test_delete_command_parses_id(self):
        with patch.object(sys, "argv", ["task", "delete", "abc-uuid"]):
            args = parse_args()
        self.assertEqual(args.command, "delete")
        self.assertEqual(args.id, "abc-uuid")

    def test_list_rejects_invalid_status(self):
        with patch.object(sys, "argv", ["task", "list", "invalid-status"]):
            with self.assertRaises(SystemExit):
                parse_args()


if __name__ == "__main__":
    unittest.main()