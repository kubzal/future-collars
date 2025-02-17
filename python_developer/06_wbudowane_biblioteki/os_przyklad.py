import os

nazwa_folderu = input("Podaj nazwe folderu: ")

if os.path.exists(nazwa_folderu):

    for plik in os.listdir(nazwa_folderu):
        # print(os.path.join(nazwa_folderu, plik))

        # Szukamy ktory z elementow jest folderem
        if os.path.isdir(os.path.join(nazwa_folderu, plik)):
            # Jezeli jest folderem wykonaj ponizsza petle
            print(f"Folder: {plik}")
            print(f"Ścieżka bezwzględna: {os.path.abspath(plik)}")
            for plik_w_kolejnym_folderze in os.listdir(os.path.join(nazwa_folderu, plik)):
                # Wypisz elementy w folderze
                print(plik_w_kolejnym_folderze)
else:
    print(f"Folder {nazwa_folderu} nie istnieje")