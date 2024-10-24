# Program do obliczania Największego Wspólnego Dzielnika (NWD)
# Program do obliczania Najmniejszej Wspólnej Wielokrotności (NWW)

# Wprowadzenie liczb od użytkownika
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

# Algorytm Euklidesa do obliczania NWD (konieczny do obliczenia NWW)
a = liczba1
b = liczba2

while b != 0:
    temp = b
    b = a % b
    a = temp

najwiekszy_wspolny_dzielnik = a

# Wyświetlenie wyniku
print(f"NWD liczb {liczba1} i {liczba2} wynosi: {najwiekszy_wspolny_dzielnik}")

# Obliczanie NWW na podstawie wzoru: NWW(a, b) = |a * b| / NWD(a, b)
najmniejsza_wspolna_wielokrotnosc = (
    abs(liczba1 * liczba2) // najwiekszy_wspolny_dzielnik
)

# Wyświetlenie wyniku
print(f"NWW liczb {liczba1} i {liczba2} wynosi: {najmniejsza_wspolna_wielokrotnosc}")
