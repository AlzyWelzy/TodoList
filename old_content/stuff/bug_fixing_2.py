try:
    waiting_list = ["john", "marry"]
    name = input("Enter your name: ")

    number = waiting_list.index(name)
    print(f"{name} you are number {number+1} in the waiting list")
except ValueError:
    print(f"{name} you are not in the waiting list")
else:
    print("No error")
finally:
    print("Finally")
