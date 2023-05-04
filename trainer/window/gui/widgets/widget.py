from PyQt5.QtWidgets import QWidget


class Widget(QWidget):
    def __init__(self, window: QWidget, x_val: int,
                 y_val: int, width: int, height: int) -> None:
        super().__init__(window)
        self.setGeometry(x_val, y_val, width, height)
