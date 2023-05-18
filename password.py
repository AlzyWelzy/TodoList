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

# What is 1001 Arabic Nights?
# A collection of Middle Eastern folk tales compiled in Arabic during the Islamic Golden Age.
# It is often known in English as the Arabian Nights, from the first English language edition (1706), which rendered the title as The Arabian Nights' Entertainment.
# The work was collected over many centuries by various authors, translators, and scholars across West, Central, and South Asia and North Africa.
# The tales themselves trace their roots back to ancient and medieval Arabic, Persian, Mesopotamian, Indian, Jewish, and Egyptian folklore and literature.
# In particular, many tales were originally folk stories from the Caliphate era, while others, especially the frame story, are most probably drawn from the Pahlavi Persian work Hazār Afsān (Persian: هزار افسان‎, lit. A Thousand Tales) which in turn relied partly on Indian elements.
# What is the frame story?
# The frame story of Scheherazade telling stories over a thousand nights to save her life from the Persian king Shahryar and the Persian queen Scheherazade.
# What is the frame story of the frame story?
# The frame story of the frame story is the Persian king Shahryar and the Persian queen Scheherazade.
# What kind of king is Shahryar?
# Shahryar is a Persian king who is betrayed by his wife. He then marries a new wife every day and kills her the next morning.
# What kind of queen is Scheherazade?
# Scheherazade is a Persian queen who tells stories to the king every night to save her life.
# what kind of stories does Scheherazade tell?
# Scheherazade tells stories about the Middle East.
# All of the stories are about the Middle East and is that true?
