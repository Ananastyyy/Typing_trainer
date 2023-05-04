from PyQt5.QtWidgets import QAction, QWidget


class Action(QAction):
    def __init__(self, window: QWidget, text: str) -> None:
        super().__init__(window)
        self.setText(text)
