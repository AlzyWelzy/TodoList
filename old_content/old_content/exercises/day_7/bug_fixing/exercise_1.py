# temperatures = [10, 12, 14]

# file = open("file.txt", "w")

# file.writelines(temperatures)

temperatures = [10, 12, 14]

temperatures = [str(temperature) + "\n" for temperature in temperatures]

file = open("file.txt", "w")

file.writelines(temperatures)
