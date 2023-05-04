from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout)

from config.conf_parser import ConfParser
from trainer.window.logic.database_handler import DatabaseHandler


class LoginDialog(QDialog):
    def __init__(self, database: DatabaseHandler) -> None:
        super().__init__()
        self._init_config_file()
        self._build_window()
        self.database = database
        self.setModal(True)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)

    def _build_window(self) -> None:
        self.setWindowTitle(self.constants["window_title"])
        self.username_label = QLabel(self.constants["login"])
        self.username_edit = QLineEdit()

        self.login_button = QPushButton(self.constants["log_on"])
        self.login_button.clicked.connect(self.login_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def _init_config_file(self) -> None:
        config = ConfParser()
        self.constants = config.login_dialog

    def login_clicked(self) -> None:
        self.database.authorise(self.username_edit.text())
        self.accept()
