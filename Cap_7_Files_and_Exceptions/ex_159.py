# EXERCISE 159 : Two word random password

from random import randrange

words = []
inf = open("words.txt", "r")

for word in inf:
    line = word.strip()

    if 3 <= len(line) <= 7:
        words.append(line)

inf.close()

first_word = words[randrange(0, len(words))]
first_word = first_word.capitalize()

pw = first_word

while len(pw) < 8 or len(pw) > 10:
    second_word = words[randrange(0, len(words))]
    second_word = second_word.capitalize()
    pw = first_word + second_word


print(pw)
