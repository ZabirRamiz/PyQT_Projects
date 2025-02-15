import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_main import Ui_MainWindow


class InventoryApp(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Main class for the inventory management application.

    This class is responsible for the main window UI and handling the inventory-related
    CRUD operations (Create, Read, Update, Delete) using a SQLite database.
    """

    def __init__(self):
        """
        Initializes the inventory application, sets up UI components,
        establishes a database connection, and loads required data into dropdowns and table.

        Connects UI elements to their corresponding functions for adding, editing, deleting,
        and searching inventory records.
        """
        super().__init__()
        self.setupUi(self)
        self.conn = sqlite3.connect("inventory.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        self.load_table()
        self.load_brandDropdown()
        self.load_countryDropdown()

        # Connecting button click events to their respective methods
        self.addButton.clicked.connect(self.add_record)
        self.editButton.clicked.connect(self.edit_record)
        self.deleteButton.clicked.connect(self.delete_record)
        self.searchButton.clicked.connect(self.search_records)

        # Connecting filter UI events
        self.filterCheckBox.stateChanged.connect(self.toggle_filter)
        self.filterDropdown.currentTextChanged.connect(self.load_filter_elements)
        self.filterElementDropdown.currentTextChanged.connect(self.apply_filter)

    def create_table(self):
        """
        Creates necessary tables in the database if they do not exist.

        Creates `inventory`, `brand`, and `country` tables in the SQLite database.
        """
        try:
            # Uncomment these lines if you need to drop tables for testing
            # self.cursor.execute("DROP TABLE IF EXISTS brand")
            # self.cursor.execute("DROP TABLE IF EXISTS country")
            # self.cursor.execute("DROP TABLE IF EXISTS inventory")

            # Create the inventory table
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS inventory (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    size TEXT,
                                    brand TEXT,
                                    country TEXT,
                                    date TEXT,
                                    stock INTEGER)"""
            )
            # Create the brand table
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS brand (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                ) 
                """
            )

            # Create the country table
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
        """
        Loads inventory records from the database and displays them in the table.

        Fetches all records from the inventory table and displays them in the `QTableWidget`.
        """
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
        """
        Loads available brands from the database and populates the brand dropdown.

        Fetches all brands from the brand table and adds them to the brand dropdown (`brandDropdown`).
        """
        try:
            self.brandDropdown.clear()  # Clear existing items
            self.cursor.execute("SELECT name FROM brand ORDER BY name ASC")
            rows = self.cursor.fetchall()
            for row in rows:
                self.brandDropdown.addItem(
                    row[0]
                )  # Add each brand name to the dropdown
            self.brandDropdown.addItem(
                "Add New Brand ..."
            )  # Add option to add new brand
            self.brandDropdown.activated.connect(
                self.add_newBrand
            )  # Connect the "Add New Brand" action

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to load brandDropdown data: {e}"
            )

    def load_countryDropdown(self):
        """
        Loads available countries from the database and populates the country dropdown.

        Fetches all countries from the country table and adds them to the country dropdown (`countryDropdown`).
        """
        try:
            self.countryDropdown.clear()  # Clear existing items
            self.cursor.execute("SELECT name FROM country ORDER BY name ASC")
            rows = self.cursor.fetchall()
            for row in rows:
                self.countryDropdown.addItem(
                    row[0]
                )  # Add each country name to the dropdown
            self.countryDropdown.addItem(
                "Add New Country ..."
            )  # Add option to add new country
            self.countryDropdown.activated.connect(
                self.add_newCountry
            )  # Connect the "Add New Country" action
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to load countryDropdown data: {e}"
            )

    def edit_record(self):
        """
        Allows the user to edit the selected inventory record in the table.

        Fetches data from the form, and updates the selected record in the database.
        Displays a success or error message based on the result.
        """
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

        # Get new data from the form, use old values if no new value is provided
        size = self.sizeEdit.text() or old_size
        brand = self.brandDropdown.currentText() or old_brand
        country = self.countryDropdown.currentText() or old_country
        date = self.dateEdit.text() or old_date
        stock = self.stockEdit.text() or old_stock

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
        """
        Searches inventory records based on the entered text in the search box.

        Fetches records that match the search text in the `size`, `brand`, or `country` fields
        and displays the results in the table.
        """
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
        """
        Adds a new inventory record to the database.

        Retrieves data from the form and inserts it into the `inventory` table.
        """
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
        """
        Deletes the selected inventory record from the database.

        Prompts for confirmation before removing the record from the `inventory` table.
        """
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
        """
        Enables or disables the filter dropdowns based on the filter checkbox state.

        If checked, it loads the filter elements, otherwise, it reloads the table without filtering.
        """
        if state:
            self.load_filter_elements()
        else:
            # Clear the filter dropdown without reloading the table
            self.filterElementDropdown.clear()
            self.load_table()
        self.filterDropdown.setEnabled(state)
        self.filterElementDropdown.setEnabled(state)

    def load_filter_elements(self):
        """
        Loads available filter elements based on the selected filter type (e.g., year, size, brand).

        Populates the `filterElementDropdown` with the relevant values from the database.
        """
        filter_type = self.filterDropdown.currentText().lower()
        try:
            if self.filterCheckBox.isChecked():
                if filter_type == "year":
                    query = "SELECT DISTINCT substr(date, 7, 4) AS year FROM inventory"
                else:
                    query = f"SELECT DISTINCT {filter_type} FROM inventory"
                self.cursor.execute(query)
                elements = [row[0] for row in self.cursor.fetchall()]
                self.filterElementDropdown.clear()
                self.filterElementDropdown.addItems(elements)
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database Error", f"Failed to load filter elements: {e}"
            )

    def apply_filter(self):
        """
        Applies the selected filter to the inventory records.

        Filters records based on the selected filter type and value from the `filterElementDropdown`.
        """
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
        """
        Allows the user to add a new brand to the database.

        Prompts the user for a brand name and inserts it into the `brand` table.
        """
        brand_name, ok = QtWidgets.QInputDialog.getText(
            self, "New Brand", "Enter brand name:"
        )
        if ok and brand_name:
            try:
                self.cursor.execute(
                    "INSERT INTO brand (name) VALUES (?)", (brand_name,)
                )
                self.conn.commit()
                self.load_brandDropdown()
                QtWidgets.QMessageBox.information(
                    self, "Success", "Brand added successfully."
                )
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(
                    self, "Database Error", f"Failed to add brand: {e}"
                )

    def add_newCountry(self):
        """
        Allows the user to add a new country to the database.

        Prompts the user for a country name and inserts it into the `country` table.
        """
        country_name, ok = QtWidgets.QInputDialog.getText(
            self, "New Country", "Enter country name:"
        )
        if ok and country_name:
            try:
                self.cursor.execute(
                    "INSERT INTO country (name) VALUES (?)", (country_name,)
                )
                self.conn.commit()
                self.load_countryDropdown()
                QtWidgets.QMessageBox.information(
                    self, "Success", "Country added successfully."
                )
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(
                    self, "Database Error", f"Failed to add country: {e}"
                )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
