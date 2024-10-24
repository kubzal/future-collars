class Manager:
    def __init__(self):
        self.methods = {}

    def assign(self, action_name):
        # Dekorator przypisujący funkcję do instancji na podstawie podanej nazwy akcji
        def decorator(func):
            self.methods[action_name.upper()] = func
            return func

        return decorator

    def execute(self, action, biblioteka):
        # Metoda wywołująca przypisaną funkcję
        action = action.upper()  # Obsługuje małe/duże litery
        if action in self.methods:
            return self.methods[action](biblioteka)
        else:
            print(f"Nieznana akcja: {action}")


# Tworzymy słownik jako bibliotekę z 3 przykładowymi książkami
biblioteka = {"Wiedźmin": 3, "Hobbit": 2, "Harry Potter": 5}

# Tworzymy obiekt managera
manager = Manager()


# Akcja dodawania książki
@manager.assign("dodaj")
def dodaj_ksiazke(biblioteka):
    tytul = input("Podaj tytuł książki: ").strip()
    liczba_sztuk = int(input("Podaj liczbę sztuk: ").strip())
    if tytul in biblioteka:
        biblioteka[tytul] += liczba_sztuk
    else:
        biblioteka[tytul] = liczba_sztuk
    print(f"Dodano {liczba_sztuk} sztuk książki '{tytul}' do biblioteki.")


# Akcja wypożyczania książki
@manager.assign("wypozycz")
def wypozycz_ksiazke(biblioteka):
    tytul = input("Podaj tytuł książki: ").strip()
    if tytul in biblioteka and biblioteka[tytul] > 0:
        biblioteka[tytul] -= 1
        print(f"Książka '{tytul}' została wypożyczona.")
    else:
        print(f"Książka '{tytul}' nie jest dostępna.")


# Akcja wyświetlania dostępnych książek
@manager.assign("wyswietl")
def wyswietl_ksiazki(biblioteka):
    if not biblioteka:
        print("Brak książek w bibliotece.")
    else:
        print("Dostępne książki w bibliotece:")
        for tytul, liczba in biblioteka.items():
            print(f"- {tytul}: {liczba} sztuk")


# Pętla do obsługi akcji od użytkownika
while True:
    akcja = (
        input("Wprowadź akcję (dodaj, wypozycz, wyswietl) lub 'wyjdz' aby zakończyć: ")
        .strip()
        .lower()
    )
    if akcja == "wyjdz":
        print("Zakończono program.")
        break
    manager.execute(akcja, biblioteka)
