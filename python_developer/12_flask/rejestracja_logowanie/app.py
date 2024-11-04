from flask import Flask, render_template, request, redirect, url_for, session
import csv
import os

app = Flask(__name__)
app.secret_key = "twoj_tajny_klucz"  # Sekretna fraza potrzebna do sesji


# Funkcja zapisująca login i hasło do pliku CSV
def save_user_to_csv(username, password):
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])


# Funkcja sprawdzająca login i hasło w pliku CSV
def check_user_in_csv(username, password):
    if not os.path.exists("users.csv"):
        return False
    with open("users.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row == [username, password]:
                return True
    return False


# Strona główna
@app.route("/")
def home():
    return "Witaj w mojej aplikacji Flask!"


# Formularz rejestracji
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        save_user_to_csv(username, password)
        return redirect(url_for("login"))
    return render_template("register.html")


# Formularz logowania
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if check_user_in_csv(username, password):
            session["username"] = username
            return redirect(url_for("welcome"))
        else:
            return "Nieprawidłowy login lub hasło"
    return render_template("login.html")


# Strona powitalna dla zalogowanego użytkownika
@app.route("/welcome")
def welcome():
    if "username" in session:
        return render_template("welcome.html", username=session["username"])
    return redirect(url_for("login"))


# Uruchamianie aplikacji
if __name__ == "__main__":
    app.run(debug=True)
