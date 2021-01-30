# EXERCISE 151 : Concatenate multiple files

import sys

if len(sys.argv) == 1:
    print("You must provide at least one file name")
    quit()


for i in range(1, len(sys.argv)):
    fname = sys.argv[i]

    try:
        inf = open(fname, "r")

        for line in inf:
            print(line)

        inf.close()

    except:
        print("Couldn't open/display", fname)

