import json
import sys


class Coin:
    def __init__(self):
        self.sides = {"heads": 0, "tails": 0}
        self.commands = {
            "heads": lambda: self.toss("heads"),
            "tails": lambda: self.toss("tails"),
            "percentage": self.percentage,
            "save": self.save,
            "load": self.load,
            "exit": sys.exit,
        }

    def toss(self, side):
        self.sides[side] += 1

    def percentage(self):
        total = self.sides["heads"] + self.sides["tails"]
        if total == 0:
            print("No tosses yet!")
        heads_percentage = self.sides["heads"] / total * 100
        tails_percentage = self.sides["tails"] / total * 100
        print(f"Heads: {heads_percentage:.2f}% with {self.sides['heads']} tosses")
        print(f"Tails: {tails_percentage:.2f}% with {self.sides['tails']} tosses")

    def save(self):
        with open("coin.json", "w") as file:
            json.dump(self.sides, file)

    def load(self):
        with open("coin.json", "r") as file:
            self.sides = json.load(file)

    def run(self):
        while True:
            print("What would you like to do? Here are your options:")
            for x, y in enumerate(list(self.commands.keys())):
                print(f"{x + 1}: {y}")
            command = input(">>> ")

            if command in self.commands:
                self.commands[command]()
            else:
                print("Sorry, I don't understand that command.")


def main():
    coin = Coin()
    coin.run()


main()
