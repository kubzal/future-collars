# Zadanie 6: Masz słownik przedstawiający liczbę punktów zdobytych przez drużyny:
# punkty = {"druzyna_A": 10, "druzyna_B": 8, "druzyna_C": 12}
# - Zwiększ punkty drużyny "druzyna_A" o 3.
# - Dodaj nową drużynę "druzyna_D" z punktami 9.
# - Wyświetl sumę wszystkich punktów.

punkty = {"druzyna_A": 10, "druzyna_B": 8, "druzyna_C": 12}

# Zwiększ punkty drużyny_A o 3
punkty["druzyna_A"] += 3

# Dodaj nową drużynę druzyna_D
punkty["druzyna_D"] = 9

# Oblicz sumę wszystkich punktów
suma_punktow = sum(punkty.values())

print("Suma punktów:", suma_punktow)
