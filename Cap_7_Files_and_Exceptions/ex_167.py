# EXERCISE 167 : Spell checker

# from Cap_5_Lists.ex_117_BIS import only_words
import sys

WORDS_FILE = "words.txt"

if len(sys.argv) != 2:
    print("One command line argument must be provided.")
    print("Quitting...")
    quit()

try:
    inf = open(sys.argv[1], "r")
except IOError:
    print("Failed to open '%s' for reading." % sys.argv[1])
    print("Quitting...")
    quit()

valid = dict()
words_file = open(WORDS_FILE, "r")

for word in words_file:
    word = word.lower().rstrip()
    valid[word] = 0

words_file.close()


misspelled = []
for line in inf:
    words = only_words(line)
    for word in words:
        if word.lower() not in valid or word not in misspelled:
            misspelled.append(word)

inf.close()

if len(misspelled) == 0:
    print("No words were mispelled.")
else:
    print("The following words are misspelled:")
    for word in misspelled:
        print(" ", word)

