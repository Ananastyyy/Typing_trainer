from PyQt5.QtCore import QElapsedTimer
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QLineEdit


class LineHandler:
    def __init__(self):
        self.timer = QElapsedTimer()
        self.blocked_text = None
        self.size = None
        self.error_count = None

    def set_blocked_text(self, blocked_text: str):
        self.timer.start()
        self.error_count = 0
        self.blocked_text = blocked_text
        self.size = len(blocked_text)

    def handle(self, line_edit: QLineEdit) -> tuple[int, int] or None:
        edit_text = line_edit.text()
        size = len(edit_text)

        if not size:
            return None
        palette = line_edit.palette()
        is_match = edit_text == self.blocked_text[:size]
        palette.setColor(QPalette.Text, QColor('black') if is_match else QColor('red'))

        if not is_match:
            if size > 1:
                if edit_text[-2] != self.blocked_text[size - 2]:
                    line_edit.backspace()
            self.error_count += 1
        elif size == self.size:
            return int(60000 * size / self.timer.elapsed()), int(100 * self.error_count / size)

        line_edit.setPalette(palette)
