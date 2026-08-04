import sqlite3

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

def insert_user(name,age,city):
    connection = sqlite3.connect('advpy.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name,age,city) VALUES (?,?,?)",(name,age,city))
    user_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return user_id


def insert_many_users(users_list):
    connection = sqlite3.connect('advpy.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO users (name,age,city) VALUES (?,?,?)",users_list)
    connection.commit()
    cursor.close()
    connection.close()
   
def get_all_users():
    connection = sqlite3.connect('advpy.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users

def get_user_by_id(user_id):
    connection = sqlite3.connect('advpy.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?",(user_id,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

def update_user_by_age(new_age,user_id):
    connection = sqlite3.connect('advpy.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET age = ? WHERE id = ?",(new_age,user_id))
    rows_affected = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()
    return rows_affected

def delete_user(user_id):
    connection = sqlite3.connect('advpy.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?",(user_id,))
    rows_deleted = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()
    return rows_deleted

def crud_demo():
    create_tables()
    print("Tablecreated")
    insert_user('Namrata',20,'Mumbai')
    insert_user('Purva',19,'Devgad')
    print("User inserted.")

    insert_many_users([
        ('Sumit',20,'Bengaluru'),
        ('Pasu',39,'Indore')
    ])
    print("Multiple users inserted.")

    print("\nAll users List.")
    users = get_all_users()
    for user in users:
        print(f" {user}")

    print("\nAll users List.")
    user = get_user_by_id(2)
    print(f" {user}")

    print("Updating user")
    rows_updated = update_user_by_age(33,2)
    print(f"Updated {rows_updated} row(s)")

    print("\nAll users List.")
    users = get_all_users()
    for user in users:
        print(f" {user}")

    print("Deleting user")
    rows_updated = delete_user(4)
    print(f"Deleted {rows_updated} row(s)")

    print("\nAll users List.")
    user = get_all_users()
    for user in users:
        print(f" {user}")

crud_demo()