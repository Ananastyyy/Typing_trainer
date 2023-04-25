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
        result = self.handle_text(line_edit.text())
        line_edit.setText(result[0])
        palette = self._set_color_to_text(line_edit, result[1])

        text = result[0]

        if not len(text):
            return None

        elif len(text) == self.size:
            return int(int(self.milliseconds_to_minutes)
                       * len(text) / self.timer.elapsed()), self.error_count

        self._select_button(keyboard, result[0], result[1])
        line_edit.setPalette(palette)

    def handle_text(self, text: str) -> tuple[str, bool]:
        size = len(text)
        is_match = text == self.blocked_text[:size]

        if not is_match:
            if size > 1:
                if text[-2] != self.blocked_text[size - 2]:
                    text = text[:size - 1]
            self.error_count += 1
            code = False
        else:
            code = True
        return text, code

    def _set_color_to_text(self, line_edit: QLineEdit, is_match: bool):
        palette = line_edit.palette()
        palette.setColor(QPalette.Text,
                         QColor(self.constants["color_for_right_text"])
                         if is_match else
                         QColor(self.constants["color_for_wrong_text"]))
        return palette

    def _select_button(self, keyboard: Keyboard, text: str, code: bool):
        if code:
            keyboard.select_button(self.blocked_text[len(text)])
        else:
            keyboard.select_button("Backspace")
