# EXERCISE 23 : Area of a regular polygon
import math

s = float(input('Enter the length of each sides: '))
n = int(input('Enter the number of sides: '))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print('The area of the polygon is %.2f' % area)
