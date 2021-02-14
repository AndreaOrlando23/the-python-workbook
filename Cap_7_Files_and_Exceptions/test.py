"""
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

word = input("Enter a word: ")

found = False
for letter in word:
    if letter in vowels:
        found = True
        print(letter)
if not found:
    print(f"There is no vowels in {word}")
"""

test = ['e', 'i', 'o', 'u', 'a', 'y']
test2 = ['a', 'e', 'i', 'o', 'u', 'y']


print(sorted(test) == test2)