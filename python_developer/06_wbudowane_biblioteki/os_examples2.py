import os

plik = "plik1.txt"
if os.path.exists(plik):
    os.unlink(plik)

plik = "plik2.txt"
if os.path.exists(plik):
    os.remove(plik)

print("PID", os.getpid())

plik = input("Podaj nazwe pliku:")
if os.path.exists(plik):
    os.rename(plik, f"{plik}2.txt")
else:
    print(f"{plik} nie istnieje")

print(os.system("python --version"))