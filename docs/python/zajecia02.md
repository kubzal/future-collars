# Zajęcia 2 - if, pętle

### Decyzje i powtórki – czyli jak Python myśli i działa! 🤔🔄

W Pythonie mamy kilka sprytnych sposobów, żeby komputer podejmował decyzje i powtarzał coś, kiedy tego potrzebujemy. Poznajmy **if**, **for** i **while** – trójkę najlepszych przyjaciół programisty!

### If – decyzje w stylu komputera! 💡

Chcesz, żeby komputer podjął decyzję? Zrób to za pomocą **if**! Python działa wtedy jak super szybki sędzia: jeśli coś jest prawdziwe, zrobi to, co każesz, a jak nie, to... po prostu nic nie zrobi (chyba że dorzucisz inne opcje).

Przykład:
```python
x = 10
if x > 5:
    print("X jest większe od 5!")
else:
    print("X jest mniejsze lub równe 5!")
```
Wynik: `X jest większe od 5!`

Komputer sprawdza, czy `x > 5` i jeśli tak, wyświetla to, co jest w **if**. Jeśli nie, przechodzi do **else** – bo przecież życie to sztuka wyborów!

### For – powtarzanie rzeczy na okrągło! 🔁

Jeśli musisz coś zrobić kilka razy, np. przejść przez listę ulubionych piosenek, Python użyje pętli **for**, by powtórzyć to tak długo, jak trzeba.

Przykład:
```python
piosenki = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"]
for piosenka in piosenki:
    print(f"Słucham: {piosenka}")
```
Wynik:
```
Słucham: Bohemian Rhapsody
Słucham: Stairway to Heaven
Słucham: Hotel California
```
Python przejdzie przez każdą piosenkę na liście i wyświetli jej tytuł – prosto, prawda?

### While – dopóki warunki są spełnione! ⏳

Pętla **while** to jak powiedzenie "będę to robić, dopóki...", a Python robi to tak długo, aż warunek przestanie być prawdziwy.

Przykład:
```python
licznik = 5
while licznik > 0:
    print(f"Licznik: {licznik}")
    licznik -= 1
```
Wynik:
```
Licznik: 5
Licznik: 4
Licznik: 3
Licznik: 2
Licznik: 1
```
Pętla będzie się kręcić, dopóki licznik nie spadnie do zera. Potem Python się zatrzyma, bo wszystko ma swoje granice!

### Podsumowanie

- **If** – komputer wybiera jedną z dróg, jak prawdziwy Sherlock Holmes! 🕵️‍♂️
- **For** – powtarzanie, żeby coś zrobić dla każdego elementu w zbiorze. 📀
- **While** – robienie czegoś, dopóki warunek jest spełniony. ⏰

I to tyle! Teraz już wiesz, jak sprawić, żeby Twój program podejmował decyzje i powtarzał rzeczy bez końca (albo przynajmniej do momentu, gdy powiesz "stop"). 😉

### Zadanie
Ponizej znajduje się wizualizacja działąnia pętli z Przykładu 2 do pracy domowej:
```
Przykład 2:
Ilość elementów: 6
Wagi elementów: 3, 6, 5, 8, 2, 3
``` 

![Tak działa pętla w zadaniu z paczkami](https://raw.githubusercontent.com/kubzal/future-collars/refs/heads/main/python_developer/02_warunki_petle/zadanie_paczki_v2.svg)