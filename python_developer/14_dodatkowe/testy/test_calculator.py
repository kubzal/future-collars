import pytest
from calculator import add, subtract


def test_add():
    assert add(2, 3) == 5  # Sprawdza poprawność dodawania
    assert add(-1, 1) == 0  # Obsługuje liczby ujemne
    assert add(0, 0) == 0  # Sprawdza przypadek zerowy


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0


# Opcjonalnie: test z obsługą błędów
def test_add_type_error():
    with pytest.raises(TypeError):
        add("2", 3)  # Powinno rzucić błąd, bo nie można dodać stringa do liczby


# # Uruchamiamy testy w terminalu:
# pytest test_calculator.py
