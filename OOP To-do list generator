# Clean To-Do List Program using OOP

# Class representing a Task
class Task:
    def __init__(self, description):
        self.description = description
        self.done = False  # Initially not marked done

    def mark_done(self):
        self.done = True  # Marks Task Completed 

    def __str__(self):
        if self.done == True:
            printed = "[X]"  # Task done
        else:
            printed = "[ ]"  # Task not done
        return printed + " " + self.description


# ToDo List Class
class ToDoList:

    def __init__(self):
        self.tasks = []  # Defines the empty Task List 

    # Function to Add Task
    def add_task(self, description):
        self.tasks.append(Task(description))  # Utilizes append to add task to list 
        print("Task added.")

    # Function to View Task 
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")  # If no tasks, doesn't showcase
            return
        for id, task in enumerate(self.tasks, 1):  # Loops through task
            print(f"{id}. {task}")  # Prints task number and status

    # Function to mark tasks
    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    # Function to Remove Tasks based on index
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):  # If the index is in the list
            removed_task = self.tasks.pop(index)  # Utilizes pop function to remove the task based on number
            print(f"Task removed.")
        else:  # If task number is invalid 
            print("Invalid task number.")


# Menu function
def menu():
    todo = ToDoList()  # Declares list as todo

    # While True 
    while True:
        # Prints the menu
        print("--- To Do Menu ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        # If user chooses 1, add task
        if choice == '1':
            description = input("Enter task description: ")
            todo.add_task(description)

        # If user chooses 2, view tasks
        elif choice == '2':
            todo.view_tasks()

        # If user chooses 3, mark certain completed tasks
        elif choice == '3':
            try:
                num = int(input("Enter task number to mark as done: "))
                todo.mark_task_done(num - 1)
            except ValueError:
                print("Please enter a valid number.")

        # If user chooses 4, remove certain tasks
        elif choice == '4':
            try:
                num = int(input("Enter task number to delete: "))
                todo.remove_task(num - 1)
            except ValueError:
                print("Please enter a valid number.")

        # If user chooses 5, exit program
        elif choice == '5':
            print("Exiting program. Goodbye.")
            break

        # If invalid number 
        else:
            print("Choose between 1-5.")

menu()
