# EXERCISE 149 : Display the head of a file
import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print("Provide the file name as a command line argument.")
    quit()


try:
    inf = open(sys.argv[1], "r")

    line = inf.readline()

    count = 0
    while count < NUM_LINES and line != "":
        line = line.strip()
        count += 1

        print(line)

        line = inf.readline()

    inf.close()

