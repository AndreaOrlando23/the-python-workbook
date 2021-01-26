# EXERCISE 144 : Anagrams Again
punctuations = [",", ".", "?", "!", "-", ":", ";"]


def histogram(s):
    d = dict()
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


def check_dictionary(dict_1, dict_2):
    d1 = histogram(dict_1.replace(" ", ""))
    d2 = histogram(dict_2.replace(" ", ""))

    if d1 == d2:
        return True


def main():
    word_1 = input("Enter first word: ")
    word_2 = input("Enter second word: ")

    string_1 = ""
    string_2 = ""

    for char in word_1, word_2:
        if char in punctuations:
            string_1 = word_1.replace(char, "")
            string_2 = word_2.replace(char, "")

    if check_dictionary(string_1, string_2):
        print("Those words are anagrams")


main()