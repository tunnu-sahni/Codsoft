class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            del self.tasks[task_number]
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx + 1}. {task['task']} - {status}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Remove Task")
        print("4. Show Tasks")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.show_tasks()
            task_number = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_completed(task_number)
        elif choice == '3':
            todo_list.show_tasks()
            task_number = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(task_number)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            print("Exiting the To-Do List program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
