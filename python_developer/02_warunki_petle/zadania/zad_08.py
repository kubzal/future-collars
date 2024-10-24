# Zadanie 8: Napisz program, który wypisze pierwsze n liczb naturalnych w kolejności
# rosnącej i malejącej w osobnych kolumnach.

## FOR

# Wprowadzenie liczby n przez użytkownika
n = int(input("Podaj liczbę n: "))

# Nagłówki kolumn
print("Rosnąco | Malejąco")
print("-" * 18)

# Pętla iterująca po liczbach od 1 do n
for i in range(1, n + 1):
    print(f"{i} \t | \t {n - i + 1}")


## WHILE

# Wprowadzenie liczby n przez użytkownika
n = int(input("Podaj liczbę n: "))

# Nagłówki kolumn
print("Rosnąco | Malejąco")
print("-" * 18)

# Inicjalizacja zmiennych do pętli
i = 1
j = n

# Pętla while iterująca po liczbach
while i <= n:
    print(f"{i}\t | \t{j}")
    i += 1
    j -= 1
