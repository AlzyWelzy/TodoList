import os

tasks = {}


def add():
    """Add a new task."""
    print("Adding task")
    task = {}
    task["title"] = input("Enter task title: ")
    task["priority"] = input("Enter task priority: ")
    task["due_date"] = input("Enter task due date: ")
    task["category"] = input("Enter task category: ")
    task["status"] = "incomplete"
    tasks[0] = task


os.system("clear")
add()

print(tasks)

for _, __ in tasks.items():
    task = f"{__['priority']} {__['title']} (Due: {__['due_date']}, Category: {__['category']}, Status: {__['status']})"

    print(task)
