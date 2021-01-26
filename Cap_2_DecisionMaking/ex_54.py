# EXERCISE 54 : Assigning Employees

# Grade of employees performance
UNACCEPTABLE = 0.0
ACCEPTABLE = 0.4
MERITORIOUS = 0.6  # or more
RAISE = 2400

table = "TABLE OF RATINGS\nUNACCEPTABLE = 0.0\nACCEPTABLE = 0.4\nMERITORIOUS = 0.6 (or more)"
print(table)
print()

rating = float(input("Enter your rating: "))
amount = 0

if rating == UNACCEPTABLE:
    amount = RAISE * rating
elif rating == ACCEPTABLE:
    amount = RAISE * rating
elif rating >= MERITORIOUS:
    amount = RAISE * rating

if rating == UNACCEPTABLE or rating == ACCEPTABLE or rating >= MERITORIOUS:
    print("The amount raise of your rating %.1f is %.2f $" % (rating, amount))
else:
    print("ERROR: please enter a correct value of rating (see the table)")
