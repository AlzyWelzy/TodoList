from pathlib import Path
import sys


class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)

    def remove(self, todo):
        self.todos.remove(todo)

    def print(self):
        for i, todo in enumerate(self.todos):
            print(f"{i + 1}: {todo}")

    def save(self):
        path = Path("todos.txt")
        with open(path, "w") as f:
            for todo in self.todos:
                f.write(todo + "\n")

    def load(self):
        path = Path("todos.txt")
        with open(path, "r") as f:
            for line in f:
                self.todos.append(line.strip())

    def run(self):
        while True:
            command = input("What would you like to do? (add/remove/print/save/load/quit) ")
            if command == "quit":
                print("Goodbye!")
                sys.exit(0)
            elif command == "add":
                todo = input("What would you like to add? ")
                self.add(todo)
            elif command == "remove":
                self.print()
                index = int(input("What index would you like to remove? "))
                self.remove(self.todos[index - 1])
            elif command == "print":
                self.print()
            elif command == "save":
                self.save()
            elif command == "load":
                self.load()
            else:
                print("Sorry, I don't understand that command.")


def main():
    todo_list = TodoList()
    todo_list.run()


if __name__ == "__main__":
    main()
