tasks = []

def add_task():
    task = input("Enter a new task: ")
    priority = input("Enter the priority (high, medium, low): ")
    deadline = input("Enter the deadline (YYYY-MM-DD): ")
    tasks.append({"task": task, "priority": priority, "deadline": deadline})
    print("Task added successfully!\n")

def show_tasks():
    if not tasks:
        print('No tasks available.')
        return 
    print("\nTo-Do List:")
    for i, task in enumerate(tasks,1):
        print(f"{i}. {task['task']} - Priority: {task['priority']}, Deadline: {task['deadline']}")
    print()

def complete_tasks():
    show_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            remove_task = tasks.pop(task_num - 1)
            print(f"Task '{remove_task['task']}' completed and removed!\n")
        else:
            print("Invalid task number. Please try again.\n")
    except ValueError:
        print("Please enter a valid number.\n")

while True:
    print("1. Add Task\n2. Show Tasks\n3. Exit\n4. Complete a Task")
    choice = input("Choose an option: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        print("Exiting the program.")
        break
    elif choice == '4':
        complete_tasks()
    else:
        print("Invalid choice. Please try again.\n")
# This is a simple command-line to-do list application that has priority and deadlines.