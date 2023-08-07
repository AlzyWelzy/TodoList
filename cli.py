import json
import pathlib
import sys
import time

TODOS_PATH = pathlib.Path.home() / ".todos.json"


class todolist:
    def __init__(self):
        self.todos = []
        self.commands = ["add", "remove", "list", "help"]
        self.commands = ["add", "remove", "list", "help"]


    # def login(self):
    #     print("Welcome to the todo list!")
    #     print("Please login to continue")
    #     username = input("Username: ")
    #     password = input("Password: ")


    def create_user(self):
        print("Welcome to the todo list!")
        print("Please create a new user")
        username = input("Username: ")
        password = input("Password: ")

        with open("users.json", "a") as f:
            json.dump({"username": username, "password": password}, f)


    def save(self):
        with open(, "w") as f:
            json.dump(self.todos, f)

    def add(self):
        todo = input("What do you want to add? ")
        self.todos.append(todo)
        self.save()
