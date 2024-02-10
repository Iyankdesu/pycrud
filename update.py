import mysql.connector


def update_todo(connection):
    todo_id = input("ID to update: ")
    new_title = input("New title (Leave blank if you don't want to change): ")
    new_description = input(
        "New description (Leave blank if you don't want to change): "
    )
    try:
        cursor = connection.cursor()
        update_query = "UPDATE todo SET"
        update_data = []
        if new_title:
            update_query += " title = %s,"
            update_data.append(new_title)
        if new_description:
            update_query += " description = %s,"
            update_data.append(new_description)
        update_query = update_query.rstrip(",") + " WHERE id = %s"
        update_data.append(todo_id)
        cursor.execute(update_query, update_data)
        connection.commit()
        print("Updated successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
