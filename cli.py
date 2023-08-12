import pathlib
import sys

FILEPATH = pathlib.Path("todos.txt")


class TodoList:
    def __init__(self):
        self.todos = []

        self.commands = {
            "add": ("add a todo", self.add),
            "remove": ("remove a todo", self.remove),
            "print": ("print all todos", self.print),
            "load": ("loads all todos from file", self.load),
            "save": ("saves all todos to file", self.save),
            "quit": ("quit the program without saving", self.quit),
        }

    def add(self, todo):
        """Add a new todo."""
        print("Adding todo")
        print("Adding todo")
        self.todos.append(todo)

    def remove(self, todo):
        """Remove a todo by index."""
        print("Removing todo")
        try:
            index = int(todo) - 1
            self.todos.pop(index)
        except (ValueError, IndexError):
            print("Invalid index")

    def print(self):
        """Print all todos."""
        print("Printing todos")
        for i, todo in enumerate(self.todos):
            print(f"{i + 1}: {todo}")

    def save(self):
        """Save todos to a file."""
        print("Saving todos")
        with open(FILEPATH, "w") as write_file:
            for todo in self.todos:
                write_file.write(todo + "\n")

    def load(self):
        """Load todos from a file."""
        print("Loading todos")
        try:
            with open(FILEPATH, "r") as read_file:
                self.todos = [line.strip() for line in read_file]
        except FileNotFoundError:
            print("File not found")

    def quit(self):
        """Quit the program."""
        print("Quitting todo")
        sys.exit(0)

    def run(self):
        print("Welcome to the Todo List App!")
        while True:
            print("What would you like to do? Here are your options:")
            for command, (description, _) in self.commands.items():
                print(f"{command}: {description}")
            choice = input(">>> ").strip().lower()
            if choice in self.commands:
                _, func = self.commands[choice]
                arg = input(f"{func.__name__}: ")
                func(arg)
            else:
                print("Invalid command")


def main():
    todo_list = TodoList()
    todo_list.run()


if __name__ == "__main__":
    main()
