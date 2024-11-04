from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)


# Funkcja do wczytywania danych z pliku CSV
def load_users_from_csv():
    users = []
    with open("users.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users


# Funkcja do zapisywania nowego użytkownika do pliku CSV
def save_user_to_csv(imie, nazwisko, wiek, miasto, login):
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([imie, nazwisko, wiek, miasto, login])


# Endpoint do wyświetlania użytkowników jako lista
@app.route("/lista")
def user_list():
    users = load_users_from_csv()
    return render_template("user_list.html", users=users)


# Endpoint do wyświetlania użytkowników w tabeli
@app.route("/tabela")
def user_table():
    users = load_users_from_csv()
    return render_template("user_table.html", users=users)


# Endpoint do dodawania użytkownika przez formularz
@app.route("/dodaj_uzytkownika", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        imie = request.form["imie"]
        nazwisko = request.form["nazwisko"]
        wiek = request.form["wiek"]
        miasto = request.form["miasto"]
        login = request.form["login"]
        save_user_to_csv(imie, nazwisko, wiek, miasto, login)
        return redirect(url_for("user_table"))
    return render_template("add_user.html")


# Uruchamianie aplikacji
if __name__ == "__main__":
    app.run(debug=True)
