# EXERCISE 38 : Name That Shape

nsides = int(input('Enter the number of sides: '))

name = ""
if nsides == 3:
    name = "Triangle"
elif nsides == 4:
    name = "Quadrilateral"
elif nsides == 5:
    name = "Pentagon"
elif nsides == 6:
    name = "Hexagon"
elif nsides == 7:
    name = "Heptagon"
elif nsides == 8:
    name = "Octagon"
elif nsides == 9:
    name = "Nonagon"
elif nsides == 10:
    name = "Decagon"

if name == "":
    print('ERROR: That number of sides is not supported. Enter a value grater than 2 and less than 11.')
else:
    print(f'That is a {name}')
