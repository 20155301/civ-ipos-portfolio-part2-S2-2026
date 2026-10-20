from src.task_manager import add_task, delete_task, list_tasks, edit_task
from src.file_handler import load_tasks


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. List Tasks")
        print("4. Edit Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (DD-MM-YYYY): ")
            add_task(tasks, title, description, due_date)
        elif choice == "2":
            title = input("Title of the task to delete: ")
            if delete_task(tasks, title):
                print("Task deleted successfully.")
            else:
                print("Task not found.")
        elif choice == "3":
            list_tasks(tasks)

        elif choice == "4":
            if not tasks:
                print("No tasks available to edit.")
                continue

            print("\nAvailable tasks:")
            list_tasks(tasks)

            title = input("Enter title you want to edit: ")
            new_title = input("New Title: ")
            new_description = input("New Description: ")
            new_due_date = input("New Due Date (DD-MM-YYYY): ")

            if edit_task(tasks, title, new_title, new_description, new_due_date):
                print("Task edited successfully.")
            else:
                print("Task could not be edited.")

        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
