# Formularze
### Formularze – interakcja z użytkownikiem! 📋💌

Formularze w HTML to sposób, aby uzyskać dane od użytkownika – mogą to być informacje kontaktowe, komentarze, dane do logowania i wiele więcej. Formularze składają się z różnych pól, przycisków i elementów, które użytkownik wypełnia, a potem wysyła za pomocą przycisku.

Przykładowy formularz:

```html
<form action="/submit_form" method="post">
    <label for="name">Imię:</label>
    <input type="text" id="name" name="name" required><br><br>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required><br><br>

    <label for="message">Wiadomość:</label><br>
    <textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>

    <input type="submit" value="Wyślij">
</form>
```

### Co się tu dzieje? 📥

- **`<form action="..." method="..."`** – `<form>` otwiera formularz. `action` wskazuje, gdzie dane mają być wysłane, a `method` (zwykle `post` lub `get`) mówi, w jaki sposób dane mają być przesłane.
  
- **`<input type="text">`** – To pole tekstowe do wpisywania pojedynczej linii tekstu, np. imienia.

- **`<input type="email">`** – Pole do wpisania adresu e-mail. Przeglądarka sprawdzi, czy to prawidłowy adres.

- **`<textarea>`** – Większe pole tekstowe na dłuższą wiadomość. Możesz ustawić ilość wierszy i kolumn (`rows` i `cols`).

- **`<input type="submit">`** – Przycisk wysyłający formularz, dzięki któremu dane zostaną przesłane pod adres podany w `action`.

Formularze są niesamowicie elastyczne – można dodawać pola wyboru, listy rozwijane i wiele innych elementów, by dostosować je do potrzeb. Dzięki nim użytkownicy mogą wysyłać dane, a Ty możesz je odbierać i przetwarzać.