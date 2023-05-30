# FILEPATH = "todos_item.txt"
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Return a list of todos from a file"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write todos to a file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions.py")
    print(get_todos())
