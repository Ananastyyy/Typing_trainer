from PyQt5.QtGui import QFont


class Font(QFont):
    def __init__(self):
        super().__init__()
        self.setFamily("Open Sans Medium")
        self.setPointSize(14)
