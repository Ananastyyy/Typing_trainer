from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QWidget


class Label(QLabel):
    def __init__(self, window: QWidget, label_text: str, stylesheet: str,
                 font: QFont, x_val: int, y_val: int, width: int,
                 height: int):
        super().__init__(label_text, window)
        self.setGeometry(x_val, y_val, width, height)
        self.setStyleSheet(stylesheet)
        self.setFont(font)
