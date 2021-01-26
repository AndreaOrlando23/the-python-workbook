# EXERCISE 75 : Is a string a palindrome? - SOLUTION 2

word = input("Enter a word: ").lower()

if word[::1] == word[::-1]:
    print("Is a palindrome")
else:
    print("Is not a palindrome")
