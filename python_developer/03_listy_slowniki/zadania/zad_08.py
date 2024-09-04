# Zadanie 8: Masz dwa zbiory imion:
# A = {"Anna", "Kasia", "Ola", "Jan"}
# B = {"Jan", "Marek", "Ola", "Ewa"}
# - Znajdź imiona, które są wspólne dla obu zbiorów.
# - Usuń z pierwszego zbioru imiona, które są w drugim zbiorze.

A = {"Anna", "Kasia", "Ola", "Jan"}
B = {"Jan", "Marek", "Ola", "Ewa"}

# Imiona wspólne dla obu zbiorów
wspolne_imiona = A.intersection(B)

# Usuń z A imiona, które są w B
A.difference_update(B)

print("Wspólne imiona:", wspolne_imiona)
print("Zbiór A po usunięciu wspólnych imion:", A)
