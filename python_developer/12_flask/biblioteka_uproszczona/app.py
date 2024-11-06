import csv
import os.path

from flask import Flask, request
from flask import render_template

app = Flask(__name__)

CSV_FILE_PATH = "data/books.csv"


class Book:
    def __init__(self, title, author, count):
        self.title = title
        self.author = author
        self.count = int(count)

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, count={self.count})"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "count": self.count}


# Zwraca liste ksiazek z pliku CSV
def get_books():
    books = []
    with open(CSV_FILE_PATH, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            book = Book(title=row["title"], author=row["author"], count=row["count"])
            books.append(book)

        return books


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    # Pobranie danych z formularza
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        count = int(request.form.get("count"))

        books = get_books()

        # Sprawdzenie czy ksiazka juz istnieje
        book_exists = False
        for book in books:
            # Jesli ksiazka istnieje to zwiekszamy liczbe
            if book.title == title and book.author == author:
                book.count += count
                book_exists = True
                break
        
        # Jesli ksiazka nie istnieje to dodajemy nowa
        if not book_exists:
                # Dodanie nowej ksiazki
                books.append(Book(title, author, count))

        with open(CSV_FILE_PATH, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["title", "author", "count"]
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            writer.writerows([book.to_dict() for book in books])

    return render_template("add_book.html", subtitle="Dodaj książkę")


@app.route("/book-list")
def book_list():
    books = get_books()
    return render_template("book_list.html", books=books, subtitle="Lista książek")


@app.route("/borrow-book", methods=["GET", "POST"])
def borrow_book():
    # Pobranie danych z formularza
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        count = int(request.form.get("count"))

        szukana_ksiazka = Book(title, author, count)

        # Szukana ksiazka
        print("Szukana ksiazka:", szukana_ksiazka)

        with open(CSV_FILE_PATH, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            books = []
            for row in reader:
                print(row)
                if row["title"] == title and row["author"] == author:
                    print("Znaleziono ksiazke")
                    dostepne_ksiazki = int(row["count"])
                    if dostepne_ksiazki >= count:
                        # wystarczajca liczba ksiazek
                        row["count"] = str(dostepne_ksiazki - count)
                    else:
                        print("Nie ma wystarczającej liczby ksiązek")
                books.append(row)

            # Zapisz liste ksiazek po wypozyczeniu
            with open(CSV_FILE_PATH, "w", encoding="utf-8") as csvfile:
                fieldnames = ["title", "author", "count"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(books)

    return render_template("borrow_book.html", subtitle="Wypożycz książkę")


@app.route("/operations-history")
def operations_history():
    return render_template("operations_history.html", subtitle="Historia operacji")


if __name__ == "__main__":
    app.run(debug=True)
