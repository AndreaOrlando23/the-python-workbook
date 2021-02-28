from math import sqrt

class Point:
    """Represent a point in 2-D space."""


blank = Point()

blank.x = 3.0
blank.y = 4.0


def print_point(p):
    print('{}, {}'.format(p.x, p.y))


def distance_between(p):
    distance = sqrt(p.x ** 2 + p.y ** 2)
    print(distance)


distance_between(blank)
