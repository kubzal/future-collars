from flask import Flask, render_template
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


# Uruchamianie aplikacji
if __name__ == "__main__":
    app.run(debug=True)
