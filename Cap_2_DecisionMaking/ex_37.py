# EXERCISE 37 : Vowel or consonant

VOWELS = 'aeiouy'
letter = input('Choose a letter from the alphabet: ')

if letter == 'y':
    print(f'Sometimes {letter} is a vowel... Sometimes is a consonant')
elif letter in VOWELS:
    print(f'The entered letter {letter} is a vowel')
else:
    print(f'The entered letter {letter} is a consonant')
