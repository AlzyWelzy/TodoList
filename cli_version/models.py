import json


class Task:
    def __init__(self, title, description, priority, due_date, category, status):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.status = status


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.title] = task

    # Define other methods for managing tasks
