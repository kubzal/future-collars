import sys

# print("Hello Future Collars!")
# print(sys.stdout)

with open("output.txt", "w") as f:
    sys.stdout = sys.__stdout__
    print("Ala ma kota")
    print("Kuba ma psa")

    sys.stdout = f
    print("Kot ma Alę")
    print("Pies ma Kubę")

