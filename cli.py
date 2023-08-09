import pathlib
import sys
import time

FILEPATH = pathlib.Path("todos.txt")


class TodoList:
    def __init__(self):
        self.todos = []
        # self.commands = [
        #     "add",
        #     "remove",
        #     "print",
        #     "load",
        #     "save",
        #     "help",
        #     "quit",
        # ]

        self.commands = {
            "add": "add a todo",
            "remove": "remove a todo",
            "print": "print all todos",
            "load": "loads all todos from file",
            "save": "saves all todos to file",
            "quit": "quit the program without saving",
        }

    def add(self, todo):
        print("adding todo")
        self.todos.append(todo)

    def remove(self, todo):
        print("removing todo")
        del self.todos[todo]

    def print(self):
        print("printing todo")
        for i in enumerate(self.todos):
            print(f"{i + 1}: {todo}")

    def save(self):
        print("saving todo")
        with open(FILEPATH, "w") as write_file:
            for todo in self.todos:
                write_file.write(todo + "\n")

    def load(self):
        print("loading todo")
        with open(FILEPATH, "r") as read_file:
            for line in read_file:
                self.todos.append(line.strip())

    def quit(self):
        print("quitting todo")
        sys.exit(0)

    def run(self):
        while True:
            input_text = "What would you link to do? Here are your options:"
            print(input_text)
            for x, y in self.commands.items():
                print(f"{x}: {y}")
            command = input(">>> ").strip().lower()
            if command == "add":
                todo = input("What would you like to add? ")
                self.add(todo)
            elif command == "remove":
                todo = input("What index would you like to remove? ")
                self.remove(todo - 1)
            elif command == "print":
                self.print()
            elif command == "load":
                self.load()
            elif command == "save":
                self.save()
            elif command == "quit":
                print("Goodbye!")
                self.quit()
            else:
                print("Invalid command")


def main():
    todo_list = TodoList()
    todo_list.run()


if __name__ == "__main__":
    main()
