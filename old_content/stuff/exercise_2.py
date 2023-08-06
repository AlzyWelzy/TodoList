class PercentageCalculator:
    def __init__(self):
        pass

    def calculate(self):
        while True:
            try:
                num1 = int(input("Enter total value: "))
                num2 = int(input("Enter value: "))
                if num1 is 0:
                    print("Please enter a number other than 0.")
                    print("Your total value cannot be 0.")
                    continue
                if num2 > num1:
                    print("Please enter a number smaller than your total value.")
                    continue
                percentage = float((num2 / num1) * 100)
                print(f"{num2} is {percentage}% of {num1}")
                print(f"That is {percentage}%")
                break
            except ValueError:
                print("Please enter a valid number.")
                continue
            except ZeroDivisionError:
                print("Please enter a number other than 0.")
                continue


something = PercentageCalculator()
something.calculate()
