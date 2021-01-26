# EXERCISE 66 : No more Pennies

PENNIES_FOR_NICKEL = 5
NICKEL = 0.05

# Track the total cost for all the item
total = 0.00

line = input("Enter the price of item (blank to quit): ")

while line != "":
    # Add the cost of the item to the total(after converting it to a floating-point number)
    total += float(line)

    # Read the cost of the next item
    line = input("Enter the price of item (blank to quit): ")

print("The exact amount payable is %.02f" % total)

# Compute the number of pennies that would be left if the total was paid using nickels
rounding_indicator = total * 100 % PENNIES_FOR_NICKEL

if rounding_indicator < PENNIES_FOR_NICKEL / 2:
    # if the number of pennies left is less than 2.5 then we round down by subtracting that
    # number of pennies from the total
    cash_total = total - rounding_indicator / 100
else:
    # Otherwise we add a nickel and then subtract that number of pennies
    cash_total = total + NICKEL - rounding_indicator / 100

print("The cash amount payable is %.02f" % cash_total)
