import PySimpleGUI as sg

title = "Convertor"

feet_label = sg.Text("Enter Feet:")
feet_input = sg.Input()

inches_label = sg.Text("Enter Inches:")
inches_input = sg.Input()

convert_button = sg.Button("Convert")

window = sg.Window(
    title=title,
    layout=[[feet_label, feet_input], [inches_label, inches_input], [convert_button]],
)

window.read()
window.close()
