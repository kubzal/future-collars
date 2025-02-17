import sys

class Tee:
    def __init__(self, file):
        self.file = file
        self.console = sys.stdout

    def write(self, data):
        self.file.write(data)
        self.console.write(data)

    def flush(self):
        self.file.flush()
        self.console.flush()

with open("output2.txt", "w") as f:
    sys.stdout = Tee(f)

    print("ten tekst trafi do konsoli i trafi do pliku")
    print("ten tez")

sys.stdout = sys.__stdout__
print("a to juz trafi tylko do konsoli")