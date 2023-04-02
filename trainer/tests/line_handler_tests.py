import unittest

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QLineEdit

from trainer.window.logic.line_handler import LineHandler


class TestLineHandler(unittest.TestCase):

    def test_set_blocked_text(self):
        handler = LineHandler()
        blocked_text = "test text"
        handler.set_blocked_text(blocked_text)
        self.assertEqual(handler.blocked_text, blocked_text)
        self.assertEqual(handler.size, len(blocked_text))
        self.assertEqual(handler.error_count, 0)

    # def test_handle_with_wrong_char(self):
    #     handler = LineHandler()
    #     blocked_text = "test text"
    #     handler.set_blocked_text(blocked_text)
    #     line_edit = QLineEdit()
    #
    #     line_edit.setText("abc")
    #     handler.handle(line_edit)
    #     self.assertEqual(line_edit.palette().color(QPalette.Text), QColor('red'))
    #
    #     line_edit.setText("t")
    #     handler.handle(line_edit)
    #     self.assertEqual(line_edit.palette().color(QPalette.Text), QColor('green'))
    #
    #     line_edit.setText("")
    #     handler.handle(line_edit)
    #     self.assertEqual(line_edit.palette().color(QPalette.Text), QColor('green'))