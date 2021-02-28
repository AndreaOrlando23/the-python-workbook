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


class Rectangle:
    """Represents a rectangle

    attributes: width, height, corner.
    """


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
# go to the object box refers to and select the attribute named corner,
# than go to that object and select the attributes named x and y
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


# center = find_center(box)
# print_point(center)


def grow_rectangle(rect, d_width, d_height):
    rect.width += d_width
    rect.height += d_height


print(box.width, box.height)
grow_rectangle(box, 50, 100)
print(box.width, box.height)


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


print(box.corner.x, box.corner.y)
move_rectangle(box, 10, 10)
print(box.corner.x, box.corner.y)

center = find_center(box)
print_point(center)
