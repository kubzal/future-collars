class Uzytkownik:
    def __init__(self, nazwa, poziom_uprawnien):
        self.nazwa = nazwa
        self.poziom_uprawnien = poziom_uprawnien

def sprawdz_uprawnienia(wymagany_poziom_uprawnien):
    def dekorator(funkcja):
        def opakowanie(*args, **kwargs):
            user = kwargs.get("user")  # Pobieramy użytkownika z argumentów
            if isinstance(user, Uzytkownik) and user.poziom_uprawnien == wymagany_poziom_uprawnien:
                print(f"Użytkownik ma poziom uprawnień: {wymagany_poziom_uprawnien}")
                return funkcja(*args, **kwargs)
            else:
                print(f"Brak odpowiednich uprawnień! Wymagane: {wymagany_poziom_uprawnien}")
        return opakowanie
    return dekorator

@sprawdz_uprawnienia("admin")
def pokaz_dane_uzytkownika(user):
    print(f"Dane użytkownika: {user.nazwa}, Poziom uprawnień: {user.poziom_uprawnien}")

# Użytkownik 1: Użytkownik z uprawnieniami "admin"
uzytkownik_1 = Uzytkownik("Kuba", "admin")
pokaz_dane_uzytkownika(user=uzytkownik_1)

# Użytkownik 2: Użytkownik bez uprawnień
uzytkownik_2 = Uzytkownik("Ola", "user")
pokaz_dane_uzytkownika(user=uzytkownik_2)

@sprawdz_uprawnienia("moderator")
def usun_komentarz(user, komentarz_id):
    print(f"Komentarz o ID {komentarz_id} został usunięty przez {user.nazwa}")

# Użytkownik 3: Użytkownik z uprawnieniami "moderator"
uzytkownik_3 = Uzytkownik("Piotr", "moderator")
usun_komentarz(user=uzytkownik_3, komentarz_id=42)