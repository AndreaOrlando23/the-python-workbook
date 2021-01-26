# EXERCISE 62 : Roulette payouts

from random import randrange

# Simulate spinning the wheel, using 37 to represent 00
value = randrange(0, 38)

if value == 37:
    print("The spin resulted in 00...")
else:
    print("The spin resulted in %d..." % value)

# Display the payout for single number
if value == 37:
    print("Pay 00")
else:
    print("Pay", value)

"""
Display the color payout
The first line in the condition checks 1, 3, 5, 7 and 9
The second line in the condition checks for 12, 14, 16 and 18
The third line in the condition checks for 19, 21, 23, 25 and 27
The fourth line in the condition checks for 30, 32, 34 and 36
"""

if value % 2 == 1 and 1 <= value <= 9 or \
    value % 2 == 0 and 12 <= value <= 18 or \
    value % 2 == 1 and 19 <= value <= 27 or \
    value % 2 == 0 and 30 <= value <= 36:
    print("Pay Red")
elif value == 0 or value == 37:
    pass
else:
    print("Pay Black")

# Display the odd vs even payout
if 1 <= value <= 18:
    print("Pay 1 to 18")
elif 19 <= value <= 36:
    print("Pay 19 to 36")
