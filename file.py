import os
import datetime

class Task:
    def __init__(self, task_id, title, description, due_date, status="To Do"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def display_details(self):
        print(f"\nTask ID: {self.task_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date}")
        print(f"Status: {self.status}")

def add_task():
    task_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")

    task = Task(task_id, title, description, due_date)

    with open("tasks.txt", "a") as file:
        file.write(f"{task.task_id},{task.title},{task.description},{task.due_date},{task.status}\n")

    print("Task added successfully!")

def view_tasks():
    with open("tasks.txt", "r") as file:
        for line in file:
            data = line.strip().split(',')
            task = Task(*data)
            task.display_details()

def search_by_id(id):
    with open("tasks.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == id:
                task = Task(*data)
                task.display_details()

def delete_task(task_id_to_delete):
    with open("tasks.txt", "r") as file:
        lines = file.readlines()

    with open("tasks.txt", "w") as file:
        for line in lines:
            data = line.strip().split(',')
            if data[0] != task_id_to_delete:
                file.write(line)

    print(f"Task with ID {task_id_to_delete} deleted successfully!")

def main_menu():
    while True:
        print("\nTask Management System Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Task")
        print("4. Search by ID")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            task_id_to_delete = input("Enter Task ID to delete: ")
            delete_task(task_id_to_delete)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            id_to_view = input("Enter Task ID to view: ")
            search_by_id(id_to_view)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")

if __name__ == "__main__":
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass

    main_menu()
