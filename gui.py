import functions
import PySimpleGUI as sg
import time


label = sg.Text("Enter a to-do item")
input_box = sg.InputText(tooltip="Enter a task", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(
    values=functions.get_todos(),
    key="todos",
    enable_events=True,
    size=([45, 10]),
)

edit_button = sg.Button("Edit")

window = sg.Window(
    "My To-Do App",
    layout=[[label], [input_box, add_button], [list_box, edit_button]],
    font=("Helvetica", 20),
)

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case sg.WIN_CLOSED:
            break

        case "Add":
            todos = functions.get_todos()
            new_todo = values.get("todo")
            todos.append(f"{new_todo}\n")
            functions.write_todos(todos)
            print(f"Added {new_todo}")
            window["todos"].update(values=todos)

        case "Edit":
            todos = functions.get_todos()
            selected_todo = values.get("todos")[0]
            new_todo = sg.popup_get_text(
                "Edit to-do item",
                default_text=selected_todo,
            )
            todos.remove(selected_todo)
            todos.append(f"{new_todo}\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values.get("todos")[0])


window.close()
