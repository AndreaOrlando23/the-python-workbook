# EXERCISE 69 : Admission price - SOLUTION 1

price_group = []
line = input("Enter the age of guest (blank to quit): ")

while line != "":
    age = int(line)
    if 0 <= age <= 2:
        price = 0
        price_group.append(price)
    elif 3 <= age <= 12:
        price = 14
        price_group.append(price)
    elif age >= 65:
        price = 18
        price_group.append(price)
    else:
        price = 23
        price_group.append(price)

    line = input("Enter the age of guest (blank to quit): ")

bill = sum(price_group)

print("The amount of bill is %.2f $" % bill)
