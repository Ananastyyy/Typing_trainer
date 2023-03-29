from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit, QWidget


class Line(QLineEdit):
    def __init__(self, window: QWidget, font: QFont, x_val: int, y_val: int, width: int, height: int,
                 is_readable: bool):
        super().__init__(window)
        self.setGeometry(x_val, y_val, width, height)
        self.setReadOnly(is_readable)
        self.setFont(font)
