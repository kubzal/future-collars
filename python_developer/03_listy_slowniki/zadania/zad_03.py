# Zadanie 3: Masz krotkę `dane` zawierającą dane osoby:
# ("Jan", "Kowalski", 32, "Warszawa").
# - Wyświetl imię i nazwisko.
# - Zamień miasto na "Kraków" (stwórz nową krotkę).
# - Wyświetl nową krotkę.

dane = ("Jan", "Kowalski", 32, "Warszawa")

# Wyświetl imię i nazwisko
print("Imię:", dane[0], "Nazwisko:", dane[1])

# Zmień miasto na Kraków
nowe_dane = (dane[0], dane[1], dane[2], "Kraków")
print("Nowe dane:", nowe_dane)
