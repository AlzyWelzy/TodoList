import time

cur_year = int(time.strftime("%Y"))


def calculate_age(birth_year):
    age = cur_year - birth_year
    return f"You are {age} years old."


birth_year = int(input("What year were you born? "))
print(calculate_age(birth_year=birth_year))
