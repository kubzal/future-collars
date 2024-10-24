import csv


def csv_reader(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            yield row


# Using the generator
for row in csv_reader("przykladowy.csv"):
    print(row)

print()
print("-" * 100)
print()

# Using next()
csv_gen = csv_reader("przykladowy.csv")

# Fetch the first row
print("First row:\t", next(csv_gen))
print("Second row:\t", next(csv_gen))
print("Third row:\t", next(csv_gen))
