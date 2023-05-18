import random
import string  # for string constants
import sys  # for sys.exit()

strength = {}


def strength_checker(password):
    if len(password) < 8:
        strength["length"] = False
    else:
        strength["length"] = True

    if not any(char.isupper() for char in password):
        strength["uppercase"] = False
    else:
        strength["uppercase"] = True

    if not any(char.islower() for char in password):
        strength["lowercase"] = False
    else:
        strength["lowercase"] = True

    if not any(char.isdigit() for char in password):
        strength["digit"] = False
    else:
        strength["digit"] = True

    if not any(char in string.punctuation for char in password):
        strength["special"] = False
    else:
        strength["special"] = True


while True:
    password = input("Enter a password: ")
    strength_checker(password)
    print(strength)
    if all(strength.values()):
        print("Your password is strong enough.")
        break
    else:
        print("Your password is not strong enough.")
        print(
            "Please include at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character."
        )
        strength = {}
        continue
