import os
import csv


def load_data():
    """
    Funkcja do wczytywania danych
    """
    file_path = os.path.join("data", "pracownicy.csv")

    with open(file_path, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    return data

def pretty_print(data):
    """
    Funkcja do drukowania ladnej tabelki w konsoli
    """
    print("\n")

    max_lengths = []

    for col in range(len(data[0])):
        max_col_length = 0
        for row in data:
            max_col_length = max(max_col_length, len(row[col]))
        max_lengths.append(max_col_length)

    # przechodzimy po wierszach tabeli
    for row in data:
        text = ""

        # dodajemy komorki do wiersza tabeli
        for i, cell in enumerate(row):
            text = text + "\t" + str(cell).ljust(max_lengths[i])
        print(text)

def modify_data(data, row, col, new_value):
    """
    Zmiana wartosci w tabeli
    """
    if validate_cooridnates(data, row, col):
        data[row][col] = new_value
    return data

def validate_cooridnates(data, row, col):
    if row < 0 or row >= len(data):
        print("Podano bledny nr wiersza")
        return False

    if col < 0 or col >= len(data[0]):
        print("Podano bledny numer kolumny")
        return False

    return True

def save_data(data, file_path):
    with open(file_path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def main():
    print("Witaj w programie Mini Table Editor!")

    # Wczytanie danych
    data = load_data()

    # Drukowanie tabeli
    pretty_print(data)

    # Modyfikowanie tabeli
    data = modify_data(data=data,row=5, col=1, new_value="Jakub Zalewski")

    # Ponowne wydrukowanie danych
    pretty_print(data)

    # Zapisanie danych
    save_data(data=data, file_path=os.path.join("data", "pracownicy_modified.csv"))


if __name__ == "__main__":
    main()