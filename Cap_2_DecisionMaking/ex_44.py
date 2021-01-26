# EXERCISE 44 : Faces on money

banknote = int(input("Enter the denomination of a banknote: "))

individual = ""
if banknote == 1:
    individual = "George Washington"
elif banknote == 2:
    individual = "Thomas Jefferson"
elif banknote == 5:
    individual = "Abraham Lincoln"
elif banknote == 10:
    individual = "Alexander Hamilton"
elif banknote == 20:
    individual = "Andrew Jackson"
elif banknote == 50:
    individual = "Ulysses S. Grant"
elif banknote == 100:
    individual = "Benjamin Franklin"

if individual == "":
    print("ERROR: the amount entered not exist")
else:
    print(individual)
