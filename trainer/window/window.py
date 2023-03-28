from PyQt5.QtWidgets import QMainWindow
from trainer.window.gui.widgets import Widget, Line, Button, Label, MenuBar, StatusBar, Menu, Action, Font
from trainer.window.logic.helpers import SentenceGenerator, LineHandler


class Window(QMainWindow):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedSize(722, 361)
        self.setObjectName("MainWindow")
        self._build_user_interface()
        self.generator = SentenceGenerator()
        self.line_handler = LineHandler()

    def _build_user_interface(self):
        self.central_widget = Widget(self, 0, 0, 0, 0)
        self.widget = Widget(self.central_widget, 80, 0, 551, 241)
        font = Font()
        self.line_edit = Line(self.widget, font, 0, 50, 551, 51, True)
        self.line_edit.textChanged.connect(self.on_text_changed)

        self.line_blocked = Line(self.widget, font, 0, 100, 551, 51, True)
        button_style = """QPushButton:hover{background-color: #666666;}
                          QPushButton:!hover {background-color: #cccccc;}"""
        label_style = "border-color: #000000; border-width: 1px; border-button_style: solid;"

        self.start_button = Button(self.widget, "Начать", button_style, 198, 170, 150, 50)
        self.start_button.clicked.connect(self.on_start_click)

        self.minute_symbols = Label(self.widget, "0", label_style, font, 360, 10, 51, 31)
        self.mistake_percents = Label(self.widget, "0%", label_style, font, 450, 10, 81, 31)
        self.setCentralWidget(self.central_widget)
        self.statusbar = StatusBar(self)
        self.setStatusBar(self.statusbar)
        self.menuBar = MenuBar(self, 0, 0, 722, 26)
        self.userMenu = Menu(self.menuBar, "Пользователь")
        self.setMenuBar(self.menuBar)
        self.stat = Action(self, "Статистика")
        self.userMenu.addAction(self.stat)
        self.menuBar.addAction(self.userMenu.menuAction())
        self.show()

    def on_start_click(self):
        self.line_edit.clear()
        sentence = self.generator.get_sentence()
        self.line_blocked.setText(sentence)
        self.line_handler.set_blocked_text(sentence)
        self.line_edit.setReadOnly(False)

    def on_text_changed(self):
        time = self.line_handler.handle(self.line_edit)
        if time:
            print(time)
            self.line_edit.clear()
            self.on_start_click()
