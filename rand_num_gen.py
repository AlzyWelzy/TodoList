import random

RANDOM_RANGE = (1, 100)
HIGH_SCORE_FILE = "hiscore.txt"


def generate_random_int():
    return random.randint(*RANDOM_RANGE)


def get_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read())
    except (IOError, ValueError):
        return 0


def set_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))


def game():
    random_int = generate_random_int()
    high_score = get_high_score()
    print(
        f"Try to guess the random number between {RANDOM_RANGE[0]} and {RANDOM_RANGE[1]}."
    )
    print(f"Your current high score is {high_score}.")

    for i in range(1, RANDOM_RANGE[1]):
        try:
            user_int = int(input(f"Enter your guess ({i}/{RANDOM_RANGE[1]}): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if user_int == random_int:
            print(f"CORRECT! You guessed the random number in {i} guesses.")
            break
        elif user_int < random_int:
            print("Too low!")
        else:
            print("Too high!")
    else:
        print(
            f"You failed to guess the random number ({random_int}) within {RANDOM_RANGE} guesses."
        )

    if i < high_score:
        print(f"You broke your high score of {high_score} with a score of {i}!")
        set_high_score()


game()
