import csv
import json
import pickle

# Sample data
data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"},
    {"name": "Charlie", "age": 22, "city": "Chicago"}
]

# Writing and reading CSV
csv_file = "data.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(data)

with open(csv_file, mode="r") as file:
    reader = csv.DictReader(file)
    csv_data = [row for row in reader]
    print("CSV Data (DictReader):", csv_data)

# Basic CSV reader (non-DictReader)
with open(csv_file, mode="r") as file:
    reader = csv.reader(file)
    csv_basic_data = [row for row in reader]
    print("CSV Data (Basic Reader):", csv_basic_data)


# Writing and reading JSON
json_file = "data.json"
with open(json_file, mode="w") as file:
    json.dump(data, file, indent=4)

with open(json_file, mode="r") as file:
    json_data = json.load(file)
    print("JSON Data:", json_data)

# Writing and reading Pickle
pkl_file = "data.pkl"
with open(pkl_file, mode="wb") as file:
    pickle.dump(data, file)

with open(pkl_file, mode="rb") as file:
    pkl_data = pickle.load(file)
    print("Pickle Data:", pkl_data)