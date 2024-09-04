# Zadanie 2: Masz listę imion ["Ala", "Ola", "Ewa", "Jan", "Adam", "Olek"].
# Wykonaj następujące kroki:
# - Posortuj listę alfabetycznie.
# - Utwórz nową listę zawierającą imiona dłuższe niż 3 litery.
# - Wyświetl nową listę.

imiona = ["Ala", "Ola", "Ewa", "Jan", "Adam", "Olek"]

# Posortuj listę alfabetycznie
imiona.sort()

# Utwórz nową listę z imionami dłuższymi niż 3 litery
nowe_imiona = []
for imie in imiona:
    if len(imie) > 3:
        nowe_imiona.append(imie)

# Wyświetl nową listę
print("Imiona dłuższe niż 3 litery:", nowe_imiona)

# --------------------------------------------------------------------
# Rozwiązanie z wykorzystaniem list comprehension
# --------------------------------------------------------------------

imiona = ["Ala", "Ola", "Ewa", "Jan", "Adam", "Olek"]

# Posortuj listę alfabetycznie
imiona.sort()

# Utwórz nową listę z imionami dłuższymi niż 3 litery

nowe_imiona = [imie for imie in imiona if len(imie) > 3]

# Wyświetl nową listę
print("Imiona dłuższe niż 3 litery:", nowe_imiona)
