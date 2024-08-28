# Zadanie 4: Liczby podzielne przez 3
# Opis: Napisz program, który użyje pętli while, aby wypisać wszystkie liczby od 1 do 30, które są podzielne przez 3.

liczba = 1

while liczba <= 30:
    if liczba % 3 == 0:
        print(liczba)
    liczba += 1
