from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QMenuBar, QStatusBar, QMenu, QAction


class Widget(QWidget):
    def __init__(self, window: QWidget, x_val: int,
                 y_val: int, width: int, height: int):
        super().__init__(window)
        self.setGeometry(x_val, y_val, width, height)


class Button(QPushButton):
    def __init__(self, window: QWidget, button_text: str, stylesheet: str,
                 x_val: int, y_val: int, width: int, height: int):
        super().__init__(button_text, window)
        self.setGeometry(x_val, y_val, width, height)
        self.setStyleSheet(stylesheet)


class Label(QLabel):
    def __init__(self, window: QWidget, label_text: str, stylesheet: str,
                 font: QFont, x_val: int, y_val: int, width: int, height: int):
        super().__init__(label_text, window)
        self.setGeometry(x_val, y_val, width, height)
        self.setStyleSheet(stylesheet)
        self.setFont(font)


class Line(QLineEdit):
    def __init__(self, window: QWidget, font: QFont, x_val: int, y_val: int, width: int, height: int,
                 is_readable: bool):
        super().__init__(window)
        self.setGeometry(x_val, y_val, width, height)
        self.setReadOnly(is_readable)
        self.setFont(font)


class Menu(QMenu):
    def __init__(self, window: QWidget, title: str):
        super().__init__(window)
        self.setTitle(title)


class StatusBar(QStatusBar):
    def __init__(self, window: QWidget):
        super().__init__(window)


class MenuBar(QMenuBar):
    def __init__(self, window: QWidget, x_val: int, y_val: int, width: int, height: int):
        super().__init__(window)
        self.setGeometry(x_val, y_val, width, height)


class Action(QAction):
    def __init__(self, window: QWidget, text: str):
        super().__init__(window)
        self.setText(text)


class Font(QFont):
    def __init__(self):
        super().__init__()
        self.setFamily("Open Sans Medium")
        self.setPointSize(14)
