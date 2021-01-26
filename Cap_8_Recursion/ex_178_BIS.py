# EXERCISE 178 : Recursive Palindrome


def is_palindrome(word):
    if len(word) <= 1:
        return True

    if word[0] == word[-1] and is_palindrome(word[1:-1]):
        return True


def main():
    word = input("Enter a word: ")

    if is_palindrome(word):
        print(f"{word} was a palindrome!")
    else:
        print(f"{word} is not a palindrome")


main()