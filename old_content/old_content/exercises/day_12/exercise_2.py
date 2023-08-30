def strength(password):
    if len(password) >= 8 and has_numbers(password) and has_uppercase(password):
        return "Strong Password"
    elif len(password) >= 8 or has_numbers(password) or has_uppercase(password):
        return "Weak Password"


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def has_uppercase(inputString):
    return any(char.isupper() for char in inputString)


result = strength("123$Ankit")

print(result)
