import unittest

from trainer.window.logic.line_handler import LineHandler


class TestTypingTrainer(unittest.TestCase):
    def setUp(self):
        self.line_handler = LineHandler()
        self.line_handler.set_blocked_text("Hello World")

    def test_handle_text_with_empty_string(self):
        self.setUp()
        result = self.line_handler.handle_text("")
        expected_result = ("", True)
        self.assertEqual(result, expected_result)

    def test_handle_text_with_incorrect_text(self):
        result = self.line_handler.handle_text("Hedd")
        expected_result = ("Hed", False)
        self.assertEqual(result, expected_result)

    def test_handle_text_with_correct_text(self):
        result = self.line_handler.handle_text("Hello World")
        expected_result = ("Hello World", True)
        self.assertEqual(result, expected_result)
