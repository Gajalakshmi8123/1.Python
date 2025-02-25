def add_task(task_list):
    """Adds a new task to the task list."""
    new_task = input("Enter the task: ")
    task_list.append(new_task)
    print(f"Task '{new_task}' added successfully!")

def view_task(task_list):
    """Displays all tasks."""
    if not task_list:
        print("\nNo tasks in the list.")
    else:
        print("\nCurrent To-Do List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def main():
    task_list = []  # Initialize an empty task list

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                add_task(task_list)
            elif choice == 2:
                view_task(task_list)
            elif choice == 3:
                print("Exiting the To-Do List. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the program
main()
