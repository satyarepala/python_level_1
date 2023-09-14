"""
**Problem Statement: Task Scheduling and Tracking**

You are tasked with creating a Python program to help users schedule and track their tasks efficiently. The program should allow users to add, update, and manage tasks, and it should provide features for organizing tasks based on priority and due dates.

Here are the specific requirements for your solution:

1. **Task Management:** Implement a system for managing tasks. Each task should have the following attributes:
   - Task name
   - Task description
   - Priority (e.g., high, medium, low)
   - Due date (optional)
   - Status (e.g., not started, in progress, completed)

2. **User Interaction:** Create a user-friendly command-line interface (CLI) that allows users to:
   - Add new tasks with details.
   - View a list of all tasks.
   - Update task information (e.g., change priority, mark as completed, update due date).
   - Delete tasks.
   - Sort tasks based on priority or due date.
   - Search for tasks by name or status.

3. **Task Notifications:** Implement a notification system that reminds users of upcoming tasks that have due dates.

4. **Task Statistics:** Provide statistics on tasks, such as the number of completed tasks, tasks by priority, and tasks overdue.

5. **Data Storage:** Store tasks and their details within the program's memory, eliminating the need for external files or databases.

6. **Efficiency:** Ensure that the program can efficiently handle a large number of tasks without significant performance issues.

7. **Optional Features:** Consider adding optional features such as task categories or labels, task dependencies, and recurring tasks.

Here's an example of how the program might be used:

```python
# User interacts with the task scheduling and tracking program.

# Your program should provide options for adding, updating, and managing tasks.
# Users can organize tasks by priority, due date, and status.
# The program should also notify users of upcoming tasks.
```

Your solution should help users efficiently manage their tasks and stay organized without the need for external files or libraries.
"""

# Task scheduling and tracking program

# Initialize an empty list to store tasks
tasks = []

# Function to add a new task
def add_task():
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    priority = input("Enter task priority (high, medium, low): ")
    due_date = input("Enter task due date (optional): ")

    task = {
        'name': name,
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'status': 'Not started',
    }

    tasks.append(task)
    print("Task added successfully.")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. Name: {task['name']}, Priority: {task['priority']}, Status: {task['status']}")

# Function to update a task
def update_task():
    list_tasks()
    choice = int(input("Enter the task number to update: "))
    if 1 <= choice <= len(tasks):
        task = tasks[choice - 1]
        print("Current task details:")
        print(f"Name: {task['name']}")
        print(f"Description: {task['description']}")
        print(f"Priority: {task['priority']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Status: {task['status']}")

        field = input("Enter field to update (name, description, priority, due_date, status): ")
        if field in task:
            new_value = input(f"Enter new {field}: ")
            task[field] = new_value
            print("Task updated successfully.")
        else:
            print("Invalid field.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    list_tasks()
    choice = int(input("Enter the task number to delete: "))
    if 1 <= choice <= len(tasks):
        del tasks[choice - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\nTask Scheduling and Tracking")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    option = input("Select an option: ")

    if option == '1':
        add_task()
    elif option == '2':
        list_tasks()
    elif option == '3':
        update_task()
    elif option == '4':
        delete_task()
    elif option == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")
