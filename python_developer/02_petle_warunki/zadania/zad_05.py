# Zadanie 5: Sprawdź, czy liczba jest dodatnia, ujemna, czy zero
# Opis: Napisz program, który pobierze od użytkownika liczbę i sprawdzi, czy jest ona dodatnia, ujemna, czy jest zerem.

liczba = float(input("Podaj liczbę: "))

if liczba > 0:
    print(f"{liczba} jest dodatnia.")
elif liczba < 0:
    print(f"{liczba} jest ujemna.")
else:
    print("Liczba jest zerem.")
