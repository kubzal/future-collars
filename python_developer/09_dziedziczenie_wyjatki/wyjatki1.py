def dzielenie(a, b):
    try:
        wynik = a / b
        print(f"Wynik dzielenia: {wynik}")
    except ZeroDivisionError:
        print("Błąd: Nie można dzielić przez zero!")
    except TypeError:
        print("Błąd: Wprowadzone wartości muszą być liczbami!")
    else:
        print("Dzielenie zakończone pomyślnie!")
    finally:
        print("Operacja dzielenia zakończona.")


# Przykłady użycia:
dzielenie(10, 2)  # Prawidłowe dzielenie
dzielenie(10, 0)  # Błąd: dzielenie przez zero
dzielenie(10, "a")  # Błąd: typ danych


# Jak to działa:
# try: Kod wewnątrz bloku try jest próbą wykonania operacji. Jeśli coś pójdzie nie tak, program przechodzi do bloku except.
# except: Tutaj definiujemy, jakie błędy chcemy przechwycić. W tym przykładzie obsługujemy dwa wyjątki: ZeroDivisionError i TypeError.
# else: Kod w bloku else zostanie wykonany, jeśli nie wystąpi żaden wyjątek.
# finally: Kod w bloku finally zostanie wykonany bez względu na to, czy wyjątek wystąpił, czy nie.
