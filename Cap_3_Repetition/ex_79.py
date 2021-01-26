# EXERCISE 79 : Greatest common divisor

n = int(input("Enter a positive integer: "))
m = int(input("Enter a positive integer: "))


d = min(n, m)

while n % d != 0 or m % d != 0:
    d -= 1

print(f"The greatest common divisor of {n} and {m} is {d}")
