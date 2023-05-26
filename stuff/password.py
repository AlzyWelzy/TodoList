import string  # for string constants


class PWD_Strength_Checker:
    def __init__(self):
        self.strength = {}

    def strength_checker(self, password):
        if len(password) < 8:
            self.strength["length"] = False
        else:
            self.strength["length"] = True

        if not any(char.isupper() for char in password):
            self.strength["uppercase"] = False
        else:
            self.strength["uppercase"] = True

        if not any(char.islower() for char in password):
            self.strength["lowercase"] = False
        else:
            self.strength["lowercase"] = True

        if not any(char.isdigit() for char in password):
            self.strength["digit"] = False
        else:
            self.strength["digit"] = True

        if not any(char in string.punctuation for char in password):
            self.strength["special"] = False
        else:
            self.strength["special"] = True

    def check_strength(self):
        while True:
            password = input("Enter a password: ")
            self.strength_checker(password)
            print(self.strength)
            if all(self.strength.values()):
                print("Your password is strong enough.")
                break
            else:
                print("Your password is not strong enough.")
                print(
                    "Please include at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character."
                )
                self.strength = {}
                continue


def main():
    pwd = PWD_Strength_Checker()
    pwd.check_strength()


if __name__ == "__main__":
    main()
