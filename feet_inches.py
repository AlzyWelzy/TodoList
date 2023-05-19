import string


def feet_inches():
    feet_inches_value = input("Enter the value in feet and inches: ").strip()
    if len(feet_inches_value.split(" ")) != 2:
        # feet = string.strip(feet_inches_value)
        feet = feet_inches_value.strip()
        print(feet)
        inches = 0
    else:
        print(feet_inches_value.split(" "))
        feet, inches = feet_inches_value.split(" ")
    inches = float(inches) + float(feet) * 12
    print(f"{feet_inches_value} is {inches} inches")
    return int(feet), int(inches)


feet_inches()
