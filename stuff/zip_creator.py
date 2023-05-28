import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as zip:
        file = pathlib.Path(file)
        for file in filepaths:
            zip.write(file, arcname=file.name)


if __name__ == "__main__":
    make_archive(filepaths=["zip_creator.py", "bonus_example.py"], dest_dir="dest")
