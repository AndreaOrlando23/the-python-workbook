# EXERCISE 12 : Distance between two points on earth
import math

RADIUS = 6371.01
t1 = float(input('Enter the latitude of the first point in degrees: '))
g1 = float(input('Enter the longitude of the first point in degrees: '))
t2 = float(input('Enter the latitude of the second point in degrees: '))
g2 = float(input('Enter the longitude of the first point in degrees: '))

t1 = math.radians(t1)
g1 = math.radians(g1)
t2 = math.radians(t2)
g2 = math.radians(g2)

arccos = math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
distance = RADIUS * arccos

print('The distance between points is %.2f Km' % distance)