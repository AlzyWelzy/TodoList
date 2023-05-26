import csv

with open("some_stuff.csv", "r") as f:
    reader = csv.reader(f)
    # for row in reader:
    #     print(row)

    reader_list = list(reader)
    print(reader_list)
city = input("Enter a city: ").lower()

for cities in reader_list:
    if city in cities:
        # print(cities)
        # print(f"Found {city} in {cities}")
        print(f"{city.capitalize()} has {cities[1]} million people")
        break
    else:
        continue
else:
    print("Not found")
