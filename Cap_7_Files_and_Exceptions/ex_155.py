# EXERCISE 155 : Words that occur most

from string import digits, punctuation
from operator import itemgetter

f_name = input("Please enter the file name: ")
words = {}


with open(f_name, "r") as file:
    for line in file:
        for word in line.split():
            word = word.replace(" ", "").lower()
            word = word.translate(str.maketrans("", "", punctuation))
            word = word.translate(str.maketrans("", "", digits))

            words[word] = words.get(word, 0) + 1

    print(sorted(words.items(), key=itemgetter(1), reverse=True))




