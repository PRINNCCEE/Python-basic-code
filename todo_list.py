# Simple To-Do List in Python

tasks = []  # Empty list to store tasks

def add_task(task):
    tasks.append(task)
    print(f"✅ '{task}' task added!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"❌ '{task}' task removed!")
    else:
        print(f"⚠️ Task '{task}' not found!")

def show_tasks():
    if tasks:
        print("\n📌 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\n📭 No tasks added yet!")

while True:
    print("\n1️⃣ Add Task  2️⃣ Remove Task  3️⃣ Show Tasks  4️⃣ Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("🚀 Exiting... Have a great day!")
        break
    else:
        print("❌ Invalid choice! Try again.")
