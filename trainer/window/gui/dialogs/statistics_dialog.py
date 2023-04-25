import configparser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout


class StatisticsDialog(QDialog):
    def __init__(self, data: tuple):
        super().__init__()
        self._init_config_file()
        self._build_window(data)
        self.setModal(True)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)

    def _build_window(self, data: tuple):
        self.setWindowTitle(f"{self.stat}")
        self.sentences_label = QLabel(f"{self.solved}: {data[0]}")
        self.symbols_label = QLabel(f"{self.speed}: {data[1]}")
        self.rate_label = QLabel(f"{self.error}: {data[2]}")

        self.statistics_button = QPushButton(f"{self.verification}")
        self.statistics_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.sentences_label)
        layout.addWidget(self.symbols_label)
        layout.addWidget(self.rate_label)
        layout.addWidget(self.statistics_button)
        self.setLayout(layout)

    def _init_config_file(self):
        config = configparser.ConfigParser()
        config.read("config/dialogs.ini", encoding='utf-8')
        constants = dict(config.items("STATISTICS_DIALOG"))
        self.stat = constants["stat"]
        self.verification = constants["verification"]
        self.solved = constants["solved"]
        self.speed = constants["symb"]
        self.error = constants["error"]
