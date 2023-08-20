import json
import os
import sys
from datetime import datetime
import pathlib


class TodoList:
    def __init__(self):
        self.tasks = {}

        self.commands = {
            "add": ("add a task", self.add),
            "list": ("display tasks", self.list),
            "complete": ("complete a task", self.complete),
            "delete": ("delete a task", self.delete),
            "filter": ("filter tasks by priority, due date, or category", self.filter),
            "sort": ("sort tasks by priority, due date, status", self.sort),
            "load": ("loads tasks from file", self.load),
            "save": ("saves tasks to file", self.save),
            "exit": (
                "Exit program after saving",
                self.quit,
            ),
        }

        self.FILEPATH = pathlib.Path("tasks.json")

    def get_valid_date_input(self, prompt):
        while True:
            date = input(prompt)
            try:
                datetime.strptime(date, "%Y-%m-%d")
                return date
            except ValueError:
                print("Invalid date format")

    def get_valid_priority_input(self, prompt):
        while True:
            priority = input(prompt)
            if priority in ["L", "M", "H"]:
                return priority
            else:
                print("Invalid priority")

    def add(self):
        """Add a new task."""
        print("Adding task")
        task = {}
        task["title"] = input("Enter task name: ")
        task["priority"] = self.get_valid_priority_input("Enter priority (L/M/H): ")
        task["due_date"] = self.get_valid_date_input("Enter due date (YYYY-MM-DD): ")
        task["category"] = input("Enter category: ")
        task["status"] = "incomplete"
        self.tasks[task["title"]] = task
        print("Task added")

    def list(self):
        """Print all tasks."""
        print("Displaying tasks")
        for _, task in enumerate(self.tasks.values()):
            task = f"{_+1}. [{task['priority']}] {task['title']} (Due: {task['due_date']}, Category: {task['category']}, Status: {task['status']})"
            print(task)

    def complete(self):
        """Complete a task by title."""
        print("Completing task")
        title = input("Enter task title: ")
        try:
            self.tasks[title]["status"] = "complete"
        except KeyError:
            print("Invalid title")

    def delete(self):
        """Delete a task by title."""
        print("Deleting task")
        title = input("Enter task title: ")
        try:
            del self.tasks[title]
        except KeyError:
            print("Invalid title")

    def filter(self):
        """Filter takes by priority, due date, or category."""
        print("Filtering tasks")
        filter_type = input("Enter filter type (priority, due date, category): ")
        filter_value = input("Enter filter value (eg. [L/M/H] for priority filter): ")

        filtered_tasks = {}
        for _, task in self.tasks.items():
            if task[filter_type] == filter_value:
                filtered_tasks[task["title"]] = task

        print("Displaying filtered tasks")
        for _, task in filtered_tasks.items():
            task = f"{task['priority']} {task['title']} (Due: {task['due_date']}, Category: {task['category']}, Status: {task['status']})"
            print(task)

    def sort(self):
        """Sort tasks by priority, due date, or status."""
        print("Sorting tasks")
        sort_type = input("Enter sort type (priority, due date, status): ")

        sorted_tasks = {}
        if sort_type == "priority":
            sorted_tasks = sorted(
                self.tasks.items(), key=lambda x: x[1]["priority"], reverse=True
            )
        elif sort_type == "due date":
            sorted_tasks = sorted(
                self.tasks.items(), key=lambda x: x[1]["due_date"], reverse=True
            )
        elif sort_type == "status":
            sorted_tasks = sorted(
                self.tasks.items(), key=lambda x: x[1]["status"], reverse=True
            )
        else:
            print("Invalid sort type")

        print("Displaying sorted tasks")
        for _, task in sorted_tasks:
            task = f"{task['priority']} {task['title']} (Due: {task['due_date']}, Category: {task['category']}, Status: {task['status']})"
            print(task)

    def load(self):
        """Load tasks from a file."""
        print("Loading tasks")
        try:
            with open(self.FILEPATH, "r") as read_file:
                self.tasks = json.load(read_file)
        except FileNotFoundError:
            print("File not found")

    def save(self):
        """Save tasks to a file."""
        print("Saving tasks")
        with open(self.FILEPATH, "w") as write_file:
            json.dump(self.tasks, write_file)

    def quit(self):
        """Quit the program."""
        print("Quitting task manager")
        self.save()
        sys.exit(0)

    def run(self):
        self.load()
        print("Welcome to the Task Manager!")
        print("Commands:")

        for command, (description, _) in self.commands.items():
            print(f"{command}: {description}")

        print("")

        while True:
            command = input("Enter a command: ").strip().lower()
            if command not in self.commands:
                print("Invalid command")
                continue

            self.commands[command][1]()


def main():
    todo_list = TodoList()
    todo_list.run()


if __name__ == "__main__":
    main()
