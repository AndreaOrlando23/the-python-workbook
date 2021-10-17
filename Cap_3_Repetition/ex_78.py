# EXERCISE 78 : The Collatz Conjecture

NEW_BASE = 2

num = int(input('Enter a non-negative integer: '))
result = ""
q = num

r = q % NEW_BASE
result = str(r) + result
q = q // NEW_BASE

while q > 0:
    r = q % NEW_BASE
    result = str(r) + result
    q = q // NEW_BASE

print(f"{num} in decimal is {result} in binary")
