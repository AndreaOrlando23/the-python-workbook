# EXERCISE 149 : Display the head of a file TRIS

import sys

NUM_LINES = 10

# Verify that exactly one command line argument (in addition to the .py file) was supplied
if len(sys.argv) != 2:
    print("Provide the file name as a command line argument.")
    quit()


try:
    # Open the file for reading
    inf = open(sys.argv[1], "r")

    # Keep looping until we have either read and displayed 10 lines or we have reached the end of the file
    count = 0
    for num, word in enumerate(inf):
        line = word.strip()
        print(num + 1, line)
        count += 1
        if count == 10:
            quit()

    inf.close()

# Display an error message and quit if the file was not opened successfully
except IOError:
    print("An error occurred while accessing the file.")