import os.path

# sciezka_do_pliku = "moj-folder/plik.txt"

sciezka_do_pliku = os.path.join("moj-folder", "plik.txt")
print(sciezka_do_pliku)
with open(sciezka_do_pliku) as f:
    plik = f.read()
    print(plik)

# os.path.join()
# os.path.exists()
# os.path.isdir()
print(os.path.pardir)
print()

print(os.path.join(os.path.dirname(os.path.abspath(sciezka_do_pliku)), os.pardir))