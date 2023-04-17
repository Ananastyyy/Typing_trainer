import unittest

from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import QLineEdit, QFrame

from trainer.window.logic.line_handler import LineHandler


class TestLineHandler(unittest.TestCase):

    def setUp(self):
        self.handler = LineHandler()
        self.blocked_text = "test text"
        self.line_edit = QLineEdit()
        self.right_line_edit = QLineEdit()

    def test_set_blocked_text(self):
        self.setUp()
        self.handler.set_blocked_text(self.blocked_text)
        self.assertEqual(self.handler.blocked_text, self.blocked_text)
        self.assertEqual(self.handler.size, len(self.blocked_text))
        self.assertEqual(self.handler.error_count, 0)

    def test_handle_with_wrong_text(self):
        self.setUp()
        self.line_edit.setText("teur")
        self.right_line_edit.setText("teu")
        self.palette = self.right_line_edit.palette()
        self.palette.setColor(QPalette.Text, QColor("red"))
        self.handler.handle(self.line_edit, None)
        self.assertEqual(self.line_edit.text(), self.right_line_edit.text())


if __name__ == "__main__":
    unittest.main()
