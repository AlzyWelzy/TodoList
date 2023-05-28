def feet_inches_2_meters(feet, inches):
    total_inches = (feet * 12) + inches
    meters = total_inches * 0.0254
    return meters


if __name__ == "__main__":
    print(feet_inches_2_meters(5, 11))
