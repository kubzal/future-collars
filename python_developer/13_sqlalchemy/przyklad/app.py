# ORM (Object-Relational Mapping)

# Przykład użycia SQLAlchemy w aplikacji Flask
# pip install flask flask_sqlalchemy

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import flash

# from flask_alembic import Alembic

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# Ustawienie klucza tajnego dla sesji
app.config["SECRET_KEY"] = "bardzotajnyklucz"

# Konfiguracja bazy danych
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

# Inicjalizacja bazy danych
db = SQLAlchemy(app)

# Inicjalizacja Alembic (później)
# alembic = Alembic(app)
# alembic.init_app(app)

# w terminalu: 
# > flask db revision initial
# > flask db upgrade


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    
    # Późniejsze dodanie kolumny borrowed
    # borrowed = db.Column(db.Boolean, default=False)
    # pip install flask-alembic
    
# Dlaczego używamy app.app_context()?
# Ponieważ tworzymy tabele w kontekście aplikacji Flask.
# W przeciwnym razie, jeśli nie użyjemy app.app_context(),
# SQLAlchemy nie będzie wiedziało, do której aplikacji należy przypisać tabele.

# Tworzenie tabeli w bazie danych
with app.app_context():
    db.create_all()  # Tworzenie tabeli w bazie danych
    

@app.route("/")
def index():
    # new_book = Book(title="Python Programming", author="John Doe", quantity=5)
    
    # ## podstawowy sposób dodawania do bazy danych
    # # db.session.add(new_book)  # Dodanie nowej książki do sesji
    # # db.session.commit()  # Zatwierdzenie sesji
    
    # ## alternatywnie
    # try:
    #     db.session.add(new_book)  # Dodanie nowej książki do sesji
    #     db.session.commit()  # Zatwierdzenie sesji
    # except Exception as e:
    #     db.session.rollback()
    #     print(f"Error: {e}")
    # finally:
    #     db.session.close()  # Zamknięcie sesji
        
    # Pobranie wszystkich książek z bazy danych
    books = Book.query.all()
        
    return render_template("index.html", books=books)


@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        quantity = int(request.form["quantity"])
        
        # Wypisanie danych do konsoli
        print(f"Title: {title}, Author: {author}, Quantity: {quantity}")
        
        # Sprawdzenie, czy książka już istnieje
        book = db.session.query(Book).filter_by(title=title).first()
        
        if book:
            # Jeśli książka już istnieje, zwiększamy jej ilość
            print("Książka już istnieje w bazie danych.")
            print(f"Zwiększamy ilość książki o {quantity}.")
            
            flash(f"Zwiększamy ilość książki {title} o {quantity}.")
            
            book.quantity += quantity
        else:
            # Jeśli książka nie istnieje, tworzymy nowy obiekt Book
            # i dodajemy go do bazy danych
            print("Książka nie istnieje w bazie danych.")
            
            flash(f"Książka {title} została dodana do bazy danych.")
            
            # Tworzenie nowego obiektu Book
            # i dodanie go do bazy danych    
            book = Book(title=title, author=author, quantity=quantity)
            db.session.add(book)  # Dodanie nowej książki do sesji
        
        # Zatwierdzenie sesji (z obu przypadków)
        db.session.commit()

        
        return redirect(url_for("index"))  # Przekierowanie do strony głównej

    return render_template("add_book.html")

@app.route("/delete-book")
def delete_book():
    book_id = request.args.get("book_id")
    book = db.session.query(Book).filter_by(id=book_id).first()
    if book:
        db.session.delete(book)  # Usunięcie książki z sesji
        db.session.commit()  # Zatwierdzenie sesji

        flash(f"Książka {book.title} została usunięta z bazy danych.")
    else:
        flash("Nie znaleziono książki o podanym ID.")
    
    return redirect(url_for("index"))

@app.route("/increment-book")
def increment_book():
    book_id = int(request.args.get("book_id"))
    book = db.session.query(Book).filter_by(id=book_id).first()
    print(f"Zwiększamy ilość książki {book.title} (id = {book.id}) o 1.")
    
    if book:
        book.quantity += 1
        db.session.commit()
        flash(f"Ilość książki {book.title} została zwiększona o 1.")
        
    return redirect(url_for("index"))


    
if __name__ == "__main__":
    app.run(debug=True)