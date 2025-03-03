import random


class Sensor:
    """Klasa symulująca czujnik temperatury."""

    def __init__(self, location: str):
        self.location = location

    def read_temperature(self) -> float:
        """Symuluje odczyt temperatury."""
        return round(random.uniform(-10, 40), 2)

    def temperature_stream(self):
        """Generator strumienia temperatur."""
        while True:
            yield self.read_temperature()


# Przykład użycia:
kitchen_sensor = Sensor("Kitchen")
temp_gen = kitchen_sensor.temperature_stream()

# Pobranie kilku pierwszych odczytów
for _ in range(5):
    print(f"Temperature: {next(temp_gen)} °C")
