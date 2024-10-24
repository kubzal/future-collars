# Zadanie: Program do zarządzania pracownikami firmy:
# 1. Tworzenie:
#    - Możliwość dodania:
#      -> Managera (imię, nazwisko, dział, zarobki)
#      -> Pracownika (imię, nazwisko, dział, stanowisko, zarobki)
#      -> Zarządu (placeholder, brak szczegółów)
# 2. Zarządzanie:
#    - Stanowisko: wyświetla pracowników na danym stanowisku
#    - Podwładni: wyświetla pracowników zarządzanych przez wybranego managera
#    - Bilans: wyświetla sumę zarobków wszystkich pracowników
# 3. Zakończenie: opcja 'koniec' kończy program.


class Manager:
    def __init__(self, imie, nazwisko, dzial, zarobki):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dzial = dzial
        self.zarobki = zarobki


class Pracownik:
    def __init__(self, imie, nazwisko, dzial, stanowisko, zarobki):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dzial = dzial
        self.stanowisko = stanowisko
        self.zarobki = zarobki

    def __str__(self):
        return f"<Pracownik: {self.imie} {self.nazwisko} - dzial: {self.dzial}, stanowisko: {self.stanowisko}>"


managerowie = []
pracownicy = []


def wczytaj_managera():
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    dzial = input("Podaj dzial: ")
    zarobki = input("Podaj zarobki: ")

    nowy_manager = Manager(imie, nazwisko, dzial, zarobki)
    return nowy_manager


def wczytaj_pracownika():
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    dzial = input("Podaj dzial: ")
    stanowisko = input("Podaj stanowisko: ")
    zarobki = input("Podaj zarobki: ")

    nowy_pracownik = Pracownik(imie, nazwisko, dzial, stanowisko, zarobki)
    return nowy_pracownik


while True:
    akcja = input("Co chcesz zrobić? [utworz, zarzadzaj, koniec]: ")

    if akcja == "koniec":
        break

    elif akcja == "utworz":
        print("Utwórz: [zarząd, manager, pracownik]")
        while True:
            akcja_utworz = input(
                "Co chcesz utworzyć? [zarzad, manager, pracownik, koniec]: "
            )

            if akcja_utworz == "koniec":
                break

            elif akcja_utworz == "zarzad":
                print("Dodaj zarząd")

            elif akcja_utworz == "manager":
                print("Dodaj managera")

                nowy_manager = wczytaj_managera()
                managerowie.append(nowy_manager)

            elif akcja_utworz == "pracownik":
                print("Dodaj pracownika")

                nowy_pracownik = wczytaj_pracownika()
                pracownicy.append(nowy_pracownik)

            else:
                print(f"Nie można dodać elementu '{akcja_utworz}'")

    elif akcja == "zarzadzaj":
        print("Zarządzaj: [stanowisko, podwladni, bilans]")

        while True:
            akcja_zarzadzaj = input(
                "Co chcesz zrobić? [stanowisko, podwladni, bilans, koniec]: "
            )

            if akcja_zarzadzaj == "koniec":
                break

            elif akcja_zarzadzaj == "stanowisko":
                print("Wypisz pracowników na danym stanowisku")

                stanowisko = input("Podaj stanowisko: ")

                for pracownik in pracownicy:
                    if pracownik.stanowisko == stanowisko:
                        print(pracownik)

            elif akcja_zarzadzaj == "podwladni":
                print("Wypisz podwładnych managera")

                imie_managera = input("Podaj imie i nazwisko managera: ")
                nazwisko_managera = input("Podaj nazwisko managera: ")

                for manager in managerowie:
                    if (
                        manager.imie == imie_managera
                        and manager.nazwisko == nazwisko_managera
                    ):
                        for pracownik in pracownicy:
                            if pracownik.dzial == manager.dzial:
                                print(pracownik)

            elif akcja_zarzadzaj == "bilans":
                print("Bilans")

            else:
                print(f"Nie można wykonać akcji '{akcja_zarzadzaj}'")

    else:
        print("Nieprawidłowa komenda")
