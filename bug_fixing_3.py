def speed(distance, time):
    return distance / time


print(speed([200, 4]))
print(speed(*[200, 4]))

print(speed([5, 300]))
print(speed([300, 5]))
print(speed(*[300, 5]))
