# Zadanie: System Zarządzania Zamówieniami w Restauracji
#
# Opis:
# Twoim zadaniem jest napisanie prostego programu do zarządzania zamówieniami w
# restauracji. Program ma umożliwiać klientom składanie zamówień na wybrane dania,
# a następnie podsumować ich zamówienie, wyliczając łączny koszt. Dodatkowo, program
# powinien umożliwiać dodanie napiwku.
#
# Założenia:
# 1. Restauracja oferuje cztery dania: Pizza, Burger, Sałatka, Zupa.
# 2. Ceny dań są następujące:
#    - Pizza: 25 PLN
#    - Burger: 20 PLN
#    - Sałatka: 15 PLN
#    - Zupa: 10 PLN
# 3. Program powinien umożliwiać klientowi wielokrotne składanie zamówień, aż do
#    momentu wpisania komendy 'koniec', która zakończy proces zamawiania.
# 4. Program powinien weryfikować poprawność wprowadzonych danych:
#    - Jeżeli klient wybierze danie, które nie istnieje w menu, program powinien
#      poinformować o tym i pozwolić na ponowne wprowadzenie.
#    - Jeżeli klient poda nieprawidłową ilość (np. wartość ujemną lub zero),
#      program powinien poprosić o ponowne wprowadzenie tej ilości.
# 5. Po zakończeniu składania zamówienia, program powinien wyświetlić podsumowanie
#    zamówionych dań wraz z ich ilością i łącznym kosztem.
# 6. Program powinien umożliwić klientowi dodanie napiwku w procentach. Wartość
#    napiwku powinna być doliczona do całkowitej kwoty zamówienia.
# 7. Po obliczeniu całkowitej kwoty (z napiwkiem), program wyświetla finalną kwotę
#    do zapłaty i kończy działanie.


# Ceny poszczególnych dań
CENA_PIZZA = 25
CENA_BURGER = 20
CENA_SALATKA = 15
CENA_ZUPA = 10

# Zmienne do przechowywania ilości zamówionych dań
ilosc_pizza = 0
ilosc_burger = 0
ilosc_salatka = 0
ilosc_zupa = 0

print("Witamy w naszej restauracji! Oto nasze menu:")
print(f"Pizza: {CENA_PIZZA} PLN")
print(f"Burger: {CENA_BURGER} PLN")
print(f"Sałatka: {CENA_SALATKA} PLN")
print(f"Zupa: {CENA_ZUPA} PLN")

# Pętla do składania zamówienia
while True:
    wybor = input(
        "\nCo chcesz zamówić? (wpisz 'koniec' aby zakończyć składanie zamówienia): "
    ).lower()

    if wybor == "koniec":
        break

    if wybor == "pizza":
        ilosc = int(input(f"Ile porcji pizzy chcesz zamówić? "))
        if ilosc > 0:
            ilosc_pizza += ilosc
            print(f"Dodano {ilosc}x Pizza do Twojego zamówienia.")
        else:
            print("Ilość musi być większa niż zero. Spróbuj ponownie.")
        continue

    elif wybor == "burger":
        ilosc = int(input(f"Ile porcji burgera chcesz zamówić? "))
        if ilosc > 0:
            ilosc_burger += ilosc
            print(f"Dodano {ilosc}x Burger do Twojego zamówienia.")
        else:
            print("Ilość musi być większa niż zero. Spróbuj ponownie.")
        continue

    elif wybor == "salatka":
        ilosc = int(input(f"Ile porcji sałatki chcesz zamówić? "))
        if ilosc > 0:
            ilosc_salatka += ilosc
            print(f"Dodano {ilosc}x Sałatka do Twojego zamówienia.")
        else:
            print("Ilość musi być większa niż zero. Spróbuj ponownie.")
        continue

    elif wybor == "zupa":
        ilosc = int(input(f"Ile porcji zupy chcesz zamówić? "))
        if ilosc > 0:
            ilosc_zupa += ilosc
            print(f"Dodano {ilosc}x Zupa do Twojego zamówienia.")
        else:
            print("Ilość musi być większa niż zero. Spróbuj ponownie.")
        continue

    else:
        print("Przepraszamy, nie mamy tego dania. Proszę wybrać coś z menu.")
        continue

# Podsumowanie zamówienia
print("\nTwoje zamówienie:")
suma = 0

if ilosc_pizza > 0:
    koszt_pizza = ilosc_pizza * CENA_PIZZA
    suma += koszt_pizza
    print(f"{ilosc_pizza}x Pizza - {koszt_pizza} PLN")

if ilosc_burger > 0:
    koszt_burger = ilosc_burger * CENA_BURGER
    suma += koszt_burger
    print(f"{ilosc_burger}x Burger - {koszt_burger} PLN")

if ilosc_salatka > 0:
    koszt_salatka = ilosc_salatka * CENA_SALATKA
    suma += koszt_salatka
    print(f"{ilosc_salatka}x Sałatka - {koszt_salatka} PLN")

if ilosc_zupa > 0:
    koszt_zupa = ilosc_zupa * CENA_ZUPA
    suma += koszt_zupa
    print(f"{ilosc_zupa}x Zupa - {koszt_zupa} PLN")

if suma == 0:
    print("Nie złożyłeś żadnego zamówienia.")
else:
    print(f"Łączna kwota do zapłaty: {suma} PLN")

    # Opcjonalny warunek dotyczący napiwku
    napiwek = input("Czy chcesz dodać napiwek? (tak/nie): ").lower()

    if napiwek == "tak":
        procent = int(input("Ile procent napiwku chcesz dodać? "))
        kwota_napiwku = (suma * procent) / 100
        suma += kwota_napiwku
        print(f"Dodano {kwota_napiwku:.2f} PLN jako napiwek.")

    print(f"Całkowita kwota do zapłaty (z napiwkiem): {suma:.2f} PLN")
    print("Dziękujemy za zamówienie!")
