# Repozytoria zdalne
### Praca z repozytoriami zdalnymi – czyli jak współpracować z resztą świata! 🌍🛠️

Git świetnie sprawdza się na Twoim komputerze, ale co zrobić, gdy chcesz współpracować z innymi? Tutaj pojawiają się **repozytoria zdalne** – miejsca, w których możemy przechowywać i udostępniać swój kod. Najpopularniejszym serwisem do hostowania zdalnych repozytoriów jest **GitHub**, ale istnieją też inne, jak GitLab czy Bitbucket.

Repozytorium zdalne jest jak serwer, na którym trzymasz kopię swojego projektu. Dzięki niemu Ty i Twój zespół możecie synchronizować zmiany, wspólnie edytować kod i zawsze mieć dostęp do najnowszej wersji projektu.

### 1. Co to jest `origin`? 🏷️

Kiedy pracujesz z repozytorium zdalnym, Git przypisuje mu **alias** – domyślnie nazywany `origin`. To skrót, który odnosi się do adresu zdalnego repozytorium, na przykład adresu na GitHubie. Dzięki `origin` możesz łatwo wykonywać operacje na repozytorium zdalnym, np. pobierać zmiany (`git pull`) lub wysyłać swoje (`git push`).

### 2. Jak sklonować istniejące repozytorium? 🧩

Jeśli chcesz pobrać istniejące repozytorium na swój komputer, użyj komendy `git clone`. Sklonuje ona pełną kopię repozytorium, łącznie z historią commitów.

```bash
git clone https://github.com/uzytkownik/nazwa_repo.git
```

Ta komenda tworzy nowy folder o nazwie repozytorium, w którym znajdziesz jego pełną zawartość. Teraz możesz pracować na lokalnej kopii i synchronizować ją z wersją zdalną.

### 3. Jak podpiąć się do istniejącego repozytorium? 🔗

Jeśli masz projekt na komputerze, ale nie jest jeszcze powiązany z repozytorium zdalnym, możesz dodać do niego zdalne repozytorium ręcznie:

```bash
git remote add origin https://github.com/uzytkownik/nazwa_repo.git
```

Ta komenda dodaje adres zdalnego repozytorium pod aliasem `origin`. Teraz Twój lokalny projekt jest połączony ze zdalnym repozytorium, co pozwala na wysyłanie i pobieranie zmian.

#### Sprawdzanie, czy masz już połączone repozytorium zdalne (`git remote -v`) 🔍

Chcesz sprawdzić, czy Twoje lokalne repozytorium jest już powiązane ze zdalnym repozytorium? Możesz to zrobić za pomocą komendy:

```bash
git remote -v
```

Ta komenda wyświetli listę wszystkich zdalnych repozytoriów powiązanych z Twoim projektem, wraz z ich adresami URL. Jeśli wcześniej dodałeś zdalne repozytorium jako `origin`, zobaczysz coś takiego:

```
origin  https://github.com/uzytkownik/nazwa_repo.git (fetch)
origin  https://github.com/uzytkownik/nazwa_repo.git (push)
```

**`(fetch)`** wskazuje adres, z którego Git pobiera zmiany, a **`(push)`** pokazuje, dokąd zmiany są wysyłane. Dzięki temu możesz szybko upewnić się, czy masz już podpięte repozytorium zdalne oraz jakie aliasy i adresy są z nim powiązane.

### 4. Wysyłanie zmian do zdalnego repozytorium (`git push`) 📤

Kiedy wykonasz commity na swoim komputerze i chcesz je udostępnić, użyj komendy `git push`. Ta komenda wysyła Twoje zmiany do zdalnego repozytorium (domyślnie do `origin` i gałęzi `main` lub `master`).

```bash
git push origin main
```

Dzięki `git push` Twój kod jest teraz dostępny w zdalnym repozytorium i widoczny dla innych osób.

### 5. Pobieranie zmian z repozytorium zdalnego (`git pull`) 📥

Jeśli pracujesz z zespołem, inni mogą wprowadzać zmiany w projekcie, które chcesz zsynchronizować z Twoją lokalną wersją. Aby pobrać najnowsze zmiany z repozytorium zdalnego, użyj `git pull`.

```bash
git pull origin main
```

Ta komenda pobiera wszystkie zmiany z gałęzi `main` (lub innej, jeśli ją podasz) i łączy je z Twoim lokalnym kodem. `git pull` to połączenie dwóch komend: `git fetch` (pobieranie zmian) i `git merge` (łączenie zmian).

### 6. Aktualizacja zdalnego repozytorium (`git fetch`) 👀

Jeśli chcesz jedynie pobrać zmiany z repozytorium zdalnego, ale nie łączyć ich od razu z lokalnym kodem, możesz użyć `git fetch`. Ta komenda aktualizuje informacje o zdalnych zmianach, ale ich nie scala.

```bash
git fetch origin
```

Dzięki `git fetch` zobaczysz najnowsze zmiany w repozytorium zdalnym, a potem możesz zdecydować, czy chcesz je połączyć (np. za pomocą `git merge`).

### Podsumowanie – najważniejsze komendy do repozytoriów zdalnych 🌐

- **`git clone [adres]`** – Sklonowanie zdalnego repozytorium na lokalny komputer.
- **`git remote add origin [adres]`** – Powiązanie lokalnego repozytorium ze zdalnym.
- **`git push origin [gałąź]`** – Wysyłanie commitów do zdalnego repozytorium.
- **`git pull origin [gałąź]`** – Pobieranie i łączenie zmian ze zdalnego repozytorium.
- **`git fetch origin`** – Pobieranie zmian bez łączenia ich z lokalnym kodem.

Dzięki repozytoriom zdalnym możesz współpracować z innymi, mieć dostęp do kopii zapasowych swojego kodu i pracować na różnych komputerach, zachowując ciągłość projektu. Git sprawia, że współpraca i synchronizacja są łatwe i bezpieczne! 🧑‍🤝‍🧑💻

---

### Notatki dla prowadzącego:

#### **1. Gałęzie**
- **Definicja**: Gałęzie to niezależne ścieżki rozwoju projektu.
- **Przykład wizualny**: 
  - master: A -> B -> C -> D -> E -> F
  - feature: A -> B -> C -> D -> E -> F -> G -> H
- **Dlaczego używamy gałęzi?**
  - Stabilny kod w głównej gałęzi.
  - Równoległa praca nad różnymi funkcjami.
  - Rozdzielenie wersji produkcyjnej (master/main) od deweloperskiej (develop).

---

#### **2. Podstawowe operacje na gałęziach**
- **Sprawdzenie dostępnych gałęzi**: `git branch`
- **Utworzenie nowej gałęzi**: `git checkout -b <nazwa gałęzi>`
- **Przełączenie na inną gałąź**: `git checkout <nazwa gałęzi>`
- **Dodanie zmian do aktualnej gałęzi**:
  - `git add <plik>`
  - `git commit -m "<komentarz>"`

---

#### **3. Łączenie gałęzi**
- **Łączenie gałęzi do bieżącej**: `git merge <nazwa gałęzi>`
- **Rozwiązywanie konfliktów:**
  - Oznaczenie konfliktów w pliku: `<<<<<<<`, `=======`, `>>>>>>>`
  - Rozwiązanie konfliktu ręcznie.
  - Zatwierdzenie zmian: 
    - `git add <plik>`
    - `git commit -m "<komentarz>"`

---

#### **4. Praca z repozytoriami zdalnymi**
- **Dodanie repozytorium zdalnego**: `git remote add origin <url>`
- **Kluczowe komendy:**
  - `git fetch` – pobieranie zmian z serwera bez ich scalania.
  - `git pull` – pobieranie i automatyczne scalanie zmian.
  - `git push <repozytorium> <gałąź>` – wysyłanie zmian na serwer.
- **Sprawdzenie gałęzi zdalnych**: `git branch -a`

---

#### **5. Tworzenie repozytorium zdalnego**
- **Nowe repozytorium lokalne + zdalne**:
  - `git clone <url repozytorium>`
- **Istniejące repozytorium lokalne + zdalne**:
  - `git remote add origin <url>`
  - `git push -u origin <gałąź>` – pierwszy push z ustawieniem domyślnego repozytorium.

---

#### **6. Konflikty i ich rozwiązywanie**
- **Scenariusz konfliktu**:
  - Ten sam plik zmodyfikowany w dwóch gałęziach.
  - Próba merge generuje konflikt.
- **Rozwiązanie konfliktu:**
  - Otwórz plik.
  - Usuń oznaczenia `<<<<<<<`, `=======`, `>>>>>>>`.
  - Wybierz właściwą treść lub połącz zmiany.
  - Zatwierdź zmiany: `git add <plik>`, `git commit`.

---

#### **7. Praca w zespole z repozytoriami zdalnymi**
- **Codzienne praktyki:**
  - Regularne push do repozytorium zdalnego.
  - Fetch/pull na początku dnia pracy.
- **Najwięksi dostawcy repozytoriów:**
  - GitHub.
  - GitLab.
  - Bitbucket.

---

#### **8. Zalety repozytoriów zdalnych**
- Bezpieczeństwo – kopia na serwerze.
- Współpraca – ułatwia dzielenie się kodem.
- Narzędzia dodatkowe – pull requesty, komentarze, integracja z bugtrackerami.

---

To lista punktów kluczowych do omówienia. Pozwala na płynne prowadzenie lekcji, koncentrując się na praktycznych aspektach pracy z gałęziami i repozytoriami zdalnymi.