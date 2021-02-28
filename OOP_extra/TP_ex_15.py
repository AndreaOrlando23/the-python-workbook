from TP_chap_15 import Point, Rectangle, distance_between


class Circle:
    """Represent a circle

    attributes center, radius.
    """


def point_in_circle(point, circle):

    d = distance_between(point, circle.center)
    print(d)
    return d <= circle.radius


def main():

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle()
    circle.center = Point()
    circle.center.x = 150
    circle.center.y = 100
    circle.radius = 75

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))


if __name__ == '__main__':
    main()
