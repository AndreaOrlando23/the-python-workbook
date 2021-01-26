# EXERCISE 18 : Volume of a Cylinder
import math

radius = float(input('Enter the radius: '))
height = float(input('Enter the height: '))

area_base = math.pi * radius ** 2
volume = area_base * height

print('The volume of the Cylinder is: %.2f' % volume)
