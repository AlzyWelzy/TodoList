"""Created a speed functon that takes in a list of two numbers, distance and time, and returns the speed."""


def speed(distance, time):
    return distance / time


# print(speed([200, 4]))
print(speed(*[200, 4]))

# print(speed([5, 300]))
# print(speed([300, 5]))
print(speed(*[300, 5]))
