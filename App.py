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


def add_task(task_name):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    
    cursor.execute("INSERT INTO tasks (task_name) VALUES (?)", (task_name,))

    connection.commit()
    connection.close()


def view_tasks():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

 
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}")

    connection.close()


def delete_task(task_id):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

   
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    connection.commit()
    connection.close()