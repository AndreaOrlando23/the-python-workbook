# EXERCISE 161 : What's that element again?

inf = input("Enter the name of the file: ")

try:
    open(inf, "r")

except IOError:
    print("File not found")
    quit()


protons = {}
symbols = {}
elements = {}


for line in inf:
    line = line.strip()
    el_info = line.split(',')

    protons[el_info[0]] = (el_info[1], el_info[2])
    symbols[el_info[1]] = (el_info[0], el_info[2])
    elements[el_info[2]] = (el_info[0], el_info[1])


inf.close()


# TODO
