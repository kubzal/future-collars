# Zadanie 7: Masz dwa zbiory liczb:
# A = {1, 2, 3, 4, 5, 6}
# B = {4, 5, 6, 7, 8, 9}
#  - Znajdź sumę zbiorów A i B (wszystkie unikalne elementy).
#  - Znajdź elementy wspólne obu zbiorów.
#  - Znajdź elementy, które należą tylko do jednego z tych zbiorów (różnica symetryczna).

A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}

# Suma zbiorów A i B
suma_zbiorow = A.union(B)

# Zbiór wspólny
zbior_wspolny = A.intersection(B)

# Różnica symetryczna
roznica_symetryczna = A.symmetric_difference(B)

print("Suma zbiorów:", suma_zbiorow)
print("Zbiór wspólny:", zbior_wspolny)
print("Różnica symetryczna:", roznica_symetryczna)
