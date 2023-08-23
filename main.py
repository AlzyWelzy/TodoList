# Get the user's ID number
id_number = input("Enter your ID number: ")


# Function to get user input and format as <item name>: value
def get_input(item_name):
    return input(f"Enter your {item_name}: ")


# Collect user inputs
biodata = [
    "Name",
    "Civil Status",
    "Gender",
    "Birthdate",
    "Age",
    "Birthplace",
    "Birth Country",
    "Street, Barangay",
    "Municipality, Province",
    "Mobile Number",
    "Email Address",
    "Nationality",
    "Is Working-Student?",
    "Course",
    "Name of the last school attended",
    "Guardian's Name",
    "Are you a new student?",
    "Are you a shifter?",
    "Are you a transferee?",
    "Do you love programming so far?",
]

# Format and store biodata
formatted_biodata = ""
for item in biodata:
    user_input = get_input(item)
    formatted_biodata += f"{item}: {user_input}\n"

# Save biodata to a file
file_name = f"{id_number}.txt"
with open(file_name, "w") as file:
    file.write(formatted_biodata)

print("Biodata saved successfully.")


with open(file_name, "r") as file:
    print(file.read())
