from random import randint

from PyQt5.QtCore import QElapsedTimer
from PyQt5.QtGui import QPalette, QColor

from trainer.window.gui.widgets import Line


class SentenceGenerator:
    sentences = [
        "Съешь ещё этих мягких французских булок",
        "Мама мыла раму",
        "Я пошёл гулять в парк",
        "Он приготовил обед для своих друзей",
        "Ребёнок играл в футбол на улице"
    ]
    size = len(sentences)

    def get_sentence(self):
        return self.sentences[randint(0, self.size - 1)]


class LineHandler:
    def __init__(self):
        self.timer = QElapsedTimer()
        self.blocked_text = None
        self.wrong_input = False
        self.size = None

    def set_blocked_text(self, blocked_text: str):
        self.timer.start()
        self.blocked_text = blocked_text
        self.size = len(blocked_text)

    def handle(self, line_edit: Line) -> None or float:
        edit_text = line_edit.text()
        size = len(edit_text)
        if not size:
            return
        palette = line_edit.palette()
        is_match = edit_text == self.blocked_text[:size]
        palette.setColor(QPalette.Text, QColor('green') if is_match else QColor('red'))
        if not is_match and size > 1:
            if edit_text[-2] != self.blocked_text[size - 2]:
                line_edit.backspace()
        elif size == self.size:
            return 60000*size/self.timer.elapsed()
        line_edit.setPalette(palette)
