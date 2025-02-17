import os

print("Obecny folder:", os.getcwd())

# Stworz folder
os.makedirs("moj-folder", exist_ok=True)

# Zawartosc katalogu
print("Zawartosc katalogu:", os.listdir())

nazwa_pliku_txt = input("Podaj nazwe pliku txt (bez .txt): ")

if os.path.exists(f"{nazwa_pliku_txt}.txt"):
    with open(f"{nazwa_pliku_txt}.txt", "r") as f:
        output = f.read()
        print(output)
else:
    print(f"Plik {nazwa_pliku_txt}.txt nie istnieje")

print("Terminal size:", os.get_terminal_size())

imie = input("Jak masz na imię? : ")

print("-" * os.get_terminal_size().columns)
print(f"Witaj {imie} :) ! ".center(os.get_terminal_size().columns))
print("Miło Cię widzieć! ".center(os.get_terminal_size().columns))
print("-" * os.get_terminal_size().columns)