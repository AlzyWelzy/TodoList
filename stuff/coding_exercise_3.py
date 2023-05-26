ice_temperature = 0
steam_temperature = 100


def water_temperature(temperature):
    if temperature <= ice_temperature:
        return "ice"
    elif temperature >= steam_temperature:
        return "steam"
    else:
        return "liquid"


temperature = float(input("Enter the temperature of water: "))
print(water_temperature(temperature))
