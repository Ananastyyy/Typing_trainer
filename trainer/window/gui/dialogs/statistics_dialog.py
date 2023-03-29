from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout

from trainer.window.logic.database_handler import DatabaseHandler


class StatisticsDialog(QDialog):
    def __init__(self, database: DatabaseHandler):
        super().__init__()
        self.setWindowTitle("Статистика")
        data = database.get_user_stats()
        self.sentences_label = QLabel(f"Словосочетаний решено: {data[0]}")
        self.symbols_label = QLabel(f"Символов в минуту: {data[1]}")
        self.rate_label = QLabel(f"Процент ошибок: {data[2]}")

        self.statistics_button = QPushButton('ОК')
        self.statistics_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.sentences_label)
        layout.addWidget(self.symbols_label)
        layout.addWidget(self.rate_label)
        layout.addWidget(self.statistics_button)
        self.setModal(True)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setLayout(layout)
