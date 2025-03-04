import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_main import Ui_MainWindow


class InventoryApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.conn = sqlite3.connect("inventory.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        self.load_table()
        self.load_brandDropdown()
        self.load_countryDropdown()

        self.addButton.clicked.connect(self.add_record)
        self.editButton.clicked.connect(self.edit_record)
        self.deleteButton.clicked.connect(self.delete_record)
        self.searchButton.clicked.connect(self.search_records)

        self.filterCheckBox.stateChanged.connect(self.toggle_filter)
        self.filterDropdown.currentTextChanged.connect(self.load_filter_elements)
        self.filterElementDropdown.currentTextChanged.connect(self.apply_filter)

    def create_table(self):
        try:
            # self.cursor.execute("DROP TABLE IF EXISTS brand")
            # self.cursor.execute("DROP TABLE IF EXISTS country")
            # self.cursor.execute("DROP TABLE IF EXISTS inventory")
            # inventory table
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS inventory (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    size TEXT,
                                    brand TEXT,
                                    country TEXT,
                                    date TEXT,
                                    stock INTEGER)"""
            )
            # brand table
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS brand (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                ) 
                """
            )

            # country table
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS country (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                ) 
                """
            )

            self.conn.commit()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to create tables: {e}"
            )

    def load_table(self):
        try:
            self.cursor.execute(
                "SELECT id, size, brand, country, date, stock FROM inventory"
            )
            rows = self.cursor.fetchall()
            self.table.setRowCount(len(rows))
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data):
                    self.table.setItem(
                        row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data))
                    )
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to load table data: {e}"
            )

    def load_brandDropdown(self):
        try:
            self.brandDropdown.clear()  # Clear existing items
            self.cursor.execute("SELECT name FROM brand ORDER BY name ASC")
            rows = self.cursor.fetchall()
            for row in rows:
                self.brandDropdown.addItem(
                    row[0]
                )  # Add each brand name to the dropdown
            self.brandDropdown.addItem("Add New Brand ...")
            self.brandDropdown.activated.connect(self.add_newBrand)

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to load brandDropdown data: {e}"
            )

    def load_countryDropdown(self):
        try:
            self.countryDropdown.clear()  # Clear existing items
            self.cursor.execute("SELECT name FROM country ORDER BY name ASC")
            rows = self.cursor.fetchall()
            for row in rows:
                self.countryDropdown.addItem(
                    row[0]
                )  # Add each country name to the dropdown
            self.countryDropdown.addItem("Add New Country ...")
            self.countryDropdown.activated.connect(self.add_newCountry)
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to load countryDropdown data: {e}"
            )

    def edit_record(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            QtWidgets.QMessageBox.warning(
                self, "Selection Error", "Please select a record to edit."
            )
            return

        record_id = self.table.item(current_row, 0).text()
        old_size = self.table.item(current_row, 1).text()
        old_brand = self.table.item(current_row, 2).text()
        old_country = self.table.item(current_row, 3).text()
        old_date = self.table.item(current_row, 4).text()
        old_stock = self.table.item(current_row, 5).text()

        size = self.sizeEdit.text()
        brand = self.brandDropdown.currentText()
        country = self.countryDropdown.currentText()
        date = self.dateEdit.text()
        stock = self.stockEdit.text()

        size = size if size else old_size
        brand = brand if brand else old_brand
        country = country if country else old_country
        date = date if date else old_date
        stock = stock if stock else old_stock

        try:
            self.cursor.execute(
                "UPDATE inventory SET size=?, brand=?, country=?, date=?, stock=? WHERE id=?",
                (size, brand, country, date, stock, record_id),
            )
            self.conn.commit()
            self.load_table()
            QtWidgets.QMessageBox.information(
                self, "Success", "Record updated successfully."
            )

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to update record: {e}"
            )

    def search_records(self):
        search_text = self.searchEdit.text()
        query = "SELECT id, size, brand, country, date, stock FROM inventory WHERE size LIKE ? OR brand LIKE ? OR country LIKE ?"
        params = (f"%{search_text}%", f"%{search_text}%", f"%{search_text}%")

        try:
            self.cursor.execute(query, params)
            records = self.cursor.fetchall()
            self.table.setRowCount(len(records))
            for row_idx, row_data in enumerate(records):
                for col_idx, col_data in enumerate(row_data):
                    self.table.setItem(
                        row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data))
                    )
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to search records: {e}"
            )

    def add_record(self):
        size = self.sizeEdit.text()
        brand = self.brandDropdown.currentText()
        country = self.countryDropdown.currentText()
        date = self.dateEdit.text()
        stock = self.stockEdit.text()
        try:
            self.cursor.execute(
                "INSERT INTO inventory (size, brand, country, date, stock) VALUES (?, ?, ?, ?, ?)",
                (size, brand, country, date, stock),
            )
            self.conn.commit()
            self.load_table()
            QtWidgets.QMessageBox.information(
                self, "Success", "Record added successfully."
            )
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to add record: {e}"
            )

    def delete_record(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            QtWidgets.QMessageBox.warning(
                self, "Selection Error", "Please select a record to delete."
            )
            return

        record_id = self.table.item(current_row, 0).text()

        confirm = QtWidgets.QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete this record?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No,
        )
        if confirm == QtWidgets.QMessageBox.Yes:
            try:
                self.cursor.execute("DELETE FROM inventory WHERE id=?", (record_id,))
                self.conn.commit()
                self.load_table()
                QtWidgets.QMessageBox.information(
                    self, "Success", "Record deleted successfully."
                )
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(
                    self, "Database Error", f"Failed to delete record: {e}"
                )

    def toggle_filter(self, state):
        if state:
            self.load_filter_elements()
        else:
            # Clear the filter dropdown without reloading the table
            self.filterElementDropdown.clear()
            self.load_table()
        self.filterDropdown.setEnabled(state)
        self.filterElementDropdown.setEnabled(state)

    def load_filter_elements(self):
        filter_type = self.filterDropdown.currentText().lower()
        try:
            if self.filterCheckBox.isChecked():
                if filter_type == "year":
                    query = "SELECT DISTINCT substr(date, 7, 4) AS year FROM inventory"

                else:
                    query = f"SELECT DISTINCT {filter_type} FROM inventory"
                self.cursor.execute(query)
                elements = [row[0] for row in self.cursor.fetchall()]
                print(elements)

                self.filterElementDropdown.clear()
                self.filterElementDropdown.addItems(elements)
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to load filter elements: {e}"
            )

    def apply_filter(self):
        filter_value = self.filterElementDropdown.currentText()
        try:
            if self.filterCheckBox.isChecked():
                filter_type = self.filterDropdown.currentText().lower()
                if filter_type == "year":
                    query = """
                            SELECT id, size, brand, country, date, stock
                            FROM inventory
                            WHERE substr(date, 7, 4) = ?
                        """
                else:
                    query = f"SELECT id, size, brand, country, date, stock FROM inventory WHERE {filter_type} = ?"
                self.cursor.execute(query, (filter_value,))
                rows = self.cursor.fetchall()
                self.table.setRowCount(len(rows))
                for row_idx, row_data in enumerate(rows):
                    for col_idx, col_data in enumerate(row_data):
                        self.table.setItem(
                            row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data))
                        )
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to apply filter: {e}"
            )

    def add_newBrand(self):
        if self.brandDropdown.currentText() == "Add New Brand ...":
            new_brand, ok = QtWidgets.QInputDialog.getText(
                self, "New Brand", "Enter New Brand"
            )
            if ok and new_brand:  # Ensure that the input is not empty
                try:
                    self.cursor.execute(
                        "INSERT INTO brand (name) VALUES (?)",
                        (new_brand.lower().capitalize(),),
                    )
                    self.conn.commit()
                    self.load_brandDropdown()  # Reload to include the new brand
                    QtWidgets.QMessageBox.information(
                        self, "Success", "Brand Added Successfully."
                    )
                except sqlite3.IntegrityError:
                    QtWidgets.QMessageBox.warning(
                        self, "Error", "This brand already exists."
                    )
                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.critical(
                        self, "Database Error", f"Failed to add brand: {e}"
                    )

    def add_newCountry(self):
        if self.countryDropdown.currentText() == "Add New Country ...":
            new_country, ok = QtWidgets.QInputDialog.getText(
                self, "New Country", "Enter New Country"
            )
            if ok and new_country:  # Ensure that the input is not empty
                try:
                    self.cursor.execute(
                        "INSERT INTO country (name) VALUES (?)",
                        (new_country.lower().capitalize(),),
                    )
                    self.conn.commit()
                    self.load_countryDropdown()  # Reload to include the new country
                    QtWidgets.QMessageBox.information(
                        self, "Success", "Country Added Successfully."
                    )
                except sqlite3.IntegrityError:
                    QtWidgets.QMessageBox.warning(
                        self, "Error", "This country already exists."
                    )
                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.critical(
                        self, "Database Error", f"Failed to add country: {e}"
                    )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = InventoryApp()
    mainWin.show()
    sys.exit(app.exec_())
