def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(h=100)
print(time)