# EXERCISE 154 : Letter Frequencies

import sys
from operator import itemgetter

if len(sys.argv) == 1:
    print("You must provide at least on file name")
    quit()


try:
    letters = {}
    with open(sys.argv[1], "r") as file:
        for words in file:
            words = words.replace("\n", "").lower()
            for letter in words:
                letters[letter] = letters.get(letter, 0) + 1

        print(sorted(letters.items(), key=itemgetter(1), reverse=True))

except IOError:
    print("Errors while accessing the file.")
