# Podstawy HTML
### Co oznaczają te wszystkie tajemnicze tagi? 👀

- **`<!DOCTYPE html>`** – Mówi przeglądarce, że używamy HTML5, najnowszej wersji języka HTML.
- **`<html>`** – Otwiera główny blok strony HTML.
- **`<head>`** – To miejsce na metadane, czyli informacje o stronie, takie jak tytuł (`<title>`) i różne ustawienia.
- **`<title>`** – Tytuł strony wyświetlany na karcie przeglądarki.
- **`<body>`** – Tutaj umieszczasz wszystko, co chcesz, aby pojawiło się na stronie: teksty, zdjęcia, listy, nagłówki itd.

### Podstawowe Tagi HTML – Elementy, bez których strona nie istnieje! 🧱

#### 1. **Nagłówki (`<h1>`, `<h2>` ... `<h6>`)**

Nagłówki to tytuły i podtytuły na stronie. HTML oferuje sześć poziomów nagłówków, od `<h1>` (najważniejszy, największy) do `<h6>` (najmniej ważny, najmniejszy).

```html
<h1>To jest główny nagłówek</h1>
<h2>A to jest podtytuł</h2>
```

#### 2. **Paragraf (`<p>`)**

Dla zwykłego tekstu używamy tagu **`<p>`**. Każdy paragraf jest wyświetlany w osobnej linii.

```html
<p>HTML to podstawowy język tworzenia stron internetowych.</p>
```

#### 3. **Link (`<a>`)**

Chcesz, żeby użytkownik mógł przejść na inną stronę? Użyj tagu **`<a>`**. Pamiętaj, aby podać adres w atrybucie `href`.

```html
<a href="https://www.example.com">Kliknij, aby odwiedzić przykład!</a>
```

#### 4. **Obraz (`<img>`)**

Aby dodać obrazek, używamy **`<img>`** i ustawiamy jego źródło (adres obrazka) za pomocą `src`.

```html
<img src="obrazek.jpg" alt="Opis obrazka" width="300">
```

#### 5. **Lista uporządkowana (`<ul>`) i elementy listy (`<li>`)**

Listy uporządkowane, czyli wypunktowane, tworzymy za pomocą **`<ul>`**, a każdy element listy za pomocą **`<li>`**.

```html
<ul>
    <li>Jabłka</li>
    <li>Banany</li>
    <li>Pomarańcze</li>
</ul>
```

#### 6. **Tabela (`<table>`)**

Jeśli potrzebujesz tabelki do danych, użyj tagu **`<table>`**. Wewnątrz mamy tagi na rzędy **`<tr>`**, komórki nagłówkowe **`<th>`**, oraz zwykłe komórki **`<td>`**.

```html
<table border="1">
    <tr>
        <th>Imię</th>
        <th>Wiek</th>
    </tr>
    <tr>
        <td>Kuba</td>
        <td>30</td>
    </tr>
    <tr>
        <td>Ola</td>
        <td>25</td>
    </tr>
</table>
```

#### 7. **Przerwa (`<br>`)**

Tag **`<br>`** dodaje przerwę, przełamując linię – jak wciśnięcie "Enter" na klawiaturze.

```html
<p>To jest tekst.<br>Przeszedłem do nowej linii.</p>
```

#### 8. **Font (niestandardowe kolory i rozmiary)**

Tag **`<font>`** był kiedyś używany do ustawiania koloru i rozmiaru tekstu, ale w nowoczesnym HTML używamy CSS do stylowania. Mimo to, warto znać, że kiedyś działał tak:

```html
<font color="blue" size="4">To jest tekst w niebieskim kolorze.</font>
```

### Podsumowanie:

- **Nagłówki (`<h1>`, `<h2>`...)** – Tworzą hierarchię tytułów.
- **Paragraf (`<p>`)** – Zwykły tekst.
- **Link (`<a href="...">`)** – Klikalny odnośnik.
- **Obraz (`<img src="...">`)** – Dodaje obrazek.
- **Lista (`<ul>` i `<li>`)** – Tworzy listy wypunktowane.
- **Tabela (`<table>`)** – Do prezentowania danych w wierszach i kolumnach.
- **Przerwa (`<br>`)** – Przełamanie linii.

HTML to prosty, ale potężny sposób na budowanie stron internetowych. Z tymi podstawowymi elementami możesz stworzyć strukturę swojej strony, a potem wystylizować ją i urozmaicić, jak tylko sobie wymarzysz! 🌟