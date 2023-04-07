import unittest

from trainer.window.logic.line_handler import LineHandler


class TestLineHandler(unittest.TestCase):

    def test_set_blocked_text(self):
        handler = LineHandler()
        blocked_text = "test text"
        handler.set_blocked_text(blocked_text)
        self.assertEqual(handler.blocked_text, blocked_text)
        self.assertEqual(handler.size, len(blocked_text))
        self.assertEqual(handler.error_count, 0)
