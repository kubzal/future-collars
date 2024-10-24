def sprawdz_wiek(wiek):
    if wiek < 0:
        raise ValueError("Wiek nie może być ujemny!")
    elif wiek < 18:
        print("Użytkownik jest niepełnoletni.")
    else:
        print("Użytkownik jest pełnoletni.")


# Przykłady użycia:
try:
    sprawdz_wiek(25)  # Prawidłowy wiek
    sprawdz_wiek(-5)  # Błąd: ujemny wiek
except ValueError as e:
    print(f"Błąd: {e}")
