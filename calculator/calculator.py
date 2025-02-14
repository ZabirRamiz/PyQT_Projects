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
from function import Function

## main window
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(300, 500)


## create design


# components
text_box = QLineEdit()

grid = QGridLayout()

clear_button = QPushButton("Clear")
delete_button = QPushButton("<")

# functions
calculator = Function(app, text_box)

calculator.create_buttons(grid, col_limit=3)


# design
master_layout = QVBoxLayout()
button_row = QHBoxLayout()

button_row.addWidget(clear_button)
button_row.addWidget(delete_button)

master_layout.addWidget(text_box)
master_layout.addLayout(grid)
master_layout.addLayout(button_row)

main_window.setLayout(master_layout)

clear_button.clicked.connect(calculator.call_button)
delete_button.clicked.connect(calculator.call_button)
## execution
main_window.show()
app.exec()
