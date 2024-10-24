# Zajęcia 4 - funkcje, klasy

### Funkcje – czyli jak nauczyć komputer robić coś za Ciebie! 🧑‍🍳🤖

Funkcje to jedne z najlepszych wynalazków w Pythonie (i nie tylko!). Dzięki nim możesz sprawić, że komputer wykona za Ciebie konkretne zadania, a Ty nie będziesz musiał pisać tego samego kodu milion razy. To jak przepis, który możesz używać do pieczenia ciasta tyle razy, ile chcesz – wystarczy raz go stworzyć!

#### Tworzenie funkcji – czyli magiczne zaklęcie! ✨

Kiedy chcesz, żeby komputer coś dla Ciebie zrobił, tworzysz funkcję. Zaczynasz od słowa kluczowego `def`, które mówi Pythonowi: "Hej, teraz tworzę przepis!". Potem nadajesz funkcji nazwę, podajesz jej składniki (parametry), a na koniec piszesz, co ta funkcja ma zrobić.

Przykład:
```python
def powiedz_czesc(imie):
    print(f"Cześć, {imie}!")
```

A teraz wystarczy wywołać tę funkcję:
```python
powiedz_czesc("Kuba")  # Wynik: Cześć, Kuba!
```

Funkcja `powiedz_czesc` przyjmuje jedno "składnik" – imię – i wyświetla powitanie. Prosto i przyjemnie!

#### Funkcje zwracające wartość – jakby komputer Ci coś oddawał! 🎁

Niektóre funkcje nie tylko coś robią, ale też mogą coś **zwrócić** (czyli oddać Ci wynik). Używamy do tego słowa `return`. Dzięki temu możesz zapisać wynik działania funkcji i użyć go gdzieś indziej.

Przykład:
```python
def dodaj(a, b):
    return a + b

wynik = dodaj(3, 5)
print(wynik)  # Wynik: 8
```

Tutaj funkcja **dodaj** sumuje dwie liczby i oddaje wynik – możesz go później wykorzystać w innym miejscu.

### Wstęp do klas – czyli jak nauczyć Pythona, czym jest pies! 🐕🏛️

Kiedy funkcje przestają wystarczać, czas na **klasy**! Klasy to taki sposób, żeby w Pythonie tworzyć obiekty – np. pies, samochód albo postać w grze. Klasy to takie "plany budowy" dla obiektów. Dają Ci możliwość stworzenia czegoś bardziej złożonego, co ma zarówno **dane** (jakieś właściwości, np. imię psa), jak i **metody** (czyli to, co obiekt może robić, np. szczekać).

#### Tworzenie klasy – plan na Twój obiekt! 📐

Kiedy tworzysz klasę, mówisz Pythonowi, jak zbudować obiekt i jakie będzie miał cechy. A potem możesz stworzyć tyle obiektów na podstawie tej klasy, ile potrzebujesz!

Przykład:
```python
class Pies:
    def __init__(self, imie, rasa):
        self.imie = imie
        self.rasa = rasa

    def szczekaj(self):
        print(f"{self.imie} szczeka! Hau hau!")

# Tworzymy obiekt (czyli psa) na podstawie klasy Pies
mój_pies = Pies("Torvi", "Entlebucher")
mój_pies.szczekaj()  # Wynik: Torvi szczeka! Hau hau!
```

Co tu się dzieje?
- **class** – Słowo kluczowe, które mówi: "Tworzę nową klasę".
- **__init__** – To taka funkcja specjalna, która uruchamia się, gdy tworzysz nowy obiekt. Ustawia początkowe wartości (np. imię i rasę psa).
- **self** – To taki wskaźnik, który mówi: "Hej, tu chodzi o ten konkretny obiekt". Dzięki temu pies wie, że `self.imie` to jego imię, a nie jakieś przypadkowe imię.

### Klasy i obiekty – co dalej? 🚀

Klasy to fundament programowania obiektowego (OOP), które pozwala tworzyć bardziej złożone i uporządkowane programy. Obiekty na podstawie klas mogą mieć różne właściwości i metody, dzięki czemu programy stają się modularne i łatwiejsze do zarządzania. Na początku brzmi to trochę skomplikowanie, ale jak zaczniesz bawić się klasami, odkryjesz, że są naprawdę potężnym narzędziem!

Podsumowując:
- **Funkcje** to jak przepisy na małe, powtarzalne zadania.
- **Klasy** to plany budowy obiektów, które mają zarówno dane, jak i metody.

Teraz masz narzędzia do tworzenia własnych funkcji i pierwszych klas. Czas na Twój własny świat Pythona, pełen szczekających psów, liczących funkcji i innych cudów programowania! 🐍🚀