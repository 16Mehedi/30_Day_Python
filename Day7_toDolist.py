# To Do List App

tasks = []

while True:
    print("\n==== TO DO LIST ====")
    print("1 - Show tasks")
    print("2 - Add task")
    print("3 - Delete task")
    print("0 - Quit")

    choice = input("Choose: ")

    # Show tasks
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

    # Add task
    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    # Delete task
    elif choice == "3":
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        print("Task deleted!")

    # Quit
    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
