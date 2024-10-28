# Arkusze stylów
### CSS – Styl i wygląd Twojej strony! 🎨✨

HTML tworzy strukturę strony, ale to CSS (Cascading Style Sheets) sprawia, że wygląda ona pięknie i profesjonalnie. CSS to język stylowania, który pozwala na kontrolowanie kolorów, czcionek, układów i innych wizualnych elementów Twojej strony. Dzięki CSS możesz przekształcić surowy HTML w prawdziwe dzieło sztuki!

#### Jak działa CSS? 🎭

CSS działa jak „ubranie” dla HTML – mówisz przeglądarce, jak każdy element ma wyglądać, definiując zasady dla wybranych tagów. Te zasady składają się z selektorów (czyli tego, co chcesz wystylizować) i deklaracji (czyli co chcesz z tym zrobić).

Przykład:
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: lightblue;
            font-family: Arial, sans-serif;
        }

        h1 {
            color: darkblue;
            text-align: center;
        }

        p {
            color: darkgray;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>Witaj na mojej pięknej stronie!</h1>
    <p>CSS sprawia, że HTML wygląda po prostu cudownie.</p>
</body>
</html>
```

#### Składnia CSS – Jak to działa?

CSS składa się z selektorów (czyli elementów, które chcemy stylizować) i deklaracji (co dokładnie chcemy zmienić).

```css
h1 {
    color: darkblue;
    text-align: center;
}
```

- **`h1`** – Selektor wskazujący, że chcemy zmieniać styl nagłówków `<h1>`.
- **`color: darkblue;`** – Deklaracja, która ustawia kolor tekstu na ciemnoniebieski.
- **`text-align: center;`** – Ustawia wyrównanie tekstu do środka.

#### Najważniejsze właściwości CSS, które warto znać 🛠️

1. **Kolor** – Za pomocą `color` ustawiamy kolor tekstu, a `background-color` ustala kolor tła.

    ```css
    p {
        color: #333333;  /* kolor tekstu */
        background-color: #f0f0f0;  /* kolor tła */
    }
    ```

2. **Czcionki** – `font-family` wybiera czcionkę, `font-size` ustala rozmiar tekstu, a `font-weight` pozwala na zmianę grubości.

    ```css
    body {
        font-family: Arial, sans-serif;
        font-size: 16px;
        font-weight: bold;
    }
    ```

3. **Wyrównanie** – `text-align` pozwala ustawić wyrównanie tekstu (lewo, prawo, środek).

    ```css
    h1 {
        text-align: center;
    }
    ```

4. **Marginesy i odstępy** – `margin` kontroluje odstęp na zewnątrz elementu, a `padding` na wewnątrz.

    ```css
    .box {
        margin: 20px;
        padding: 15px;
    }
    ```

5. **Obramowania** – Dzięki `border` możesz dodać ramkę do elementu.

    ```css
    img {
        border: 2px solid black;
    }
    ```

### Gdzie umieścić CSS? 🏠

CSS można dodawać na trzy sposoby:

1. **Style wewnętrzne** – Bezpośrednio w kodzie HTML, wewnątrz `<style>` w `<head>` (tak jak w przykładzie).
2. **Style zewnętrzne** – W osobnym pliku `.css`, który jest podłączony do HTML za pomocą `<link>`.
    ```html
    <link rel="stylesheet" href="style.css">
    ```
3. **Style liniowe** – Wewnątrz konkretnego tagu HTML, za pomocą `style`, np. `<p style="color: red;">`.

### Podsumowanie

CSS daje Ci pełną kontrolę nad wyglądem Twojej strony. Dzięki niemu możesz zmieniać kolory, czcionki, rozmiary i położenie elementów – wszystko po to, aby stworzyć stronę, która nie tylko działa, ale też wygląda niesamowicie! 🌟