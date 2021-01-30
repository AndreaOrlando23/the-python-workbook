# EXERCISE 150 : Display the tail of a file

import sys

if len(sys.argv) != 2:
    print("Provide the file name as a command line argument")
    quit()


try:

    inf = open(sys.argv[1], "r")
    lines = inf.readlines()
    last_lines = lines[-10:]

    print(last_lines)

    inf.close()

except FileNotFoundError:
    print("The file does not exist")