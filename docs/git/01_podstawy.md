# Podstawy
### Git – Twój superbohater od wersji! 🦸‍♂️

Git to taki Batman świata programowania. Pomaga Ci zarządzać wersjami Twojego kodu, żebyś nie musiał nazywać plików „projekt_FINAL_Ostateczny_FINAŁv2.zip”. Dzięki Gitowi możesz cofać zmiany, porównywać wersje i pracować z zespołem, nie wpadając w chaos. A teraz czas poznać najważniejsze polecenia, żebyś i Ty mógł poczuć się jak mistrz wersji! ⚡

### Staging i Commit – przystanek i podpis! 📝

Wyobraź sobie, że pracujesz nad kodem i chcesz zapisać pewien fragment swojej pracy, ale jeszcze nie oddać go światu (czyli nie zatwierdzić w repo). **Staging** to takie miejsce, gdzie możesz przygotować zmiany – jakbyś układał składniki na kanapce przed włożeniem do piekarnika.

Przykład:
```bash
git add nazwa_pliku.py  # Wkładasz plik do "piekarnika", czyli staging area.
```

A teraz **commit** to taki oficjalny „klik” – zapisujesz swoje zmiany, nadajesz im etykietkę (komentarz), żeby nie zapomnieć, co zrobiłeś, i bum! Gotowe!

```bash
git commit -m "Dodałem nową funkcję do pieczenia kanapek!"
```

Zapisane! Możesz teraz wrócić do tej wersji w każdej chwili.

### Branch – Twoje własne laboratorium eksperymentów! 🧪

**Branch** to gałąź, na której możesz eksperymentować bez niszczenia głównego projektu. Chcesz spróbować nowych rzeczy, ale boisz się, że rozwalisz coś ważnego? Żaden problem! Tworzysz nową gałąź, robisz swoje eksperymenty, a jak się uda, łączysz to z główną wersją.

Przykład:
```bash
git branch moja-nowa-galaz  # Tworzymy nową gałąź.
git checkout moja-nowa-galaz  # Przechodzimy na naszą nową gałąź.
```

Teraz możesz szaleć, a Twój główny kod jest bezpieczny jak w sejfie! 🛡️

### Git Checkout – podróże w czasie! ⏳

Chcesz wrócić do poprzedniego commita? A może przerzucić się na inną gałąź? **Git checkout** to Twoja maszyna czasu! Pozwala Ci przenosić się między wersjami kodu, jakbyś nigdy nie popełnił tych fatalnych błędów w nowej funkcji.

```bash
git checkout nazwa-innej-galazki  # Podróż na inną gałąź.
```

Hop, zmiana! I jesteś w innym miejscu w kodzie, bez żadnych problemów.

### Git Diff – co się zmieniło?! 🔍

Chcesz sprawdzić, co dokładnie zmieniłeś w swoim kodzie? **Git diff** pokaże Ci, jak detektyw, jakie linie kodu zostały zmodyfikowane, dodane lub usunięte. To takie porównywanie starych i nowych wersji tekstu przed oddaniem pracy domowej.

```bash
git diff  # Pokaże różnice między obecną wersją a tym, co było wcześniej.
```

Możesz zobaczyć wszystko, co się zmieniło – czy to dobrze, czy źle... to już inna sprawa! 😉

### Git Log – historia Twoich bohaterskich czynów! 📜

Potrzebujesz przypomnieć sobie, co robiłeś tydzień temu? A może chcesz zobaczyć wszystkie commity w projekcie? **Git log** to Twoje osobiste archiwum. Każdy commit, każda zmiana, wszystko zapisane i czeka, aż to przeczytasz.

```bash
git log  # Lista wszystkich commitów, jak długa historia Twojego życia!
```

Możesz przeglądać każdy commit i zobaczyć, kto, kiedy i dlaczego coś zmienił – jak śledztwo w kryminalnej zagadce kodu!

### Podsumowanie:

- **git add** – Wrzuć pliki do staging area (czyli przygotuj zmiany do commita).
- **git commit** – Zatwierdź zmiany z komentarzem.
- **git branch** – Stwórz nową gałąź, żeby eksperymentować.
- **git checkout** – Przełącz się na inną wersję kodu lub gałąź.
- **git diff** – Zobacz, co się zmieniło między wersjami.
- **git log** – Przeglądaj historię commitów.

Teraz, uzbrojony w te narzędzia, możesz śmiało pracować nad swoim kodem, niczym programistyczny superbohater, ratujący dzień i wersje! 🦸‍♀️👨‍💻


---

### Notatki dla prowadzącego:

#### **1. Co to jest Git?**
- Rozproszony system kontroli wersji.
- Standard w wersjonowaniu kodu.
- **Git ≠ GitHub**: GitHub to dostawca repozytoriów Git.

#### **2. Problemy rozwiązywane przez Git**
- Współpraca wielu osób nad jednym projektem.
- Zarządzanie wersjami programu.
- Odporność na awarie lokalne i serwerowe.
- Łatwość w scalaniu zmian.
- Równoległa praca nad różnymi funkcjami.
- Rozdzielenie wersji stabilnej od rozwojowej.

#### **3. Praca z linią komend**
- **Nawigacja w terminalu**: `pwd`, `cd`, `ls -a` (Unix) / `DIR /a:h` (Windows).
- **Tworzenie repozytorium**: 
  - `git init`
  - Sprawdzenie statusu: `git status`
- **Dodanie pierwszego pliku**:
  - `touch pierwszy.txt`
  - `git add pierwszy.txt`
  - `git commit -m "dodaję plik pierwszy.txt"`

#### **4. Commit - podstawy**
- **Commit**: Paczka zmian z identyfikatorem i komentarzem.
- **Dwustopniowy proces:**
  - `git add <plik>`
  - `git commit -m "<komentarz>"`

#### **5. Operacje na plikach**
- **Zmiana nazwy/pliku**:
  - `git mv <stara_nazwa> <nowa_nazwa>`
- **Dodawanie katalogu**:
  - `git add <katalog>`
- **Usunięcie pliku**:
  - `git rm <plik>`

#### **6. Przywracanie plików i resetowanie zmian**
- **Przywracanie do ostatniego commita**: `git checkout <plik>`
- **Usunięcie ze staging**: `git reset HEAD <plik>`

#### **7. Historia zmian**
- **Wyświetlanie logów**: `git log`
- **Historia dla konkretnego pliku**: `git log -p <plik>`

#### **8. Cofanie zmian**
- **Zachowanie przyszłych commitów**: `git revert <commit_ID>`
- **Cofnięcie się do konkretnego commita**: `git checkout <commit_ID>`

#### **9. Detach HEAD**
- Wyjaśnienie: Cofanie do konkretnego commita odłącza HEAD od gałęzi. 