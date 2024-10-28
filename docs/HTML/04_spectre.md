# Frameworki CSS
### Frameworki CSS – szybka droga do pięknych stron! 🎨🚀

Pisanie stylów od podstaw jest świetne, ale czasami potrzebujemy czegoś, co przyspieszy pracę i da nam gotowy, profesjonalny wygląd bez godzin spędzonych na stylowaniu. Tutaj wkraczają **zewnętrzne frameworki CSS** – zbiory gotowych stylów, które możemy zaimportować i użyć od razu.

#### Przykład: Spectre.css

**[Spectre.css](https://picturepan2.github.io/spectre/)** to lekki framework CSS, który oferuje minimalistyczny, nowoczesny wygląd. Jest świetny do szybkiego budowania eleganckich stron bez zbędnych dodatków. Zawiera stylizację dla przycisków, formularzy, tabel, siatki layoutu i innych elementów, co pozwala łatwo tworzyć spójną stronę.

### Jak używać Spectre.css? 📦

1. **Dodanie frameworka** – Aby zacząć, wystarczy dodać Spectre.css do swojego projektu. Możesz użyć linku CDN w sekcji `<head>`:

    ```html
    <link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre.min.css">
    ```

2. **Korzystanie z gotowych klas** – Framework dostarcza wiele gotowych klas, które wystarczy dodać do elementów HTML. Poniżej kilka przykładów:

    - **Przyciski**:
      ```html
      <button class="btn">Zwykły przycisk</button>
      <button class="btn btn-primary">Przycisk główny</button>
      <button class="btn btn-error">Przycisk z błędem</button>
      ```

    - **Siatka layoutu**:
      Spectre używa klas `.columns` i `.column` do tworzenia siatki opartej na kolumnach, dzięki czemu łatwo rozmieścisz elementy na stronie.
      ```html
      <div class="columns">
          <div class="column col-6">Lewa kolumna (50%)</div>
          <div class="column col-6">Prawa kolumna (50%)</div>
      </div>
      ```

    - **Formularze**:
      Spectre oferuje również klasy do stylizacji formularzy, co pozwala szybko zbudować atrakcyjne, responsywne formularze.
      ```html
      <form>
          <div class="form-group">
              <label for="name">Imię</label>
              <input type="text" class="form-input" id="name" placeholder="Wpisz swoje imię">
          </div>
          <button class="btn btn-primary">Wyślij</button>
      </form>
      ```

Spectre.css to tylko jeden z wielu frameworków CSS, ale jego lekkość i prostota sprawiają, że jest świetnym wyborem na początek. Dzięki niemu możesz stworzyć nowoczesną, responsywną stronę w bardzo krótkim czasie – i przy minimalnym wysiłku!