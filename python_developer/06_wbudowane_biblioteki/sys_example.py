import sys

print("Nazwa skryptu:", sys.argv[0])
print("System path:", sys.path)
print("Executable path:", sys.executable)
print("Python version:", sys.version)
print("Platform:", sys.platform)
print("Max size:", sys.maxsize)

MIN_VERSION = 12
# Sprawdz czy Python w wersji 3
if sys.version_info.major == 3:
    print("Python w wersji 3")
    if sys.version_info.minor > MIN_VERSION:
        print(f"Twój Python jest OK :)")
    else:
        print("Twój Python jest za stary :(")
    print(f"Masz Pythona w wersji 3.{sys.version_info.minor}, minimalna wymagana to 3.{MIN_VERSION}")
else:
    print("Python musi być w wersji 3.X")
