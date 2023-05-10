from pathlib import Path
import sys
class TodoList:
    def __init__(self):
        self.todos = []
        self.commands = ["add", "remove", "print", "save", "load", "quit"]

    def add(self, todo):
        self.todos.append(todo)

    def remove(self, todo):
        del self.todos[todo]

    def print(self):
        for i, todo in enumerate(self.todos):
            print(f"{i + 1}: {todo}")

    def save(self):
        path = Path("todos.txt")
        write_file = open(path, "w")
        for todo in self.todos:
            write_file.write(todo + "\n")
        write_file.close()

    def load(self):
        path = Path("todos.txt")
        read_file = open(path, "r")
        for line in read_file:
            self.todos.append(line.strip())
        read_file.close()

    def run(self):
        while True:
            input_text = "What would you like to do? Here are your options:"
            print(input_text)
            # print("Here are your options:")
            for x, y in enumerate(self.commands):
                print(f"{x + 1}: {y}")
            command = input(">>> ")
            if command == "quit":
                print("Goodbye!")
                sys.exit(0)
            elif command == "add":
                todo = input("What would you like to add? ")
                self.add(todo)
            elif command == "remove":
                self.print()
                index = int(input("What index would you like to remove? "))
                self.remove(index - 1)
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
