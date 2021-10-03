# EXERCISE 71 : Approximate pi

# pi = ~3 + (4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - 4/(12*13*14) ... )

# set first parameters for the first term operation
a = 2
b = 3
c = 4

first_term = 4 / (a * b * c)
second_term = 4 / ((a+2) * (b+2) * (c+2))

approximation = first_term - second_term

# Set a, b and c for next term operations
a = 4
b = 5
c = 6

index = 1
while index < 16:

    a += 2
    b += 2
    c += 2
    operation1 = 4 / (a * b * c)

    a += 2
    b += 2
    c += 2
    operation2 = 4 / (a * b * c)

    approximation += operation1 - operation2
    index += 1

approximation += 3

print(f"After 15 operation, the approximation of pi is:\n{approximation}")
