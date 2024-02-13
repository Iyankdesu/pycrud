import database
import create
import read
import update
import delete


def display_menu():
    print("\n1. Add")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Quit")


def main():
    connection = database.connect()
    database.create_table(connection)

    while True:
        display_menu()
        choice = input("Choose (1/2/3/4/5): ")

        if choice == "1":
            create.create_todo(connection)
        elif choice == "2":
            read.read_todos(connection)
        elif choice == "3":
            update.update_todo(connection)
        elif choice == "4":
            delete.delete_todo(connection)
        elif choice == "5":
            print("Quit...")
            break
        else:
            print("Invalid choice.")

    connection.close()


if __name__ == "__main__":
    main()
