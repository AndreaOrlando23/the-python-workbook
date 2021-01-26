# EXERCISE 16 : Area and Volume
import math

radius = float(input('Enter the radius: '))

area = math.pi * radius ** 2
volume = 4 / 3 * math.pi * radius ** 3

print('The area of a circle with radius %.2f is %.2f' % (radius, area))
print('The volume of a circle with radius %.2f is %.2f' % (radius, volume))
