# waiting_list = ["john", "marry"]
# name = input("Enter name: ")

# number = waiting_list.index(name)
# print(f"{name}'s turn is {number}")

waiting_list = ["john", "marry"]
name = input("Enter name: ")
try:
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")

except ValueError:
    print(f"{name} not in waiting list")
