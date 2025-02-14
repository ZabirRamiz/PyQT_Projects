## import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
)


class Function:
    def __init__(self, app, text_box):
        self.app = app
        self.text_box = text_box

    def call_button(self):
        button = self.app.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))

            except Exception as e:
                message = "Error" + str(e)
                self.text_box.setText(message)

        elif text == "Clear":
            self.text_box.clear()

        elif text == "<":
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])

        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)

    def create_buttons(self, grid, col_limit):
        calc_buttons = "7 8 9 / 4 5 6 * 1 2 3 - 0 . = +".split()
        row = 0
        col = 0

        for i in calc_buttons:
            button = QPushButton(i)
            button.clicked.connect(self.call_button)
            grid.addWidget(button, row, col)

            col += 1

            if col > col_limit:
                row += 1
                col = 0
