tasks = []

def add_task():
    task_name = input("Enter Task Name: ")
    priority = input("Priority (High/Medium/Low): ")

    task = {
        "name": task_name,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(task)
    print(" Task Added Successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']}")
        print(f"   Priority : {task['priority']}")
        print(f"   Status   : {task['status']}")
        print("-" * 30)

def complete_task():
    view_tasks()

    if tasks:
        task_no = int(input("Enter task number to mark as completed: "))

        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["status"] = "Completed"
            print("Task Completed!")
        else:
            print("Invalid Task Number")

def delete_task():
    view_tasks()

    if tasks:
        task_no = int(input("Enter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"'{removed['name']}' deleted.")
        else:
            print("Invalid Task Number")

while True:
    print("\n==============================")
    print("     SMART TO-DO LIST")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using Smart To-Do List!")
        break

    else:
        print("Invalid Choice. Try Again.")
