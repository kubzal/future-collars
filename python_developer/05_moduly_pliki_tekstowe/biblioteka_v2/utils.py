def wczytaj_ksiazki():
    ksiazki = {}
    with open("ksiazki.txt", "r") as plik:
        for linia in plik:
            tytul, liczba = linia.strip().split(",")
            ksiazki[tytul] = int(liczba)
    return ksiazki


# ksiazki = wczytaj_ksiazki()
# print(ksiazki)


def wyswietl_pomoc(with_log=True):
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

    if with_log:
        log_message = "Wyświetlono pomoc."
        return log_message
    else:
        return ""


def wyswietl_powitanie():
    print("Witaj w programie Biblioteka v2.0")
    wyswietl_pomoc(with_log=False)


def aktualizuj_baze_ksiazek(ksiazki):
    # Zapisz do pliku
    with open("ksiazki.txt", "w") as plik:
        for tytul, liczba in ksiazki.items():
            plik.write(f"{tytul}, {liczba}\n")


def wprowadz_ksiazke(ksiazki):
    tytul = input("Podaj tytuł książki: ")
    liczba = int(input("Podaj liczbę sztuk: "))
    if tytul in ksiazki:
        ksiazki[tytul] += liczba
    else:
        ksiazki[tytul] = liczba

    log_message = f"Wprowadzono książkę: {tytul}, liczba: {liczba}"
    print(log_message)

    aktualizuj_baze_ksiazek(ksiazki)
    return ksiazki, log_message


def wypozycz_ksiazke(ksiazki):
    tytul = input("Podaj tytuł książki: ")
    liczba = int(input("Podaj liczbę sztuk do wypożyczenia: "))
    if tytul in ksiazki and ksiazki[tytul] >= liczba:
        ksiazki[tytul] -= liczba
        if ksiazki[tytul] == 0:
            del ksiazki[tytul]  # Usuwanie książki z biblioteki, jeśli liczba wynosi 0
        log_message = f"Wypożyczono książkę: {tytul}, liczba: {liczba}"
        print(log_message)
    else:
        print(
            f"Brak wystarczającej liczby sztuk książki: {tytul} lub nie ma jej w bibliotece."
        )

    aktualizuj_baze_ksiazek(ksiazki)
    return ksiazki, log_message


def wyswietl_historie(historia):
    if historia:
        print("Historia operacji:")
        for wpis in historia:
            print(wpis)
    else:
        print("Historia jest pusta.")

    log_message = "Wyświetlono historię operacji."
    return log_message


def wyswietl_liczbe_woluminow(ksiazki):
    liczba_woluminow = sum(ksiazki.values())
    print(f"Łączna liczba woluminów w bibliotece: {liczba_woluminow}")

    log_message = f"Wyświetlono łączną liczbę woluminów: {liczba_woluminow}"
    return log_message


def wyswietl_dostepnosc(ksiazki):
    tytul = input("Podaj tytuł książki: ")
    if tytul in ksiazki:
        print(f"Książka '{tytul}' jest dostępna, liczba sztuk: {ksiazki[tytul]}")
    else:
        print(f"Książka '{tytul}' nie jest dostępna.")

    log_message = f"Wyświetlono dostępność książki: {tytul}"
    return log_message


def zapisz_historie(historia):
    with open("historia.txt", "w") as plik:
        for wpis in historia:
            plik.write(f"{wpis}\n")
    print("Zapisano historię operacji.")
