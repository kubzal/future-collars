# Przyklad 1: Logowanie wywolania funkcji
import functools
import time
import random
import json
from datetime import datetime


def log_calls(func):
    """Dekorator logujący wywołanie funkcji."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Wywołano funkcję {func.__name__} z argumentami {args} i {kwargs}")
        result = func(*args, **kwargs)
        print(f"Funkcja {func.__name__} zwróciła {result}")
        return result

    return wrapper


@log_calls
def add(a, b):
    return a + b


# Przyklad 2: Mierzenie czasu wykonania funkcji
def timer(func):
    """Dekorator mierzący czas wykonania funkcji."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funkcja {func.__name__} wykonana w {end_time - start_time:.4f} sekund")
        return result

    return wrapper


@timer
def calculate():
    time.sleep(2)
    return "Gotowe!"


# Przyklad 3: Cache wyników funkcji
def cache(func):
    """Dekorator cache'ujący wyniki funkcji."""
    memo = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in memo:
            print(f"Zwracam wynik z cache dla {args}")
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Przyklad 4: Sprawdzanie uprawnien uzytkownika
def requires_permission(permission):
    """Dekorator sprawdzający uprawnienia użytkownika."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if permission not in user["permissions"]:
                raise PermissionError(f"Użytkownik nie ma uprawnień: {permission}")
            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@requires_permission("admin")
def delete_data(user):
    return "Dane usunięte!"


# Przyklad 5: Ograniczanie liczby wywołań funkcji
def rate_limit(limit, period):
    """Dekorator ograniczający liczbę wywołań funkcji."""
    calls = []

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            now = time.time()
            calls = [call for call in calls if now - call < period]
            if len(calls) >= limit:
                raise RuntimeError("Limit wywołań osiągnięty")
            calls.append(now)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit(3, 5)
def send_message(msg):
    print(f"Wysłano wiadomość: {msg}")


# Przyklad 6: Automatyczna obsluga wyjatkow
def exception_handler(func):
    """Dekorator przechwytujący wyjątki."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Wystąpił błąd w funkcji {func.__name__}: {e}")
            return None

    return wrapper


@exception_handler
def divide(a, b):
    return a / b


# Przyklad 7: Wymuszanie typu argumentow
def enforce_types(*types):
    """Dekorator wymuszający typy argumentów."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, type_ in zip(args, types):
                if not isinstance(arg, type_):
                    raise TypeError(f"Argument {arg} nie jest typu {type_}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@enforce_types(int, int)
def multiply(a, b):
    return a * b


# Przyklad 8: Retry funkcji w przypadku bledu
def retry(times):
    """Dekorator ponawiający wywołanie funkcji."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Próba {attempt + 1} nie powiodła się: {e}")
            raise Exception("Wszystkie próby nieudane")

        return wrapper

    return decorator


@retry(3)
def risky_operation():
    if random.random() < 0.7:
        raise ValueError("Losowy błąd!")
    return "Sukces!"


# Przyklad 9: Dodawanie funkcjonalnosci do metod klasy
def log_method(func):
    """Dekorator logujący wywołanie metody klasy."""

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Wywołano metodę {func.__name__} z argumentami {args} i {kwargs}")
        return func(self, *args, **kwargs)

    return wrapper


class MyClass:
    @log_method
    def greet(self, name):
        print(f"Cześć, {name}!")


# Przyklad 10: Zapisywanie wynikow funkcji do pliku
def save_to_file(filename):
    """Dekorator zapisujący wyniki funkcji do pliku."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "w") as f:
                json.dump(result, f, indent=4)
            print(f"Wynik zapisano do pliku {filename}")
            return result

        return wrapper

    return decorator


@save_to_file("output.json")
def get_data():
    return {"name": "Kuba", "age": 30, "hobby": ["guitar", "coding"]}


# Przyklad 11: Limity dostepu czasowego
def working_hours_only(start_hour, end_hour):
    """Dekorator blokujący funkcję poza określonymi godzinami."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_hour = datetime.now().hour
            if start_hour <= current_hour < end_hour:
                return func(*args, **kwargs)
            else:
                raise RuntimeError("Funkcja dostępna tylko w godzinach pracy!")

        return wrapper

    return decorator


@working_hours_only(9, 17)
def perform_task():
    print("Zadanie wykonane!")


# Przyklad 12: Dynamiczne wlaczanie/wylaczanie funkcji
def toggleable(enabled):
    """Dekorator dynamicznie włączający lub wyłączający funkcję."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not enabled:
                print(f"Funkcja {func.__name__} jest wyłączona.")
                return None
            return func(*args, **kwargs)

        return wrapper

    return decorator


@toggleable(enabled=False)
def send_email():
    print("Wysłano e-mail!")
