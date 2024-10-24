# Zajęcia 1
## Typy proste w Pythonie – Wersja dla ludzkości! 🧙‍♂️

W Pythonie mamy kilka podstawowych typów zmiennych, które są tak proste, że nawet Twój kot by je zrozumiał (no dobra, może nie każdy kot...). Oto one:

- **int** – liczby całkowite. Idealne do liczenia kotletów na talerzu. 🍖  
  Przykład:  
  ```python
  kotlety = 5  ## Czyli tyle, ile dasz radę zjeść na obiad.
  ```

- **float** – liczby zmiennoprzecinkowe, czyli takie z przecinkiem. Używaj, kiedy chcesz być precyzyjny jak szwajcarski zegarek. ⏱️  
  Przykład:  
  ```python
  pi = 3.14  ## Idealne do liczenia obwodu pizzy! 🍕
  ```

- **str** – łańcuch znaków, czyli tekst. Bez tego nie ma rozmów, wiadomości ani koderskich żartów! 🤓  
  Przykład:  
  ```python
  imie = "Kuba"  ## Bo każde zmienne zasługują na imię.
  ```

- **bool** – wartości logiczne, które są jak światło w lodówce: albo włączone, albo wyłączone. 💡  
  Przykład:  
  ```python
  czy_pizza_zjadana = True  ## Odpowiedź zawsze brzmi: tak! 🍕
  ```

No i to tyle! Proste jak strzałka w kodzie – teraz możesz pisać swoje programy z taką swobodą, jakbyś rozmawiał o tym przy kawie! ☕

## Pobieranie tekstu od użytkownika – czyli jak rozmawiać z komputerem! 🖥️💬

W Pythonie możesz poprosić użytkownika o wpisanie czegoś, a komputer to odczyta jak najlepszy kumpel na czacie. Używamy do tego funkcji `input()`, która czeka na wpisanie tekstu i potem robi z nim cuda (albo przynajmniej wyświetla).

Przykład:
```python
imie = input("Jak masz na imię? ")
print("Cześć, " + imie + "!")
```

Kiedy uruchomisz ten kod, komputer grzecznie zapyta o imię i odpowie: „Cześć, Kuba!” (jeśli masz na imię Kuba...).

## Formatowanie stringów – czyli jak ładnie poskładać tekst! 🎨

Jeśli chcesz zrobić coś bardziej fancy, mamy na to **dwa sposoby**: `.format()` i f-stringi. Oba pozwolą Ci włożyć zmienne do tekstu jak kawałki puzzli.

1. **Metoda .format()** – trochę jak układanie puzzli na spokojnie:
   
   ```python
   imie = "Kuba"
   wiek = 30
   tekst = "Cześć, {}! Masz {} lat.".format(imie, wiek)
   print(tekst)
   ```
   Wynik: `Cześć, Kuba! Masz 30 lat.`

2. **F-stringi** – czyli wersja turbo dla leniwych (albo super sprawnych):
   
   ```python
   imie = "Kuba"
   wiek = 30
   tekst = f"Cześć, {imie}! Masz {wiek} lat."
   print(tekst)
   ```
   Wynik: `Cześć, Kuba! Masz 30 lat.`

F-stringi są jak zamówienie kawy z odbiorem na wynos – szybkie, proste i idealne do wszystkiego. Po prostu wstawiasz zmienne w `{}` i Python zrobi resztę!

To tyle! Teraz wiesz, jak zapytać użytkownika o coś, a potem ładnie odpowiedzieć, żeby wszystko wyglądało pro jak w filmach! 🎬

## Przykład z zajęć

Zadania z narciarzami.

<script src="https://gist.github.com/kubzal/fcb03a1addd69fbdb41d0f6d5c0d3ee7.js"></script>
