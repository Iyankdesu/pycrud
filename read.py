import mysql.connector
from prettytable import PrettyTable


def read_todos(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM todo")
        todos = cursor.fetchall()
        if todos:
            table = PrettyTable(["ID", "Title", "Description", "Date"])
            for todo in todos:
                table.add_row(todo)
            print(table)
    except mysql.connector.Error as err:
        print("Error:", err)
