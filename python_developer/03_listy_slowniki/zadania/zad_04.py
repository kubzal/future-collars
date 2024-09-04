# Zadanie 4: Masz listę krotek, gdzie każda krotka zawiera współrzędne punktu na
# płaszczyźnie: punkty = [(3, 4), (1, 2), (5, 6), (2, 8), (7, 1)].
# Zamień wszystkie krotki tak, aby każdy punkt był reprezentowany jako (y, x)
# (zamień współrzędne miejscami). Wyświetl listę punktów po zamianie współrzędnych.

punkty = [(3, 4), (1, 2), (5, 6), (2, 8), (7, 1)]
print("Lista punktów przed zamianą współrzędnych:", punkty)

# Zamiana współrzędnych (x, y) na (y, x)
zamienione_punkty = []
for punkt in punkty:
    zamienione_punkty.append((punkt[1], punkt[0]))

# Wyświetlenie wynikowej listy punktów
print("Lista punktów po zamianie współrzędnych:", zamienione_punkty)
