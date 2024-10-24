# Zadanie 3: Napisz program, który obliczy sumę wszystkich liczb od 1 do n, gdzie n jest
# podane przez użytkownika.

n = int(input("Podaj liczbę n: "))
suma = 0

for i in range(1, n + 1):
    suma += i

print(f"Suma liczb od 1 do {n} wynosi: {suma}")
