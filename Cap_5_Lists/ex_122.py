# Pig Latin

VOWEL = ['a', 'e', 'i', 'o', 'u']

word = input("Enter your word: ").lower()

first_char = word[0]
second_char = word[1]

if first_char in VOWEL:
    pig_latin = word + "way"
    print(pig_latin)

if first_char not in VOWEL:
    pig_latin = word[1:] + first_char + "ay"
    if second_char not in VOWEL:
        pig_latin = word[2:] + first_char + second_char + "ay"

    print(pig_latin)

