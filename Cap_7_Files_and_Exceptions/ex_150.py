# EXERCISE 150 : Display the tail of a file

import sys


if len(sys.argv) != 2:
    print("Provide the file name as a command line argument")
    quit()


try:
    inf = open(sys.argv[1], "r")

    words = []
    for word in inf:
        line = word.strip()
        words.append(line)

    inf.close()

    # Read the last 10 words of a file provided
    print(words[-10:])

except FileNotFoundError:
    print("The file does not exist")
