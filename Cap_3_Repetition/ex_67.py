# EXERCISE 67 : Compute the perimeter of a Polygon
from math import sqrt

"""
class Color:
    BOLD = '\033[1m'
"""

# Store the perimeter of Polygon
perimeter = 0

first_x = input("Enter the first x-coordinate (blank to quit): ")
if first_x == "":
    print("Quitting the program ... ")
    quit()

first_y = input("Enter the first y-coordinate: ")

# Provide initial values for prev_x and prev_y
prev_x = float(first_x)
prev_y = float(first_y)

# Read remaining coordinates
line = input("Enter the next x-coordinate (blank to quit): ")
if line == "":
    print(f"Only 2 coordinates are entered. The distance between them is: {prev_x + prev_y}")
    print("Quitting the program ... ")
    quit()

while line != "":
    # Convert the x-coordinate to a number and read the y coordinate
    x = float(line)
    y = float(input("Enter the first y-coordinate: "))

    # Compute the distance to the previous point and add it to the perimeter
    dist = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)  # Distance between 2 points is computed by Pythagorean theorem
    perimeter += dist

    # Set up prev_x and prev_y for the next loop iteration
    prev_x = x
    prev_y = y

    line = input("Enter the next x-coordinate (blank to quit): ")

# Compute the distance from the last point to the first point and add it to the perimeter
dist = sqrt((float(first_x) - x) ** 2 + (float(first_y) - y) ** 2)
perimeter += dist

# print(Color.BOLD + "The perimeter of that polygon is", perimeter)
print("The perimeter of that polygon is", perimeter)  # whitout bold class
