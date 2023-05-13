temperatures = [10, 12, 14]

file = open("file.txt", "w")

file.writelines(str(temperatures))

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)

with open("dump_file.txt", "w") as file:
    file.writelines("Hello You!")

with open("dump_file.txt", "r") as file:
    content = file.read()
    print(content)
    print(type(content))
    print(len(content))
