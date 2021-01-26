# EXERCISE 101 : Random license plate
from random import randint, random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
L1 = random.choice(letters)
L2 = random.choice(letters)
L3 = random.choice(letters)
L4 = random.choice(letters)

# Find the length of digits for licence plate (3 digits = old, 4 digits = new)
digits = randint(100, 9999)


def random_licence_plate():
    if digits < 999:
        licence_plate = L1 + L2 + L3 + str(digits)
        return licence_plate
    elif digits > 999:
        licence_plate = str(digits) + L1 + L2 + L3 + L4
        return licence_plate


def main():
    print(random_licence_plate())


main()
