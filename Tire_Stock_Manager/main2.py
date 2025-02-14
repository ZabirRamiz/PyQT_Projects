import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main import Ui_MainWindow  # Import generated UI class

# from database import Database


class tyreInventoryApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.db = Database()
        # self.load_products()
        # self.addProductButton.clicked.connect(self.add_product)

    def load_products(self):
        products = self.db.get_products()
        for product in products:
            self.productList.addItem(
                f"{product[1]} - Quantity: {product[2]}, Price: {product[3]}"
            )

    def add_product(self):
        name = self.productNameInput.text()
        quantity = self.productQuantityInput.value()
        price = self.productPriceInput.value()
        if name and quantity > 0 and price > 0:
            self.db.add_product(name, quantity, price)
            self.productList.clear()
            self.load_products()
            QMessageBox.information(self, "Success", "Product added successfully!")
        else:
            QMessageBox.warning(
                self, "Input Error", "Please provide valid product details."
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = tyreInventoryApp()
    window.show()
    sys.exit(app.exec_())
