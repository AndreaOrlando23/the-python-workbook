# EXERCISE 178 : Recursive Palindrome


def isPalindrome(word):
    if len(word) <= 1:
        return True

    # The string is a palindrome only if the first and the last characters match
    # and the rest of the string is a palindrome
    return word[0] == word[len(word) - 1] and isPalindrome(word[1: len(word) - 1])


def main():
    word = input("Enter a word: ")

    if isPalindrome(word):
        print(f"{word} was a palindrome!")
    else:
        print(f"{word} is not a palindrome")


main()