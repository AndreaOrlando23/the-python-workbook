# EXERCISE 69 : Admission price - SOLUTION 2

# Store the admission prices as constants
BABY_PRICE = 0.00
CHILD_PRICE = 14.00
ADULT_PRICE = 23.00
SENIOR_PRICE = 18.00

# Store the age limits as constants
BABY_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64

# Create a variable to hold the total admission cost for all guests
total = 0

# Keep on reading ages until the user enters a blank line
line = input("Enter the age of the guest (blank to quit): ")

while line != "":
    age = int(line)

    # Add the correct amount to the total
    if age <= BABY_LIMIT:
        total += BABY_PRICE
    elif age <= CHILD_LIMIT:
        total += CHILD_PRICE
    elif age <= ADULT_LIMIT:
        total += ADULT_PRICE
    else:
        total += SENIOR_PRICE

    # Read the next age from the user
    line = input("Enter the age of the guest (blank to quit): ")

print("The total for that group is $%.2f" % total)
