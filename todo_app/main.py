import sys
import utils

def main():
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Quit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            utils.add_task(title, description, priority, due_date)
            print("Task added successfully!")

        elif choice == '2':
            task_id = input("Enter the task ID to remove: ")
            utils.remove_task(task_id)
            print("Task removed successfully!")

        elif choice == '3':
            task_id = input("Enter the task ID to mark as completed: ")
            utils.mark_task_completed(task_id)
            print("Task marked as completed!")

        elif choice == '4':
            tasks = utils.list_tasks()
            print("\nTasks:")
            for task in tasks:
                task_id, title, priority, description , due_date, completed = task
                status = "Completed" if completed else "Pending"
                print(f"{task_id}. {title} ( Priority: {priority} , Description: {description}, Due Date: {due_date}, Status: {status})")


        elif choice == '5':
            sys.exit(0)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
