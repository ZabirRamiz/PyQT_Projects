import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow  # Import the generated UI class
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Connect Buttons to Functions
        self.addItemButton.clicked.connect(self.add_item)
        self.editItemButton.clicked.connect(self.edit_item)
        self.deleteItemButton.clicked.connect(self.delete_item)
        self.searchButton.clicked.connect(self.search_item)

        self.addRecordButton.clicked.connect(self.add_record)
        self.editRecordButton.clicked.connect(self.edit_record)
        self.deleteRecordButton.clicked.connect(self.delete_record)

    # Define Functionalities
    def create_database(self):
        query = QSqlQuery()
        query.exec_(
            """
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                part_name TEXT,
                purchase_history TEXT,
                selling_price TEXT,
                part_number TEXT
            )
            """
        )
        query.exec_(
            """
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                FOREIGN KEY (part_name) REFERENCES inventory(part_name),
                date TEXT,
                sales_quantity TEXT,
            )
            """
        )
        query.exec_(
            """
            CREATE TABLE IF NOT EXISTS stock_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                FOREIGN KEY (part_name) REFERENCES inventory(part_name),
                quarter TEXT,
                stock_received TEXT,
                total_stock TEXT
            )
            """
        )

    def load_table(self):
        query.exec_("SELECT * FROM inventory")

        self.table.setColumnCount(5)
        col_headings = ["ID", "Size", "Brand", "Country", "Date", "Purchase", "Stock"]
        self.table.setHorizontalHeaderLabels(col_headings)

    def add_item(self):
        print("Add Item Button Clicked")

    def edit_item(self):
        print("Edit Item Button Clicked")

    def delete_item(self):
        print("Delete Item Button Clicked")

    def search_item(self):
        print("Search Button Clicked")

    def add_record(self):
        print("Add Record Button Clicked")

    def edit_record(self):
        print("Edit Record Button Clicked")

    def delete_record(self):
        print("Delete Record Button Clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
