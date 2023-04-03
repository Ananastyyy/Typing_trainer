from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, \
    QPushButton, QVBoxLayout


class LoginDialog(QDialog):
    def __init__(self, database):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.database = database

        self.username_label = QLabel('Логин:')
        self.username_edit = QLineEdit()

        self.login_button = QPushButton('Войти')
        self.login_button.clicked.connect(self.login_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.login_button)
        self.setModal(True)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setLayout(layout)

    def login_clicked(self):
        self.database.authorise(self.username_edit.text())
        self.accept()
