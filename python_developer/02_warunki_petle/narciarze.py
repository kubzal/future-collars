# Zadanie: Wagoniki kolejki linowej z narciarzami jadącymi na stok
#
# Opis:
# Napisz program, który obliczy, ile wagoników kolejki linowej będzie potrzebnych do
# przewiezienia grupy narciarzy na stok. Każdy wagonik może pomieścić maksymalnie 10
# par nart. Liczba narciarzy jest wczytywana na początku. Każdy narciarz ma od 1 do
# 3 par nart (losowana liczba). Narciarze wchodzą do wagoników po kolei, co oznacza,
# że wagoniki nie zawsze będą wypełnione optymalnie. Jeśli kolejny narciarz ma więcej
# par nart niż jest miejsc w wagoniku, musi wsiąść do następnego wagonika. Program
# oblicza, ile wagoników jest potrzebnych, aby przewieźć wszystkich narciarzy na stok.
#
# Założenia:
# 1. Na początku wczytywana jest liczba narciarzy.
# 2. Każdy narciarz ma losowo od 1 do 3 par nart.
# 3. Wagonik kolejki linowej może pomieścić maksymalnie 10 par nart.
# 4. Narciarze wchodzą do wagoników po kolei.
# 5. Program oblicza i wyświetla liczbę potrzebnych wagoników.

import random

DEBUG = True

# Wczytanie liczby narciarzy
liczba_narciarzy = int(input("Podaj liczbę narciarzy: "))

# Inicjalizacja zmiennych
laczna_liczba_par_nart = 0
liczba_wagonikow = 1  # Zaczynamy od pierwszego wagonika
aktualna_ilosc_nart_w_wagoniku = 0
najwiecej_nart = 0  # Zmienna do śledzenia największej liczby nart w wagoniku
nr_wagonika_najwiecej_nart = 1

print()

# Pętla, która dla każdego narciarza losuje liczbę par nart i umieszcza je w wagoniku
for i in range(liczba_narciarzy):
    liczba_par_nart = random.randint(1, 3)  # Losowanie liczby par nart (1-3)
    laczna_liczba_par_nart += liczba_par_nart

    if DEBUG:
        print(f"Narciarz {i + 1}: {liczba_par_nart} par nart")

    # Sprawdzenie, czy narciarz zmieści się w aktualnym wagoniku
    if aktualna_ilosc_nart_w_wagoniku + liczba_par_nart > 10:
        print(
            f"\nWagonik {liczba_wagonikow} zapełniony: {aktualna_ilosc_nart_w_wagoniku} par nart\n"
        )

        # Sprawdzenie, czy ten wagonik miał najwięcej nart
        if aktualna_ilosc_nart_w_wagoniku > najwiecej_nart:
            najwiecej_nart = aktualna_ilosc_nart_w_wagoniku
            nr_wagonika_najwiecej_nart = liczba_wagonikow

        # Jeśli się nie zmieści, potrzebny jest nowy wagonik
        liczba_wagonikow += 1
        aktualna_ilosc_nart_w_wagoniku = liczba_par_nart
    else:
        # Jeśli się zmieści, dodajemy narty do aktualnego wagonika
        aktualna_ilosc_nart_w_wagoniku += liczba_par_nart

# Wyświetlenie nart w ostatnim wagoniku
print(
    f"\nWagonik {liczba_wagonikow} zapełniony: {aktualna_ilosc_nart_w_wagoniku} par nart\n"
)

# Sprawdzenie ostatniego wagonika, czy miał najwięcej nart
if aktualna_ilosc_nart_w_wagoniku > najwiecej_nart:
    najwiecej_nart = aktualna_ilosc_nart_w_wagoniku
    nr_wagonika_najwiecej_nart = liczba_wagonikow

# Wyświetlenie wyników końcowych
print(f"\nLiczba narciarzy: {liczba_narciarzy}")
print(f"Liczba potrzebnych wagoników: {liczba_wagonikow}")
print(
    f"Wagonik z największą liczbą nart: {nr_wagonika_najwiecej_nart} ({najwiecej_nart} par nart)"
)
