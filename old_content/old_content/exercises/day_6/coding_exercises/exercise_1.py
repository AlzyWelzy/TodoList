file = open("./members.txt")

with file as f:
    for line in f:
        print(line.strip())
file.close()

usr_inp = input("Enter a name that you want to append to the file: ")

file = open("./members.txt", "a")

with file as f:
    f.write(usr_inp)

f.close()

file = open("./members.txt")

with file as f:
    for line in f:
        print(line.strip())
f.close()
