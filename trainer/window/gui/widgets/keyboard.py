from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame

from trainer.window.gui.widgets.keyboardButton import KeyboardButton
from trainer.window.gui.widgets.line import Line


class Keyboard:
    def __init__(self, window: QFrame, font: QFont):
        self.hands = {"left": "левая рука",
                      "right": "правая рука",
                      "anyone": "любая рука"}
        self.fingers = {"thumb": "большой палец",
                        "index": "указательный палец",
                        "middle": "указательный палец",
                        "ring": "безымянный палец",
                        "pink": "мизинец"}
        self.active_button = None
        self._add_buttons(window, font)
        self.name_fingers = Line(window, font, 92, 220, 410, 40, True)
        self.name_fingers.setAlignment(Qt.AlignCenter)

    def _add_buttons(self, window: QFrame, font: QFont):
        self.buttons = {
            "Ё": KeyboardButton("Ё", window, font, 0, 0, 40, 40, True,
                                self.hands["left"], self.fingers["pink"]),
            "1": KeyboardButton("1", window, font, 41, 0, 40, 40, True,
                                self.hands["left"], self.fingers["ring"]),
            "2": KeyboardButton("2", window, font, 82, 0, 40, 40, True,
                                self.hands["left"], self.fingers["ring"]),
            "3": KeyboardButton("3", window, font, 123, 0, 40, 40, True,
                                self.hands["left"], self.fingers["middle"]),
            "4": KeyboardButton("4", window, font, 164, 0, 40, 40, True,
                                self.hands["left"], self.fingers["middle"]),
            "5": KeyboardButton("5", window, font, 205, 0, 40, 40, True,
                                self.hands["left"], self.fingers["index"]),
            "6": KeyboardButton("6", window, font, 246, 0, 40, 40, True,
                                self.hands["left"], self.fingers["index"]),
            "7": KeyboardButton("7", window, font, 287, 0, 40, 40, True,
                                self.hands["right"], self.fingers["index"]),
            "8": KeyboardButton("8", window, font, 328, 0, 40, 40, True,
                                self.hands["right"], self.fingers["middle"]),
            "9": KeyboardButton("9", window, font, 369, 0, 40, 40, True,
                                self.hands["right"], self.fingers["middle"]),
            "0": KeyboardButton("0", window, font, 410, 0, 40, 40, True,
                                self.hands["right"], self.fingers["ring"]),
            "-": KeyboardButton("-", window, font, 451, 0, 40, 40, True,
                                self.hands["right"], self.fingers["pink"]),
            "=": KeyboardButton("=", window, font, 492, 0, 40, 40, True,
                                self.hands["right"], self.fingers["pink"]),
            "BACKSPACE": KeyboardButton("Bs", window, font, 533, 0, 60,
                                        40, True, self.hands["right"],
                                        self.fingers["pink"]),

            "TAB": KeyboardButton("Tab", window, font, 0, 41, 60, 40, True,
                                  self.hands["left"], self.fingers["pink"]),
            "Й": KeyboardButton("Й", window, font, 61, 41, 40, 40, True,
                                self.hands["left"], self.fingers["pink"]),
            "Ц": KeyboardButton("Ц", window, font, 102, 41, 40, 40, True,
                                self.hands["left"], self.fingers["ring"]),
            "У": KeyboardButton("У", window, font, 143, 41, 40, 40, True,
                                self.hands["left"], self.fingers["middle"]),
            "К": KeyboardButton("К", window, font, 184, 41, 40, 40, True,
                                self.hands["left"], self.fingers["index"]),
            "Е": KeyboardButton("Е", window, font, 225, 41, 40, 40, True,
                                self.hands["left"], self.fingers["index"]),
            "Н": KeyboardButton("Н", window, font, 266, 41, 40, 40, True,
                                self.hands["right"], self.fingers["index"]),
            "Г": KeyboardButton("Г", window, font, 307, 41, 40, 40, True,
                                self.hands["right"], self.fingers["index"]),
            "Ш": KeyboardButton("Ш", window, font, 348, 41, 40, 40, True,
                                self.hands["right"], self.fingers["middle"]),
            "Щ": KeyboardButton("Щ", window, font, 389, 41, 40, 40, True,
                                self.hands["right"], self.fingers["ring"]),
            "З": KeyboardButton("З", window, font, 430, 41, 40, 40, True,
                                self.hands["right"], self.fingers["pink"]),
            "Х": KeyboardButton("Х", window, font, 471, 41, 40, 40, True,
                                self.hands["right"], self.fingers["pink"]),
            "Ъ": KeyboardButton("Ъ", window, font, 512, 41, 40, 40, True,
                                self.hands["right"], self.fingers["pink"]),
            "\\": KeyboardButton("\\", window, font, 553, 41, 40, 40, True,
                                 self.hands["right"], self.fingers["pink"]),

            "CL": KeyboardButton("CL", window, font, 0, 82, 70, 40, True,
                                 self.hands["left"], self.fingers["pink"]),
            "Ф": KeyboardButton("Ф", window, font, 71, 82, 40, 40, True,
                                self.hands["left"], self.fingers["pink"]),
            "Ы": KeyboardButton("Ы", window, font, 112, 82, 40, 40, True,
                                self.hands["left"], self.fingers["ring"]),
            "В": KeyboardButton("В", window, font, 153, 82, 40, 40, True,
                                self.hands["left"], self.fingers["middle"]),
            "А": KeyboardButton("А", window, font, 194, 82, 40, 40, True,
                                self.hands["left"], self.fingers["index"]),
            "П": KeyboardButton("П", window, font, 235, 82, 40, 40, True,
                                self.hands["left"], self.fingers["index"]),
            "Р": KeyboardButton("Р", window, font, 276, 82, 40, 40, True,
                                self.hands["right"], self.fingers["index"]),
            "О": KeyboardButton("О", window, font, 317, 82, 40, 40, True,
                                self.hands["right"], self.fingers["index"]),
            "Л": KeyboardButton("Л", window, font, 358, 82, 40, 40, True,
                                self.hands["right"], self.fingers["middle"]),
            "Д": KeyboardButton("Д", window, font, 399, 82, 40, 40, True,
                                self.hands["right"], self.fingers["ring"]),
            "Ж": KeyboardButton("Ж", window, font, 440, 82, 40, 40, True,
                                self.hands["right"], self.fingers["pink"]),
            "Э": KeyboardButton("Э", window, font, 481, 82, 40, 40, True,
                                self.hands["right"], self.fingers["pink"]),
            "ENTER": KeyboardButton("Enter", window, font, 522, 82, 71, 40,
                                    True, self.hands["right"],
                                    self.fingers["pink"]),

            "SHIFT1": KeyboardButton("Shift1", window, font, 0, 123, 91, 40,
                                     True, self.hands["left"],
                                     self.fingers["pink"]),
            "Я": KeyboardButton("Я", window, font, 92, 123, 40, 40, True,
                                self.hands["left"], self.fingers["ring"]),
            "Ч": KeyboardButton("Ч", window, font, 133, 123, 40, 40, True,
                                self.hands["left"], self.fingers["middle"]),
            "С": KeyboardButton("С", window, font, 174, 123, 40, 40, True,
                                self.hands["left"], self.fingers["index"]),
            "М": KeyboardButton("М", window, font, 215, 123, 40, 40, True,
                                self.hands["left"], self.fingers["index"]),
            "И": KeyboardButton("И", window, font, 256, 123, 40, 40, True,
                                self.hands["left"], self.fingers["index"]),
            "Т": KeyboardButton("Т", window, font, 297, 123, 40, 40, True,
                                self.hands["right"], self.fingers["index"]),
            "Ь": KeyboardButton("Ь", window, font, 338, 123, 40, 40, True,
                                self.hands["right"], self.fingers["index"]),
            "Б": KeyboardButton("Б", window, font, 379, 123, 40, 40, True,
                                self.hands["right"], self.fingers["middle"]),
            "Ю": KeyboardButton("Ю", window, font, 420, 123, 40, 40, True,
                                self.hands["right"], self.fingers["ring"]),
            ".": KeyboardButton(".", window, font, 461, 123, 40, 40, True,
                                self.hands["right"], self.fingers["pink"]),
            "SHIFT2": KeyboardButton("Shift2", window, font, 502, 123, 91, 40,
                                     True, self.hands["right"],
                                     self.fingers["pink"]),
            " ": KeyboardButton("Space", window, font, 153, 164, 287, 40,
                                True, self.hands["anyone"], self.fingers[
                                    "thumb"]),

        }

    def select_button(self, letter: str):
        self._deselect_button()
        self.active_button = self.buttons[letter.upper()]
        self.active_button.setStyleSheet("background-color: lightgreen")
        self.name_fingers.setText(f"{self.active_button.name_hand}, "
                                  f"{self.active_button.name_fingers}")

    def _deselect_button(self):
        if self.active_button:
            self.active_button.setStyleSheet("background-color: white")
            self.active_button = None
            self.name_fingers.setText("")
