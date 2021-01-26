# EXERCISE 76 : Multiple world palindromes

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input("Enter a string: ")
no_punctuation = ""

for ch in my_str:
    if ch not in punctuations:
        no_punctuation += ch.strip()

print(no_punctuation[::-1])
