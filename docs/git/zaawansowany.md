### Git – Tryb zaawansowany: Tajne Triki Superbohatera! 🦸‍♂️💻

Skoro już znasz podstawy Gita, czas na bardziej zaawansowane sztuczki! Git to nie tylko zapis zmian, to prawdziwe narzędzie ninja, które pozwala Ci bezpiecznie eksperymentować, resetować, a nawet cofać czas (no, przynajmniej w kodzie). Oto kilka trików, które wyniosą Cię na wyższy poziom! 🚀

### Szybkie tworzenie i przełączanie się na nową gałąź 🌿

Pamiętasz, jak mówiłem o **branchach**? Jest szybszy sposób na stworzenie nowej gałęzi i natychmiastowe przełączenie się na nią. Zamiast tworzyć ją i potem się przerzucać, możesz to zrobić w jednym ruchu:

```bash
git checkout -b moja-nowa-galaz  # Tworzy nową gałąź i od razu na nią przechodzi.
```

Teraz masz nową gałąź w jednej komendzie. Mistrzostwo!

### Resetowanie staging area – Ups! 🙊

Coś wrzuciłeś do staging area, a teraz myślisz: "Oj, jednak tego nie chciałem"? Żaden problem! Możesz cofnąć dodanie pliku do staging area bez niszczenia kodu.

```bash
git reset nazwa_pliku.py  # Cofasz plik ze staging area, ale nie usuwasz zmian w nim.
```

I po kłopocie! Plik wraca do swojej pierwotnej postaci i czeka na Twoje decyzje.

### Checkout na konkretny commit – Podróż w czasie! ⏳

Chcesz cofnąć się do konkretnego momentu w historii projektu? Możesz to zrobić za pomocą **commit ID**, które znajdziesz w historii `git log`.

```bash
git checkout [commit_id]  # Przenosisz się do konkretnej wersji kodu.
```

To jak powrót do przeszłości, gdzie możesz zobaczyć, jak kod wyglądał przed każdą katastrofą!

### Mergowanie gałęzi – Złączenie sił! 🤝

Stworzyłeś nową gałąź, coś w niej majstrowałeś, a teraz chcesz te zmiany połączyć z główną wersją (czyli gałęzią `master`)? Czas na **merge**! Mergowanie to jak dodanie Twoich eksperymentów do głównego kodu.

Najpierw przechodzisz na `master`:
```bash
git checkout master
```

A potem mergujesz swoją gałąź z masterem:
```bash
git merge moja-nowa-galaz  # Łączy zmiany z gałęzią master.
```

I voila! Wszystko jest teraz w jednej, szczęśliwej wersji. 🥳

### Cofanie commitów – O nie, jednak nie to chciałem! 😱

Co zrobić, jeśli wykonałeś commit, ale teraz tego żałujesz? Spokojnie, jest na to sposób! Możesz cofnąć ostatni commit bez straty zmian, żeby poprawić kod lub komentarz.

```bash
git reset --soft HEAD~1  # Cofasz ostatni commit, ale zachowujesz zmiany.
```

Jeśli natomiast chcesz totalnie zresetować wszystko (i wrócić do stanu przed commitem), użyj:
```bash
git reset --hard HEAD~1  # Cofasz commit i wszystkie zmiany.
```

Uwaga: **--hard** usuwa wszystkie zmiany, więc używaj tego jak supermocy – z rozwagą!

### Podsumowanie: Twoje nowe supermoce w Git! ⚡

- **git checkout -b** – Tworzenie i przechodzenie na nową gałąź w jednym kroku!
- **git reset [nazwa_pliku]** – Usuwasz plik ze staging area.
- **git checkout [commit_id]** – Przejście do konkretnej wersji kodu.
- **git merge [nazwa_gałęzi]** – Łączysz swoją gałąź z główną wersją (master).
- **git reset --soft HEAD~1** – Cofasz commit, ale zachowujesz zmiany.
- **git reset --hard HEAD~1** – Cofasz commit i kasujesz zmiany (używaj ostrożnie!).

Teraz jesteś gotowy na najtrudniejsze bitwy programistyczne! Dzięki tym komendom nie tylko będziesz zarządzać swoim kodem jak ninja, ale też naprawiać błędy i łączyć zmiany jak prawdziwy superbohater! 💥