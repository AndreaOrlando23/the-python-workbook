# Negatives, Zeros and Positives

negatives = []
zeros = []
positives = []

value = input("Enter a value (blank to quit): ")

# Read all the values from the user storing each integer in the correct list
while value != "":
    num = int(value)

    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    elif num > 0:
        positives.append(num)

    value = input("Enter a value (blank to quit): ")

# Display negatives, then zeros, then positives
for i in negatives:
    print(i)

for i in zeros:
    print(i)

for i in positives:
    print(i)