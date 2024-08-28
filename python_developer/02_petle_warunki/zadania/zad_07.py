# Zadanie 7: Zgadnij liczbę
# Opis: Napisz program, który pozwoli użytkownikowi zgadywać liczbę z przedziału od 1 do 5.
# Program powinien używać pętli while, aby kontynuować zgadywanie, dopóki użytkownik nie trafi.

tajna_liczba = 3
zgadnij = int(input("Zgadnij liczbę od 1 do 5: "))

while zgadnij != tajna_liczba:
    print("Spróbuj ponownie!")
    zgadnij = int(input("Zgadnij liczbę od 1 do 5: "))

print("Brawo! Zgadłeś!")
