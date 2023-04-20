import configparser

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
from trainer.window.gui.widgets.widget import Widget
from trainer.window.logic.database_handler import DatabaseHandler
from trainer.window.logic.sentence_generator import SentenceGenerator
from trainer.window.logic.line_handler import LineHandler


class Window(QMainWindow):
    def __init__(self, *__args):
        super().__init__(*__args)
        self._init_config_file()
        self._build_main_window()
        self._build_user_interface()
        self.generator = SentenceGenerator()
        self.line_handler = LineHandler()
        self.database = DatabaseHandler(self.constants["path_to_database"])

    def _init_config_file(self):
        config = configparser.ConfigParser()
        config.read("config/window.ini", encoding='utf-8')
        self.constants = dict(config.items("WINDOW"))

    def _build_main_window(self):
        self.setWindowTitle(self.constants["window_title"])
        self.setFixedSize(700, 590)
        self.setStyleSheet(self.constants["background_window"])
        self.central_widget = Widget(self, 0, 0, 0, 0)
        self.setCentralWidget(self.central_widget)
        self.widget = Widget(self.central_widget, 57, 0, 593, 241)
        self.font = Font()

    def _build_user_interface(self):
        self._build_line()
        self._build_keyboard()
        self._build_button()
        self._build_label()
        self.show()

    def _build_line(self):
        self.line_edit = Line(self.widget, self.font, 0, 50, 593, 51, True)
        self.line_edit.textChanged.connect(self.on_text_changed)

        self.line_blocked = Line(self.widget, self.font, 0, 100, 593, 51, True)

    def _build_keyboard(self):
        self.keyboardFrame = QFrame(self.central_widget)
        self.keyboardFrame.setGeometry(QRect(57, 260, 761, 311))

        self.keyboard = Keyboard(self.keyboardFrame, self.font)

    def _build_button(self):
        button_style = self.constants["button_style"]
        self.start_button = Button(self.widget, self.constants[
            "generate_sentences"], button_style, 221, 180, 150, 50)
        self.start_button.clicked.connect(self.on_start_click)

    def _build_label(self):
        label_style = self.constants["label_style"]
        self.emoji_time = Label(self.widget, self.constants["emoji_time"],
                                label_style, self.font, 328, 10, 31, 31)
        self.emoji_time.setToolTip(self.constants["description_timer"])

        self.minute_symbols = Label(self.widget, self.constants["start_time"],
                                    label_style, self.font, 360, 10, 51, 31)

        self.emoji_mistake = Label(self.widget, self.constants["emoji_fail"],
                                   label_style, self.font, 418, 10, 31, 31)
        self.emoji_mistake.setToolTip(self.constants["description_error"])
        self.mistake_percents = Label(self.widget,
                                      self.constants["start_error"],
                                      label_style, self.font, 450, 10, 81, 31)

    def _build_menu_bar(self):
        self.menuBar = MenuBar(self, 0, 0, 722, 26)
        menu_style = self.constants["menu_bar_style"]
        self.menuBar.setStyleSheet(menu_style)
        self.userMenu = Menu(self.menuBar, self.constants["user_menu"])
        self.setMenuBar(self.menuBar)
        self.auth = Action(self, self.constants["action_auth"])
        self.auth.triggered.connect(self.show_login_dialog)
        self.stat = Action(self, self.constants["action_stat"])
        self.stat.triggered.connect(self.show_statistics_dialog)
        self.userMenu.addAction(self.auth)
        self.userMenu.addAction(self.stat)
        self.menuBar.addAction(self.userMenu.menuAction())

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
