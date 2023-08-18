# elements = ["a", "b", "c"]
# new = "x"
# new = elements[1]
# print(elements)

elements = ["a", "b", "c"]
print(elements)
elements = [i.replace("b", "x") for i in elements]
print(elements)
