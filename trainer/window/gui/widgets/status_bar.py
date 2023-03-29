from PyQt5.QtWidgets import QStatusBar, QWidget


class StatusBar(QStatusBar):
    def __init__(self, window: QWidget):
        super().__init__(window)
