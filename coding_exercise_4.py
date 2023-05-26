import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_number = random.randint(lower_bound, upper_bound)

print("I'm thinking of a number between", lower_bound, "and", upper_bound)

guess = int(input("Enter your guess: "))

while guess != random_number:
    if guess < random_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Enter your guess: "))
else:
    print("You got it!")
