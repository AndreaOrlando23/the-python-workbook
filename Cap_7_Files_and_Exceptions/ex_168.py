# EXERCISE 168 : Repeated words

import sys

WORDS_FILE = "words.txt"

if len(sys.argv) != 2:
    print("One command line argument must be provided.")
    print("Quitting...")
    quit()


try:
    with open(sys.argv[1], "r") as file:
        dict_words = dict()
        for n, line in enumerate(file, 1):
            words = line.split()
            for word in words:
                if word in dict_words:
                    locations = dict_words[word]
                    print("Line {} | Word -{}-  is repeated".format(str(locations)[1:-1], word))
                    locations.append(n)
                else:
                    dict_words[word] = [n + 1]

except IOError:
    print("File opening error, please try again.")