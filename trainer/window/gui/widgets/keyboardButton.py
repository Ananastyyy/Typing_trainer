from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QFrame

from trainer.window.gui.widgets.line import Line


class KeyboardButton(Line):
    def __init__(self, text: str, window: QFrame, font: QFont, x_val: int,
                 y_val: int, width: int, height: int, is_readable: bool,
                 name_hand: str, name_fingers: str) -> object:
        super().__init__(window, font, x_val, y_val, width, height,
                         is_readable)
        self.setText(text)
        self.name_hand = name_hand
        self.name_fingers = name_fingers
        self.setAlignment(Qt.AlignCenter)
