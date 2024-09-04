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

# Inicjalizacja zmiennych
ksiazki = {
    "Harry Potter i Kamień Filozoficzny": 3,
    "Władca Pierścieni Druzyna Pierścienia": 5,
    "Buszujący w zbożu": 4,
    "Bezcenny": 1,
    "Glukozowa rewolucja": 2,
}  # Słownik z początkowymi książkami i liczbą sztuk
historia = []  # Lista do przechowywania historii operacji


# Główna pętla programu
while True:
    # Pobieranie komendy od użytkownika
    komenda = input("\nPodaj komendę: ").upper()
    print(f"Wpisałeś komendę: {komenda}")

    if komenda == "WPROWADZ":
        tytul = input("Podaj tytuł książki: ")
        liczba = int(input("Podaj liczbę sztuk: "))
        if tytul in ksiazki:
            ksiazki[tytul] += liczba
        else:
            ksiazki[tytul] = liczba
        historia.append(f"Wprowadzono książkę: {tytul}, liczba: {liczba}")
        print(f"Wprowadzono książkę: {tytul}, liczba sztuk: {liczba}")

    elif komenda == "WYPOZYCZ":
        tytul = input("Podaj tytuł książki: ")
        liczba = int(input("Podaj liczbę sztuk do wypożyczenia: "))
        if tytul in ksiazki and ksiazki[tytul] >= liczba:
            ksiazki[tytul] -= liczba
            if ksiazki[tytul] == 0:
                del ksiazki[
                    tytul
                ]  # Usuwanie książki z biblioteki, jeśli liczba wynosi 0
            historia.append(f"Wypożyczono książkę: {tytul}, liczba: {liczba}")
            print(f"Wypożyczono książkę: {tytul}, liczba sztuk: {liczba}")
        else:
            print(
                f"Brak wystarczającej liczby sztuk książki: {tytul} lub nie ma jej w bibliotece."
            )

    elif komenda == "KSIAZKI":
        if ksiazki:
            print("Lista książek i liczba dostępnych sztuk:")
            for tytul, liczba in ksiazki.items():
                print(f"- {tytul}: {liczba} szt.")
        else:
            print("Biblioteka jest pusta.")

    elif komenda == "DOSTEPNOSC":
        tytul = input("Podaj tytuł książki: ")
        if tytul in ksiazki:
            print(f"Książka '{tytul}' jest dostępna, liczba sztuk: {ksiazki[tytul]}")
        else:
            print(f"Książka '{tytul}' nie jest dostępna.")

    elif komenda == "UNIKALNE":
        liczba_unikalnych = len(ksiazki)
        print(f"Liczba unikalnych tytułów w bibliotece: {liczba_unikalnych}")

    elif komenda == "LICZBA":
        liczba_woluminow = sum(ksiazki.values())
        print(f"Łączna liczba woluminów w bibliotece: {liczba_woluminow}")

    elif komenda == "HISTORIA":
        if historia:
            print("Historia operacji:")
            for wpis in historia:
                print(wpis)
        else:
            print("Historia jest pusta.")

    elif komenda == "POMOC":
        print(
            """
        Dostępne komendy:
        1. WPROWADZ - Wprowadzanie nowych książek
        2. WYPOZYCZ - Wypożyczenie książek
        3. KSIAZKI - Wyświetlenie listy książek z liczbą sztuk
        4. DOSTEPNOSC - Sprawdzenie dostępności książki
        5. UNIKALNE - Liczba unikalnych tytułów książek
        6. LICZBA - Łączna liczba wszystkich woluminów
        7. HISTORIA - Wyświetlenie historii operacji
        8. POMOC - Wyświetlenie dostępnych komend
        9. KONIEC - Zakończenie programu
        """
        )

    elif komenda == "KONIEC":
        print("Zakończenie programu.")
        break

    else:
        print("Nieznana komenda. Wpisz 'POMOC', aby wyświetlić listę komend.")
