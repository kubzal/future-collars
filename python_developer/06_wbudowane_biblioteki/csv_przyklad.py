import csv

with open("zwierzeta.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# print(zawartosc)