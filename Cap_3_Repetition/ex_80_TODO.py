# EXERCISE 80 : Prime factors

# TODO

n = int(input("Enter a positive integer greater than 2: "))
factor = 2

if n < factor:
    print("Error: the value must be grater than 2")
    n = int(input("Enter a positive integer greater than 2: "))

while factor <= n:
    if n % factor == 0:
        print(n)
        n = (n // factor)
    else:
        factor += 1

print(f"The prime factors of {n}:")
