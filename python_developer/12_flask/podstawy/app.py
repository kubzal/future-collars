from flask import Flask, render_template, request

# Tworzymy instancję aplikacji Flask
app = Flask(__name__)


# Strona główna
@app.route("/")
def home():
    return "Witaj w mojej aplikacji Flask!"


# Przykład przekazywania parametru do adresu URL
@app.route("/greet/<name>")
def greet(name):
    return render_template("greeting.html", name=name)


@app.route("/greet_v2", defaults={"name": None, "country": "pl"})
@app.route("/greet_v2/<name>", defaults={"country": "pl"})
@app.route("/greet_v2/<name>/<country>")
def greet_v2(name, country):
    greetings = {"pl": "Cześć", "en": "Hello", "es": "Hola"}
    greeting = greetings.get(country, "Cześć")  # Domyślnie polskie przywitanie
    return render_template("greeting_v2.html", name=name, greeting=greeting)


# Przykład odbierania parametru z URL jako zapytanie
@app.route("/search")
def search():
    query = request.args.get("query")
    return f"Szukasz: {query}"


# Uruchamianie aplikacji
if __name__ == "__main__":
    app.run(debug=True)
