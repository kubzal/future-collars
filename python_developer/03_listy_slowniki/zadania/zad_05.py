# Zadanie 5: Masz słownik z cenami produktów:
# produkty = {"jabłko": 3.50, "banan": 2.80, "pomarańcza": 4.20, "winogrona": 6.00}
# Wykonaj następujące operacje:
# - Dodaj produkt "gruszka" z ceną 5.00.
# - Usuń produkt "banan".
# - Zaktualizuj cenę "winogrona" do 5.50.
# - Wyświetl ostateczny słownik.

produkty = {"jabłko": 3.50, "banan": 2.80, "pomarańcza": 4.20, "winogrona": 6.00}

# Dodaj gruszkę
produkty["gruszka"] = 5.00

# Usuń banan
produkty.pop("banan")

# Zaktualizuj cenę winogrona
produkty["winogrona"] = 5.50

# Wyświetl ostateczny słownik
print(produkty)
