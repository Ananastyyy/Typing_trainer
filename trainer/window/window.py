from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QFrame

from trainer.window.gui.dialogs.login_dialog import LoginDialog
from trainer.window.gui.dialogs.statistics_dialog import StatisticsDialog
from trainer.window.gui.widgets.action import Action
from trainer.window.gui.widgets.button import Button
from trainer.window.gui.widgets.font import Font
from trainer.window.gui.widgets.keyboard import Keyboard
from trainer.window.gui.widgets.label import Label
from trainer.window.gui.widgets.line import Line
from trainer.window.gui.widgets.menu import Menu
from trainer.window.gui.widgets.menu_bar import MenuBar
from trainer.window.gui.widgets.status_bar import StatusBar
from trainer.window.gui.widgets.widget import Widget
from trainer.window.logic.database_handler import DatabaseHandler
from trainer.window.logic.sentence_generator import SentenceGenerator
from trainer.window.logic.line_handler import LineHandler


class Window(QMainWindow):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setWindowTitle(
            "QuickType Pro: Practice to Speed Up Your Fingers!")
        self.setFixedSize(700, 590)
        self.setStyleSheet("background-color: lightblue")
        self.setObjectName("MainWindow")
        self._build_user_interface()
        self.generator = SentenceGenerator()
        self.line_handler = LineHandler()
        self.database = DatabaseHandler("database/users.json")

    def _build_user_interface(self):
        self.central_widget = Widget(self, 0, 0, 0, 0)
        self.widget = Widget(self.central_widget, 57, 0, 593, 241)
        font = Font()
        self.line_edit = Line(self.widget, font, 0, 50, 593, 51, True)
        self.line_edit.textChanged.connect(self.on_text_changed)

        self.keyboardFrame = QFrame(self.central_widget)
        self.keyboardFrame.setGeometry(QRect(57, 260, 761, 311))

        self.keyboard = Keyboard(self.keyboardFrame, font)

        self.line_blocked = Line(self.widget, font, 0, 100, 593, 51, True)
        button_style = """QPushButton:hover{background-color: #666666;}
                          QPushButton:!hover {background-color: #cccccc;}"""
        label_style = "border-color: #000000; " \
                      "border-width: 1px; border-button_style: solid;"

        self.start_button = Button(self.widget, "Сгенерировать пример",
                                   button_style, 221, 180, 150, 50)
        self.start_button.clicked.connect(self.on_start_click)

        self.emoji_time = Label(self.widget, "⏰",
                                label_style, font, 328, 10, 31, 31)
        self.emoji_time.setToolTip('Скорость')

        self.minute_symbols = Label(self.widget, "0",
                                    label_style, font, 360, 10, 51, 31)

        self.emoji_mistake = Label(self.widget, "❌",
                                   label_style, font, 418, 10, 31, 31)
        self.emoji_mistake.setToolTip('Количество ошибок')
        self.mistake_percents = Label(self.widget, "0",
                                      label_style, font, 450, 10, 81, 31)

        self.setCentralWidget(self.central_widget)
        self.statusbar = StatusBar(self)
        self.setStatusBar(self.statusbar)
        self.menuBar = MenuBar(self, 0, 0, 722, 26)
        menu_style = """
        QMenuBar {
            background-color: blue;
            color: white;
        }

        QMenuBar::item {
            background-color: blue;
            color: white;
        }

        QMenuBar::item:selected {
            background-color: white;
            color: black;
        }
        QMenu {
            background-color: blue;
            color: white;
        }

        QMenu::item {
            background-color: blue;
            color: white;
        }

        QMenu::item:selected {
            background-color: white;
            color: black;
        }
        """
        self.menuBar.setStyleSheet(menu_style)
        self.userMenu = Menu(self.menuBar, "Пользователь")
        self.setMenuBar(self.menuBar)
        self.auth = Action(self, "Авторизация")
        self.auth.triggered.connect(self.show_login_dialog)
        self.stat = Action(self, "Статистика")
        self.stat.triggered.connect(self.show_statistics_dialog)
        self.userMenu.addAction(self.auth)
        self.userMenu.addAction(self.stat)
        self.menuBar.addAction(self.userMenu.menuAction())
        self.show()

    def on_start_click(self):
        self.line_edit.clear()
        sentence = self.generator.get_sentence()
        self.line_blocked.setText(sentence)
        self.line_handler.set_blocked_text(sentence)
        self.line_edit.setReadOnly(False)
        self.keyboard.select_button(str(sentence[0]))

    def on_text_changed(self):
        data = self.line_handler.handle(self.line_edit, self.keyboard)
        if data:
            symbols = data[0]
            count = data[1]
            self.minute_symbols.setText(f"{symbols}")
            self.mistake_percents.setText(f"{count}")
            self.database.update_user_stats(1, symbols, count)
            self.line_edit.clear()
            self.on_start_click()

    def show_login_dialog(self):
        login_dialog = LoginDialog(self.database)
        login_dialog.exec_()

    def show_statistics_dialog(self):
        data = self.database.get_user_stats()
        if data:
            stat_dialog = StatisticsDialog(data)
            stat_dialog.exec_()
