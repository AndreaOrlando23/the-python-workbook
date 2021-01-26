# EXERCISE 13 : Making change

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

print(' ', cents // CENTS_PER_PENNIE, 'pennies')
cents = cents % CENTS_PER_PENNIE
