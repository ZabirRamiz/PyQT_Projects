# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 575)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("/* List Item */\n"
"QListWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D3D3D3;\n"
"    border-radius: 3px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: #F4F4F9;\n"
"    padding: 5px;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #E0E0E0;\n"
"}\n" 
"\n"
"QListWidget::item:selected {\n"
"    background-color: #A8DADC;\n"
"    color: #ffffff;\n"
"}\n"
"/* Buttons */\n"
"QPushButton#searchButton {\n"
"    background-color: #A8DADC;\n"
"    border: 1px solid #81C3C8;\n"
"    border-radius: 5px;\n"
"    color: #ffffff;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton#searchButton:hover {\n"
"    background-color: #81C3C8;\n"
"}\n"
"\n"
"/* Add Button */\n"
"QPushButton#addItemButton {\n"
"    background-color: #BDE7BD;\n"
"    border: 1px solid #A3D9A3;\n"
"    border-radius: 5px;\n"
"    color: #ffffff;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton#addItemButton:hover {\n"
"    background-color: #A3D9A3;\n"
"}\n"
"QPushButton#addRecordButton {\n"
"    background-color: #BDE7BD;\n"
"    border: 1px solid #A3D9A3;\n"
"    border-radius: 5px;\n"
"    color: #ffffff;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton#addRecordButton:hover {\n"
"    background-color: #A3D9A3;\n"
"}\n"
"\n"
"/* Edit Button */\n"
"QPushButton#editItemButton {\n"
"    background-color: #FAD6A5;\n"
"    border: 1px solid #F9C784;\n"
"    border-radius: 5px;\n"
"    color: #ffffff;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton#editItemButton:hover {\n"
"    background-color: #F9C784;\n"
"}\n"
"QPushButton#editRecordButton {\n"
"    background-color: #FAD6A5;\n"
"    border: 1px solid #F9C784;\n"
"    border-radius: 5px;\n"
"    color: #ffffff;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton#editRecordButton:hover {\n"
"    background-color: #F9C784;\n"
"}\n"
"/* Delete Button */\n"
"QPushButton#deleteItemButton {\n"
"    background-color: #FFADAD;\n"
"    border: 1px solid #FF8585;\n"
"    border-radius: 5px;\n"
"    color: #ffffff;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton#deleteItemButton:hover {\n"
"    background-color: #FF8585;\n"
"}\n"
"QPushButton#deleteRecordButton {\n"
"    background-color: #FFADAD;\n"
"    border: 1px solid #FF8585;\n"
"    border-radius: 5px;\n"
"    color: #ffffff;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton#deleteRecordButton:hover {\n"
"    background-color: #FF8585;\n"
"}\n"
"/* Input Box */\n"
"QLineEdit {\n"
"    background-color: #F1F1F1;\n"
"    border: 1px solid #D3D3D3;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Table */\n"
"QTableWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;\n"
"    gridline-color: #E0E0E0;\n"
"    color: #333333;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #C9CCD5;\n"
"    color: #333333;\n"
"    padding: 5px;\n"
"    border: 1px solid #E0E0E0;\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: #F4F4F9;\n"
"}\n"
"QTableWidget::item:alternate {\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"/* Main Background */\n"
"QWidget#centralwidget {\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QWidget#col1 {\n"
"    background-color: #EDEEF7;\n"
"}\n"
"QWidget#col3 {\n"
"    background-color: #EDEEF7;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(20, 20, 1231, 486))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.masterLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.masterLayout.setContentsMargins(0, 0, 0, 0)
        self.masterLayout.setObjectName("masterLayout")
        self.col1 = QtWidgets.QVBoxLayout()
        self.col1.setObjectName("col1")
        self.itemList = QtWidgets.QListWidget(self.horizontalLayoutWidget_7)
        self.itemList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.itemList.setObjectName("itemList")
        item = QtWidgets.QListWidgetItem()
        self.itemList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.itemList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.itemList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.itemList.addItem(item)
        self.col1.addWidget(self.itemList)
        self.addItemButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.addItemButton.setObjectName("addItemButton")
        self.col1.addWidget(self.addItemButton)
        self.editItemButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.editItemButton.setObjectName("editItemButton")
        self.col1.addWidget(self.editItemButton)
        self.deleteItemButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.deleteItemButton.setObjectName("deleteItemButton")
        self.col1.addWidget(self.deleteItemButton)
        self.masterLayout.addLayout(self.col1)
        self.col2 = QtWidgets.QVBoxLayout()
        self.col2.setObjectName("col2")
        self.col2_row1 = QtWidgets.QHBoxLayout()
        self.col2_row1.setObjectName("col2_row1")
        self.searchInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.searchInput.setObjectName("searchInput")
        self.col2_row1.addWidget(self.searchInput)
        self.searchButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.searchButton.setObjectName("searchButton")
        self.col2_row1.addWidget(self.searchButton)
        self.col2.addLayout(self.col2_row1)
        self.inventoryTable = QtWidgets.QTableWidget(self.horizontalLayoutWidget_7)
        self.inventoryTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.inventoryTable.setObjectName("inventoryTable")
        self.inventoryTable.setColumnCount(5)
        self.inventoryTable.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(4, item)
        self.inventoryTable.horizontalHeader().setCascadingSectionResizes(False)
        self.col2.addWidget(self.inventoryTable)
        self.masterLayout.addLayout(self.col2)
        self.col3 = QtWidgets.QVBoxLayout()
        self.col3.setObjectName("col3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(45)
        self.verticalLayout.setObjectName("verticalLayout")
        self.col3_row1 = QtWidgets.QHBoxLayout()
        self.col3_row1.setObjectName("col3_row1")
        self.partNumberLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.partNumberLabel.setObjectName("partNumberLabel")
        self.col3_row1.addWidget(self.partNumberLabel)
        self.partNumberInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.partNumberInput.setObjectName("partNumberInput")
        self.col3_row1.addWidget(self.partNumberInput)
        self.verticalLayout.addLayout(self.col3_row1)
        self.col3_row2 = QtWidgets.QHBoxLayout()
        self.col3_row2.setObjectName("col3_row2")
        self.purchasePriceLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.purchasePriceLabel.setObjectName("purchasePriceLabel")
        self.col3_row2.addWidget(self.purchasePriceLabel)
        self.purchasePriceInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.purchasePriceInput.setObjectName("purchasePriceInput")
        self.col3_row2.addWidget(self.purchasePriceInput)
        self.verticalLayout.addLayout(self.col3_row2)
        self.col2_row3 = QtWidgets.QHBoxLayout()
        self.col2_row3.setObjectName("col2_row3")
        self.sellingPriceLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.sellingPriceLabel.setObjectName("sellingPriceLabel")
        self.col2_row3.addWidget(self.sellingPriceLabel)
        self.sellingPriceInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.sellingPriceInput.setObjectName("sellingPriceInput")
        self.col2_row3.addWidget(self.sellingPriceInput)
        self.verticalLayout.addLayout(self.col2_row3)
        self.col3_row4 = QtWidgets.QHBoxLayout()
        self.col3_row4.setObjectName("col3_row4")
        self.quraterLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.quraterLabel.setObjectName("quraterLabel")
        self.col3_row4.addWidget(self.quraterLabel)
        self.quarterInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.quarterInput.setInputMask("")
        self.quarterInput.setObjectName("quarterInput")
        self.col3_row4.addWidget(self.quarterInput)
        self.verticalLayout.addLayout(self.col3_row4)
        self.col3_row5 = QtWidgets.QHBoxLayout()
        self.col3_row5.setObjectName("col3_row5")
        self.stockLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.stockLabel.setObjectName("stockLabel")
        self.col3_row5.addWidget(self.stockLabel)
        self.stockInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.stockInput.setObjectName("stockInput")
        self.col3_row5.addWidget(self.stockInput)
        self.verticalLayout.addLayout(self.col3_row5)
        self.col3.addLayout(self.verticalLayout)
        self.addRecordButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.addRecordButton.setObjectName("addRecordButton")
        self.col3.addWidget(self.addRecordButton)
        self.editRecordButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.editRecordButton.setObjectName("editRecordButton")
        self.col3.addWidget(self.editRecordButton)
        self.deleteRecordButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.deleteRecordButton.setObjectName("deleteRecordButton")
        self.col3.addWidget(self.deleteRecordButton)
        self.masterLayout.addLayout(self.col3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1281, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.itemList.isSortingEnabled()
        self.itemList.setSortingEnabled(False)
        item = self.itemList.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.itemList.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.itemList.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.itemList.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        self.itemList.setSortingEnabled(__sortingEnabled)
        self.addItemButton.setText(_translate("MainWindow", "Add Item"))
        self.editItemButton.setText(_translate("MainWindow", "Edit Item"))
        self.deleteItemButton.setText(_translate("MainWindow", "Delete Item"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        item = self.inventoryTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.inventoryTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.inventoryTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.inventoryTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.inventoryTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.inventoryTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.inventoryTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.inventoryTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.inventoryTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.inventoryTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.inventoryTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        self.partNumberLabel.setText(_translate("MainWindow", "Part Number:"))
        self.purchasePriceLabel.setText(_translate("MainWindow", "Purchase Price:"))
        self.sellingPriceLabel.setText(_translate("MainWindow", "Selling Price:"))
        self.quraterLabel.setText(_translate("MainWindow", "Quarter:"))
        self.stockLabel.setText(_translate("MainWindow", "Stock:"))
        self.addRecordButton.setText(_translate("MainWindow", "Add Record"))
        self.editRecordButton.setText(_translate("MainWindow", "Edit Record"))
        self.deleteRecordButton.setText(_translate("MainWindow", "Delete Record"))
