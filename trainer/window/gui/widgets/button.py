from PyQt5.QtWidgets import QPushButton, QWidget


class Button(QPushButton):
    def __init__(self, window: QWidget, button_text: str, stylesheet: str,
                 x_val: int, y_val: int, width: int, height: int):
        super().__init__(button_text, window)
        self.setGeometry(x_val, y_val, width, height)
        self.setStyleSheet(stylesheet)
