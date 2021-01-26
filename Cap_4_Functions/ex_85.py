# EXERCISE 85 : Compute the Hypotenuse
from math import sqrt


def hypotenuse(a, b):
    c = sqrt(a**2 + b**2)
    return c


def main():
    side1 = int(input("Enter the first shorter side of the triangle: "))
    side2 = int(input("Enter the second shorter side of the triangle: "))

    if side1 <= 0 or side2 <= 0:
        print("ERROR: the value is not correct")
        quit()

    result = hypotenuse(side1, side2)
    print(f"The value of the hypotenuse is: {result}")


main()
