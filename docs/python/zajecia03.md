# Zajęcia 3 - listy, słowniki itd.

### Listy, krotki, słowniki i zbiory – czyli jak Python organizuje chaos! 🧠🔢

W Pythonie mamy kilka sprytnych sposobów na przechowywanie danych w większych paczkach. Poznaj cztery tajne bronie do tego zadania: **listy**, **krotki**, **słowniki** i **zbiory**! Każda z nich ma swoje unikalne supermoce, więc dowiedzmy się, czym się różnią i do czego najlepiej ich używać. 🚀

### Listy – taka tablica, tylko bardziej cool! 📝

**Lista** to zbiór rzeczy, które można dowolnie zmieniać, dodawać i usuwać, jakby to była Twoja codzienna lista zakupów. Masz pełną swobodę!

Przykład:
```python
owoce = ["jabłko", "banan", "pomarańcza"]
owoce.append("gruszka")  # Dodajemy gruszkę do listy
print(owoce)  # Wynik: ["jabłko", "banan", "pomarańcza", "gruszka"]
```

Co możesz robić z listami?  
- Dodawać nowe elementy: `owoce.append("gruszka")`
- Usuwać elementy: `owoce.remove("banan")`
- Odczytywać elementy: `owoce[0]` (pierwszy element to "jabłko")

Lista to elastyczny kolega, który zawsze jest gotowy na zmiany! 💪

### Krotki – dla fanów stabilności! 🔒

**Krotka** (ang. tuple) to jak lista, ale taka, której nie można zmieniać – jak umowa, której musisz dotrzymać. Raz utworzona, nie pozwala na dodawanie czy usuwanie elementów. Używaj jej, kiedy wiesz, że dane mają być "zamrożone" na wieki.

Przykład:
```python
kolory = ("czerwony", "zielony", "niebieski")
print(kolory[1])  # Wynik: "zielony"
```

Co można robić z krotkami?
- Odczytywać elementy: `kolory[0]`
- Ale nie można zmieniać ani dodawać nowych elementów!

Krotki to doskonały wybór, jeśli chcesz, żeby dane pozostały nienaruszone – jak skarb w sejfie. 🏛️

### Słowniki – Twój osobisty organizer! 📖🔑

**Słownik** (ang. dictionary) to zbiór kluczy i przypisanych do nich wartości. Myślisz o nim jak o prawdziwym słowniku: klucz (słowo) i wartość (definicja). Każdy klucz w słowniku jest unikalny, a do każdej wartości można się łatwo dostać przez ten klucz.

Przykład:
```python
osoba = {"imie": "Kuba", "wiek": 30, "miasto": "Warszawa"}
print(osoba["imie"])  # Wynik: "Kuba"
```

Co można robić ze słownikami?  
- Dodawać lub modyfikować wartości: `osoba["praca"] = "programista"`
- Odczytywać wartości: `osoba["wiek"]`
- Usuwać elementy: `del osoba["miasto"]`

Słowniki to doskonałe narzędzie, gdy masz dane w parach (klucz – wartość) i chcesz mieć szybki dostęp do informacji. 🧠🔑

### Zbiory – dla miłośników porządku i unikalności! 🧹

**Zbiór** (ang. set) to taki pojemnik, który pozwala przechowywać wyłącznie unikalne elementy. Czyli zero duplikatów! Idealny, kiedy musisz pozbyć się powtarzających się rzeczy albo gdy chcesz pracować z danymi, które są tylko raz.

Przykład:
```python
cyfry = {1, 2, 3, 3, 4}  # Zbiór automatycznie wyrzuci powtórzenia
print(cyfry)  # Wynik: {1, 2, 3, 4}
```

Co można robić ze zbiorami?  
- Dodawać elementy: `cyfry.add(5)`
- Usuwać elementy: `cyfry.remove(2)`
- Sprawdzać unikalność!

Zbiory to porządkowi, którzy usuwają wszystkie duplikaty i dbają o czystość w Twoich danych! 🧽

### Podsumowanie: 

- **Listy** – Elastyczne i łatwe do zmiany, jak lista zakupów. 📋
- **Krotki** – Stabilne i niezmienne, jak posąg w muzeum. 🗿
- **Słowniki** – Zbiory klucz-wartość, idealne do przechowywania informacji. 🔐
- **Zbiory** – Unikalne elementy, świetne do porządkowania danych. ✨

Teraz masz cztery potężne narzędzia do zarządzania danymi w Pythonie. Używaj ich mądrze i niech Twoje dane zawsze będą zorganizowane jak należy! 😎