def save_biodata(filename, data):
    with open(filename, "w") as file:
        for key, value in data.items():
            print(f"{key}: {value}", file=file)


# Collect user inputs
data = {}
data["Name"] = input("Enter your Name: ")
data["Civil Status"] = input("Enter your Civil Status: ")
data["Gender"] = input("Enter your Gender: ")
data["Birthdate"] = input("Enter your Birthdate: ")
data["Age"] = input("Enter your Age: ")
data["Birthplace"] = input("Enter your Birthplace: ")
data["Birth Country"] = input("Enter your Birth Country: ")
data["Street, Barangay"] = input("Enter your Street, Barangay: ")
data["Municipality, Province"] = input("Enter your Municipality, Province: ")
data["Mobile Number"] = input("Enter your Mobile Number: ")
data["Email Address"] = input("Enter your Email Address: ")
data["Nationality"] = input("Enter your Nationality: ")
data["Is Working-Student?"] = input("Enter if you are a Working Student (Yes/No): ")
data["Course"] = input("Enter your Course: ")
data["Name of the last school attended"] = input(
    "Enter the Name of the last school attended: "
)
data["Guardian's Name"] = input("Enter your Guardian's Name: ")
data["Are you a new student?"] = input("Are you a new student? (Yes/No): ")
data["Are you a shifter?"] = input("Are you a shifter? (Yes/No): ")
data["Are you a transferee?"] = input("Are you a transferee? (Yes/No): ")
data["Do you love programming so far?"] = input(
    "Do you love programming so far? (Yes/No): "
)

# Generate a unique ID number based on the Name and Birthdate (you can replace this with an actual algorithm)
id_number = data["Name"].split()[0].lower() + data["Birthdate"].replace("-", "")

# Save data to a text file with the unique ID number as the filename
filename = f"{id_number}.txt"
save_biodata(filename, data)

print("Biodata saved successfully.")
