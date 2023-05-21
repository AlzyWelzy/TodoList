def names(s):
    return s.split(",")


usr_input = input("Enter names separated by commas: ")
print(names(usr_input))
names_list = names(usr_input)
len_names_list = len(names_list)
print(f"There are {len_names_list} names in the list.")
print(f"The first name is {names_list[0]} and the last name is {names_list[-1]}.")
print(f"The names in reverse order are {names_list[::-1]}.")
