def przyklad_args_kwargs(*args, **kwargs):
    print("Argumenty pozycyjne (*args):")
    for arg in args:
        print(arg)

    print("\nArgumenty nazwane (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Wywołanie funkcji z kilkoma argumentami pozycyjnymi i nazwanymi
przyklad_args_kwargs(1, 2, 3, imie="Kuba", wiek=30, miasto="Warszawa")


## Przykład 2: Funkcja z argumentami pozycyjnymi i nazwanymi
def oblicz_cene_zamowienia(cena_podstawowa, *dodatki, **opcje):
    """
    Oblicza końcową cenę zamówienia na podstawie ceny podstawowej,
    opcjonalnych dodatków (args) oraz dodatkowych opcji (kwargs).

    - dodatki: lista cen dodatków (np. dodatki do pizzy)
    - opcje: opcje takie jak 'znizka' i 'dostawa'
    """

    # Dodaj cenę wszystkich dodatków
    suma_dodatkow = sum(dodatki)

    # Oblicz cenę końcową
    cena_koncowa = cena_podstawowa + suma_dodatkow

    # Zastosuj opcjonalną zniżkę, jeśli jest podana
    znizka = opcje.get("znizka", 0)  # Domyślnie brak zniżki
    cena_koncowa -= znizka

    # Dodaj koszt dostawy, jeśli jest podany
    dostawa = opcje.get("dostawa", 0)  # Domyślnie brak kosztu dostawy
    cena_koncowa += dostawa

    return cena_koncowa


# Przykładowe wywołanie funkcji
cena = oblicz_cene_zamowienia(100, 10, 15, znizka=20, dostawa=5)
print(f"Końcowa cena zamówienia: {cena} zł")


# Przykład 3:
def suma_liczb(*args, **kwargs):
    """
    Sumuje liczby podane jako argumenty pozycyjne (args)
    i wyświetla dodatkową wiadomość, jeśli jest podana w kwargs.
    """
    suma = sum(args)

    # Wyświetla sumę
    print(f"Suma liczb: {suma}")

    # Wyświetla dodatkową wiadomość, jeśli została podana
    if "wiadomosc" in kwargs:
        print(f"Wiadomość: {kwargs['wiadomosc']}")


# Przykład wywołania funkcji
suma_liczb(1, 2, 3, 4, wiadomosc="To jest prosty przykład!")
