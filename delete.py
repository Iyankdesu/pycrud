import mysql.connector


def delete_todo(connection):
    todo_id = input("ID to delete: ")
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM todo WHERE id = %s", (todo_id,))
        connection.commit()
        print("Deleted successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
