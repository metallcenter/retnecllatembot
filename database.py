import sqlite3


def connect_database():
    database = sqlite3.connect("database.sqlite")
    cursor = database.cursor()
    return database, cursor


database, cursor = connect_database()


def create_users_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(50) NOT NULL,
        chat_id INTEGER NOT NULL UNIQUE,
        name VARCHAR(50),
        second_name VARCHAR(50),
        phone_number VARCHAR(13)
    )""")

database.execute
create_users_table()
database.commit
database.close