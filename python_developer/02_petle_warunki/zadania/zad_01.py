# Zadanie 1: Sprawdź, czy liczba jest parzysta czy nieparzysta
# Opis: Napisz program, który pobierze od użytkownika liczbę i sprawdzi, czy jest ona parzysta czy nieparzysta.
# Wynik wyświetl na ekranie.

liczba = int(input("Podaj liczbę: "))

if liczba % 2 == 0:
    print(f"{liczba} jest parzysta.")
else:
    print(f"{liczba} jest nieparzysta.")
