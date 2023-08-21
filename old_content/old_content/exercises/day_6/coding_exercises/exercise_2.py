filenames = ["doc.txt", "report.txt", "presentation.txt"]

for filename in filenames:
    with open(filename, "w") as file:
        file.write(f"Hello")
    with open(filename) as file:
        print(file.read())
