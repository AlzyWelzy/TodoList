import json
import os
import sys
from datetime import datetime, timedelta
import pathlib
from plyer import notification
import schedule
import threading


class TodoList:
    def __init__(self):
        self.tasks = {}

        self.commands = {
            "schedule": ("schedule reminders", self.remind),
            "add": ("add a task", self.add),
            "update": ("update a task", self.update),
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

        self.load()

        # Start a seperate thread to run the scheduled tasks
        self.schedule_thread = threading.Thread(target=self.remind)
        self.schedule_thread.daemon = True
        self.schedule_thread.start()

        # Schedule the daily reminder
        # Inside the __init__ method
        schedule.every().day.at("11:20").do(self.remind_wrapper)

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

    def get_valid_scheduled_input(self, prompt, choices, func=None):
        user_input = input(prompt)
        if user_input in choices:
            func(user_input) if func else None
            return user_input
        else:
            print("Invalid input")
            return self.get_valid_scheduled_input(prompt, choices)

    def notify(self, title, message):
        notification.notify(
            title=title,
            message=message,
            app_name="Task Manager",
            timeout=5,
        )

    def remind(self, scheduled, due_date):
        if scheduled == "Y":
            today = datetime.today().date()
            task_due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

            if task_due_date == today:
                self.notify(
                    "Task Due Today", f"Task with due date {due_date} is due today."
                )
            elif task_due_date == today + timedelta(days=1):
                self.notify(
                    "Task Due Tomorrow",
                    f"Task with due date {due_date} is due tomorrow.",
                )

    def remind_wrapper(self):
        for task in self.tasks.values():
            if task["scheduled"] == "Y":
                self.remind(task["scheduled"], task["due_date"])

    def format_task_line(self, index, task):
        return "{:<5} {:<10} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(
            index,
            task["priority"],
            task["title"],
            task["description"],
            task["due_date"],
            task["category"],
            task["status"],
            task["scheduled"],
        )

    def display_tasks(self, tasks):
        """Display tasks in a formatted table."""
        print(
            "{:<5} {:<10} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(
                "No.",
                "Priority",
                "Title",
                "Description",
                "Due Date",
                "Category",
                "Status",
                "Scheduled",
            )
        )
        print("-" * 125)

        for index, task in enumerate(tasks, start=1):
            task_line = self.format_task_line(index, task)
            print(task_line)

    def add(self):
        """Add a new task."""
        print("Adding task")
        task = {}
        task["title"] = input("Enter task name: ")
        task["description"] = input("Enter task description: ")
        task["priority"] = self.get_valid_priority_input("Enter priority (L/M/H): ")
        task["due_date"] = self.get_valid_date_input("Enter due date (YYYY-MM-DD): ")
        task["category"] = input("Enter category: ")
        task["status"] = "incomplete"
        task["scheduled"] = self.get_valid_scheduled_input(
            "Schedule task? (Y/N): ",
            ["Y", "N"],
        )

        self.tasks[task["title"]] = task
        if task["scheduled"] == "Y":
            schedule.every().day.at("10:00").do(
                self.remind, task["scheduled"], task["due_date"]
            )
        print("Task added")

    def list(self):
        """Print all tasks."""
        print("Displaying tasks")
        self.display_tasks(self.tasks.values())

    def update(self):
        """Update a task by title."""
        print("Updating task")
        title = input("Enter task title: ")
        try:
            task = self.tasks[title]
        except KeyError:
            print("Invalid title")
            return

        print("Current task:")
        task = f"[{task['priority']}] {task['title']} (Due: {task['due_date']}, Category: {task['category']}, Status: {task['status']})"
        print(task)

        task["priority"] = self.get_valid_priority_input("Enter priority (L/M/H): ")
        task["due_date"] = self.get_valid_date_input("Enter due date (YYYY-MM-DD): ")
        task["category"] = input("Enter category: ")
        print("Task updated")

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

        filtered_tasks = []
        for task in self.tasks.values():
            if task[filter_type] == filter_value:
                filtered_tasks.append(task)

        print("Displaying filtered tasks")
        self.display_tasks(filtered_tasks)

    def sort(self):
        """Sort tasks by priority, due date, or status."""
        print("Sorting tasks")
        sort_type = input("Enter sort type (priority, due date, status): ")

        sorted_tasks = {}
        if sort_type == "priority":
            sorted_tasks = sorted(
                self.tasks.values(), key=lambda x: x["priority"], reverse=True
            )
        elif sort_type == "due date":
            sorted_tasks = sorted(
                self.tasks.values(), key=lambda x: x["due_date"], reverse=True
            )
        elif sort_type == "status":
            sorted_tasks = sorted(
                self.tasks.values(), key=lambda x: x["status"], reverse=True
            )
        else:
            print("Invalid sort type")

        print("Displaying sorted tasks")
        self.display_tasks(sorted_tasks)

    def load(self):
        """Load tasks from a file."""
        print("Loading tasks")
        if not self.FILEPATH.exists():
            print("No tasks found")
            return

        #  check if file is empty
        if os.stat(self.FILEPATH).st_size == 0:
            print("No tasks found")
            return

        with open(self.FILEPATH, "r") as read_file:
            self.tasks = json.load(read_file)

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
        os.system("clear")
        print("Welcome to the Task Manager!")
        # self.load()
        print("")
        print("Commands:")

        for command, (description, _) in self.commands.items():
            print(f"{command}: {description}")

        print("")

        # schedule.every().day.at("10:").do(self.remind)

        while True:
            schedule.run_pending()
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
