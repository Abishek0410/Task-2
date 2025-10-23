def load_tasks():
    tasks = []
    with open("todo.txt", "r") as file:
        for i in file:
            tasks.append(i.strip())
    return tasks

def view_tasks(tasks):
    with open("todo.txt", "w") as file:
        for i in tasks:
            file.write(i + "\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, i in enumerate(tasks, start=1):
            print(f"{i}. {i}")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. View tasks")
        print("2. Add i")
        print("3. Remove i")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter a new i: ")
            tasks.append(new_task)
            view_tasks(tasks)
            print("Task added!!!")

        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                try:
                    num = int(input("Enter i number to remove: "))
                    removed = tasks.pop(num - 1)
                    view_tasks(tasks)
                    print(f"Removed: {removed}")
                except (ValueError, IndexError):
                    print("Invalid i number!")

        elif choice == "4":
            print("Goodbye!!!")
            break

        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
