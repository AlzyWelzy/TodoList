import pathlib
import sys
import time

FILEPATH=pathlib.Path("todos.txt")1


class todolist:
    def __init__(self):
        self.todos = []
        self.commands = ["add", "remove", "list", "help"]


    # def login(self):
    #     print("Welcome to the todo list!")
    #     print("Please login to continue")
    #     username = input("Username: ")
    #     password = input("Password: ")

    def save(self):
        with open(, "w") as f:
            json.dump(self.todos, f)

    def add(self):
        todo = input("What do you want to add? ")
        self.todos.append(todo)
        self.save()
