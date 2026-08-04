import sqlite3
import os
connection = sqlite3.connect('advpy.db')
connection.close()

connection = sqlite3.connect('advpy.db')
cursor = connection.cursor()
cursor.close()
connection.close()

def create_tables():
    connection = sqlite3.connect('advpy.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL,
        stock INTEGER DEFAULT 0,
        category TEXT
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()
    print("Tables created successfully")
create_tables()