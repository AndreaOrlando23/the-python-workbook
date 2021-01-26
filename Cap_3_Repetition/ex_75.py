# EXERCISE 75 : Is a string a palindrome? - SOLUTION 1

word = input("Enter a word: ").lower()
index = 0

while index < len(word):
    if word[index] != word[len(word) - index - 1]:
        print("Is not a palindrome")
        break
    index += 1
    print("Is a palindrome")
    break
