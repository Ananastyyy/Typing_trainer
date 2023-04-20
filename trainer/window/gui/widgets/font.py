import configparser

from PyQt5.QtGui import QFont


class Font(QFont):
    def __init__(self):
        super().__init__()
        self._config_init()
        self.setFamily(self.typeface)
        self.setPointSize(self.size)

    def _config_init(self):
        self.config = configparser.ConfigParser()
        self.config.read("config/widgets.ini")
        self.constants = dict(self.config.items("FONT"))
        self.typeface = self.constants["typeface"]
        self.size = int(self.constants["size"])
