# EXERCISE 143 : Anagrams


def histogram(s):
    d = dict()
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


def check_dictionary(dict_1, dict_2):
    d1 = histogram(dict_1)
    d2 = histogram(dict_2)
    if d1 == d2:
        return True


def main():
    word_1 = input("Enter first word: ")
    word_2 = input("Enter second word: ")

    if check_dictionary(word_1, word_2):
        print("Those words are anagrams")


main()