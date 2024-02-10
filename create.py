import mysql.connector


def create_todo(connection):
    title = input("Title: ")
    description = input("Description: ")
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO todo (title, description, date)
            VALUES (%s, %s, CURRENT_DATE)
        """,
            (title, description),
        )
        connection.commit()
        print("Added successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
