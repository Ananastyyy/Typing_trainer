from PyQt5.QtWidgets import QMenu, QWidget


class Menu(QMenu):
    def __init__(self, window: QWidget, title: str) -> None:
        super().__init__(window)
        self.setTitle(title)
