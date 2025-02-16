import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow  # Import the generated UI class

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
