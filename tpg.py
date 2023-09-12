import random


class ThePerfectGuess:
    def __init__(self):
        self.RANDOM_RANGE = (1, 100)
        self.HIGH_SCORE_FILE = "hiscore.txt"

    def generate_random_int(self):
        return random.randint(*self.RANDOM_RANGE)

    def get_high_score(self):
        try:
            with open(self.HIGH_SCORE_FILE, "r") as f:
                return int(f.read())
        except (IOError, ValueError):
            return 0

    def set_high_score(self, score):
        with open(self.HIGH_SCORE_FILE, "r") as f:
            f.write(str(score))

    def game(self):
        random_int = self.generate_random_int()
        high_score = self.get_high_score()
        print(
            f"Try to guess the random number between {self.RANDOM_RANGE[0]} and {self.RANDOM_RANGE[1]}."
        )
        print(f"Your current high score is {high_score}.")

        for i in range(1, self.RANDOM_RANGE[1]):
            try:
                user_int = int(
                    input(f"Enter your guess ({i}/{self.RANDOM_RANGE[1]}): ")
                )
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
                f"You failed to guess the random number ({random_int}) within {self.RANDOM_RANGE} guesses."
            )

        if i < high_score:
            print(f"You broke your high score of {high_score} with a score of {i}!")
            self.set_high_score()


def main():
    tpg = ThePerfectGuess()
    tpg.game()


if __name__ == "__main__":
    main()
