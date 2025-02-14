# database.py
import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("tyreInventory.db")
        self.cursor = self.connection.cursor()
        self.create_tables()


    def create_tables(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                size TEXT NOT NULL,
                brand TEXT NOT NULL,
                country TEXT NOT NULL,
                date TEXT NOT NULL,
                stock INTEGER NOT NULL
                )"""
        )
        




        self.connection.commit()

    def add_product(self, name, quantity, price):
        








        self.cursor.execute(
            """INSERT INTO products (name, quantity, price)
                               VALUES (?, ?, ?)
                               """,
            (name, quantity, price),
        )
        self.connection.commit()

    def get_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()
