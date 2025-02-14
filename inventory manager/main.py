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
    QInputDialog,
)
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys


## app class
class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        # Main App Objects and Settings
        self.setWindowTitle("Inventory Manager")
        self.resize(850, 500)

        ## create Objects
        # search and filter
        self.search = QLineEdit()

        # add and remove
        self.size = QLineEdit()
        self.datebox = QDateEdit()
        self.stock = QLineEdit()

        self.brand = QComboBox()
        self.load_brand_dropdown()

        self.country = QComboBox()
        self.load_country_dropdown()

        # table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        col_headings = ["ID", "Size", "Brand", "Country", "Date", "Purchase", "Stock"]
        self.table.setHorizontalHeaderLabels(col_headings)

        # buttons
        self.search_button = QPushButton("Search")
        self.add_button = QPushButton("Add Stock")
        self.delete_button = QPushButton("Delete Stock")

        ## styling input box
        # datebox
        self.datebox.setDate(QDate.currentDate())
        self.datebox.setDisplayFormat("dd-MM-yyyy")

        ## styling table
        # hardcoding column widths
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # sorting by date
        self.table.sortByColumn(1, Qt.DescendingOrder)

        ## design app with layouts
        # create layouts
        self.master_layout = QVBoxLayout()
        self.col_1 = QVBoxLayout()
        self.col_row_1 = QHBoxLayout()
        self.row_0 = QHBoxLayout()
        self.row_1 = QHBoxLayout()
        self.row_2 = QHBoxLayout()
        self.row_3 = QHBoxLayout()

        # row_0
        self.row_0.addWidget(self.search)
        self.row_0.addWidget(self.search_button)
        # col_1
        self.col_1.addWidget(QLabel("Size"), 10)
        self.col_row_1.addWidget(self.size, 30)
        self.col_1.addWidget(QLabel("Date"), 10)
        self.col_1.addWidget(self.datebox, 20)
        self.col_1.addWidget(QLabel("Brand"), 10)
        self.col_1.addWidget(self.brand, 20)
        # row_1
        self.row_1.addWidget(self.table, 60)
        self.row_1.addLayout(self.col_1, 40)
        # row_2
        self.row_2.addWidget(QLabel("Stock"), 10)
        self.row_2.addWidget(self.stock, 40)
        self.row_2.addWidget(QLabel("Country"), 10)
        self.row_2.addWidget(self.country, 40)
        # row_3
        self.row_3.addWidget(self.add_button)
        self.row_3.addWidget(self.delete_button)
        # add layouts to master layout
        self.master_layout.addLayout(self.row_0)
        self.master_layout.addLayout(self.col_1)
        self.master_layout.addLayout(self.row_1)
        self.master_layout.addLayout(self.row_2)
        self.master_layout.addLayout(self.row_3)

        # self.master_layout.addWidget(self.table)

        self.setLayout(self.master_layout)

        # connecting methods
        self.load_table()

        self.search_button.clicked.connect(self.search_inventory)
        self.add_button.clicked.connect(self.add_stock)
        self.delete_button.clicked.connect(self.delete_stock)

    def load_table(self, search_query="SELECT * FROM stock"):
        self.table.setRowCount(0)

        query = QSqlQuery(search_query)
        ## efficient
        while query.next():
            row = self.table.rowCount()
            self.table.insertRow(row)
            for i in range(5):
                self.table.setItem(row, i, QTableWidgetItem(str(query.value(i))))

    def load_brand_dropdown(self):
        query = QSqlQuery("SELECT name FROM brand")
        while query.next():
            self.brand.addItem(query.value(0))

        self.brand.addItem("Add New Brand")
        self.brand.activated.connect(self.add_new_brand)
        return

    def load_country_dropdown(self):
        query = QSqlQuery("SELECT name FROM country")
        while query.next():
            self.country.addItem(query.value(0))

        self.country.addItem("Add New Country")
        self.country.activated.connect(self.add_new_country)

    def search_inventory(self):
        search_term = self.search.text()
        if search_term:
            self.load_table(
                "SELECT * FROM expenses WHERE brand = '{}'".format(search_term)
            )

    def add_new_brand(self):
        if self.brand.currentText() == "Add New brand":
            new_brand, ok = QInputDialog.getText(self, "New brand", "Enter New brand")
            if ok:
                query = QSqlQuery()
                query.prepare("INSERT INTO brand (name) VALUES (:name)")
                query.bindValue(":name", new_brand.lower().capitalize())
                query.exec_()

                self.brand.clear()
                self.load_brand_dropdown()

            else:
                return

    def add_new_country(self):
        if self.country.currentText() == "Add New Country":
            new_country, ok = QInputDialog.getText(
                self, "New Country", "Enter New Country"
            )
            if ok:
                query = QSqlQuery()
                query.prepare("INSERT INTO country (name) VALUES (:name)")
                query.bindValue(":name", new_country.lower().capitalize())
                query.exec_()

                self.country.clear()
                self.load_country_dropdown()

            else:
                return

    def add_stock(self):
        date = self.datebox.date().toString("yyyy-MM-dd")
        brand = self.brand.currentText()
        stock = self.stock.text()
        country = self.country.text()

        if date and brand and stock and country:
            query = QSqlQuery()
            query.prepare(
                """
                INSERT INTO stock (date, brand, stock, country)
                VALUES (:date, :brand, :stock, :country)
                """
            )
            query.bindValue(":date", date)
            query.bindValue(":brand", brand)
            query.bindValue(":stock", stock)
            query.bindValue(":country", country)
            query.exec_()

            self.datebox.setDate(QDate.currentDate())
            self.brand.setCurrentIndex(0)
            self.stock.clear()
            self.country.clear()

            self.load_table()
        else:
            QMessageBox.warning(self, "Error", "All fields must be filled")

    def delete_stock(self):
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
        query.prepare("DELETE FROM stock WHERE id = :id")
        query.bindValue(":id", expense_id)
        query.exec_()

        self.load_table()


## create Database
database = QSqlDatabase.addDatabase("QSQLITE")
database.setDatabaseName("stock.db")
if not database.open():
    QMessageBox.critical(
        None,
        "Error",
        "Database Connection Error: {}".format(database.lastError().text()),
    )
    sys.exit(1)

# creating inventory table
query = QSqlQuery()
query.exec_(
    """
    CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        size TEXT,
        brand TEXT,
        country TEXT
        date TEXT,
        purchase TEXT,
        stock TEXT
    )
    """
)
# creating brand table
query.exec_(
    """
    CREATE TABLE IF NOT EXISTS brand (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name TEXT 
    )
    """
)
# creating country table
query.exec_(
    """
    CREATE TABLE IF NOT EXISTS country (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name TEXT 
    )
    """
)

## Run APP
if __name__ == "__main__":
    app = QApplication([])
    main_app = ExpenseApp()
    main_app.show()
    app.exec()
