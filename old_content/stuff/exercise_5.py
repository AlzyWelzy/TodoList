import string
import re


def strength_of_password(password):
    """Returns the strength of a password"""
    if (
        len(password) >= 8
        and any(char.isdigit() for char in password)
        and any(char.isupper() for char in password)
    ):
        return "Strong"
    else:
        return "Weak"


user_input = input("Enter a password: ")
print(strength_of_password(user_input))
