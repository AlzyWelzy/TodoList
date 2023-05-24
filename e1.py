import glob

myfiles = glob.glob("*.py")
print(myfiles)


for file in myfiles:
    print(f">>> Contents of {file}:")
    with open(file, "r") as f:
        print(f.read())
