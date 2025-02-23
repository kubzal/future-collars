print(" * Kółko i krzyżyk * ")
print()
print("Witaj w grze kółko i krzyżyk")
print()
print("Plansza do gry:")
print("1 | 2 | 3")
print("---------")
print("4 | 5 | 6")
print("---------")
print("7 | 8 | 9")
print()

p1 = "-"
p2 = "-"
p3 = "-"
p4 = "-"
p5 = "-"
p6 = "-"
p7 = "-"
p8 = "-"
p9 = "-"

ruch_komputera = True

while True:
    # ruch komputera, komputer jest krzyżykiem

    if ruch_komputera:
        ## pierwszy ruch komputera
        if p5 == "-":
            p5 = "X"

        ## blokada ruchu gracza
        ### poziomo, pierwszy rząd
        elif p1 == "O" and p2 == "O" and p3 == "-":
            p3 = "X"
        elif p1 == "O" and p2 == "-" and p3 == "O":
            p2 = "X"
        elif p1 == "-" and p2 == "O" and p3 == "O":
            p1 = "X"

        ### poziomo, drugi rząd
        # nie ma potrzeby blokady, bo komputer zawsze zaczyna od środka

        ### poziomo, trzeci rząd
        elif p7 == "O" and p8 == "O" and p9 == "-":
            p9 = "X"
        elif p7 == "O" and p8 == "-" and p9 == "O":
            p8 = "X"
        elif p7 == "-" and p8 == "O" and p9 == "O":
            p7 = "X"

        ### pionowo, pierwsza kolumna
        elif p1 == "O" and p4 == "O" and p7 == "-":
            p7 = "X"
        elif p1 == "O" and p4 == "-" and p7 == "O":
            p4 = "X"
        elif p1 == "-" and p4 == "O" and p7 == "O":
            p1 = "X"

        ###  pionowo, druga kolumna
        # nie ma potrzeby blokady, bo komputer zawsze zaczyna od środka

        ### pionowo, trzecia kolumna
        elif p3 == "O" and p6 == "O" and p9 == "-":
            p9 = "X"
        elif p3 == "O" and p6 == "-" and p9 == "O":
            p6 = "X"
        elif p3 == "-" and p6 == "O" and p9 == "O":
            p3 = "X"

        ### przekątna, od lewej do prawej
        # nie ma potrzeby blokady, bo komputer zawsze zaczyna od środka

        ### przekątna, od prawej do lewej
        # nie ma potrzeby blokady, bo komputer zawsze zaczyna od środka

        ## ruch wygrywający (dwa pola zajęte przez X)
        ### poziomo, pierwszy rząd
        elif p1 == "X" and p2 == "X" and p3 == "-":
            p3 = "X"
        elif p1 == "X" and p2 == "-" and p3 == "X":
            p2 = "X"
        elif p1 == "-" and p2 == "X" and p3 == "X":
            p1 = "X"

        ### poziomo, drugi rząd
        elif p4 == "X" and p5 == "X" and p6 == "-":
            p6 = "X"
        elif p4 == "X" and p5 == "-" and p6 == "X":
            p5 = "X"
        elif p4 == "-" and p5 == "X" and p6 == "X":
            p4 = "X"

        ### poziomo, trzeci rząd
        elif p7 == "X" and p8 == "X" and p9 == "-":
            p9 = "X"
        elif p7 == "X" and p8 == "-" and p9 == "X":
            p8 = "X"
        elif p7 == "-" and p8 == "X" and p9 == "X":
            p7 = "X"

        ### pionowo, pierwsza kolumna
        elif p1 == "X" and p4 == "X" and p7 == "-":
            p7 = "X"
        elif p1 == "X" and p4 == "-" and p7 == "X":
            p4 = "X"
        elif p1 == "-" and p4 == "X" and p7 == "X":
            p1 = "X"

        ###  pionowo, druga kolumna
        elif p2 == "X" and p5 == "X" and p8 == "-":
            p8 = "X"
        elif p2 == "X" and p5 == "-" and p8 == "X":
            p5 = "X"
        elif p2 == "-" and p5 == "X" and p8 == "X":
            p2 = "X"

        ### pionowo, trzecia kolumna
        elif p3 == "X" and p6 == "X" and p9 == "-":
            p9 = "X"
        elif p3 == "X" and p6 == "-" and p9 == "X":
            p6 = "X"
        elif p3 == "-" and p6 == "X" and p9 == "X":
            p3 = "X"

        ### przekątna, od lewej do prawej
        elif p1 == "X" and p5 == "X" and p9 == "-":
            p9 = "X"
        elif p1 == "X" and p5 == "-" and p9 == "X":
            p5 = "X"
        elif p1 == "-" and p5 == "X" and p9 == "X":
            p1 = "X"

        ### przekątna, od prawej do lewej
        elif p3 == "X" and p5 == "X" and p7 == "-":
            p7 = "X"
        elif p3 == "X" and p5 == "-" and p7 == "X":
            p5 = "X"
        elif p3 == "-" and p5 == "X" and p7 == "X":
            p3 = "X"

        ## ruch gdy dwa pola wolne
        ### przekątna, od lewej do prawej
        elif p1 == "-" and p5 == "X" and p9 == "-":
            p1 = "X"
        ### przekątna, od prawej do lewej
        elif p3 == "-" and p5 == "X" and p7 == "-":
            p3 = "X"
        ### poziomo, pierwszy rząd
        elif p4 == "-" and p5 == "X" and p6 == "-":
            p4 = "X"
        ### pionowo, druga kolumna
        elif p2 == "-" and p5 == "X" and p8 == "-":
            p2 = "X"

    # rysowanie planszy
    print(p1, p2, p3)
    print(p4, p5, p6)
    print(p7, p8, p9)

    # sprawdzanie wygranej
    if p1 == "X" and p2 == "X" and p3 == "X":
        print("Wygrałem!")
        break
    elif p4 == "X" and p5 == "X" and p6 == "X":
        print("Wygrałem!")
        break
    elif p7 == "X" and p8 == "X" and p9 == "X":
        print("Wygrałem!")
        break
    elif p1 == "X" and p4 == "X" and p7 == "X":
        print("Wygrałem!")
        break
    elif p2 == "X" and p5 == "X" and p8 == "X":
        print("Wygrałem!")
        break
    elif p3 == "X" and p6 == "X" and p9 == "X":
        print("Wygrałem!")
        break
    elif p1 == "X" and p5 == "X" and p9 == "X":
        print("Wygrałem!")
        break
    elif p3 == "X" and p5 == "X" and p7 == "X":
        print("Wygrałem!")
        break
    # sprawdzanie remisu
    elif (
        p1 != "-"
        and p2 != "-"
        and p3 != "-"
        and p4 != "-"
        and p5 != "-"
        and p6 != "-"
        and p7 != "-"
        and p8 != "-"
        and p9 != "-"
    ):
        print("Remis!")
        break


    # ruch gracza
    ruch = input("Podaj pole: ")
    if ruch == "1":
        if p1 == "-":
            p1 = "O"
            ruch_komputera = True
        else:
            print("To pole jest już zajęte")
            ruch_komputera = False
            continue
    elif ruch == "2":
        if p2 == "-":
            p2 = "O"
            ruch_komputera = True
        else:
            print("To pole jest już zajęte")
            ruch_komputera = False
            continue
    elif ruch == "3":
        if p3 == "-":
            p3 = "O"
            ruch_komputera = True
        else:
            print("To pole jest już zajęte")
            ruch_komputera = False
            continue
    elif ruch == "4":
        if p4 == "-":
            p4 = "O"
            ruch_komputera = True
        else:
            print("To pole jest już zajęte")
            ruch_komputera = False
            continue
    elif ruch == "5":
        if p5 == "-":
            p5 = "O"
            ruch_komputera = True
        else:
            print("To pole jest już zajęte")
            ruch_komputera = False
            continue
    elif ruch == "6":
        if p6 == "-":
            p6 = "O"
            ruch_komputera = True
        else:
            print("To pole jest już zajęte")
            ruch_komputera = False
            continue
    elif ruch == "7":
        if p7 == "-":
            p7 = "O"
            ruch_komputera = True
        else:
            print("To pole jest już zajęte")
            ruch_komputera = False
            continue
    elif ruch == "8":
        if p8 == "-":
            p8 = "O"
            ruch_komputera = True
        else:
            print("To pole jest już zajęte")
            ruch_komputera = False
            continue
    elif ruch == "9":
        if p9 == "-":
            p9 = "O"
            ruch_komputera = True
        else:
            print("To pole jest już zajęte")
            ruch_komputera = False
            continue
    else:
        print("Nieprawidłowe pole")
        ruch_komputera = False
        continue
