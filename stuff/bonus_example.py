import PySimpleGUI as sg
from zip_creator import make_archive

files_label = sg.Text("Select files to compress:")
# file_location = sg.InputText(tooltip="Enter file location")
file_location = sg.Input(tooltip="Enter file location")
files_button = sg.FilesBrowse("Choose", key="files")

destination_label = sg.Text("Select destination folder:")
destination_location = sg.Input(tooltip="Enter destination folder")
destination_button = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
# output_label = sg.Text("Output: ", key="output")
output_label = sg.Text(key="output")

location_layout = [files_label, file_location, files_button]
destination_layout = [destination_label, destination_location, destination_button]
comp_output_layout = [compress_button, output_label]

title = "File Compressor"

window = sg.Window(
    title=title,
    layout=[
        location_layout,
        destination_layout,
        comp_output_layout,
    ],
)

while True:
    event, values = window.read()
    print(event, values)
    print(type(values))
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths=filepaths, dest_dir=folder)
    window["output"].update("Done!")

window.close()
