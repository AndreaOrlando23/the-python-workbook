# EXERCISE 82 : Decimal to Binary

# Convert a number from decimal (base 10) to binary (base 2)

NEW_BASE = 2

num = int(input("Enter a non-negative integer: "))

# Generate the binary representation of num, storing it in result
result = ""
q = num

# Perform the body of the loop once
r = q % NEW_BASE
result = str(r) + result
q = q // NEW_BASE

# Keep on looping of the loop until q is 0
while q > 0:
    r = q % NEW_BASE
    result = str(r) + result
    q = q // NEW_BASE

print(f"{num} in decimal is {result} in binary")
