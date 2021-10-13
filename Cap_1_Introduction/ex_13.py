# EXERCISE 13 : Making change

CENTS_PER_TWO_EURO = 200
CENTS_PER_ONE_EURO = 100
HALF_EURO = 50
TWENTY_CENTS = 20
TEN_CENTS = 10
FIVE_CENTS = 5
ONE_CENTS = 1

euro = float(input('Enter the number of euro: '))
cents = euro * 100

print(' {}  x  2.00 €'.format(int(cents // CENTS_PER_TWO_EURO)))
cents = cents % CENTS_PER_TWO_EURO

print(' {}  x  1.00 €'.format(int(cents // CENTS_PER_ONE_EURO)))
cents = cents % CENTS_PER_ONE_EURO

print(' {}  x  0.50 €'.format(int(cents // HALF_EURO)))
cents = cents % HALF_EURO

print(' {}  x  0.20 €'.format(int(cents // TWENTY_CENTS)))
cents = cents % TWENTY_CENTS

print(' {}  x  0.10 €'.format(int(cents // TEN_CENTS)))
cents = cents % TEN_CENTS

print(' {}  x  0.05 €'.format(int(cents // FIVE_CENTS)))
cents = cents % FIVE_CENTS

print(' {}  x  0.01 €'.format(int(cents // ONE_CENTS)))
cents = cents % ONE_CENTS






"""
---BOOK VERSION---

CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 15
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5
CENTS_PER_PENNIE = 1

cents = int(input('Enter the number of cents: '))

# Determine the number of toonies by performing an integer division by 200.
# Then compute the amount of change that still needs to be considered by computing the remainder after dividing by 200.
# Repeat the process for loonies, quarters, dimes, nickels and pennies

print(' ', cents // CENTS_PER_TOONIE, 'toonies')
cents = cents % CENTS_PER_TOONIE

print(' ', cents // CENTS_PER_LOONIE, 'loonies')
cents = cents % CENTS_PER_LOONIE

print(' ', cents // CENTS_PER_QUARTER, 'quarters')
cents = cents % CENTS_PER_QUARTER

print(' ', cents // CENTS_PER_DIME, 'dimes')
cents = cents % CENTS_PER_DIME

print(' ', cents // CENTS_PER_NICKEL, 'nickels')
cents = cents % CENTS_PER_NICKEL

print(' ', cents, 'pennies')
# print(' ', cents // CENTS_PER_PENNIE, 'pennies')
# cents = cents % CENTS_PER_PENNIE
"""
