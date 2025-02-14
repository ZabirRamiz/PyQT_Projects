## import modules
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys


## app class
class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        # Main App Objects and Settings
        self.setWindowTitle("Expense Tracker")
        self.resize(550, 500)

        # create Objects
        self.datebox = QDateEdit()

        self.dropdown = QComboBox()
        dropdown_values = ["Food", "Transport", "Rent", "Entertainment", "Other"]
        self.dropdown.addItems(dropdown_values)

        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.add_button = QPushButton("Add Expense")
        self.delete_button = QPushButton("Delete Expense")

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        col_headings = ["ID", "Date", "Category", "Amount", "Description"]
        self.table.setHorizontalHeaderLabels(col_headings)

        ## styling input box
        # datebox
        self.datebox.setDate(QDate.currentDate())
        self.datebox.setDisplayFormat("dd-MM-yyyy")

        ## styling table
        # harcoding column widths
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # sorting by date
        self.table.sortByColumn(1, Qt.DescendingOrder)

        # design app with layouts
        self.master_layout = QVBoxLayout()
        self.row_1 = QHBoxLayout()
        self.row_2 = QHBoxLayout()
        self.row_3 = QHBoxLayout()

        self.row_1.addWidget(QLabel("Date"), 10)
        self.row_1.addWidget(self.datebox, 40)
        self.row_1.addWidget(QLabel("Category"), 10)
        self.row_1.addWidget(self.dropdown, 40)

        self.row_2.addWidget(QLabel("Amount"), 10)
        self.row_2.addWidget(self.amount, 40)
        self.row_2.addWidget(QLabel("Description"), 10)
        self.row_2.addWidget(self.description, 40)

        self.row_3.addWidget(self.add_button)
        self.row_3.addWidget(self.delete_button)

        self.master_layout.addWidget(self.table)

        self.master_layout.addLayout(self.row_1)
        self.master_layout.addLayout(self.row_2)
        self.master_layout.addLayout(self.row_3)

        self.setLayout(self.master_layout)

        # connecting methods
        self.load_table()
        self.add_button.clicked.connect(self.add_expense)
        self.delete_button.clicked.connect(self.delete_expense)

    def load_table(self):
        self.table.setRowCount(0)

        query = QSqlQuery("SELECT * FROM expenses")
        ## efficient
        # while query.next():
        #     row = self.table.rowCount()
        #     self.table.insertRow(row)
        #     for i in range(5):
        #         self.table.setItem(row, i, QTableWidgetItem(str(query.value(i))))

        ## basic
        row = 0
        while query.next():
            expense_id = query.value(0)
            date = query.value(1)
            category = query.value(2)
            amount = query.value(3)
            description = query.value(4)

            # add values to the table
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(expense_id)))
            self.table.setItem(row, 1, QTableWidgetItem(date))
            self.table.setItem(row, 2, QTableWidgetItem(category))
            self.table.setItem(row, 3, QTableWidgetItem(str(amount)))
            self.table.setItem(row, 4, QTableWidgetItem(description))

            row += 1

    def add_expense(self):
        date = self.datebox.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        if date and category and amount:
            query = QSqlQuery()
            query.prepare(
                """
                INSERT INTO expenses (date, category, amount, description)
                VALUES (:date, :category, :amount, :description)
                """
            )
            query.bindValue(":date", date)
            query.bindValue(":category", category)
            query.bindValue(":amount", amount)
            query.bindValue(":description", description)
            query.exec_()

            self.datebox.setDate(QDate.currentDate())
            self.dropdown.setCurrentIndex(0)
            self.amount.clear()
            self.description.clear()

            self.load_table()

    def delete_expense(self):
        selected_row = self.table.currentRow()
        if selected_row is None:
            QMessageBox.warning(self, "Error", "Select a row to delete")

        expense_id = int(self.table.item(selected_row, 0).text())

        confirm = QMessageBox.question(
            self,
            "Delete",
            "Are you sure you want to delete this expense?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if confirm == QMessageBox.No:
            return

        query = QSqlQuery()
        query.prepare("DELETE FROM expenses WHERE id = :id")
        query.bindValue(":id", expense_id)
        query.exec_()

        self.load_table()


## create Database
database = QSqlDatabase.addDatabase("QSQLITE")
database.setDatabaseName("expenses.db")
if not database.open():
    QMessageBox.critical(
        None,
        "Error",
        "Database Connection Error: {}".format(database.lastError().text()),
    )
    sys.exit(1)

query = QSqlQuery()
query.exec_(
    """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT
    )
    """
)

## Run APP
if __name__ == "__main__":
    app = QApplication([])
    main_app = ExpenseApp()
    main_app.show()
    app.exec()
