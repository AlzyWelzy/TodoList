import PySimpleGUI as sq
import functionality

feet_label = sq.Text("Enter feet:")
feet_input = sq.Input(key="feet")

inches_label = sq.Text("Enter inches:")
inches_output = sq.Input(key="inches")

convert_button = sq.Button("Convert")
answer_label = sq.Text(key="answer")

feet_layout = [feet_label, feet_input]
inches_layout = [inches_label, inches_output]
convert_layout = [convert_button, answer_label]

title = "Feet to Inches Converter"

window = sq.Window(
    title=title,
    layout=[
        feet_layout,
        inches_layout,
        convert_layout,
    ],
)

while True:
    event, values = window.read()
    if event == sq.WIN_CLOSED:
        break

    feet = float(values["feet"])
    inches = float(values["inches"])
    answer = functionality.feet_inches_2_meters(feet, inches)
    window["answer"].update(answer)


window.close()
