# Zadanie 1: Utwórz listę liczby zawierającą liczby od 10 do 20 (włącznie).
# Następnie:
# - Usuń wszystkie liczby parzyste.
# - Policz sumę pozostałych liczb i wyświetl wynik.

liczby = list(range(10, 21))

# Usuń liczby parzyste (tworzenie nowej listy za pomocą pętli for)
nieparzyste = []
for liczba in liczby:
    if liczba % 2 != 0:
        nieparzyste.append(liczba)

# Policz sumę pozostałych liczb
suma = 0
for liczba in nieparzyste:
    suma += liczba

print("Suma liczb:", suma)

# --------------------------------------------------------------------
# Rozwiązanie z wykorzystaniem list comprehension
# --------------------------------------------------------------------

liczby = list(range(10, 21))

# Usuń liczby parzyste
liczby = [x for x in liczby if x % 2 != 0]

# Policz sumę pozostałych liczb
suma = sum(liczby)
print("Suma liczb:", suma)
