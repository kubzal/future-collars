import csv
import json
import pickle


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        raise NotImplementedError("Metoda 'load' musi być zaimplementowana w klasie dziedziczącej.")

    def save(self, data):
        raise NotImplementedError("Metoda 'save' musi być zaimplementowana w klasie dziedziczącej.")


class CSVFileHandler(FileHandler):
    def load(self):
        with open(self.file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            return [row for row in reader]

    def save(self, data):
        with open(self.file_path, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)


# nowy_plik_csv = CSVFileHandler("nowy_plik.csv")
#
# dane = [["imie","nazwisko","miasto"],
# ["Jan","Kowalski","Warszawa"],
# ["Paweł","Nowak","Kraków"],
# ["Anna","Wiśniewska","Szczecin"]]
#
# # print(dane)
#
# nowy_plik_csv.save(dane)

class JSONFileHandler(FileHandler):
    def load(self):
        with open(self.file_path, "r") as json_file:
            return json.load(json_file)
    def save(self, data):
        with open(self.file_path, "w") as json_file:
            json.dump(data, json_file, indent=6)


plik_json = JSONFileHandler("plik.json")
# print(plik_json.load())

# dane_json = [
#   {"id": 100, "name":  "Jan Kowalski", "city":  "Warszawa"},
#   {"id": 200, "name":  "Konrad Pawłowski", "city":  "Kraków"},
#   {"id": 300, "name":  "Grażyna Nowak", "city":  "Poznań"}
# ]
#
# nowy_plik_json = JSONFileHandler("nowy_plik.json")
# nowy_plik_json.save(dane_json)

class PickleFileHandler(FileHandler):
    def load(self):
        with open(self.file_path, "rb") as pickle_file:
            return pickle.load(pickle_file)

    def save(self, data):
        with open(self.file_path, "wb") as pickle_file:
            pickle.dump(data, pickle_file)


# plik_pickle  = PickleFileHandler("plik.pkl")
#
# slownik = plik_json.load()[0]
# # print(slownik)
#
# plik_pickle.save(slownik)

nowy_pickle = PickleFileHandler("plik.pkl")

wczytany_slownik_z_pickle = nowy_pickle.load()

print(type(wczytany_slownik_z_pickle), wczytany_slownik_z_pickle)
