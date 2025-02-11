tasks = []

def add_task(task):
    tasks.append({"task":task, "completed":False})
    print("task added")

def list_tasks():
    print("\nTo-Do list")
    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            status=["done"]
        else:
            status = " "
        print(f"{index}. [{status}] {task['task']}")
    print()
def mark_completed(index):
    if 1 <= index <= len(tasks):
        tasks[index -1]["completed"] = True
        print("Task marked as complete")
    else:
        print("invalid task index")


while True:
    print("===To Do List===")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark as complete")
    print("4. Exit")

    choice = input("Enter Your Choice")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()

    elif choice == "3":
        list_tasks()
        index = int(input("Enter the task number"))
        mark_completed(index)

    elif choice == "4":
        print("bye")
        break
    else:
        print("Invalid choice. Please choose between 1,2,3,4")