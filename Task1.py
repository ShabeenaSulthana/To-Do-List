

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task added: {task}")

def view_tasks():
    print("Your tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def update_task():
    task_num = int(input("Enter the task number to update: "))
    task = input("Enter the updated task: ")
    tasks[task_num - 1] = task
    print(f"Task updated: {task}")

def delete_task():
    task_num = int(input("Enter the task number to delete: "))
    tasks.pop(task_num - 1)
    print("Task deleted")

def main():
    while True:
        print("\n1. Add task\n2. View tasks\n3. Update task\n4. Delete task\n5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()