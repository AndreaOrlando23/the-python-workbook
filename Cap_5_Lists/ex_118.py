# Word by Word Palindromes

from ex_117 import contractions
"""
The function `contraction` take a string as its only parameters
and returns a list of strings without spaces and punctuations
"""


def is_palindrome(s):
    new_s = contractions(s)
    """
    Traverse the new_s towards and backwards
    check if new_s is a word by word palindrome
    """
    if new_s[::1] == new_s[::-1]:
        return True
    return False


def main():
    line = input("Enter your sentence: ").lower()
    if is_palindrome(line):
        print("Yes, is a palindrome!")
    else:
        print("No, is not a palindrome!")


main()