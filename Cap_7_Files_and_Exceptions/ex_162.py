# EXERCISE 162 : A book with no E

from string import digits, punctuation
from operator import itemgetter

# f_name used: In-to-the-frozen-south.txt
f_name = input("Please enter the file name: ")
letters = {}

with open(f_name, "r") as file:
    for line in file:

        for word in line.split():
            word = word.replace(" ", "").lower()
            word = word.translate(str.maketrans("", "", punctuation))
            word = word.translate(str.maketrans("", "", digits))

            for letter in word:
                letters[letter] = letters.get(letter, 0) + 1


print(sorted(letters.items(), key=itemgetter(1), reverse=True))

