import os
import csv

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash

from models import Book

CSV_FILE_PATH = "data/books.csv"
HISTORY_FILE_PATH = "data/history.csv"


def log_operation(operation, title, author, count, user="Admin"):
    try:
        with open(HISTORY_FILE_PATH, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["date", "operation", "title", "author", "count", "user"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header only if file is empty
            if os.path.getsize(HISTORY_FILE_PATH) == 0:
                writer.writeheader()

            writer.writerow(
                {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "operation": operation,
                    "title": title,
                    "author": author,
                    "count": count,
                    "user": user,
                }
            )
    except Exception as e:
        print(f"Error logging operation: {e}")


def get_books():
    books = []

    if not os.path.exists(CSV_FILE_PATH):
        raise FileNotFoundError(f"File {CSV_FILE_PATH} not found")

    with open(CSV_FILE_PATH, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book = Book(title=row["title"], author=row["author"], count=row["count"])
            books.append(book)
    return books


def get_history():
    history = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    history_file = os.path.join(BASE_DIR, "data", "history.csv")

    if not os.path.exists(history_file):
        return history  # Return empty list if the file doesn't exist

    with open(history_file, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            history.append(row)
    return history


app = Flask(__name__)
app.secret_key = "super_tajny_klucz"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        # Retrieve form data
        title = request.form.get("title")
        author = request.form.get("author")
        count = request.form.get("count")

        # Create a Book instance
        book = Book(title=title, author=author, count=count)

        try:
            # Save the book to the CSV file
            with open(CSV_FILE_PATH, "a", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["title", "author", "count"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write header only if file is empty
                if os.path.getsize(CSV_FILE_PATH) == 0:
                    writer.writeheader()

                writer.writerow(book.to_dict())

            # Log the operation
            log_operation("Dodano książkę", title, author, count)

            # Flash a success message with book details
            flash(
                f'Dodano książkę: "{title}", Autor: {author}, Liczba sztuk: {count}.',
                "success",
            )
            return render_template("add_book.html", subtitle="Dodaj książkę")
        except Exception as e:
            flash(f"Wystąpił błąd podczas dodawania książki: {e}", "error")
            return render_template("add_book.html", subtitle="Dodaj książkę")
    else:
        return render_template("add_book.html", subtitle="Dodaj książkę")


@app.route("/book-list")
def book_list():
    books = get_books()
    return render_template("book_list.html", subtitle="Lista ksiąek", books=books)


@app.route("/update_book_count", methods=["POST"])
def update_book_count():
    title = request.form.get("title")
    author = request.form.get("author")
    action = request.form.get("action")

    books = []
    book_found = False
    try:
        # Read current books
        with open(CSV_FILE_PATH, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["title"] == title and row["author"] == author:
                    book_found = True
                    count = int(row["count"])
                    if action == "increase":
                        count += 1
                        row["count"] = str(count)
                        flash(
                            f'Liczba sztuk książki "{title}" została zwiększona.',
                            "success",
                        )
                        # Log the operation
                        log_operation("Zwiększono liczbę książek", title, author, 1)
                    elif action == "decrease":
                        if count > 0:
                            count -= 1
                            row["count"] = str(count)
                            flash(
                                f'Liczba sztuk książki "{title}" została zmniejszona.',
                                "success",
                            )
                            # Log the operation
                            log_operation(
                                "Zmniejszono liczbę książek", title, author, 1
                            )
                        else:
                            flash(
                                f'Liczba sztuk książki "{title}" nie może być mniejsza niż zero.',
                                "error",
                            )
                            # No change to count
                    else:
                        flash("Nieznana akcja.", "error")
                books.append(row)
        if not book_found:
            flash("Książka nie została znaleziona.", "error")

        # Write updated books back to CSV
        with open(CSV_FILE_PATH, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["title", "author", "count"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(books)

        return redirect(url_for("book_list"))
    except Exception as e:
        flash(f"Wystąpił błąd: {e}", "error")
        return redirect(url_for("book_list"))


@app.route("/borrow_book", methods=["GET", "POST"])
def borrow_book():
    # Ensure the data directory and CSV file path
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(BASE_DIR, "data", "books.csv")

    # Get unique titles and authors
    books = get_books()
    titles = sorted(set(book.title for book in books))
    authors = sorted(set(book.author for book in books))

    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        count = int(request.form.get("count"))

        books = []
        book_found = False
        try:
            # Read the books
            with open(csv_file_path, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["title"] == title and row["author"] == author:
                        book_found = True
                        available_count = int(row["count"])
                        if available_count >= count:
                            # Enough books are available
                            row["count"] = str(available_count - count)
                            flash("Książka została wypożyczona pomyślnie!", "success")
                        else:
                            # Not enough books
                            flash(
                                "Nie ma wystarczającej liczby książek do wypożyczenia.",
                                "error",
                            )
                            return render_template(
                                "borrow_book.html",
                                subtitle="Wypożycz książkę",
                                titles=titles,
                                authors=authors,
                            )
                    books.append(row)
            if not book_found:
                flash("Podana książka nie istnieje w bazie.", "error")
                return render_template(
                    "borrow_book.html",
                    subtitle="Wypożycz książkę",
                    titles=titles,
                    authors=authors,
                )

            # Write the updated books
            with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["title", "author", "count"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(books)

            # Log the operation
            log_operation("Wypożyczono książkę", title, author, count)

            return render_template(
                "borrow_book.html",
                subtitle="Wypożycz książkę",
                titles=titles,
                authors=authors,
            )
        except Exception as e:
            flash(f"Wystąpił błąd: {e}", "error")
            return render_template("borrow_book.html", titles=titles, authors=authors)
    else:
        return render_template(
            "borrow_book.html",
            subtitle="Wypożycz książkę",
            titles=titles,
            authors=authors,
        )


@app.route("/operations_history")
def operations_history():
    history = get_history()
    return render_template(
        "operations_history.html", subtitle="Historia operacji", history=history
    )


if __name__ == "__main__":
    app.run(debug=True)
