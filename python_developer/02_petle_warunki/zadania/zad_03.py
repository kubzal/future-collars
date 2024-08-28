# Zadanie 3: Suma liczb od 1 do N
# Opis: Napisz program, który obliczy sumę wszystkich liczb od 1 do N, gdzie N jest podane przez użytkownika.

n = int(input("Podaj liczbę N: "))
suma = 0

for i in range(1, n + 1):
    suma += i

print(f"Suma liczb od 1 do {n} wynosi: {suma}")
