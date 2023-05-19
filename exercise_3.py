def get_max():
    grades = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    return max(grades)


print(get_max())


def get_min_max():
    grades = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    return f"Min: {min(grades)} Max: {max(grades)}"


print(get_min_max())
