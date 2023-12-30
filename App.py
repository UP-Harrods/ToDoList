import sqlite3

def create_database():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()