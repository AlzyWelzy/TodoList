import time

cur_year = int(time.strftime("%Y"))


def calculate_age(birth_year):
    age = cur_year - birth_year
    return age


birth_year = int(input("What year were you born? "))
years_old = calculate_age(birth_year)
print(f"You are {years_old} years old.")

if years_old > 120:
    print("You are the oldest person alive! I have ever seen!")
else:
    print("You are not the oldest person alive! I have ever seen!")
