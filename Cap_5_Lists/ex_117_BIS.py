# EXERCISE 117 : Only the Words BIS

import re
from string import punctuation


def only_words(word):
    # word = word.replace(" ", "")
    # word = word.translate(str.maketrans("", "", punctuation))
    word = re.split('[:;!?.,]', word)
    return word


def main():
    user_input = input("Enter the text: ")
    print(only_words(user_input))


if __name__ == '__main__':
    main()
