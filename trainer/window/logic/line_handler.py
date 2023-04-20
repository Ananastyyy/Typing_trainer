from PyQt5.QtCore import QElapsedTimer
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QLineEdit

import config
from trainer.window.gui.widgets.keyboard import Keyboard
import configparser


class LineHandler:
    def __init__(self):
        self.timer = QElapsedTimer()
        self.blocked_text = None
        self.size = None
        self.error_count = None
        self.keyboard = None
        self._init_config_file()

    def _init_config_file(self):
        self.config = configparser.ConfigParser()
        self.config.read("config/logic.ini")
        self.constants = dict(self.config.items("LINE_HANDLER"))
        self.milliseconds_to_minutes = self.constants[
            "milliseconds_to_minutes"]

    def set_blocked_text(self, blocked_text: str):
        self.timer.start()
        self.error_count = 0
        self.blocked_text = blocked_text
        self.size = len(blocked_text)

    def handle(self, line_edit: QLineEdit, keyboard: Keyboard) \
            -> tuple[int, int] or None:
        edit_text = line_edit.text()
        size = len(edit_text)

        if not size:
            keyboard.select_button(self.blocked_text[0])
            return None

        is_match = edit_text == self.blocked_text[:size]
        palette = self._set_color_to_text(line_edit, is_match)

        if not is_match:
            keyboard.select_button("Backspace")
            if size > 1:
                if edit_text[-2] != self.blocked_text[size - 2]:
                    line_edit.backspace()
            self.error_count += 1
        elif size == self.size:
            return int(int(self.milliseconds_to_minutes)
                       * size / self.timer.elapsed()), self.error_count
        else:
            keyboard.select_button(self.blocked_text[size])

        line_edit.setPalette(palette)

    def _set_color_to_text(self, line_edit: QLineEdit, is_match: bool):
        palette = line_edit.palette()
        palette.setColor(QPalette.Text,
                         QColor(self.constants["color_for_right_text"])
                         if is_match else
                         QColor(self.constants["color_for_wrong_text"]))
        return palette
