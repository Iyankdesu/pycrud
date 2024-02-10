import mysql.connector


def read_todos(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM todo")
        todos = cursor.fetchall()
        print("List:")
        for todo in todos:
            print(todo)
    except mysql.connector.Error as err:
        print("Error:", err)
