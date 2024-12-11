# Dekoratory w Pythonie to specjalne funkcje, które pozwalają "opakować" inne funkcje,
# dodając im dodatkowe funkcjonalności bez zmieniania ich kodu. Wyobraź sobie to jak
# nakładanie dodatkowej warstwy na tort - tort jest taki sam, ale możesz dodać coś na
# wierzch, co go ulepszy.

napisz_na_ekranie = print  # Przypisanie funkcji do zmiennej
napisz_na_ekranie("Cześć!")  # Wywołanie funkcji przez zmienną


# Przykład 1: Ramka wokół tekstu
import os


def ramka_dekorator(funkcja):
    def opakowanie(*args, **kwargs):
        # Pobierz rozmiar terminala
        terminal_size = os.get_terminal_size()
        szerokosc = terminal_size.columns

        # Wywołaj oryginalną funkcję, aby uzyskać jej wynik (string)
        wynik = funkcja(*args, **kwargs)

        # Oblicz szerokość ramki
        linia_ramka = "-" * szerokosc

        # Wyświetl wynik w ramce
        print(linia_ramka)
        print(wynik.center(szerokosc))
        print(linia_ramka)

        return wynik  # Zwróć wynik oryginalnej funkcji (jeśli potrzebne)

    return opakowanie


@ramka_dekorator
def powitanie():
    return "Witaj w terminalu!"


# Wywołanie funkcji
powitanie()


# Przykład 2: Cześć!
def przywitanie():
    print("Cześć!")


def dekorator(funkcja):
    def opakowanie():
        print(f"Wywołuję funkcję: {funkcja.__name__}")
        funkcja()  # Wywołuje oryginalną funkcję
        print(f"Zakończyłem wywoływanie funkcji: {funkcja.__name__}")

    return opakowanie


@dekorator  # przywitanie = dekorator(przywitanie)
def przywitanie():
    print("Cześć!")


przywitanie()


# Przykład 3: Mierzenie czasu wykonania funkcji

import time  # Potrzebne do mierzenia czasu


def mierzenie_czasu(funkcja):
    def opakowanie(*args, **kwargs):  # Przyjmujemy dowolne argumenty
        start = time.time()  # Zapisz początkowy czas
        wynik = funkcja(*args, **kwargs)  # Wykonaj funkcję
        koniec = time.time()  # Zapisz czas po wykonaniu
        print(f"Funkcja {funkcja.__name__} zajęła {koniec - start:.4f} sekundy.")
        return wynik  # Zwróć wynik oryginalnej funkcji

    return opakowanie


@mierzenie_czasu
def liczenie_do_miliona():
    suma = 0
    for i in range(1, 1000001):
        suma += i
    return suma


wynik = liczenie_do_miliona()
print(f"Wynik: {wynik}")

# Przykład 4: Sprawdzanie uprawnień użytkownika


def sprawdz_uprawnienia(wymagany_poziom_uprawnien):
    def dekorator(funkcja):
        def opakowanie(*args, **kwargs):
            user = kwargs.get("user")  # Pobieramy użytkownika z argumentów
            if user.get("poziom_uprawnien") == wymagany_poziom_uprawnien:
                print(f"Użytkownik ma poziom uprawnień: {wymagany_poziom_uprawnien}")
                return funkcja(*args, **kwargs)
            else:
                print(
                    f"Brak odpowiednich uprawnień! Wymagane: {wymagany_poziom_uprawnien}"
                )

        return opakowanie

    return dekorator


@sprawdz_uprawnienia("admin")
def pokaz_dane_uzytkownika(user):
    print(f"Dane użytkownika: {user}")


# Użytkownik 1: Użytkownik z uprawnieniami "admin"
uzytkownik_1 = {"nazwa": "Kuba", "poziom_uprawnien": "admin"}
pokaz_dane_uzytkownika(user=uzytkownik_1)

# Użtkownik 2: Użytkownik bez uprawnień
uzytkownik_2 = {"nazwa": "Ola", "poziom_uprawnien": "user"}
pokaz_dane_uzytkownika(user=uzytkownik_2)


@sprawdz_uprawnienia("moderator")
def usun_komentarz(user, komentarz_id):
    print(f"Komentarz o ID {komentarz_id} został usunięty przez {user["nazwa"]}")


# Użytkownik 3 Użytkownik z uprawnieniami "moderator"
uzytkownik_3 = {"nazwa": "Piotr", "uprawnienie": "moderator"}
usun_komentarz(user=uzytkownik_3, komentarz_id=42)


# Przykład 5: Dekorator cache'owania
def cache_decorator(funkcja):
    cache = {}  # Słownik na przechowywanie wyników

    def opakowanie(*args):
        if args in cache:
            print(f"Zwracam wynik z cache dla argumentów {args}")
            return cache[args]  # Zwracamy wynik z cache
        else:
            wynik = funkcja(*args)  # Obliczamy wynik
            cache[args] = wynik  # Zapisujemy wynik w cache
            print(f"Obliczam wynik dla argumentów {args}")
            return wynik

    return opakowanie


@cache_decorator
def silnia(n):
    if n == 0 or n == 1:
        return 1
    return n * silnia(n - 1)


print(silnia(5))
print(silnia(5))  # Powinien zwrócić wynik z cache
print(silnia(6))  # Obliczy wynik tylko dla n = 6, bo wynik dla 5 już jest w cache
