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
            handle_delete_task(tasks)

        elif choice == "3":
            list_tasks(tasks)

        elif choice == "4":
            handle_edit_task(tasks)

        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")


def handle_edit_task(tasks):
    """
    Handle user input for editing an existing task.

    Displays the list of available tasks and prompts the user to
    select a task by its title. The user can then enter a new title,
    description and due date.

    The function calls edit_task() to validate and update the task
    details and displays a message indicating whether the edit
    was successful.

    Args:
        tasks (list): The list of existing Task objects.

    """
    if not tasks:
        print("No tasks available to edit.")
        return

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


def handle_delete_task(tasks):
    """
    Handle user input for deleting an existing task.

    Prompts the user to enter the title of the task to delete.
    Calls delete_task() to remove the selected task and displays
    a message indicating whether the deletion was successful.

    Args:
        tasks (list): The list of existing Task objects.
    """
    title = input("Title of the task to delete: ")

    if delete_task(tasks, title):
        print("Task deleted successfully.")
    else:
        print("Task not found.")


if __name__ == "__main__":
    main()
