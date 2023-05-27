import PySimpleGUI as sg

files_label = sg.Text("Select files to compress:")
file_location = sg.InputText(tooltip="Enter file location")
files_button = sg.Button("Choose")

destination_label = sg.Text("Select destination folder:")
destination_location = sg.InputText(tooltip="Enter destination folder")
destination_button = sg.Button("Choose")

compress_button = sg.Button("Compress")

location_layout = [files_label, file_location, files_button]
destination_layout = [destination_label, destination_location, destination_button]

title = "File Compressor"

window = sg.Window(
    title=title,
    layout=[
        [
            location_layout,
            destination_layout,
        ],
        [
            compress_button,
        ],
    ],
)

window.read()
window.close()
