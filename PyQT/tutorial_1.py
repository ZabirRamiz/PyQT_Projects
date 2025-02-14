# imports
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from random import choice

# main window
app = QApplication([])  # notice empty list
main_window = QWidget()
main_window.setWindowTitle("Tutorial 1: design, handle event")
main_window.resize(900, 700)


# create all app objects (buttons, labels)
title = QLabel("This is the title")

text_1 = QLabel("?")
text_2 = QLabel("?")
text_3 = QLabel("?")

button_1 = QPushButton("Click 1")
button_2 = QPushButton("Click 2")
button_3 = QPushButton("Click 3")

## create design (rows, columns)
# creating row columns
master_column = QVBoxLayout()

row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
row_3 = QHBoxLayout()
# adding elements to row columns
row_1.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)

row_2.addWidget(text_1, alignment=Qt.AlignmentFlag.AlignCenter)
row_2.addWidget(text_2, alignment=Qt.AlignmentFlag.AlignCenter)
row_2.addWidget(text_3, alignment=Qt.AlignmentFlag.AlignCenter)

row_3.addWidget(button_1)
row_3.addWidget(button_2)
row_3.addWidget(button_3)

master_column.addLayout(row_1)
master_column.addLayout(row_2)
master_column.addLayout(row_3)

# Setting the layout of the main window
main_window.setLayout(master_column)

## Functions
my_list = "this is a random word generator".split()


def random_word_1():
    word = choice(my_list)
    text_1.setText(word)


def random_word_2():
    word = choice(my_list)
    text_2.setText(word)


def random_word_3():
    word = choice(my_list)
    text_3.setText(word)


# events
button_1.clicked.connect(random_word_1)
button_2.clicked.connect(random_word_2)
button_3.clicked.connect(random_word_3)

# execution
main_window.show()
app.exec()
