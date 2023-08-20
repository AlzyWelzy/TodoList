# elements = ["a", "b", "c"]
# new = "x"
# new = elements[1]
# print(elements)

elements = ["a", "b", "c"]

print(elements)

# elements = [i.replace("b", "x") for i in elements]
# print(elements)

new_elements = []
for element in elements:
    if element == "b":
        new_elements.append("x")
        continue
    new_elements.append(element)

print(new_elements)
