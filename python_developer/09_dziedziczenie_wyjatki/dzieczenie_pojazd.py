##### bez dziedziczenia #####


class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def uruchom(self):
        print(f"Samochód {self.marka} {self.model} został uruchomiony.")

    def zatrzymaj(self):
        print(f"Samochód {self.marka} {self.model} został zatrzymany.")


class Motocykl:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def uruchom(self):
        print(f"Motocykl {self.marka} {self.model} został uruchomiony.")

    def zatrzymaj(self):
        print(f"Motocykl {self.marka} {self.model} został zatrzymany.")


class Rower:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def uruchom(self):
        print(f"Rower {self.marka} {self.model} został uruchomiony.")

    def zatrzymaj(self):
        print(f"Rower {self.marka} {self.model} został zatrzymany.")


# Tworzenie obiektów
samochod = Samochod("Toyota", "Corolla")
motocykl = Motocykl("Yamaha", "MT-07")
rower = Rower("Kross", "Level")

# Wywoływanie metod
samochod.uruchom()
motocykl.uruchom()
rower.uruchom()

samochod.zatrzymaj()
motocykl.zatrzymaj()
rower.zatrzymaj()


##### z dziedziczeniem #####


# Klasa bazowa Pojazd
class Pojazd:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def uruchom(self):
        print(
            f"{self.__class__.__name__} {self.marka} {self.model} został uruchomiony."
        )

    def zatrzymaj(self):
        print(f"{self.__class__.__name__} {self.marka} {self.model} został zatrzymany.")


# Klasy dziedziczące
class Samochod(Pojazd):
    pass


class Motocykl(Pojazd):
    pass


class Rower(Pojazd):
    pass


# Tworzenie obiektów
samochod = Samochod("Toyota", "Corolla")
motocykl = Motocykl("Yamaha", "MT-07")
rower = Rower("Kross", "Level")

# Wywoływanie metod
samochod.uruchom()
motocykl.uruchom()
rower.uruchom()

samochod.zatrzymaj()
motocykl.zatrzymaj()
rower.zatrzymaj()
