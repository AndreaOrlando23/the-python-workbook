# EXERCISE 41 : Classifying triangles

a = float(input('Enter the length of first side of a triangle: '))
b = float(input('Enter the length of second side of a triangle: '))
c = float(input('Enter the length of third side of a triangle: '))

if a + b + c < 3:
    print('ERROR: all length of sides must be positive and greater than 0')
elif a == b == c:
    print('Equilateral')
elif a == b or b == c or c == a:
    print('Isosceles')
elif a != b and b != c and c != a:
    print('Scalene')
