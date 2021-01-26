# Pig Latin Improved

# TODO

PUNCTUATION = [",", ".", "?", "!", "-", ":", ";"]
VOWEL = ['a', 'e', 'i', 'o', 'u']

word = input("Enter your word: ")
pig_latin = ""
store_chr = ""
index = 0

for letter in word:
    if letter[index] in VOWEL:
        pig_latin = word + "ay"

    if letter[index] not in VOWEL:
        store_chr += letter
        index += 1
        pig_latin = word[index:] + store_chr + "way"

    print(pig_latin)


