import sys
import threading

from PyQt5.QtWidgets import QApplication

from trainer.window.window import Window


class GUIThread(threading.Thread):
    def __init__(self) -> None:
        super().__init__()
        self.app = QApplication(sys.argv)

    def start(self) -> None:
        window = Window()
        sys.exit(self.app.exec_())
