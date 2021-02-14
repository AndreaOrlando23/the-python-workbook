# EXERCISE 170 : Missing comment

from sys import argv

if len(argv) == 1:
    print("One command line argument must be provided.")
    print("Quitting...")
    quit()

for file_name in argv[1: len(argv)]:
    try:
        with open(file_name, "r") as file:
            previous = " "
            line_numb = 1
            for line in file:
                if line.startswith("def ") and previous[0] != "#":
                    bracket_pos = line.index("(")
                    name = line[4: bracket_pos]
                    print("%s line %d: %s" % (file_name, line_numb, name))
                previous = line
                line_numb += 1

    except IOError:
        print("A problem was encountered with file ’%s’." % file_name)
