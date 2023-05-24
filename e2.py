import csv

with open("some_stuff.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

    # reader_list = list(reader)
    # print(reader_list)
