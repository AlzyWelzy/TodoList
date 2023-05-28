import PySimpleGUI as sg

files_label = sg.Text("Select files to compress:")
# file_location = sg.InputText(tooltip="Enter file location")
file_location = sg.Input(tooltip="Enter file location")
files_button = sg.FilesBrowse("Choose", key="files")

destination_label = sg.Text("Select destination folder:")
destination_location = sg.Input(tooltip="Enter destination folder")
destination_button = sg.FolderBrowse("Choose", key="folder")

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

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values.get("files").split(";")
    folder = values.get("folder")

window.close()
