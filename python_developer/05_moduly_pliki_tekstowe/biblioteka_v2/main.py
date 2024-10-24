# Zadanie: Program obsługujący prostą bibliotekę
#
# Umożliwia wprowadzanie książek, wypożyczanie, sprawdzanie dostępności,
# wyświetlanie listy książek oraz historii akcji.
# Program działa w pętli, pozwalając użytkownikowi na wprowadzanie komend
# takich jak:
# 1. WPROWADZ - Wprowadzenie nowych książek do biblioteki
# 2. WYPOZYCZ - Wypożyczenie książek z biblioteki
# 3. KSIAZKI - Wyświetlenie wszystkich książek i liczby dostępnych sztuk
# 4. DOSTEPNOSC - Sprawdzenie, czy dana książka jest dostępna w bibliotece
# 5. UNIKALNE - Wyświetlenie liczby unikalnych tytułów w bibliotece
# 6. LICZBA - Wyświetlenie łącznej liczby książek (woluminów) w bibliotece
# 7. HISTORIA - Wyświetlenie historii wszystkich operacji na książkach
# 8. POMOC - Wyświetlenie dostępnych komend
# 9. KONIEC - Zakończenie działania programu

# # Inicjalizacja zmiennych
# ksiazki = {
#     "Harry Potter i Kamień Filozoficzny": 3,
#     "Władca Pierścieni Druzyna Pierścienia": 5,
#     "Buszujący w zbożu": 4,
#     "Bezcenny": 1,
#     "Glukozowa rewolucja": 2,
# }  # Słownik z początkowymi książkami i liczbą sztuk

from utils import (
    wczytaj_ksiazki,
    wprowadz_ksiazke,
    wypozycz_ksiazke,
    wyswietl_dostepnosc,
    wyswietl_historie,
    wyswietl_liczbe_woluminow,
    wyswietl_pomoc,
    wyswietl_powitanie,
    zapisz_historie,
)

historia = []  # Lista do przechowywania historii operacji
ksiazki = wczytaj_ksiazki()

# Wyświetl powitanie
wyswietl_powitanie()

# Główna pętla programu
while True:
    log_message = ""

    # Pobieranie komendy od użytkownika
    komenda = input("\nPodaj komendę: ").upper()
    print(f"Wpisałeś komendę: {komenda}")

    if komenda == "WPROWADZ":
        ksiazki, log_message = wprowadz_ksiazke(ksiazki)

    elif komenda == "WYPOZYCZ":
        ksiazki, log_message = wypozycz_ksiazke(ksiazki)

    elif komenda == "KSIAZKI":
        if ksiazki:
            print("Lista książek i liczba dostępnych sztuk:")
            for tytul, liczba in ksiazki.items():
                print(f"- {tytul}: {liczba} szt.")
        else:
            print("Biblioteka jest pusta.")

    elif komenda == "DOSTEPNOSC":
        log_message = wyswietl_dostepnosc(ksiazki)

    elif komenda == "UNIKALNE":
        liczba_unikalnych = len(ksiazki)
        print(f"Liczba unikalnych tytułów w bibliotece: {liczba_unikalnych}")

    elif komenda == "LICZBA":
        log_message = wyswietl_liczbe_woluminow(ksiazki)

    elif komenda == "HISTORIA":
        log_message = wyswietl_historie(historia)

    elif komenda == "POMOC":
        log_message = wyswietl_pomoc()

    elif komenda == "KONIEC":
        print("Zakończenie programu.")

        zapisz_historie(historia)  # Zapisanie historii do pliku
        break

    else:
        print("Nieznana komenda. Wpisz 'POMOC', aby wyświetlić listę komend.")
        log_message = "Nieznana komenda."

    # Dodanie komunikatu do historii
    historia.append(log_message)
