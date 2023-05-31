import functions
import PySimpleGUI as sg
import time

sg.theme("DarkAmber")

# now = time.strftime("%b %d, %Y %H:%M:%S")
clock = sg.Text("", key="clock")
label = sg.Text("Enter a to-do item")
input_box = sg.InputText(tooltip="Enter a task", key="todo")
# add_button = sg.Button("Add")
add_button = sg.Button(
    image_source="plus.png",
    key="Add",
    tooltip="Add a task",
    size=10,
    mouseover_colors="red",
)

list_box = sg.Listbox(
    values=functions.get_todos(),
    key="todos",
    enable_events=True,
    size=[45, 10],
    size=[45, 10],
)

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window(
    "My To-Do App",
    layout=[
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button],
    ],
    font=("Helvetica", 20),
)

while True:
    now = time.strftime("%b %d, %Y %H:%M:%S")
    event, values = window.read(timeout=10)
    window["clock"].update(value=now)
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
            try:
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
            except IndexError:
                sg.popup("Please select a to-do item to edit", font=("Helvetica", 20))

            else:
                print(f"Edited {selected_todo}")
            finally:
                window["todo"].update(value="")

        case "Complete":
            try:
                todo_to_complete = values.get("todos")[0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup(
                    "Please select a to-do item to complete", font=("Helvetica", 20)
                )
            else:
                print(f"Completed {todo_to_complete}")
            finally:
                window["todo"].update(value="")

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values.get("todos")[0])


window.close()
