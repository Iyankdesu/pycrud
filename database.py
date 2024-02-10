import mysql.connector

host = "localhost"
user = "root"
password = ""
database = "db_pytodo"


def connect():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )
        print("Database connection success!")
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)


def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS todo (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                date DATE
            )
        """
        )
        connection.commit()
        print("Table created successfully or already exists.")
    except mysql.connector.Error as err:
        print("Error:", err)
